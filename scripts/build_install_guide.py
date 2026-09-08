#!/usr/bin/env python3
r"""Build GENIE_INSTALLATION_GUIDE.docx + .pdf from GENIE_INSTALLATION_GUIDE.md.

Handles headings, bold/code inline marks, numbered/bulleted lists, quotes,
code fences, and image lines of the form ![alt](guide_images/name.png)
(images render centered at 5.8in with a small caption). Rerun after any edit
to the .md (and scripts/gen_guide_images.py first if the graphics changed);
the factory ships the PDF with every new client delivery.
"""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "GENIE_INSTALLATION_GUIDE.md")
DOCX = os.path.join(HERE, "GENIE_INSTALLATION_GUIDE.docx")
PDF = os.path.join(HERE, "GENIE_INSTALLATION_GUIDE.pdf")
PRIN = RGBColor(0x1F, 0x4E, 0x5F)
ACC = RGBColor(0xC8, 0x87, 0x3F)
GRAY = RGBColor(0x77, 0x77, 0x77)

d = Document()
st = d.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(11)
for s in d.sections:
    s.left_margin = s.right_margin = Inches(0.9)


def add_runs(p, text, base_size=11, color=None, bold=False):
    for part in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = p.add_run(part[1:-1])
            r.font.name = "Consolas"; r.font.color.rgb = PRIN; r.bold = True
        else:
            r = p.add_run(part)
        r.font.size = Pt(base_size)
        if bold:
            r.bold = True
        if color is not None:
            r.font.color.rgb = color


lines = open(SRC, encoding="utf-8").read().splitlines()
i = 0
while i < len(lines):
    ln = lines[i]
    img_m = re.match(r"^!\[(.*)\]\((.+)\)\s*$", ln)
    if ln.startswith("# "):
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(ln[2:]); r.bold = True; r.font.size = Pt(24); r.font.color.rgb = PRIN
    elif ln.startswith("#### ") or ln.startswith("### ") and lines[0].startswith("# ") and i < 4:
        p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(ln.lstrip("# ")); r.italic = True; r.font.size = Pt(13); r.font.color.rgb = ACC
    elif ln.startswith("### "):
        p = d.add_paragraph(); p.space_before = Pt(10)
        r = p.add_run(ln[4:]); r.bold = True; r.font.size = Pt(12.5); r.font.color.rgb = ACC
    elif ln.startswith("## "):
        p = d.add_paragraph(); p.space_before = Pt(14)
        r = p.add_run(ln[3:]); r.bold = True; r.font.size = Pt(15); r.font.color.rgb = PRIN
    elif img_m:
        alt, rel = img_m.groups()
        path = os.path.join(HERE, rel.replace("/", os.sep))
        if os.path.exists(path):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(path, width=Inches(5.8))
            if alt:
                cp = d.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = cp.add_run(alt); r.italic = True; r.font.size = Pt(9); r.font.color.rgb = GRAY
    elif ln.strip() == "---":
        pass
    elif ln.startswith("> "):
        p = d.add_paragraph(); p.paragraph_format.left_indent = Inches(0.35)
        add_runs(p, ln[2:], 10.5, ACC)
    elif re.match(r"^\s*\d+\.\s", ln) or re.match(r"^\s*-\s", ln):
        m = re.match(r"^(\s*)(\d+\.|-)\s(.*)$", ln)
        indent, marker, body = m.groups()
        while (i + 1 < len(lines) and lines[i + 1].startswith("   ")
               and not re.match(r"^\s*(\d+\.|-)\s", lines[i + 1])
               and lines[i + 1].strip() and not lines[i + 1].strip().startswith("`")):
            body += " " + lines[i + 1].strip(); i += 1
        p = d.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.3 + 0.25 * (len(indent) // 3))
        p.paragraph_format.space_after = Pt(4)
        pre = p.add_run(("%s " % marker) if marker != "-" else "• ")
        pre.bold = True; pre.font.color.rgb = ACC; pre.font.size = Pt(11)
        add_runs(p, body)
    elif ln.strip().startswith("`") and ln.strip().endswith("`") and len(ln.strip()) > 2:
        p = d.add_paragraph(); p.paragraph_format.left_indent = Inches(0.45)
        r = p.add_run(ln.strip().strip("`"))
        r.font.name = "Consolas"; r.font.size = Pt(11); r.bold = True; r.font.color.rgb = PRIN
    elif ln.strip() == "```":
        i += 1; buf = []
        while i < len(lines) and lines[i].strip() != "```":
            buf.append(lines[i]); i += 1
        for c in buf:
            p = d.add_paragraph(); p.paragraph_format.left_indent = Inches(0.45)
            r = p.add_run(c.strip())
            r.font.name = "Consolas"; r.font.size = Pt(11); r.bold = True; r.font.color.rgb = PRIN
    elif ln.strip():
        body = ln.strip()
        while (i + 1 < len(lines) and lines[i + 1].strip()
               and not lines[i + 1].startswith(("#", ">", "-", "`", "!"))
               and not re.match(r"^\s*(\d+\.|-)\s", lines[i + 1])
               and lines[i + 1].strip() != "---"):
            body += " " + lines[i + 1].strip(); i += 1
        p = d.add_paragraph(); p.paragraph_format.space_after = Pt(6)
        add_runs(p, body)
    i += 1

d.save(DOCX)
print("docx saved:", DOCX)


def pdf_via_reportlab():
    """Word-free PDF render of the same Markdown (Community Edition builds on
    machines without Word or LibreOffice)."""
    from xml.sax.saxutils import escape
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib import colors
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                    KeepTogether)

    prin, acc, gray = colors.HexColor("#1F4E5F"), colors.HexColor("#C8873F"), colors.HexColor("#777777")
    S = {
        "title": ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=prin, alignment=1, spaceAfter=4),
        "sub": ParagraphStyle("s", fontName="Helvetica-Oblique", fontSize=12.5, leading=16, textColor=acc, alignment=1, spaceAfter=10),
        "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=prin, spaceBefore=14, spaceAfter=6),
        "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=12.5, leading=16, textColor=acc, spaceBefore=10, spaceAfter=4),
        "body": ParagraphStyle("b", fontName="Helvetica", fontSize=11, leading=15, spaceAfter=6),
        "quote": ParagraphStyle("q", fontName="Helvetica", fontSize=10.5, leading=14, textColor=acc, leftIndent=0.35 * inch, spaceAfter=6),
        "code": ParagraphStyle("c", fontName="Courier-Bold", fontSize=10.5, leading=14, textColor=prin, leftIndent=0.45 * inch, spaceAfter=4),
        "cap": ParagraphStyle("cap", fontName="Helvetica-Oblique", fontSize=9, leading=12, textColor=gray, alignment=1, spaceAfter=8),
    }

    def inline(text):
        out = []
        for part in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
            if not part:
                continue
            if part.startswith("**") and part.endswith("**"):
                out.append("<b>%s</b>" % escape(part[2:-2]))
            elif part.startswith("`") and part.endswith("`"):
                out.append('<font face="Courier-Bold" color="#1F4E5F">%s</font>' % escape(part[1:-1]))
            else:
                out.append(escape(part))
        return "".join(out)

    story, j = [], 0
    while j < len(lines):
        ln = lines[j]
        img_m = re.match(r"^!\[(.*)\]\((.+)\)\s*$", ln)
        if ln.startswith("# "):
            story.append(Paragraph(escape(ln[2:]), S["title"]))
        elif ln.startswith("### ") and j < 4:
            story.append(Paragraph(escape(ln[4:]), S["sub"]))
        elif ln.startswith("### "):
            story.append(Paragraph(escape(ln[4:]), S["h3"]))
        elif ln.startswith("## "):
            story.append(Paragraph(escape(ln[3:]), S["h2"]))
        elif img_m:
            alt, rel = img_m.groups()
            path = os.path.join(HERE, rel.replace("/", os.sep))
            if os.path.exists(path):
                from PIL import Image as PILImage
                w, h = PILImage.open(path).size
                width = 5.8 * inch
                block = [Image(path, width=width, height=width * h / w)]
                if alt:
                    block.append(Paragraph(escape(alt), S["cap"]))
                story.append(KeepTogether(block))
        elif ln.strip() == "---":
            story.append(Spacer(1, 6))
        elif ln.startswith("> "):
            story.append(Paragraph(inline(ln[2:]), S["quote"]))
        elif re.match(r"^\s*\d+\.\s", ln) or re.match(r"^\s*-\s", ln):
            m = re.match(r"^(\s*)(\d+\.|-)\s(.*)$", ln)
            indent, marker, body = m.groups()
            while (j + 1 < len(lines) and lines[j + 1].startswith("   ")
                   and not re.match(r"^\s*(\d+\.|-)\s", lines[j + 1])
                   and lines[j + 1].strip() and not lines[j + 1].strip().startswith("`")):
                body += " " + lines[j + 1].strip(); j += 1
            left = 0.3 * inch + 0.25 * inch * (len(indent) // 3)
            st = ParagraphStyle("li", parent=S["body"], leftIndent=left + 0.2 * inch, firstLineIndent=-0.2 * inch, spaceAfter=4)
            pre = ("%s " % marker) if marker != "-" else "• "
            story.append(Paragraph('<font color="#C8873F"><b>%s</b></font>%s' % (escape(pre), inline(body)), st))
        elif ln.strip().startswith("`") and ln.strip().endswith("`") and len(ln.strip()) > 2:
            story.append(Paragraph(escape(ln.strip().strip("`")), S["code"]))
        elif ln.strip() == "```":
            j += 1
            while j < len(lines) and lines[j].strip() != "```":
                story.append(Paragraph(escape(lines[j].strip()), S["code"])); j += 1
        elif ln.strip():
            body = ln.strip()
            while (j + 1 < len(lines) and lines[j + 1].strip()
                   and not lines[j + 1].startswith(("#", ">", "-", "`", "!"))
                   and not re.match(r"^\s*(\d+\.|-)\s", lines[j + 1])
                   and lines[j + 1].strip() != "---"):
                body += " " + lines[j + 1].strip(); j += 1
            story.append(Paragraph(inline(body), S["body"]))
        j += 1
    SimpleDocTemplate(PDF, pagesize=letter, leftMargin=0.9 * inch, rightMargin=0.9 * inch,
                      topMargin=0.8 * inch, bottomMargin=0.8 * inch,
                      title="Genie Installation Guide").build(story)


try:
    from docx2pdf import convert
    convert(DOCX, PDF)
    print("pdf saved via Word: %s (%d KB)" % (PDF, os.path.getsize(PDF) // 1024))
except Exception as exc:  # no Word / no docx2pdf: render the Markdown directly
    print("Word conversion unavailable (%s); rendering PDF with reportlab" % exc.__class__.__name__)
    pdf_via_reportlab()
    print("pdf saved: %s (%d KB)" % (PDF, os.path.getsize(PDF) // 1024))
