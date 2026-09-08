#!/usr/bin/env python3
"""
CODEX IMAGE AUTO-REPAIR - uapf-image-engines
============================================
Clients who pick Codex for images sometimes hit a dead engine: the CLI is
missing, not logged in, or codex exec cannot run. This tool diagnoses and
AUTO-REPAIRS what a machine can fix, so the book never waits on a broken
engine and never ships imageless.

  python codex_image_repair.py --check            # diagnose only (exit 0 healthy / 2 broken)
  python codex_image_repair.py --repair           # diagnose + fix what is fixable
  python codex_image_repair.py --repair --smoke   # also run a tiny real generation test

Repairs performed automatically:
  - Codex CLI missing  -> npm install -g @openai/codex (Node installed first via
    winget if npm itself is missing).
  - Login missing      -> prints the exact one-time step (codex login) and, in an
    interactive session, offers to launch it. Login itself is the client's action
    (account credentials are never handled by Genie).
If the engine is still broken after repair, the caller falls back to
FLUX.1-schnell for THIS book (recorded in the choice), so production continues
immediately; codex can be re-picked once healthy.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile

def _run(cmd, timeout=120):
    try:
        if os.name == "nt":
            # .CMD shims (codex, npm) need a shell on Windows; utf-8 with
            # replacement so codex's log stream never crashes the reader.
            p = subprocess.run(subprocess.list2cmdline(cmd), capture_output=True,
                               text=True, timeout=timeout, shell=True,
                               encoding="utf-8", errors="replace")
        else:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                               encoding="utf-8", errors="replace")
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except FileNotFoundError:
        return 127, "not found"
    except subprocess.TimeoutExpired:
        return 124, "timeout"

def find_codex():
    """Resolve the codex executable even when the npm global dir is not on this
    session's PATH (the root cause of 'codex not found' on machines where codex
    IS installed)."""
    cli = shutil.which("codex")
    if cli:
        return cli
    if os.name == "nt":
        appdata = os.environ.get("APPDATA") or os.path.expanduser(r"~\AppData\Roaming")
        for ext in (".CMD", ".cmd", ".exe", ".ps1"):
            cand = os.path.join(appdata, "npm", "codex" + ext)
            if os.path.exists(cand):
                return cand
    else:
        for cand in ("/usr/local/bin/codex", os.path.expanduser("~/.npm-global/bin/codex")):
            if os.path.exists(cand):
                return cand
    return None

def clear_stuck_codex(max_min=4, dry=False):
    """Kill codex processes older than max_min minutes. A `codex exec` image job
    that has run that long has hung: it produces nothing AND jams every
    subsequent codex exec (they contend for the shared local runtime). Real
    image generation never exceeds ~3 minutes, so a codex older than 4 min is
    stuck. Returns the PIDs cleared. Run this BEFORE a codex image batch so one
    orphan from a killed prior run cannot stall the whole job (root cause of the
    2026-08-22 9-minute hang)."""
    killed = []
    if os.name == "nt":
        ps = ("Get-CimInstance Win32_Process -Filter \"Name='codex.exe'\" | "
              "ForEach-Object { $s=[Management.ManagementDateTimeConverter]::ToDateTime($_.CreationDate); "
              "if ((New-TimeSpan $s (Get-Date)).TotalMinutes -gt %d) { $_.ProcessId } }" % max_min)
        rc, out = _run(["powershell", "-NoProfile", "-NonInteractive", "-Command", ps], timeout=30)
        for line in out.splitlines():
            pid = line.strip()
            if pid.isdigit():
                killed.append(pid)
                if not dry:
                    _run(["taskkill", "/T", "/F", "/PID", pid], timeout=15)
    else:
        rc, out = _run(["bash", "-c",
                        "ps -eo pid,etimes,comm | awk '$3==\"codex\" && $2>%d {print $1}'" % (max_min*60)], timeout=30)
        for line in out.splitlines():
            pid = line.strip()
            if pid.isdigit():
                killed.append(pid)
                if not dry:
                    _run(["kill", "-9", pid], timeout=10)
    return killed

def check(smoke=False):
    """Returns (healthy: bool, findings: list[str])."""
    findings = []
    cli = find_codex()
    if not cli:
        findings.append("CLI_MISSING: the Codex CLI is not installed")
        return False, findings
    findings.append(f"cli: {cli}")
    rc, out = _run([cli, "login", "status"], timeout=60)
    logged = rc == 0 and ("logged in" in out.lower() or "signed in" in out.lower() or "authenticated" in out.lower())
    if not logged and rc == 0 and out.strip() and "not" not in out.lower():
        logged = True  # some versions print the account line only
    if not logged:
        findings.append("NOT_LOGGED_IN: codex login has not been completed on this machine")
        return False, findings
    findings.append("login: OK")
    if smoke:
        with tempfile.TemporaryDirectory() as td:
            prompt = ("Generate one small test image of a red circle on white, "
                      "save it as test.png in the current directory, then stop.")
            rc, out = _run([find_codex() or "codex", "exec",
                            "-c", 'model_reasoning_effort="low"',  # image calls run at reduced reasoning for speed
                            "--sandbox", "workspace-write",
                            "--skip-git-repo-check", "--cd", td, prompt],
                           timeout=420)
            made = any(f.lower().endswith(".png") for f in os.listdir(td)) if os.path.isdir(td) else False
            if not made:
                findings.append("SMOKE_FAIL: codex exec ran but produced no image "
                                f"(rc={rc}); output tail: {out[-200:]}")
                return False, findings
            findings.append("smoke: OK (test image generated)")
    return True, findings

def genie_root():
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "CLAUDE.md")) or os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    return os.path.expanduser("~/Genie")

def ensure_codex_config():
    """Pipeline-guide Step 1, automated ADDITIVELY: ensure ~/.codex/config.toml
    has sandbox_mode=workspace-write, approval_policy=never, network_access=true,
    and writable_roots including the Genie folder. Existing settings are never
    duplicated or overwritten; a .bak is written before any change; forward
    slashes only (backslashes break this file)."""
    import re as _re
    actions = []
    cdir = os.path.join(os.path.expanduser("~"), ".codex")
    cfg = os.path.join(cdir, "config.toml")
    os.makedirs(cdir, exist_ok=True)
    text = open(cfg, encoding="utf-8-sig").read() if os.path.exists(cfg) else ""
    orig = text
    root = genie_root().replace(chr(92), "/")

    top_add = []
    if "sandbox_mode" not in text:
        top_add.append('sandbox_mode = "workspace-write"')
    if "approval_policy" not in text:
        top_add.append('approval_policy = "never"')
    if top_add:
        lines = text.splitlines()
        insert_at = next((i for i, l in enumerate(lines) if l.strip().startswith("[")), len(lines))
        lines[insert_at:insert_at] = top_add + [""]
        text = chr(10).join(lines)
        if not text.endswith(chr(10)):
            text += chr(10)
        actions.append("config.toml: added " + ", ".join(x.split(" =")[0] for x in top_add))
    NL = chr(10)
    if "[sandbox_workspace_write]" not in text:
        text = text.rstrip() + (NL + NL + "[sandbox_workspace_write]" + NL +
                                "network_access = true" + NL +
                                'writable_roots = ["' + root + '"]' + NL)
        actions.append("config.toml: added [sandbox_workspace_write] (network_access=true, "
                       "writable_roots incl. the Genie folder)")
    else:
        after = text.split("[sandbox_workspace_write]", 1)[1]
        _m = _re.search("\\n\\[[A-Za-z_]", after)
        sec_head = after[:_m.start()] if _m else after
        if "network_access" not in sec_head:
            text = text.replace("[sandbox_workspace_write]",
                                "[sandbox_workspace_write]" + NL + "network_access = true", 1)
            actions.append("config.toml: added network_access=true")
        if "writable_roots" not in sec_head:
            text = text.replace("[sandbox_workspace_write]",
                                "[sandbox_workspace_write]" + NL +
                                'writable_roots = ["' + root + '"]', 1)
            actions.append("config.toml: added writable_roots incl. the Genie folder")
        elif root.lower() not in sec_head.lower():
            m = _re.search(r"(writable_roots\s*=\s*\[)([^\]]*)(\])", text)
            if m:
                inner = m.group(2).strip()
                text = (text[:m.start()] + m.group(1) + (inner + ", " if inner else "")
                        + '"' + root + '"' + m.group(3) + text[m.end():])
                actions.append("config.toml: appended the Genie folder to writable_roots")
    if text != orig:
        if orig:
            open(cfg + ".bak", "w", encoding="utf-8").write(orig)
        open(cfg, "w", encoding="utf-8").write(text)
        actions.append("config.toml saved (.bak kept); restart Claude Code/Codex to load it")
    return actions

def repair():
    """Fix what is fixable. Returns list of actions taken."""
    actions = []
    stuck = clear_stuck_codex()
    if stuck:
        actions.append(f"cleared {len(stuck)} stuck codex process(es) that would jam generation")
    actions += ensure_codex_config()
    if not find_codex():
        if not shutil.which("npm"):
            # Node first (winget on Windows; brew handled by genie_environment on mac)
            if shutil.which("winget"):
                rc, out = _run(["winget", "install", "-e", "--id", "OpenJS.NodeJS.LTS",
                                "--accept-source-agreements", "--accept-package-agreements"], timeout=900)
                actions.append(f"installed Node.js LTS via winget (rc={rc})")
            else:
                actions.append("BLOCKED: npm missing and winget unavailable; install Node.js manually")
                return actions
        rc, out = _run(["npm", "install", "-g", "@openai/codex"], timeout=900)
        actions.append(f"installed Codex CLI via npm (rc={rc})")
        if not find_codex():
            actions.append("BLOCKED: Codex CLI still not on PATH after install (new terminal may be needed)")
            return actions
    cli = find_codex()
    rc, out = _run([cli or "codex", "login", "status"], timeout=60)
    if rc != 0 or "not" in out.lower():
        actions.append("LOGIN_NEEDED: run `codex login` once in a terminal and finish in the browser; "
                       "Genie never enters account credentials")
    return actions

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--repair", action="store_true")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--clear-stuck", dest="clear_stuck", action="store_true",
                    help="kill codex processes older than 4 min (stuck image jobs that jam the runtime)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.clear_stuck:
        pids = clear_stuck_codex()
        print(f"cleared {len(pids)} stuck codex process(es)" + (": " + ", ".join(pids) if pids else " (none)"))
        if not (a.check or a.repair or a.smoke):
            return
    actions = []
    if a.repair:
        healthy, findings = check(smoke=False)
        if not healthy:
            actions = repair()
    healthy, findings = check(smoke=a.smoke)
    result = {"healthy": healthy, "findings": findings, "repairs": actions,
              "fallback": None if healthy else "flux"}
    if a.json:
        print(json.dumps(result, indent=1))
    else:
        print("CODEX IMAGE ENGINE:", "HEALTHY" if healthy else "BROKEN (fallback: FLUX.1-schnell)")
        for f in findings: print("  -", f)
        for x in actions: print("  repair:", x)
        if not healthy:
            print("This book's images will generate with FLUX.1-schnell so production")
            print("continues now; pick codex again once it is healthy.")
    sys.exit(0 if healthy else 2)

if __name__ == "__main__":
    main()
