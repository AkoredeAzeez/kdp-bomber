"""PAGE-COUNT GATE (catalog-wide, every niche, both engines).

STRICT LAW (operator directive 2026-08-18): the delivered book's final rendered
page count must equal the target page count, or fall within a 5% increase or
decrease of it. Anything outside [target - 5%, target + 5%] is a FAIL and blocks
delivery until the book is brought into the band.

The band is fixed by CONTENT, never by cheating layout: you add or cut real
material, or re-plan chapters, to change the page count. You never pad with
blank pages/whitespace, and you never shrink type below the niche/senior floor
to squeeze pages in (rules 17 and 18 still bind). Under-count is repaired by
expanding content (deeper chapters, more examples/recipes/exercises, added
back-matter that belongs); over-count by tightening or re-planning.

Target resolution (first that is found, unless --target is given):
  --target N                              (explicit; authoritative)
  project.json: requested_page_count
  project.json: page_count_target / target_page_count / target_pages
  project.json: provisional_page_ceiling (treated as the target)
  project.json: projected_physical_pages
  project.json: target_pages_min & target_pages_max  -> band used directly

Actual page count:
  --pdf PATH    count pages in a finished PDF (fast, no Word)
  --docx PATH   export via Word and count (reuses render_qa.export_pdf)
  --actual N    supply a known count directly

Usage:
  python page_count_gate.py --project BOOKDIR --docx BOOK.docx
  python page_count_gate.py --target 120 --pdf book.pdf
  python page_count_gate.py --target 120 --actual 118

Exit 0 = PASS (within band), 1 = FAIL, 2 = usage/target error. Prints JSON.
"""
import argparse
import json
import math
import os
import sys

TOL = 0.05  # strict 5% either side

TARGET_FIELDS = ["requested_page_count", "page_count_target", "target_page_count",
                 "target_pages", "provisional_page_ceiling", "projected_physical_pages"]


def resolve_target(project):
    """Return (target, band_lo, band_hi, source) from project.json, or Nones."""
    pj = os.path.join(project, "project.json")
    if not os.path.exists(pj):
        return None, None, None, None
    d = json.load(open(pj, encoding="utf-8"))
    # explicit band
    lo, hi = d.get("target_pages_min"), d.get("target_pages_max")
    if isinstance(lo, (int, float)) and isinstance(hi, (int, float)):
        return None, int(lo), int(hi), "target_pages_min/max"
    for f in TARGET_FIELDS:
        v = d.get(f)
        if isinstance(v, (int, float)) and v > 0:
            return int(v), None, None, f
    return None, None, None, None


def band_for(target):
    lo = int(math.floor(target * (1 - TOL)))
    hi = int(math.ceil(target * (1 + TOL)))
    return lo, hi


def actual_pages(docx=None, pdf=None, actual=None):
    if actual is not None:
        return int(actual)
    if pdf:
        import fitz
        return fitz.open(pdf).page_count
    if docx:
        import importlib.util
        here = os.path.dirname(os.path.abspath(__file__))
        spec = importlib.util.spec_from_file_location("render_qa", os.path.join(here, "render_qa.py"))
        rq = importlib.util.module_from_spec(spec); spec.loader.exec_module(rq)
        import tempfile
        tmp = tempfile.mkdtemp(); out = os.path.join(tmp, "pc.pdf")
        try:
            return rq.export_pdf(docx, out)
        finally:
            import shutil; shutil.rmtree(tmp, ignore_errors=True)
    return None


def evaluate(target, band_lo, band_hi, actual):
    if band_lo is None or band_hi is None:
        band_lo, band_hi = band_for(target)
    ok = band_lo <= actual <= band_hi
    rep = {"pass": ok, "target": target, "band": [band_lo, band_hi],
           "actual_pages": actual, "tolerance": TOL}
    if not ok:
        if actual < band_lo:
            need = band_lo - actual
            to_target = (target - actual) if target else need
            rep["finding"] = (
                "Class A: book rendered %d pages, below the allowed band %d to %d. "
                "UNDER by %d page(s) to reach the band (%s to hit target). Expand "
                "real content (deeper chapters, more units, legitimate back matter); "
                "do NOT pad blank pages or enlarge type beyond the design."
                % (actual, band_lo, band_hi, need,
                   ("+%d" % to_target) if target else "n/a"))
        else:
            over = actual - band_hi
            to_target = (actual - target) if target else over
            rep["finding"] = (
                "Class A: book rendered %d pages, above the allowed band %d to %d. "
                "OVER by %d page(s) to reach the band (%s to hit target). Tighten or "
                "re-plan content; do NOT shrink type below the niche/senior floor."
                % (actual, band_lo, band_hi, over,
                   ("-%d" % to_target) if target else "n/a"))
    return rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", help="book folder (reads target from project.json)")
    ap.add_argument("--target", type=int, default=None, help="explicit target page count")
    ap.add_argument("--docx", help="finished DOCX (exported via Word to count)")
    ap.add_argument("--pdf", help="finished PDF (counted directly)")
    ap.add_argument("--actual", type=int, default=None, help="known page count")
    a = ap.parse_args()

    target, band_lo, band_hi = a.target, None, None
    src = "--target"
    if target is None and a.project:
        target, band_lo, band_hi, src = resolve_target(a.project)
    if target is None and band_lo is None:
        print(json.dumps({"pass": False, "error":
              "no target page count found (pass --target N, or set requested_page_count "
              "/ target_pages_min+max in project.json)"}, indent=2))
        sys.exit(2)

    actual = actual_pages(docx=a.docx, pdf=a.pdf, actual=a.actual)
    if actual is None:
        print(json.dumps({"pass": False, "error":
              "no page count to check (pass --docx, --pdf, or --actual)"}, indent=2))
        sys.exit(2)

    rep = evaluate(target, band_lo, band_hi, actual)
    rep["target_source"] = src
    print(json.dumps(rep, indent=2))
    sys.exit(0 if rep["pass"] else 1)


if __name__ == "__main__":
    main()
