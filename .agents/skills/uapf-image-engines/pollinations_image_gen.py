#!/usr/bin/env python3
"""
POLLINATIONS BACKUP ENGINE - uapf-image-engines (operator directive 2026-08-19)
===============================================================================
Free backup image engine for when Codex hits its usage limit or fails. Uses
ONLY the classic free endpoint (image.pollinations.ai); the gen.pollinations.ai
premium routes are never used (they fail with "insufficient pollen"). Works
keyless; a free token (sk_..., from enter.pollinations.ai, no card) in the
POLLINATIONS_TOKEN env var or .env raises the rate limits. The free tier
serves a softer model, so every output gets the POLISH pass (1.6x Lanczos
upscale + UnsharpMask) before the standard compression: backup/draft quality,
honestly labeled; Codex remains the quality engine.

  python pollinations_image_gen.py --prompt "..." --out images/IMG-37.jpg
         [--width 1024 --height 576]

429 -> wait 20 s, retry up to 5 times. Exit 0 saved; exit 2 honest failure
(the caller reports it; never silently switch tools).
"""
import argparse, os, random, sys, time, urllib.parse, urllib.request

def load_token():
    tok = os.environ.get("POLLINATIONS_TOKEN", "").strip()
    if tok:
        return tok
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        envp = os.path.join(d, ".env")
        if os.path.exists(envp):
            for line in open(envp, encoding="utf-8-sig"):
                if line.strip().startswith("POLLINATIONS_TOKEN="):
                    return line.strip().split("=", 1)[1].strip().strip('"').strip("'")
        d = os.path.dirname(d)
    return ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1024)
    ap.add_argument("--height", type=int, default=576)   # 16:9 default
    a = ap.parse_args()

    q = urllib.parse.quote(a.prompt)
    url = (f"https://image.pollinations.ai/prompt/{q}"
           f"?width={a.width}&height={a.height}&nologo=true&seed={random.randint(1, 10**9)}")
    tok = load_token()
    if tok:
        url += "&key=" + urllib.parse.quote(tok)

    data = None
    for attempt in range(1, 6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            r = urllib.request.urlopen(req, timeout=180)
            data = r.read()
            if data and len(data) > 5000:
                break
            print(f"[attempt {attempt}] tiny/empty response, retrying in 20s...")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[attempt {attempt}] 429 rate-limited; waiting 20s...")
            else:
                print(f"POLLINATIONS FAILED: HTTP {e.code}: {str(e.reason)[:120]}")
                sys.exit(2)
        except Exception as e:
            print(f"[attempt {attempt}] {type(e).__name__}: {str(e)[:120]}; retrying in 20s...")
        time.sleep(20)
    if not data or len(data) <= 5000:
        print("POLLINATIONS FAILED: no image after 5 attempts. Report honestly; do not switch silently.")
        sys.exit(2)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    raw = os.path.splitext(a.out)[0] + ".raw.png"
    open(raw, "wb").write(data)

    # POLISH + compress via the shared delivery tool logic
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "codex_image_deliver",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "codex_image_deliver.py"))
    d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
    out = os.path.splitext(a.out)[0] + ".jpg"
    final = d.compress(raw, out_path=out, polish=True)
    from PIL import Image
    W, H = Image.open(final).size
    print(f"saved {final}  {W}x{H}  {os.path.getsize(final)//1024} KB "
          f"(pollinations free tier, polished; backup quality)")

if __name__ == "__main__":
    main()
