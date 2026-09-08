#!/usr/bin/env python3
"""
LINE-ART QA GATE - uapf-coloring-studio
=======================================
Mechanically validates a coloring page image before it may enter a book:

  1. LINE ART: overwhelmingly near-white paper + near-black lines; gray
     midtones (which print muddy and ruin colorability) below threshold.
  2. INK COVERAGE: line coverage in a sane band (too little = empty page,
     too much = solid blobs no one can color).
  3. RESOLUTION: at least 300 DPI at the target trim.
  4. MARGIN SAFETY: page edges essentially white (art must not touch the
     trim edge unless the design is explicitly full-bleed: --bleed).

Exit 0 PASS / 2 FAIL per file; a FAILing page is regenerated, never shipped.

Usage:
  python lineart_qa.py <image(s)> [--trim 8.5x11] [--bleed] [--json out.json]
"""
import argparse, glob, json, os, sys

def check(path, trim_w, trim_h, bleed):
    from PIL import Image
    im = Image.open(path).convert("L")
    w, h = im.size
    problems = []
    need_w, need_h = int(trim_w * 300), int(trim_h * 300)
    if w < need_w * 0.98 or h < need_h * 0.98:
        problems.append(f"resolution {w}x{h} below 300 DPI for {trim_w}x{trim_h} in ({need_w}x{need_h} needed)")
    hist = im.histogram()
    total = w * h
    dark = sum(hist[:64]) / total          # near-black lines
    light = sum(hist[192:]) / total        # near-white paper
    mid = 1.0 - dark - light               # muddy grays
    if mid > 0.10:
        problems.append(f"{mid:.0%} gray midtones (max 10%): not clean line art, will print muddy")
    if dark < 0.015:
        problems.append(f"only {dark:.1%} ink coverage: page is nearly empty")
    if dark > 0.45:
        problems.append(f"{dark:.0%} ink coverage: too heavy to color")
    if not bleed:
        m = max(2, int(w * 0.02))
        edges = [im.crop((0, 0, w, m)), im.crop((0, h - m, w, h)),
                 im.crop((0, 0, m, h)), im.crop((w - m, 0, w, h))]
        edge_dark = sum(sum(e.histogram()[:128]) for e in edges) / sum(e.size[0] * e.size[1] for e in edges)
        if edge_dark > 0.02:
            problems.append(f"art touches page edges ({edge_dark:.1%} dark pixels in margin band); not margin-safe for a no-bleed page")
    return {"file": os.path.basename(path), "size": [w, h],
            "ink": round(dark, 3), "midtones": round(mid, 3),
            "verdict": "FAIL" if problems else "PASS", "problems": problems}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--trim", default="8.5x11")
    ap.add_argument("--bleed", action="store_true")
    ap.add_argument("--json")
    a = ap.parse_args()
    tw, th = (float(x) for x in a.trim.lower().split("x"))
    files = [f for pat in a.images for f in glob.glob(pat)]
    results = [check(f, tw, th, a.bleed) for f in files]
    fails = 0
    for r in results:
        print(f"{r['verdict']}  {r['file']}  {r['size'][0]}x{r['size'][1]}  ink {r['ink']:.1%}  mid {r['midtones']:.1%}")
        for p in r["problems"]:
            print("    -", p)
        fails += r["verdict"] == "FAIL"
    if a.json:
        json.dump(results, open(a.json, "w"), indent=1)
    print(f"{len(results) - fails}/{len(results)} pages pass")
    sys.exit(2 if fails else 0)

if __name__ == "__main__":
    main()
