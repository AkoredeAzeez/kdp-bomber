#!/usr/bin/env python3
"""
EPUB BUILDER - uapf-platform-target
===================================
Builds a reflowable EPUB 3 from a finished Genie book project:
final rolling DOCX -> XHTML chapters (split on Heading 1) + embedded
images + metadata from publish_manifest.json + cover.

Usage:
  python epub_build.py <project_folder> [--docx path] [--out path]

Requires: python-docx (always installed by the bootstrap) and ebooklib
(installed on first use: pip install ebooklib). No network needed.
Global rules honored: no publisher name, no ISBN placeholder, no em dashes
introduced. Reflowable by design: print-only layout (columns, fixed panels)
is simplified to clean single-flow formatting.
"""
import argparse, glob, html, json, os, sys

def find_docx(folder, given):
    if given: return given
    cands = [p for p in glob.glob(os.path.join(folder, "*.docx"))
             if "metadata" not in os.path.basename(p).lower()
             and not os.path.basename(p).startswith("~$")]
    if not cands:
        sys.exit("no DOCX found in project folder")
    return max(cands, key=os.path.getsize)

def find_cover(folder, manifest):
    for key in ("cover_front", "cover_wrap_pdf"):
        p = (manifest.get("files") or {}).get(key)
        if p and os.path.exists(p) and p.lower().endswith((".jpg", ".jpeg", ".png")):
            return p
    for pat in ("cover_front*.png", "cover_front*.jpg", "cover*.jpg", "cover*.png"):
        c = glob.glob(os.path.join(folder, pat)) + glob.glob(os.path.join(folder, "cover*", pat))
        if c: return c[0]
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--docx")
    ap.add_argument("--out")
    a = ap.parse_args()

    try:
        import docx as _docx
    except ImportError:
        sys.exit("python-docx missing: run the bootstrap first")
    try:
        from ebooklib import epub
    except ImportError:
        import subprocess
        print("[deps] installing ebooklib ...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "ebooklib"])
        from ebooklib import epub

    folder = os.path.abspath(a.project)
    man_path = os.path.join(folder, "publish_manifest.json")
    manifest = json.load(open(man_path, encoding="utf-8")) if os.path.exists(man_path) else {}
    docx_path = find_docx(folder, a.docx)
    doc = _docx.Document(docx_path)

    title = manifest.get("exact_title") or os.path.splitext(os.path.basename(docx_path))[0]
    author = manifest.get("author_pen_name") or ""
    lang = (manifest.get("language") or "en")[:2].lower()
    desc = manifest.get("description") or ""

    book = epub.EpubBook()
    book.set_identifier("genie-" + "".join(c for c in title.lower() if c.isalnum())[:40])
    book.set_title(title)
    book.set_language(lang)
    if author: book.add_author(author)
    if desc: book.add_metadata("DC", "description", desc[:2000])

    cover = find_cover(folder, manifest)
    if cover:
        book.set_cover("cover" + os.path.splitext(cover)[1],
                       open(cover, "rb").read())

    css = epub.EpubItem(uid="style", file_name="style/book.css",
        media_type="text/css", content="""
body{font-family:serif;line-height:1.5;margin:0 4%}
h1{font-size:1.5em;text-align:center;margin:2em 0 1em;page-break-before:always}
h2{font-size:1.15em;margin:1.4em 0 .5em}
h3{font-size:1em;margin:1.2em 0 .4em}
p{margin:.4em 0;text-indent:0}
.callout{border:1px solid #999;border-radius:6px;padding:.6em .9em;margin:.9em 0}
img{max-width:100%}
.caption{font-size:.85em;font-style:italic;text-align:center}
""".encode())
    book.add_item(css)

    # split document on Heading 1
    chapters, cur, cur_title, img_n = [], [], None, 0
    def flush():
        nonlocal cur, cur_title
        if cur_title or cur:
            chapters.append((cur_title or "Front Matter", cur))
        cur, cur_title = [], None

    rels = doc.part.rels
    for block in doc.element.body:
        if block.tag.endswith("}p"):
            from docx.text.paragraph import Paragraph
            p = Paragraph(block, doc)
            style = (p.style.name or "").lower()
            text = html.escape(p.text.strip())
            # inline images
            for r in p.runs:
                for blip in r._element.findall(
                        ".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip"):
                    rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                    if rid and rid in rels:
                        img_n += 1
                        part = rels[rid].target_part
                        ext = os.path.splitext(part.partname)[1] or ".png"
                        fname = f"images/img{img_n}{ext}"
                        book.add_item(epub.EpubItem(uid=f"img{img_n}", file_name=fname,
                            media_type=part.content_type, content=part.blob))
                        cur.append(f'<p style="text-align:center"><img src="../{fname}" alt=""/></p>')
            if not text:
                continue
            if style.startswith("heading 1") or style == "title":
                flush(); cur_title = p.text.strip()
            elif style.startswith("heading 2"):
                cur.append(f"<h2>{text}</h2>")
            elif style.startswith("heading 3") or style.startswith("heading 4"):
                cur.append(f"<h3>{text}</h3>")
            elif "caption" in style:
                cur.append(f'<p class="caption">{text}</p>')
            else:
                cur.append(f"<p>{text}</p>")
        elif block.tag.endswith("}tbl"):
            from docx.table import Table
            t = Table(block, doc)
            rows_html = []
            for row in t.rows[:60]:
                cells = "".join(f"<td>{html.escape(c.text.strip())}</td>" for c in row.cells)
                rows_html.append(f"<tr>{cells}</tr>")
            cur.append('<div class="callout"><table>' + "".join(rows_html) + "</table></div>")
    flush()

    spine, toc = ["nav"], []
    for i, (ct, body) in enumerate(chapters, 1):
        if not body and i == 1:
            continue
        c = epub.EpubHtml(title=ct, file_name=f"text/ch{i:03d}.xhtml", lang=lang)
        c.content = (f"<h1>{html.escape(ct)}</h1>" + "\n".join(body)).encode()
        c.add_item(css)
        book.add_item(c); spine.append(c); toc.append(c)

    book.toc = toc
    book.add_item(epub.EpubNcx()); book.add_item(epub.EpubNav())
    book.spine = spine

    out = a.out or os.path.join(folder, os.path.splitext(os.path.basename(docx_path))[0] + ".epub")
    epub.write_epub(out, book)
    # structural sanity
    import zipfile
    z = zipfile.ZipFile(out)
    ok = ("mimetype" in z.namelist() and any("nav" in n for n in z.namelist()))
    print(f"EPUB written: {out} ({os.path.getsize(out)//1024} KB, "
          f"{len(toc)} chapters, {img_n} images, structure {'OK' if ok else 'CHECK'})")

if __name__ == "__main__":
    main()
