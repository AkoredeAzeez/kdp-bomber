---
name: uapf-niche-crafts
description: Craft and hobby project books — invoked by uapf-phase0-router when title signals crochet, knitting, sewing, DIY, needlecraft, quilting, woodworking, ceramics, macrame, stained glass, candle making, scrapbooking, or any project-count-driven hobby niche.
---

# UAPF Niche: Crafts & Hobbies — Project Books (OV-CRAFT)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Crafts-Edition/` (config, validation, phases, and deterministic ops in `genie_crafts.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Crafts Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title contains any of the following craft or hobby signals — crochet, knitting, sewing, crafts, DIY projects, home improvement (DIY-facing), gardening projects, needlecraft, ceramics, woodworking, hobby, stained glass, macrame, quilting, scrapbooking, candle making, embroidery, cross-stitch, weaving, loom, beading, resin, decoupage, leatherwork, soap making, wreath making, card making, origami, jewelry making, or any title where the core deliverable is a numbered set of hands-on projects.

**NOT routed here when:** The title is a maintenance/repair manual for a product (route to OV-GUIDE), a step-by-step skill tutorial with no project count (route to OV-HOWTO), or a gardening reference book focused on plant science rather than make-and-create projects.

---

## Expert Panel

1. **Master Multi-Craft Coordinator** (Domain Master) — 25+ years across 8+ craft disciplines with guild leadership, instructor certification, and craft business development. Governs project structure integrity, technique accuracy, tool and materials specifications, and cross-craft skill transfer. Signs off on every project unit before it advances to layout.

2. **Textile Arts & Cultural Preservation Specialist** — 25+ years in traditional and contemporary fiber arts (knitting, crochet, needlecraft, weaving, quilting, embroidery). Validates stitch notation accuracy, pattern symbols, cultural attribution of traditional techniques, and therapeutic application claims. Required on all fiber-art, needlecraft, and textile titles.

3. **Construction & Home Systems Authority** — 22+ years in construction and sustainable building. Required on woodworking, home improvement DIY, ceramics (kiln and ventilation safety), stained glass (chemical and cutting safety), and any project involving power tools, adhesives, or structural elements. Validates all OSHA-adjacent safety callouts.

4. **Environmental Science & Sustainable Living Expert** — 15+ years in environmental science and sustainable lifestyle implementation. Validates eco-material sourcing claims, VOC and chemical safety disclosures, and sustainable craft practice guidance. Required when projects use resins, dyes, solvents, or specialty adhesives.

5. **Therapeutic Arts & Wellness Specialist** — 15+ years art therapy and adult wellness programming (ATR-BC). Advises on therapeutic framing, stress-reduction benefit claims, and mindfulness integration where the title positions crafting as a wellness activity. Consulted when title or subtitle includes "mindful," "stress-free," "therapeutic," "relaxing," or "self-care."

**Panel Consensus Rule:** All five experts must agree that every safety callout is correctly placed (at the hazard step, not in a preface note) before Gate 3 clears.

---

## Phase 0 — Title Analysis

Execute all steps in sequence before any content is generated.

### Step 0-A: Trademark Clearance (MANDATORY FIRST ACTION)

Extract every distinctive word, phrase, product name, and brand-like term from the submitted title and all candidate subtitles. Generic descriptive words (crochet, knitting, beginner, projects) are exempt.

**Craft-Space Brand Alert — these are registered marks that must NEVER appear in a title or subtitle:**
Cricut, Mod Podge, Sharpie, X-Acto, Dremel, Perler, Crayola, LEGO, Ravelry, Etsy (as a product endorsement), Tunisian (only if claimed as a brand), Lion Brand, Red Heart (yarn brand names), Fiskars, Bernina, Brother (sewing machines).

Registry coverage: USPTO (US) Class 16 + Class 9, EUIPO (EU), UKIPO (UK), CIPO (Canada), IP Australia, JPO (Japan) — matched to target marketplace.

**Verdicts:**
- CLEAR: Proceed to Step 0-B.
- CAUTION: Present 3-5 reworded alternatives preserving keyword intent; require operator approval before advancing.
- BLOCKED: Title must change. Present 3-5 alternative titles with same keyword intent. Halt until resolved.

**Output:** Trademark Clearance Report (system layer, English) listing every term checked, registry queried, mark status, and final verdict. No content work begins until CLEAR or approved CAUTION is confirmed.

### Step 0-B: Craft Sub-Niche Classification

Classify the title into one of these OV-CRAFT sub-niches. The sub-niche governs the expert panel composition, safety callout set, and material-science depth required.

| Sub-Niche Code | Triggers |
|---|---|
| CRAFT-FIBER | knitting, crochet, embroidery, cross-stitch, needlepoint, tapestry, macrame, weaving, loom, quilting, sewing, stitching |
| CRAFT-WOOD | woodworking, wood carving, pyrography, wood burning, scroll saw, turning |
| CRAFT-GLASS | stained glass, mosaic, fused glass, glass painting |
| CRAFT-RESIN | resin art, epoxy projects, resin jewelry, casting |
| CRAFT-PAPER | scrapbooking, card making, origami, paper crafts, bookbinding |
| CRAFT-CANDLE-SOAP | candle making, soap making, bath bombs, wax crafts |
| CRAFT-CERAMIC | ceramics, pottery, clay projects, sculpting |
| CRAFT-GENERAL | DIY projects, crafts (general), hobby projects, seasonal crafts, multi-craft |
| CRAFT-GARDEN | garden crafts, floral arrangement, wreath making, pressed flowers |
| CRAFT-JEWELRY | jewelry making, beading, wirework, metal stamping |

Record the sub-niche code in the configuration report. If the title spans multiple sub-niches, assign the primary code and list secondary codes — secondary codes expand the expert panel and the safety callout set.

### Step 0-C: Project Count Extraction

**THE PROJECT COUNT IS ALWAYS SUPPLIED BY THE USER INSIDE THE TITLE. The framework NEVER invents or overrides this number.**

Extract the explicit project count from the title (e.g., "50 Crochet Projects" = 50 projects). If no count appears in the title, flag it in the configuration report and note: "Project count not specified in title — framework will size content to the selected page band with project count estimated at completion."

Record: Project Count = [N] (from title) or [unspecified].

### Step 0-D: Audience & Difficulty Range Analysis

From the title language, extract:
- **Declared skill level:** beginner / intermediate / advanced / all-levels / unspecified
- **Age audience:** adult (default) / senior / family / children (requires age-appropriate safety uplift)
- **Project complexity signal:** quick projects (under 2 hours), weekend projects (2–8 hours), extended projects (8+ hours)

These three parameters drive: body font size selection (11pt standard; 13pt for seniors), line spacing selection (1.15 standard; 1.5 for seniors/large-print), and the Difficulty/Time/Cost META line defaults on each project unit.

### Step 0-E: Subtitle Generation

Generate 7 subtitle candidates using these formulas. Every candidate must pass the Step 0-A trademark screen before presentation.

1. [Project Count] + [Technique/Material] + [Skill Level] + Projects + [Benefit]
2. [Skill Level] Guide to + [Craft Name] + with + [Project Count] + Step-by-Step Patterns
3. [Project Count] + [Time Signal, e.g., "Weekend"] + [Craft] + Projects for [Audience]
4. From Beginner to [Advanced Milestone]: [Project Count] + [Craft] + Projects with Full Instructions
5. [Project Count] + Beautiful + [Craft] + Projects — Complete Instructions, Materials Lists & Patterns
6. [Craft Name] for [Audience]: [Project Count] + [Difficulty] + Projects with [Visual Promise]
7. The Complete [Craft Name] Project Book: [Project Count] + Designs with Step-by-Step Instructions

Present all 7. State the recommended subtitle with strategic justification. Note which KDP search terms the recommended subtitle captures.

### Step 0-F: Auto-Configuration

After trademark clearance and subtitle selection, auto-select and announce the complete configuration. Do not ask the user to select — present it and request Proceed confirmation.

| Parameter | Selection Logic |
|---|---|
| Content Pathway | Hybrid (web research + knowledge base) for all OV-CRAFT titles unless operator uploads reference materials |
| Page Band | 80–150 pp (compact, 25–40 projects); 180–250 pp (standard, 41–75 projects); 280–350 pp (extended, 76–120 projects) |
| Visual Density | Heavy Visual (80–150+ images) — every project unit requires one hero image + one image per key step |
| Body Font Size | 11pt (standard adult); 13pt (seniors/large-print signal in title) |
| Line Spacing | 1.15 (standard); 1.5 (senior/large-print) |
| Layout Engine | Adapted Cookbook — two-column project containment (see Book Architecture) |
| Interior Color | Two-color professional: primary accent + secondary accent (from Design Signature palette) |
| Design Signature | Composed from six dimensions per Module 4.6; announced in configuration; operator logs to register |

**Configuration Gate:** Present configuration summary ending with: "Shall I proceed with the Table of Contents? Type Proceed to continue."

---

## Book Architecture

### Structural Unit: The Project Unit

Every craft book produced under OV-CRAFT is organized as a collection of **Project Units**. A Project Unit is the atomic deliverable — one complete, self-contained craft project.

**Project Unit Template (mandatory for every project):**

```
PROJECT TITLE                          [16pt, block caps, centered, primary accent color]
──────────────────────────────────────────────────────
META LINE:  Difficulty: [Beginner/Intermediate/Advanced]  |  Time: [X hrs]  |  Cost: [$X–$X]
──────────────────────────────────────────────────────
HERO IMAGE: [One full-width or half-column photograph of the completed project]

MATERIALS & TOOLS
  • [Item 1 with quantity and specification]
  • [Item 2 ...]
  [Safety note if any hazardous material is listed here]

INSTRUCTIONS
  Step 1. [Action verb + exact instruction + precision detail]
           [STEP IMAGE - MANDATORY: one image per step, generated and embedded]
           [SAFETY CALLOUT if hazard occurs at this step]
  Step 2. ...
  [Continue through final step - EVERY step carries its own image]

  Expected result: [Description of the correctly completed project]

PROJECT FACTS TABLE
┌─────────────────┬─────────────────────────────────┐
│ Skill Techniques│ [List techniques used]           │
│ Yarn/Material   │ [Specification with weight/grade]│
│ Hook/Tool Size  │ [Exact size in metric + imperial]│
│ Gauge/Tension   │ [Where applicable]               │
│ Finished Size   │ [Dimensions]                     │
│ Variations      │ [Color/size/material alternatives]│
└─────────────────┴─────────────────────────────────┘
```

**Unit-element vocabulary (house standard, from the corpus).** Every project unit uses the exact house labels, bold lead-words, in this order:
- *Fiber crafts (crochet/knit/Tunisian/amigurumi):* `Skill Level` → `Yarn` → `Hook` → `Gauge` (where it matters; "gauge is not critical" allowed) → `Finished Size` → `Abbreviations` (or a pointer to Appendix A) → `Pattern Notes` → instructions as `Round 1 / Round 2 ...` (in-the-round) or `Row 1 / Row 2 ...` (flat) → `Assembly` → `Finishing`.
- *Non-fiber crafts (glass/wood/resin/clay/paper/general):* `Difficulty` → `Time` → `Materials` → `Tools` → instructions as `Step 1 / Step 2 ...` → `Assembly` (where parts join) → `Finishing` → `Tip` / `Variation` (optional close).
Labels never improvise ("What You Need", "Supplies", "Directions" are all non-house; use the standard set).

**Step-image law (operator directive 2026-08-19).** Projects are written STEP BY STEP and EVERY step carries its own image: a photoreal or technically accurate step photo/diagram showing exactly the action or state that step describes, generated with the book's locked image engine, checked against its caption under the image realism law, and embedded at the step (never batched at the end of the unit). A project step without its image is an incomplete unit and FAILS the per-project gate. Fiber-craft Round/Row instructions image at technique-change points and milestone shapes (minimum one image per 5 rounds/rows plus every new technique); Step N instructions image every step.

### HOUSE TOC ARCHITECTURE (BINDING LAW, derived from the 43-book house corpus, operator directive 2026-08-19)

The full skeleton of every OV-CRAFT book follows the proven house pattern extracted from the Pegasus Press craft corpus. This is the law; deviations require an explicit operator instruction.

```
INTRODUCTION                                  (page 1; pagination starts here)
CHAPTER 1: [TOOLKIT / MATERIALS CHAPTER]      (hooks/tools, materials, workspace, safety)
CHAPTER 2: [CORE TECHNIQUES / FOUNDATIONS]    (technique reference, reading patterns, gauge)
CHAPTER 3..N: [PROJECT CHAPTERS]              (one of the three sanctioned grouping modes)
CHAPTER N+1: TROUBLESHOOTING [YOUR CRAFT]     (dedicated problem->cause->fix chapter)
APPENDIX A / B / C (up to F): [references]    (lettered, from the sub-niche appendix menu)
ACKNOWLEDGMENTS                               (final page)
```

**Introduction interior (standard H2 set).** The Introduction carries the house H2 vocabulary, 3 to 5 of: `Who This Book Is For`, `How This Book Is Organized`, `How to Use This Book`, `What This Book Covers`, `A Note on [Yarn Substitution / Colour / Gauge / Measurements]`, `Before You Begin`. "How to Use This Book" lives INSIDE the Introduction as an H2 (its own front-matter page only when the book's unit format needs a full-page explanation).

**Chapter naming law.** Chapter titles are `CHAPTER N: DESCRIPTIVE NAME` in BLOCK CAPS (28pt+ at 8.5x11 per the heading law). Project-range suffixes in parentheses are encouraged for tier chapters: `CHAPTER 4: TIER 1 - ACCESSORIES (PROJECTS 1-10)`. Chapters median 8 to 12 per Standard book.

**The three sanctioned project-grouping modes** (choose by title keyword emphasis):
1. **Difficulty ladder** — project chapters climb Beginner -> Building -> Confident; each chapter is one rung. Best for "for Beginners" titles.
2. **Category tiers** — chapters group by product category (accessories, tops, blankets; or animals, rattles, mobiles), 8 to 12 projects per chapter, PROJECTS NUMBERED CONTINUOUSLY across the whole book (1..40, never restarting per chapter). For 4+ categories, wrap chapters in `PART ONE: [CATEGORY]` part-openers. Best for collection titles ("40 Granny Square Wearables").
3. **Technique curriculum + flat patterns** — CHAPTERS 1-7 teach the craft as a course, then every project is its own top-level `PROJECT N: NAME` heading (flat, sequential, evocative 2-4 word names). Best for pattern-book titles ("Copper Foil Stained Glass": 7 technique chapters then PROJECT 1-20).

**Word heading styles are MANDATORY (mechanical gate).** Every chapter, part, project, and section heading must carry a real Word Heading style (Heading 1 for chapters/parts/flat projects, Heading 2 for projects-within-chapters and sub-sections, decimal-numbered H2s like `1.1`, `1.2` allowed for curriculum books). Direct-formatted bold text posing as a heading is a PRODUCTION FAILURE: it silently breaks the live TOC and the pagination checks. 7 of 43 corpus books had this defect; the gate now catches it.

**Heading case law (operator directive 2026-08-19).** Chapter-level headings (H1: chapters, parts, flat PROJECT N titles, appendices) are BLOCK LETTERS. Subchapter headings (H2) are Sentence case (capitalize the first word and proper nouns only). Mixed conventions in one book are a FAIL.

**New-page law.** Every chapter (every H1 unit: chapter, part opener, appendix, Acknowledgments) STARTS ON A NEW PAGE (page-break-before on the H1, never a manual empty-paragraph stack). Flat PROJECT N units in pattern-book mode also start on a new page.

**Pagination law.** Page numbering starts at the Introduction, whose first page is page 1; front matter before it (title page, copyright, TOC) shows no folio numbers. This is the global pagination law applied to every craft book; the final TOC is reworked against the final rendered layout and verified entry by entry.

**Section Opener Pages:** Each project chapter opens on a new page with a divider carrying: the chapter number and title (primary accent color, block caps), a 2-3 sentence overview, and a visual preview strip (thumbnails of 3-4 projects in the chapter).

### Page-Band Targets

| Book Size | Project Count Range | Target Page Count | Sections |
|---|---|---|---|
| Compact | 25–40 projects | 80–150 pages | 3–4 sections |
| Standard | 41–75 projects | 180–250 pages | 5–6 sections |
| Extended | 76–120 projects | 280–350 pages | 7–10 sections |

**Two-Projects-Per-Page Rule (Double-Column Layout):**
Short projects (under 6 steps, no pattern chart) may be formatted two per page in double-column. Projects with stitch patterns, charts, full-page photos, or more than 8 steps occupy a full page minimum. Project Units must be **contained** — a project never splits between a right-hand and left-hand page opening if containable; use a blank half-column fill or "continued on next page" cue only when containment is impossible due to step count.

### Front Matter (Mandatory Order)

1. **Title Page** — Title, author name (First Name, Middle Initial. Surname). No publisher or imprint line (global hard rule 4).
2. **Copyright Page** — Copyright line + year + author name; all-rights-reserved statement; reproduction prohibition; disclaimer and liability notice (crafts-specific: tool safety, individual results vary); trademark acknowledgment for any technique names; edition statement. No publisher name, no ISBN placeholder.
3. **Table of Contents** — LIVE Word TOC field built from real Heading styles (never hand-typed entries); lists chapters, parts, and all project titles with page numbers; reworked against the final rendered layout at completion per the pagination law.
4. **Introduction** — Begins on page 1 (visible pagination starts here). Carries the standard house H2 set (Who This Book Is For; How This Book Is Organized; How to Use This Book; A Note on [X]; Before You Begin) and covers context, what the reader will make, and how the book teaches. Length: 1,500–2,500 words. The toolkit/materials deep-dive belongs to CHAPTER 1, not the Introduction.

A separate Preface is NOT used in house craft books (the corpus is unanimous); the author's voice and promise open the Introduction instead.

### Back Matter (Mandatory Order, per the house corpus)

1. **TROUBLESHOOTING chapter** — the last numbered chapter: common problems → causes → fixes, organized by symptom, specific to this book's craft and projects. This replaces a generic "Conclusion" (the corpus closes with troubleshooting, not pep talk; a short closing paragraph may end this chapter).
2. **Lettered Appendices (A, B, C; up to F)** — 3 to 4 from the sub-niche menu:
   - *Fiber:* Stitch Reference / Abbreviations & Symbol Key; Yarn Weight & Hook Size Reference; Size Charts & Yardage Estimator; Yarn & Colour Selection Reference.
   - *Glass/Wood/Resin:* Technique Quick Reference; Materials & Tool Reference; Pattern Templates (with enlargement percentages); Safety Checklist.
   - *Any:* Materials Master Shopping List; Measurement Conversion Chart; Project Difficulty Index; craft-appropriate Safety Self-Checklist (mandatory for baby/child-use projects, e.g. Baby Safety Checklist).
3. **Acknowledgments** — brief, final page of the book.

---

## Interior Design

**Trim Size:** 8.5 × 11 inches (US Letter). All four margins: 0.7 inches. Increase inside margin only for books above 500 pages to meet KDP gutter requirements.

**Font:** Times New Roman throughout.

**Body Text:** 11pt (standard adult); 13pt (seniors or "easy/simple/large print" in title). Justified alignment.

**Line Spacing:** 1.15 (standard); 1.5 (seniors or "large print" signal).

**Chapter/Section Headings:** 16pt, BLOCK CAPITAL LETTERS, center aligned, primary accent color.

**Project Title (within Project Unit):** 14pt, Title Case, center aligned, primary accent color. Bold.

**META Line:** 10pt, small caps or italic, center aligned, secondary accent color.

**Subheadings within Project Unit** (Materials, Instructions, Project Facts): 11pt, Title Case, left aligned, bold, secondary accent color.

**Step Numbers:** Bold. Steps left aligned.

**Two-Color Interior:** Primary accent color applied to section dividers, project titles, section headings, table headers, and TOC section headings. Secondary accent applied to META lines, subheadings, callout box borders, and Project Facts table rows.

**Safety Callout Box** (mandatory design element):
```
┌─ SAFETY NOTE ──────────────────────────────────────┐
│ [Safety instruction in bold. Embedded at the exact  │
│  step where the hazard occurs, not in front matter.] │
└────────────────────────────────────────────────────┘
```
Color: Red-tinted border and header, white fill. Never placed in a generic location — always at the hazard step.

**Tip/Maker's Tip Callout Box** (Design Signature governs naming — Maker's Tip / Crafter's Note / From the Bench / Workshop Wisdom):
- Left accent bar in primary color, light fill background, 10pt italic text.

**Pattern Charts and Stitch Diagrams** (fiber-art sub-niches): Embedded as high-resolution images. Grid-style charts use primary accent color for filled cells. Symbol key immediately follows every chart.

**Step Images:** One realistic photographic image per step, placed immediately below the step text. If AI cannot generate: output a [STEP IMAGE PROMPT] block in the structure:
`[STEP IMAGE PROMPT - Step X: Subject and exact action | Hand and tool positions | Materials and their state | Setting and background | Camera angle and framing | Lighting | Style: photorealistic, high resolution | Aspect ratio: 4:3]`

**Hero Images (completed project):** Full-column or half-column width. Placed at the top of each Project Unit immediately after the META line. Photorealistic only — no vectors, clip art, or illustrations.

**Section Divider Pages:** Right-hand (recto) pages. Full primary accent color background or high-contrast design with section title (20pt, white, block caps, centered) and project preview thumbnails.

**Design Signature:** Composed from six dimensions per UAPF Module 4.6 (accent palette family, callout treatment, chapter opening ornament, title page composition, callout naming set, voice persona). Announced in configuration report. Logged to operator's Design Signature Register. No two books share an identical six-dimension signature.

---

## Content Rules

### The Fatal Flaw to Avoid

**Projects that cannot be completed as written.** Every project in an OV-CRAFT book must be technically executable by a reader at the declared difficulty level using the materials and tools listed in that project's Materials section, following only the steps provided. A project that requires undocumented techniques, unlisted tools, or pattern knowledge not explained in the book is a publication defect.

### Hard Constraints

1. **Project Count from Title Only.** The number of projects is always taken from the user's title. The framework never invents, inflates, or reduces the count. Every project counted in the title must appear in full as a complete Project Unit.

2. **Every Project Unit Must Be Self-Contained.** Materials, steps, and verification are all within the unit. Cross-references to other projects are allowed for variations only ("See Project 12 for the base square") but the current project must be completable without performing the referenced project first.

3. **Safety Callouts at Point of Hazard — Never Only in Preface.** If a step involves a sharp tool, hot surface, chemical exposure, electrical tool, or UV resin, the safety note appears inside that step's Safety Callout Box. General safety overviews in the Introduction are permitted but do not replace in-step callouts.

4. **No Registered Brand Names in Project Text.** Do not instruct the reader to use specific brand-name products (e.g., "apply Mod Podge" or "use a Cricut machine"). Use generic category terms ("decoupage medium," "electronic cutting machine"). Brand names in the supplier directory appendix are acceptable if clearly attributed and not written as endorsements.

5. **Difficulty/Time/Cost META Line on Every Project.** No project unit may be published without a complete META line. Time estimates must be realistic for the declared difficulty level. Cost estimates must reflect current general market pricing ranges (not brand-specific pricing).

6. **Metric and Imperial Measurements — Both Required.** All measurements appear in both metric (primary) and imperial (parenthetical), or imperial (primary) with metric (parenthetical) depending on target marketplace. US marketplace: imperial primary, metric secondary. UK/AU/EU marketplace: metric primary, imperial secondary.

7. **Pattern Notation Must Be Defined.** Any abbreviation used in stitch instructions (k2tog, sc, ch, dc, etc.) must be defined in the "How to Use This Book" front matter AND in the Technique Glossary appendix.

8. **No Cultural Appropriation Without Attribution.** Techniques rooted in specific cultural traditions (e.g., Hawaiian quilting, Native beadwork patterns, Japanese sashiko, Peruvian knitting traditions) must include a cultural context note within the project or section, acknowledging the tradition's origin. The Textile Arts & Cultural Preservation Specialist validates all such attributions.

9. **Anti-AI Language Strictly Enforced.** Prohibited phrases: "In today's rapidly evolving craft world...", "It's important to note...", "Here's what you need to know...", "Let's dive into...", "At the end of the day...", "Moving forward...", "In conclusion...", generic marketing superlatives. Required voice: Master Multi-Craft Educator's direct instructional register — specific, concrete, practitioner-native.

10. **One Action Per Step.** Steps are numbered and contain exactly one action verb instruction. Instructions requiring two actions are split into two steps. Tools and materials are listed before Step 1, not introduced mid-step.

---

## QA Checklist

### Gate 1 — Pre-Creation Foundation (Before TOC or Any Content)

- [ ] Trademark Clearance Report completed; verdict is CLEAR or operator-approved CAUTION
- [ ] All candidate subtitles passed trademark screen
- [ ] Sub-niche code assigned (CRAFT-FIBER, CRAFT-WOOD, etc.)
- [ ] Project count extracted from title and recorded
- [ ] Audience and difficulty range identified
- [ ] Auto-configuration announced (pathway, page band, visual density, font size, line spacing, Design Signature)
- [ ] Expert panel confirmed — correct specialists for sub-niche assigned
- [ ] Safety standard set identified for sub-niche (e.g., OSHA tool standards for CRAFT-WOOD; CPSC chemical standards for CRAFT-CANDLE-SOAP; ANSI blade safety for CRAFT-GLASS)
- [ ] Cultural sensitivity pre-check: any techniques requiring cultural attribution identified before writing begins
- [ ] Operator has confirmed Design Signature is not a repeat

### Gate 2 — Real-Time Content Development (Per Project Unit)

- [ ] Every Project Unit contains all required elements: Title, META line, Hero Image or prompt, Materials list with quantities, numbered steps with one action each, Expected result, Project Facts Table
- [ ] Safety Callout Box present at every hazard step (not only in the Introduction)
- [ ] Step images (or STEP IMAGE PROMPT blocks) present for every step
- [ ] No registered brand names appear in instructional text
- [ ] Measurements appear in both metric and imperial
- [ ] Pattern abbreviations used are defined in the front matter glossary
- [ ] Cultural techniques attributed correctly
- [ ] Anti-AI language protocol enforced — no prohibited phrases
- [ ] Step verb family consistent with assigned Voice Persona

### Gate 3 — Post-Creation Section Review (Per Section Completion)

- [ ] Section Divider page completed with section overview and project preview thumbnails
- [ ] All projects in the section are technically executable as written — Master Multi-Craft Coordinator sign-off
- [ ] Textile Arts Specialist has reviewed all fiber-art stitch notations in this section
- [ ] Construction & Home Systems Authority has reviewed all power-tool and chemical steps
- [ ] No project requires undocumented techniques
- [ ] Project Facts Table is accurate (gauge verified for fiber projects, tool sizes confirmed for woodworking, cure times confirmed for resins)
- [ ] Time estimates are realistic for the declared difficulty level
- [ ] Cost estimates reflect current general market ranges
- [ ] Hero images / prompts are photorealistic (no vectors, cartoons, or illustrations)
- [ ] Visual continuity maintained (same hands, tools, lighting, and setting across all steps of one project)
- [ ] Section word count and page estimate are within the page-band target

### Gate 4 — Final Certification Before KDP Upload

- [ ] All [N] projects from the title are present as complete Project Units
- [ ] Total project count in the book matches the count in the title exactly
- [ ] Front matter complete and in correct order: Title Page → Copyright Page → TOC → Preface → How to Use This Book → Introduction
- [ ] Preface is exactly one page; How to Use This Book is exactly one page
- [ ] Conclusion is 1.5 pages
- [ ] Appendix contains: Project Difficulty Index, Materials Master List, Stitch/Technique Glossary, Measurement Conversion Chart, Supplier Directory, Project Planner Template, Troubleshooting Quick Reference
- [ ] Visible page numbers start at Introduction (page 1); front matter is unnumbered
- [ ] Design Signature applied consistently across all chapters (same accent palette, callout treatment, chapter ornament)
- [ ] Two-color interior confirmed: primary and secondary accent colors applied correctly throughout
- [ ] Author name (First Name, Middle Initial. Surname) is consistent on Title Page, Copyright Page, and all metadata
- [ ] KDP category assignments confirmed correct (see KDP Positioning)
- [ ] All seven back-matter appendix elements present
- [ ] No prohibited AI-pattern language found in any chapter
- [ ] Safety information accuracy: 100% — all tool, chemical, and electrical safety callouts validated against CPSC/OSHA/ANSI standards for the sub-niche
- [ ] Cultural attributions validated by Textile Arts & Cultural Preservation Specialist

---

## KDP Positioning

### Amazon Category Tree

**Primary Category:**
Crafts, Hobbies & Home > [Sub-Niche Specific]

**Sub-Niche Category Mapping:**

| Sub-Niche Code | Primary Amazon Category | Secondary Amazon Category |
|---|---|---|
| CRAFT-FIBER (knitting) | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Knitting | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Yarn |
| CRAFT-FIBER (crochet) | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Crocheting | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts |
| CRAFT-FIBER (quilting) | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Quilting | Crafts, Hobbies & Home > Sewing |
| CRAFT-FIBER (sewing) | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Sewing | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts |
| CRAFT-FIBER (embroidery) | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts > Embroidery | Crafts, Hobbies & Home > Needlecrafts & Textile Crafts |
| CRAFT-WOOD | Crafts, Hobbies & Home > Crafts & Hobbies > Woodworking | Crafts, Hobbies & Home > Home Improvement & Design > Woodworking |
| CRAFT-GLASS | Crafts, Hobbies & Home > Crafts & Hobbies > Glass & Glasswork | Crafts, Hobbies & Home > Crafts & Hobbies |
| CRAFT-RESIN | Crafts, Hobbies & Home > Crafts & Hobbies > Mixed Media | Crafts, Hobbies & Home > Crafts & Hobbies |
| CRAFT-PAPER | Crafts, Hobbies & Home > Crafts & Hobbies > Scrapbooking & Paper Crafts | Crafts, Hobbies & Home > Crafts & Hobbies > Papermaking |
| CRAFT-CANDLE-SOAP | Crafts, Hobbies & Home > Crafts & Hobbies > Candle & Soap Making | Crafts, Hobbies & Home > Crafts & Hobbies |
| CRAFT-CERAMIC | Crafts, Hobbies & Home > Crafts & Hobbies > Pottery & Ceramics | Crafts, Hobbies & Home > Crafts & Hobbies |
| CRAFT-GENERAL | Crafts, Hobbies & Home > Crafts & Hobbies | Crafts, Hobbies & Home > Crafts & Hobbies > General Crafts |
| CRAFT-GARDEN | Crafts, Hobbies & Home > Crafts & Hobbies > Floral Arts & Crafts | Crafts, Hobbies & Home > Gardening & Landscape Design |
| CRAFT-JEWELRY | Crafts, Hobbies & Home > Crafts & Hobbies > Jewelry Making | Crafts, Hobbies & Home > Crafts & Hobbies |

### KDP Description Formula

The description **leads with the project count and the reader's outcome promise**. Structure:

1. **Hook sentence:** "[Project Count] [craft name] projects, every one completely explained — materials, steps, and a finished-project photo."
2. **Audience identification:** "Whether you are working your first [craft] or looking to build a confident technique library..."
3. **Differentiation:** What makes this book different from competing titles (unique project types, cultural variety, difficulty range, special techniques covered).
4. **Feature bullets** (5–7 bullets): Project count, difficulty range, dual measurements, cultural notes, safety guidance, back matter tools.
5. **Closing call to action:** "Open to any page and start today."

### Metadata Signals

- **Keywords (7 slots):** Project count + craft name (e.g., "50 crochet projects"), skill level + craft, craft + "for beginners", craft + "step by step", craft + "complete guide", craft + "patterns", craft + "ideas" or "inspiration."
- **Series potential:** Title as Book 1 of a series if project count allows ("Volume 1" or "Beginner Collection") — only if title does not specify "complete" or "ultimate."

---

## Key Rules — Do NOT Break

1. **The project count stated in the title is the contract with the reader.** Every single project must be present, complete, and executable. One missing project is a refund trigger.

2. **Safety callouts live inside the step where the hazard occurs.** A safety section in the Introduction does not satisfy the requirement. Hazard step = safety callout box, every time.

3. **No registered brand names in instructional text.** Use generic category names. Brand names in appendix supplier directories are the only exception.

4. **Project Units must be self-contained.** A reader must be able to start and complete any project in the book without completing any other project first.

5. **The Project Visual Template is mandatory and non-negotiable.** Every project has: Title, META line (Difficulty/Time/Cost), Hero image, Materials list, Numbered steps with step images, Expected result, Project Facts Table.

6. **Every step contains exactly one action.** No compound steps. Materials are listed before Step 1 and never introduced mid-step.

7. **Both metric and imperial measurements appear for every measurement.** Target marketplace determines which is primary. No exceptions for "obvious" dimensions.

8. **Pattern abbreviations must be defined in front matter AND the glossary appendix.** An undefined abbreviation in a fiber-art book is a fatal content defect.

9. **Cultural techniques require cultural context attribution.** Techniques originating in named cultural traditions must be acknowledged in the project or section note. This is both an ethical and a marketplace reputation requirement.

10. **The Design Signature must be logged before the TOC gate and must differ from the last five signatures in the register.** Consecutive books in the same category must differ on at least three of six signature dimensions and must not share a primary accent color.

11. **Visual continuity across step images is mandatory.** Same hands, same tools, same lighting, same workspace background across all steps of a single project. A continuity break is a post-production defect.

12. **The anti-AI language protocol is non-negotiable.** No prohibited phrases, no generic transitions, no enthusiastic preambles. Every sentence must read as practitioner-native instruction.

## HOUSE REFERENCE BANK — CRAFT AND HOW-TO BOOKS (2026-08-14)

Catalog masters are banked at `cover_db/_interiors/crafts/` (Crochet Farm
Animals) and `cover_db/_interiors/howto/` (DIY Home Repair for Women, Solar
Panel Installation Guide), local only, never shipped. BINDING for every
craft and how-to book on BOTH engines (Claude and Codex) and on every
install; where the bank folders are absent (client installs never receive
them), the codified standards below carry the full weight of the reference
study. CONSULT the masters where present: study a step-by-step page, a
technique-explanation page, and a panel page.

Standards verified across the bank:

* STEP ARCHITECTURE: procedures run as bold run-in step headings ("Step by
  Step: Painted-Shut Window", "Step 12: Compare actual to expected.")
  followed by numbered, substantive steps: each step carries the action,
  the method detail, and the cue or tolerance that tells the reader it
  went right. Never bare one-line commands.
* TROUBLESHOOTING PATTERN: diagnostic sequences as bold lead-in paragraphs
  ("Check for a failed or underperforming panel.") each followed by the
  reasoning and remedy; worked numeric examples with real figures where
  the subject is technical.
* TECHNIQUE-FIRST TEACHING (craft books): before a pattern or project, a
  technique section explains the METHOD and why it works; projects open
  with a construction overview: a bulleted parts list with bold lead-ins
  naming each piece, its construction, and its color.
* PANEL FAMILIES (at least two per book): bordered "Note:" safety boxes
  whose first sentence is bold and imperative; tinted "KEY CONCEPT:" or
  "KEY DIFFERENCE:" panels with colored ALL-CAPS lead-ins carrying the
  chapter's central principle.
* COLOR SYSTEM: accent-colored subheads and section heads in the book's
  two-color fingerprint (the crochet master runs green + orange); how-to
  books may run a more restrained system, but the premium color bar still
  applies (plain black-on-white is a production failure).
* STEP IMAGES: technique steps, builds, and finished projects get real
  images per the images-at-any-page-count law, placed at the step they
  teach, Figure C.N captioned.
* TRIM: the standing defaults govern (crafts and how-to are 8.5 x 11, with
  the binding heading law); the masters' patterns scale to the page, their
  trims are not copied.
* ONE ACCENT SYSTEM PER BOOK, NO REPEATS: no two craft or how-to books
  share the same palette, panel family, step treatment, or layout
  fingerprint (No-Two-Books-Alike, operator restated 2026-08-14).
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
