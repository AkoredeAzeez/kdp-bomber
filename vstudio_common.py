#!/usr/bin/env python3
"""
VIDEO STUDIO - shared engine (uapf-video-studio, MAX pack)
==========================================================
Fonts, brand kit, ffmpeg helpers, and the PIL scrim/caption primitives shared by
every video-studio script. No API keys are ever required by this module; stock
sourcing and narration live in their own scripts. Windows-safe (subprocess lists,
explicit ffmpeg discovery, utf-8 with replacement).
"""
import os, sys, json, shutil, subprocess, glob, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "assets", "fonts")
BRANDS = os.path.join(HERE, "assets", "brands")

# ---------------------------------------------------------------- ffmpeg ----
def _ff(name):
    p = shutil.which(name)
    if p:
        return p
    if os.name == "nt":
        for base in (os.environ.get("LOCALAPPDATA", ""),):
            hits = glob.glob(os.path.join(base, r"Microsoft\WinGet\Packages\*FFmpeg*\**", name + ".exe"), recursive=True)
            if hits:
                return hits[0]
    return name  # hope it's on PATH

FFMPEG = _ff("ffmpeg")
FFPROBE = _ff("ffprobe")

def run(cmd, timeout=1800):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError("ffmpeg failed:\n" + " ".join(str(c) for c in cmd[:8]) +
                           "\n" + (p.stderr or "")[-1600:])
    return p

def dur(path):
    p = subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    try:
        return float((p.stdout or "0").strip())
    except ValueError:
        return 0.0

# ----------------------------------------------------------------- fonts ----
# Google Fonts (OFL) raw TTFs, fetched once into assets/fonts.
_FONT_URLS = {
    "Figtree-VF.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/figtree/Figtree%5Bwght%5D.ttf",
    "InstrumentSans-VF.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/InstrumentSans%5Bwdth%2Cwght%5D.ttf",
    "InstrumentSans-Italic-VF.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/instrumentsans/InstrumentSans-Italic%5Bwdth%2Cwght%5D.ttf",
    "IBMPlexMono-Regular.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-Regular.ttf",
    "IBMPlexMono-Medium.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-Medium.ttf",
    "IBMPlexMono-SemiBold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-SemiBold.ttf",
    # editorial alternates (optional brands)
    "Fraunces-VF.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/fraunces/Fraunces%5BSOFT%2CWONK%2Copsz%2Cwght%5D.ttf",
}

def ensure_fonts():
    os.makedirs(FONTS, exist_ok=True)
    missing = []
    for name, url in _FONT_URLS.items():
        dest = os.path.join(FONTS, name)
        if os.path.exists(dest) and os.path.getsize(dest) > 5000:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=45) as r, open(dest, "wb") as f:
                f.write(r.read())
        except Exception as e:
            missing.append(f"{name}: {e}")
    return missing

def _var(path, size, axes):
    from PIL import ImageFont
    f = ImageFont.truetype(path, int(size))
    try:
        f.set_variation_by_axes(axes)
    except Exception:
        pass
    return f

def font(role, size, italic=False):
    """role: display (Figtree 900), body (Instrument Sans), mono, editorial (Fraunces)."""
    from PIL import ImageFont
    ensure_fonts()
    if role == "display":
        return _var(os.path.join(FONTS, "Figtree-VF.ttf"), size, [900])
    if role == "display-mid":
        return _var(os.path.join(FONTS, "Figtree-VF.ttf"), size, [700])
    if role == "body":
        fn = "InstrumentSans-Italic-VF.ttf" if italic else "InstrumentSans-VF.ttf"
        return _var(os.path.join(FONTS, fn), size, [100, 400])  # wdth, wght
    if role == "body-mid":
        return _var(os.path.join(FONTS, "InstrumentSans-VF.ttf"), size, [100, 500])
    if role == "editorial":
        return _var(os.path.join(FONTS, "Fraunces-VF.ttf"), size, [min(144, max(9, int(size*0.7))), 500, 0, 0])
    if role in ("mono", "mono-medium", "mono-semibold"):
        fn = {"mono": "IBMPlexMono-Regular.ttf", "mono-medium": "IBMPlexMono-Medium.ttf",
              "mono-semibold": "IBMPlexMono-SemiBold.ttf"}[role]
        return ImageFont.truetype(os.path.join(FONTS, fn), int(size))
    return ImageFont.truetype(os.path.join(FONTS, "InstrumentSans-VF.ttf"), int(size))

# ----------------------------------------------------------------- brand ----
def hexc(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

DEFAULT_BRAND = {
    "name": "Genie",
    "palette": {"ink": "#F4F7F8", "ink2": "#AEB9C4", "ink3": "#6C7A87",
                "accent": "#32E6E2", "accent2": "#7C5CFF", "green": "#4ADE80",
                "scrim": "#06070A", "panel": "#0F141A"},
    "fonts": {"display": "display", "body": "body", "mono": "mono-medium"},
    "pill_text": "#08100F",
}

def load_brand(name_or_path=None):
    if not name_or_path or name_or_path == "genie":
        b = dict(DEFAULT_BRAND)
    elif os.path.exists(name_or_path):
        b = json.load(open(name_or_path, encoding="utf-8"))
    else:
        cand = os.path.join(BRANDS, name_or_path + ".json")
        b = json.load(open(cand, encoding="utf-8")) if os.path.exists(cand) else dict(DEFAULT_BRAND)
    pal = {k: hexc(v) for k, v in b.get("palette", DEFAULT_BRAND["palette"]).items()}
    b["rgb"] = pal
    b["pill_text_rgb"] = hexc(b.get("pill_text", "#08100F"))
    return b

# ------------------------------------------------------ PIL primitives -------
def spaced(d, cx, y, txt, f, fill, tr, anchor="m"):
    ws = [d.textlength(c, font=f) for c in txt]
    total = sum(ws) + tr * (len(txt) - 1)
    x = cx - total / 2 if anchor == "m" else (cx if anchor == "l" else cx - total)
    for c, w in zip(txt, ws):
        d.text((x, y), c, font=f, fill=fill)
        x += w + tr

def fit_font(d, lines, role, base, tr, maxw):
    s = base
    while s > 14:
        f = font(role, s)
        if all(sum(d.textlength(c, font=f) for c in ln) + tr * (len(ln) - 1) <= maxw for ln in lines):
            return f, s
        s -= 2
    return font(role, 14), 14

def scrim_bottom(im, start=0.42, amax=238, scrim=(6, 7, 8)):
    from PIL import Image, ImageDraw
    W, H = im.size
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for y in range(H):
        if y > H * start:
            a = int(((y - H * start) / (H * (1 - start))) ** 1.25 * amax)
            d.line([(0, y), (W, y)], fill=scrim + (a,))
    return Image.alpha_composite(im, lay)

def scrim_top(im, amax=130, scrim=(6, 7, 8)):
    from PIL import Image, ImageDraw
    W, H = im.size
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for y in range(int(H * 0.34)):
        a = int((1 - y / (H * 0.34)) * amax)
        d.line([(0, y), (W, y)], fill=scrim + (a,))
    return Image.alpha_composite(im, lay)

def scrim_uniform(im, a=80, scrim=(6, 7, 8)):
    from PIL import Image
    return Image.alpha_composite(im, Image.new("RGBA", im.size, scrim + (a,)))

def scrim_center(im, a=214, scrim=(6, 7, 8)):
    from PIL import Image, ImageDraw, ImageFilter
    W, H = im.size
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cx, cy, mr = W // 2, int(H * 0.5), int(W * 0.62)
    for i in range(mr, 0, -3):
        d.ellipse([cx - i, cy - int(i * 0.62), cx + i, cy + int(i * 0.62)],
                  fill=scrim + (int(a * (1 - i / mr)),))
    return Image.alpha_composite(im, lay.filter(ImageFilter.GaussianBlur(60)))

def panel(im, box, a=214, r=22, panelc=(12, 13, 15), stroke=(255, 255, 255, 30)):
    from PIL import Image, ImageDraw
    lay = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle(box, radius=r, fill=panelc + (a,), outline=stroke, width=2)
    return Image.alpha_composite(im, lay)

def pill(d, cx, cy, text, f, fill, tcol):
    w = d.textlength(text, font=f)
    x0, x1 = cx - w / 2 - 34, cx + w / 2 + 34
    y0, y1 = cy - f.size * 0.82, cy + f.size * 0.92
    d.rounded_rectangle([x0, y0, x1, y1], radius=int((y1 - y0) / 2), fill=fill)
    d.text((cx, (y0 + y1) / 2), text, font=f, fill=tcol, anchor="mm")

def chip(d, x, y, text, f, tcol, h=52):
    w = d.textlength(text, font=f) + 46
    d.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, outline=(255, 255, 255, 55), width=2)
    d.text((x + 23, y + h // 2), text, font=f, fill=tcol, anchor="lm")
    return x + w + 18

# --------------------------------------------------------- text hygiene -----
def clean_text(s):
    """House rules: no em dash, no en dash ranges left raw, straight quotes kept."""
    if not s:
        return s
    return (s.replace("—", ", ").replace("–", " to ")
             .replace("  ", " ").strip())

if __name__ == "__main__":
    miss = ensure_fonts()
    print("ffmpeg:", FFMPEG)
    print("ffprobe:", FFPROBE)
    print("fonts dir:", FONTS)
    print("font issues:", miss or "none")
