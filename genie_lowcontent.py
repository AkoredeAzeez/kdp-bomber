#!/usr/bin/env python3
"""
GENIE LOW / NO-CONTENT FACTORY
==============================
Generates print-ready KDP interior PDFs (vector, crisp) with correct trim size,
mirrored gutter margins by page count, and page numbers.

Types:
  Notebooks/no-content : lined | dot | graph | blank
  Planner              : planner-weekly
  Puzzle books         : sudoku | wordsearch | maze   (each with a solutions section)

Examples:
  python genie_lowcontent.py --type lined --trim 6x9 --pages 120 --title "My Notebook" --out interior.pdf
  python genie_lowcontent.py --type sudoku --trim 8.5x11 --count 50 --difficulty medium --title "Sudoku" --out sud.pdf
  python genie_lowcontent.py --type wordsearch --trim 8.5x11 --count 40 --theme animals --title "Word Search" --out ws.pdf
  python genie_lowcontent.py --type maze --trim 8.5x11 --count 40 --title "Mazes" --out mz.pdf

Coloring books are NOT here: their line-art comes from the image pipeline; this
tool lays out deterministic interiors only.
"""
import argparse, hashlib, random
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# ── KDP geometry ─────────────────────────────────────────────────────────────
def inside_margin_in(pages):
    if pages <= 150: return 0.375
    if pages <= 300: return 0.5
    if pages <= 500: return 0.625
    if pages <= 700: return 0.75
    return 0.875

def rect(page_no, W, H, pages):
    """Content rectangle in points for a 1-indexed page (odd = right-hand)."""
    inside = (inside_margin_in(pages) + 0.125) * inch
    outer, top, bottom = 0.5 * inch, 0.5 * inch, 0.6 * inch
    if page_no % 2 == 1:      # right-hand page: gutter on the left
        x0, x1 = inside, W - outer
    else:                      # left-hand page: gutter on the right
        x0, x1 = outer, W - inside
    return x0, bottom, x1, H - top

def footer(c, page_no, W):
    c.setFont("Helvetica", 9)
    c.setFillGray(0.5)
    c.drawCentredString(W / 2, 0.35 * inch, str(page_no))
    c.setFillGray(0)

def title_page(c, W, H, title, subtitle=""):
    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(W / 2, H * 0.6, title[:40])
    if subtitle:
        c.setFont("Helvetica", 14)
        c.drawCentredString(W / 2, H * 0.6 - 30, subtitle[:60])
    c.showPage()

# ── Notebook / planner pages ─────────────────────────────────────────────────
def page_lined(c, r, spacing=0.32 * inch):
    x0, y0, x1, y1 = r
    c.setStrokeGray(0.6); c.setLineWidth(0.6)
    y = y1 - spacing
    while y > y0:
        c.line(x0, y, x1, y); y -= spacing

def page_dot(c, r, spacing=0.22 * inch):
    x0, y0, x1, y1 = r
    c.setFillGray(0.55)
    y = y1
    while y > y0:
        x = x0
        while x < x1:
            c.circle(x, y, 0.9, stroke=0, fill=1); x += spacing
        y -= spacing
    c.setFillGray(0)

def page_graph(c, r, spacing=0.22 * inch):
    x0, y0, x1, y1 = r
    c.setStrokeGray(0.7); c.setLineWidth(0.4)
    x = x0
    while x <= x1:
        c.line(x, y0, x, y1); x += spacing
    y = y0
    while y <= y1:
        c.line(x0, y, x1, y); y += spacing

def page_planner_weekly(c, r):
    x0, y0, x1, y1 = r
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday / Sunday", "Notes"]
    n = len(days); h = (y1 - y0) / n
    c.setStrokeGray(0.3); c.setLineWidth(0.8)
    for i, d in enumerate(days):
        yy = y1 - i * h
        c.rect(x0, yy - h, x1 - x0, h, stroke=1, fill=0)
        c.setFont("Helvetica-Bold", 11); c.drawString(x0 + 6, yy - 16, d)
        c.setStrokeGray(0.75); c.setLineWidth(0.4)
        ly = yy - 30
        while ly > yy - h + 6:
            c.line(x0 + 6, ly, x1 - 6, ly); ly -= 0.28 * inch
        c.setStrokeGray(0.3); c.setLineWidth(0.8)

# ── Sudoku ───────────────────────────────────────────────────────────────────
def _sudoku_full():
    g = [[0] * 9 for _ in range(9)]
    def ok(r, cc, v):
        if any(g[r][i] == v for i in range(9)): return False
        if any(g[i][cc] == v for i in range(9)): return False
        br, bc = 3 * (r // 3), 3 * (cc // 3)
        return all(g[br + i][bc + j] != v for i in range(3) for j in range(3))
    def fill(p=0):
        if p == 81: return True
        r, cc = divmod(p, 9)
        nums = list(range(1, 10)); random.shuffle(nums)
        for v in nums:
            if ok(r, cc, v):
                g[r][cc] = v
                if fill(p + 1): return True
                g[r][cc] = 0
        return False
    fill(); return g

def _count_solutions(g, limit=2):
    for r in range(9):
        for cc in range(9):
            if g[r][cc] == 0:
                cnt = 0
                for v in range(1, 10):
                    if (all(g[r][i] != v for i in range(9)) and all(g[i][cc] != v for i in range(9))
                            and all(g[3*(r//3)+i][3*(cc//3)+j] != v for i in range(3) for j in range(3))):
                        g[r][cc] = v; cnt += _count_solutions(g, limit); g[r][cc] = 0
                        if cnt >= limit: return cnt
                return cnt
    return 1

def make_sudoku(difficulty="medium"):
    givens = {"easy": 40, "medium": 32, "hard": 26}.get(difficulty, 32)
    full = _sudoku_full()
    puzzle = [row[:] for row in full]
    cells = [(r, c) for r in range(9) for c in range(9)]; random.shuffle(cells)
    remaining = 81
    for (r, c) in cells:
        if remaining <= givens: break
        saved = puzzle[r][c]; puzzle[r][c] = 0
        if _count_solutions([row[:] for row in puzzle]) != 1:
            puzzle[r][c] = saved
        else:
            remaining -= 1
    return puzzle, full

def draw_grid9(c, r, grid, small=False):
    x0, y0, x1, y1 = r
    side = min(x1 - x0, y1 - y0)
    ox = x0 + ((x1 - x0) - side) / 2
    oy = y0 + ((y1 - y0) - side) / 2
    cell = side / 9
    for i in range(10):
        w = 1.6 if i % 3 == 0 else 0.5
        c.setLineWidth(w)
        c.line(ox + i * cell, oy, ox + i * cell, oy + side)
        c.line(ox, oy + i * cell, ox + side, oy + i * cell)
    c.setFont("Helvetica", (cell * 0.55))
    for rr in range(9):
        for cc in range(9):
            v = grid[rr][cc]
            if v:
                c.drawCentredString(ox + cc * cell + cell / 2,
                                    oy + (8 - rr) * cell + cell * 0.28, str(v))

# ── Word search ──────────────────────────────────────────────────────────────
THEMES = {
    "animals": "TIGER LION ZEBRA HORSE EAGLE SHARK WHALE PANDA KOALA OTTER RABBIT MONKEY DONKEY FALCON TURTLE".split(),
    "kitchen": "SPOON KNIFE PLATE WHISK LADLE GRATER KETTLE SKILLET SPATULA COLANDER PITCHER BLENDER TEAPOT".split(),
    "garden": "FLOWER PETAL LEAF ROOTS SEEDS SHOVEL TROWEL HEDGE MULCH BLOOM SPROUT ORCHID DAISY TULIP".split(),
    "travel": "PLANE TRAIN HOTEL BEACH VISA MAPS CABIN FLIGHT PASSPORT LUGGAGE CAMERA JOURNEY TICKET".split(),
}
def make_wordsearch(words, size=15):
    grid = [["" for _ in range(size)] for _ in range(size)]
    dirs = [(0,1),(1,0),(1,1),(-1,1),(0,-1),(-1,0),(-1,-1),(1,-1)]
    placed = []
    for w in sorted(words, key=len, reverse=True):
        w = w.upper()
        if len(w) > size: continue
        ok = False
        for _ in range(200):
            dr, dc = random.choice(dirs)
            r = random.randrange(size); cc = random.randrange(size)
            er = r + dr * (len(w) - 1); ec = cc + dc * (len(w) - 1)
            if not (0 <= er < size and 0 <= ec < size): continue
            good = True
            for i, ch in enumerate(w):
                cur = grid[r + dr * i][cc + dc * i]
                if cur and cur != ch: good = False; break
            if good:
                for i, ch in enumerate(w):
                    grid[r + dr * i][cc + dc * i] = ch
                placed.append((w, r, cc, dr, dc)); ok = True; break
    for r in range(size):
        for cc in range(size):
            if not grid[r][cc]:
                grid[r][cc] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return grid, placed

def draw_wordsearch(c, r, grid, words, solution=False, placed=None):
    x0, y0, x1, y1 = r
    size = len(grid)
    listh = 1.2 * inch
    side = min(x1 - x0, (y1 - y0) - listh)
    ox = x0 + ((x1 - x0) - side) / 2
    oy = y1 - side
    cell = side / size
    c.setFont("Helvetica", cell * 0.55)
    sol = set()
    if solution and placed:
        for (w, rr, cc, dr, dc) in placed:
            for i in range(len(w)):
                sol.add((rr + dr * i, cc + dc * i))
    for rr in range(size):
        for cc in range(size):
            cx = ox + cc * cell + cell / 2; cy = oy + (size - 1 - rr) * cell + cell * 0.28
            if (rr, cc) in sol:
                c.setFont("Helvetica-Bold", cell * 0.6); c.setFillGray(0)
            else:
                c.setFont("Helvetica", cell * 0.55); c.setFillGray(0.15 if not solution else 0.6)
            c.drawCentredString(cx, cy, grid[rr][cc])
    c.setFillGray(0)
    c.setFont("Helvetica", 10)
    cols = 4; per = (len(words) + cols - 1) // cols
    for i, w in enumerate(sorted(words)):
        col = i // per; row = i % per
        c.drawString(x0 + col * (x1 - x0) / cols, y0 + listh - 12 - row * 13, w.upper())

# ── Maze (recursive backtracker) ─────────────────────────────────────────────
def make_maze(n=18):
    # walls[r][c] = [top,right,bottom,left] present?
    walls = [[[True, True, True, True] for _ in range(n)] for _ in range(n)]
    vis = [[False] * n for _ in range(n)]
    stack = [(0, 0)]; vis[0][0] = True
    while stack:
        r, c = stack[-1]
        nb = []
        if r > 0 and not vis[r-1][c]: nb.append((r-1, c, 0))
        if c < n-1 and not vis[r][c+1]: nb.append((r, c+1, 1))
        if r < n-1 and not vis[r+1][c]: nb.append((r+1, c, 2))
        if c > 0 and not vis[r][c-1]: nb.append((r, c-1, 3))
        if not nb: stack.pop(); continue
        nr, nc, d = random.choice(nb)
        walls[r][c][d] = False; walls[nr][nc][(d + 2) % 4] = False
        vis[nr][nc] = True; stack.append((nr, nc))
    return walls

def solve_maze(walls):
    n = len(walls); import collections
    prev = {(0, 0): None}; q = collections.deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if (r, c) == (n-1, n-1): break
        moves = [(-1,0,0),(0,1,1),(1,0,2),(0,-1,3)]
        for dr, dc, d in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and not walls[r][c][d] and (nr, nc) not in prev:
                prev[(nr, nc)] = (r, c); q.append((nr, nc))
    path = []; cur = (n-1, n-1)
    while cur is not None: path.append(cur); cur = prev.get(cur)
    return path

def draw_maze(c, r, walls, path=None):
    x0, y0, x1, y1 = r
    n = len(walls)
    side = min(x1 - x0, y1 - y0)
    ox = x0 + ((x1 - x0) - side) / 2; oy = y0 + ((y1 - y0) - side) / 2
    cell = side / n
    c.setStrokeGray(0); c.setLineWidth(1.4)
    for rr in range(n):
        for cc in range(n):
            px = ox + cc * cell; py = oy + (n - 1 - rr) * cell
            w = walls[rr][cc]
            if w[0]: c.line(px, py + cell, px + cell, py + cell)
            if w[1]: c.line(px + cell, py, px + cell, py + cell)
            if w[2]: c.line(px, py, px + cell, py)
            if w[3]: c.line(px, py, px, py + cell)
    if path:
        c.setStrokeGray(0.5); c.setLineWidth(cell * 0.18)
        pts = [(ox + cc * cell + cell / 2, oy + (n - 1 - rr) * cell + cell / 2) for (rr, cc) in path]
        for i in range(len(pts) - 1):
            c.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1])

# ── Book assembly ────────────────────────────────────────────────────────────
def build(kind, out, trim, pages, count, title, difficulty, theme, seed, images_dir=None, blank_backs=False):
    W, H = trim[0] * inch, trim[1] * inch
    random.seed(seed)
    c = canvas.Canvas(out, pagesize=(W, H))

    if kind == "coloring":
        import os
        imgs = sorted(f for f in os.listdir(images_dir)
                      if f.lower().endswith((".png", ".jpg", ".jpeg"))) if images_dir else []
        if not imgs:
            raise SystemExit("coloring needs --images <folder> of line-art PNG/JPG files")
        total = 2 + len(imgs) * (2 if blank_backs else 1)
        title_page(c, W, H, title)
        pno = 2
        for f in imgs:
            r = rect(pno, W, H, total)
            c.drawImage(os.path.join(images_dir, f), r[0], r[1], width=r[2] - r[0], height=r[3] - r[1],
                        preserveAspectRatio=True, anchor="c", mask="auto")
            footer(c, pno, W); c.showPage(); pno += 1
            if blank_backs:
                footer(c, pno, W); c.showPage(); pno += 1
        c.save(); return pno - 1

    NOTEBOOK = {"lined": page_lined, "dot": page_dot, "graph": page_graph,
                "blank": lambda cc, r: None, "planner-weekly": page_planner_weekly}
    if kind in NOTEBOOK:
        title_page(c, W, H, title)
        total = pages
        for p in range(2, total + 1):
            NOTEBOOK[kind](c, rect(p, W, H, total)); footer(c, p, W); c.showPage()
        c.save(); return total

    # puzzle books: title, puzzles, solutions divider, solutions
    title_page(c, W, H, title, {"sudoku": "Difficulty: " + difficulty, "wordsearch": "Theme: " + theme, "maze": ""}.get(kind, ""))
    est_pages = 2 + count + 1 + count
    puzzles = []
    pno = 2
    if kind == "sudoku":
        for i in range(count):
            pz, full = make_sudoku(difficulty); puzzles.append((pz, full))
            r = rect(pno, W, H, est_pages)
            c.setFont("Helvetica-Bold", 14); c.drawString(r[0], r[3] - 6, f"Puzzle {i+1}")
            draw_grid9(c, (r[0], r[1], r[2], r[3] - 24), pz); footer(c, pno, W); c.showPage(); pno += 1
    elif kind == "wordsearch":
        words = THEMES.get(theme, THEMES["animals"])
        for i in range(count):
            grid, placed = make_wordsearch(words); puzzles.append((grid, placed, words))
            r = rect(pno, W, H, est_pages)
            c.setFont("Helvetica-Bold", 14); c.drawString(r[0], r[3] - 6, f"Puzzle {i+1}")
            draw_wordsearch(c, (r[0], r[1], r[2], r[3] - 24), grid, words); footer(c, pno, W); c.showPage(); pno += 1
    elif kind == "maze":
        for i in range(count):
            wl = make_maze(); puzzles.append(wl)
            r = rect(pno, W, H, est_pages)
            c.setFont("Helvetica-Bold", 14); c.drawString(r[0], r[3] - 6, f"Maze {i+1}")
            draw_maze(c, (r[0], r[1], r[2], r[3] - 24), wl); footer(c, pno, W); c.showPage(); pno += 1

    # solutions divider
    c.setFont("Helvetica-Bold", 28); c.drawCentredString(W / 2, H * 0.55, "Solutions"); footer(c, pno, W); c.showPage(); pno += 1
    for i, item in enumerate(puzzles):
        r = rect(pno, W, H, est_pages)
        c.setFont("Helvetica-Bold", 12); c.drawString(r[0], r[3] - 6, f"Solution {i+1}")
        inner = (r[0], r[1], r[2], r[3] - 20)
        if kind == "sudoku": draw_grid9(c, inner, item[1])
        elif kind == "wordsearch": draw_wordsearch(c, inner, item[0], item[2], solution=True, placed=item[1])
        elif kind == "maze": draw_maze(c, inner, item, path=solve_maze(item))
        footer(c, pno, W); c.showPage(); pno += 1
    c.save(); return pno - 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", required=True,
                    choices=["lined", "dot", "graph", "blank", "planner-weekly", "sudoku", "wordsearch", "maze", "coloring"])
    ap.add_argument("--images", help="folder of line-art PNG/JPG for --type coloring (from the image pipeline)")
    ap.add_argument("--blank-backs", action="store_true", help="insert a blank page after each coloring page (no bleed-through)")
    ap.add_argument("--trim", default="8.5x11")
    ap.add_argument("--pages", type=int, default=120)
    ap.add_argument("--count", type=int, default=40)
    ap.add_argument("--title", default="Activity Book")
    ap.add_argument("--difficulty", default="medium", choices=["easy", "medium", "hard"])
    ap.add_argument("--theme", default="animals")
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=None)
    a = ap.parse_args()
    w, h = (float(x) for x in a.trim.lower().split("x"))
    seed = a.seed if a.seed is not None else int(hashlib.sha256(a.title.encode()).hexdigest()[:8], 16)
    n = build(a.type, a.out, (w, h), a.pages, a.count, a.title, a.difficulty, a.theme, seed, a.images, a.blank_backs)
    print(f"Built {a.out}: {a.type}, trim {a.trim}, {n} pages.")

if __name__ == "__main__":
    main()
