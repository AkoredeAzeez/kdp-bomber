---
name: uapf-series-engine
description: Plan and produce a coherent multi-book series. Defines one shared brand (author, audience, look, series name, reading order), then produces each book through the normal pipeline while keeping every title unique (No-Two-Books-Alike). Maintains a series ledger, generates cross-promotion back matter, and preps the KDP Series link. Use when the operator wants a series rather than a single book.
---

# UAPF Series Engine

Turn one idea into a coherent line of books that sell each other. The series shares a brand and a look; every individual book stays a unique design (No-Two-Books-Alike). Genie keeps the plan in series.json and produces each book with the normal skills.

## When to run
- The operator wants a SERIES (several linked books), or wants to extend an existing series with another title.

## The series brand versus No-Two-Books-Alike
- SHARED across the series (constant): author or pen name, target audience, trim size, the premium-interior SYSTEM, a series name and a small series label or motif on every cover, and the reading-order logic.
- UNIQUE per book (never repeated): the specific concept, palette, cover art, motif arrangement, and design fingerprint. The series look is a frame; each book fills it differently. Never ship two books in the series with the same palette or cover layout.

## Workflow
1. Define the series with the operator: name, author or pen name, audience, promise, trim, naming convention (numbered or themed), and how many books to start with.
2. Choose each book's angle. Optionally run uapf-niche-finder on each candidate angle and keep the ones that score well, so the series is built on real demand, not guesses.
3. Create the ledger:
   python genie_series.py --series series.json init --name "NAME" --author "AUTHOR" --audience "..." --brand "..." --naming "..." --trim 6x9
   Then add each planned book:
   python genie_series.py --series series.json add --title "TITLE" --angle "ANGLE" --blurb "one line"
4. Produce each book through the normal pipeline (manuscript, low-content interior if applicable, cover via uapf-cover-reference then uapf-chatgpt-cover-pipeline, metadata via uapf-kdp-assets). Keep the shared brand on the cover (series label) and a unique design per book.
5. Before finalizing each book, add its cross-promotion back matter:
   python genie_series.py --series series.json backmatter --for "TITLE" --out backmatter.md
   Insert that "More in this series" page into the book's back matter. It lists the other titles, never the current one.
6. As books publish, record status and ASIN:
   python genie_series.py --series series.json set --title "TITLE" --status published --asin ASIN
7. Regenerate the overview any time:
   python genie_series.py --series series.json overview --out series_overview.html

## KDP Series linking (operator step)
Amazon can group the books into one Series page. After 2 or more books are live, tell the operator the series name and reading order to enter in KDP (Bookshelf, then Create Series). Genie preps the name and order; the operator does the KDP action. Never invent an ASIN or claim a series page exists before it does.

## Read-through and cross-promotion
- Every book ends with the "More in the [Series]" back-matter page.
- Consistent author or pen name across all books so Amazon groups them under one author.
- Consistent series label on each cover so buyers recognize the line on the shelf.
- Optionally open each book with a short "About this series" note.

## Hard rules
- No-Two-Books-Alike still governs every individual book: shared frame, unique execution. Two books that look alike is a failure.
- Real data only: never fabricate an ASIN, a sales rank, a review, or a "bestselling series" claim.
- The pen name is one consistent identity across the series, screened for collisions, never paired with fabricated credentials.
- Every book still passes its own full QA and the global hard rules (content standards, no em dashes, no publisher name in reader-facing content, no ISBN placeholder, margins and captions).
- Per-book operator confirmation before any publish click, always.
