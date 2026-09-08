# Genie / Pegasus Press UAPF — Changelog​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Version history of the Genie framework. This copy is the free Community
Edition of the MAX pack.

## 6.4.4 Community Edition — 2026-09-03

Free, license-less build of the MAX pack, made by the studio owner for
community use:
- Removed the license key, activation, device binding, kill switch,
  file-integrity guard, and self-updater. No session-start license or
  integrity check exists; nothing to activate.
- Every MAX skill ships and is available to every user; pack gating and
  upgrade offers are gone. Publishing hard stops (money, credentials, final
  Publish click) still bind.
- Rule 14 rewritten as the Community Edition rule: sharing is allowed.
- Installation guide rewritten: extract and start, no installer, no key.
- Updates apply with `python genie_update.py <new-package.zip>`.

## 5.5 — 2026-08-14

Niche specialist intelligence upgrade (2026-08-15, Methods 16-26):
- market_math.py engine: BSR-to-sales/revenue estimation (labeled estimates,
  log-log curve, per-marketplace scaling), KDP print-cost and margin
  calculator, composite A-F Niche Score, keyword difficulty 0-100.
- Extensive data law: 20+ competitors per validation, field-complete top 10,
  and a machine-readable JSON twin saved with every report.
- Review-gap mining: competitor 1-3 star complaints become complaint_map.json
  and drive the new book's TOC (differentiation engine).
- Seasonal keyword tracker: monthly state-backed snapshots per keyword,
  seasonal classification with peak months, PRODUCE-NOW standup flags timed
  to the 10-week production lead.
- Category badge thresholds, seasonality radar with launch calendars,
  profit-first margin gates (color-trap detection), localization arbitrage
  queue, own-catalog learning loop (actuals-only calibration), rising-niche
  and saturation-urgency alerts.

Publishing manifest and client-side publish gates (2026-08-15):
- Every completed book now writes publish_manifest.json alongside the KDP
  metadata DOCX: exact title, subtitle, pen name, description, the 7
  keywords, categories, trim, page count, prices, and file paths to the
  manuscript, cover wrap, and A+ assets. uapf-publisher reads it FIRST on
  every platform, so uploads to KDP, IngramSpark, D2D, Kobo and the rest
  never re-derive metadata; missing manifests on older projects are
  generated before any upload.
- The publishing hard gates (final Publish click per book per platform,
  money actions with exact amounts, credentials never handled) are stated
  to bind EVERY install including licensed MAX clients, with the licensed
  user holding the confirmations.

Genie packs and MAX package delivery (operator-side, 2026-08-14):
- Three packs: STARTER (book writing, premium formatting, interior images,
  all 29 niches, quality and safety gates), PRO (Starter + market research
  and intelligence, KDP metadata, covers, A+ Content), MAX (everything,
  including the publishing and business operations layer).
- The delivered MAX package contains the complete MAX tier master and all
  MAX instruction files. The license record remains authoritative for access:
  package wording or instruction labels do not activate a higher tier.
- License keys encode the pack: keys ending GENIESTART (Starter) and
  GENIEPRO (Pro); classic keys are MAX. Enterprise keys carry a seat count
  so one key activates on multiple devices, at any pack level.
- Upgrades are one operator action (upgradeKeyTo): the new-tier key is
  pre-bound to the client's device for frictionless re-activation, the old
  key stays active until revoked, and one factory run delivers the new pack
  by email automatically.
- The build factory selects the tier master by key suffix; tier masters are
  produced by the operator-side tier builder from a single skill map. Each
  tiered install politely offers an upgrade when asked for a capability of
  a higher pack. Operator-only skills ship in no tier.

Production cadence and interior laws (binding operator rules 2026-08-14,
BOTH engines, Claude and Codex):
- Chapter-by-chapter build law: a book is NEVER built all at once. Exactly
  one chapter at a time: build the chapter, deliver its DOCX + PDF download,
  then automatically move to the next. Multi-chapter passes and batch
  deliveries are production failures in every mode, autopilot included.
  Encoded in both root instruction files, uapf-autonomous-full-pipeline, the
  CodexBookStudio house rules, and the Codex generate-book workflow.
- Chapter preview delivery: each finished chapter is delivered as BOTH a DOCX
  and a PDF download for operator inspection, rendered exactly as it will
  ship with the full premium color design. AUTO-ADVANCE delivers both files
  then continues without waiting; the delivery is never skipped. Encoded in
  uapf-chapter-production, uapf-autonomous-full-pipeline, uapf-auto-advance,
  and both root instruction files, with the premium-color bar restated in
  the manuscript quality requirements.
- 8.5 x 11 interior heading and introduction law: chapter titles in BLOCK
  LETTERS, bold, 28 pt or larger; subchapter headings 14 to 18 pt; neither
  ever cut off by the page margins, verified on the rendered page in render
  QA. Introduction for 8.5 x 11 books is about a page and a half and must
  fill its pages completely with substantive explanations (6 x 9 prose books
  keep the 2 to 3 page target). Overrides smaller per-niche heading defaults
  on 8.5 x 11 trims.
- Pagination and final TOC law: page numbering starts at the Introduction
  (page 1); front matter before it carries no folio numbers. After the whole
  book is finished the Table of Contents is REWORKED against the final
  rendered layout and verified entry by entry in the final PDF; completion
  checklists now require it.

Clean in-place updater (new):
- genie_update.py applies a new package over an existing install with no
  scratch reinstall: replaces code/instruction files, removes retired files
  (manifest-driven via package_manifest.txt), re-checks dependencies through
  the bootstrap, and refreshes the integrity-guard baseline so an official
  update never reads as tampering.
- Never touches client data: .genie_license, Books/, projects/, cover_db/
  (incl. _aplus), state/, guard baseline. Pre-manifest installs get an
  additive-only first update. --dry-run previews; downgrades refused unless
  forced. Accepts older install roots (AGENTS.md + .agents/) so the first
  in-place update works on installs that predate genie_bootstrap.py.
- Build flow: run `python genie_update.py --make-manifest` inside the built
  client package folder right before zipping.
- The client update-notification email template (License Dashboard, deployed
  Version 9, same URL) now carries the step-by-step in-place update
  procedure for Windows and Mac.

House interior reference banks (operator-supplied catalog masters, banked
locally at cover_db/_interiors/, never shipped; the codified standards ship
in the niche skills and bind BOTH engines on every install):
- Cookbook (8 masters): two proven recipe-card archetypes (two-per-page
  compact, one-per-page hero), title-only full-bleed photo dividers,
  operator-confirmed interior standards from the live kidney-cookbook run
  (30pt ALL-CAPS unlabeled chapter titles, 15pt subheads, recipe-card law).
- Textbook/educational (5 clinical masters): scholarly justified body,
  decimal sections, evidence-spotlight panels, shaded-header tables,
  labeled multi-panel figures; binding also on study-guide, exam-simulator,
  reference, user-guide, language.
- Travel (6 masters): two-column body, ALL-CAPS accent banners, tinted
  feature panels, directory entries, full-bleed photo dividers; trim
  confirmed 8.5x11; MINIMUM 4 MAPS per guide, maps via Codex gpt-image-2,
  photos via Google Flow.
- Workbook (5 masters): numbered worksheets with shaded header bars and
  purpose lines, prompt/response tables with real writing space, fill-in
  registers, worked-explanation answer keys.
- Craft/how-to (3 masters): run-in step headings with cued numbered steps,
  Check-for troubleshooting, technique-first teaching, Note/KEY CONCEPT
  panels.
- Self-help typography law: justified body, left-aligned lists, 1.5 line
  spacing, premium world-standard typesetting.
- Every bank restates No-Two-Books-Alike: anatomy and quality bar are
  copied, palettes and fingerprints never repeat.

Client custom formatting (new skill):
- uapf-custom-formatting: the user saves their own formatting style per niche
  ("Genie, customize formatting for [niche]"; show / reset commands). Profiles
  at state/custom_formatting/<niche>.json, applied automatically to every
  future book in that niche by BOTH engines, surviving every update (state/
  is never touched by the updater and never ships). Aesthetics only: profiles
  outrank the formatting standard's general defaults but never a binding law
  (premium bar, containment, type floors, pagination/TOC, hard rules).

Documentation and reference banks:
- UAPF Skill Command Reference updated to v5.4+: cover/A+ designer with the
  Codex engine, cover_db reference banks, the INSTALL/UPDATE/LICENSE
  section, THE CODEX ENGINE section (studio workflows, failover, two-phase
  cover security, Codex license check), and per-engine image timing (Codex
  generates images inline chapter by chapter; Claude writes the whole
  manuscript first, then runs the Flow image pipeline).
- A+ reference bank completed across ALL 29 niches (501 modules banked;
  trade-published shelves honestly thinner than indie shelves).

## 5.4 — 2026-08-14

Cover and A+ production system (new):
- uapf-cover-aplus-designer is the MASTER cover/A+ skill (art direction,
  design law, QA gate), grounded in a live study of 1,273 best-seller covers
  across all 29 niches with a per-niche pattern library.
- uapf-cover-db: 29-niche cover reference bank (cover_db.py) with new-install
  seeding, all-29 completion gate, and 6-month automatic refresh, on operator
  and client installs alike.
- A+ reference bank: aplus_db.py at cover_db/_aplus, dense-infographic law
  from a live A+ study (icon cards, 3D book render, open-book mockup, badges,
  pill banners, numbered plans, integrated photography); one module = one
  image = one 970x600 file.
- Cover laws: block-letter titles (non-negotiable), comprehensive photoreal
  prompts, no text ever cut off (crop-safe verified after finishing),
  premium/top-publisher finish, No-Two-Books-Alike.
- CODEX is the default engine for all cover and A+ production (native
  gpt-image-2, CLI and VS Code); Claude drives it headlessly via codex exec.
  ChatGPT web "Pegasus Covers" project is the operator-led alternative.

Formatting (new/consolidated):
- uapf-formatting-standard: consolidated master formatting standard
  (universal rules, per-niche interior specs incl. drafted sections 15-16,
  cover/wrap/A+ rules, final preflight), binding both engines.
- Premium/professional/high-grade bar in every niche, verified on the
  rendered page (render_qa).
- Trim size defaults by niche (8.5x11 education/practical incl. travel;
  6x9 narrative/lifestyle; health by mode); Codex stamps trim at intake.
- Senior type floor (13-14 pt) and 8.5x11 4-line block-title sizing.

Engine and security:
- Two-phase Codex security split: generation in workspace-write (third-party
  refs fenced), finishing + render_qa in full access on Genie artifacts only.
- uapf-license-guard: SHA-256 file-integrity tamper-evidence over the rule
  and protection files (complements, does not duplicate, the existing
  device-bound kill switch codex_license_check.py + Genie License Dashboard).
- Licensing consolidated onto the existing dashboard; confidentiality and
  license-protection rules bind both engines in every sandbox; delivery
  hygiene gate strips internal material from client packages.
- codex_license_check.py: one customer key licenses BOTH agents (shared
  .genie_license, product "genie", one device binding, one revoke).
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
