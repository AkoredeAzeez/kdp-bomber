#!/usr/bin/env python3
"""
STOCK FETCH - uapf-video-studio  (stock VIDEOS + stock IMAGES)
=============================================================
Sources only FREE, COMMERCIAL-USE, no-attribution stock: Pexels and Pixabay.
Paid/watermarked results (e.g. iStock ads inside a web search) are never used.

Two modes:
  API mode (reliable, HD) - needs a free key in .env:
      PEXELS_API_KEY=...        (https://www.pexels.com/api/  - free, instant)
      PIXABAY_API_KEY=...       (https://pixabay.com/api/docs/ - free)
    python stock_fetch.py --batch queries.json --out assets/ --orientation landscape
    python stock_fetch.py --query "typing laptop" --kind video --n 3 --out assets/

  Harvest-plan mode (no key) - prints a plan for Genie to fetch via its browser
    (Pexels DOM: images.pexels.com/photos + videos.pexels.com/video-files), then
    Genie curls the chosen URLs. Filters out media.istockphoto.com.
    python stock_fetch.py --batch queries.json --harvest-plan

queries.json: [{"id":"s1","query":"typing laptop","kind":"video","orientation":"landscape"}, ...]
Every downloaded file is recorded in <out>/stock_manifest.json with its source
URL and provider so the licence trail is kept.
"""
import argparse, json, os, sys, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))

def _env(key):
    if os.environ.get(key):
        return os.environ[key]
    d = HERE
    for _ in range(6):
        envp = os.path.join(d, ".env")
        if os.path.exists(envp):
            for line in open(envp, encoding="utf-8-sig"):
                if line.strip().startswith(key + "="):
                    return line.split("=", 1)[1].strip()
        d = os.path.dirname(d)
    return None

def _get(url, headers=None, timeout=45):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def _json(url, headers=None):
    return json.loads(_get(url, headers).decode("utf-8", "replace"))

def _dl(url, dest):
    data = _get(url, timeout=120)
    with open(dest, "wb") as f:
        f.write(data)
    return os.path.getsize(dest)

# ------------------------------------------------------------- Pexels -------
def pexels_video(query, orientation, want_w=1920):
    key = _env("PEXELS_API_KEY")
    if not key:
        return None
    o = {"landscape": "landscape", "portrait": "portrait", "square": "square"}.get(orientation, "landscape")
    u = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": o, "per_page": 8, "size": "medium"})
    js = _json(u, {"Authorization": key})
    best = None
    for v in js.get("videos", []):
        for f in v.get("video_files", []):
            if not f.get("link", "").endswith(".mp4"):
                continue
            w, h = f.get("width") or 0, f.get("height") or 0
            if orientation == "landscape" and w < h:
                continue
            if orientation == "portrait" and h < w:
                continue
            score = -abs((w or 0) - want_w)
            if best is None or score > best[0]:
                best = (score, f["link"], w, h, v.get("url"), v.get("user", {}).get("name"))
    if best:
        return {"url": best[1], "w": best[2], "h": best[3], "page": best[4],
                "author": best[5], "provider": "pexels"}
    return None

def pexels_photo(query, orientation):
    key = _env("PEXELS_API_KEY")
    if not key:
        return None
    o = {"landscape": "landscape", "portrait": "portrait", "square": "square"}.get(orientation, "landscape")
    u = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": query, "orientation": o, "per_page": 5})
    js = _json(u, {"Authorization": key})
    for p in js.get("photos", []):
        src = p.get("src", {}).get("large2x") or p.get("src", {}).get("original")
        if src:
            return {"url": src, "page": p.get("url"), "author": p.get("photographer"),
                    "provider": "pexels"}
    return None

# ------------------------------------------------------------ Pixabay -------
def pixabay_video(query, orientation):
    key = _env("PIXABAY_API_KEY")
    if not key:
        return None
    u = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": key, "q": query, "per_page": 8})
    js = _json(u)
    for h in js.get("hits", []):
        v = h.get("videos", {}).get("large") or h.get("videos", {}).get("medium")
        if v and v.get("url"):
            w, hh = v.get("width", 0), v.get("height", 0)
            if orientation == "landscape" and w < hh:
                continue
            if orientation == "portrait" and hh < w:
                continue
            return {"url": v["url"], "w": w, "h": hh, "page": h.get("pageURL"),
                    "author": h.get("user"), "provider": "pixabay"}
    return None

def pixabay_photo(query, orientation):
    key = _env("PIXABAY_API_KEY")
    if not key:
        return None
    u = "https://pixabay.com/api/?" + urllib.parse.urlencode(
        {"key": key, "q": query, "per_page": 5, "image_type": "photo"})
    js = _json(u)
    for h in js.get("hits", []):
        if h.get("largeImageURL"):
            return {"url": h["largeImageURL"], "page": h.get("pageURL"),
                    "author": h.get("user"), "provider": "pixabay"}
    return None

def fetch_one(query, kind, orientation, provider="auto"):
    order = ["pexels", "pixabay"] if provider == "auto" else [provider]
    for prov in order:
        try:
            if kind == "video":
                r = pexels_video(query, orientation) if prov == "pexels" else pixabay_video(query, orientation)
            else:
                r = pexels_photo(query, orientation) if prov == "pexels" else pixabay_photo(query, orientation)
            if r:
                return r
        except Exception as e:
            sys.stderr.write(f"[{prov}] {query}: {e}\n")
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch")
    ap.add_argument("--query")
    ap.add_argument("--kind", default="video", choices=["video", "photo"])
    ap.add_argument("--orientation", default="landscape", choices=["landscape", "portrait", "square"])
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--provider", default="auto", choices=["auto", "pexels", "pixabay"])
    ap.add_argument("--out")
    ap.add_argument("--harvest-plan", action="store_true")
    a = ap.parse_args()

    jobs = []
    if a.batch:
        jobs = json.load(open(a.batch, encoding="utf-8"))
    elif a.query:
        jobs = [{"id": "q1", "query": a.query, "kind": a.kind, "orientation": a.orientation}]
    else:
        sys.exit("need --batch or --query")

    have_key = bool(_env("PEXELS_API_KEY") or _env("PIXABAY_API_KEY"))
    if a.harvest_plan or not have_key:
        # No API key: emit a plan Genie executes with its browser (DOM harvest).
        plan = {"mode": "browser-harvest",
                "note": ("No PEXELS_API_KEY / PIXABAY_API_KEY in .env. Genie: for each query open "
                         "https://www.pexels.com/search/videos/<query>/ (or /search/<query>/ for photos), "
                         "extract only videos.pexels.com/video-files or images.pexels.com/photos URLs "
                         "(NEVER media.istockphoto.com), pick landscape/portrait to match, and curl them "
                         "into the out folder. A free key from pexels.com/api makes this automatic + HD."),
                "queries": jobs}
        print(json.dumps(plan, indent=1))
        return

    if not a.out:
        sys.exit("--out required for download")
    os.makedirs(a.out, exist_ok=True)
    manifest = []
    for j in jobs:
        r = fetch_one(j["query"], j.get("kind", "video"), j.get("orientation", a.orientation), a.provider)
        if not r:
            print(f"MISS  {j.get('id')}  {j['query']}")
            manifest.append({"id": j.get("id"), "query": j["query"], "ok": False})
            continue
        ext = ".mp4" if j.get("kind", "video") == "video" else ".jpg"
        dest = os.path.join(a.out, f"{j.get('id','q')}{ext}")
        try:
            sz = _dl(r["url"], dest)
        except Exception as e:
            print(f"DLFAIL {j.get('id')}  {e}")
            manifest.append({"id": j.get("id"), "query": j["query"], "ok": False})
            continue
        print(f"OK    {j.get('id')}  {r['provider']}  {os.path.basename(dest)}  {sz//1024}KB")
        manifest.append({"id": j.get("id"), "query": j["query"], "file": dest, "ok": True,
                         "provider": r["provider"], "source_page": r.get("page"),
                         "author": r.get("author"), "license": "free commercial, no attribution required"})
    json.dump(manifest, open(os.path.join(a.out, "stock_manifest.json"), "w"), indent=1)
    ok = sum(1 for m in manifest if m.get("ok"))
    print(f"\n{ok}/{len(jobs)} fetched -> {a.out}")
    if ok < len(jobs):
        sys.exit(2)

if __name__ == "__main__":
    main()
