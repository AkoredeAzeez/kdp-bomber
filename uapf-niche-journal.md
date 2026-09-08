---
name: uapf-niche-journal
description: Low-Content & Guided Journals overlay (OV-LOWC) — invoked by uapf-phase0-router when the title signals a journal, planner, notebook, log book, diary, tracker, or prompted/guided journal
---

# UAPF Niche: Low-Content & Guided Journals (OV-LOWC)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** the title contains any of: journal, planner, notebook, log book, diary, tracker, habit tracker, gratitude journal, prompted journal, blood pressure log, fishing log, guest book, prayer journal, lined notebook, composition book, memory book — or any equivalent phrasing that names a fill-in book whose value lies in its repeating page structure rather than in authored prose.

## Expert Panel

1. **Low-Content Publishing Master (Domain Master)** — veteran KDP low-content publisher; owns the page system design, tier classification, and the walkthrough audit. Final authority on whether the repeating unit actually serves the logging or journaling task.
2. **Subject-Matter Practitioner** — a real practitioner of whatever the book logs or guides (angler for a fishing log, nurse or hypertension patient for a blood pressure log, grief counselor for a grief journal). Tests every field label against the real task.
3. **Interior Layout Designer** — print-interior specialist; owns spread logic, line spacing, field geometry, trim-size fit, and margin/gutter compliance.
4. **KDP Metadata & Category Strategist** — owns the title-position formula (function + audience + format), category tree placement, and keyword fields for low-content search behavior.
5. **Clinical/Sensitivity Reviewer (Tier 3 only)** — licensed-profession-informed reviewer seated whenever the subject overlay assigns R2–R4; owns prompt safety, professional-support framing, and the crisis-resource page.

## Phase 0 — Title Analysis

Execute these steps in order the moment the title arrives. Do not generate any interior content before all steps complete.

### 0.1 Immediate trademark and risk screen
Screen the exact title for trademark conflicts and KDP-risk terms before anything else. Report findings before subtitle generation. Low-content categories are heavily policed for trademark abuse (character names, brand names, sports teams); reject or flag any title term that is a live mark.

### 0.2 Language lock
The language of the supplied title is the manuscript language for every printed page (labels, prompts, front matter). Operator-facing workflow output remains in English.

### 0.3 Tier classification (mandatory, drives everything downstream)
Classify the title into exactly one tier and state the classification with a one-line justification:

- **TIER 1 — No-content:** lined journals, blank notebooks, sketchbooks, guest books, address books, password books. Value = format quality + cover + niche targeting. Interior is a simple repeating unit with essentially no per-page variation.
- **TIER 2 — Structured low-content:** planners, logbooks (fishing, blood pressure, mileage, maintenance), habit trackers, recipe blanks, workout logs, budget trackers. Value = a purpose-built form the user fills repeatedly. Interior is a designed data-capture unit.
- **TIER 3 — Guided/prompted:** gratitude journals, prompted diaries, grief journals, couples' question books, anxiety journals, prayer journals with devotional prompts. Value = authored prompts + structured response space. Interior is a prompt system with real written content.

### 0.4 Subject analysis
Identify the specific activity or subject being logged/guided, the implied audience (including age/print-size implications — "for Seniors" mandates large print), the real-world task the user performs with the book in hand, and the physical context of use (bedside, tackle box, kitchen counter, gym bag). The physical context influences trim size and layout density.

### 0.5 Risk regime assignment
- Tiers 1–2: **R0** (no factual-claim risk; standard disclaimers only). Exception: a Tier 2 medical log (blood pressure, glucose, medication tracker) carries a medical-tracking disclaimer ("this log does not replace professional monitoring; share readings with your clinician") — still R0 content, strengthened disclaimer.
- Tier 3: risk regime **R1–R4 assigned by the subject overlay.** Examples: gratitude journal = R1; anxiety journal = R3 (evidence-informed prompt framing, no therapeutic claims); grief journal = R4 (professional-support framing throughout, mandatory crisis-resource page, no prompts that instruct processing of trauma without support). The Clinical/Sensitivity Reviewer is seated for R2 and above.

### 0.6 Dated vs. undated determination
Default is **UNDATED** for every format. Dated interiors (e.g., 2027 Daily Planner) are produced only when the user explicitly declares a dated edition, because dated stock expires and kills long-tail sales. If the supplied title itself contains a year, confirm with the operator that a dated edition is intended before proceeding.

### 0.7 Subtitle engine
Generate 6–8 KDP-compliant subtitle options. Title + subtitle ≤ 200 characters combined; subtitle 50–150 characters; benefit-driven; keyword-bearing; no prohibited claims. For low-content, subtitles carry the specification payload the cover cannot: page count, size, undated/dated status, audience. Example pattern: "Undated Daily Log with 110 Guided Entry Pages, Large Print 8.5 x 11 — Track Readings, Medication, and Notes." Mark one RECOMMENDED with a one-line rationale and adopt it as the working subtitle; the operator may override at the specification gate.

### 0.8 Auto-configuration
The AI auto-selects and presents with brief rationale: trim size, page count, the page-system design (unit(s), repetition count, special pages), accent color scheme, line style and spacing, dated/undated confirmation, audience print-size tier, and (Tier 3) prompt count and prompt architecture. All selections surface at one specification gate ending with **Type Proceed**. Nothing is generated until the operator types Proceed.

## Book Architecture

**The chapter is REPLACED by the PAGE SYSTEM.** There is no chapter formula in this niche. The structural law of an OV-LOWC book is the exact definition of its repeating page unit(s), the repetition count, and the special pages. A page system is not "lined pages" — it is a full engineering spec.

### The Page System specification (mandatory before any interior generation)
Define, in writing, at the specification gate:

1. **The repeating unit(s)** — every element on the unit, exhaustively:
   - every field and its exact label text;
   - every line: count, weight, spacing (e.g., 24 rules at 0.32 inch spacing for adult handwriting; 0.5 inch or more for children or seniors);
   - every checkbox and its purpose;
   - every rating scale, icon row, or tracker grid with its range and meaning;
   - free-space zones and their captions;
   - the unit's page count (one-page unit, two-page spread unit, etc.).
2. **The repetition count** — exactly how many times the unit repeats (e.g., 110 entry spreads = 220 pages), with arithmetic shown against the total page budget.
3. **Special pages** — everything that is not the repeating unit: title page, copyright, "This book belongs to," how-to-use page, self-index/contents pages for logbooks, periodic review/summary pages (e.g., monthly reflection in a habit tracker), reference pages (blood pressure category chart, fish species reference, measurement conversions), and the crisis-resource page where R3–R4 requires it.

### Field-label reality test
Every field on a Tier 2 unit must map to something the real user actually records during the real task. A fishing log unit must carry the fields an angler fills at the water: date, location/water body, weather, air/water temperature, water conditions, time in/out, species, bait/lure, rod/setup, catch size and count, released/kept, notes. A blood pressure log needs: date, time, systolic, diastolic, pulse, position/arm, medication taken, notes — not decorative filler. The Subject-Matter Practitioner panel role signs off on every label. Fields nobody fills are deleted; fields the task needs but the draft lacks are added.

### Spread logic
Decide and hold the left/right page roles for the entire book. If the unit is a two-page spread (left = data capture, right = notes/sketch), every spread in the book keeps that orientation, and the repetition count must be even-aligned so no unit is broken across a sheet. Verso/recto alignment is checked at Gate 3: page 1 of the first unit must land on the correct side after front matter, padding with a blank or design page if needed.

### Page-count bands by tier (KDP paperback norms)
- Tier 1: 100–120 pages typical (lined journal standard: 100 or 120); guest books 100–150.
- Tier 2: 100–150 pages; logbooks commonly 100–120 units' worth; planners (undated) 120–200 depending on daily/weekly unit size.
- Tier 3: 120–200 pages depending on prompt count (a 90-prompt journal with one prompt spread each plus front/back matter is roughly 190 pages).
- KDP minimum is 24 pages; never publish near the minimum. Keep totals well inside KDP's trim-size maximums.

### Front matter (locked order, minimal)
Title page → Copyright page (author name generated from fakenamegenerator.com in First Name, Initials. Surname format; disclaimer tuned to tier and risk regime) → "This Book Belongs To" page (Tiers 1–2; optional Tier 3) → How to Use This Book (one page; mandatory for Tiers 2–3, optional Tier 1) → (Tier 3, R3–R4) support-framing page and crisis-resource page placement per Content Rules. No preface, no auto-TOC (a logbook may instead carry a self-indexing contents page the user fills in).

### Back matter
Tier 2: reference charts relevant to the log (e.g., blood pressure categories per current major guidelines, species/season reference, conversion charts), plus a handful of blank notes pages. Tier 3: closing reflection page, additional free-writing pages, and the crisis-resource page repeated at the back where R4 applies. All tiers: a single courteous review-invitation line on the closing page is the maximum; no review-begging pages.

## Interior Design

Inherits UAPF default DOCX/Word automation conventions with these niche overrides:

- **Trim size:** auto-selected by use context. Default 6 x 9 for journals, diaries, and prompted books; 8.5 x 11 for planners, large-print medical logs, and worksheet-like trackers; 5 x 8 or 5.25 x 8 acceptable for pocket logs (fishing, mileage) when the physical context demands it. State the choice and rationale at the specification gate.
- **Margins:** meet KDP minimums with gutter scaled to page count (0.375 inch gutter under 150 pages; verify against the current KDP margin table). No-bleed default; bleed only if the design carries full-bleed decorative elements.
- **Typography:** field labels and prompts in a clean readable serif or humanist sans, 10–12 pt; large-print editions (audience includes seniors) 14 pt minimum for labels and 0.5 inch line spacing. Prompt text (Tier 3) may use an accent display face for the prompt itself, but response-area text and labels stay in the workhorse face. Em dashes are banned catalogue-wide; use commas, colons, or parentheses.
- **Lines:** true typeset rules (table borders or underline rules), never rows of underscores or periods. Line spacing: 0.28–0.32 inch adult standard, 0.5 inch or more for senior/child editions.
- **Color:** interiors default to black ink (color printing cost destroys low-content margins). The accent color scheme lives on the cover and, at most, as grayscale-safe tints in the interior. One niche-appropriate scheme per title, changed on every new title, never repeating a prior catalogue look.
- **Tables/grids:** native Word table objects only, locked-sample border discipline (single half-point rules, consistent column widths, adequate cell padding, sufficient row heights). No ASCII, markdown, or pipe pseudo-tables anywhere.
- **Word automation:** headings mapped to Word Styles; page geometry set by section properties; the repeating unit built once as a master and duplicated programmatically so all units are structurally identical.

## Content Rules

**The fatal flaw in this niche: a repeating unit that looks like a journal page but fails the real task** — fields no one fills, missing fields the task needs, lines too tight to write on, prompts that are generic filler ("Write about your day") instead of authored, specific, progressive prompts. A low-content book with a broken unit is broken on every single page. The unit is the product.

Hard constraints:

1. **Unit fidelity:** every repetition of the unit is exactly identical (except intentional variation such as alternating prompts). No drift in line counts, field order, or spacing between page 12 and page 112.
2. **Field-label reality (Tier 2):** every label passes the practitioner test against the real logging task, using the vocabulary the practitioner uses.
3. **Prompt authorship (Tier 3):** every prompt is specific, non-repeating, and sequenced with intent (an arc: easier openers, deeper middles, integrative closers). No prompt appears twice. Prompt count stated at the specification gate and verified at assembly.
4. **Risk-regime obedience (Tier 3):** prompts obey the subject overlay's regime. R4 (grief, trauma-adjacent): every section carries professional-support framing ("a journal supports, and never replaces, professional care"), no prompt instructs re-living traumatic detail, and a crisis-resource page (region-generic: emergency services, national helpline guidance, "contact a licensed professional") appears in front matter and is repeated in back matter. R3 (anxiety, mental health): evidence-informed framing, no therapeutic-outcome claims, no diagnostic language. R2: standard sensitivity review. No Tier 3 book ever claims to treat, cure, or diagnose.
5. **Undated default:** no printed years, dates, or day names unless the operator declared a dated edition. Undated units use "Date: ____" style fields.
6. **Response-space sizing:** space matches the expected answer — a pulse field is short; "What are you grateful for today?" gets 6–10 rules, not 2.
7. **Content-standards catalogue compliance:** no alcohol, pork or pig derivatives, or gambling references in any prompt, example, reference chart, or cover/image prompt; compliant substitutions always. A non-compliant concept (e.g., a wine-tasting journal) is declined or reframed at Phase 0.
8. **No filler pages:** every non-unit page earns its place (reference value, orientation, or reflection). Padding with quote pages to hit a page count is prohibited; adjust the repetition count instead.
9. **Medical logs:** reference charts must match current major-guideline values and carry the medical-tracking disclaimer; the log never interprets readings for the user.

## QA Checklist

### Gate 1 — Specification gate (after Phase 0, before any interior)
- [ ] Trademark/risk screen reported; title clear or flagged
- [ ] Tier classified and justified; risk regime assigned (R0 / R1–R4)
- [ ] Dated/undated confirmed (undated unless the operator declared otherwise)
- [ ] Page system fully specified: every field, label, line count, and checkbox of every unit; repetition count with arithmetic; all special pages listed
- [ ] Trim size, margins/gutter, page total, and typography tier (standard vs large print) stated
- [ ] Working subtitle adopted from 6–8 options; title + subtitle ≤ 200 characters
- [ ] Accent scheme selected and verified unique against the catalogue
- [ ] Message ends with Type Proceed; nothing generated past the gate

### Gate 2 — Unit approval gate (master unit and special pages rendered)
- [ ] Master repeating unit rendered exactly to spec; all labels verbatim from the approved spec
- [ ] Field-label reality audit: Subject-Matter Practitioner review of every field against the real task; fields added/deleted as needed and the spec updated
- [ ] Line spacing physically writable for the audience (measured, not eyeballed)
- [ ] Response spaces sized to expected answers
- [ ] Tier 3: full prompt list reviewed — no duplicates, arc verified, every prompt regime-compliant; R3–R4 framing and crisis-resource page present
- [ ] Tables and rules are native Word objects; no underscores-as-lines
- [ ] Content-standards and em-dash ban verified across all labels and prompts

### Gate 3 — Assembly gate (full interior built)
- [ ] **Page-system walkthrough audit: simulate 7 days/entries of real use.** Fill seven consecutive units as the real user would (7 fishing trips, 7 days of readings, 7 prompted entries). Every field must be usable, every space sufficient, nothing missing, nothing dead. Log the walkthrough results; any friction is a blocking correction before Proceed.
- [ ] **Spread-logic check:** left/right page roles consistent through the entire book; first unit lands on the correct verso/recto after front matter; two-page units never split across a sheet; repetition-count parity verified
- [ ] Unit fidelity: spot-check units at start, middle, and end — structurally identical
- [ ] Repetition-count arithmetic matches the delivered page total; total within KDP limits for the trim
- [ ] Front matter order correct; copyright/disclaimer tuned to tier and regime; author name in house format
- [ ] Dated content absent (or correct, if a dated edition was declared)
- [ ] Reference pages accurate to current guidelines (medical logs)

### Gate 4 — Release gate
- [ ] Final PDF preflight at exact trim; margins and gutter pass KDP preflight; no live elements outside the safe area
- [ ] Undated status, page count, and trim in subtitle/description match the actual interior
- [ ] Cover spine width computed for the final page count and paper color
- [ ] Trademark findings re-confirmed against the final title, subtitle, and cover text
- [ ] R3–R4: crisis-resource page present in required positions; no therapeutic claims anywhere in the book or metadata
- [ ] Catalogue uniqueness confirmed (scheme, cover treatment, unit design differ from all prior titles)
- [ ] Content-standards and em-dash sweeps re-run on the final build

## KDP Positioning

- **Category tree:** place by function, not by "journals" generically. Blood pressure log → Health, Fitness & Dieting > Diseases & Physical Ailments > Heart Disease; fishing log → Sports & Outdoors > Hunting & Fishing; planners → Self-Help > Time Management; gratitude/anxiety journals → Self-Help > Motivational or relevant mental-health subtree; grief journals → Self-Help > Death & Grief; prayer journals → Christian Books & Bibles or Religion & Spirituality per faith context; guest books → Reference or Crafts, Hobbies & Home / Weddings as applicable. Build the standard ten-category placement plan across marketplaces, pairing high-relevance categories with winnable-rank categories.
- **Title position formula (locked):** function + audience + format in the title position. Pattern: "Blood Pressure Log Book — Large Print Daily Tracker for Seniors." The function keyword (log book, journal, planner, tracker) must sit in the title itself, because low-content buyers search by function.
- **Description leads with:** what the book does for the user and the exact specification — unit design, number of entries/pages, trim size, undated status, large print if applicable — in the first two lines; then the feature list (what is on each page, special pages, format); then who it is for and gift positioning. 2,000–4,000 characters, HTML bold on key phrases, no prohibited claims, literally accurate to the interior. Tier 3 R3–R4 descriptions use supportive, non-clinical framing and never promise therapeutic outcomes.
- **Backend keywords:** seven fields of up to 50 characters, each a distinct search-intent cluster; include function synonyms not used in the title (diary/notebook/logbook variants), "gifts for" phrasings, and audience terms; no words already in the title or subtitle, no competitor names, no quality claims.
- **Pricing posture:** low-content competes at the category's impulse price band; scan the top competing titles (length, price, trim, review posture) and recommend list and promotional pricing with rationale, delivered in the standard marketing DOCX.

## Key Rules — Do NOT Break

1. **The page system replaces the chapter.** Never generate "chapters" for an OV-LOWC title. The full unit spec (every field, label, line count, checkbox), repetition count, and special pages must be approved at the specification gate before any interior is built.
2. **The unit is the product.** Any defect in the repeating unit is a defect on every page. Unit fidelity is absolute: identical structure at every repetition.
3. **Field labels must survive the practitioner test.** Every Tier 2 field maps to something the real user records during the real task, in the practitioner's vocabulary. No decorative fields; no missing task-critical fields.
4. **Undated by default.** Dated interiors only on explicit operator declaration; dated stock expires. A year in the supplied title triggers a confirmation, never an assumption.
5. **Tier 3 prompts obey the subject overlay's risk regime.** Grief = R4: professional-support framing plus a crisis-resource page in front and back matter; anxiety = R3: no therapeutic claims or diagnostic language. No Tier 3 book claims to treat, cure, or diagnose — in the interior or in the metadata.
6. **The 7-entry walkthrough audit is mandatory at Gate 3.** Simulate seven real days/entries of use; any friction found is a blocking correction.
7. **Spread logic is locked book-wide.** Left/right roles never flip; multi-page units never split across a sheet; verso/recto alignment is verified after front matter.
8. **Risk regimes:** R0 for Tiers 1–2 (with a strengthened disclaimer for medical logs); R1–R4 by subject for Tier 3, with the Clinical/Sensitivity Reviewer seated at R2 and above.
9. **The KDP title position carries function + audience + format.** The function keyword (log book, journal, planner, tracker) sits in the title; the subtitle carries the specification payload (page count, size, undated status, audience).
10. **True typeset rules only.** Never underscores or dot-runs as writing lines; all grids are native Word tables to the locked border spec.
11. **Catalogue hard rules bind fully:** absolute content restrictions (prompts, examples, reference charts, cover art briefs), the em dash ban, fakenamegenerator.com author names in First Name, Initials. Surname format, and catalogue-wide visual uniqueness on every new title.
12. **Every gate ends with Type Proceed** and generation never continues past a gate without the operator typing Proceed.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
