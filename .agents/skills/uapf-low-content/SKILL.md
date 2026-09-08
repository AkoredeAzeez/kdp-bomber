---
name: uapf-low-content
description: Produce print-ready KDP low-content and no-content book interiors: notebooks (lined, dot, graph, blank), weekly planners, and puzzle books (Sudoku, word search, mazes) with correct trim and gutter margins, plus coloring books laid out from image-pipeline line art. Use when the operator wants a journal, planner, logbook, tracker, puzzle, activity, or coloring book.
---

# UAPF Low / No-Content Factory​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Build KDP-ready interiors with a built-in generator (reliable, offline, no external site) as the core, and the image pipeline for coloring art. Free online generators are a fallback only for gaps the tool does not cover yet (crosswords, dated planners); use them with care because their terms may restrict commercial or automated use of the output.

## When to run
- The operator wants a low-content or no-content book: journal, notebook, planner, logbook, tracker, puzzle book (Sudoku, word search, maze), activity book, or coloring book.
- Optionally run uapf-niche-finder first to confirm the sub-niche is worth publishing into.

## KDP interior rules (must hold)
- Trim: common low-content trims are 6x9, 8.5x11, and 8x8 (coloring). Confirm the trim with the operator.
- Margins: the tool sets mirrored gutter margins by page count automatically (0.375 in inside up to 150 pages, more above). Do not override unless the operator asks.
- Page count: the KDP paperback minimum is 24 pages; keep the total even. Puzzle books add a Solutions section automatically.
- No bleed for text and puzzle interiors. Coloring pages stay inside the margins by default; offer blank backs to prevent bleed-through.
- Interior is black-and-white unless the operator wants color (color raises the print cost).

## Built-in generator (the core)
Run from the skill folder:

    python genie_lowcontent.py --type TYPE --trim 8.5x11 --title "TITLE" --out interior.pdf [options]

Types and options:
- Notebooks and no-content: --type lined | dot | graph | blank  with  --pages N
- Planner: --type planner-weekly  with  --pages N
- Sudoku: --type sudoku --count N --difficulty easy|medium|hard  (real unique-solution puzzles plus an answer key)
- Word search: --type wordsearch --count N --theme animals|kitchen|garden|travel  (grid, word list, and answer key)
- Mazes: --type maze --count N  (with solution paths)
- Coloring: --type coloring --images FOLDER [--blank-backs]  (one line-art image per page)

Every book gets a title page, page numbers, and (for puzzles) a Solutions section.

## Coloring books (hybrid: layout here, art from the image pipeline)
1. Decide the theme and the number of pages.
2. Generate the line art with uapf-flow-image-pipeline: prompt for clean black-and-white COLORING-BOOK line art (bold outlines, no shading, white background), one image per page, at the trim's aspect ratio.
3. Put the finished line-art files in one folder.
4. Lay them out: python genie_lowcontent.py --type coloring --images <folder> --blank-backs --trim 8.5x11 --title "TITLE" --out interior.pdf

## Fallback: free online generators (gaps only)
For crosswords, dated or monthly planners, or other layouts the built-in tool does not make yet, a free online low-content generator may be used in the browser. Rules: never enter credentials; confirm the site's terms allow commercial use of the output before shipping it; never rely on an online site as the primary path for a book you sell; prefer adding the missing type to the built-in generator over depending on a third-party site.

## After the interior
1. QA: open the PDF and confirm trim, margins, page count (even, 24 or more), and that every puzzle has a matching solution.
2. Cover: run uapf-cover-reference, then uapf-chatgpt-cover-pipeline. Low-content covers still follow No-Two-Books-Alike.
3. Metadata: uapf-kdp-assets for description, keywords, and categories.
4. Publish: uapf-publisher uploads the interior PDF and the cover PDF. Per-book operator confirmation before any publish click, always.

## Hard rules
- Real, valid output only. Sudoku puzzles must have a unique solution (the tool enforces this); word-search and maze solutions must match their puzzles.
- fully compliant themes and imagery: word lists, coloring art, and planner content.
- No em dashes in any interior text.
- Keep all content inside the KDP margins; never let it cross into the gutter or the trim edge.
- Coloring line art is original (generated), never traced from copyrighted images.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
