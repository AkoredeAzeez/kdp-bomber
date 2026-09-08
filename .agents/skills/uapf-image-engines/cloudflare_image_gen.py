#!/usr/bin/env python3
"""
CLOUDFLARE WORKERS AI IMAGE ENGINE - uapf-image-engines (operator directive 2026-08-21)
=======================================================================================
Free, headless, commercial-safe image generation via Cloudflare Workers AI
(@cf/black-forest-labs/flux-1-schnell, Apache-2.0). Verified 2026-08-21: the
Workers Free plan gives 10,000 Neurons/day at no charge (no card), resetting
daily at 00:00 UTC, which is on the order of ~100 book images per day. Each
install uses its OWN free Cloudflare account, so its quota is separate from HF
Spaces and Pollinations: adding this raises the total free ceiling.

  python cloudflare_image_gen.py --prompt "..." --out images/IMG-37.png
         [--width 1024 --height 576 --steps 4]

PER-INSTALL KEY LAW (same as Gemini): the client puts their OWN free Cloudflare
credentials in a .env at the Genie root:
    CF_ACCOUNT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    CF_API_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Token needs the "Workers AI" permission. The .env is never shipped (factory
excludes it), never committed (.gitignore), never printed, never entered by
Genie. Get them free at dash.cloudflare.com (no card for the free tier).

FLUX-schnell is Apache-2.0 -> commercial-safe for sold books. Output is a real
photoreal render; the standard compression pass still applies before embedding.
Exit 0 = saved. Exit 2 = honest failure (bad token, rate limit, no image); the
caller reports it and falls back, never silently.
"""
import argparse, base64, json, os, sys, urllib.request, urllib.error

MODEL = "@cf/black-forest-labs/flux-1-schnell"

def load_creds():
    acct = os.environ.get("CF_ACCOUNT_ID", "").strip()
    tok = os.environ.get("CF_API_TOKEN", "").strip()
    if acct and tok:
        return acct, tok
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        envp = os.path.join(d, ".env")
        if os.path.exists(envp):
            for line in open(envp, encoding="utf-8-sig"):
                line = line.strip()
                if line.startswith("CF_ACCOUNT_ID=") and not acct:
                    acct = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("CF_API_TOKEN=") and not tok:
                    tok = line.split("=", 1)[1].strip().strip('"').strip("'")
        d = os.path.dirname(d)
    return acct, tok

def crop_to_aspect(path, width, height):
    from PIL import Image
    img = Image.open(path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    target = width / height
    W, H = img.size
    cur = W / H
    if abs(cur - target) > 0.02:
        if cur > target:                      # too wide -> crop sides
            nw = int(H * target)
            left = (W - nw) // 2
            img = img.crop((left, 0, left + nw, H))
        else:                                 # too tall -> crop top/bottom
            nh = int(W / target)
            top = (H - nh) // 2
            img = img.crop((0, top, W, top + nh))
    img = img.resize((width, height), Image.LANCZOS)
    img.save(path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--width", type=int, default=1024)
    ap.add_argument("--height", type=int, default=576)   # 16:9 default
    ap.add_argument("--steps", type=int, default=4)      # schnell: 1-8
    a = ap.parse_args()

    acct, tok = load_creds()
    if not acct or not tok:
        print("Cloudflare credentials missing. Put CF_ACCOUNT_ID and CF_API_TOKEN "
              "in a .env at the Genie root (free at dash.cloudflare.com, no card).")
        sys.exit(2)

    url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/{MODEL}"
    body = json.dumps({"prompt": a.prompt, "steps": max(1, min(a.steps, 8))}).encode()
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=180)
        raw = resp.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:200]
        if e.code == 429:
            print("Cloudflare RATE LIMITED (daily 10,000-neuron free cap reached or too fast). "
                  "Fall back to another engine; resets 00:00 UTC.")
        elif e.code in (401, 403):
            print("Cloudflare AUTH FAILED: check CF_API_TOKEN has the Workers AI permission "
                  "and CF_ACCOUNT_ID is correct.")
        else:
            print(f"Cloudflare HTTP {e.code}: {detail}")
        sys.exit(2)
    except Exception as e:
        print("Cloudflare request failed:", str(e)[:160]); sys.exit(2)

    img_bytes = None
    ctype = None
    try:
        j = json.loads(raw.decode("utf-8"))
        if j.get("success") and isinstance(j.get("result"), dict) and j["result"].get("image"):
            img_bytes = base64.b64decode(j["result"]["image"])
        else:
            errs = j.get("errors") or j
            print("Cloudflare returned no image:", json.dumps(errs)[:200]); sys.exit(2)
    except (ValueError, UnicodeDecodeError):
        img_bytes = raw          # some models return raw binary image bytes

    if not img_bytes or len(img_bytes) < 2000:
        print("Cloudflare produced an empty/tiny image."); sys.exit(2)

    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    with open(a.out, "wb") as f:
        f.write(img_bytes)
    try:
        crop_to_aspect(a.out, a.width, a.height)
    except Exception as e:
        print("saved but aspect-crop skipped:", str(e)[:100])
    print(f"SAVED {a.out}  {os.path.getsize(a.out)//1024} KB  (cloudflare flux-1-schnell)")

if __name__ == "__main__":
    main()
