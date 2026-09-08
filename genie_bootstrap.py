#!/usr/bin/env python3
"""
GENIE FIRST-RUN BOOTSTRAP
=========================
Runs once on a new installation (operator or client) to make Genie work
perfectly out of the box, with no manual setup:

  1. DEPENDENCIES: install every Python package Genie needs (requirements.txt)
     into the active interpreter, idempotently. Already-satisfied packages are
     skipped; failures are reported, never hidden.
  2. DATABASE SEEDING: immediately begin building the two local reference
     databases the cover and A+ systems need:
       - cover_db/<niche>/            (uapf-cover-db / cover_db.py)
       - cover_db/_aplus/<niche>/     (aplus_db.py)
     The active book's niche is seeded first (so the first cover is never
     blocked); the rest fill in between production tasks per the completion
     gates in uapf-cover-db.

Idempotent: safe to run every session start. It marks completion in
state/bootstrap.json and, once dependencies are in and the active niche is
seeded, becomes a fast no-op that only reports what remains.

Usage:
  python genie_bootstrap.py                 # full first-run setup
  python genie_bootstrap.py --deps-only     # just install dependencies
  python genie_bootstrap.py --status        # report without changing anything
  python genie_bootstrap.py --active-niche <key>   # seed this niche first
"""
import argparse, json, os, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(HERE, "requirements.txt")
COVER_DB = os.path.join(HERE, ".agents", "skills", "uapf-cover-db", "cover_db.py")
APLUS_DB = os.path.join(HERE, ".agents", "skills", "uapf-cover-db", "aplus_db.py")
STATE_DIR = os.path.join(HERE, "state")
MARK = os.path.join(STATE_DIR, "bootstrap.json")

# One import name per pip package that must import cleanly after install.
IMPORT_CHECK = {
    "python-docx": "docx", "Pillow": "PIL", "reportlab": "reportlab",
    "numpy": "numpy", "PyMuPDF": "fitz",
}
NICHES = ["health", "cookbook", "textbook", "medical", "workbook", "study-guide",
          "exam-simulator", "childrens", "childrens-facts", "activity", "crafts",
          "selfhelp", "howto", "humor", "history", "fiction", "public-domain",
          "travel", "user-guide", "journal", "faith", "business", "biography",
          "parenting", "sports", "language", "poetry", "reference",
          "popular-science", "coloring", "puzzle"]
N_NICHES = len(NICHES)


def _load_mark():
    if os.path.exists(MARK):
        try:
            return json.loads(open(MARK, encoding="utf-8").read())
        except Exception:
            return {}
    return {}


def _save_mark(d):
    os.makedirs(STATE_DIR, exist_ok=True)
    open(MARK, "w", encoding="utf-8").write(json.dumps(d, indent=2))


def install_dependencies():
    """Install requirements.txt into the active interpreter. Returns True if
    all core imports resolve afterward."""
    print("  Installing Genie components — this only takes a moment...")
    if os.path.exists(REQ):
        r = subprocess.run([sys.executable, "-m", "pip", "install", "-r", REQ,
                            "--disable-pip-version-check", "--quiet"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            last_err = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "unknown error"
            print("  Note: one or more components had a setup issue.")
            print(f"  Details: {last_err}")
            print("  Genie will continue — most features should still work.")
            print("  If you see problems, contact your studio owner for help.")
    else:
        print("  Component list (requirements.txt) not found — skipping auto-install.")
    missing = []
    for pkg, mod in IMPORT_CHECK.items():
        try:
            __import__(mod)
        except Exception:
            missing.append(pkg)
    if missing:
        print()
        print("  Some components could not be installed automatically:")
        for m in missing:
            print(f"    - {m}")
        print("  Contact your studio owner and share the list above — they can fix it quickly.")
        return False
    print("  All components ready.")
    return True


def _covers_have(niche):
    d = os.path.join(HERE, "cover_db", niche)
    if not os.path.isdir(d):
        return 0
    return len([f for f in os.listdir(d)
                if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))])


def _aplus_have(niche):
    d = os.path.join(HERE, "cover_db", "_aplus", niche)
    if not os.path.isdir(d):
        return 0
    return len([f for f in os.listdir(d)
                if f.lower().endswith((".jpg", ".jpeg", ".png"))])


def seeding_status():
    cov_done = sum(1 for n in NICHES if _covers_have(n) >= 15)
    apl_done = sum(1 for n in NICHES if _aplus_have(n) >= 15)
    return cov_done, apl_done


def report_seeding(active=None):
    cov, apl = seeding_status()
    cov_pct = int(100 * cov / N_NICHES)
    apl_pct = int(100 * apl / N_NICHES)
    print(f"  Reference library: covers {cov}/{N_NICHES} categories ready ({cov_pct}%)"
          f"  |  A+ images {apl}/{N_NICHES} categories ready ({apl_pct}%)")
    # INTERIOR bank (skipped when the skill folder is absent)
    idb = os.path.join(HERE, ".agents", "skills", "uapf-interior-db", "interior_db.py")
    if os.path.exists(idb):
        print("  Interior reference library: building in the background.")
        subprocess.run([sys.executable, idb, "list"])
    cov_todo = [n for n in NICHES if _covers_have(n) < 15]
    apl_todo = [n for n in NICHES if _aplus_have(n) < 15]
    if active:
        print(f"  Active category '{active}': "
              f"covers={_covers_have(active)}, A+={_aplus_have(active)}")
    if cov_todo or apl_todo:
        print("  Library is still filling in — Genie continues building it between")
        print("  book tasks. Your books are never delayed waiting for it.")
    return cov_todo, apl_todo


def main():
    ap = argparse.ArgumentParser(description="Genie first-run bootstrap")
    ap.add_argument("--deps-only", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--active-niche")
    a = ap.parse_args()

    mark = _load_mark()
    env_script = os.path.join(HERE, "genie_environment.py")
    if a.status:
        deps_ok = mark.get("deps_installed", False)
        print()
        print("  Genie Setup Status")
        print("  " + "-"*40)
        print(f"  Components installed : {'Yes' if deps_ok else 'No — run without --status to fix'}")
        if os.path.exists(env_script):
            subprocess.run([sys.executable, env_script, "--check"])
        report_seeding(a.active_niche)
        print()
        return

    print()
    print("  ============================================")
    print("   GENIE  --  First-Time Setup")
    print("  ============================================")
    print()
    print("  Getting Genie ready for your first book.")
    print("  This runs once and usually finishes in under 2 minutes.")
    print()

    # Step 0: apps and extensions (Node, engine CLIs, Chrome, DOCX->PDF
    # converter, VS Code extensions). Idempotent; failures are reported as
    # blockers by the script itself and never stop the rest of the bootstrap.
    if os.path.exists(env_script):
        subprocess.run([sys.executable, env_script])
        print()

    # Codex speed + auto-advance tuning (operator directive 2026-08-30):
    # keeps ~/.codex/config.toml fast (medium reasoning) and hands-off
    # (approval_policy never). Idempotent, additive-safe, .bak before change.
    tune_script = os.path.join(HERE, ".agents", "skills", "uapf-image-engines",
                               "codex_tune.py")
    if os.path.exists(tune_script):
        subprocess.run([sys.executable, tune_script], timeout=30)

    deps_ok = install_dependencies()
    mark["deps_installed"] = deps_ok
    mark["deps_checked_at"] = time.strftime("%Y-%m-%d")
    _save_mark(mark)
    if a.deps_only:
        return

    print()
    report_seeding(a.active_niche)
    mark["bootstrap_ran_at"] = time.strftime("%Y-%m-%d")
    _save_mark(mark)
    print()
    if deps_ok:
        print("  ============================================")
        print("   Setup complete! Genie is ready.")
        print("   Open Genie and tell it your book title")
        print("   to start your first book.")
        print("  ============================================")
    else:
        print("  ============================================")
        print("   Setup finished with some issues (see above).")
        print("   Contact your studio owner for help,")
        print("   or try opening Genie anyway — most features")
        print("   will still work.")
        print("  ============================================")
    print()


if __name__ == "__main__":
    main()
