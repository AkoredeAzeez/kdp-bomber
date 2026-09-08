#!/usr/bin/env python3
"""
EDITORIAL READABILITY + AI-TELL AUDIT - uapf-editorial-pass
===========================================================
Scores a chapter (DOCX, MD, or TXT) for:
  1. Readability vs the locked audience band (Flesch Reading Ease + FK grade)
  2. AI "tells": stock phrases, uniform sentence rhythm, repeated sentence
     starters, robotic paragraph uniformity, duplicated sentences
Exit 0 = PASS, 1 = WARN (advisory), 2 = FAIL (block chapter advancement).

Usage:
  python readability.py <file> [--audience children|general|senior|professional]
                               [--json out.json]
"""
import argparse, json, math, os, re, statistics, sys

STOCK_PHRASES = [
    "in today's fast-paced world", "it's important to note", "it is important to note",
    "delve into", "delving into", "embark on a journey", "embark on this journey",
    "a testament to", "tapestry of", "treasure trove", "game-changer", "game changer",
    "look no further", "unlock the", "unlocking the", "elevate your",
    "navigate the world of", "navigating the world of", "the landscape of",
    "a beacon of", "dive into the world", "in the realm of", "whether you're a",
    "at the end of the day", "when it comes to", "in conclusion,",
    "seamlessly", "revolutionize", "harness the power", "the power of",
    "let's explore", "in this chapter, we will", "as we have seen",
    "needless to say", "without further ado", "rich tapestry",
]
CONNECTOR_OVERUSE = ["furthermore", "moreover", "additionally", "however"]

AUDIENCE_BANDS = {
    # name: (min Flesch Reading Ease, max FK grade) targets
    "children":     (80.0, 6.0),
    "general":      (55.0, 10.0),
    "senior":       (60.0, 9.0),
    "health":       (40.0, 13.0),   # patient-facing medical: necessary terminology inflates scores
    "professional": (30.0, 16.0),
}

def read_text(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".docx":
        import docx
        d = docx.Document(path)
        return "\n\n".join(p.text for p in d.paragraphs if p.text.strip())
    return open(path, encoding="utf-8", errors="replace").read()

def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    groups = re.findall(r"[aeiouy]+", w)
    n = len(groups)
    if w.endswith("e") and not w.endswith(("le", "ee")) and n > 1:
        n -= 1
    return max(1, n)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--audience", default="general", choices=list(AUDIENCE_BANDS))
    ap.add_argument("--json")
    a = ap.parse_args()

    text = read_text(a.file)
    # strip md furniture
    text = re.sub(r"^#+\s.*$|\|.*\||^[-*]\s|!\[.*?\]\(.*?\)|\[|\]", " ", text, flags=re.M)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if len(p.split()) >= 8]
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.split()) >= 3]
    words = re.findall(r"[A-Za-z']+", text)
    if len(words) < 150:
        print("PASS (too short to score meaningfully)")
        return
    n_w, n_s = len(words), max(1, len(sentences))
    n_syl = sum(syllables(w) for w in words)

    fre = 206.835 - 1.015 * (n_w / n_s) - 84.6 * (n_syl / n_w)
    fk = 0.39 * (n_w / n_s) + 11.8 * (n_syl / n_w) - 15.59

    low = text.lower()
    stock_hits = {p: low.count(p) for p in STOCK_PHRASES if low.count(p)}
    stock_per_1k = sum(stock_hits.values()) / (n_w / 1000.0)
    conn_per_1k = sum(low.count(c) for c in CONNECTOR_OVERUSE) / (n_w / 1000.0)

    # rhythm: sentence-length variance (robotic prose has low variation)
    slens = [len(s.split()) for s in sentences]
    rhythm_cv = (statistics.pstdev(slens) / statistics.mean(slens)) if len(slens) > 5 else 1.0

    # repeated sentence starters
    starters = [s.split()[0].lower().strip(",.;:") for s in sentences if s.split()]
    top_starter_share = (max(starters.count(x) for x in set(starters)) / len(starters)) if starters else 0

    # paragraph uniformity
    plens = [len(p.split()) for p in paragraphs]
    para_cv = (statistics.pstdev(plens) / statistics.mean(plens)) if len(plens) > 4 else 1.0

    # exact duplicate sentences (8+ words)
    longs = [s.lower() for s in sentences if len(s.split()) >= 8]
    dupes = len(longs) - len(set(longs))

    min_fre, max_fk = AUDIENCE_BANDS[a.audience]
    problems, warns = [], []
    if fre < min_fre - 10 or fk > max_fk + 3:
        problems.append(f"readability far off audience band ({a.audience}): FRE {fre:.0f} (target >={min_fre:.0f}), FK grade {fk:.1f} (target <={max_fk:.0f})")
    elif fre < min_fre or fk > max_fk:
        warns.append(f"readability slightly off band: FRE {fre:.0f}, FK {fk:.1f}")
    if stock_per_1k >= 3.0:
        problems.append(f"stock AI phrases: {stock_per_1k:.1f}/1k words: " + ", ".join(list(stock_hits)[:6]))
    elif stock_per_1k >= 1.2:
        warns.append(f"stock phrases creeping in ({stock_per_1k:.1f}/1k): " + ", ".join(list(stock_hits)[:4]))
    if conn_per_1k >= 5.0:
        warns.append(f"connector overuse (furthermore/moreover/additionally/however): {conn_per_1k:.1f}/1k")
    if rhythm_cv < 0.32:
        problems.append(f"robotic sentence rhythm (length variation {rhythm_cv:.2f}; healthy prose >0.40)")
    elif rhythm_cv < 0.40:
        warns.append(f"sentence rhythm getting uniform ({rhythm_cv:.2f})")
    if top_starter_share > 0.22:
        warns.append(f"{top_starter_share:.0%} of sentences start with the same word")
    if para_cv < 0.25:
        warns.append(f"paragraph lengths near-uniform ({para_cv:.2f}); vary structure")
    if dupes:
        problems.append(f"{dupes} exactly duplicated sentence(s) inside the chapter")

    verdict = "FAIL" if problems else ("WARN" if warns else "PASS")
    print(f"{verdict}  ({os.path.basename(a.file)}, {n_w} words, audience={a.audience})")
    print(f"  FRE {fre:.0f} | FK grade {fk:.1f} | rhythm {rhythm_cv:.2f} | stock {stock_per_1k:.1f}/1k")
    for p in problems: print("  FAIL:", p)
    for w in warns:    print("  warn:", w)
    if a.json:
        json.dump({"verdict": verdict, "fre": round(fre, 1), "fk_grade": round(fk, 1),
                   "rhythm_cv": round(rhythm_cv, 2), "stock_per_1k": round(stock_per_1k, 2),
                   "stock_hits": stock_hits, "duplicate_sentences": dupes,
                   "problems": problems, "warnings": warns},
                  open(a.json, "w", encoding="utf-8"), indent=2)
    sys.exit(0 if verdict == "PASS" else (1 if verdict == "WARN" else 2))

if __name__ == "__main__":
    main()
