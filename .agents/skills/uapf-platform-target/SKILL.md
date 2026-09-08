---
name: uapf-platform-target
description: Produce books for platforms beyond Amazon KDP. Invoke on "Genie, target [platform] for [Title]", "Genie, write this book for [platform]", "Genie, cover size for [platform]", or "Genie, convert [Title] to PDF and EPUB" (or "to epub"). Calculates the exact cover dimensions the platform accepts (using the platform's official calculator or template tool, live) and converts finished books to print PDF and reflowable EPUB inside Claude Code.
---

# UAPF Platform Target (multi-platform production and conversion)

## Commands

| Command | Action |
|---|---|
| "Genie, target [platform] for [Title]" | Lock the platform into the book's records; pull and record its exact specs |
| "Genie, write this book for [platform]" | Same, at intake: the whole pipeline produces to that platform's specs |
| "Genie, cover size for [platform]" | Report the platform's accepted cover dimensions for this book |
| "Genie, convert [Title] to PDF and EPUB" | Convert the finished book to both formats |
| "Genie, convert [Title] to epub" | EPUB only |

Platforms: Amazon KDP (default), IngramSpark, Draft2Digital, Kobo Writing
Life, Google Play Books, Barnes & Noble Press, Apple Books, Lulu.

## Platform spec matrix (baseline; ALWAYS verify live before production)

| Platform | Print cover geometry source | Ebook cover | Interior formats |
|---|---|---|---|
| Amazon KDP | KDP Cover Calculator (kdp.amazon.com/cover-calculator) | 1600x2560 JPG | Print PDF; KPF/EPUB |
| IngramSpark | IngramSpark Cover Template Generator (myaccount.ingramspark.com tools) | 1600x2400+ | Print PDF (PDF/X preferred); EPUB |
| Draft2Digital | n/a (print via D2D Print beta: their template) | 1600x2400 JPG/PNG | EPUB (they convert from DOCX too) |
| Kobo Writing Life | n/a | 1600x2400 min | EPUB |
| Google Play Books | n/a | 1400x2100 min (2:3) | EPUB and/or PDF |
| Barnes & Noble Press | B&N Press cover template tool | 1400x2100 min | Print PDF; EPUB |
| Apple Books | n/a | 1400px min shortest side; 2400x3600 recommended | EPUB |
| Lulu | Lulu book creation tool / template calculator | 1600x2400 | Print PDF; EPUB |

LIVE VERIFICATION LAW: platform specs change. Before producing a cover or
interior for a non-KDP platform, open that platform's OFFICIAL calculator,
template generator, or current spec page in the browser, enter the book's
exact trim, final page count, and paper type, and record the returned
dimensions (total wrap width/height, spine width, bleed, barcode rules) in
the project's cover records. The official tool's numbers govern; the matrix
above is only the starting point. This mirrors the KDP Cover Calculator law
in uapf-cover-aplus-designer and extends it to every platform.

## Targeting a platform

1. Record `platform_target` (one or several) in `book_lock.md` and
   `publish_manifest.json`.
2. Trim: confirm the platform offers the book's trim; if not, surface the
   nearest supported trim to the user and re-lock on their choice.
3. Covers: produced under all standing cover laws (premium HD, originality,
   block letters, containment) at the dimensions the platform's official
   tool returned: front, back, spine, and full wrap PDF for print
   platforms; the correctly sized ebook cover JPG for ebook platforms.
4. Interior: print PDF per the platform's requirements (fonts embedded,
   bleed as specified); reflowable EPUB per the conversion law below.
5. uapf-publisher reads `platform_target` and the manifest when uploading.

## Conversion law (PDF + EPUB inside Claude Code)

On "convert [Title] to PDF and EPUB" (any finished book, any age):

1. PDF: render the final rolling DOCX to print PDF through the standard
   render path (the same renderer used by render QA), fonts embedded, at
   the book's locked trim. This is the print-ready interior.
2. EPUB: build with `epub_build.py` (this folder):
   `python epub_build.py <project_folder>` reads the final DOCX, the
   `publish_manifest.json` metadata, and the cover image, and produces a
   reflowable EPUB 3: cover, title page, navigable TOC, one XHTML file per
   chapter, images embedded, metadata (title, author pen name, language,
   description) from the manifest. No publisher name, no ISBN placeholder
   (global rules apply to EPUB metadata identically).
3. HONEST REFLOW NOTE: EPUB is reflowable; the premium PRINT design
   (two-column recipe cards, fixed panels) is intentionally simplified to
   clean single-flow formatting with styled headings, images, and callout
   paragraphs. Tell the user this once per conversion; it is industry
   standard, not a defect.
4. Deliver both files in chat and record their paths in
   `publish_manifest.json` (`files.interior_epub`, per-platform covers
   under `files.platform_covers`).
5. Validate: open the EPUB (it is a zip) and verify structure: mimetype,
   nav document, one spine item per chapter, cover present. If epubcheck
   is available locally, run it; report results honestly either way.

## Tier and engines

Included in every Community Edition install: multi-platform targeting,
platform cover sizing, and PDF/EPUB conversion, alongside the publishing
operations layer they feed. Binds both engines; Codex sessions follow the
same specs and laws.
