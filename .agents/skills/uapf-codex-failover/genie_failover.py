#!/usr/bin/env python3
"""
GENIE FAILOVER CONTROLLER
=========================
Adds Codex as Genie's SECONDARY / FAILOVER production agent, without changing
how Genie already works. Hierarchy:

    GENIE
    ├── Claude Code  -- PRIMARY  production agent
    └── Codex        -- FAILOVER production agent

This controller EXTENDS Genie's existing per-project state model
(`project.json` + `state/` + `chapters/`, read by generate_handoff.py) with one
authoritative agent-state file, `state/agent_state.json`, so either agent can
resume from disk alone -- with no access to the other agent's chat history.

It provides:
  * shared authoritative state (state/agent_state.json), reusing project.json
  * a Codex adapter via `codex exec` (workspace-write sandbox, JSON output)
  * failure classification + a configurable auto-failover policy
  * write-ownership locking so both agents never edit the same unit at once
  * Claude -> Codex handoff and Codex -> Claude hand-back
  * an append-only audit log (state/audit_log.jsonl)
  * a health check
  * a controlled 10-unit handoff self-test (uses mock executors)

Framework is SHARED: both agents read the same framework from project.json.
There is no Claude-only or Codex-only framework.

CLI:
    python genie_failover.py health [--project DIR]
    python genie_failover.py status --project DIR
    python genie_failover.py init --project DIR [--framework NAME] [--units N]
    python genie_failover.py advance --project DIR --agent claude|codex --unit ID
    python genie_failover.py failover --project DIR [--reason TEXT] [--error TEXT]
    python genie_failover.py write-book --project DIR [--max-units N] [--stall-limit N]
    python genie_failover.py handback --project DIR
    python genie_failover.py run-codex --project DIR [--task TEXT]
    python genie_failover.py selftest
"""

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- config
DEFAULT_CONFIG = {
    "primary_agent": "claude",
    "failover_agent": "codex",
    "return_to_primary": True,
    # Automatic Codex takeover happens only for these failure classes.
    "auto_failover_on": ["USAGE_LIMIT", "RATE_LIMIT"],
    # How to locate each CLI: "auto" = detect (PATH -> WinGet package dir);
    # or an explicit absolute path to pin it.
    "executables": {"claude": "auto", "codex": "auto"},
}

FAILURE_CLASSES = [
    "USAGE_LIMIT", "RATE_LIMIT", "AUTH_ERROR", "NETWORK_ERROR",
    "TOOL_ERROR", "VALIDATION_ERROR", "UNKNOWN_ERROR",
]

AUDIT_EVENTS = {
    "CLAUDE_TASK_STARTED", "CLAUDE_TASK_COMPLETED", "CLAUDE_USAGE_LIMIT",
    "FAILOVER_STARTED", "CODEX_TASK_STARTED", "CODEX_TASK_COMPLETED",
    "CODEX_TASK_FAILED", "CLAUDE_AVAILABLE", "HAND_BACK_TO_CLAUDE",
    "FAILOVER_BLOCKED",
    "BOOK_INTAKE_STARTED", "TRADEMARK_SET", "CLASSIFICATION_RATIFIED",
    "PUBLISH_BLOCKED", "PUBLISH_ALLOWED",
    "WRITE_BOOK_STARTED", "WRITE_BOOK_FINISHED",
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- small IO
def _read_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return default


def _write_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def state_dir(project):
    return os.path.join(project, "state")


def agent_state_path(project):
    return os.path.join(state_dir(project), "agent_state.json")


def load_config(project):
    cfg = dict(DEFAULT_CONFIG)
    # repo default, then per-project override -- reuse whichever exists
    for p in (os.path.join(ROOT, "failover_config.json"),
              os.path.join(state_dir(project), "failover.config.json")):
        data = _read_json(p)
        if isinstance(data, dict):
            cfg.update({k: v for k, v in data.items() if k in DEFAULT_CONFIG})
    return cfg


# ---------------------------------------------------------------- executable locator
# Windows caveat: a shell started BEFORE the CLIs were installed will not have them on
# PATH, so shutil.which() alone is unreliable. Resolve to an absolute path via
# PATH -> config override (codex_path/claude_path in failover_config.json) -> WinGet
# package dirs. Result is cached so the failover controller always finds the executable.
_EXE_CACHE = {}
_WINGET_GLOBS = {
    "codex": ["Microsoft/WinGet/Packages/OpenAI.Codex*/codex.exe",
              "Microsoft/WinGet/Packages/OpenAI.Codex*/codex-x86_64-pc-windows-msvc.exe"],
    "claude": ["Microsoft/WinGet/Packages/Anthropic.ClaudeCode*/claude.exe"],
}


def resolve_exe(name):
    if name in _EXE_CACHE:
        return _EXE_CACHE[name]
    cfg = _read_json(os.path.join(ROOT, "failover_config.json")) or {}
    exes = cfg.get("executables") or {}
    pin = exes.get(name)
    # 1) explicit pinned path from config.executables (anything other than "auto")
    if isinstance(pin, str) and pin.strip().lower() != "auto" and os.path.exists(pin):
        _EXE_CACHE[name] = pin
        return pin
    # 2) legacy "<name>_path" override
    legacy = cfg.get(name + "_path")
    if legacy and os.path.exists(legacy):
        _EXE_CACHE[name] = legacy
        return legacy
    # 3) auto: PATH, then WinGet package dir
    found = shutil.which(name)
    if not found:
        la = os.environ.get("LOCALAPPDATA") or os.path.expanduser(r"~\AppData\Local")
        for pattern in _WINGET_GLOBS.get(name, []):
            hits = sorted(glob.glob(os.path.join(la, pattern)))
            if hits:
                found = hits[-1]
                break
    # 4) npm global dir (where `npm install -g @openai/codex` actually puts the
    #    shim on Windows). Sessions whose PATH lacks %APPDATA%\npm hit "codex
    #    not found" with codex fully installed - the root cause of client
    #    image-generation failures (operator directive 2026-08-19).
    if not found and os.name == "nt":
        appdata = os.environ.get("APPDATA") or os.path.expanduser(r"~\AppData\Roaming")
        for ext in (".CMD", ".cmd", ".exe", ".ps1", ""):
            cand = os.path.join(appdata, "npm", name + ext)
            if os.path.exists(cand):
                found = cand
                break
    if not found and os.name != "nt":
        for cand in ("/usr/local/bin/" + name, os.path.expanduser("~/.npm-global/bin/" + name),
                     os.path.expanduser("~/.nvm/current/bin/" + name)):
            if os.path.exists(cand):
                found = cand
                break
    _EXE_CACHE[name] = found
    return found


# ---------------------------------------------------------------- audit log
def audit(project, event, agent=None, detail=None):
    assert event in AUDIT_EVENTS, "unknown audit event: " + event
    os.makedirs(state_dir(project), exist_ok=True)
    line = {"ts": now_iso(), "event": event, "agent": agent, "detail": detail}
    with open(os.path.join(state_dir(project), "audit_log.jsonl"),
              "a", encoding="utf-8") as fh:
        fh.write(json.dumps(line, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- state
def project_config(project):
    """Reuse Genie's existing project.json (title/framework/niche/etc.)."""
    return _read_json(os.path.join(project, "project.json"), {}) or {}


# ---------------------------------------------------------------- niche/classification adapter
# The niche decision is made by the EXISTING uapf-phase0-router and persisted by the
# EXISTING niche skills (book_lock.md ROUTING/BOOK LOCK, or project.json). This adapter
# only READS those existing records so the locked niche/framework flows to Codex. It does
# NOT classify titles, does not re-route, and does not author any niche metadata of its own.
_OVERLAY_MAP_CACHE = {}


def router_overlay_map():
    """Overlay-code -> niche-skill map, parsed live from the EXISTING router skill's
    'NICHE SKILL INVOCATION TABLE' (uapf-phase0-router/SKILL.md). Single source of
    truth: the router file. This is a lookup of an already-made decision, not a
    classifier."""
    if _OVERLAY_MAP_CACHE:
        return _OVERLAY_MAP_CACHE
    path = os.path.join(GENIE_ROOT(), ".agents", "skills",
                        "uapf-phase0-router", "SKILL.md")
    mapping = {}
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                m = re.search(r"(OV-[A-Z0-9]+)\s*(?:->|→|=>)\s*invoke\s+(uapf-niche-[a-z0-9-]+)",
                              line, re.IGNORECASE)
                if m:
                    mapping[m.group(1).upper()] = m.group(2).lower()
    except OSError:
        pass
    _OVERLAY_MAP_CACHE.update(mapping)
    return mapping


def niche_skill_path(skill_name):
    """Absolute path to an existing niche skill's SKILL.md (the shared source of truth
    both agents read); None if it does not exist."""
    if not skill_name:
        return None
    p = os.path.join(GENIE_ROOT(), ".agents", "skills", skill_name, "SKILL.md")
    return p if os.path.exists(p) else None


def discover_framework(skill_name, framework_name=None):
    """Find a niche's integrated framework by scanning <niche>/frameworks/*/framework.json
    (self-declared in the niche folder -- NOT a central registry). If framework_name is
    given, match its id; else if exactly one framework exists, use it. Returns
    {framework_id, dir, status, components, source_of_truth} or None."""
    if not skill_name:
        return None
    base = os.path.join(GENIE_ROOT(), ".agents", "skills", skill_name, "frameworks")
    if not os.path.isdir(base):
        return None
    found = []
    for name in sorted(os.listdir(base)):
        anchor = os.path.join(base, name, "framework.json")
        meta = _read_json(anchor)
        if isinstance(meta, dict) and meta.get("framework_id"):
            meta["dir"] = os.path.join(base, name)
            found.append(meta)
    if not found:
        return None
    if framework_name:
        want = str(framework_name).strip().lower()
        for m in found:
            fid = m["framework_id"].lower()
            if fid == want or fid.startswith(want) or _slug(fid).startswith(_slug(want)):
                return m
    return found[0] if len(found) == 1 else None


def parse_book_lock(project):
    """Read the EXISTING book_lock.md production record (the real authoritative lock
    used by Genie projects) and return the locked routing decision. Returns {} when
    there is no book_lock.md. Never invents or overrides values."""
    path = os.path.join(project, "book_lock.md")
    if not os.path.exists(path):
        return {}
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return {}
    out = {}
    # HIGHEST PRIORITY: the canonical machine-readable classification line that the
    # router/niche skills now stamp into every book_lock.md (global rule 16). Format:
    #   Classification (locked, machine-readable): overlay=OV-COOK; selected_skill=uapf-niche-cookbook; framework=UAPF 1.0; classification_locked=true; framework_locked=true
    # Deterministic, no heuristics needed. key=value or key:value, separated by ; · or ,
    m = re.search(r"^.*Classification.*?:(.*)$", text, re.IGNORECASE | re.MULTILINE)
    if m and ("selected_skill" in m.group(1) or "overlay" in m.group(1)):
        for k, v in re.findall(r"(overlay|selected_skill|framework|classification_locked|"
                               r"framework_locked)\s*[=:]\s*([^;·,\n]+)", m.group(1), re.IGNORECASE):
            k = k.lower(); v = v.strip()
            if k == "overlay":
                out["overlay"] = v.upper()
            elif k == "selected_skill":
                out["selected_skill"] = v.lower()
            elif k == "framework":
                fw = re.match(r"(.*?)\s*[vV]?\s*([0-9]+(?:\.[0-9]+)*)?\s*$", v)
                out["framework"] = (fw.group(1) or v).strip()
                if fw.group(2):
                    out["framework_version"] = fw.group(2)
            elif k in ("classification_locked", "framework_locked"):
                out[k] = v.lower() in ("true", "yes", "1")
    # Overlay code (router taxonomy) -- reliable fallback if no canonical line
    if not out.get("overlay"):
        m = re.search(r"\bOV-[A-Z0-9]+\b", text)
        if m:
            out["overlay"] = m.group(0).upper()
    # Working/locked title
    m = re.search(r"^\s*[-*]?\s*(?:Working title|Locked title|Title)\s*:\s*(.+)$",
                  text, re.IGNORECASE | re.MULTILINE)
    if m:
        out["title"] = m.group(1).strip()
    else:
        m = re.search(r"^#\s+(.+?)\s+(?:—|-)\s+Production Record", text, re.MULTILINE)
        if m:
            out["title"] = m.group(1).strip()
    # Framework name + optional version (e.g. "CBF 2.0", "UAPF 1.0", "UCGF v2.7")
    # -- only if the canonical line did not already provide it.
    if not out.get("framework"):
        m = re.search(r"(?:Framework|Page-pattern family)\s*:\s*([A-Za-z][A-Za-z0-9 _]*?)"
                      r"(?:\s*[vV]?\s*([0-9]+(?:\.[0-9]+)*))?\b", text)
        if not m:
            m = re.search(r"\b([A-Z]{2,6})[ _]v?([0-9]+(?:\.[0-9]+)+)\b", text)  # header token e.g. CBF 2.0
        if m:
            out["framework"] = (m.group(1) or "").strip()
            if m.lastindex and m.group(m.lastindex) and re.match(r"[0-9]", m.group(m.lastindex) or ""):
                out["framework_version"] = m.group(m.lastindex)
    # Profile line (some niches persist a profile rather than an OV code)
    m = re.search(r"^\s*[-*]?\s*Profile\s*:\s*(.+)$", text, re.IGNORECASE | re.MULTILINE)
    if m:
        out["profile"] = m.group(1).strip()
    # Profile CODE (e.g. CB-PIC) for legacy/hand-authored records lacking an OV- code
    m = re.search(r"\bCB-[A-Z0-9]+\b", text)
    if m:
        out["profile_code"] = m.group(0).upper()
    return out


# Legacy/hand-authored profile codes -> router overlay. Grounded in the children's
# skills' own taxonomy (all CB-* are children's; CB-FACT is the facts variant). Only
# used when a record lacks an explicit OV- code; not a title classifier.
_PROFILE_TO_OVERLAY = {"CB-FACT": "OV-CFACT"}


def _profile_to_overlay(code):
    if not code:
        return None
    code = code.upper()
    if code in _PROFILE_TO_OVERLAY:
        return _PROFILE_TO_OVERLAY[code]
    if code.startswith("CB-"):        # any other children's book profile
        return "OV-CHILD"
    return None


def resolve_niche(project, book_lock=None):
    """Resolve the LOCKED niche skill for a project from its EXISTING records, without
    classifying. Order: explicit selected_skill in project.json -> overlay code in
    book_lock -> legacy profile code alias -> None (never guess). Returns
    {overlay, primary_niche, selected_skill, niche_skill_path} (values may be None)."""
    pc = project_config(project)
    bl = book_lock if book_lock is not None else parse_book_lock(project)
    overlay = (pc.get("overlay") or bl.get("overlay") or "").upper() or None
    if not overlay:                    # legacy record: derive overlay from a profile code
        overlay = _profile_to_overlay(bl.get("profile_code"))
    # Canonical selected_skill (book_lock line) or explicit project.json wins; else map overlay.
    skill = pc.get("selected_skill") or pc.get("niche_skill") or bl.get("selected_skill")
    if not skill and overlay:
        skill = router_overlay_map().get(overlay)
    primary = pc.get("primary_niche") or pc.get("niche")
    if not primary and skill and skill.startswith("uapf-niche-"):
        primary = skill[len("uapf-niche-"):]
    return {"overlay": overlay, "primary_niche": primary,
            "selected_skill": skill, "niche_skill_path": niche_skill_path(skill)}


def _apply_classification(project, st):
    """Fold the EXISTING locked routing decision (book_lock.md / project.json) into the
    shared agent-state, WITHOUT overwriting values already set explicitly. Marks the
    niche and framework as locked so Codex inherits them and never re-runs Phase 0.
    Reuses existing field names (framework/framework_version/locked_decisions) and adds
    only the minimal classification fields."""
    bl = parse_book_lock(project)
    rn = resolve_niche(project, book_lock=bl)
    if rn.get("overlay") and not st.get("overlay"):
        st["overlay"] = rn["overlay"]
    if rn.get("primary_niche") and not st.get("primary_niche"):
        st["primary_niche"] = rn["primary_niche"]
    if rn.get("selected_skill") and not st.get("selected_skill"):
        st["selected_skill"] = rn["selected_skill"]
    if rn.get("niche_skill_path") and not st.get("niche_skill_path"):
        st["niche_skill_path"] = rn["niche_skill_path"]
    if bl.get("title") and not st.get("title"):
        st["title"] = bl["title"]
    if bl.get("framework") and not st.get("framework"):
        st["framework"] = bl["framework"]
    if bl.get("framework_version") and not st.get("framework_version"):
        st["framework_version"] = bl["framework_version"]
    # Discover the niche's integrated framework folder (machine-executable projection) so
    # both agents load the SAME framework files. Self-declared in the niche folder.
    if st.get("selected_skill") and not st.get("framework_dir"):
        disc = discover_framework(st["selected_skill"], st.get("framework"))
        if disc:
            st["framework_id"] = disc["framework_id"]
            st["framework_dir"] = disc["dir"]
            st.setdefault("framework_status", disc.get("decomposition_status"))
            if not st.get("framework"):     # fall back to the framework id if none locked yet
                st["framework"] = disc["framework_id"]
    # Lock flags: true once we actually know the niche/framework from existing records
    if st.get("selected_skill") or st.get("overlay"):
        st.setdefault("classification_locked", True)
    if st.get("framework") or st.get("framework_id"):
        st.setdefault("framework_locked", True)
    return st


def stage_failover_packet(project, st=None):
    """FALLBACK (option 2) for locked-down sandboxes that cannot read outside --cd:
    stage a VERBATIM copy of the selected niche skill + the global rules into
    <project>/state/failover_packet/, plus a classification.json. This is a transient
    build artifact regenerated from the live skills at each handoff -- NOT a second,
    separately-authored framework. Not used by default (direct read is verified working).
    Returns the list of staged file paths."""
    st = st or load_state(project)
    dest = os.path.join(state_dir(project), "failover_packet")
    os.makedirs(dest, exist_ok=True)
    staged = []
    banner = ("<!-- AUTO-GENERATED verbatim copy for Codex failover. Do NOT edit; it is\n"
              "regenerated from the live skill at each handoff. Single source of truth is\n"
              "the original skill under .agents/skills/. -->\n\n")
    for name in (st.get("selected_skill"), "uapf-global-rules"):
        src = niche_skill_path(name)
        if not src:
            continue
        out = os.path.join(dest, "%s.md" % name)
        with open(src, encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(banner + body)
        staged.append(out)
    cls = {k: st.get(k) for k in ("overlay", "primary_niche", "selected_skill",
                                  "framework", "framework_version",
                                  "classification_locked", "framework_locked", "title")}
    cpath = os.path.join(dest, "classification.json")
    _write_json(cpath, cls)
    staged.append(cpath)
    return staged


def load_state(project):
    """Authoritative agent/production state. Framework comes from project.json
    so both agents share ONE framework (never duplicated per agent)."""
    st = _read_json(agent_state_path(project))
    if st is None:
        pc = project_config(project)
        st = {
            "project_id": pc.get("project_id") or os.path.basename(os.path.abspath(project)),
            "framework": pc.get("framework") or pc.get("niche") or pc.get("overlay") or "",
            "framework_version": pc.get("framework_version") or pc.get("version") or "",
            "locked_decisions": pc.get("locked_decisions") or {},
            "current_phase": pc.get("current_phase") or "production",
            "current_chapter": None,
            "current_section": None,
            "last_completed_item": None,
            "next_unfinished_item": None,
            "completed_items": [],
            "files_modified": [],
            "validation_status": "PENDING",
            "active_production_agent": load_config(project)["primary_agent"],
            "agent_available": {"claude": True, "codex": True},
            "handoff_reason": None,
            "last_valid_checkpoint": None,
        }
    # Fold in the locked niche/framework decision from the existing book_lock.md /
    # project.json so Codex inherits it and never re-runs Phase 0. Never overwrites.
    _apply_classification(project, st)
    return st


def save_state(project, st):
    _write_json(agent_state_path(project), st)


def checkpoint(project, st):
    st["last_valid_checkpoint"] = now_iso()
    save_state(project, st)
    # Keep the existing human-facing next_action.md in sync for generate_handoff.py
    if st.get("next_unfinished_item"):
        os.makedirs(state_dir(project), exist_ok=True)
        with open(os.path.join(state_dir(project), "next_action.md"),
                  "w", encoding="utf-8") as fh:
            fh.write("# Next action\n\nContinue at: **%s**\nActive agent: %s\n"
                     % (st["next_unfinished_item"], st["active_production_agent"]))
    return st


# ---------------------------------------------------------------- locking
def _lock_path(project, unit):
    return os.path.join(state_dir(project), "locks", "%s.lock" % _slug(unit))


def _slug(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", str(s))[:80]


def acquire_lock(project, unit, agent):
    """Only one agent may hold WRITE ownership of a production unit."""
    lp = _lock_path(project, unit)
    os.makedirs(os.path.dirname(lp), exist_ok=True)
    existing = _read_json(lp)
    if existing and existing.get("agent") != agent:
        return False  # held by the other agent -- do not double-write
    _write_json(lp, {"unit": str(unit), "agent": agent, "acquired_at": now_iso()})
    return True


def release_lock(project, unit, agent):
    lp = _lock_path(project, unit)
    existing = _read_json(lp)
    if existing and existing.get("agent") == agent and os.path.exists(lp):
        os.remove(lp)
        return True
    return False


# ---------------------------------------------------------------- unit completion
def advance(project, agent, unit, files=None, executor=None):
    """Mark one production unit completed by `agent`. Enforces write-ownership
    and never records a duplicate. Returns the updated state."""
    st = load_state(project)
    if st["active_production_agent"] != agent:
        raise RuntimeError("agent %r is not the active production agent (%r)"
                           % (agent, st["active_production_agent"]))
    if not acquire_lock(project, unit, agent):
        raise RuntimeError("unit %r is write-locked by the other agent" % unit)
    try:
        if executor is not None:
            executor(project, unit)  # actually produce the unit (real or mock)
        if str(unit) not in [str(u) for u in st["completed_items"]]:
            st["completed_items"].append(str(unit))
            st["last_completed_item"] = str(unit)
        for f in (files or []):
            if f not in st["files_modified"]:
                st["files_modified"].append(f)
        st["validation_status"] = "PASS"
        _recompute_next(st)
        checkpoint(project, st)
    finally:
        release_lock(project, unit, agent)
    return st


# ---------------------------------------------------------------- failure classification
def classify_error(text):
    t = (text or "").lower()
    if re.search(r"usage limit|quota exceeded|monthly limit|out of credits|plan limit", t):
        return "USAGE_LIMIT"
    if re.search(r"rate limit|too many requests|429|slow down|retry after", t):
        return "RATE_LIMIT"
    if re.search(r"unauthorized|forbidden|invalid api key|401|403|auth", t):
        return "AUTH_ERROR"
    if re.search(r"timeout|connection|network|dns|econnreset|unreachable", t):
        return "NETWORK_ERROR"
    if re.search(r"tool|mcp|command not found|no such file|exit code", t):
        return "TOOL_ERROR"
    if re.search(r"validation|gate failed|schema|invalid output", t):
        return "VALIDATION_ERROR"
    return "UNKNOWN_ERROR"


def should_auto_failover(project, failure_class):
    return failure_class in load_config(project)["auto_failover_on"]


# ---------------------------------------------------------------- Codex adapter
def codex_available():
    return resolve_exe("codex") is not None


def build_codex_prompt(project, st):
    """Everything Codex needs to continue from disk alone -- no chat history.
    Carries the LOCKED niche/framework classification so Codex never re-runs Phase 0."""
    skill = st.get("selected_skill")
    skill_path = st.get("niche_skill_path") or niche_skill_path(skill)
    global_rules = niche_skill_path("uapf-global-rules")
    reads = ["book_lock.md (the locked title, overlay, and BOOK LOCK / STYLE LOCK decisions)",
             "state/agent_state.json (authoritative agent/production state)"]
    fw_dir = st.get("framework_dir")
    if fw_dir:
        reads.insert(0, "the integrated framework folder at %s -- its machine-executable "
                        "projection (framework.json, and where present config.json, phases.md, "
                        "validation.json, and deterministic ops) that you MUST apply exactly" % fw_dir)
    if skill_path:
        reads.insert(0, "the selected niche skill at %s -- the authoritative source that defines "
                        "the architecture, expert panel, content rules, QA gates, and hard rules "
                        "you MUST follow for this niche" % skill_path)
    if global_rules:
        reads.append("the global rules at %s (catalog-wide hard rules)" % global_rules)
    read_block = "".join("  %d. %s\n" % (i + 1, r) for i, r in enumerate(reads))
    return (
        "You are Codex, Genie's FAILOVER production agent. Claude Code (the primary) "
        "is temporarily unavailable. Continue this Genie/UAPF book project from the "
        "authoritative state on disk. Do NOT regenerate any completed work.\n\n"
        "=== CLASSIFICATION IS LOCKED (do NOT change) ===\n"
        "Do NOT run Phase 0. Do NOT re-detect, re-route, or reclassify the niche. Do NOT "
        "select a different niche skill or framework. Only the operator may order "
        "reclassification. Use exactly:\n"
        "  primary_niche      : %s\n"
        "  selected_skill     : %s\n"
        "  overlay            : %s\n"
        "  framework          : %s %s\n"
        "  classification_locked: %s   framework_locked: %s\n\n"
        "Project directory : %s\n"
        "Project id        : %s\n"
        "Locked title      : %s\n"
        "Locked decisions  : %s\n"
        "Already completed (do NOT redo): %s\n"
        "Your exact next unfinished unit: %s\n"
        "  (If that says 'None', it means NO explicit unit plan exists yet - this is an "
        "intake-started book. That is NOT a reason to do nothing. Derive the unit sequence "
        "yourself from the niche skill's architecture: front matter first, then each "
        "chapter/section in the framework's order, then back matter. Compare that sequence "
        "against the completed list above and the manuscript files already on disk, and "
        "write the FIRST missing unit. Use a clear, stable unit id like 'front-matter', "
        "'chapter-01', 'appendix-a' in completed_units so the next run continues after it.)\n\n"
        "READ these authoritative files before writing (they are the SAME framework "
        "sources Claude uses -- one source of truth for both agents):\n%s\n"
        "Then produce ONLY the next unfinished unit, following that niche skill's rules "
        "and all locked decisions, save it to the project files, and update state. Treat "
        "the files above as authoritative; never guess where Claude stopped from prose. "
        "When done, print a single JSON object: {\"status\":\"completed\",\"agent\":"
        "\"codex\",\"project_id\":\"...\",\"task\":\"...\",\"completed_units\":[...],"
        "\"last_completed_unit\":\"...\",\"next_task\":\"...\",\"files_modified\":[...],"
        "\"validation_notes\":[...],\"blockers\":[]}. In validation_notes, confirm the "
        "overlay, selected_skill, and framework you actually read from the locked files "
        "(proof you did not reclassify). SPECIAL CASE - manuscript already complete: if "
        "every unit the niche skill's architecture requires (front matter, all chapters, "
        "back matter) already exists in the project files, write NOTHING NEW and return "
        "{\"status\":\"completed\",\"agent\":\"codex\",\"book_complete\":true,"
        "\"completed_units\":[],\"files_modified\":[],\"validation_notes\":"
        "[\"manuscript complete per niche architecture\"],\"blockers\":[]} instead of "
        "inventing extra units. IMPORTANT - blockers[] semantics: list something in "
        "blockers ONLY if it actually PREVENTED you from producing the unit. The "
        "trademark/publish gate blocks PUBLISHING, never manuscript production - NEVER "
        "report trademark_status or publish blocking as a blocker; put any such remark "
        "in validation_notes. If you produced the unit, blockers MUST be []."
        % (st.get("primary_niche"), skill, st.get("overlay"),
           st.get("framework"), st.get("framework_version") or "",
           st.get("classification_locked"), st.get("framework_locked"),
           os.path.abspath(project), st.get("project_id"), st.get("title"),
           json.dumps(st.get("locked_decisions") or {}),
           json.dumps(st.get("completed_items") or []),
           st.get("next_unfinished_item"), read_block)
    )


def run_codex(project, task=None, executor=None, timeout=1800, on_event=None):
    """Run Codex non-interactively (workspace-write sandbox, structured output).
    `executor` lets the self-test inject a mock without a real CLI.
    `on_event(line)` (optional): if given, Codex's JSONL event stream is read line by line
    and each raw line is handed to the callback AS IT ARRIVES, so a caller can watch Codex
    work live. Without it, the call is blocking/captured (unchanged behavior)."""
    st = load_state(project)
    prompt = task or build_codex_prompt(project, st)
    if executor is not None:
        return executor(project, prompt)
    codex = resolve_exe("codex")
    if not codex:
        return {"status": "unavailable", "agent": "codex",
                "error": "codex CLI not found on PATH, config, or WinGet package dir"}
    # Restricted workspace-write sandbox rather than unrestricted access.
    # --skip-git-repo-check: Genie project dirs are not their own git repos.
    # The prompt is fed via stdin (robust for long prompts).
    # Absolute exe path so this works even when `codex` is not on the caller's PATH.
    cmd = [codex, "exec", "--sandbox", "workspace-write",
           "--skip-git-repo-check", "--cd", os.path.abspath(project), "--json"]
    if on_event is None:
        try:
            proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                  timeout=timeout, encoding="utf-8", errors="replace")
        except FileNotFoundError:
            return {"status": "unavailable", "agent": "codex",
                    "error": "codex CLI not found on PATH"}
        except subprocess.TimeoutExpired:
            return {"status": "failed", "agent": "codex", "error": "codex exec timed out"}
        out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    else:
        # streaming mode: feed the prompt, then relay each stdout line live
        try:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True,
                                    encoding="utf-8", errors="replace", bufsize=1)
        except FileNotFoundError:
            return {"status": "unavailable", "agent": "codex",
                    "error": "codex CLI not found on PATH"}
        try:
            proc.stdin.write(prompt)
            proc.stdin.close()
        except Exception:
            pass
        lines = []
        for line in proc.stdout:
            lines.append(line)
            try:
                on_event(line)
            except Exception:
                pass
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            return {"status": "failed", "agent": "codex", "error": "codex exec timed out"}
        out = "".join(lines)
    result = _parse_codex_json(out)
    if result is None:
        return {"status": "failed", "agent": "codex",
                "error": "could not parse Codex structured output",
                "raw_tail": out[-800:]}
    return result


def _status_objs_in(s):
    """Yield every balanced-brace JSON object in `s` that parses and has a
    "status" key. A brace-depth scan (not a regex) so it survives nested objects
    and JSON embedded in surrounding prose (Codex often prints prose then JSON)."""
    depth = 0
    start = -1
    for i, ch in enumerate(s):
        if ch == "{":
            if depth == 0:
                start = i
            depth += 1
        elif ch == "}":
            if depth > 0:
                depth -= 1
                if depth == 0 and start >= 0:
                    frag = s[start:i + 1]
                    try:
                        obj = json.loads(frag)
                    except Exception:
                        obj = None
                    if isinstance(obj, dict) and "status" in obj:
                        yield obj


def _parse_codex_json(text):
    """Extract the structured result from Codex output.

    `codex exec --json` emits JSONL events; the agent's final message (our result
    JSON) is nested as an escaped string inside an `agent_message` item's `text`,
    and Codex may wrap that JSON in prose. Prefer the LAST status object found in
    the last agent_message; fall back to the last status object anywhere.
    """
    result = None
    # 1) JSONL event stream: scan each agent_message's text for an embedded status object
    for line in text.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            evt = json.loads(line)
        except Exception:
            continue
        item = evt.get("item") if isinstance(evt, dict) else None
        msg = None
        if isinstance(item, dict) and item.get("type") == "agent_message":
            msg = item.get("text")
        elif isinstance(evt, dict) and "status" in evt:
            msg = line  # plain object already
        if msg:
            for obj in _status_objs_in(msg):   # last one wins (prose + JSON tolerated)
                result = obj
    if result is not None:
        return result
    # 2) Fallback: last status object anywhere in the raw output (non --json mode)
    for obj in _status_objs_in(text):
        result = obj
    return result


def validate_codex_result(result):
    """Validate the structured Codex result before advancing authoritative state."""
    notes = []
    if not isinstance(result, dict):
        return False, ["result is not an object"]
    if result.get("status") != "completed":
        notes.append("status is %r (expected 'completed')" % result.get("status"))
    if not result.get("completed_units") and not result.get("last_completed_unit"):
        notes.append("no completed units reported")
    # Informational remarks about the publish/trademark gate are NOT production blockers
    # (the gate blocks publishing, never manuscript work). Codex is told not to put them
    # in blockers[], but tolerate it if one slips through and production still happened.
    raw = result.get("blockers") or []
    info = [b for b in raw
            if re.search(r"trademark|publish", str(b), re.I)
            and re.search(r"did not block|does not block|not block(ed)?\b", str(b), re.I)]
    blockers = [b for b in raw if b not in info]
    if info:
        notes.append("informational gate remark(s) moved out of blockers: %s" % info)
    if blockers:
        notes.append("codex reported blockers: %s" % blockers)
    ok = result.get("status") == "completed" and not blockers
    return ok, notes


# ---------------------------------------------------------------- failover / hand-back
def failover(project, reason=None, error_text=None, executor=None, units=None, task=None,
             on_event=None):
    """Claude -> Codex handoff. Claude does NOT need to initiate this; Genie does.
    `units` (optional list) lets the caller drive N units of Codex work in the
    self-test; `task` (optional) is an explicit continuation prompt for a real Codex
    exec; in production Codex determines the next unit from state via build_codex_prompt.
    `on_event` (optional): stream Codex's live events to this callback (watch mode)."""
    st = load_state(project)
    cfg = load_config(project)

    failure_class = classify_error(error_text) if error_text else (reason or "USAGE_LIMIT")
    if failure_class not in FAILURE_CLASSES:
        failure_class = "UNKNOWN_ERROR"

    audit(project, "CLAUDE_USAGE_LIMIT", "claude", failure_class)
    if error_text and not should_auto_failover(project, failure_class):
        return {"failed_over": False, "reason": failure_class,
                "note": "failure class not in auto_failover_on policy"}

    # Preflight: never hand a REAL Codex run an unresolved niche. If the existing records
    # (book_lock.md / project.json) don't yield a niche skill, refuse loudly instead of
    # letting Codex run without the locked framework. (Driven `units` self-test mode is
    # exempt -- it supplies its own units and asserts continuity, not niche resolution.)
    if units is None and not (st.get("selected_skill") or st.get("niche_skill_path")):
        audit(project, "FAILOVER_BLOCKED", "codex", "classification unresolved")
        return {"failed_over": False, "codex_ok": False,
                "reason": "CLASSIFICATION_UNRESOLVED",
                "blocker": ("No niche skill could be resolved from the project's existing "
                            "records (book_lock.md / project.json). Failover is refused so "
                            "Codex is never handed a book without its locked niche/framework. "
                            "Operator: confirm the niche (add the OV- overlay or selected_skill "
                            "to book_lock.md) and retry."),
                "resolved": resolve_niche(project)}

    # 1-4: preserve/checkpoint valid state, mark Claude unavailable, record why
    st["agent_available"]["claude"] = False
    st["handoff_reason"] = failure_class
    checkpoint(project, st)
    audit(project, "FAILOVER_STARTED", cfg["failover_agent"], failure_class)

    # 5-11: assign Codex, give it dir/framework/decisions/next unit, run it
    st["active_production_agent"] = cfg["failover_agent"]
    save_state(project, st)

    produced = []
    audit(project, "CODEX_TASK_STARTED", "codex", st.get("next_unfinished_item"))
    if units is not None:
        # self-test / driven mode: advance the given units under Codex ownership
        for u in units:
            advance(project, "codex", u,
                    files=["units/unit_%s.md" % _slug(u)],
                    executor=(executor if callable(executor) else None))
            produced.append(str(u))
        result = {"status": "completed", "agent": "codex",
                  "project_id": st.get("project_id"),
                  "completed_units": produced,
                  "last_completed_unit": produced[-1] if produced else None,
                  "files_modified": ["units/unit_%s.md" % _slug(u) for u in units],
                  "validation_notes": [], "blockers": []}
    else:
        result = run_codex(project, task=task, executor=executor, on_event=on_event)

    ok, notes = validate_codex_result(result)
    if not ok:
        audit(project, "CODEX_TASK_FAILED", "codex", notes)
        return {"failed_over": True, "codex_ok": False, "result": result, "notes": notes}

    # 12-14: validate, update shared state, keep checkpointing
    st = load_state(project)
    for u in (result.get("completed_units") or []):
        if str(u) not in [str(x) for x in st["completed_items"]]:
            st["completed_items"].append(str(u))
            st["last_completed_item"] = str(u)
    st["validation_status"] = "PASS"
    _recompute_next(st)
    checkpoint(project, st)
    audit(project, "CODEX_TASK_COMPLETED", "codex", result.get("last_completed_unit"))
    return {"failed_over": True, "codex_ok": True, "result": result,
            "active_agent": st["active_production_agent"]}


def handback(project):
    """Codex -> Claude. Called when Claude becomes available again. Codex has
    already finished its current atomic unit, saved, validated and checkpointed.
    Authoritative state wins: Claude must resume at next_unfinished_item, NOT at
    its old chat position."""
    st = load_state(project)
    cfg = load_config(project)
    if not cfg["return_to_primary"]:
        return {"handed_back": False, "note": "return_to_primary is disabled"}
    st["agent_available"]["claude"] = True
    audit(project, "CLAUDE_AVAILABLE", "claude")
    st["active_production_agent"] = cfg["primary_agent"]
    st["handoff_reason"] = None
    checkpoint(project, st)
    audit(project, "HAND_BACK_TO_CLAUDE", "claude",
          {"last_verified": st.get("last_completed_item"),
           "next": st.get("next_unfinished_item")})
    return {"handed_back": True,
            "active_agent": st["active_production_agent"],
            "last_verified_item": st.get("last_completed_item"),
            "next_item": st.get("next_unfinished_item")}


def write_book(project, max_units=40, stall_limit=2, quiet=False):
    """Autopilot: loop Codex one-unit failover runs until the manuscript is complete.
    Stops on: Codex declaring book_complete, the planned-unit list being exhausted,
    `stall_limit` consecutive runs with no new units, any Codex failure, or the
    `max_units` hard cap. NEVER publishes; the trademark gate is untouched."""
    def say(msg):
        if not quiet:
            print(msg, flush=True)

    st = load_state(project)
    if not (st.get("selected_skill") or st.get("niche_skill_path")):
        return {"book_complete": False, "stopped": "CLASSIFICATION_UNRESOLVED",
                "note": "run intake (or fix book_lock.md) first"}
    audit(project, "WRITE_BOOK_STARTED", "codex",
          {"max_units": max_units, "already_done": len(st.get("completed_items") or [])})
    say("Autopilot started for %r - up to %d units. Ctrl+C to stop safely between units."
        % (st.get("title"), max_units))

    written, stalls, stopped = [], 0, "MAX_UNITS_REACHED"
    for i in range(1, max_units + 1):
        before = set(str(x) for x in load_state(project).get("completed_items") or [])
        r = failover(project)
        if not r.get("failed_over") or not r.get("codex_ok", True):
            stopped = "CODEX_FAILED"
            say("Stopped: Codex run failed - %s" % (r.get("notes") or r.get("reason")))
            break
        result = r.get("result") or {}
        if result.get("book_complete"):
            stopped = "BOOK_COMPLETE"
            say("Codex reports the manuscript is COMPLETE.")
            break
        st = load_state(project)
        new = [u for u in (st.get("completed_items") or []) if str(u) not in before]
        if new:
            stalls = 0
            written.extend(str(u) for u in new)
            say("[run %d] completed: %s  (total done: %d)"
                % (i, ", ".join(str(u) for u in new), len(st["completed_items"])))
        else:
            stalls += 1
            say("[run %d] no new unit recorded (stall %d/%d)" % (i, stalls, stall_limit))
            if stalls >= stall_limit:
                stopped = "STALLED"
                break
        if st.get("planned_units") and st.get("next_unfinished_item") is None:
            stopped = "PLAN_EXHAUSTED"
            say("All planned units are complete.")
            break

    st = load_state(project)
    complete = stopped in ("BOOK_COMPLETE", "PLAN_EXHAUSTED")
    audit(project, "WRITE_BOOK_FINISHED", "codex",
          {"stopped": stopped, "units_written": written})
    return {"book_complete": complete, "stopped": stopped,
            "units_written_this_session": written,
            "total_completed": len(st.get("completed_items") or []),
            "trademark_status": st.get("trademark_status"),
            "next_step": ("trademark screen -> set-trademark CLEARED -> ratify -> publish-ready"
                          if complete else
                          "inspect status/audit log, then re-run write-book or failover"),
            "note": "publish stays BLOCKED until the trademark gate is CLEARED"}


# ---------------------------------------------------------------- Codex intake + trademark gate
# For a TOTAL Claude outage: Codex may START a new book on a PROVISIONAL classification and write
# content, but the title/trademark is UNVERIFIED and the book is HARD-BLOCKED from publish until an
# operator (or ChatGPT, or Claude on return) clears the trademark. Codex never does the legal screen.
TRADEMARK_STATES = ("UNVERIFIED", "CLEARED", "RISK")

# Trim size defaults by niche key (operator directive 2026-08-13). health is
# deliberately absent: it keeps its niche-skill default or the per-book choice.
TRIM_8_5_X_11 = {"textbook", "workbook", "cookbook", "childrens", "childrens-facts",
                 "activity", "crafts", "howto", "user-guide", "medical",
                 "exam-simulator", "study-guide", "reference", "language", "travel"}
TRIM_6_X_9 = {"selfhelp", "history", "poetry", "fiction", "journal", "faith",
              "business", "biography", "parenting", "sports", "humor",
              "popular-science", "public-domain"}


def trim_for_niche(niche_key):
    """Default trim size for a niche key, or None when the niche has no
    operator-directed default (never guess)."""
    if niche_key in TRIM_8_5_X_11:
        return "8.5x11"
    if niche_key in TRIM_6_X_9:
        return "6x9"
    return None


def trademark_prompt(title, marketplace="Amazon US (amazon.com)"):
    """A ready-to-paste ChatGPT prompt so the operator can run the trademark + market screen when
    Claude is unavailable, then record the verdict with `set-trademark`."""
    return (
        "Act as a KDP trademark and market risk screener. This is a PRELIMINARY risk screen, not "
        "legal clearance. For the book title below, using live web search:\n"
        "  TITLE: \"%s\"\n  MARKETPLACE: %s\n\n"
        "1) TRADEMARK: search the exact title + distinctive words on the USPTO trademark database "
        "(tmsearch.uspto.gov), plus Google, for registered/pending marks in books/publishing or "
        "related classes. Report GREEN (clear), YELLOW (caution, explain), or RED (high risk, a "
        "registered mark or famous brand) with the specific marks found.\n"
        "2) MARKET: search the exact title and close variants on %s. List the top 5-10 competing "
        "books (title, author, approx. reviews/BSR if visible), note if an identical title already "
        "exists, and give a STRONG / WEAK / SATURATED verdict with evidence.\n"
        "3) If YELLOW/RED, suggest 3-5 safer title variants that keep the seed words.\n\n"
        "End with one line exactly: VERDICT: <GREEN|YELLOW|RED> - <one-sentence reason>."
        % (title, marketplace, marketplace))


def write_provisional_book_lock(project, title, overlay, selected_skill, framework,
                                framework_version="", language="English", rationale=""):
    """Write a PROVISIONAL book_lock.md (Codex intake). Carries the canonical classification line
    plus provisional/UNVERIFIED markers so downstream tools and the publish gate know it is not
    ratified and the trademark is not cleared."""
    os.makedirs(project, exist_ok=True)
    fw = (framework + (" " + framework_version if framework_version else "")).strip()
    lines = [
        "# %s -- Production Record (PROVISIONAL / Codex intake)" % title,
        "Genie -- provisional intake by Codex while Claude was unavailable. NOT trademark-cleared.",
        "",
        "## ROUTING BLOCK",
        "- Classification (locked, machine-readable): overlay=%s; selected_skill=%s; framework=%s; "
        "classification_locked=true; framework_locked=true" % (overlay, selected_skill, fw),
        "- classification_provisional=true (Codex intake; niche chosen without the router's live "
        "market screen -- confirm on Claude return or accept explicitly)",
        "- title_status=UNVERIFIED",
        "- trademark_status=UNVERIFIED  (PRELIMINARY screen not yet run; publish is BLOCKED until CLEARED)",
        "- Rationale: %s" % (rationale or "provisional niche match from the router table"),
        "",
        "## BOOK LOCK",
        "- Working title: %s" % title,
        "- Language: %s" % language,
    ]
    niche_key = (selected_skill or "").replace("uapf-niche-", "").strip()
    trim = trim_for_niche(niche_key)
    if trim:
        pretty = "8.5 x 11 in" if trim == "8.5x11" else "6 x 9 in"
        lines.append("- Trim size: %s (operator default for niche '%s', directive 2026-08-13)"
                     % (pretty, niche_key))
    with open(os.path.join(project, "book_lock.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    st = load_state(project)
    if trim:
        st["trim"] = trim
    st["trademark_status"] = "UNVERIFIED"
    st["title_status"] = "UNVERIFIED"
    st["classification_provisional"] = True
    st["intake_by"] = "codex"
    save_state(project, st)
    audit(project, "BOOK_INTAKE_STARTED", "codex", title)
    return load_state(project)


def set_trademark(project, status, by="operator", note=""):
    """Record the trademark screen verdict (from the operator / ChatGPT / Claude)."""
    status = status.upper()
    assert status in TRADEMARK_STATES, "status must be one of %s" % (TRADEMARK_STATES,)
    st = load_state(project)
    st["trademark_status"] = status
    st["trademark_by"] = by
    st["trademark_note"] = note
    if status == "CLEARED":
        st["title_status"] = "VERIFIED"
    save_state(project, st)
    audit(project, "TRADEMARK_SET", by, "%s: %s" % (status, note))
    return {"trademark_status": status, "by": by, "note": note}


def ratify_classification(project, by="claude", note=""):
    """Claude (or the operator) confirms the provisional Codex classification is correct."""
    st = load_state(project)
    st["classification_provisional"] = False
    st["classification_ratified_by"] = by
    save_state(project, st)
    audit(project, "CLASSIFICATION_RATIFIED", by, note)
    return {"classification_provisional": False, "ratified_by": by}


def publish_ready(project):
    """Hard publish gate. Publishing is BLOCKED unless the trademark is CLEARED. A still-provisional
    classification is surfaced as a warning the operator must accept (it affects format, not legality)."""
    st = load_state(project)
    tm = st.get("trademark_status") or "UNVERIFIED"
    blockers, warnings = [], []
    if tm != "CLEARED":
        blockers.append("TRADEMARK not cleared (status=%s). Run the trademark screen "
                        "(operator/ChatGPT/Claude) and record it with `set-trademark`, or fix a RISK "
                        "title, before publishing." % tm)
    if st.get("classification_provisional"):
        warnings.append("Classification is PROVISIONAL (Codex intake). Confirm the niche is right "
                        "(ratify) or accept it explicitly before publishing.")
    allowed = not blockers
    audit(project, "PUBLISH_ALLOWED" if allowed else "PUBLISH_BLOCKED", "operator", tm)
    return {"publish_allowed": allowed, "trademark_status": tm, "blockers": blockers,
            "warnings": warnings}


def build_intake_prompt(project, title):
    """Prompt for Codex to PROVISIONALLY classify a new title (Claude is out). Codex reads the
    router table + niche skills and returns a structured classification -- it does NOT do the
    trademark/market web screen (it can't) and must mark it UNVERIFIED."""
    router = os.path.join(GENIE_ROOT(), ".agents", "skills", "uapf-phase0-router", "SKILL.md")
    return (
        "You are Codex performing a PROVISIONAL Phase-0 intake because Claude (the primary) is "
        "unavailable. Read the router skill at %s (its NICHE SKILL INVOCATION TABLE maps overlay "
        "codes to uapf-niche-* skills) and, if helpful, the candidate niche SKILL.md files under "
        ".agents/skills/. Classify this book title into the correct overlay, niche skill, and "
        "framework:\n  TITLE: \"%s\"\n\n"
        "You MUST NOT attempt trademark or market web research -- you cannot clear a title; that is "
        "done later by the operator/ChatGPT/Claude. Detect the language from the title. Then print a "
        "single JSON object and nothing else:\n"
        "{\"status\":\"completed\",\"agent\":\"codex\",\"overlay\":\"OV-XXX\",\"selected_skill\":"
        "\"uapf-niche-<x>\",\"framework\":\"<name and version if known>\",\"language\":\"<lang>\","
        "\"subtitle_suggestions\":[\"...\"],\"rationale\":\"<why this niche>\",\"blockers\":[]}"
        % (router, title))


def intake(project, title, executor=None):
    """Run a provisional Codex intake for a new book (Claude fully out). Codex classifies; the
    controller writes the provisional, trademark-UNVERIFIED book_lock deterministically."""
    os.makedirs(project, exist_ok=True)
    prompt = build_intake_prompt(project, title)
    result = run_codex(project, task=prompt, executor=executor)
    if not isinstance(result, dict) or result.get("status") != "completed" or not result.get("overlay"):
        return {"intake_ok": False, "error": "Codex did not return a classification", "raw": result}
    overlay = str(result.get("overlay", "")).upper()
    skill = result.get("selected_skill") or router_overlay_map().get(overlay)
    fw = result.get("framework", "")
    # split trailing version if present
    fwv = ""
    m = re.search(r"^(.*?)\s+([0-9]+(?:\.[0-9]+)+)\s*$", fw)
    if m:
        fw, fwv = m.group(1).strip(), m.group(2)
    st = write_provisional_book_lock(project, title, overlay, skill, fw, fwv,
                                     language=result.get("language", "English"),
                                     rationale=result.get("rationale", ""))
    return {"intake_ok": True, "classification": {"overlay": overlay, "selected_skill": skill,
            "framework": (fw + " " + fwv).strip(), "language": result.get("language")},
            "trademark_status": st.get("trademark_status"),
            "subtitle_suggestions": result.get("subtitle_suggestions", []),
            "note": "PROVISIONAL: trademark UNVERIFIED, publish BLOCKED until cleared."}


# ---------------------------------------------------------------- init / plan units
def init_project(project, framework=None, units=0, decisions=None):
    """Create/attach the shared state for a project. Reuses project.json if present."""
    os.makedirs(state_dir(project), exist_ok=True)
    pc = project_config(project)
    if framework and not pc.get("framework"):
        pc["framework"] = framework
        pc.setdefault("project_id", os.path.basename(os.path.abspath(project)))
        _write_json(os.path.join(project, "project.json"), pc)
    st = load_state(project)
    if framework:
        st["framework"] = framework
    if decisions:
        st["locked_decisions"] = decisions
    if units:
        st["planned_units"] = [str(i) for i in range(1, units + 1)]
        st["next_unfinished_item"] = "1"
    save_state(project, st)
    return st


def _recompute_next(st):
    """Advance next_unfinished_item past everything already completed, in plan order."""
    plan = st.get("planned_units") or []
    done = set(str(x) for x in st.get("completed_items", []))
    st["next_unfinished_item"] = next((u for u in plan if u not in done), None)
    return st


def set_next_from_plan(project):
    st = _recompute_next(load_state(project))
    save_state(project, st)
    return st


# ---------------------------------------------------------------- health check
def _cli_ok(name, args):
    exe = shutil.which(name)
    if not exe:
        return False
    try:
        subprocess.run([name] + args, capture_output=True, text=True, timeout=20)
        return True
    except Exception:
        return False


def health(project=None):
    claude_exe = resolve_exe("claude")
    codex_exe = resolve_exe("codex")
    claude_cli = claude_exe is not None
    codex_cli = codex_exe is not None
    mcp_json = os.path.join(GENIE_ROOT(), ".mcp.json")
    mcp_configured = False
    data = _read_json(mcp_json)
    if isinstance(data, dict):
        mcp_configured = "codex" in (data.get("mcpServers") or {})
    claude_sees_codex = False
    if claude_exe:
        try:
            # project-scoped MCP servers show when `claude mcp list` runs in the project
            out = subprocess.run([claude_exe, "mcp", "list"], capture_output=True,
                                 text=True, timeout=30, cwd=GENIE_ROOT(),
                                 encoding="utf-8", errors="replace").stdout.lower()
            claude_sees_codex = "codex" in out
        except Exception:
            claude_sees_codex = False
    state_readable = True
    framework_loadable = True
    if project:
        state_readable = os.path.exists(agent_state_path(project)) or os.path.isdir(project)
        # A project's framework is loadable if any recognised state/config marker exists:
        # project.json (current), agent_state.json (this skill), or a legacy lock file.
        framework_loadable = bool(project_config(project)) or any(
            os.path.exists(os.path.join(project, p)) for p in
            ("project.json", "book_lock.md", os.path.join("state", "agent_state.json")))
    cfg = load_config(project or ".")
    return {
        "claude_cli_available": claude_cli,
        "codex_cli_available": codex_cli,
        "codex_mcp_server_startable": codex_cli,  # `codex mcp-server` ships with the CLI
        "codex_mcp_configured_project_scope": mcp_configured,
        "claude_sees_codex_mcp": claude_sees_codex,
        "direct_codex_exec_available": codex_cli,
        "shared_state_readable": state_readable,
        "current_framework_loadable": framework_loadable,
        "failover_controller_ready": True,
        "primary_agent": cfg["primary_agent"],
        "backup_agent": cfg["failover_agent"],
        "auto_failover_on": cfg["auto_failover_on"],
        "codex_exe_path": codex_exe,
        "claude_exe_path": claude_exe,
    }


def GENIE_ROOT():
    # skill dir is <genie>/.agents/skills/uapf-codex-failover
    return os.path.abspath(os.path.join(ROOT, "..", "..", ".."))


# ---------------------------------------------------------------- self-test
def _make_unit_executor():
    """Returns an executor that writes units/unit_<id>.md when a unit is produced."""
    def _exec(project, unit):
        d = os.path.join(project, "units")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "unit_%s.md" % _slug(unit)), "w",
                  encoding="utf-8") as fh:
            fh.write("# Unit %s\n\nProduced content for unit %s.\n" % (unit, unit))
    return _exec


def selftest():
    """Controlled handoff test: Claude 1-5 -> USAGE_LIMIT -> Codex 6-8 ->
    Claude restored -> Claude 9-10. Verifies continuity both directions and
    that locked config is unchanged across the switch."""
    tmp = tempfile.mkdtemp(prefix="genie_failover_test_")
    project = os.path.join(tmp, "test-project")
    os.makedirs(project, exist_ok=True)
    # locked project config that must NOT change during the switch
    locked = {"framework": "TESTFW", "framework_version": "1.0",
              "project_id": "test-project", "trim": "8.5x11",
              "locked_decisions": {"palette": "royal-blue-gold", "trim": "8.5x11"}}
    _write_json(os.path.join(project, "project.json"), locked)
    st = init_project(project, framework="TESTFW", units=10,
                      decisions=locked["locked_decisions"])
    unit_exec = _make_unit_executor()
    config_before = json.dumps(project_config(project), sort_keys=True)

    results = {}

    # Claude does 1..5
    for u in range(1, 6):
        advance(project, "claude", u, files=["units/unit_%d.md" % u], executor=unit_exec)
        audit(project, "CLAUDE_TASK_COMPLETED", "claude", u)
    set_next_from_plan(project)  # -> 6

    # Simulate Claude usage limit -> Genie triggers failover (Claude does NOT initiate)
    fo = failover(project, error_text="Error: usage limit reached for this plan",
                  units=[6, 7, 8], executor=unit_exec)
    set_next_from_plan(project)  # -> 9
    results["claude_to_codex"] = fo.get("codex_ok", False)

    # Simulate Claude restored -> hand back
    hb = handback(project)
    results["codex_to_claude"] = hb.get("handed_back", False) and hb.get("next_item") == "9"

    # Claude does 9..10
    for u in range(9, 11):
        advance(project, "claude", u, files=["units/unit_%d.md" % u], executor=unit_exec)
        audit(project, "CLAUDE_TASK_COMPLETED", "claude", u)
    set_next_from_plan(project)

    # ---- assertions ----
    st = load_state(project)
    completed = [str(x) for x in st["completed_items"]]
    files_on_disk = sorted(int(m.group(1)) for f in os.listdir(os.path.join(project, "units"))
                           for m in [re.match(r"unit_(\d+)\.md$", f)] if m)
    expected = list(range(1, 11))
    present = files_on_disk == expected
    no_dupes = len(completed) == len(set(completed))
    order_ok = [int(x) for x in completed] == expected
    config_after = json.dumps(project_config(project), sort_keys=True)
    config_unchanged = config_before == config_after

    checks = {
        "units_present_1_10": present,
        "missing_zero": present,
        "duplicates_zero": no_dupes and len(files_on_disk) == 10,
        "correct_order": order_ok,
        "claude_to_codex_continuity": results["claude_to_codex"],
        "codex_to_claude_continuity": results["codex_to_claude"],
        "locked_config_unchanged": config_unchanged,
    }
    return {
        "project": project,
        "completed_items": completed,
        "files_on_disk": files_on_disk,
        "active_agent_final": st["active_production_agent"],
        "checks": checks,
        "all_pass": all(checks.values()),
    }


# ---------------------------------------------------------------- CLI
def _p(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main():
    ap = argparse.ArgumentParser(description="Genie Codex failover controller")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("health"); sp.add_argument("--project", default=None)
    sp = sub.add_parser("status"); sp.add_argument("--project", required=True)
    sp = sub.add_parser("init")
    sp.add_argument("--project", required=True); sp.add_argument("--framework")
    sp.add_argument("--units", type=int, default=0)
    sp = sub.add_parser("advance")
    sp.add_argument("--project", required=True)
    sp.add_argument("--agent", required=True, choices=["claude", "codex"])
    sp.add_argument("--unit", required=True)
    sp = sub.add_parser("failover")
    sp.add_argument("--project", required=True)
    sp.add_argument("--reason"); sp.add_argument("--error")
    sp = sub.add_parser("handback"); sp.add_argument("--project", required=True)
    sp = sub.add_parser("write-book")
    sp.add_argument("--project", required=True)
    sp.add_argument("--max-units", type=int, default=40)
    sp.add_argument("--stall-limit", type=int, default=2)
    sp = sub.add_parser("run-codex")
    sp.add_argument("--project", required=True); sp.add_argument("--task")
    sub.add_parser("selftest")
    # Codex intake + trademark gate (total Claude outage)
    sp = sub.add_parser("intake"); sp.add_argument("--project", required=True); sp.add_argument("--title", required=True)
    sp = sub.add_parser("trademark-prompt"); sp.add_argument("--title", required=True); sp.add_argument("--marketplace", default="Amazon US (amazon.com)")
    sp = sub.add_parser("set-trademark"); sp.add_argument("--project", required=True)
    sp.add_argument("--status", required=True, choices=["UNVERIFIED", "CLEARED", "RISK"])
    sp.add_argument("--by", default="operator"); sp.add_argument("--note", default="")
    sp = sub.add_parser("ratify"); sp.add_argument("--project", required=True); sp.add_argument("--by", default="operator")
    sp = sub.add_parser("publish-ready"); sp.add_argument("--project", required=True)

    a = ap.parse_args()
    if a.cmd == "health":
        _p(health(a.project))
    elif a.cmd == "status":
        _p(load_state(a.project))
    elif a.cmd == "init":
        _p(init_project(a.project, framework=a.framework, units=a.units))
    elif a.cmd == "advance":
        _p(advance(a.project, a.agent, a.unit, executor=_make_unit_executor()))
    elif a.cmd == "failover":
        _p(failover(a.project, reason=a.reason, error_text=a.error))
    elif a.cmd == "handback":
        _p(handback(a.project))
    elif a.cmd == "write-book":
        _p(write_book(a.project, max_units=a.max_units, stall_limit=a.stall_limit))
    elif a.cmd == "run-codex":
        _p(run_codex(a.project, task=a.task))
    elif a.cmd == "selftest":
        _p(selftest())
    elif a.cmd == "intake":
        _p(intake(a.project, a.title))
    elif a.cmd == "trademark-prompt":
        print(trademark_prompt(a.title, a.marketplace))
    elif a.cmd == "set-trademark":
        _p(set_trademark(a.project, a.status, by=a.by, note=a.note))
    elif a.cmd == "ratify":
        _p(ratify_classification(a.project, by=a.by))
    elif a.cmd == "publish-ready":
        _p(publish_ready(a.project))


if __name__ == "__main__":
    main()
