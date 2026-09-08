---
name: uapf-niche-workbook
description: Workbook / practice-book / exercise-drill niche overlay (OV-WORK) — invoked by uapf-phase0-router when the title or format signals a fill-in workbook, practice book, exercise collection, drill book, activity workbook, or worksheet-driven product.
---

# UAPF Niche: Workbooks and Practice Books (OV-WORK)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Workbook-Edition/` (config, validation, phases, and deterministic ops in `genie_workbook.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Workbook Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title contains **workbook**, **practice book**, **exercises**, **drills**, **activity workbook**, **fill-in**, or **worksheet** — or the requested format is explicitly workbook/practice-focused (a book the reader writes in, dominated by exercises rather than prose). Applies to every workbook category: medical/clinical study, academic and exam preparation, technical and trades, business and professional development, creative skills, language learning, self-development, and any other niche. Derived from UWGF v1.7 (Universal Workbook Generation Framework); where this overlay states a layout law, the overlay governs.

## Expert Panel

1. **Domain Master** — subject-matter authority for the workbook's discipline (e.g., clinical educator for medical, credentialed exam coach for test prep, master tradesperson for trades). Verifies every fact, term, and exercise premise; owns accuracy sign-off at Gate 1.
2. **Instructional Designer** — owns the practice architecture: exercise sequencing, scaffolding across the three difficulty bands, spaced repetition and skill progression, question/answer integrity, and the 70–80 percent worksheet share.
3. **Assessment & Answer-Key Auditor** — independently works every exercise, verifies that every question has a determinate, checkable answer, and certifies the complete answer key with worked solutions. Nothing ships that this auditor has not solved.
4. **Print Layout Engineer** — enforces the interior layout laws: 10 pages per chapter, 8.5 x 11 trim, B&W-safe tables, justified body text, response-space sizing for handwriting, Word automation (styles, auto-TOC, page-number fields).
5. **KDP Compliance Officer** — trademark screening, category/metadata strategy, prohibited-claims review, content-standards catalogue compliance, and the KDP rejection triggers specific to workbooks (foremost: incomplete answer keys).

## Phase 0 — Title Analysis

Run the moment the title arrives, in this exact order, before generating anything else:

1. **Trademark and risk screen.** Screen the exact title for trademark conflicts and KDP-risk terms (test names, certification brands, curriculum brands are the highest-risk zone for workbooks — e.g., exam names owned by testing bodies). Report findings and risk level first. If the title contains a protected exam or brand name, propose compliant reformulations ("...for the [subject] exam"-style genericization) before proceeding.
2. **Language lock.** Detect the title language and lock it as the manuscript language for all book content (worksheets, instructions, images, answer key). Operator-facing workflow output stays in English.
3. **Niche analysis.** State explicitly: the discipline, scope boundary (what is in and out), implied audience and expertise level, the core competencies the workbook must build, and the niche-adaptation profile that applies (medical/clinical, academic/exam-prep, technical/trades, business, creative, language, self-development).
4. **Subtitle engine.** Generate 6–8 KDP-compliant subtitle options: title + subtitle at or under 200 characters combined; subtitle itself 50–150 characters; benefit-driven and keyword-bearing (lead with outcome + practice volume, e.g., number of exercises, "with complete answer key"); no bestseller language, pricing, or promotional claims. Mark one RECOMMENDED with a one-line rationale and adopt it as the working subtitle (operator may override at the specification gate).
5. **Auto-configuration.** Answer every mandatory project question yourself, each with a one-line rationale: chapter/unit count (validated against the page budget), exercises per unit, the exercise-type mix (at least three worksheet types per chapter drawn from the six-type library: fill-in, multiple-choice/objective, short-answer, applied scenario/case, template/planning, self-evaluation/rubric), audience expertise level, reference-material approach (operator materials, current web research, or hybrid), line spacing (1.15 default; 1.5 for senior/elderly editions), and the accent treatment (see Interior Design — grayscale-safe). Surface all selections at one specification gate; the operator may override any before typing Proceed.
6. **Page budget validation.** Before the TOC gate, project the total: front matter ~6 pages, Introduction 2, chapters at exactly 10 pages each, Conclusion 1.5, appendices including the full answer key (budget generously — worked solutions are long). Total must not exceed 150 pages, hard cap. At 10 pages per chapter the budget supports up to 13 chapters at minimal appendix weight, realistically 10–12 with a proper worked-solutions key. If the projection exceeds 150, reduce chapter count, never chapter depth, and re-confirm.
7. **Specification gate.** Present the working subtitle, all auto-selections, the difficulty-band plan, and the page-budget arithmetic in one message, then stop at the gate (Type Proceed).

## Book Architecture

**Structural unit: the Practice Unit (= one chapter, exactly 10 pages).** Every chapter in the book is a practice unit built to this fixed formula:

| Component | Pages | Content |
|---|---|---|
| Concept briefing | 0.5–1 | The minimum teaching needed to attempt the exercises. Explanatory text never exceeds 0.5 pages per section. Stated once, plainly, at the audience reading level. |
| Band 1 — Foundation | ~2.5–3 | Warm-up and recognition exercises. Objective formats dominate (fill-in, matching, multiple choice). Builds confidence and vocabulary. |
| Band 2 — Development | ~3 | Core skill practice. Short-answer, structured problems, guided application. The bulk of the unit's learning load. |
| Band 3 — Mastery / Challenge | ~2.5–3 | Applied scenarios, multi-step problems, transfer tasks, exam-style items where relevant. Stretches the learner beyond the briefing. |
| Unit checkpoint | 0.25–0.5 | Self-check summary, progress tracker row, pointer to the answer key. |

- **Three difficulty bands per unit is mandatory.** Every unit ramps Foundation → Development → Mastery. Band labels are printed in the unit so the reader can see the ramp.
- **Worksheet share: 70–80 percent** of every chapter is exercises and activities; explanatory text 20–30 percent. Learners spend their time doing, not reading. When content must be cut to fit 10 pages, cut text, never exercises.
- **At least three exercise types per unit** from the six-type library; the mix is auto-selected per niche in Phase 0.
- **Response spaces sized to the expected answer** — real handwriting room: ruled lines for prose answers, boxes for numeric work, tables for structured responses. A workbook the reader cannot physically write in is a failed workbook.
- **Question/answer integrity:** every question has a determinate, checkable intent; no exercise may demand knowledge the briefing has not provided or the audience level cannot supply.
- **Labelled images** (diagrams, charts, illustrations with callout labels) wherever they aid practice; **required** for medical, scientific, technical, and academic workbooks. Labels accurate, legible, in the manuscript language, and B&W-legible. If image generation is unavailable, embed a complete descriptive generation prompt plus exact placement instead.

**Front matter (locked order, unnumbered):** title page (title, working subtitle, generated author name, restrained styling) → copyright and disclaimer page (~400 words, five components: copyright notice 50–75 w; general disclaimer and limitation of liability 150–200 w; educational-use statement 75–100 w; professional-advice notice tuned to the niche's liability tier 50–75 w — strengthened for medical, health, legal, financial; publication info 25–50 w) → Preface, exactly 1 page → How to Use This Workbook, exactly 1 page (explains the difficulty bands and the answer key) → Word auto-TOC (References field, dot leaders, heading levels 1–3). Page numbering begins at the Introduction, printed page 1, via a section break and Word page-number fields. Author name generated from fakenamegenerator.com in the format First Name, Initials. Surname, shown on the title page and copyright page.

**Introduction:** 2 pages maximum, natural paragraphs only, no bullet points: Welcome (0.5), What You Will Learn (0.5), Prerequisites and Preparation (0.5), Success Tips (0.5), plus one cross-reference sentence to the How to Use page.

**Conclusion:** exactly 1.5 pages — recap of the skill journey, encouragement to keep practicing, concrete next steps, courteous invitation to leave an honest review.

**Back matter (appendices):** in order — **the complete answer key with worked solutions (mandatory, see Content Rules)**, printable blank templates of key worksheets, progress tracker, glossary of niche terms, quick-reference guides and conversion/reference charts where the niche calls for them.

**Page bands:** whole book 150 pages hard cap; chapters exactly 10 pages each; front matter ~6; Introduction 2; Conclusion 1.5; answer key + appendices sized in the Phase 0 budget.

## Interior Design

Inherits UAPF DOCX automation defaults (real heading styles, References auto-TOC with dot leaders, page-number fields, section break before the Introduction, no manual formatting) with these OV-WORK layout laws:

- **Trim: 8.5 x 11 inches (US Letter), primary and default.** Margins 0.7 inches on all four sides. Full-page room for handwriting is the point of the trim.
- **Typography:** Times New Roman throughout. Body 11–12 pt (13–14 pt for senior/elderly audiences). Chapter headings 16 pt BLOCK CAPITALS, centered. Section/band headings 13 pt ALL CAPS bold, left-aligned. **Body text fully justified**; numbered and bulleted lists left-aligned. Line spacing 1.15 (1.5 for senior editions). Em dashes banned catalogue-wide; use commas, colons, or parentheses.
- **Tables — B&W-safe ONLY (overrides the UWGF color-header spec):** native Word Table Grid objects, single half-point black borders on every cell, **white cells, black text, no color fills anywhere**. Header rows: bold, with **at most 15 percent gray shading** — never accent colors, never white-on-color text. **All table text is LEFT-ALIGNED** (headers and body cells alike). Consistent column widths, adequate cell padding, row heights tall enough to write in where the table is a fill-in exercise. ASCII, markdown, and pipe-character pseudo-tables are prohibited in all deliverables.
- **Grayscale visual identity:** because interiors must print B&W-safe, per-title uniqueness (no two workbooks look alike) is achieved through typographic treatment, rule weights, band-label styling, callout-box borders, and imagery style — not color fills. All diagrams and shading must remain legible in pure black-and-white print.
- **Difficulty-band markers:** each band opens with a labelled band header (e.g., "BAND 1 — FOUNDATION") so the ramp is visible at a glance; use a consistent, B&W-safe marker style throughout the title.

## Content Rules

- **The fatal flaw to avoid: an incomplete answer key.** Every objective exercise gets its answer; every problem gets a **worked solution** showing the steps, not just the result; every open-ended exercise gets a model answer or explicit evaluation criteria. An answer key that is missing, partial, or answers-only is a KDP rejection trigger and an automatic Gate 4 failure. The Assessment Auditor must independently work every exercise before the key is accepted.
- **Exercises match the answer key exactly:** numbering, wording, and values in the key mirror the printed exercises one-for-one. Any correction to a chapter forces a matching correction pass on the key.
- **Text is capped:** maximum 0.5 pages of explanatory text per section; concepts stated once, then practiced. Reader-facing instructions are imperative, concrete, and short.
- **Difficulty honesty:** Band 3 may stretch, but never beyond what the briefing plus prior units make solvable. Exam-prep units mirror the real exam's formats and timing conventions (genericized — no protected exam branding).
- **Niche adaptation:** medical/clinical — labelled anatomical/clinical diagrams mandatory, current standard terminology, strengthened disclaimers; academic/exam-prep — exercises mirror curriculum/exam formats, labelled diagrams mandatory; technical/trades — spec tables, safety callouts, checkpointed procedures; business — frameworks, templates, planning worksheets, invented organizations for cases; creative/skills — practice progressions and self-evaluation rubrics; language — graded drills with full answer translations in the key.
- **Catalogue hard rules:** absolute content restrictions, no exceptions (no alcohol, pork/pig derivatives, or gambling promotion in any example, scenario, image, or image prompt; use compliant substitutions). No em dashes. Manuscript in the title's language; operator-facing output in English. No content reproduced from copyrighted test banks or textbooks — every exercise is original.
- **Delivery:** one rolling manuscript DOCX; every approved phase appended and re-delivered; every phase ends at a gate with the exact final line "Type Proceed"; corrections applied exactly and only as scoped, then re-gated.

## QA Checklist

**Gate 1 — Accuracy (per chapter and whole book):**
- [ ] Every fact, term, formula, and exercise premise verified by the Domain Master (target ≥95 percent accuracy; sources ≥90 percent authoritative)
- [ ] Every exercise independently solved by the Assessment Auditor; solutions reproduce the key exactly
- [ ] No exercise requires knowledge not provided by the briefing or prior units
- [ ] Labelled images accurate; all labels correct and in the manuscript language

**Gate 2 — Structure (per chapter):**
- [ ] Chapter is exactly 10 pages
- [ ] Three difficulty bands present, labelled, and genuinely ramped (Foundation → Development → Mastery)
- [ ] Worksheet share 70–80 percent; at least three exercise types used
- [ ] Concept briefing within the 0.5-page-per-section text cap
- [ ] Response spaces sized for real handwriting
- [ ] Chapter appended to the rolling DOCX before the gate

**Gate 3 — Layout and formatting (per chapter and whole book):**
- [ ] 8.5 x 11 trim, 0.7-inch margins, Times New Roman, body fully justified
- [ ] All tables native Word objects: white cells, black half-point borders, header shading ≤15 percent gray, no color fills, all table text left-aligned
- [ ] No ASCII/markdown/pipe pseudo-tables; no em dashes anywhere
- [ ] Headings on real Word styles; auto-TOC updates cleanly; page numbering starts at the Introduction; front matter unnumbered and in locked order
- [ ] All imagery and shading legible in pure B&W print
- [ ] Visual identity unique against the catalogue (typographic/structural, not color)

**Gate 4 — Release:**
- [ ] **Answer key complete: every exercise answered, every problem's solution worked step-by-step, model answers/rubrics for open items — zero gaps**
- [ ] Key numbering and values match the final printed exercises one-for-one after all corrections
- [ ] Total pages ≤150; budget arithmetic re-verified; Introduction 2 pp; Preface and How to Use 1 p each; Conclusion exactly 1.5 pp
- [ ] Appendices complete (key, templates, tracker, glossary); progress tracker rows match the final unit list
- [ ] Trademark findings re-confirmed against final title and subtitle; content standards swept; manuscript language consistent
- [ ] 100 percent of promised competencies covered by at least one unit

## KDP Positioning

- **Category tree:** primary in the discipline's own tree — e.g., Education & Teaching > Studying & Workbooks (and Test Preparation for exam-prep titles); Medical Books > Education & Training for clinical study workbooks; Foreign Language Study for language drills; Business & Money > Skills for professional workbooks; Crafts, Hobbies & Home for creative practice. Build the full ten-category placement plan across all marketplaces, pairing high-relevance categories with winnable-rank categories, with per-marketplace notes where browse trees differ.
- **Description (2,000–4,000 characters, seven-part structure — hook, problem, solution promise, what's inside, who it's for, credibility/method, call to action; HTML bold tags on key phrases):** lead with **practice volume and completeness** — the number of exercises, the three-band difficulty ramp, and the **complete answer key with step-by-step worked solutions**. Buyers of workbooks scan for "how much practice" and "are answers included"; put both in the first two lines. State the large-format 8.5 x 11 write-in design. No prohibited claims; literally accurate to the book.
- **Backend keywords:** seven fields ≤50 characters each, distinct search-intent clusters, no words already in the title/subtitle, no competitor or exam-brand names, no quality claims. Prioritize clusters like "[skill] practice problems", "[audience] exercises with answers", "[subject] drill book".
- **Metadata signals:** exercise count in the subtitle where it fits; "with Answer Key" or "with Complete Worked Solutions" is a proven conversion phrase for this niche; audience level named explicitly (Beginner/Grade/Certification-candidate). Competitive scan of top rival workbooks (length, price, format, review posture) plus a recommended list and promotional price with rationale, delivered in the separate marketing DOCX.

## Key Rules — Do NOT Break

1. **10 pages per chapter, exactly.** Not 9, not 11. Cut text, never exercises, to hit it.
2. **Three difficulty bands in every unit** — Foundation, Development, Mastery — printed, labelled, and genuinely ramped.
3. **Complete answer key with worked solutions is mandatory.** Every exercise answered, every solution showing its steps; an incomplete key is a KDP rejection trigger and an automatic release block.
4. **B&W-safe tables only:** white cells, black half-point borders, header shading at most 15 percent gray, no color fills anywhere, all table text left-aligned, native Word objects only.
5. **Body text fully justified;** lists left-aligned; Times New Roman; no em dashes anywhere in any deliverable.
6. **8.5 x 11 primary trim,** 0.7-inch margins, 150-page hard cap validated before the TOC.
7. **70–80 percent worksheets** in every chapter; explanatory text capped at 0.5 pages per section; at least three exercise types per unit.
8. **Trademark-screen the title before anything else;** never use protected exam, certification, or curriculum brand names.
9. **Gate everything:** one phase per message, rolling DOCX re-delivered at every gate, every gated message ends with the exact final line "Type Proceed", and no advancement without it.
10. **Catalogue hard rules bind:** absolute content restrictions with compliant substitutions, per-title visual uniqueness (achieved grayscale-safe), pen name from fakenamegenerator.com in First Name, Initials. Surname format, and title-language manuscript with English operator output.

## HOUSE REFERENCE BANK — EDUCATIONAL WORKBOOKS (2026-08-14)

Five catalog masters are banked at `cover_db/_interiors/workbook/` (local
only, never shipped): The Executor's Workbook, Dosage Calculations for
Nursing Students, ECG Workbook, Financial Analysis Workbook, and the Fluid
and Electrolyte Workbook for Nurses. BINDING for every educational workbook
on BOTH engines (Claude and Codex) and on every install; where the bank
folder is absent (client installs never receive it), the codified standards
below carry the full weight of the reference study. CONSULT the masters
where present: open 2 or 3 and study a worksheet page, an answer-key page,
and a register/checklist page.

Standards verified across the bank:

* FORMAT: 8.5 x 11, roughly 150 to 200 pages, Times New Roman 11 to 12 pt,
  text- and table-led (images only where the subject needs them, e.g. ECG
  strips); the binding heading law governs chapter titles and subheads.
* NUMBERED WORKSHEET UNITS: every exercise is a numbered worksheet
  ("Worksheet 5.2: Hypernatremia Analysis") opening with a full-width
  shaded header bar in the book's principal color (white text) and an
  italic one-line Purpose statement beneath it.
* PROMPT/RESPONSE TABLES: the core working unit is a two-column table,
  bold prompt cells on the left, generous ruled blank response space on
  the right, with shaded column headers (the "Clinical Prompt | Your
  Response" form). Response space is REAL working space: sized for
  handwriting, never a token gap.
* REGISTERS AND CHECKLISTS: practical workbooks carry fill-in registers
  (the Executor's "SECTION A: REQUIRED RETURNS REGISTER" form): shaded
  ALL-CAPS section bars and multi-column tables whose blank columns the
  reader completes (Y/N, dates, amounts, confirmation numbers).
* CASE AND TAKEAWAY PANELS: tinted panels with a colored ALL-CAPS lead-in:
  case scenarios ("CLINICAL CASE:") feeding the worksheets that follow,
  and end-of-chapter "KEY TAKEAWAYS:" panels with numbered rules. At least
  two panel families per book.
* ANSWER KEYS: separate keyed sections (never under the questions, per
  house rules): numbered answers in bordered two-column grids, each with a
  bold "Explanation:" lead-in showing the worked reasoning, not just the
  result.
* ONE ACCENT SYSTEM PER BOOK, NO REPEATS: the masters run navy, blue,
  black-bar, and other distinct systems. NO TWO WORKBOOKS share the same
  palette, header-bar treatment, table style, or panel family
  (No-Two-Books-Alike, operator restated 2026-08-14).
* DENSITY: intentional response space is required and does not count as
  empty; dead trailing white space after completed content is the retired
  pattern; the density laws and render QA govern the final page.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
