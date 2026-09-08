#!/usr/bin/env python3
"""
CATALOG SELF-PLAGIARISM CHECK - uapf-editorial-pass
===================================================
Detects near-duplicate content ACROSS different books in the catalog
(an account-risk vector on KDP as a catalog grows). Shingle-based
(8-word shingles, hashed) Jaccard similarity between chapter files of
DIFFERENT book projects. Same-book files are never compared.

Usage:
  python catalog_similarity.py [--roots Books projects] [--warn 0.20] [--fail 0.35]
  python catalog_similarity.py --file <new_chapter.md>   # compare one new file vs catalog

Exit 0 = clean, 1 = warnings, 2 = failures (pairs above --fail).
"""
import argparse, hashlib, os, re, sys

def shingles(text, k=8):
    words = re.findall(r"[a-z']+", text.lower())
    return {hashlib.md5(" ".join(words[i:i+k]).encode()).hexdigest()[:12]
            for i in range(len(words) - k + 1)}

def read_any(path):
    if path.lower().endswith(".docx"):
        try:
            import docx
            return "\n".join(p.text for p in docx.Document(path).paragraphs)
        except Exception:
            return ""
    try:
        return open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""

def collect(roots):
    """{book_folder_name: [(path, shingle_set), ...]}"""
    out = {}
    for root in roots:
        if not os.path.isdir(root):
            continue
        for book in sorted(os.listdir(root)):
            bdir = os.path.join(root, book)
            if not os.path.isdir(bdir):
                continue
            files = []
            for r, ds, fs in os.walk(bdir):
                ds[:] = [d for d in ds if d not in ("images", "cover", "aplus", "__pycache__")]
                for f in fs:
                    if f.lower().endswith((".md", ".txt")) and not f.startswith(("handoff", "next_action", "README")):
                        p = os.path.join(r, f)
                        t = read_any(p)
                        if len(t.split()) >= 250:
                            files.append((p, shingles(t)))
            if files:
                out.setdefault(book, []).extend(files)
    return out

def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--roots", nargs="*", default=["Books", "projects"])
    ap.add_argument("--file", help="compare one file against the whole catalog")
    ap.add_argument("--warn", type=float, default=0.20)
    ap.add_argument("--fail", type=float, default=0.35)
    a = ap.parse_args()

    catalog = collect(a.roots)
    pairs = []
    if a.file:
        mine = shingles(read_any(a.file))
        my_book = os.path.basename(os.path.dirname(os.path.abspath(a.file)))
        for book, files in catalog.items():
            if book.lower() in os.path.abspath(a.file).lower():
                continue
            for p, s in files:
                j = jaccard(mine, s)
                if j >= a.warn:
                    pairs.append((j, a.file, p))
    else:
        books = list(catalog)
        for i in range(len(books)):
            for k in range(i + 1, len(books)):
                for p1, s1 in catalog[books[i]]:
                    for p2, s2 in catalog[books[k]]:
                        j = jaccard(s1, s2)
                        if j >= a.warn:
                            pairs.append((j, p1, p2))

    pairs.sort(reverse=True)
    fails = [p for p in pairs if p[0] >= a.fail]
    n_books = len(catalog)
    n_files = sum(len(v) for v in catalog.values())
    print(f"catalog: {n_books} books, {n_files} chapter files compared")
    if not pairs:
        print("CLEAN: no cross-book similarity above warn threshold "
              f"({a.warn:.0%})")
        sys.exit(0)
    for j, p1, p2 in pairs[:20]:
        tag = "FAIL" if j >= a.fail else "warn"
        print(f"  {tag} {j:.0%}  {p1}\n            <-> {p2}")
    print(f"{'FAIL' if fails else 'WARN'}: {len(fails)} pair(s) over {a.fail:.0%}, "
          f"{len(pairs)-len(fails)} over {a.warn:.0%}. Rewrite overlapping "
          "passages so no two books share prose.")
    sys.exit(2 if fails else 1)

if __name__ == "__main__":
    main()
