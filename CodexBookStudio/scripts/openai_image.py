#!/usr/bin/env python3
"""
OPENAI IMAGE HELPER  (Codex Book Studio)
========================================
Generates artwork for covers, A+ modules, and book interiors using OpenAI's
image models. This is the Codex agent's stand-in for Genie's Flow pipeline.

Uses gpt-image-2 (ChatGPT Images 2.0), OpenAI's reasoning image model. The
generated look differs from Genie's Flow house style, and each image spends the
user's own OpenAI credits. Requires a recent `openai` package and OPENAI_API_KEY
in the environment.

Usage:
  python openai_image.py --prompt "a cozy watercolor mountain cabin at dawn" \
      --out cover_front.png --size 1024x1536 --quality high
  python openai_image.py --prompt "..." --out art.png --n 3   # 3 variants -> art_1.png ...

Importable:
  from openai_image import generate
  paths = generate("prompt text", "out.png", size="1024x1536", n=1)

Common sizes (gpt-image-2):
  1024x1024  square (A+ tiles, spot art)
  1024x1536  portrait (front-cover art, interior portraits)
  1536x1024  landscape (A+ banners, scene spreads)
"""
import argparse, base64, os, sys
from pathlib import Path

MODEL = "gpt-image-2"
# Appended to every prompt, always. This guard is permanent and has no off switch.
CONTENT_GUARD = (" No pork, no pig imagery, no alcohol, no bottles or glasses of "
                 "wine or beer. Wholesome and family-safe.")


def generate(prompt, out_path, size="1024x1536", quality="high", n=1, model=MODEL):
    """Generate n image(s) for `prompt` and save as PNG. Returns list of paths.
    With n>1 the paths are suffixed _1, _2, ... before the extension."""
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        print("ERROR: OPENAI_API_KEY is not set in the environment.", file=sys.stderr)
        sys.exit(3)
    try:
        from openai import OpenAI
    except ImportError:
        print("ERROR: the 'openai' package is not installed. Run: pip install openai",
              file=sys.stderr)
        sys.exit(3)

    full_prompt = prompt + CONTENT_GUARD
    client = OpenAI(api_key=key)
    resp = client.images.generate(model=model, prompt=full_prompt, size=size,
                                  quality=quality, n=n)

    out = Path(out_path)
    paths = []
    for i, item in enumerate(resp.data, 1):
        b64 = getattr(item, "b64_json", None)
        if b64:
            data = base64.b64decode(b64)
        else:
            # Some models return a URL instead of inline base64.
            import urllib.request
            data = urllib.request.urlopen(item.url, timeout=120).read()
        dest = out if n == 1 else out.with_name(f"{out.stem}_{i}{out.suffix}")
        dest.write_bytes(data)
        paths.append(str(dest))
        print(f"saved {dest} ({len(data)//1024} KB)")
    return paths


def main():
    ap = argparse.ArgumentParser(description="Generate artwork via OpenAI image models")
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True, help="output PNG path")
    ap.add_argument("--size", default="1024x1536",
                    help="1024x1024 | 1024x1536 | 1536x1024")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high"])
    ap.add_argument("--n", type=int, default=1, help="number of variants")
    a = ap.parse_args()
    generate(a.prompt, a.out, size=a.size, quality=a.quality, n=a.n)


if __name__ == "__main__":
    main()
