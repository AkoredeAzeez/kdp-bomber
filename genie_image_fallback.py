"""FREE headless image fallback for use during a Claude usage limit.

When Claude is down there is no browser driver for the premium generators (Flow / ChatGPT
Image 2.0). This helper generates an image with NO browser, NO API key, and NO cost via the
Z-Image Turbo Gradio space, so Codex can keep an illustrated book moving. Every image it
produces is recorded in a regeneration queue and MUST be re-generated at premium quality
(ChatGPT Image 2.0 for Codex chapters / Google Flow for Claude chapters) once a browser
driver is available again. Fallback images are placeholder-grade, never final.

Usage:
  python genie_image_fallback.py --project DIR --prompt "..." --out units/IMG-R02.png [--slot IMG-R02]
  python genie_image_fallback.py --project DIR --list-regen        # show pending premium regens
"""
import argparse
import json
import os
import time
from datetime import datetime, timezone

SPACE = "mcp-tools/Z-Image-Turbo"
RESOLUTION = "1472x1104 ( 4:3 )"
API_NAMES = ["/generate", "/infer", "/predict", None]  # tried in order; None -> fn_index=0


def _now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _regen_queue(project):
    return os.path.join(project, "state", "image_regen_queue.jsonl")


def _flag_for_regen(project, out_rel, slot, prompt):
    """Record that this image is fallback-grade and needs premium regeneration."""
    os.makedirs(os.path.join(project, "state"), exist_ok=True)
    entry = {"ts": _now(), "slot": slot, "file": out_rel, "prompt": prompt,
             "source": "z-image-fallback", "quality": "fallback",
             "needs_premium_regen": True,
             "premium_target": "ChatGPT Image 2.0 (Codex) / Google Flow (Claude)"}
    with open(_regen_queue(project), "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def _save_result_as_png(result, out_abs):
    """Z-Image returns (gallery, seed_str, seed_int); gallery items are local file paths
    or dicts. Extract the image and save as PNG."""
    from PIL import Image
    gallery = result[0] if isinstance(result, (list, tuple)) else result
    item = gallery[0] if isinstance(gallery, (list, tuple)) else gallery
    path = None
    if isinstance(item, dict):
        path = item.get("image") or item.get("path") or item.get("url") or item.get("name")
        if isinstance(path, dict):
            path = path.get("path") or path.get("url")
    elif isinstance(item, (list, tuple)):
        path = item[0]
    else:
        path = item
    if not path:
        raise RuntimeError("could not locate image in Z-Image result: %r" % (item,))
    if str(path).startswith("http"):
        import urllib.request
        req = urllib.request.Request(path, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        import io
        Image.open(io.BytesIO(data)).convert("RGB").save(out_abs)
    else:
        Image.open(path).convert("RGB").save(out_abs)


def generate(project, prompt, out_rel, slot=None, retries=3):
    """Generate one fallback image to <project>/<out_rel> and flag it for regen.
    Returns (ok, error)."""
    from gradio_client import Client
    out_abs = os.path.join(project, out_rel)
    os.makedirs(os.path.dirname(out_abs), exist_ok=True)
    last = None
    for attempt in range(retries):
        try:
            client = Client(SPACE)
            result = None
            for name in API_NAMES:
                try:
                    kw = dict(prompt=prompt, random_seed=True, seed=42,
                              resolution=RESOLUTION, shift=3, steps=8)
                    result = client.predict(api_name=name, **kw) if name else client.predict(fn_index=0, **kw)
                    break
                except Exception as e:
                    last = str(e)
            if result is None:
                raise RuntimeError(last or "no endpoint matched")
            _save_result_as_png(result, out_abs)
            _flag_for_regen(project, out_rel, slot or os.path.basename(out_rel), prompt)
            return True, None
        except Exception as e:
            last = str(e)
            time.sleep(3)
    return False, last


def list_regen(project):
    q = _regen_queue(project)
    if not os.path.exists(q):
        return []
    return [json.loads(l) for l in open(q, encoding="utf-8") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--prompt")
    ap.add_argument("--out")
    ap.add_argument("--slot")
    ap.add_argument("--list-regen", action="store_true")
    a = ap.parse_args()
    if a.list_regen:
        for e in list_regen(a.project):
            print(json.dumps(e))
        return
    ok, err = generate(a.project, a.prompt, a.out, a.slot)
    print(json.dumps({"ok": ok, "out": a.out, "error": err,
                      "note": "FALLBACK image -- flagged for premium regeneration"}))


if __name__ == "__main__":
    main()
