#!/usr/bin/env python3
"""
BOOK ASSEMBLE  (Codex Book Studio)
==================================
Assembles a premium KDP-ready DOCX from a manifest the agent generates. Handles
styled chapter openers, a colored typographic system, body copy, styled/shaded
tables, images inside the margins with captions, and question/answer sections
with answers placed AFTER the questions (house rule).

Usage:
  python book_assemble.py manifest.json out.docx

manifest.json:
{
  "title": "...", "author": "...",
  "trim_width_in": 6.0, "trim_height_in": 9.0,
  "accent_hex": "1B6B6B",
  "chapters": [
    {"title": "Chapter 1: Getting Started", "blocks": [
      {"type": "p",  "text": "A paragraph."},
      {"type": "h2", "text": "A sub-heading"},
      {"type": "list", "items": ["one", "two"]},
      {"type": "table", "caption": "Table 1.1 Comparison", "rows": [["A","B"],["1","2"]], "header": true},
      {"type": "image", "path": "fig1.png", "caption": "Figure 1.1 A diagram", "width_in": 4.5},
      {"type": "qa", "questions": ["Q1 ...","Q2 ..."], "answers": ["A1 ...","A2 ..."]}
    ]}
  ]
}
Requires python-docx.
"""
import json, sys, os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def hexrgb(h):
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def shade_cell(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor.lstrip("#"))
    tcPr.append(shd)


def set_page(section, w_in, h_in):
    section.page_width = Inches(w_in)
    section.page_height = Inches(h_in)
    m = Inches(0.75)
    section.top_margin = section.bottom_margin = m
    section.left_margin = section.right_margin = m
    section.gutter = Inches(0.13)


def main():
    if len(sys.argv) < 3:
        print("usage: python book_assemble.py manifest.json out.docx"); sys.exit(1)
    cfg = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    base = os.path.dirname(os.path.abspath(sys.argv[1]))
    accent = hexrgb(cfg.get("accent_hex", "1B6B6B"))
    tw, th = cfg.get("trim_width_in", 6.0), cfg.get("trim_height_in", 9.0)

    doc = Document()
    set_page(doc.sections[0], tw, th)
    normal = doc.styles["Normal"]
    normal.font.name = "Georgia"
    normal.font.size = Pt(11)

    # Title page
    tp = doc.add_paragraph(); tp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = tp.add_run(cfg.get("title", "Untitled")); r.bold = True; r.font.size = Pt(30)
    r.font.color.rgb = accent
    if cfg.get("author"):
        ap = doc.add_paragraph(); ap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ar = ap.add_run(cfg["author"]); ar.font.size = Pt(15)
    doc.add_page_break()

    content_w = tw - 1.5  # inside margins

    for ci, ch in enumerate(cfg.get("chapters", []), 1):
        # Styled chapter opener
        op = doc.add_paragraph()
        orun = op.add_run(ch.get("title", f"Chapter {ci}"))
        orun.bold = True; orun.font.size = Pt(20); orun.font.color.rgb = accent
        bar = doc.add_paragraph()
        pPr = bar._p.get_or_add_pPr()
        pbdr = OxmlElement("w:pBdr"); bottom = OxmlElement("w:bottom")
        bottom.set(qn("w:val"), "single"); bottom.set(qn("w:sz"), "18")
        bottom.set(qn("w:space"), "1"); bottom.set(qn("w:color"), str(accent))
        pbdr.append(bottom); pPr.append(pbdr)

        for blk in ch.get("blocks", []):
            t = blk.get("type")
            if t == "p":
                doc.add_paragraph(blk.get("text", ""))
            elif t == "h2":
                p = doc.add_paragraph(); rn = p.add_run(blk.get("text", ""))
                rn.bold = True; rn.font.size = Pt(14); rn.font.color.rgb = accent
            elif t == "list":
                for it in blk.get("items", []):
                    doc.add_paragraph(str(it), style="List Bullet")
            elif t == "table":
                rows = blk.get("rows", [])
                if rows:
                    tbl = doc.add_table(rows=len(rows), cols=len(rows[0]))
                    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
                    tbl.style = "Table Grid"
                    for ri, row in enumerate(rows):
                        for cix, val in enumerate(row):
                            cell = tbl.cell(ri, cix)
                            cell.text = str(val)
                            if ri == 0 and blk.get("header"):
                                shade_cell(cell, str(accent))
                                for pr in cell.paragraphs:
                                    for rr in pr.runs:
                                        rr.bold = True
                                        rr.font.color.rgb = RGBColor(255, 255, 255)
                    if blk.get("caption"):
                        cap = doc.add_paragraph(); cr = cap.add_run(blk["caption"])
                        cr.italic = True; cr.font.size = Pt(9)
            elif t == "image":
                path = blk.get("path", "")
                if not os.path.isabs(path):
                    path = os.path.join(base, path)
                if os.path.exists(path):
                    ip = doc.add_paragraph(); ip.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    w = min(blk.get("width_in", content_w), content_w)
                    ip.add_run().add_picture(path, width=Inches(w))
                    if blk.get("caption"):
                        cap = doc.add_paragraph(); cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        cr = cap.add_run(blk["caption"]); cr.italic = True; cr.font.size = Pt(9)
                else:
                    doc.add_paragraph(f"[missing image: {blk.get('path')}]")
            elif t == "qa":
                # Questions first, then a single Answers section (house rule).
                qh = doc.add_paragraph(); qr = qh.add_run("Questions")
                qr.bold = True; qr.font.color.rgb = accent
                for i, q in enumerate(blk.get("questions", []), 1):
                    doc.add_paragraph(f"{i}. {q}")
                ans = blk.get("answers", [])
                if ans:
                    ah = doc.add_paragraph(); arn = ah.add_run("Answers")
                    arn.bold = True; arn.font.color.rgb = accent
                    for i, a in enumerate(ans, 1):
                        doc.add_paragraph(f"{i}. {a}")
        doc.add_page_break()

    doc.save(out)
    print(f"saved {out} ({len(cfg.get('chapters', []))} chapters)")


if __name__ == "__main__":
    main()
