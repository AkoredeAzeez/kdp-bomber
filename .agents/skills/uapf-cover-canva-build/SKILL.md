---
name: uapf-cover-canva-build
description: Alternative cover build path. Assemble the print-ready KDP paperback or hardcover wrap in Canva from the KDP cover-calculator template, using cover artwork generated from cover_prompt.md. Produces one continuous back+spine+front wrap PDF at exact print dimensions. Use instead of uapf-chatgpt-cover-pipeline when building the wrap in Canva.
---

# UAPF Cover Build — Canva wrap (alternative path)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Two cover build paths exist and both are valid; pick one per book:
- **uapf-chatgpt-cover-pipeline** — ChatGPT generates the whole wrap as one image; a Python finisher scales it to print.
- **This skill (manual alternative)** — ChatGPT Image 2.0 generates the cover ARTWORK, then the wrap is assembled in Canva on the exact KDP cover-calculator template and exported as a print-ready PDF. Use only when the operator wants to hand-assemble in Canva; otherwise the default is uapf-chatgpt-cover-pipeline, where ChatGPT Image 2.0 is the sole generator and produces the full wrap directly. Covers never use Google Flow.

Art direction for either path is governed by **uapf-cover-aplus-designer** (the master cover and A+ skill); on any design-direction conflict, the designer wins. Both consume `cover_prompt.md` and the 2-3 references from uapf-cover-db / uapf-cover-reference, both honor the KDP zone rules and the Pegasus cover house rules below, and both deliver a single continuous back+spine+front wrap PDF. Amazon KDP does not accept separate front and back files. Full standalone guide: `references/KDP-Cover-Build-Guide-Canva.pdf`.

## Preconditions
- Manuscript finished; FINAL exact page count known, not an estimate.
- `[BookTitle]_KDP_Metadata.docx` (title, subtitle, author, blurb) and `cover_prompt.md` ready.
- Operator logged into Canva and kdp.amazon.com in the browser. Genie never enters credentials.

## Step 1 — Get the template from the KDP cover calculator
Open https://kdp.amazon.com/cover-calculator and enter: binding (paperback, or hardcover case laminate), interior type (B&W / standard colour / premium colour), paper type (white / cream / colour), page-turn direction, the EXACT final page count, and trim size + unit. Click **Calculate dimensions**, then **Download template** (a ZIP with a PNG and a PDF). Record the full-cover dimensions it reports (e.g. 6 x 9 at 200 pp white is roughly 12.700 x 9.250 in); you need it twice. Lock the interior first: a one-page change moves the spine and forces a full rebuild.

## Step 2 — Generate the cover artwork
Generate the cover imagery with **ChatGPT Image 2.0** (never Google Flow for covers). Produce a full-bleed background that runs continuously across back + spine + front, plus the front focal image. Photorealistic only (house rules below). Title/subtitle/author text is added in Canva, not baked into the artwork, so spelling and placement stay controlled.

## Step 3 — Set up the Canva canvas
Create a design, Custom size, set the unit to **inches**, and enter the exact full-cover dimensions from the calculator (for example 12.700 x 9.250). Inches, not pixels, make the PDF export at 300 DPI; a pixel canvas exports the wrong physical size and KDP rejects it.

## Step 4 — Load the template as a locked guide layer
Upload the PNG template, stretch it corner to corner, then Lock it (optionally about 40% transparency). It marks the four zones you cannot touch: outer bleed band, safe zones, spine strip, and the back-cover barcode reserve.

## Step 5 — Build the three panels, back to front
1. **Background** edge to edge across the whole canvas, covering the bleed — one continuous background across back, spine, and front reads far more professional than three blocks.
2. **Front cover**: title, subtitle, and author in the right-hand safe zone; keep the title in the upper third so it reads at thumbnail size on the Amazon listing.
3. **Spine**: text only at 100+ pages; rotate 90 degrees, centre inside the spine strip, keep at least 0.0625 in inside each fold; below about 130 pages use the title only or leave it blank.
4. **Back cover**: blurb, author bio, and imprint area in the left-hand safe zone, clear of the barcode reserve; if the background is dark, place a light rounded rectangle behind the barcode area so the printed barcode scans.

## KDP zone rules (what gets covers rejected)
- **Bleed** 0.125 in on all sides: background runs to the edge, but no text, faces, or logos in the outer 0.125 in (it is trimmed off).
- **Safe zone**: keep all text and key imagery at least 0.25 in inside the trim line (0.375 in from the canvas edge).
- **Barcode reserve** 2 x 1.2 in, lower-right of the back cover: keep it plain, light, and unbusy.
- **Spine**: text only at 100+ pages, at least 0.0625 in inside each fold, centred.
- **Hardcover** adds a wrap area of about 0.6 in on all sides plus a hinge strip each side of the spine: nothing important there, and the background fills the entire wrap with no white edges.

## Step 6 — Pre-export checks
Zoom to 100% and walk the perimeter: no hard-edged element inside the bleed band; no text crossing a spine fold; barcode area clear and light. **Delete or hide the template PNG** — the single most common mistake; left on, its guide lines print on the finished book. Replace any unpaid Canva Pro element or the export carries a watermark.

## Step 7 — Export to print-ready PDF
Share, Download, **PDF Print**. Leave **"Crop marks and bleed" UNCHECKED** (bleed is already in the canvas; ticking it double-bleeds and KDP rejects the oversized file). Tick **Flatten PDF** (removes transparency, which KDP does not accept). Colour profile: CMYK with Canva Pro, otherwise RGB is accepted. Download.

## Step 8 — Verify before handing off
Open the PDF and check File > Properties > Page Size: it must match the calculator dimensions within about 0.01 in. Common failures: 12.95 x 9.50 instead of 12.70 x 9.25 means crop-marks-and-bleed was left ticked; about 4.23 x 3.08 means the canvas was built in pixels; visible pink/blue lines mean the template PNG was not deleted; a faint diagonal watermark means an unpaid Pro element is still on the canvas. Upload the single wrap PDF in KDP as the COMPLETE cover, not the front-cover-only option, and always step through the KDP Previewer, the last chance to catch a title sitting too close to an edge.

## Quick reference
- Bleed all four sides 0.125 in; safe margin 0.25 in from trim (0.375 in from canvas edge).
- Barcode reserve 2 x 1.2 in, lower-right of the back cover.
- Spine text clearance 0.0625 in per fold; minimum pages for spine text 100.
- Full cover width = (2 x trim width) + spine width + 0.25 in; height = trim height + 0.25 in.
- Export at 300 DPI by setting the canvas in inches.

## Pegasus cover house rules (apply to BOTH build paths and to cover_prompt.md)
- Photorealistic imagery only. No icons, badges, vector, or clip art.
- No selling-point callouts on the cover.
- No violence or blood.
- No background base colour repeated within a five-cover window (palette uniqueness, No-Two-Books-Alike).
- Original design only; carry the finished book's exact title, subtitle, and author name(s), spelled and cased exactly. The content restrictions apply to every cover element.

## Hard rules
- Deliverable is ALWAYS the single continuous wrap PDF at the exact calculator dimensions. Never separate front/back files; never the front-cover-only upload.
- Genie never enters credentials; login, quota, or refusal walls -> report BLOCKED to the operator.
- Per-book operator confirmation before any publish click.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
