---
name: uapf-interior-db
description: The interior reference bank. Banks interior page images of best-selling Amazon books per niche (plus operator-uploaded house master PDFs) into cover_db/_interiors/, auto-seeds itself starting at installation, and serves references to niche skills at design time. Invoke on "Genie, interior references for [niche]", "seed the interior bank", or automatically at session start and design-fingerprint time.
---

# UAPF Interior DB (interior reference bank)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Covers sell the click; INTERIORS sell the reviews. This bank gives every
book build real best-seller interior references per niche, exactly as
uapf-cover-db does for covers.

## The bank

`cover_db/_interiors/<niche>/` holds, per niche:
- HOUSE MASTER PDFs uploaded by the operator (binding exemplars:
  cookbook, textbook, travel, workbook, crafts, howto).
- AMAZON CAPTURES: hi-res interior page images that best sellers
  showcase in their product galleries, with `index.json` recording
  asin/title/rating per book.

Commands (`python .agents/skills/uapf-interior-db/interior_db.py ...`):

| Command | Action |
|---|---|
| `list` | Per-niche counts and PASS/OPEN completion gates |
| `stock <niche> <capture.json>` | Bank a harvest (skips cover image, drops placeholders) |
| `pick --niche <x> --count 5` | Serve references for a build (house PDFs always included) |

## NEW-INSTALL AUTO-SEEDING (binding, operator directive 2026-08-16)

The bank NEVER ships with an install; every PRO/MAX install builds its
own, starting immediately at installation:

1. FIRST RUN: `genie_bootstrap.py` includes the interior bank in its
   status and the first session begins seeding right after the cover
   bank check. `interior_db.py list` runs at EVERY session start.
2. WHAT TO SEED: `interior_seed_terms.json` defines the searches.
   PRIMARY niches (childrens, activity, coloring, puzzle, journal,
   cookbook, workbook, travel, childrens-facts) carry a 50-capture
   completion gate. SECONDARY niches (prose-led listings with thinner
   galleries) are seeded best-effort to 20+. A niche holding house
   master PDFs passes its gate by definition.
3. ORDER: the active book's niche first, then remaining OPEN primary
   niches, then secondary; always BETWEEN production tasks: seeding
   never blocks a book build, and a build never cancels seeding (it
   queues). Report progress in standups ("interior bank: 6/9 primary
   gates passed") until all primary gates pass; the install's setup
   stays OPEN until then.
4. HOW (the proven 2026-08 method): Amazon search per seed term in the
   browser; collect result ASINs with a 4.3+ rating floor; in-page
   fetch of each /dp page with stub-retry (2s backoff, content-length
   check); pull the hi-res gallery URLs (`"hiRes"` regex or
   extract_interiors.js); KEEP only books with 4+ gallery images
   (cover + 3 interiors); export the compact capture and bank it with
   `stock`. Marketplace: the install's primary marketplace.
5. REFRESH: any niche whose newest capture is older than about 6 months
   re-seeds between tasks; trend niches (coloring, puzzle) refresh
   quarterly. Runs on operator and client installs alike.

## Engines

Binds BOTH engines. Claude sessions do the SEEDING (they hold the
browser). Codex sessions CONSUME the bank (`pick`) but do not harvest;
if Codex finds a needed niche OPEN, it proceeds with house masters or
without references and queues a seeding note for the next Claude
session, honestly recorded in the standup.

## Use at design time

At design-fingerprint time the niche skill pulls
`pick --niche <x> --count 5` and studies page architecture, density,
unit layout, panel styling, and visual rhythm. ORIGINALITY LAW: never
copy a page, layout verbatim, illustration, or text from a reference;
No-Two-Books-Alike and the thumbnail-confusion test apply to interiors
exactly as to covers. The bank is internal reference data: it NEVER
ships to clients inside a package and never appears in any book.

## Tier

Included in every Community Edition install, alongside the research and
cover layers it parallels.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
