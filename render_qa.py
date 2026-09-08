"""Universal render-containment QA gate (every niche).

Exports a produced DOCX to PDF (Word), renders every page, and FAILS the book if any
non-bleed page has content crossing its margins -- i.e. text or an image beyond the printable
area -- or if the book spills past its expected page structure. This enforces the catalog-wide
law "no text beyond the margin, no unit beyond its column/page" that the framework text states
but which must be VERIFIED on the rendered page, not assumed.

Full-bleed pages (chapter dividers, covers, full-page images) are intentionally edge-to-edge and
are auto-detected (margins almost fully inked) or declared with --bleed-pages.

Usage:
  python render_qa.py --docx PATH [--margin-in 0.7] [--bleed-pages 2,5] [--expect-pages N] [--save-dir DIR]

Exit code 0 = PASS, 1 = FAIL. Prints a JSON report.
Requires: Microsoft Word (COM), PyMuPDF (`pip install pymupdf`), numpy.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import fitz  # PyMuPDF
import numpy as np


def export_pdf(docx, pdf):
    """Export DOCX -> PDF via Word, in-process COM (comtypes). Runs where an interactive
    session is available (a normal terminal). Returns the page count."""
    import comtypes.client
    docx_abs = os.path.abspath(docx)
    pdf_abs = os.path.abspath(pdf)
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False
    doc = None
    try:
        doc = word.Documents.Open(docx_abs, ReadOnly=True)
        doc.SaveAs(pdf_abs, FileFormat=17)  # 17 = wdFormatPDF
        pages = int(doc.ComputeStatistics(2))  # 2 = wdStatisticPages
        return pages
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()


def analyze(pdf, margin_in=0.7, dpi=150, bleed_pages=None, ink_thresh=238,
            bleed_margin_frac=0.55, edge_fail_frac=0.02, save_dir=None):
    bleed_pages = set(bleed_pages or [])
    doc = fitz.open(pdf)
    m_px = int(margin_in * dpi)
    pages = []
    for i, pg in enumerate(doc):
        n = i + 1
        pix = pg.get_pixmap(dpi=dpi)
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        gray = arr[..., :3].mean(axis=2)
        ink = gray < ink_thresh
        H, W = ink.shape
        bands = {"top": ink[:m_px, :], "bottom": ink[H - m_px:, :],
                 "left": ink[:, :m_px], "right": ink[:, W - m_px:]}
        margin_ink = sum(int(b.sum()) for b in bands.values())
        margin_tot = sum(b.size for b in bands.values())
        margin_frac = margin_ink / max(1, margin_tot)
        if n in bleed_pages or margin_frac > bleed_margin_frac:
            status, edges = "BLEED-EXEMPT", []
        else:
            edges = [e for e, b in bands.items() if b.mean() > edge_fail_frac]
            status = "FAIL" if edges else "PASS"
        pages.append({"page": n, "status": status, "margin_ink_frac": round(margin_frac, 4),
                      "violated_edges": edges})
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
            pix.save(os.path.join(save_dir, "qa-page-%02d.png" % n))
    return pages


def run(docx=None, pdf_path=None, margin_in=0.7, bleed_pages=None, expect_pages=None, save_dir=None):
    tmp = None
    if pdf_path:
        pdf = pdf_path; total = fitz.open(pdf).page_count
    else:
        tmp = tempfile.mkdtemp(); pdf = os.path.join(tmp, "qa.pdf")
        total = export_pdf(docx, pdf)
    try:
        pages = analyze(pdf, margin_in=margin_in, bleed_pages=bleed_pages, save_dir=save_dir)
    finally:
        if tmp:
            import shutil; shutil.rmtree(tmp, ignore_errors=True)
    fails = [p for p in pages if p["status"] == "FAIL"]
    findings = []
    for p in fails:
        findings.append("Class A: page %d has content crossing the margin(s): %s "
                        "(no text/image may cross the margin)" % (p["page"], ", ".join(p["violated_edges"])))
    if expect_pages is not None and total is not None and total > expect_pages:
        findings.append("Class A: book rendered %d pages, expected <= %d -- likely an overflow/"
                        "split (a unit spilled past its page)" % (total, expect_pages))
    ok = not findings
    return {"pass": ok, "source": os.path.abspath(docx or pdf_path), "total_pages": total,
            "pages": pages, "findings": findings}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docx", help="DOCX to export via Word and check")
    ap.add_argument("--pdf", help="pre-exported PDF to check (skips Word)")
    ap.add_argument("--margin-in", type=float, default=0.7)
    ap.add_argument("--bleed-pages", default="")
    ap.add_argument("--expect-pages", type=int, default=None)
    ap.add_argument("--save-dir", default=None)
    a = ap.parse_args()
    if not a.docx and not a.pdf:
        ap.error("provide --docx or --pdf")
    bleed = [int(x) for x in a.bleed_pages.split(",") if x.strip()]
    rep = run(docx=a.docx, pdf_path=a.pdf, margin_in=a.margin_in, bleed_pages=bleed,
              expect_pages=a.expect_pages, save_dir=a.save_dir)
    print(json.dumps(rep, indent=2))
    sys.exit(0 if rep["pass"] else 1)


if __name__ == "__main__":
    main()
