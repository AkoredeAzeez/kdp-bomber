---
name: uapf-cover-db
description: Per-niche database of proven best-seller competitor covers. At cover time Genie picks 2-3 random references from the niche's bank instead of running a live Amazon session, reads their shared pattern, and feeds the existing cover_prompt.md -> ChatGPT pipeline. Every live uapf-cover-reference run banks its refs here, so the database grows itself.
---

# UAPF Cover Reference Database​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

A local, per-niche bank of covers that are proven sellers, so cover design can
start instantly. It replaces the LIVE research step of uapf-cover-reference when
the niche already has enough banked covers; everything downstream (pattern
reading, cover_prompt.md, the ChatGPT build pipeline, the Pegasus cover house
rules) is unchanged.

**Location:** `cover_db/<niche>/` in the Genie project root, managed only
through `cover_db.py` in this skill folder. The 29 niche keys match the
`uapf-niche-<x>` skills (cookbook, travel, study-guide, ...).

**Reference-only, local-only.** Banked images are design references for
ORIGINAL covers. Never copy, trace, or closely imitate them; never ship,
export, or redistribute the images or the database (they are third-party
cover art). No-Two-Books-Alike and all Pegasus cover house rules apply in full.

## Using it at cover time (the normal path)

1. Resolve the book's niche from `book_lock.md` (the canonical classification
   line).
2. Ask the database for references:

       python .agents/skills/uapf-cover-db/cover_db.py pick --niche <niche> --count 3

   It returns 2-3 RANDOM covers (least-recently-used biased, so consecutive
   books in one niche do not see identical references) with their metadata,
   and stamps them used.
3. If it returns `NOT_ENOUGH_COVERS` (fewer than 2 banked): fall back to the
   full LIVE research workflow in uapf-cover-reference, and bank what it
   downloads (below) so the niche is seeded for next time.
4. Copy the picked images into the book folder as `cover_refs/ref1.jpg` ...,
   then continue exactly as uapf-cover-reference steps 7-10: read the shared
   winning pattern INCLUDING the text treatment (title case style, serif/sans
   character, weight, colour emphasis, arrangement), write `cover_prompt.md`
   (exact title/subtitle/author embedded, text treatment stated) and
   `cover_reference_brief.md` (cite each ref's banked BSR/rating
   and its captured date), and hand off to uapf-chatgpt-cover-pipeline (or the
   Canva path).

## Populating and refreshing

- **Bank every live run.** Whenever uapf-cover-reference does live Amazon
  research, add each downloaded ref with its real metadata:

      python .agents/skills/uapf-cover-db/cover_db.py add --niche cookbook --image cover_refs/ref1.jpg --title "..." --asin B0... --bsr 1234 --rating 4.7 --reviews 1809

- **Bulk import** a folder of covers (metadata unknown):

      python .agents/skills/uapf-cover-db/cover_db.py import --niche cookbook --folder PATH --source "note"

- **Dedicated stocking runs.** The operator can say "stock the cover database
  for <niche>" and Genie runs the uapf-cover-reference research method (set
  Deliver-to first, BSR-ranked, rating 4.3+ floor) to bank 5-8 covers for that
  niche without producing a book cover.
- **Freshness / AUTOMATIC REFRESH (operator directive 2026-08-13, applies to
  every install, operator and client alike).** `list` shows capture dates per
  niche. At every session start, after the seeding completion check, flag any
  niche whose NEWEST capture is older than about 6 months and refresh it
  automatically between production tasks using the same method as seeding
  (seed_terms.json term, extract_results.js, stock_niche.py). Refreshes ADD
  current best-sellers alongside the old bank; report refreshes in the
  standup. If a stale niche hits cover time before its refresh has run,
  prefer a live uapf-cover-reference run (which re-banks) over a stale pick,
  and say so in the brief. Only banked covers that still exist on disk are
  ever picked.

## NEW-INSTALL SEEDING (mandatory, operator directive 2026-08-13)

The database never ships with an installation (its images are third-party
art). Therefore, AS SOON AS GENIE IS INSTALLED ON A NEW DEVICE, seed the
database using the proven 2026-08 stocking method below. This is part of
first-run setup: run `cover_db.py list` at startup; if `cover_db/` is
missing, empty, or has niches under 15 covers, seeding is due. Seed the
active book's niche FIRST (never block a book on full seeding), then work
through the remaining niches as background work between production tasks.

Per niche, the exact proven steps:

1. Open `https://www.amazon.com/s?k=<term>` in the browser, using that
   niche's term from `seed_terms.json` (terms marked `used_2026_08` are the
   exact searches that built the original 1,273-cover bank).
2. Run `extract_results.js` (this folder) via the browser javascript tool on
   the results page. It returns pipe-format lines (`asin|rating|img_code|title`),
   deduped, rating floor 4.3 enforced.
3. If a page yields under ~30 keepers, run the niche's next term (or
   `&page=2`) and concatenate the lines.
4. Filter out non-book items (bookmarks, candles, gift sets) and anything
   violating the content restrictions before banking.
5. Save the lines to a temp `.txt` file and run:

       python .agents/skills/uapf-cover-db/stock_niche.py <niche> <file.txt>

   It downloads each cover at full size from Amazon's public image CDN and
   banks it with its real metadata (failed downloads are skipped and
   reported, never faked).
6. Target 30-50 covers per niche; 15+ is acceptable for thin shelves.
   Confirm totals with `cover_db.py list` and record the seeding in the
   device's setup log.

**Completion gate (all 31 niches, mandatory).** Seeding is COMPLETE only
when `cover_db.py list` shows every one of the 31 niches with at least 15
banked covers. Until then, seeding remains an open task on the device: check
`cover_db.py list` at EVERY session start (not just the first run) and
continue seeding unstocked niches between production tasks. A client's Genie
is not fully set up while any niche is empty. Report seeding progress in the
standup ("cover bank: 21/31 niches seeded") until the gate passes.

## A+ MODULE BANK (aplus_db.py, operator directive 2026-08-13)

Companion database at `cover_db/_aplus/<niche>/`, managed by `aplus_db.py`
(bank / pick / list). It stores REAL A+ Content modules ("From the
Publisher" images) captured from best-selling listings, so A+ design starts
from the shelf's actual conventions (see the dense-infographic law in
uapf-cover-aplus-designer). Reference-only, local-only, never ships, exactly
like the cover bank.

Harvest procedure (proven 2026-08-13):

1. ASINs come from the niche's cover-bank `manifest.json` (they are the
   proven sellers already). For niches whose manifests lack ASINs, grab ~20
   ASINs from one seed-term search page first (`data-asin` on organic
   results).
2. In the browser on an amazon.com page, fetch `/dp/<ASIN>` for AT MOST 8
   ASINs per batch and regex the HTML for
   `m.media-amazon.com/images/S/aplus-media...` URLs. Keep only modules with
   `_SX600_` or larger; cap 6 per listing; dedupe by URL.
3. PACING IS MANDATORY: Amazon serves stub pages after rapid bursts. Leave
   60+ seconds between batches; if a batch returns mostly stubs (HTML under
   ~100 KB), STOP harvesting that session and resume in a later window. Do
   not hammer; the throttle lifts on its own.
4. Save captures as `ASIN|url-path` lines and bank:
   `python .agents/skills/uapf-cover-db/aplus_db.py bank --niche <x> --json <file.txt>`
5. Not every listing has A+ (roughly half do on indie shelves; fewer on
   traditional-publisher shelves). Report what the shelf actually yields;
   never pad.

**Completion gate (mirrors the cover-bank gate).** Target 50 modules per
niche; a niche is complete at 50+, or at its documented shelf maximum after
3 paced harvest passes on different days (some shelves simply do not carry
50 A+ listings; record that honestly in the manifest folder). Check
`aplus_db.py list` at session start alongside the cover-bank check; harvest
unfilled niches between production tasks; report progress in standups. On a
NEW INSTALLATION the A+ bank seeds the same way, right after the cover bank.

At A+ design time: `aplus_db.py pick --niche <x> --count 4` and study the
picked modules next to the component kit before writing the brief.

## Status

    python .agents/skills/uapf-cover-db/cover_db.py list

## Hard rules
- Quality bar for banking: proven sellers only (best available BSR, rating 4.3+
  with a real review count when known). This bank is "covers that sell", not
  "covers that exist".
- Random pick is 2-3 covers; never fewer than 2 references for a new cover.
- The database and its images never leave this machine, never enter a delivery
  package, and never appear in reader-facing content.
- Real data only: never invent BSR/rating metadata for a banked cover; unknown
  fields stay empty.

## INTERIOR REFERENCE BANK (moved to uapf-interior-db)

The interior bank now lives in its own skill, **uapf-interior-db**:
`cover_db/_interiors/<niche>/`, interior_db.py,
extract_interiors.js, interior_seed_terms.json, the NEW-INSTALL
AUTO-SEEDING law (primary niches gate 50, secondary 20), and the refresh
law. This cover skill keeps covers and A+; consult uapf-interior-db for
everything interior-reference related.

## DEMOTED (operator directive 2026-08-29)

This bank is a FALLBACK and pattern-notes library, not a prerequisite. The
install-time mass seeding, the 31-niche completion gate, and scheduled
whole-bank refreshes in this file are RETIRED. Cover references now come live
from an Amazon title-lane search per Cover Law v2 (see
uapf-cover-aplus-designer), which banks its three picks here on every job, so
the bank grows organically. Use `cover_db.py pick` only when live search is
unavailable, and record that in the decision log. The `_aplus` and
`_interiors` banks are unaffected and keep their own rules.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
