#!/usr/bin/env python3
r"""FAST CODEX IMAGE RUNNER (operator directive 2026-08-29)
==========================================================
Covers and A+ modules were slow because every `codex exec` inherited the
global config's model_reasoning_effort="xhigh" AND started in the Genie root,
where Codex loads the full 70KB AGENTS.md law file before doing anything.

This runner strips all of that away for image jobs:
  - clean working room (state/codex_imgroom/) with a 4-line AGENTS.md that
    says "call the image tool immediately";
  - model_reasoning_effort forced to "low" (image quality is unaffected: the
    image model is separate from the reasoning model);
  - --skip-git-repo-check and --ephemeral: no repo scan, no session files;
  - the delivery rescue built in: if the sandbox blocked the save, the file
    is recovered from ~/.codex/generated_images.

Usage:
  python codex_fast_image.py --brief brief.txt --out cover.png
  python codex_fast_image.py --brief brief.txt --out module1.png \
      --image "C:\path\to\exact_cover.png"     # attach input image (A+ mockups)
  Add --timeout 600 to change the cap (default 900 s).

Prints IMAGE OK <path> <WxH> <seconds>s on success; exits non-zero on failure.
"""
import argparse, glob, os, shutil, subprocess, sys, time

GENIE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
ROOM = os.path.join(GENIE, "state", "codex_imgroom")

ROOM_RULES = """You are an image generation runner. Your ONLY job:
1. Read the brief in the prompt and call your image generation tool with it IMMEDIATELY. Do not read files, do not explore, do not plan.
2. Save the image in the current directory with the EXACT filename the prompt names.
3. Reply with just the filename. Nothing else.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", required=True, help="text file holding the full image brief")
    ap.add_argument("--out", required=True, help="destination path for the finished image")
    ap.add_argument("--image", action="append", default=[],
                    help="input image(s) to attach (A+ exact-cover mockups); repeatable")
    ap.add_argument("--timeout", type=int, default=900)
    a = ap.parse_args()

    os.makedirs(ROOM, exist_ok=True)
    with open(os.path.join(ROOM, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(ROOM_RULES)
    # start from an empty room so stale outputs are never mistaken for results
    for old in glob.glob(os.path.join(ROOM, "*.png")) + glob.glob(os.path.join(ROOM, "*.jpg")):
        os.remove(old)

    name = os.path.basename(a.out)
    brief = open(a.brief, encoding="utf-8").read().strip()
    prompt = ("Generate this image now with your image generation tool and save it in the "
              "current directory as exactly \"%s\":\n\n%s" % (name, brief))

    codex = shutil.which("codex")
    if not codex:
        sys.exit("codex CLI not found on PATH")
    # The prompt goes through STDIN (the '-' argument), never through argv:
    # Windows shell quoting mangles multiline briefs and a mangled prompt makes
    # codex block forever waiting on stdin (proven 2026-08-29).
    launcher = ["cmd.exe", "/c", codex] if codex.lower().endswith((".cmd", ".bat")) else [codex]
    cmd = launcher + ["exec",
           "-C", ROOM,
           "--skip-git-repo-check", "--ephemeral",
           "--sandbox", "workspace-write",
           "-c", 'model_reasoning_effort="low"']
    for img in a.image:
        cmd.append("--image=%s" % img)   # equals form: the bare -i flag is greedy
    cmd.append("-")

    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=a.timeout,
                       input=prompt, shell=False,
                       encoding="utf-8", errors="replace")
    dt = time.time() - t0

    produced = os.path.join(ROOM, name)
    if not os.path.exists(produced):
        # sandbox-block rescue: newest file in the codex fallback folder
        fb = os.path.join(os.path.expanduser("~"), ".codex", "generated_images")
        cands = sorted(glob.glob(os.path.join(fb, "*")), key=os.path.getmtime, reverse=True)
        if cands and os.path.getmtime(cands[0]) >= t0:
            produced = cands[0]
    if not os.path.exists(produced):
        sys.stderr.write("IMAGE FAILED after %.0fs\n--- codex tail ---\n%s\n"
                         % (dt, (r.stdout or r.stderr or "")[-800:]))
        sys.exit(1)

    from PIL import Image
    im = Image.open(produced)
    im.verify()
    im = Image.open(produced)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    if os.path.abspath(produced) != os.path.abspath(a.out):
        shutil.copy2(produced, a.out)
    print("IMAGE OK %s %dx%d %.0fs" % (a.out, im.width, im.height, dt))


if __name__ == "__main__":
    main()
