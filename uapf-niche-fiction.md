---
name: uapf-niche-fiction
description: Fiction production framework — the Universal Fiction Framework UFFV 1.1 (replaces the earlier OV-FIC). Governs every work of narrative fiction for readers 13+ (novels, novellas, story collections, series) and routes to one of twelve sub-genre overlay skills (uapf-niche-fiction-<romance|thriller|mystery|fantasy|scifi|horror|literary|historical|ya|action|womens|faith>). Invoked by uapf-phase0-router when the title is fiction. Carries the 30 Critical Rules, the 12-phase pipeline and gates, the Character/World/Continuity systems, the Prose Engine, content ratings, QA passes, typography, and series architecture.
---

# UAPF Niche: Fiction — UFFV 1.1 (parent framework and router)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

This niche is governed by the **Universal Fiction Framework, Version 1.1
(UFFV 1.1)**, the single standard for every work of narrative fiction under
Pegasus Press. It ships as two authoritative documents in THIS folder, read
before any drafting:

- **`UFFV_1.1_FRAMEWORK.md`** — the Master Framework (governing).
- **`UFFV_1.1_PIPELINE.md`** — the executable pipeline (RUN 0 to RUN 17).

On any conflict the Master Framework wins; above it, the operator's live
instructions and the global rules file win (Framework Section 0.4). This
SKILL.md operationalizes UFFV and routes to the correct sub-overlay; it never
overrides the two documents.

> Scope: readers 13+. Fiction for ages 0-12 stays under the children's niche
> (CBF 2.0). Narrative nonfiction and true stories route to their nonfiction
> frameworks. At Phase 0 stamp `framework=UFFV 1.1` plus the overlay code into
> the `book_lock.md` classification line (global rule 16).

## The twelve sub-overlay skills

Exactly ONE primary overlay governs a title. A second genre is carried as a
modifier (at most one) whose laws also run at QA; the primary's ending law and
pacing profile govern the climax (Framework 2.3, 3.1).

| Code | Overlay | Sub-skill | Reader promise | Default structure | Novel band |
|---|---|---|---|---|---|
| OV-ROM | Romance | uapf-niche-fiction-romance | Committed, hopeful ending | ROMBEAT on 3-Act | 55k-80k |
| OV-THR | Thriller & Suspense | uapf-niche-fiction-thriller | Escalating danger, threat resolved | 3-Act fast | 70k-90k |
| OV-MYS | Mystery & Crime | uapf-niche-fiction-mystery | A fair puzzle honestly solved | MYSBEAT on 3-Act | 65k-85k |
| OV-FAN | Fantasy | uapf-niche-fiction-fantasy | A consistent second world, quest fulfilled | HJ twelve-stage | 90k-120k |
| OV-SFI | Science Fiction | uapf-niche-fiction-scifi | A rigorous What If to consequence | 3-Act or HJ | 80k-110k |
| OV-HOR | Horror & Supernatural | uapf-niche-fiction-horror | Dread built and released | 3-Act escalation | 65k-85k |
| OV-LIT | Literary & Book Club | uapf-niche-fiction-literary | Depth of character, language, theme | 3-Act loose or KTK | 70k-100k |
| OV-HIS | Historical Fiction | uapf-niche-fiction-historical | A vivid, accurate past | 3-Act or DUAL | 85k-115k |
| OV-YA | Young Adult | uapf-niche-fiction-ya | Coming of age, hopeful and true | Modifier engine + YA gates | 55k-75k |
| OV-ACT | Action & Adventure | uapf-niche-fiction-action | Momentum, victory earned | HJ or 3-Act fast | 65k-85k |
| OV-WFC | Women's Fiction & Family | uapf-niche-fiction-womens | Emotional truth, relationships transformed | 3-Act or DUAL | 70k-90k |
| OV-FTH | Faith & Inspirational | uapf-niche-fiction-faith | Faith lived with dignity | 3-Act | 60k-80k |

Formats (never change overlay content laws): FMT-NOVEL (default), FMT-NOVELLA,
FMT-SHORT (themed collection), FMT-SERIAL (series, Series Bible mandatory).

## Detection and routing (Framework Section 2, Pipeline RUN 1)

1. Fiction is detected when the operator names UFFV or an overlay; or the brief
   describes an invented story/characters/plot; or uses novel/novella/fiction/
   story/saga or a genre name in a storytelling sense.
2. Select ONE primary overlay from the table above and AT MOST one modifier.
   If two primaries genuinely tie, ask the operator ONE question offering
   exactly those two, then proceed. Never ask otherwise.
3. Load the matching **sub-overlay skill** — it carries that genre's mandatory/
   forbidden elements, ending law, structure, budgets, POV, pacing, trope menu,
   content notes, image policy, cover direction, and metadata. A world-bearing
   modifier (FAN, SFI, HIS) pulls its Phase 3 world/era gate into the pipeline.
4. Age band: YA activates when the protagonist is 14-18 and the spine is coming
   of age; OV-YA runs primary with the plot-engine genre as modifier.

## The 30 Critical Rules (absolute; full text in UFFV_1.1_FRAMEWORK.md §1)

A violation of any Critical Rule is a release-blocking defect. Binding on every
overlay, format, and marketplace. The fiction-critical spine:

- **R1 Content Rating** — declare UFFV-Clean or UFFV-Mainstream at Phase 0 (Mainstream default); it binds every chapter and QA Pass 10.
- **R2 Em/En Dash Ban** — none anywhere (manuscript, matter, metadata, image prompts, cover). Ranges use a hyphen or the word "to".
- **R3 Pen Name** — fakenamegenerator.com, First M. Surname, screened against real living authors.
- **R4 Gate Line** — every phase closes with exactly `Type Proceed`.
- **R5 Rolling DOCX** — one growing manuscript; previews are versioned read-only PDFs.
- **R6 Image Manifest** — [IMG-XX] placeholders + image_manifest.md + cowork files (fiction image policy §15).
- **R7 Book Register** / **R8 Language** / **R9 State Discipline (honest states)** / **R10 Catalogue Uniqueness** — catalogue-wide law.
- **R11 Reader Promise** — the overlay's ending law is contractual; verified at QA Pass 1 and Release QC.
- **R12 Structure Lock** / **R13 POV & Tense Lock (no head-hopping)** / **R14 Word Budget Governor (±10%)**.
- **R15 Continuity Ledger** / **R16 Timeline Integrity** / **R17 Chekhov (plant fires or is cut)**.
- **R18 Fair Play (MYS)** / **R19 Escalation (THR/HOR/ACT)** / **R20 Character Bible before drafting** / **R21 Antagonist Motive**.
- **R22 Anti-Duplication Variation Engine (echo scan)** / **R23 Hook Law** / **R24 Dialogue Law (8)** / **R25 Show Priority**.
- **R26 Research Gate (HIS + real-world content)** / **R27 No Real Living Persons** / **R28 Series Integrity** / **R29 Clean Metadata** / **R30 Correction Scope**.

## The pipeline (Framework §10, Pipeline RUN 0-17)

Twelve phases, each closing with `Type Proceed`. Standing sweeps at every gate:
em/en dash scan (must be zero), declared-rating spot check, governor line.

Phase 0 Intake & Detection → 0.5 Screens → 1 Story Spec → 2 Character Bible →
3 World Gate (conditional) → 4 Beat Sheet & Chapter Blueprint → 5 Chapter Loop
(15-point self-edit per chapter, ledgers updated, preview PDF, tension score) →
6 Whole-Book QA (12 core passes + Pass 13 series / Pass 14 collection) → 7 Front/
Back Matter → 8 Formatting → 9 Cover (UDCF) → 10 Metadata & KDP pack (blurb A/B,
7 keywords, BISAC, AI declaration) → 11 Release QC & Book Register.

Follow `UFFV_1.1_PIPELINE.md` block by block; it holds every gate template,
artifact format, reference card (blacklist, filter list, casting caps), and the
cowork file templates. Resume only from artifacts (run_state.md), never memory.

## Shared systems (parent-owned; overlays inherit)

- **Story Architecture** — the 15-Beat Master Grid (Appendix A), Structure
  Library (3ACT / HJ / ROMBEAT / MYSBEAT / KTK / DUAL), scene/sequel units,
  subplot governor (max 3), opening/closing laws, prologue/epilogue law.
- **Character System** — Character Bible before drafting; 14-field protagonist
  and antagonist sheets; naming law; three voice markers per major; arc ledger;
  casting caps by word band (Appendix D).
- **World & Continuity** — Setting Sheet (all), World Bible with source/cost/
  limit triad (FAN/SFI), Era Brief via research gate (HIS); Continuity Ledger,
  Timeline Ledger, Chekhov Registry / Clue Grid, all append-only at each gate.
- **Prose Engine** — POV discipline, the 8 Dialogue Laws, show-priority + filter
  minimization, sensory anchor, sentence-rhythm rule, the Anti-Duplication
  Variation Engine, the cliche/stock-phrase blacklist, localized for non-English.
- **Content Ratings** — UFFV-Clean vs UFFV-Mainstream, enforced at every gate
  and QA Pass 10; dignity standards and YA gates apply regardless of rating.
- **Typography & Matter** — §13 (trim, body face, chapter openers, front/back
  matter order, page estimation).
- **Series** — Series Bible, per-book laws (own conflict resolved + thread
  advanced, no hard cliffhangers), series runtime carrying prior ledgers.

## Genie integration

- **Chapter-by-chapter build law** and **editorial pass / format QA / niche gate
  / render QA** apply on top of UFFV's own gates; UFFV's ceilings and laws win on
  conflict with generic defaults.
- **Image engine**: fiction interiors are text-only except the map/plate slots in
  §15; the client's chosen image engine (per the image engine law) fills any slot;
  covers run through the cover designer under UDCF (photorealistic, no icons).
- Binds BOTH engines. Ships in every pack (fiction is base writing capability;
  covers/metadata follow the normal PRO/MAX capabilities).

## Classification line (rule 16)

`Classification (locked, machine-readable): overlay=<OV-CODE>; selected_skill=uapf-niche-fiction-<slug>; framework=UFFV 1.1; classification_locked=true; framework_locked=true`
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
