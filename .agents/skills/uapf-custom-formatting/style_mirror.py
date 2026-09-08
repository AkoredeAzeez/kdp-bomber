#!/usr/bin/env python3
"""
STYLE MIRROR - uapf-custom-formatting
=====================================
Extracts the complete formatting fingerprint of a book the client uploads
(DOCX preferred; PDF supported) and saves it as the niche's custom formatting
profile, so every future book in that niche is formatted to the same SYSTEM.

  python style_mirror.py --file book.docx --niche cookbook [--out-dir state/custom_formatting]
  python style_mirror.py --file book.pdf  --niche selfhelp

THE MIRROR LAW (binding):
  MIRRORED: structure and rhythm - trim, margins, body font family + size,
  line spacing, alignment, the heading scale (sizes, case, alignment, weight),
  chapter-opener pattern, unit anatomy and label vocabulary, table style class,
  callout/panel usage, image density, front/back matter order, TOC depth.
  NEVER MIRRORED: the exact color palette (only a palette DIRECTION is
  recorded), artwork, motifs, cover identity, and any text. No-Two-Books-Alike
  still governs every book produced under the profile: each gets its own
  concrete palette, motifs, and arrangement INSIDE the mirrored system, and the
  book-fingerprint uniqueness check still applies. The premium interior law
  still binds: if the uploaded book is plain black-on-white, its structure is
  mirrored and executed with the premium color system.
"""
import argparse, json, os, re, sys
from collections import Counter
from datetime import date

def _emu_to_in(v):  # python-docx returns EMU for section dims
    return round(v / 914400, 2) if v else None

def extract_docx(path):
    from docx import Document
    from docx.oxml.ns import qn
    doc = Document(path)
    prof = {}

    # trim + margins from the last section
    sec = doc.sections[-1]
    prof["trim"] = f'{_emu_to_in(sec.page_width)} x {_emu_to_in(sec.page_height)} in'
    prof["margins_in"] = {"top": _emu_to_in(sec.top_margin), "bottom": _emu_to_in(sec.bottom_margin),
                          "left": _emu_to_in(sec.left_margin), "right": _emu_to_in(sec.right_margin)}

    body_fonts, body_sizes, spacings, aligns = Counter(), Counter(), Counter(), Counter()
    head = {1: [], 2: [], 3: []}
    labels = Counter()
    h1_seq = []
    img_count = 0
    para_count = 0
    opener_after_h1 = Counter()
    last_was_h1 = False
    LABEL_RE = re.compile(r'^(Materials|Tools|Skill Level|Difficulty|Time|Yarn|Hook|Gauge|Finished Size|Abbreviations|Instructions|Assembly|Finishing|Pattern Notes|Notes|Tip|Variation|Ingredients|Directions|Prep Time|Cook Time|Serves|Yield|Step \d+|Row \d+|Round \d+)\b[: ]', re.I)

    for p in doc.paragraphs:
        t = (p.text or "").strip()
        st = (p.style.name if p.style is not None else "") or ""
        if 'graphic' in p._p.xml or '<w:drawing' in p._p.xml:
            img_count += 1
            if last_was_h1:
                opener_after_h1["image"] += 1
        lvl = None
        if st.startswith("Heading"):
            try: lvl = int(re.sub(r'\D', '', st) or 9)
            except ValueError: lvl = None
        if lvl in (1, 2, 3) and t:
            sizes = [r.font.size.pt for r in p.runs if r.font.size]
            if not sizes and p.style is not None and p.style.font.size:
                sizes = [p.style.font.size.pt]  # size defined on the style, not the runs
            case = "BLOCK CAPS" if t == t.upper() and any(c.isalpha() for c in t) else (
                   "Title Case" if t.istitle() else "Sentence case")
            head[lvl].append({"size": max(sizes) if sizes else None, "case": case,
                              "align": str(p.alignment or "LEFT").split('.')[-1].split(' ')[0],
                              "bold": all(r.bold for r in p.runs if r.text.strip()) if p.runs else None})
            if lvl == 1:
                h1_seq.append(t[:70])
                last_was_h1 = True
                continue
        if t and lvl is None:
            para_count += 1
            m = LABEL_RE.match(t)
            if m: labels[re.sub(r'\d+', 'N', m.group(1).title())] += 1
            for r in p.runs:
                if r.text.strip():
                    if r.font.name: body_fonts[r.font.name] += 1
                    if r.font.size: body_sizes[round(r.font.size.pt, 1)] += 1
            pf = p.paragraph_format
            if pf.line_spacing: spacings[round(float(pf.line_spacing), 2)] += 1
            aligns[str(p.alignment).split('.')[-1].split(' ')[0] if p.alignment else "LEFT"] += 1
            if last_was_h1:
                opener_after_h1["prose"] += 1
        if t:
            last_was_h1 = lvl == 1

    def top(c, default=None):
        return c.most_common(1)[0][0] if c else default

    def head_summary(lst):
        if not lst: return None
        sizes = [h["size"] for h in lst if h["size"]]
        cases = Counter(h["case"] for h in lst)
        aligns_ = Counter(h["align"] for h in lst)
        return {"count": len(lst), "size_pt": max(set(sizes), key=sizes.count) if sizes else None,
                "case": top(cases), "align": top(aligns_)}

    prof["body_font"] = top(body_fonts, "Times New Roman")
    prof["body_size_pt"] = top(body_sizes, 12)
    prof["line_spacing"] = top(spacings, 1.15)
    prof["alignment"] = (top(aligns, "LEFT") or "LEFT").lower()
    prof["headings"] = {f"h{l}": head_summary(head[l]) for l in (1, 2, 3)}
    prof["chapter_opener"] = ("hero image after the chapter title"
                              if opener_after_h1.get("image", 0) >= max(1, opener_after_h1.get("prose", 0))
                              else "styled text opening (no hero image)")
    prof["unit_labels"] = [k for k, _ in labels.most_common(12)]
    prof["image_density"] = round(img_count / max(1, para_count), 3)
    prof["images_total"] = img_count
    prof["front_matter_seq"] = h1_seq[:6]
    prof["back_matter_seq"] = h1_seq[-4:] if len(h1_seq) > 6 else []
    prof["chapters_h1_total"] = len(h1_seq)

    tables = doc.tables
    shaded = 0
    for tb in tables[:20]:
        if '<w:shd' in tb._tbl.xml:
            shaded += 1
    prof["tables"] = {"count": len(tables),
                      "style_class": "shaded headers / tinted rows" if shaded else "plain grid"}
    # tinted callout approximation: shaded single-cell tables or shaded paragraphs
    prof["callout_style"] = "tinted panels present" if shaded else "minimal panels"
    return prof

def extract_pdf(path):
    import fitz
    doc = fitz.open(path)
    prof = {}
    pg = doc[min(5, doc.page_count - 1)]
    w, h = pg.rect.width / 72, pg.rect.height / 72
    prof["trim"] = f"{round(w,2)} x {round(h,2)} in"
    sizes, fonts = Counter(), Counter()
    img_pages = 0
    for i in range(min(40, doc.page_count)):
        page = doc[i]
        if page.get_images(): img_pages += 1
        for b in page.get_text("dict").get("blocks", []):
            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    if s.get("text", "").strip():
                        sizes[round(s["size"], 1)] += len(s["text"])
                        fonts[s["font"]] += len(s["text"])
    body = sizes.most_common(1)[0][0] if sizes else 12
    prof["body_size_pt"] = body
    prof["body_font"] = (fonts.most_common(1)[0][0].split("-")[0].split("+")[-1]) if fonts else "unknown"
    bigger = sorted({s for s, _ in sizes.items() if s >= body * 1.5}, reverse=True)
    prof["headings"] = {"h1": {"size_pt": bigger[0]} if bigger else None,
                        "h2": {"size_pt": bigger[1]} if len(bigger) > 1 else None}
    prof["image_density_pages"] = round(img_pages / max(1, min(40, doc.page_count)), 2)
    prof["pages"] = doc.page_count
    prof["note"] = "PDF extraction is approximate; upload the DOCX for the full fingerprint."
    return prof

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--niche", required=True)
    ap.add_argument("--out-dir", default=os.path.join("state", "custom_formatting"))
    a = ap.parse_args()
    if not os.path.exists(a.file):
        sys.exit("file not found: " + a.file)
    ext = os.path.splitext(a.file)[1].lower()
    if ext == ".docx":
        mirror = extract_docx(a.file)
    elif ext == ".pdf":
        mirror = extract_pdf(a.file)
    else:
        sys.exit("upload a .docx (best) or .pdf")

    profile = {
        "niche": a.niche,
        "mode": "mirrored",
        "mirrored_from": os.path.basename(a.file),
        "saved": str(date.today()),
        "body_font": mirror.get("body_font"),
        "body_size_pt": mirror.get("body_size_pt"),
        "line_spacing": mirror.get("line_spacing"),
        "alignment": mirror.get("alignment"),
        "palette_direction": "DERIVE per book (exact palette is never mirrored; No-Two-Books-Alike)",
        "mirror": mirror,
        "laws": "premium interior, type floors, containment, N2BA all still bind; this profile mirrors STRUCTURE only",
    }
    os.makedirs(a.out_dir, exist_ok=True)
    out = os.path.join(a.out_dir, f"{a.niche}.json")
    json.dump(profile, open(out, "w", encoding="utf-8"), indent=1)
    print(f"MIRRORED PROFILE SAVED: {out}")
    print(f"  source: {profile['mirrored_from']}")
    print(f"  trim: {mirror.get('trim')}  margins: {mirror.get('margins_in')}")
    print(f"  body: {mirror.get('body_font')} {mirror.get('body_size_pt')}pt, spacing {mirror.get('line_spacing')}, {mirror.get('alignment')}")
    print(f"  headings: {json.dumps(mirror.get('headings'))[:180]}")
    print(f"  opener: {mirror.get('chapter_opener')}")
    print(f"  unit labels: {', '.join(mirror.get('unit_labels', [])[:8]) or 'n/a'}")
    print(f"  tables: {mirror.get('tables')}  callouts: {mirror.get('callout_style')}")
    print(f"  image density: {mirror.get('image_density', mirror.get('image_density_pages'))}")
    print("Palette, motifs, and artwork are NOT mirrored: each book gets its own")
    print("unique premium palette inside this structure (No-Two-Books-Alike).")

if __name__ == "__main__":
    main()
