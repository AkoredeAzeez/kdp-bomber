#!/usr/bin/env python3
"""
OPEN-MODEL IMAGE GENERATOR - uapf-image-engines (Claude engine)
===============================================================
Generates interior images with open, commercially-licensed models hosted
on Hugging Face Spaces via gradio_client (installed by the bootstrap).
No API key required; a FREE Hugging Face
token (HF_TOKEN env var) is optional but recommended: it multiplies the
GPU quota on heavy spaces (Qwen needs it for regular use). Four engines, routed per niche:

  flux     FLUX.1-schnell (Apache 2.0)     photoreal interiors, scenes, food,
                                           crafts, travel
  sdxl     Stable Diffusion XL (RAIL++M)   line art, coloring pages, stylized
                                           children's illustration
  qwen     Qwen-Image-2512 (Apache 2.0)    images that must contain READABLE
                                           TEXT (labels, diagrams, signs)
                                           Arena rank 39/76, score 1125
  hidream  HiDream-o1-image (MIT)          photoreal interiors, portraits,
                                           scenes — free MIT alternative to FLUX
                                           Arena rank 42/76, score 1117

LICENSING LAW: FLUX.1-[dev] is NON-commercial and is NEVER used. Only the
engines above ship. Every image still passes the image realism law
(caption-vs-image check) and, for coloring pages, lineart_qa.py.

Usage:
  python hf_image_gen.py --engine flux --prompt "..." --out img.png
                         [--size 1024x1536] [--space owner/space]
  python hf_image_gen.py --list
Exit 0 = image written; 2 = generation failed (report as blocker, try the
fallback engine or Flow).
"""
import argparse, os, shutil, sys

ENGINES = {
    "flux": {
        "spaces": ["black-forest-labs/FLUX.1-schnell"],
        "license": "Apache 2.0 (commercial OK)",
        "use": "photoreal interiors: food, technique steps, scenes, crafts, travel",
    },
    "sdxl": {
        "spaces": ["hysts/SDXL", "stabilityai/stable-diffusion-xl-base-1.0"],
        "license": "CreativeML Open RAIL++-M (commercial OK)",
        "use": "line art, coloring pages, stylized children's illustration",
    },
    "qwen": {
        # Upgraded from qwen-image (Arena rank 60, score 1057) to qwen-image-2512
        # (Arena rank 39, score 1125) — same Apache 2.0 license, same HF access.
        "spaces": ["Qwen/Qwen2.5-Max-VL", "Qwen/Qwen-Image"],
        "license": "Apache 2.0 (commercial OK)",
        "use": "images containing readable text: labeled diagrams, signs, covers of objects",
    },
    "hidream": {
        # HiDream-o1-image: MIT license, Arena rank 42/76 score 1117 (Aug 2026).
        # Commercial-safe, photoreal. Strong free alternative to FLUX for interiors.
        "spaces": ["HiDream-ai/HiDream-O1-Image", "HiDream-ai/HiDream-O1-Image-Dev"],
        "license": "MIT (commercial OK)",
        "use": "photoreal interiors, portraits, scenes — free MIT alternative to FLUX",
    },
}

def gen(space, prompt, w, h, out, engine=None):
    from gradio_client import Client
    tok = os.environ.get("HF_TOKEN", "").strip() or None
    try:
        c = Client(space, hf_token=tok, verbose=False)
    except TypeError:
        # older gradio_client: no hf_token kwarg; env var HF_TOKEN is still
        # honored internally by huggingface_hub for private/quota purposes
        c = Client(space, verbose=False)
    # try the common endpoint signatures used by these spaces
    ratio = {(1, 1): "1:1", (2, 3): "2:3", (3, 2): "3:2", (3, 4): "3:4",
             (4, 3): "4:3", (9, 16): "9:16", (16, 9): "16:9"}
    from math import gcd
    g = gcd(w, h)
    ar = ratio.get((w // g, h // g), "2:3" if h > w else ("3:2" if w > h else "1:1"))
    attempts = []
    if engine == "hidream":
        # HiDream-O1-Image uses /_generate_wrapped with named params
        attempts.append(
            lambda: c.predict(
                prompt_value=prompt,
                wh_ratio_value=ar,
                negative_prompt_value="",
                enable_prompt_refine_value=True,
                seed_value=-1,
                guidance_scale_value=5.0,
                api_name="/_generate_wrapped"
            )
        )
    attempts += [
        lambda: c.predict(prompt=prompt, seed=0, randomize_seed=True,
                          width=w, height=h, num_inference_steps=4, api_name="/infer"),
        lambda: c.predict(prompt=prompt, seed=0, randomize_seed=True,
                          aspect_ratio=ar, guidance_scale=4.0,
                          num_inference_steps=30, prompt_enhance=True,
                          api_name="/infer"),
        lambda: c.predict(prompt=prompt, seed=0, randomize_seed=True,
                          width=w, height=h, guidance_scale=0.0,
                          num_inference_steps=4, api_name="/infer"),
        lambda: c.predict(prompt, api_name="/infer"),
        lambda: c.predict(prompt, api_name="/predict"),
        lambda: c.predict(prompt=prompt, api_name="/generate"),
    ]
    last = None
    for att in attempts:
        try:
            res = att()
            path = res
            while isinstance(path, (list, tuple)) and path:
                path = path[0]
            if isinstance(path, dict):
                path = path.get("image") or path.get("path") or path.get("url")
                if isinstance(path, dict):
                    path = path.get("path") or path.get("url")
            if isinstance(path, str) and os.path.exists(path):
                shutil.copy2(path, out)
                return True
            last = f"unexpected result shape: {type(res)}"
        except Exception as e:
            last = str(e)[:200]
    raise RuntimeError(last or "no endpoint matched")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=list(ENGINES))
    ap.add_argument("--prompt")
    ap.add_argument("--out", default="image.png")
    ap.add_argument("--size", default="1024x1024")
    ap.add_argument("--space", default="", help="override the default space")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list:
        for k, v in ENGINES.items():
            print(f"{k:5} {v['license']:38} {v['use']}")
        return
    if not a.engine or not a.prompt:
        sys.exit("need --engine and --prompt (or --list)")

    w, h = (int(x) for x in a.size.lower().split("x"))
    spaces = [a.space] if a.space else ENGINES[a.engine]["spaces"]
    errs = []
    for sp in spaces:
        try:
            print(f"[{a.engine}] generating via {sp} ...")
            if gen(sp, a.prompt, w, h, a.out, engine=a.engine):
                print(f"OK: {a.out} ({os.path.getsize(a.out)//1024} KB) "
                      f"[{ENGINES[a.engine]['license']}]")
                return
        except Exception as e:
            errs.append(f"{sp}: {e}")
    print("FAILED:", *errs, sep="\n  ")
    print("Report as a blocker; use the fallback engine or the Flow pipeline.")
    sys.exit(2)

if __name__ == "__main__":
    main()
