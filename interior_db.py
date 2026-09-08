#!/usr/bin/env python3
"""
INTERIOR REFERENCE BANK - uapf-cover-db
=======================================
Banks INTERIOR page images of best-selling Amazon books per niche into
cover_db/_interiors/<niche>/ alongside the operator-uploaded house master
PDFs. Internal design reference ONLY: studied for layout patterns, never
copied, never shipped to clients.

Capture file: JSON list of {asin, title, rating, imgs: [urls]} objects
(from extract_interiors.js run on each product page). The first image of
a gallery is the cover and is skipped by default.

Usage:
  python interior_db.py stock <niche> <capture.json> [--include-first]
  python interior_db.py list                       # counts + completion gate
  python interior_db.py pick --niche <x> --count 5 # random refs for a build
Target: 50+ interior captures per seeded niche (completion gate).
"""
import argparse, json, os, random, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BANK = os.path.join(ROOT, "cover_db", "_interiors")
TARGET = 50            # primary niches
TARGET_SECONDARY = 20  # prose-led niches with thinner galleries

def targets():
    p = os.path.join(HERE, "interior_seed_terms.json")
    try:
        d = json.load(open(p, encoding="utf-8"))
        return set(d.get("primary", {})), set(d.get("secondary", {}))
    except Exception:
        return set(), set()
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def large_url(u):
    parts = u.rsplit("/", 1)
    bits = parts[1].split(".")
    if len(bits) > 2:
        parts[1] = bits[0] + "." + bits[-1]
    return parts[0] + "/" + parts[1]

def index_path(niche):
    return os.path.join(BANK, niche, "index.json")

def load_index(niche):
    p = index_path(niche)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []

def stock(niche, capfile, include_first=False):
    items = json.load(open(capfile, encoding="utf-8"))
    nd = os.path.join(BANK, niche)
    os.makedirs(nd, exist_ok=True)
    idx = load_index(niche)
    have_asins = {e["asin"] for e in idx}
    n_existing = len([f for f in os.listdir(nd) if f.lower().endswith((".jpg", ".png"))])
    added = 0
    for it in items:
        if it.get("asin") in have_asins:
            print(f"  skip {it.get('asin')} (already banked)")
            continue
        imgs = it.get("imgs") or []
        if not include_first and len(imgs) > 1:
            imgs = imgs[1:]           # drop the cover
        got = []
        for u in imgs:
            u = large_url(u)
            n_existing += 1
            fname = f"{niche}_int{n_existing:03d}.jpg"
            try:
                req = urllib.request.Request(u, headers=UA)
                data = urllib.request.urlopen(req, timeout=30).read()
                if len(data) < 8000:   # tiny = sprite/placeholder, not a page
                    n_existing -= 1
                    continue
                open(os.path.join(nd, fname), "wb").write(data)
                got.append(fname)
            except Exception as e:
                n_existing -= 1
                print(f"  dl fail {u[:60]}: {e}")
        if got:
            idx.append({"asin": it.get("asin"), "title": it.get("title"),
                        "rating": it.get("rating"), "files": got})
            added += len(got)
            print(f"  {it.get('asin')} '{(it.get('title') or '')[:50]}': {len(got)} interior pages")
    json.dump(idx, open(index_path(niche), "w", encoding="utf-8"), indent=1)
    total = len([f for f in os.listdir(nd) if f.lower().endswith((".jpg", ".png"))])
    print(f"[{niche}] +{added} pages this run, {total} total "
          f"({'GATE PASS' if total >= TARGET else f'OPEN, need {TARGET-total} more'})")

def list_bank():
    primary, secondary = targets()
    niches = sorted(set(list(primary) + list(secondary) +
                        (os.listdir(BANK) if os.path.isdir(BANK) else [])))
    open_primary = 0
    for niche in niches:
        nd = os.path.join(BANK, niche)
        if not os.path.isdir(nd) and niche not in primary and niche not in secondary:
            continue
        jpgs = [f for f in os.listdir(nd) if f.lower().endswith((".jpg", ".png"))] if os.path.isdir(nd) else []
        pdfs = [f for f in os.listdir(nd) if f.lower().endswith(".pdf")] if os.path.isdir(nd) else []
        books = len(load_index(niche))
        tgt = TARGET if niche in primary else TARGET_SECONDARY
        tier = "primary" if niche in primary else ("secondary" if niche in secondary else "extra")
        gate = "PASS" if len(jpgs) >= tgt or pdfs else f"OPEN {len(jpgs)}/{tgt}"
        if gate.startswith("OPEN") and niche in primary:
            open_primary += 1
        print(f"  {niche:16} {len(jpgs):3d} captures from {books:2d} books, "
              f"{len(pdfs)} house PDFs  [{gate}] ({tier})")
    n_p = len(primary)
    print(f"primary gates: {n_p - open_primary}/{n_p} passed"
          + ("" if open_primary == 0 else f" ({open_primary} OPEN: keep seeding between tasks)"))

def pick(niche, count):
    nd = os.path.join(BANK, niche)
    jpgs = [f for f in os.listdir(nd) if f.lower().endswith((".jpg", ".png"))] if os.path.isdir(nd) else []
    pdfs = [f for f in os.listdir(nd) if f.lower().endswith(".pdf")] if os.path.isdir(nd) else []
    if not jpgs and not pdfs:
        print("NOT_ENOUGH_INTERIORS"); sys.exit(1)
    for f in pdfs:
        print(os.path.join(nd, f))          # house masters always included
    for f in random.sample(jpgs, min(count, len(jpgs))):
        print(os.path.join(nd, f))

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("stock"); s.add_argument("niche"); s.add_argument("capture")
    s.add_argument("--include-first", action="store_true")
    sub.add_parser("list")
    p = sub.add_parser("pick"); p.add_argument("--niche", required=True)
    p.add_argument("--count", type=int, default=5)
    a = ap.parse_args()
    if a.cmd == "stock":
        stock(a.niche, a.capture, a.include_first)
    elif a.cmd == "list":
        list_bank()
    else:
        pick(a.niche, a.count)

if __name__ == "__main__":
    main()
