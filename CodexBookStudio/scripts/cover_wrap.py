"""
KDP COVER WRAP ASSEMBLER - deterministic typography over AI artwork
====================================================================
Computes exact KDP paperback wrap dimensions (same formula as the official
KDP Cover Calculator) and composes a print-ready full-wrap cover at 300 DPI:
back cover + spine + front cover, with title/author/description typography
applied locally (never AI-rendered) and the barcode zone kept clear.

Usage:
  python kdp_cover_wrap.py config.json

config.json:
{
  "book_folder": "C:/path/to/book",
  "front_art": "cover_front_art.png",     // AI artwork, text-free
  "back_art": "cover_back_art.png",       // AI artwork, text-free (optional; falls back to spine_color)
  "trim_width_in": 8.5, "trim_height_in": 11.0,
  "page_count": 144,
  "paper": "bw_white",                    // bw_white | bw_cream | color
  "title": "Chair Yoga for Seniors",
  "subtitle": "Gentle 10-Minute Routines ...",
  "author": "Christopher J. Harvey",
  "back_text": "Back cover description ...",
  "spine_color": "#1B6B6B",
  "accent_color": "#E8614D",
  "output_prefix": "Chair_Yoga_for_Seniors_Cover"
}

Outputs in book_folder:  <prefix>_WRAP.png  and  <prefix>_WRAP.pdf (300 DPI)
Plus a dimensions report printed to stdout.
"""
import sys, json, os
from PIL import Image, ImageDraw, ImageFont

DPI = 300
BLEED_IN = 0.125
PAPER_THICKNESS = {"bw_white": 0.002252, "bw_cream": 0.0025, "color": 0.002347}
SPINE_TEXT_MIN_PAGES = 79          # KDP: spine text allowed from ~79 pages
BARCODE_W_IN, BARCODE_H_IN = 2.0, 1.2
BARCODE_MARGIN_IN = 0.25

def px(inches): return int(round(inches * DPI))

def load_font(size, bold=True):
    candidates = ([r"C:\Windows\Fonts\timesbd.ttf", r"C:\Windows\Fonts\georgiab.ttf"]
                  if bold else [r"C:\Windows\Fonts\times.ttf", r"C:\Windows\Fonts\georgia.ttf"])
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def wrap_text(draw, text, font, max_w):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w: line = t
        else:
            if line: lines.append(line)
            line = w
    if line: lines.append(line)
    return lines

def fit_title(draw, text, safe_w, trim_w):
    """Rule-19 title sizing: 36 to 90 pt (at 8.5x11 trim; scaled for other trims),
    the largest size whose FULL title fits in at most FOUR lines without breaking
    a word. Returns (font, lines, point_size)."""
    scale = trim_w / 8.5
    for pt in range(90, 35, -2):
        size = max(12, int(round(pt * scale * DPI / 72.0)))
        font = load_font(size)
        lines = wrap_text(draw, text, font, safe_w)
        if 0 < len(lines) <= 4 and all(draw.textlength(l, font=font) <= safe_w for l in lines):
            return font, lines, pt
    size = max(12, int(round(36 * scale * DPI / 72.0)))
    font = load_font(size)
    return font, wrap_text(draw, text, font, safe_w), 36


def fit_cover_art(art, target_w, target_h):
    """Scale-and-crop artwork to exactly fill the panel (cover-fit)."""
    ratio = max(target_w / art.width, target_h / art.height)
    art = art.resize((int(art.width * ratio) + 1, int(art.height * ratio) + 1), Image.LANCZOS)
    x = (art.width - target_w) // 2
    y = (art.height - target_h) // 2
    return art.crop((x, y, x + target_w, y + target_h))

def finish_mode(cfg_path, wrap_image):
    """--finish mode: ChatGPT produced the COMPLETE wrap design (art + text).
    This only scales it to exact KDP print dimensions and exports PNG + PDF.
    No creative changes are made."""
    cfg = json.loads(open(cfg_path, encoding="utf-8").read())
    folder = cfg["book_folder"]
    trim_w, trim_h = cfg["trim_width_in"], cfg["trim_height_in"]
    pages = cfg["page_count"]
    spine_in = pages * PAPER_THICKNESS[cfg.get("paper", "bw_white")]
    full_w_in = BLEED_IN + trim_w + spine_in + trim_w + BLEED_IN
    full_h_in = trim_h + 2 * BLEED_IN
    W, H = px(full_w_in), px(full_h_in)
    print(f"KDP wrap target: {full_w_in:.3f} x {full_h_in:.3f} in ({W} x {H} px @ {DPI} DPI); spine {spine_in:.3f} in")

    img = Image.open(os.path.join(folder, wrap_image)).convert("RGB")
    ar_src = img.width / img.height
    ar_dst = W / H
    drift = abs(ar_src - ar_dst) / ar_dst
    if drift > 0.03:
        print(f"WARNING: source aspect ratio differs from wrap by {drift*100:.1f}% - "
              "cover-fit crop will trim edges. If title/spine text sits near an edge, "
              "ask ChatGPT to regenerate at the correct proportions.")
    out = fit_cover_art(img, W, H)
    prefix = cfg.get("output_prefix", "Cover")
    png_path = os.path.join(folder, prefix + "_WRAP.png")
    pdf_path = os.path.join(folder, prefix + "_WRAP.pdf")
    out.save(png_path, dpi=(DPI, DPI))
    out.save(pdf_path, "PDF", resolution=DPI)
    print("saved", png_path)
    print("saved", pdf_path)

def main():
    if len(sys.argv) >= 4 and sys.argv[1] == "--finish":
        finish_mode(sys.argv[2], sys.argv[3])
        return
    cfg = json.loads(open(sys.argv[1], encoding="utf-8").read())
    folder = cfg["book_folder"]
    trim_w, trim_h = cfg["trim_width_in"], cfg["trim_height_in"]
    pages = cfg["page_count"]
    spine_in = pages * PAPER_THICKNESS[cfg.get("paper", "bw_white")]
    full_w_in = BLEED_IN + trim_w + spine_in + trim_w + BLEED_IN
    full_h_in = trim_h + 2 * BLEED_IN

    W, H = px(full_w_in), px(full_h_in)
    spine_px = px(spine_in)
    back_x0 = 0
    spine_x0 = px(BLEED_IN + trim_w)
    front_x0 = spine_x0 + spine_px

    print(f"KDP wrap dimensions: {full_w_in:.3f} x {full_h_in:.3f} in  "
          f"({W} x {H} px @ {DPI} DPI); spine {spine_in:.3f} in ({spine_px} px)")

    teal = hex_rgb(cfg.get("spine_color", "#1B6B6B"))
    accent = hex_rgb(cfg.get("accent_color", "#E8614D"))
    canvas = Image.new("RGB", (W, H), teal)
    draw = ImageDraw.Draw(canvas)

    # -- Front cover: artwork + typography ------------------------------------
    front_w = W - front_x0
    art = Image.open(os.path.join(folder, cfg["front_art"])).convert("RGB")
    canvas.paste(fit_cover_art(art, front_w, H), (front_x0, 0))
    draw = ImageDraw.Draw(canvas)

    # Title block, upper front: size chosen by rule 19 (36-90 pt, max 4 lines,
    # exact wording, never break a word), band sized to fit the block.
    safe_w = front_w - px(1.0)
    f_title, title_lines, title_pt = fit_title(draw, cfg["title"], safe_w, trim_w)
    line_h = int(f_title.size * 1.14)
    f_sub = load_font(max(px(0.16), int(f_title.size * 0.30)), bold=False)
    f_auth = load_font(px(0.26))
    sub_lines = wrap_text(draw, cfg.get("subtitle", ""), f_sub, safe_w)[:3]
    sub_h = int(f_sub.size * 1.3)
    pad = px(0.25)
    band_h = pad + len(title_lines) * line_h + (len(sub_lines) * sub_h + px(0.10) if sub_lines else 0) + pad
    print(f"title: {title_pt} pt across {len(title_lines)} line(s)")
    band = Image.new("RGBA", (front_w, band_h), teal + (216,))
    canvas.paste(Image.alpha_composite(
        canvas.crop((front_x0, px(0.6), W, px(0.6) + band_h)).convert("RGBA"), band).convert("RGB"),
        (front_x0, px(0.6)))
    draw = ImageDraw.Draw(canvas)

    cx = front_x0 + front_w // 2
    y = px(0.6) + pad
    for line in title_lines:
        lw = draw.textlength(line, font=f_title)
        draw.text((cx - lw / 2, y), line, font=f_title, fill=(255, 255, 255))
        y += line_h
    if sub_lines:
        y += px(0.10)
        for line in sub_lines:
            lw = draw.textlength(line, font=f_sub)
            draw.text((cx - lw / 2, y), line, font=f_sub, fill=(255, 240, 235))
            y += sub_h
    # Author band bottom front
    ab_h = px(0.7)
    draw.rectangle([front_x0, H - px(0.5) - ab_h, W, H - px(0.5)], fill=accent)
    at = cfg["author"]
    lw = draw.textlength(at, font=f_auth)
    draw.text((cx - lw / 2, H - px(0.5) - ab_h + px(0.18)), at, font=f_auth, fill=(255, 255, 255))

    # -- Back cover: artwork or solid + description ---------------------------
    back_w = spine_x0
    if cfg.get("back_art") and os.path.exists(os.path.join(folder, cfg["back_art"])):
        bart = Image.open(os.path.join(folder, cfg["back_art"])).convert("RGB")
        canvas.paste(fit_cover_art(bart, back_w, H), (0, 0))
        draw = ImageDraw.Draw(canvas)
        # Legibility panel over back art
        panel = Image.new("RGBA", (back_w - px(1.2), H - px(3.0)), (255, 255, 255, 235))
        canvas.paste(Image.alpha_composite(
            canvas.crop((px(0.6), px(0.9), px(0.6) + panel.width, px(0.9) + panel.height)).convert("RGBA"),
            panel).convert("RGB"), (px(0.6), px(0.9)))
        draw = ImageDraw.Draw(canvas)
        text_fill = (26, 26, 26)
    else:
        text_fill = (255, 255, 255)

    f_back = load_font(px(0.155), bold=False)
    f_backhead = load_font(px(0.22))
    bx, by = px(0.95), px(1.2)
    back_safe_w = back_w - px(1.9)
    head = cfg.get("back_headline", cfg["title"])
    for line in wrap_text(draw, head, f_backhead, back_safe_w):
        draw.text((bx, by), line, font=f_backhead, fill=hex_rgb(cfg.get("accent_color", "#E8614D")))
        by += px(0.28)
    by += px(0.15)
    for para in cfg["back_text"].split("\n"):
        for line in wrap_text(draw, para, f_back, back_safe_w):
            draw.text((bx, by), line, font=f_back, fill=text_fill)
            by += px(0.21)
        by += px(0.12)

    # Barcode clear zone (bottom-right of back cover). NO white patch
    # (operator directive 2026-08-29): KDP lays its own white barcode there at
    # print time, so painting white just scars the design. The zone is still
    # kept CLEAR of text and critical elements, filled with a calm tone drawn
    # from the surrounding back-cover design (or cfg barcode_zone_color) so
    # the wrap reads as one design.
    bz_x1 = spine_x0 - px(BARCODE_MARGIN_IN)
    bz_y1 = H - px(BLEED_IN) - px(BARCODE_MARGIN_IN)
    bz_box = [bz_x1 - px(BARCODE_W_IN), bz_y1 - px(BARCODE_H_IN), bz_x1, bz_y1]
    if cfg.get("barcode_zone_color"):
        zone_fill = hex_rgb(cfg["barcode_zone_color"])
    else:
        region = canvas.crop([int(v) for v in bz_box]).resize((8, 8))
        samples = list(region.getdata())
        zone_fill = tuple(sum(c[i] for c in samples) // len(samples) for i in range(3))
    draw.rectangle(bz_box, fill=zone_fill)

    # -- Spine ----------------------------------------------------------------
    draw.rectangle([spine_x0, 0, front_x0, H], fill=teal)
    if pages >= SPINE_TEXT_MIN_PAGES and spine_in >= 0.25:
        stxt = cfg["title"] + "   -   " + cfg["author"]
        simg = Image.new("RGBA", (px(trim_h - 1.0), spine_px), (0, 0, 0, 0))
        sd = ImageDraw.Draw(simg)
        # Shrink to fit the spine length; drop the author before going tiny.
        size = min(px(0.16), int(spine_px * 0.55))
        while size > px(0.08) and sd.textlength(stxt, font=load_font(size)) > simg.width:
            size -= 2
        if sd.textlength(stxt, font=load_font(size)) > simg.width:
            stxt = cfg["title"]
            while size > px(0.06) and sd.textlength(stxt, font=load_font(size)) > simg.width:
                size -= 2
        sf = load_font(size)
        slw = sd.textlength(stxt, font=sf)
        sd.text((max(0, (simg.width - slw) / 2), (spine_px - sf.size) / 2 - px(0.01)),
                stxt, font=sf, fill=(255, 255, 255))
        simg = simg.rotate(-90, expand=True)
        canvas.paste(simg, (spine_x0, (H - simg.height) // 2), simg)
    else:
        print(f"NOTE: spine text omitted (pages={pages}, spine={spine_in:.3f} in) per KDP rules")

    prefix = cfg.get("output_prefix", "Cover")
    png_path = os.path.join(folder, prefix + "_WRAP.png")
    pdf_path = os.path.join(folder, prefix + "_WRAP.pdf")
    canvas.save(png_path, dpi=(DPI, DPI))
    canvas.save(pdf_path, "PDF", resolution=DPI)
    print("saved", png_path)
    print("saved", pdf_path)

if __name__ == "__main__":
    main()
