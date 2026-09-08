#!/usr/bin/env python3
"""
GEMINI IMAGE ENGINE - uapf-image-engines (operator directive 2026-08-19)
========================================================================
Free Google AI Studio image generation (gemini-2.5-flash-image, the "Nano
Banana" line): photoreal quality, no visible watermark via the API, output
licensed for commercial use. Ships to clients: EACH INSTALL USES ITS OWN FREE
KEY, read from the GEMINI_API_KEY environment variable or a .env file at the
package root. The key is the client's own, entered by the client, never
shipped in any package, never committed (.env is git-ignored), and never
handled by Genie.

  python gemini_image_gen.py --prompt "..." --out images/fig-1-1.jpg [--aspect 16:9]

Aspect follows the book's niche image contract (--aspect 16:9 | 1:1 | 3:4 |
4:3 | 9:16); if the API rejects aspect config, the image is generated and
center-cropped to the target. Every output is auto-compressed: longest side
<= 1600 px, JPEG quality 85, target under 500 KB.

Exit 0 = image saved. Exit 2 = auth/quota/API failure with the exact error
printed: the caller reports it and falls back per the engine law (codex, then
FLUX) so a chapter never ships imageless. NEVER use the Gemini web/chat app
for book images (visible watermark); only this API route.
One-time client setup: https://aistudio.google.com/apikey -> Create API key ->
put GEMINI_API_KEY=<their key> in .env at the Genie folder root.
"""
import argparse, io, os, sys

MODEL = "gemini-2.5-flash-image"

def load_key():
    key = os.environ.get("GEMINI_API_KEY", "").strip()
    if key:
        return key
    # .env at package root (walk up from this file)
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        envp = os.path.join(d, ".env")
        if os.path.exists(envp):
            for line in open(envp, encoding="utf-8-sig"):
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
        d = os.path.dirname(d)
    return ""

def crop_to_aspect(img, aspect):
    try:
        w_r, h_r = (int(x) for x in aspect.split(":"))
    except Exception:
        return img
    W, H = img.size
    target = w_r / h_r
    cur = W / H
    if abs(cur - target) < 0.01:
        return img
    if cur > target:      # too wide -> crop width
        nw = int(H * target)
        x = (W - nw) // 2
        return img.crop((x, 0, x + nw, H))
    nh = int(W / target)  # too tall -> crop height
    y = (H - nh) // 2
    return img.crop((0, y, W, y + nh))

def compress(img, out_path, max_side=1600, quality=85):
    from PIL import Image
    W, H = img.size
    if max(W, H) > max_side:
        if W >= H:
            img = img.resize((max_side, int(H * max_side / W)), Image.LANCZOS)
        else:
            img = img.resize((int(W * max_side / H), max_side), Image.LANCZOS)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(out_path, "JPEG", quality=quality, optimize=True)
    return os.path.getsize(out_path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--aspect", default="16:9")
    a = ap.parse_args()

    key = load_key()
    if not key:
        print("GEMINI ENGINE NOT SET UP: no GEMINI_API_KEY found (env or .env).")
        print("One-time setup: https://aistudio.google.com/apikey -> Create API key,")
        print("then put  GEMINI_API_KEY=<your key>  in a .env file at the Genie root.")
        sys.exit(2)
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("SDK missing. One-time: pip install google-genai pillow")
        sys.exit(2)
    from PIL import Image

    client = genai.Client(api_key=key)
    cfg = None
    try:
        cfg = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(aspect_ratio=a.aspect))
    except Exception:
        cfg = types.GenerateContentConfig(response_modalities=["IMAGE"])
    try:
        resp = client.models.generate_content(model=MODEL, contents=a.prompt, config=cfg)
    except Exception as e:
        # honest failure for the fallback chain (auth, quota, network)
        print(f"GEMINI API FAILURE: {type(e).__name__}: {str(e)[:300]}")
        sys.exit(2)

    img = None
    try:
        for part in resp.candidates[0].content.parts:
            data = getattr(getattr(part, "inline_data", None), "data", None)
            if data:
                img = Image.open(io.BytesIO(data))
                break
    except Exception:
        pass
    if img is None:
        print("GEMINI returned no image (possibly safety-blocked prompt). Raw finish info:")
        try:
            print(" ", resp.candidates[0].finish_reason)
        except Exception:
            pass
        sys.exit(2)

    img = crop_to_aspect(img, a.aspect)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or ".", exist_ok=True)
    out = a.out if a.out.lower().endswith((".jpg", ".jpeg")) else os.path.splitext(a.out)[0] + ".jpg"
    size = compress(img, out)
    print(f"saved {out}  {img.size[0]}x{img.size[1]}  {size//1024} KB (model {MODEL}, aspect {a.aspect})")

if __name__ == "__main__":
    main()
