#!/usr/bin/env python3
"""
COVER REFERENCE DATABASE  (per-niche best-seller cover bank)
============================================================
A local library of proven competitor covers, organised by niche, so cover
generation can pull 2-3 references instantly instead of running a live Amazon
research session for every book. Populated by the operator and by banking the
references each uapf-cover-reference live run downloads.

Reference-only. Images are design references for original covers; they are
never shipped, redistributed, copied, or traced. The database stays local.

Layout:  <genie>/cover_db/<niche>/manifest.json + image files

Commands
  add     --niche cookbook --image PATH [--title T] [--asin A] [--bsr N]
          [--rating 4.7] [--reviews 1809] [--marketplace amazon.com]
          [--source NOTE]           copy one cover into the bank
  import  --niche cookbook --folder PATH [--source NOTE]
                                    bulk-add every image in a folder
  pick    --niche cookbook [--count 3]
                                    randomly pick 2-3 references (least-recently
                                    used first), print JSON, stamp last_used
  list    [--niche cookbook]        show every niche with counts and freshness
"""
import argparse, json, os, random, shutil, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.abspath(os.path.join(HERE, "..", "..", "..", "cover_db"))
IMG_EXT = (".jpg", ".jpeg", ".png", ".webp")

NICHES = ["health", "cookbook", "textbook", "medical", "workbook", "study-guide",
          "exam-simulator", "childrens", "childrens-facts", "activity", "crafts",
          "selfhelp", "howto", "humor", "history", "fiction", "public-domain",
          "travel", "user-guide", "journal", "faith", "business", "biography",
          "parenting", "sports", "language", "poetry", "reference",
          "popular-science", "coloring", "puzzle"]


def niche_dir(db, niche):
    return os.path.join(db, niche)


def load_manifest(db, niche):
    p = os.path.join(niche_dir(db, niche), "manifest.json")
    if os.path.exists(p):
        return json.loads(open(p, encoding="utf-8").read())
    return []


def save_manifest(db, niche, records):
    d = niche_dir(db, niche)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "manifest.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(records, indent=2))


def add_one(db, niche, image, meta):
    if not os.path.exists(image):
        print(f"skip (missing): {image}")
        return False
    d = niche_dir(db, niche)
    os.makedirs(d, exist_ok=True)
    base = (meta.get("asin") or os.path.splitext(os.path.basename(image))[0])
    base = "".join(c for c in base if c.isalnum() or c in "-_") or "cover"
    ext = os.path.splitext(image)[1].lower() or ".jpg"
    name = base + ext
    n = 1
    while os.path.exists(os.path.join(d, name)):
        n += 1
        name = f"{base}_{n}{ext}"
    shutil.copy2(image, os.path.join(d, name))
    records = load_manifest(db, niche)
    records.append({
        "file": name,
        "title": meta.get("title") or "",
        "asin": meta.get("asin") or "",
        "bsr": meta.get("bsr"),
        "rating": meta.get("rating"),
        "reviews": meta.get("reviews"),
        "marketplace": meta.get("marketplace") or "amazon.com",
        "source": meta.get("source") or "",
        "captured": time.strftime("%Y-%m-%d"),
        "last_used": None,
    })
    save_manifest(db, niche, records)
    print(f"added {niche}/{name}")
    return True


def cmd_add(a):
    meta = {"title": a.title, "asin": a.asin, "bsr": a.bsr, "rating": a.rating,
            "reviews": a.reviews, "marketplace": a.marketplace, "source": a.source}
    add_one(a.db, a.niche, a.image, meta)


def cmd_import(a):
    imgs = [f for f in sorted(os.listdir(a.folder))
            if f.lower().endswith(IMG_EXT)]
    if not imgs:
        print("no images found in", a.folder)
        return
    for f in imgs:
        add_one(a.db, a.niche, os.path.join(a.folder, f),
                {"source": a.source or a.folder, "marketplace": a.marketplace})
    print(f"imported {len(imgs)} image(s) into {a.niche}")


def cmd_pick(a):
    records = load_manifest(a.db, a.niche)
    d = niche_dir(a.db, a.niche)
    usable = [r for r in records if os.path.exists(os.path.join(d, r["file"]))]
    if len(usable) < 2:
        print(json.dumps({"ok": False, "reason": "NOT_ENOUGH_COVERS",
                          "niche": a.niche, "have": len(usable),
                          "hint": "need at least 2; run live research and bank the refs"}))
        sys.exit(1)
    count = min(a.count, len(usable))
    # Least-recently-used bias: sample from the never/oldest-used two-thirds.
    usable.sort(key=lambda r: (r.get("last_used") or ""))
    pool = usable[:max(count, (len(usable) * 2 + 2) // 3)]
    picked = random.sample(pool, count)
    now = time.strftime("%Y-%m-%d")
    names = {r["file"] for r in picked}
    for r in records:
        if r["file"] in names:
            r["last_used"] = now
    save_manifest(a.db, a.niche, records)
    out = [{"path": os.path.join(d, r["file"]), "title": r["title"],
            "asin": r["asin"], "bsr": r["bsr"], "rating": r["rating"],
            "reviews": r["reviews"], "captured": r["captured"]} for r in picked]
    print(json.dumps({"ok": True, "niche": a.niche, "picked": out}, indent=2))


def cmd_list(a):
    db = a.db
    niches = [a.niche] if a.niche else (
        sorted(os.listdir(db)) if os.path.exists(db) else [])
    total = 0
    for n in niches:
        if not os.path.isdir(niche_dir(db, n)):
            continue
        records = load_manifest(db, n)
        d = niche_dir(db, n)
        usable = [r for r in records if os.path.exists(os.path.join(d, r["file"]))]
        total += len(usable)
        dates = sorted(r["captured"] for r in usable) if usable else []
        rng = f"{dates[0]} .. {dates[-1]}" if dates else "-"
        print(f"{n:18} {len(usable):3} cover(s)   captured {rng}")
    print(f"{'TOTAL':18} {total:3}")


def main():
    ap = argparse.ArgumentParser(description="Per-niche cover reference database")
    ap.add_argument("--db", default=DEFAULT_DB, help=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("add")
    p.add_argument("--niche", required=True, choices=NICHES)
    p.add_argument("--image", required=True)
    p.add_argument("--title", default="")
    p.add_argument("--asin", default="")
    p.add_argument("--bsr", type=int, default=None)
    p.add_argument("--rating", type=float, default=None)
    p.add_argument("--reviews", type=int, default=None)
    p.add_argument("--marketplace", default="amazon.com")
    p.add_argument("--source", default="")
    p.set_defaults(fn=cmd_add)

    p = sub.add_parser("import")
    p.add_argument("--niche", required=True, choices=NICHES)
    p.add_argument("--folder", required=True)
    p.add_argument("--marketplace", default="amazon.com")
    p.add_argument("--source", default="")
    p.set_defaults(fn=cmd_import)

    p = sub.add_parser("pick")
    p.add_argument("--niche", required=True, choices=NICHES)
    p.add_argument("--count", type=int, default=3)
    p.set_defaults(fn=cmd_pick)

    p = sub.add_parser("list")
    p.add_argument("--niche", default=None)
    p.set_defaults(fn=cmd_list)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
