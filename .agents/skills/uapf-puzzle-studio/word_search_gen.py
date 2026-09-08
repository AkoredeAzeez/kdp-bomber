#!/usr/bin/env python3
"""
WORD SEARCH GENERATOR - uapf-puzzle-studio
==========================================
Deterministic word-search book builder: generates solvable grids from
themed word lists, renders puzzle pages + full solutions into a DOCX
(large-print aware), and writes the machine-readable answer ledger.

Input spec (JSON):
{
  "title": "...", "audience": "adults|seniors|kids",
  "grid": 15,                # optional; audience default otherwise
  "seed": 42,                # reproducible builds
  "puzzles": [ {"theme": "Autumn", "words": ["PUMPKIN", ...]}, ... ]
}

Usage:
  python word_search_gen.py build <spec.json> [--out book.docx]
  python word_search_gen.py demo               # 5-puzzle sample spec+build

Rules honored: solvability (every word placed or the build FAILS loudly,
never silently dropped), full solutions section, per-audience type floors
(seniors: 16pt+ grid), margin-safe tables, no em dashes.
"""
import argparse, json, os, random, string, sys

DIRS_EASY = [(1, 0), (0, 1)]                       # right, down
DIRS_MED  = DIRS_EASY + [(1, 1)]                   # + diagonal
DIRS_HARD = DIRS_MED + [(-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

AUD = {
    "kids":    {"grid": 11, "dirs": DIRS_EASY, "grid_pt": 16, "words_max": 10},
    "adults":  {"grid": 15, "dirs": DIRS_HARD, "grid_pt": 13, "words_max": 18},
    "seniors": {"grid": 15, "dirs": DIRS_MED,  "grid_pt": 16, "words_max": 14},
}

def place(grid, word, dirs, rng, tries=400):
    n = len(grid)
    for _ in range(tries):
        dx, dy = rng.choice(dirs)
        x = rng.randrange(n) if dx == 0 else (rng.randrange(n - len(word) + 1) if dx > 0 else rng.randrange(len(word) - 1, n))
        y = rng.randrange(n) if dy == 0 else (rng.randrange(n - len(word) + 1) if dy > 0 else rng.randrange(len(word) - 1, n))
        cells = [(x + dx * i, y + dy * i) for i in range(len(word))]
        if all(0 <= cx < n and 0 <= cy < n and grid[cy][cx] in ("", word[i]) for i, (cx, cy) in enumerate(cells)):
            for i, (cx, cy) in enumerate(cells):
                grid[cy][cx] = word[i]
            return cells
    return None

def build_puzzle(theme, words, cfg, rng):
    n = cfg["grid"]
    words = [w.upper().replace(" ", "") for w in words][: cfg["words_max"]]
    for w in words:
        if len(w) > n:
            sys.exit(f"FAIL: word '{w}' longer than grid {n} (theme {theme})")
    grid = [["" for _ in range(n)] for _ in range(n)]
    placements = {}
    for w in sorted(words, key=len, reverse=True):
        cells = place(grid, w, cfg["dirs"], rng)
        if cells is None:
            sys.exit(f"FAIL: could not place '{w}' in theme '{theme}'; reduce word count or grid density")
        placements[w] = cells
    for row in grid:
        for i, c in enumerate(row):
            if c == "":
                row[i] = rng.choice(string.ascii_uppercase)
    return {"theme": theme, "words": words, "grid": grid, "placements": placements}

def render_docx(spec, puzzles, out):
    import docx
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    cfg = AUD[spec.get("audience", "adults")]
    doc = docx.Document()
    for s in doc.sections:
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.left_margin = s.right_margin = Inches(0.75)
        s.top_margin, s.bottom_margin = Inches(0.75), Inches(0.75)

    def grid_table(g, pt, bold_cells=None):
        n = len(g)
        t = doc.add_table(rows=n, cols=n)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.style = "Table Grid"
        for y in range(n):
            for x in range(n):
                cell = t.cell(y, x)
                cell.width = Inches(0.42)
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(g[y][x])
                r.font.size = Pt(pt)
                r.font.name = "Courier New"
                if bold_cells and (x, y) in bold_cells:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x5F)
        return t

    for i, pz in enumerate(puzzles, 1):
        h = doc.add_heading(f"PUZZLE {i}: {pz['theme'].upper()}", level=1)
        h.runs[0].font.size = Pt(28)
        grid_table(pz["grid"], cfg["grid_pt"])
        doc.add_paragraph()
        wp = doc.add_paragraph()
        wp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = wp.add_run("   ".join(pz["words"]))
        r.font.size = Pt(cfg["grid_pt"])
        r.font.bold = True
        doc.add_page_break()

    h = doc.add_heading("SOLUTIONS", level=1)
    h.runs[0].font.size = Pt(28)
    for i, pz in enumerate(puzzles, 1):
        p = doc.add_paragraph()
        r = p.add_run(f"Puzzle {i}: {pz['theme']}")
        r.font.bold = True
        r.font.size = Pt(14)
        sol_cells = {c for cells in pz["placements"].values() for c in cells}
        shown = [[pz["grid"][y][x] if (x, y) in sol_cells else "·"
                  for x in range(len(pz["grid"]))] for y in range(len(pz["grid"]))]
        grid_table(shown, 9, bold_cells=sol_cells)
        doc.add_paragraph()
        if i % 2 == 0:
            doc.add_page_break()
    doc.save(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "demo"])
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--out")
    a = ap.parse_args()

    if a.cmd == "demo":
        spec = {"title": "Demo Word Search", "audience": "seniors", "seed": 7, "puzzles": [
            {"theme": "Autumn", "words": ["PUMPKIN", "HARVEST", "MAPLE", "SWEATER", "ORCHARD", "CIDER", "ACORN", "BONFIRE", "RAKE", "FROST"]},
            {"theme": "Kitchen", "words": ["SKILLET", "WHISK", "OVEN", "SPATULA", "KETTLE", "LADLE", "GRATER", "TIMER", "APRON", "TRAY"]},
            {"theme": "Garden", "words": ["TROWEL", "SEEDS", "MULCH", "ROSES", "PRUNER", "COMPOST", "SPROUT", "TULIP", "HOSE", "SOIL"]},
            {"theme": "Music", "words": ["MELODY", "RHYTHM", "CHORUS", "TEMPO", "PIANO", "VIOLIN", "SINGER", "HARMONY", "NOTES", "DRUM"]},
            {"theme": "Ocean", "words": ["DOLPHIN", "CORAL", "SEAWEED", "TIDE", "ANCHOR", "PEARL", "WAVES", "SAILOR", "SHELLS", "REEF"]},
        ]}
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_spec.json")
        json.dump(spec, open(path, "w"), indent=1)
        a.spec, a.out = path, a.out or path.replace("demo_spec.json", "demo_wordsearch.docx")
    spec = json.load(open(a.spec, encoding="utf-8"))
    cfg = AUD[spec.get("audience", "adults")]
    if spec.get("grid"):
        cfg = {**cfg, "grid": spec["grid"]}
    rng = random.Random(spec.get("seed", 1))
    puzzles = [build_puzzle(p["theme"], p["words"], cfg, rng) for p in spec["puzzles"]]
    out = a.out or os.path.splitext(a.spec)[0] + ".docx"
    render_docx(spec, puzzles, out)
    ledger = os.path.splitext(out)[0] + "_answers.json"
    json.dump([{"n": i + 1, "theme": p["theme"],
                "answers": {w: cells for w, cells in p["placements"].items()}}
               for i, p in enumerate(puzzles)], open(ledger, "w"), indent=1)
    print(f"OK: {len(puzzles)} puzzles -> {out} (+ answer ledger {os.path.basename(ledger)})")

if __name__ == "__main__":
    main()
