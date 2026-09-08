#!/usr/bin/env python3
"""
CODEX IMAGE DELIVERY STEP - uapf-image-engines (operator directive 2026-08-19)
==============================================================================
Codex's native image tool saves to %USERPROFILE%\\.codex\\generated_images\\
<thread-id>\\ and on Windows often reports "read-only workspace prevented
saving" even though the image EXISTS there. This tool is the delivery man:
after EVERY codex image call it rescues the file, names it, verifies it, and
compresses it, so no image is ever lost to the sandbox.

  python codex_image_deliver.py --dest <project>/images --name IMG-37 [--src <path>]
      rescue: use --src when codex's reply printed the file path; otherwise the
      newest image in generated_images (all subfolders) is taken.
  python codex_image_deliver.py --compress-only <image.png|jpg>
      universal compression pass for ANY engine's output.

Compression law (all engines, before embedding): longest side <= 1600 px,
JPEG quality 85, target under 500 KB. Optional --polish adds 1.6x Lanczos
upscale + UnsharpMask (for softer free-tier engines like Pollinations).
Exit 0 = delivered/compressed, path printed. Exit 2 = nothing to deliver
(honest error; the caller reports and falls back, never silently).
"""
import argparse, os, shutil, sys, time

def newest_generated(minutes=180):
    root = os.path.join(os.path.expanduser("~"), ".codex", "generated_images")
    if not os.path.isdir(root):
        return None
    best, best_t = None, 0
    cutoff = time.time() - minutes * 60
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                p = os.path.join(dp, f)
                t = os.path.getmtime(p)
                if t > best_t and t >= cutoff:
                    best, best_t = p, t
    return best

def compress(src, out_path=None, max_side=1600, quality=85, polish=False):
    from PIL import Image, ImageFilter
    img = Image.open(src)
    if polish:
        W, H = img.size
        img = img.resize((int(W * 1.6), int(H * 1.6)), Image.LANCZOS)
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))
    W, H = img.size
    if max(W, H) > max_side:
        if W >= H:
            img = img.resize((max_side, int(H * max_side / W)), Image.LANCZOS)
        else:
            img = img.resize((int(W * max_side / H), max_side), Image.LANCZOS)
    if img.mode != "RGB":
        img = img.convert("RGB")
    out = out_path or (os.path.splitext(src)[0] + ".jpg")
    q = quality
    img.save(out, "JPEG", quality=q, optimize=True)
    while os.path.getsize(out) > 500 * 1024 and q > 60:
        q -= 5
        img.save(out, "JPEG", quality=q, optimize=True)
    if out != src and os.path.exists(src) and os.path.abspath(out) != os.path.abspath(src):
        try: os.remove(src)
        except OSError: pass
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", help="target images folder (rescue mode)")
    ap.add_argument("--name", help="target base name, e.g. IMG-37 or fig-3-2")
    ap.add_argument("--src", default=None, help="exact generated file path from codex's reply")
    ap.add_argument("--compress-only", dest="conly", default=None)
    ap.add_argument("--polish", action="store_true",
                    help="upscale 1.6x + unsharp mask before compressing (backup engines)")
    a = ap.parse_args()

    if a.conly:
        if not os.path.exists(a.conly):
            print("file not found:", a.conly); sys.exit(2)
        out = compress(a.conly, polish=a.polish)
        print(f"compressed -> {out}  {os.path.getsize(out)//1024} KB")
        return

    if not a.dest or not a.name:
        sys.exit("rescue mode needs --dest and --name (or use --compress-only FILE)")
    src = a.src if a.src and os.path.exists(a.src) else newest_generated()
    if not src:
        print("DELIVERY FAILED: no generated image found (reply path missing and "
              "~/.codex/generated_images has no recent file). Report this honestly; "
              "do not claim the image exists.")
        sys.exit(2)
    os.makedirs(a.dest, exist_ok=True)
    staging = os.path.join(a.dest, a.name + os.path.splitext(src)[1].lower())
    shutil.copy2(src, staging)
    if os.path.getsize(staging) <= 0:
        print("DELIVERY FAILED: copied file is 0 KB"); sys.exit(2)
    out = compress(staging, out_path=os.path.join(a.dest, a.name + ".jpg"), polish=a.polish)
    try: os.remove(src)  # tidy the leftover original
    except OSError: pass
    from PIL import Image
    W, H = Image.open(out).size
    print(f"DELIVERED {out}  {W}x{H}  {os.path.getsize(out)//1024} KB  (rescued from {os.path.basename(os.path.dirname(src))})")

if __name__ == "__main__":
    main()
