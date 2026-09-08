#!/usr/bin/env python3
"""
OVERLAY GEN - uapf-video-studio
===============================
Render one transparent text/graphics overlay PNG per scene, in the brand look,
to composite over stock footage. No blue "brand background" is drawn: the scene
background IS the stock video; overlays add a neutral scrim + brand-coloured text
so the footage stays visible and the copy stays readable.

  python overlay_gen.py --scenes scenes.json --brand genie --aspect 16:9 --out overlays/

Scene styles: caption (footage + bottom copy), center (centred copy), title/end
(wordmark + optional plan chips + pill), panel (structured card over footage).
"""
import argparse, json, os
from PIL import Image, ImageDraw
import vstudio_common as C

SIZES = {"16:9": (1920, 1080), "9:16": (1080, 1920), "1:1": (1080, 1080)}

def render(spec, brand, size):
    W, H = size
    pal = brand["rgb"]
    INK, INK2, INK3 = pal["ink"], pal["ink2"], pal["ink3"]
    ACC, GREEN = pal["accent"], pal.get("green", pal["accent"])
    SCRIM = pal.get("scrim", (6, 7, 8)); PANEL = pal.get("panel", (12, 13, 15))
    PT = brand["pill_text_rgb"]
    big = 0.052 if size[0] >= size[1] else 0.075   # heading size factor vs width
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    style = spec.get("style", "caption")
    kick = C.clean_text(spec.get("kicker", "")); head = C.clean_text(spec.get("heading", ""))
    sub = C.clean_text(spec.get("sub", "")); pill_txt = spec.get("pill")

    def mono(sz): return C.font("mono-medium", sz)
    def disp(sz): return C.font("display", sz)
    def body(sz, it=False): return C.font("body", sz, italic=it)

    if style in ("caption",):
        im = C.scrim_uniform(im, 70, SCRIM); im = C.scrim_bottom(im, 0.42, 240, SCRIM); im = C.scrim_top(im, 120, SCRIM)
        d = ImageDraw.Draw(im)
        if kick: C.spaced(d, W//2, int(H*0.635), kick.upper(), mono(int(W*0.016)), ACC, int(W*0.005))
        f, _ = C.fit_font(d, [head], "display", int(W*big), 1, W*0.86)
        d.text((W//2, int(H*0.71)), head, font=f, fill=INK, anchor="mm")
        if sub: d.text((W//2, int(H*0.80)), sub, font=body(int(W*0.019), True), fill=INK2, anchor="mm")

    elif style in ("center", "statement"):
        im = C.scrim_uniform(im, 70, SCRIM); im = C.scrim_center(im, 224, SCRIM)
        d = ImageDraw.Draw(im)
        if kick: C.spaced(d, W//2, int(H*0.34), kick.upper(), mono(int(W*0.016)), ACC, int(W*0.005))
        f, _ = C.fit_font(d, [head], "display", int(W*0.06), 1, W*0.82)
        d.text((W//2, int(H*0.44)), head, font=f, fill=INK, anchor="mm")
        for i, ln in enumerate(spec.get("lines", ([sub] if sub else []))):
            col = ACC if i == len(spec.get("lines", [sub]))-1 and spec.get("accent_last") else INK2
            d.text((W//2, int(H*0.55)+i*int(H*0.06)), C.clean_text(ln), font=body(int(W*0.02)), fill=col, anchor="mm")
        if pill_txt: C.pill(d, W//2, int(H*0.80), pill_txt, C.font("display-mid", int(W*0.018)), ACC, PT)

    elif style in ("title", "end"):
        im = C.scrim_uniform(im, 70, SCRIM); im = C.scrim_center(im, 232, SCRIM)
        d = ImageDraw.Draw(im)
        if kick: C.spaced(d, W//2, int(H*0.14), kick.upper(), mono(int(W*0.014)), INK2, int(W*0.004))
        C.spaced(d, W//2, int(H*0.18), spec.get("wordmark", brand["name"]), disp(int(W*0.09)), ACC, 1)
        if sub: d.text((W//2, int(H*0.37)), sub, font=body(int(W*0.021), False), fill=INK, anchor="mm")
        chips = spec.get("plans", [])
        if chips:
            ew = int(W*0.24); gap = int(W*0.02); total = ew*len(chips)+gap*(len(chips)-1)
            ex = (W-total)//2; ey = int(H*0.45); eh = int(H*0.20)
            for name, forr, feat in chips:
                d.rounded_rectangle([ex, ey, ex+ew, ey+eh], radius=18, fill=PANEL+(220,),
                                    outline=(ACC+(255,) if feat else (255, 255, 255, 45)), width=2)
                d.text((ex+ew//2, ey+int(eh*0.42)), name, font=disp(int(W*0.024)), fill=INK, anchor="mm")
                d.text((ex+ew//2, ey+int(eh*0.72)), forr, font=body(int(W*0.015), True), fill=INK2, anchor="mm")
                ex += ew+gap
        if spec.get("cohort"): d.text((W//2, int(H*0.73)), C.clean_text(spec["cohort"]), font=disp(int(W*0.026)), fill=INK, anchor="mm")
        if pill_txt: C.pill(d, W//2, int(H*0.81), pill_txt, C.font("display-mid", int(W*0.016)), ACC, PT)
        if spec.get("fine"): d.text((W//2, int(H*0.89)), C.clean_text(spec["fine"]), font=mono(int(W*0.012)), fill=INK3, anchor="mm")

    elif style == "panel":
        im = C.scrim_uniform(im, 66, SCRIM)
        d = ImageDraw.Draw(im)
        if kick: C.spaced(d, W//2, int(H*0.08), kick.upper(), mono(int(W*0.015)), ACC, int(W*0.005))
        if head:
            f, _ = C.fit_font(d, [head], "display", int(W*0.045), 1, W*0.82)
            d.text((W//2, int(H*0.14)), head, font=f, fill=INK, anchor="mm")
        px0, px1 = int(W*0.20), int(W*0.80); py0, py1 = int(H*0.24), int(H*0.82)
        im = C.panel(im, [px0, py0, px1, py1], a=220, panelc=PANEL)
        d = ImageDraw.Draw(im)
        ix = px0 + int(W*0.03); iy = py0 + int(H*0.04); iw = px1 - px0 - int(W*0.06)
        for blk in spec.get("items", []):
            k = blk.get("kind")
            if k == "row":
                a, b = blk["cols"]
                d.text((ix, iy), C.clean_text(a), font=body(int(W*0.02), False), fill=INK, anchor="la")
                d.text((ix+iw, iy), C.clean_text(b), font=mono(int(W*0.016)), fill=ACC, anchor="ra")
                iy += int(H*0.058); d.line([(ix, iy-6), (ix+iw, iy-6)], fill=(255, 255, 255, 22), width=1)
            elif k == "bullet":
                if blk.get("check"): d.text((ix, iy), "✓", font=C.font("display-mid", int(W*0.02)), fill=ACC, anchor="la")
                d.text((ix+int(W*0.035), iy+2), C.clean_text(blk["text"]), font=body(int(W*0.02)), fill=INK, anchor="la")
                iy += int(H*0.07)
            elif k == "chips":
                cx = ix
                for c in blk["items"]:
                    cx = C.chip(d, cx, iy, C.clean_text(c), mono(int(W*0.014)), INK2, h=int(H*0.048))
                iy += int(H*0.075)
            elif k == "note":
                d.text((ix, iy), C.clean_text(blk.get("label", "")), font=C.font("display-mid", int(W*0.018)), fill=GREEN, anchor="la")
                d.text((ix+d.textlength(C.clean_text(blk.get("label","")), font=C.font("display-mid", int(W*0.018)))+16, iy+2),
                       C.clean_text(blk.get("text", "")), font=body(int(W*0.016), True), fill=INK2, anchor="la")
                iy += int(H*0.06)
            elif k == "kvhead":
                C.spaced(d, ix, iy, blk["text"].upper(), mono(int(W*0.013)), ACC, int(W*0.004), anchor="l"); iy += int(H*0.045)
            elif k == "text":
                d.text((ix, iy), C.clean_text(blk["text"]), font=body(int(W*0.016)), fill=INK, anchor="la"); iy += int(H*0.045)
        if spec.get("footer"):
            d.text((W//2, py1+int(H*0.05)), C.clean_text(spec["footer"]), font=C.font("display-mid", int(W*0.023)), fill=ACC, anchor="mm")

    return im

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenes", required=True)
    ap.add_argument("--brand", default="genie")
    ap.add_argument("--aspect", default="16:9", choices=list(SIZES))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    C.ensure_fonts()
    brand = C.load_brand(a.brand)
    size = SIZES[a.aspect]
    os.makedirs(a.out, exist_ok=True)
    scenes = json.load(open(a.scenes, encoding="utf-8"))
    for s in scenes:
        im = render(s, brand, size)
        im.save(os.path.join(a.out, f"s{s['id']}.png"))
    print(f"rendered {len(scenes)} overlays -> {a.out}")

if __name__ == "__main__":
    main()
