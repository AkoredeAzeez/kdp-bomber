#!/usr/bin/env python3
"""
A+ ASSEMBLE  (Codex Book Studio)
================================
Composes Amazon A+ content modules into 970x600 masters: generated art plus a
locally rendered headline and body (text is never baked into the AI art). Two
layouts: "split" (art on one side, text panel on the other) and "banner" (art
full-bleed with a legibility panel).

Usage:
  python aplus_assemble.py manifest.json

manifest.json:
{
  "out_dir": "aplus",
  "accent_hex": "1B6B6B",
  "modules": [
    {"art": "mod1.png", "headline": "One clear benefit",
     "body": "One or two lines drawn from the book.", "layout": "split", "art_side": "left"}
  ]
}
Outputs out_dir/aplus_01.png ... at exactly 970x600. Requires Pillow.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 970, 600


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def font(size, bold=True):
    cands = ([r"C:\Windows\Fonts\georgiab.ttf", r"C:\Windows\Fonts\timesbd.ttf"]
             if bold else [r"C:\Windows\Fonts\georgia.ttf", r"C:\Windows\Fonts\times.ttf"])
    for c in cands:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            line = t
        else:
            if line:
                lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def fit(art, tw, th):
    ratio = max(tw / art.width, th / art.height)
    art = art.resize((int(art.width * ratio) + 1, int(art.height * ratio) + 1), Image.LANCZOS)
    x = (art.width - tw) // 2
    y = (art.height - th) // 2
    return art.crop((x, y, x + tw, y + th))


def draw_text_block(draw, x, y, headline, body, accent, text_col, max_w):
    fh = font(40); fb = font(22, bold=False)
    for line in wrap(draw, headline, fh, max_w):
        draw.text((x, y), line, font=fh, fill=accent)
        y += 48
    y += 12
    for para in body.split("\n"):
        for line in wrap(draw, para, fb, max_w):
            draw.text((x, y), line, font=fb, fill=text_col)
            y += 30
        y += 8


def compose(mod, base, accent):
    layout = mod.get("layout", "split")
    raw_art = mod.get("art", "")
    art_path = raw_art
    if raw_art and not os.path.isabs(art_path):
        art_path = os.path.join(base, art_path)
    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    have_art = bool(raw_art) and os.path.exists(art_path)

    if layout == "banner":
        if have_art:
            canvas.paste(fit(Image.open(art_path).convert("RGB"), W, H), (0, 0))
        panel = Image.new("RGBA", (W - 80, 210), (255, 255, 255, 232))
        canvas.paste(Image.alpha_composite(
            canvas.crop((40, H - 250, 40 + panel.width, H - 250 + panel.height)).convert("RGBA"),
            panel).convert("RGB"), (40, H - 250))
        draw = ImageDraw.Draw(canvas)
        draw_text_block(draw, 70, H - 230, mod.get("headline", ""), mod.get("body", ""),
                        accent, (26, 26, 26), W - 180)
    else:  # split
        art_side = mod.get("art_side", "left")
        art_w = 430
        if have_art:
            fitted = fit(Image.open(art_path).convert("RGB"), art_w, H)
            canvas.paste(fitted, (0 if art_side == "left" else W - art_w, 0))
        tx = art_w + 45 if art_side == "left" else 45
        draw_text_block(draw, tx, 90, mod.get("headline", ""), mod.get("body", ""),
                        accent, (30, 30, 30), W - art_w - 90)
    return canvas


def main():
    if len(sys.argv) < 2:
        print("usage: python aplus_assemble.py manifest.json"); sys.exit(1)
    cfg = json.load(open(sys.argv[1], encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    accent = hexrgb(cfg.get("accent_hex", "1B6B6B"))
    out_dir = cfg.get("out_dir", "aplus")
    if not os.path.isabs(out_dir):
        out_dir = os.path.join(base, out_dir)
    os.makedirs(out_dir, exist_ok=True)
    for i, mod in enumerate(cfg.get("modules", []), 1):
        img = compose(mod, base, accent)
        p = os.path.join(out_dir, f"aplus_{i:02d}.png")
        img.save(p, dpi=(72, 72))
        print(f"saved {p} (970x600)")


if __name__ == "__main__":
    main()
