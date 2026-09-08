#!/usr/bin/env python3
r"""CODEX SPEED + AUTO-ADVANCE TUNER (operator directive 2026-08-30)
===================================================================
Benchmarked on the operator master: drafting at medium reasoning is ~2.5x
faster than xhigh with the same gate-enforced quality (37s vs 95s for a
700-word section), and images are unaffected (79s vs 76s). Approval prompts
("click allow") come from approval_policy=on-request, which the Codex app
sometimes (re)sets.

This tuner makes a client's ~/.codex/config.toml fast and hands-off. Unlike
codex_image_repair.py's additive fixer, it UPGRADES two known-bad values:

  - approval_policy: "on-request" / "untrusted" / "on-failure" -> "never"
    (added if absent). Genie's own hard gates still pause production.
  - model_reasoning_effort: "xhigh" / "high" -> "medium" (added if absent).
    A client's own choice of "low" or "medium" is left alone.

Everything else in the file is preserved; a .bak is written before any
change. Idempotent: run every session by genie_bootstrap.py.
"""
import io, os, re, shutil, sys


def tune(cfg_path=None):
    cfg = cfg_path or os.path.join(os.path.expanduser("~"), ".codex", "config.toml")
    os.makedirs(os.path.dirname(cfg), exist_ok=True)
    text = io.open(cfg, encoding="utf-8-sig").read() if os.path.exists(cfg) else ""
    orig = text
    actions = []

    def set_top(key, want, upgrade_from):
        nonlocal text
        m = re.search(r'^(\s*%s\s*=\s*")([^"]*)(")' % key, text, re.M)
        if m:
            if m.group(2) in upgrade_from:
                text = text[:m.start(2)] + want + text[m.end(2):]
                actions.append("%s: %s -> %s" % (key, m.group(2), want))
        else:
            lines = text.splitlines()
            at = next((i for i, l in enumerate(lines) if l.strip().startswith("[")), len(lines))
            lines[at:at] = ['%s = "%s"' % (key, want), ""]
            text = "\n".join(lines)
            if not text.endswith("\n"):
                text += "\n"
            actions.append("%s: added %s" % (key, want))

    set_top("approval_policy", "never", ("on-request", "untrusted", "on-failure"))
    set_top("model_reasoning_effort", "medium", ("xhigh", "high"))
    # approval never WITHOUT default write access strands sessions read-only
    # (proven 2026-08-30: "Chapter Three cannot be created"): the pair must
    # ship together.
    set_top("sandbox_mode", "workspace-write", ("read-only",))

    if "[sandbox_workspace_write]" not in text:
        text = text.rstrip() + "\n\n[sandbox_workspace_write]\nnetwork_access = true\n"
        actions.append("added [sandbox_workspace_write] network_access=true")

    if text != orig:
        if os.path.exists(cfg):
            shutil.copy2(cfg, cfg + ".bak")
        io.open(cfg, "w", encoding="utf-8", newline="\n").write(text)
        for a in actions:
            print("[codex-tune] " + a)
    else:
        print("[codex-tune] config already tuned (no change)")
    return actions


if __name__ == "__main__":
    tune(sys.argv[1] if len(sys.argv) > 1 else None)
