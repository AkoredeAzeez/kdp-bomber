---
name: uapf-chatgpt-cover-pipeline
description: After a UAPF book's manuscript and metadata are finished, generate the complete cover with ChatGPT Image 2.0 as the SOLE cover generator. Download the best-selling competitor covers as references, run the house designer prompt with the references + manuscript to make the FRONT cover, get the exact paperback size from the KDP cover calculator, then generate the back cover, spine, and full paperback wrap and deliver it as a print-ready PDF. Also drives the A+ modules (ChatGPT Image 2.0). Runs in the browser on the operator's logged-in ChatGPT account.
---

# UAPF ChatGPT Cover Pipeline (ChatGPT Image 2.0, sole generator)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Art direction is governed by uapf-cover-aplus-designer (the master cover and
A+ skill): its concepts, per-niche pattern library, design law, and QA gate
direct what this pipeline generates. On any design-direction conflict, the
designer wins. STATUS (operator directive 2026-08-13): this browser pipeline
is the operator-led ALTERNATIVE for interactive art-direction sessions; the
DEFAULT engine for all cover and A+ production is CODEX (see the designer
skill's Codex engine section).**

**ChatGPT Image 2.0 (gpt-image-2) is the SOLE generator for covers and A+ content.**
Never use Google Flow, or any other generator, for a cover or A+ image. Flow remains the
photo generator for book interiors only.

Genie's job: gather references, upload the book, send the house designer prompt, get the
exact print dimensions, drive ChatGPT to produce the front cover and then the full
paperback wrap, finish it to a print-ready PDF, and generate the A+ modules.

## Preconditions
- Manuscript finished; final exact PAGE COUNT known.
- `[BookTitle]_KDP_Metadata.docx` exists (exact title, subtitle, author, description).
- Operator is logged into chatgpt.com in the browser (Genie NEVER enters credentials).
- Uploading the manuscript to ChatGPT sends the book to OpenAI; that is the operator's
  standing instruction for this pipeline. Upload only the finished manuscript and its
  reference covers, nothing else.
- Run every cover chat inside the ChatGPT project **"Pegasus Covers"** (installed
  2026-08-13). Its project instructions carry the Pegasus design law (exact strings
  and casing, bank-derived text treatment, 4-line title cap, wrap geometry, barcode
  zone, content restrictions), so any chat in that project acts as the house
  designer. The installed text is mirrored at
  `.agents/skills/uapf-cover-aplus-designer/chatgpt_standing_instruction.md`; if
  that file changes, re-paste it into the project's settings.

## Step 1 — Download the best-selling competitor covers (references)
Run **uapf-cover-reference** to pick the three best-selling competitor covers for this
title by Best Sellers Rank and download them to `cover_refs/`. Choose the **one or two**
strongest, most on-target covers as the reference image(s) for the designer prompt (the
lowest-BSR, closest-match ones). These are market inspiration only, never to be copied.

## Step 2 — Generate the FRONT cover with the house designer prompt
1. Open ChatGPT, start a new chat.
2. Upload the **1 to 2 reference covers** and the **finished manuscript** (PDF or DOCX).
3. Send the house cover-generation prompt verbatim from
   `references/kdp-cover-designer-prompt.md`, substituting:
   - the book's **exact** Title, Subtitle, and Author name (from the locked metadata),
   - the OUTPUT trim size and pixel dimensions to the book's **actual** trim (for 8.5 x 11
     that is 2550 x 3300 px at 300 DPI; for 6 x 9 it is 1800 x 2700 px; etc.),
   - the book's real category wording (cookbook, travel, workbook, ...) in place of
     "textbook" while keeping the same premium, market-driven discipline.
4. ChatGPT Image 2.0 generates the **front cover only** (flat, edge-to-edge, no spine, no
   back, no mockup). Inspect it: title/subtitle/author spelled exactly, sharp, premium,
   thumbnail-legible, original. Iterate up to 4 times for spelling or quality, then
   download the final front cover to the book folder as `front_cover.png`.

## Step 3 — Get the exact paperback size from the KDP cover calculator
Open https://kdp.amazon.com/cover-calculator and enter binding Paperback, interior type,
paper, the book's trim size, and the FINAL page count. Read the full-cover width x height,
spine width, and bleed, and multiply the inch dimensions by 300 for the print pixel target.
Record them (fall back to the formula in uapf-cover-canva-build only if the page is down).

## Step 4 — Generate the back cover, spine, and full paperback wrap
In the same ChatGPT chat, using the finished `front_cover.png` as the locked design
language (palette, typography, imagery), have ChatGPT Image 2.0 generate the **complete
paperback wrap in one image: back cover + spine + front cover, laid out left to right**, at
the exact calculator dimensions:
- full wrap [W] x [H] inches, spine [S] inches at the horizontal centre, 0.125 in bleed all
  sides, generated at the largest size in exactly these proportions;
- the **front** matches the approved front cover;
- the **spine** carries the title and author reading top to bottom (only at >=100 pages;
  centred, >=0.0625 in inside each fold);
- the **back cover** carries compelling back-cover copy written from the book, with a clear,
  light 2 x 1.2 inch barcode zone in the bottom-right, 0.25 in from the edges;
- all text spelled exactly; original design; Pegasus cover house rules apply.
Iterate for spelling, proportions, and the barcode zone. Download as `chatgpt_wrap.png`.

## Step 5 — Finish to a print-ready PDF (the paperback deliverable is a PDF)
Write `cover_config.json` (book_folder, trim sizes, page_count, paper, output_prefix) and run:
```powershell
python `
  "$env:LOCALAPPDATA\FlowPipeline\kdp_cover_wrap.py" --finish "<book_folder>\cover_config.json" chatgpt_wrap.png
```
This scales the wrap to the exact print pixels at 300 DPI and exports `<prefix>_WRAP.png`
plus **`<prefix>_WRAP.pdf`** (the paperback cover deliverable). It warns if the aspect ratio
drifts more than 3% (then regenerate at step 4 rather than accepting a crop). ChatGPT
outputs roughly 1 to 2K px, so upscaling to print size is the known trade-off; if fine text
looks soft at print size, run one more ChatGPT iteration asking for a cleaner, bolder text
treatment.

## Step 6 — Generate the A+ modules
Generate the **5 A+ Content modules** (uapf-kdp-assets) with **ChatGPT Image 2.0**, in the
same design language and palette as the cover, at Amazon A+ sizes. Never use Flow for A+.

## Step 7 — QA and report
- Zoom the finished PDF: title/subtitle/author spelled exactly; spine text inside the spine
  band; barcode zone clear and light; no upscaling artifacts that make text illegible.
- Report dimensions, file paths, iteration count, and an honest print-quality note.
- Deliverables: `front_cover.png`, `<prefix>_WRAP.pdf` (paperback), and the 5 A+ modules.
- Next: operator review; then uapf-publisher uploads the WRAP.pdf at the KDP cover step.
  Per-book operator confirmation before any publish click, always.

## Hard rules
1. **ChatGPT Image 2.0 is the sole cover and A+ generator. Never Flow for covers or A+.**
2. Dimensions always come from the KDP cover calculator (formula only as fallback).
3. Upload only the finished manuscript + its reference covers to ChatGPT; nothing else.
4. Spine text only at page count >= 100 (or spine >= 0.25 in); otherwise tell ChatGPT to
   leave the spine free of text.
5. The paperback cover deliverable is ALWAYS the PDF (`_WRAP.pdf`, 300 DPI). The PNG is a
   preview; uapf-publisher uploads the PDF at the KDP cover step, never the PNG.
6. References are market inspiration ONLY. Never copy, trace, or closely imitate a
   competitor cover; the design is original and unique (No-Two-Books-Alike).
7. Pegasus cover house rules apply: photorealistic imagery only; no icons, badges, vector,
   or clip art; no selling-point callouts on the cover; no violence or blood; no background
   base colour repeated within a five-cover window.
8. Login walls, quota refusals, or content refusals -> report BLOCKED to the operator;
   never work around them. Genie never enters credentials.

## Runtime
- Browser tools (in-app browser or Claude-in-Chrome) with the operator's ChatGPT session;
  file upload via the composer's attach control.
- Python 3.10+ with Pillow; finisher at `%LOCALAPPDATA%\FlowPipeline\kdp_cover_wrap.py`.
- The full house cover prompt is in `references/kdp-cover-designer-prompt.md`.
- A manual Canva template-build alternative exists in **uapf-cover-canva-build**, but
  ChatGPT Image 2.0 is the default sole generator for covers.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
