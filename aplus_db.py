#!/usr/bin/env python3
"""
A+ CONTENT REFERENCE DATABASE  (per-niche best-seller A+ module bank)
=====================================================================
Companion to cover_db.py. Stores real A+ Content modules (the "From the
Publisher" images) captured from best-selling Amazon listings, organised by
niche, so A+ design can start from the shelf's real conventions instantly.

Reference-only, local-only: never ship, export, or redistribute (third-party
marketing art). Never copy or closely imitate; pattern reference only.

Layout:  <genie>/cover_db/_aplus/<niche>/manifest.json + module images

Commands
  bank  --niche cookbook --json capture.json
        capture.json = {"ASIN1": ["url1", "url2"], "ASIN2": [...]}
        downloads every module image and records source ASIN + date
  pick  --niche cookbook [--count 4]   random refs (LRU-biased), stamp used
  list                                  per-niche counts and freshness
"""
import argparse, json, os, random, sys, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.abspath(os.path.join(HERE, "..", "..", "..", "cover_db", "_aplus"))
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
NICHES = ["health", "cookbook", "textbook", "medical", "workbook", "study-guide",
          "exam-simulator", "childrens", "childrens-facts", "activity", "crafts",
          "selfhelp", "howto", "humor", "history", "fiction", "public-domain",
          "travel", "user-guide", "journal", "faith", "business", "biography",
          "parenting", "sports", "language", "poetry", "reference",
          "popular-science"]


def load_manifest(niche):
    p = os.path.join(DB, niche, "manifest.json")
    if os.path.exists(p):
        return json.loads(open(p, encoding="utf-8").read())
    return []


def save_manifest(niche, records):
    d = os.path.join(DB, niche)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "manifest.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(records, indent=2))


def load_capture(path):
    """JSON {asin: [urls]} or compact .txt lines 'ASIN|path-after-images/S/'."""
    if path.endswith(".json"):
        return json.loads(open(path, encoding="utf-8").read())
    data = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        asin, suffix = line.split("|", 1)
        data.setdefault(asin, []).append(
            "https://m.media-amazon.com/images/S/" + suffix)
    return data


def cmd_bank(niche, json_path):
    data = load_capture(json_path)
    d = os.path.join(DB, niche)
    os.makedirs(d, exist_ok=True)
    records = load_manifest(niche)
    have = {r["source_url"] for r in records if "source_url" in r}
    today = time.strftime("%Y-%m-%d")
    ok = fail = skip = 0
    for asin, urls in data.items():
        for i, url in enumerate(urls):
            if url in have:
                skip += 1
                continue
            ext = ".png" if ".png" in url.lower() else ".jpg"
            name = f"{asin}_m{i+1}{ext}"
            n = 1
            while os.path.exists(os.path.join(d, name)):
                n += 1
                name = f"{asin}_m{i+1}_{n}{ext}"
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=30) as r, \
                        open(os.path.join(d, name), "wb") as f:
                    f.write(r.read())
                if os.path.getsize(os.path.join(d, name)) < 4000:
                    raise ValueError("too small")
            except Exception as e:
                print("download fail", asin, i + 1, e)
                fail += 1
                continue
            records.append({"file": name, "asin": asin, "source_url": url,
                            "captured": today, "last_used": None})
            have.add(url)
            ok += 1
    save_manifest(niche, records)
    print(f"{niche}: banked {ok}, skipped {skip} dupes, failed {fail}; total {len(records)}")


def cmd_pick(niche, count):
    records = [r for r in load_manifest(niche)
               if os.path.exists(os.path.join(DB, niche, r["file"]))]
    if len(records) < 2:
        print(json.dumps({"ok": False, "error": "NOT_ENOUGH_MODULES",
                          "have": len(records)}))
        return
    records.sort(key=lambda r: (r.get("last_used") or "", random.random()))
    n = min(count, len(records))
    picked = records[:n]
    today = time.strftime("%Y-%m-%d")
    for r in picked:
        r["last_used"] = today
    save_manifest(niche, load_and_merge(niche, picked))
    print(json.dumps({"ok": True, "niche": niche, "picked": [
        {"path": os.path.join(DB, niche, r["file"]), "asin": r["asin"],
         "captured": r["captured"]} for r in picked]}, indent=2))


def load_and_merge(niche, picked):
    records = load_manifest(niche)
    by_file = {r["file"]: r for r in records}
    for p in picked:
        if p["file"] in by_file:
            by_file[p["file"]]["last_used"] = p["last_used"]
    return list(by_file.values())


def cmd_list():
    total = 0
    if not os.path.isdir(DB):
        print("empty A+ bank")
        return
    for niche in sorted(os.listdir(DB)):
        if not os.path.isdir(os.path.join(DB, niche)):
            continue
        recs = load_manifest(niche)
        files = [r for r in recs
                 if os.path.exists(os.path.join(DB, niche, r["file"]))]
        loose = [f for f in os.listdir(os.path.join(DB, niche))
                 if f.lower().endswith((".png", ".jpg", ".jpeg"))
                 and f not in {r["file"] for r in recs}]
        count = len(files) + len(loose)
        total += count
        dates = sorted(r["captured"] for r in files) or ["-"]
        print(f"{niche:18s} {count:4d} module(s)   captured {dates[0]} .. {dates[-1]}")
    print(f"{'TOTAL':18s} {total:4d}")


def main():
    ap = argparse.ArgumentParser(description="Per-niche A+ module reference database")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("bank")
    b.add_argument("--niche", required=True, choices=NICHES)
    b.add_argument("--json", required=True)
    p = sub.add_parser("pick")
    p.add_argument("--niche", required=True, choices=NICHES)
    p.add_argument("--count", type=int, default=4)
    sub.add_parser("list")
    a = ap.parse_args()
    if a.cmd == "bank":
        cmd_bank(a.niche, a.json)
    elif a.cmd == "pick":
        cmd_pick(a.niche, a.count)
    else:
        cmd_list()


if __name__ == "__main__":
    main()
