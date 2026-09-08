"""Stocking helper for the cover reference database.

Downloads the cover images listed in a capture file and banks them into
cover_db/<niche>/ with their real metadata via cover_db.py. Used by live
uapf-cover-reference runs (step 6b) and by the NEW-INSTALL SEEDING procedure
in SKILL.md.

Capture file formats:
  .txt  pipe format, one cover per line:  asin|rating|img_code|title
        (img_code is the Amazon image id from m.media-amazon.com/images/I/<code>._AC_UY218_.jpg)
  .json list of {asin, rating, title, img} objects (img = full URL)

Usage:
  python stock_niche.py <niche> <capture-file>
"""
import json, os, subprocess, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CDB = os.path.join(HERE, "cover_db.py")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def large_url(u):
    # strip the size segment (_AC_UY218_ etc.) to request the largest image
    parts = u.rsplit("/", 1)
    name = parts[1]
    bits = name.split(".")
    if len(bits) > 2:
        name = bits[0] + "." + bits[-1]
    return parts[0] + "/" + name

def load_items(path):
    if path.endswith(".json"):
        return json.loads(open(path, encoding="utf-8").read())
    items = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        asin, rating, code, title = line.split("|", 3)
        items.append({"asin": asin, "rating": float(rating), "title": title,
                      "img": f"https://m.media-amazon.com/images/I/{code}.jpg"})
    return items

def main(niche, capture_path):
    items = load_items(capture_path)
    tmp = tempfile.mkdtemp(prefix="stock_")
    ok = fail = 0
    for it in items:
        url = large_url(it["img"])
        dest = os.path.join(tmp, it["asin"] + ".jpg")
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
                f.write(r.read())
            if os.path.getsize(dest) < 5000:
                raise ValueError("too small, likely placeholder")
        except Exception as e:
            print("download fail", it["asin"], e)
            fail += 1
            continue
        cmd = [sys.executable, CDB, "add", "--niche", niche, "--image", dest,
               "--title", it.get("title") or "", "--asin", it["asin"],
               "--marketplace", "amazon.com", "--source", "stocking run"]
        if it.get("rating") is not None:
            cmd += ["--rating", str(it["rating"])]
        if it.get("reviews") is not None:
            cmd += ["--reviews", str(it["reviews"])]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            ok += 1
        else:
            print("add fail", it["asin"], r.stdout, r.stderr)
            fail += 1
    print(f"{niche}: banked {ok}, failed {fail}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
