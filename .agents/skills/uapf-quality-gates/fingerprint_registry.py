#!/usr/bin/env python3
"""
FINGERPRINT REGISTRY - the mechanical Design Log (operator directive 2026-08-19)
================================================================================
Turns "no two books alike" from discipline into a GATE. One machine-readable
catalog registry records every book's locked design axes; a collision check
runs BEFORE drafting (at fingerprint time) and blocks by exit code.

  python fingerprint_registry.py check    --niche cookbook --opener side-band \
         --unit C --palette-family "warm earth" --palette "#2D6A4F,#E9A14D" [--cover C2]
  python fingerprint_registry.py register --project <folder> --title "..." \
         --niche cookbook --opener side-band --unit C --palette-family "warm earth" \
         --palette "#2D6A4F,#E9A14D" [--cover C2] [--pen-name "..."]
  python fingerprint_registry.py list [--niche cookbook]

Exit codes: check -> 0 UNIQUE, 2 COLLISION (reasons printed).
Collision rules (per the archetype laws):
  R1 same niche + same opener + same unit + same palette family    -> FAIL
  R2 same primary palette hex anywhere in the catalog              -> FAIL
  R3 same niche + same cover composition + same palette family     -> FAIL
The registry lives at state/fingerprint_registry.json (survives updates,
per-install, never ships to other installs).
"""
import argparse, json, os, sys
from datetime import date

def find_root():
    d = os.getcwd()
    for _ in range(8):
        if os.path.exists(os.path.join(d, "CLAUDE.md")) or os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        nd = os.path.dirname(d)
        if nd == d:
            break
        d = nd
    return os.getcwd()

def reg_path(args):
    if args.registry:
        return args.registry
    return os.path.join(find_root(), "state", "fingerprint_registry.json")

def load(path):
    if os.path.exists(path):
        return json.load(open(path, encoding="utf-8"))
    return {"books": []}

def norm(s):
    return (s or "").strip().lower()

def primary_hex(palette):
    return norm((palette or "").split(",")[0])

def _axis_match(x, y):
    """Unknown ('') on either side acts as a WILDCARD: we cannot prove the axes
    differ, so for collision purposes they match (conservative, protects the
    catalog even against backfilled books with partial data)."""
    x, y = norm(x), norm(y)
    return (not x) or (not y) or x == y

def collisions(reg, a):
    hits = []
    for b in reg["books"]:
        same_niche = norm(b.get("niche")) == norm(a.niche)
        if same_niche and a.palette_family and \
           norm(b.get("palette_family")) == norm(a.palette_family) and \
           _axis_match(b.get("unit"), a.unit) and \
           _axis_match(b.get("opener"), a.opener):
            hits.append((b, "R1: same niche + palette family with matching (or unknown) opener/unit archetypes"))
        if a.palette and primary_hex(b.get("palette")) and \
           primary_hex(b.get("palette")) == primary_hex(a.palette):
            hits.append((b, "R2: same primary palette color"))
        if same_niche and a.cover and b.get("cover") and a.palette_family and \
           norm(b.get("cover")) == norm(a.cover) and \
           norm(b.get("palette_family")) == norm(a.palette_family):
            hits.append((b, "R3: same niche + cover composition + palette family"))
    return hits

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    def common(p):
        p.add_argument("--niche", required=True)
        p.add_argument("--opener", default="")
        p.add_argument("--unit", default="")
        p.add_argument("--palette-family", dest="palette_family", default="")
        p.add_argument("--palette", default="", help="hex list, primary first: '#2D6A4F,#E9A14D'")
        p.add_argument("--cover", default="", help="cover composition archetype (C1-C8)")
        p.add_argument("--registry", default=None)
    c = sub.add_parser("check"); common(c)
    r = sub.add_parser("register"); common(r)
    r.add_argument("--project", required=True)
    r.add_argument("--title", required=True)
    r.add_argument("--pen-name", dest="pen_name", default="")
    l = sub.add_parser("list")
    l.add_argument("--niche", default=None)
    l.add_argument("--registry", default=None)
    a = ap.parse_args()

    path = reg_path(a)
    reg = load(path)

    if a.cmd == "list":
        rows = [b for b in reg["books"] if not a.niche or norm(b.get("niche")) == norm(a.niche)]
        print(f"registered books: {len(rows)}" + (f" (niche={a.niche})" if a.niche else ""))
        for b in rows:
            print(f"  {b.get('title','?')[:44]:46} niche={b.get('niche')} opener={b.get('opener') or '-'} "
                  f"unit={b.get('unit') or '-'} cover={b.get('cover') or '-'} palette={b.get('palette_family') or '-'}")
        return

    hits = collisions(reg, a)
    if a.cmd == "check":
        if hits:
            print("COLLISION: this fingerprint repeats the catalog. Vary the palette first, then the archetype:")
            for b, why in hits:
                print(f"  vs '{b.get('title','?')[:50]}': {why}")
            sys.exit(2)
        print("UNIQUE: fingerprint clears the catalog registry.")
        return

    # register
    if hits:
        print("REFUSED: registering would violate No-Two-Books-Alike:")
        for b, why in hits:
            print(f"  vs '{b.get('title','?')[:50]}': {why}")
        sys.exit(2)
    reg["books"].append({
        "title": a.title, "project": os.path.abspath(a.project),
        "pen_name": a.pen_name, "niche": a.niche, "opener": a.opener,
        "unit": a.unit, "cover": a.cover, "palette_family": a.palette_family,
        "palette": a.palette, "date": str(date.today()),
    })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(reg, open(path, "w", encoding="utf-8"), indent=1)
    print(f"REGISTERED: '{a.title}' ({a.niche}) -> {path}  [{len(reg['books'])} books in catalog]")

if __name__ == "__main__":
    main()
