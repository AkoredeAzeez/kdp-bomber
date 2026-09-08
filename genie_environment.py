#!/usr/bin/env python3
"""
GENIE ENVIRONMENT INSTALLER (first-run, every install, every tier)
==================================================================
Automatically installs the apps and extensions Genie needs to run
effectively, so a client never has to assemble their own toolchain.
Called by genie_bootstrap.py on every run; idempotent and fast once
satisfied. Never blocks production: anything it cannot install is
reported as a blocker with the exact manual command.

What it manages:
  REQUIRED
    - Node.js LTS                (runs the engine CLIs)
    - Claude Code CLI            (primary engine)   npm @anthropic-ai/claude-code
    - Codex CLI                  (failover engine)  npm @openai/codex
    - Google Chrome              (live research, cover/interior seeding, KDP)
    - DOCX->PDF converter        (Microsoft Word if present, else LibreOffice)
  OPTIONAL (installed only if the host app is already present)
    - VS Code extensions: openai.chatgpt (Codex), anthropic.claude-code

Windows: uses winget (App Installer, preinstalled on Win 10/11).
macOS:   uses Homebrew when present; otherwise prints the exact commands.

Usage:
  python genie_environment.py            # install whatever is missing
  python genie_environment.py --check    # report only, change nothing
State: state/environment.json  (render engine choice + last check result)
"""
import argparse, json, os, platform, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "state", "environment.json")
IS_WIN = platform.system() == "Windows"
IS_MAC = platform.system() == "Darwin"

def run(cmd, timeout=900):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           shell=isinstance(cmd, str))
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return 1, str(e)

def which(name):
    return shutil.which(name)

def word_present():
    if IS_WIN:
        for pf in (os.environ.get("ProgramFiles", r"C:\Program Files"),
                   os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")):
            for ver in ("root\\Office16", "Microsoft Office\\root\\Office16", "Microsoft Office\\Office16"):
                if os.path.exists(os.path.join(pf, ver, "WINWORD.EXE")):
                    return True
        return bool(which("winword"))
    if IS_MAC:
        return os.path.exists("/Applications/Microsoft Word.app")
    return False

def soffice_present():
    if which("soffice"):
        return True
    for p in (r"C:\Program Files\LibreOffice\program\soffice.exe",
              "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if os.path.exists(p):
            return True
    return False

def chrome_present():
    if IS_WIN:
        for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                  r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                  os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")):
            if os.path.exists(p):
                return True
        return False
    if IS_MAC:
        return os.path.exists("/Applications/Google Chrome.app")
    return bool(which("google-chrome") or which("chromium"))

def winget_install(pkg_id, label):
    print(f"[env] installing {label} via winget ...")
    code, out = run(["winget", "install", "-e", "--id", pkg_id, "--silent",
                     "--accept-package-agreements", "--accept-source-agreements"])
    ok = code == 0 or "already installed" in out.lower()
    print(f"[env]   {label}: {'OK' if ok else 'FAILED'}")
    if not ok:
        print(f"[env]   manual: winget install -e --id {pkg_id}")
    return ok

def brew_install(pkg, label, cask=False):
    if not which("brew"):
        print(f"[env] {label}: Homebrew not found. Manual: "
              f"brew install {'--cask ' if cask else ''}{pkg}")
        return False
    print(f"[env] installing {label} via brew ...")
    code, out = run(["brew", "install"] + (["--cask"] if cask else []) + [pkg])
    ok = code == 0 or "already installed" in out.lower()
    print(f"[env]   {label}: {'OK' if ok else 'FAILED'}")
    return ok

def npm_install(pkg, label):
    npm = which("npm")
    if not npm:
        print(f"[env] {label}: npm missing (Node not ready). Manual: npm install -g {pkg}")
        return False
    print(f"[env] installing {label} via npm ...")
    code, out = run([npm, "install", "-g", pkg])
    ok = code == 0
    print(f"[env]   {label}: {'OK' if ok else 'FAILED: ' + out.strip()[:120]}")
    return ok

def vscode_extension(ext_id, label):
    code_cli = which("code")
    if not code_cli:
        return None   # VS Code absent: extension is optional, skip silently
    code, out = run([code_cli, "--install-extension", ext_id, "--force"], timeout=300)
    ok = code == 0
    print(f"[env] VS Code extension {label}: {'OK' if ok else 'FAILED'}")
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report only")
    a = ap.parse_args()

    report, blockers = {}, []

    def ensure(name, present, installer):
        report[name] = "present" if present else "MISSING"
        if present or a.check:
            return present
        ok = installer()
        report[name] = "installed" if ok else "INSTALL FAILED"
        if not ok:
            blockers.append(name)
        return ok

    # 1) Node.js (prerequisite for both engine CLIs)
    ensure("node", bool(which("node")),
           lambda: winget_install("OpenJS.NodeJS.LTS", "Node.js LTS") if IS_WIN
           else brew_install("node", "Node.js"))

    # 2) Engine CLIs
    ensure("claude-code-cli", bool(which("claude")),
           lambda: npm_install("@anthropic-ai/claude-code", "Claude Code CLI"))
    ensure("codex-cli", bool(which("codex")),
           lambda: npm_install("@openai/codex", "Codex CLI"))

    # 3) Chrome
    ensure("chrome", chrome_present(),
           lambda: winget_install("Google.Chrome", "Google Chrome") if IS_WIN
           else brew_install("google-chrome", "Google Chrome", cask=True))

    # 4) DOCX->PDF converter: Word wins if present; LibreOffice is the free fallback
    have_word = word_present()
    have_soffice = soffice_present()
    if have_word:
        report["docx-to-pdf"] = "Microsoft Word"
        engine = "word"
    elif have_soffice:
        report["docx-to-pdf"] = "LibreOffice"
        engine = "libreoffice"
    elif a.check:
        report["docx-to-pdf"] = "MISSING (no Word, no LibreOffice)"
        engine = None
    else:
        ok = (winget_install("TheDocumentFoundation.LibreOffice", "LibreOffice") if IS_WIN
              else brew_install("libreoffice", "LibreOffice", cask=True))
        report["docx-to-pdf"] = "LibreOffice (installed)" if ok else "INSTALL FAILED"
        engine = "libreoffice" if ok else None
        if not ok:
            blockers.append("docx-to-pdf converter")

    # 5) VS Code extensions (only when VS Code is already installed)
    if which("code"):
        if not a.check:
            vscode_extension("openai.chatgpt", "Codex")
            vscode_extension("anthropic.claude-code", "Claude Code")
        report["vscode-extensions"] = "managed (VS Code present)"
    else:
        report["vscode-extensions"] = "skipped (VS Code not installed; optional)"

    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump({"render_engine": engine, "report": report}, open(STATE, "w"), indent=1)

    print("\n[env] environment summary:")
    for k, v in report.items():
        print(f"  {k:18} {v}")
    if blockers:
        print(f"[env] BLOCKERS (production continues; queue and retry): {', '.join(blockers)}")
        sys.exit(1)
    print("[env] environment ready.")

if __name__ == "__main__":
    main()
