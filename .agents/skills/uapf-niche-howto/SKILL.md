---
name: uapf-niche-howto
description: Practical how-to and skill-instruction books — invoked by uapf-phase0-router when the title signals step-by-step instruction for a practical skill, "how to", "complete guide to", "step-by-step guide", or a beginner's guide to a hands-on topic that is not a product manual and does not resolve to a project-count-driven craft book.
---

# UAPF Niche: How-To & Practical Skill Guides (OV-HOWTO)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-How-To-Edition/` (config, validation, phases, and deterministic ops in `genie_howto.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 How-To Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title contains any of the following instructional signals — "how to", "how-to", "complete guide to", "step-by-step guide", "step by step", "beginner's guide to [practical skill]", "learn [skill] from scratch", "master [skill]", "the [skill] handbook", "teach yourself [skill]", "practical guide to", "everything you need to know about [skill]", or when the format is clearly instructional/procedural and the core promise is that the reader will acquire a defined practical skill by the end of the book.

**NOT routed here when:**
- The title contains a numeric project count that makes it project-unit-driven (route to OV-CRAFT).
- The title references a specific product, device, software version, or platform that the reader must operate (route to OV-GUIDE).
- The title is primarily a reference or encyclopedia of information without a skill-acquisition arc.

---

## Expert Panel

1. **Master Instructional Design & Skills Transfer Authority** (Domain Master) — 20+ years in instructional design, vocational training, and step-by-step curriculum development across multiple trades. Certified Professional in Talent Development (CPTD/ATD) and vocational teaching qualified. Governs task decomposition, learning objective sequencing, prerequisite calibration, and reader-success validation for every chapter. Must sign off on every numbered procedure before Gate 2 clears.

2. **Construction & Home Systems Authority** — 22+ years in construction and sustainable building (licensed contractor, LEED certified). Required for how-to titles in home repair, plumbing, electrical, carpentry, painting, tiling, HVAC maintenance, or any trade-skill topic. Validates all tool specifications, code-compliance notes, and OSHA-adjacent safety language.

3. **Master Multi-Craft Educator** — 25+ years across craft disciplines (guild memberships, instructor certifications). Required for how-to titles in craft skills (e.g., "How to Knit," "How to Make Candles," "Step-by-Step Woodcarving") where the skill is craft-based rather than trade-based. Validates technique accuracy and instructional scaffolding.

4. **Environmental Science & Sustainable Living Expert** — 15+ years environmental science and sustainable lifestyle implementation. Required for how-to titles covering chemical use, outdoor skills, gardening technique, sustainability practices, or any topic where material selection has environmental or health implications. Validates VOC disclosures, chemical handling, and sustainable alternative guidance.

5. **Safety & Compliance Reviewer** (role filled by the most appropriate panelist above based on sub-niche) — Responsible for confirming every procedure's safety callouts meet the applicable standard (OSHA, CPSC, ANSI, EPA) and that no step instructs a reader to bypass a safety measure. When the sub-niche does not require Construction Authority or Craft Educator, this role defaults to the Instructional Design Authority reviewing against adult learning safety principles.

**Panel Consensus Rule:** The Instructional Design Authority and the relevant domain expert must both confirm that every numbered procedure in the book is executable as written by a reader at the declared skill level before that chapter advances to Gate 3. Disagreements on step clarity escalate to a plain-language audit against a 6th-grade reading comprehension baseline for technical prose.

---

## Phase 0 — Title Analysis

Execute all steps in sequence before generating any content.

### Step 0-A: Trademark Clearance (MANDATORY FIRST ACTION)

Extract every distinctive word, phrase, technique name, method name, and brand-like term from the submitted title and all candidate subtitles. Generic terms (guide, beginner, step-by-step, complete, practical) are exempt.

**Watch categories for OV-HOWTO titles:**
- Named proprietary methods or techniques that may be registered (e.g., "The Marie Kondo Method," "GTD," specific trademarked curriculum names).
- Brand names of tools or platforms referenced in the title (e.g., "Excel How-To" — Microsoft is a registered mark; reframe as "Spreadsheet Formulas: A Complete How-To Guide").
- Any term that functions as a brand name in its field rather than a generic descriptor.

Registry coverage: USPTO (US) Class 16 + Class 9, EUIPO (EU), UKIPO (UK), CIPO (Canada), IP Australia, JPO (Japan) — matched to target marketplace.

**Verdicts:**
- CLEAR: Proceed to Step 0-B.
- CAUTION: Present 3-5 reworded alternatives; require operator approval.
- BLOCKED: Title must change. Present 3-5 alternatives with same keyword intent. Halt until resolved.

**Output:** Trademark Clearance Report (system layer, English).

### Step 0-B: Skill Domain Classification

Classify the title into a Skill Domain. The domain drives expert panel composition, applicable safety standards, and the type of decision points and failure-recovery boxes required.

| Domain Code | Triggers |
|---|---|
| HOWTO-TRADE | Home repair, plumbing, electrical, carpentry, painting, tiling, HVAC, roofing, flooring |
| HOWTO-CRAFT-SKILL | Knitting, crochet, sewing, woodworking, leatherworking, welding, pottery — skill-acquisition framing without project count |
| HOWTO-GARDEN | Vegetable gardening, landscape design, composting, permaculture, pruning, propagation |
| HOWTO-COOK-BAKE | Cooking technique, baking science, fermentation, preservation — skill not recipe collection |
| HOWTO-DIGITAL | Computer skills, software skills (generic), social media, photography technique, video editing |
| HOWTO-BUSINESS | Small business start-up, freelancing, self-publishing, side hustles, financial planning basics |
| HOWTO-WELLNESS | Fitness technique, yoga instruction, meditation practice, stretching, nutrition basics |
| HOWTO-CREATIVE | Writing, drawing, painting, music, photography as skill instruction |
| HOWTO-OUTDOOR | Camping, hiking, navigation, survival skills, fishing, hunting |
| HOWTO-GENERAL | Practical skill guides that do not fit the above — apply general instructional design standards |

### Step 0-C: Declared Audience & Prerequisite Map

Identify:
- **Declared skill level:** Complete beginner (no prior knowledge assumed) / Intermediate (some exposure assumed) / All-levels / Unspecified.
- **Prerequisite knowledge floor:** What the reader must already know to begin. State this explicitly — it becomes the "Who This Book Is For" section in the Introduction.
- **Outcome promise:** What the reader will be able to do after completing the book. The outcome promise must be specific and measurable (e.g., "complete a 12-week vegetable garden from seed to harvest" not "grow your own food").
- **Age/audience signal:** Adult (default) / Senior (13pt font, 1.5 spacing) / Young adult / Professional.

### Step 0-D: Quick-Win Chapter Identification

**The OV-HOWTO structural mandate:** The reader must experience a tangible skill win — a result they can show, use, or demonstrate — by the end of Chapter 3 (or by 20% of the book's total chapters, whichever comes first).

From the title and outcome promise, identify the "Quick-Win Deliverable" — the smallest complete sub-skill or practical result the reader can produce early in the book. Record this in the configuration report. The Table of Contents must be structured so Chapter 3 ends with the reader having achieved this deliverable.

Examples:
- "How to Knit" → Quick-Win by Chapter 3: A completed 4-inch tension swatch using the knit stitch.
- "How to Start a Vegetable Garden" → Quick-Win by Chapter 3: Seeds planted in prepared containers or beds, with a care schedule in hand.
- "How to Wire a Light Switch" → Quick-Win by Chapter 3: A single-pole switch replaced safely and tested, with the breaker panel documented.

### Step 0-E: Competitor Analysis & Market Intelligence

Execute web search:
- "[TITLE]" + "Amazon book" + [marketplace]
- [Key skill term from title] + "beginner's guide" + "Amazon"
- [Key skill term] + "how to book" + "step by step"

**Report:** Top 5 competing titles (title, author, price, star rating, review count, key differentiators). Market gap analysis. Reader complaint patterns from 1- and 2-star reviews (these reveal what OV-HOWTO content must fix in this book).

### Step 0-F: Subtitle Generation

Generate 7 subtitle candidates. Every candidate must pass the Step 0-A trademark screen.

1. [Outcome Statement]: A Step-by-Step Guide to [Skill] for [Audience]
2. [Audience] Guide to [Skill]: [Outcome Promise] in [Time Frame or N Steps]
3. The Complete [Skill] Handbook: From [Starting Point] to [End Capability]
4. [Skill] Made Simple: [N]-Step Instructions Anyone Can Follow
5. Master [Skill] from Scratch: A Practical, [Audience]-Friendly Step-by-Step System
6. [Skill] for [Audience]: Proven [N]-Step Methods with Troubleshooting, Tips & Real-World Practice
7. Step-by-Step [Skill]: Everything a [Audience] Needs — Instructions, Diagrams & Failure-Recovery Guides

Recommend the best subtitle with strategic justification and KDP keyword capture analysis.

### Step 0-G: Auto-Configuration

Auto-select and announce all parameters. Do not ask the user to choose.

| Parameter | Selection Logic |
|---|---|
| Content Pathway | Hybrid (web research + knowledge base) for all OV-HOWTO titles unless operator uploads reference materials |
| Page Band | 80–150 pp (compact, 8–12 chapters); 180–250 pp (standard, 13–20 chapters); 280–350 pp (extended, 21–30 chapters) |
| Visual Density | Moderate Visual (40–70 images) for text-dominant skill guides; Heavy Visual (80–150+ images) for trade, craft-skill, and outdoor titles where physical demonstration is critical |
| Body Font Size | 11pt (standard); 13pt (seniors or large-print signal) |
| Line Spacing | 1.15 (standard); 1.5 (senior/large-print/workbook signal) |
| Quick-Win Chapter | Chapter 3 (or adjusted per Step 0-D analysis — announce which chapter delivers the Quick Win) |
| Design Signature | Composed from six dimensions per UAPF Module 4.6; announced in configuration; operator logs to register |

**Configuration Gate:** Present configuration summary and Quick-Win chapter identification, ending with: "Shall I proceed with the Table of Contents? Type Proceed to continue."

---

## Book Architecture

### Structural Principle: Outcome-Ordered Chapters

**OV-HOWTO books are organized by the reader's skill-acquisition arc, not by topic completeness.** Chapters are sequenced so each one builds capability that the next chapter requires. No chapter introduces a concept whose prerequisite has not been covered in a prior chapter.

**The Three-Zone Structure:**

| Zone | Chapters | Purpose |
|---|---|---|
| Zone 1: Foundation & Quick Win | Ch. 1–3 (approx. 20% of content) | Minimum viable knowledge + the Quick-Win Deliverable |
| Zone 2: Core Skill Expansion | Ch. 4–[penultimate] (approx. 65% of content) | Systematic skill building, increasing complexity, real-world application |
| Zone 3: Mastery & Continuation | Final 1–2 chapters (approx. 15% of content) | Advanced techniques, troubleshooting, where to go from here |

### Chapter Formula

Each chapter follows this internal architecture:

```
CHAPTER [NUMBER]: [CHAPTER TITLE IN BLOCK CAPS]
[Chapter Learning Objective — one sentence stating what the reader will be able to do by chapter end]
[Chapter overview paragraph — 100–150 words, no AI-pattern openers]

[SUBCHAPTER 1: Context or Concept]
[Body text — explains the why and what before the how]

[SUBCHAPTER 2: Preparation]
[Tools, materials, workspace requirements before first procedure]
[SAFETY NOTE callout if any hazardous tool or material is introduced here]

[PROCEDURE BLOCK]
[Titled procedure with numbered steps — see Procedure Architecture below]

[DECISION POINT BOX — where applicable]
[FAILURE-RECOVERY BOX — where applicable]

[SUBCHAPTER N: Practice Exercise]
[A short, completable exercise that verifies the reader has acquired the chapter skill]

[CHAPTER CHECKPOINT]
[3–5 bullet points summarizing what the reader now knows and can do]
[Link to next chapter — one sentence stating what the next chapter builds on this]
```

### Procedure Architecture (The Core Instructional Unit)

Every technique, task, or process is delivered as a **numbered procedure**. No exceptions.

```
[PROCEDURE TITLE]
─────────────────────────────────────────────
Skill Level: [Beginner / Intermediate / Advanced]
Time Required: [X minutes / hours]
Tools & Materials (before Step 1):
  • [Item 1 with specification]
  • [Item 2 ...]
  [SAFETY NOTE callout if any hazardous item is listed]
─────────────────────────────────────────────
Step 1. [Action verb] [exact instruction] [precision detail — measurement, setting, duration].
        [Step image or STEP IMAGE PROMPT]
        [SAFETY CALLOUT if hazard occurs here]

Step 2. [Action verb] [exact instruction].
        [Step image or STEP IMAGE PROMPT]

[...continue through final step]

Expected Result: [Concrete description of correct outcome — what the reader should see, feel, or measure].

If your result does not match: [Immediate failure-recovery guidance — first most-likely cause and correction.]
```

**One action per step. One verb per step.** If a step requires two sequential actions, it is two steps.

### Decision Point Boxes

A **Decision Point Box** appears wherever the correct next action depends on a variable condition the reader must assess. Format:

```
┌─ DECISION POINT ───────────────────────────────────────────────┐
│ IF [condition A is true]  →  Go to Step [X]                    │
│ IF [condition B is true]  →  Go to Step [Y]                    │
│ IF [condition C is true]  →  See: Failure-Recovery — [Name]    │
└────────────────────────────────────────────────────────────────┘
```

Decision Point Boxes are mandatory at every fork in a procedure where the wrong path damages materials, wastes significant time, or creates a safety hazard.

### Failure-Recovery Boxes

A **Failure-Recovery Box** appears:
- After every procedure, as a consolidated "If it went wrong" reference.
- Inside a procedure step at the exact point where a mistake is most commonly made.

Format:

```
┌─ FAILURE RECOVERY: [TITLE] ────────────────────────────────────┐
│ SYMPTOM: [What the reader observes]                             │
│ MOST LIKELY CAUSE: [Root cause]                                 │
│ CORRECTION: [Numbered steps to fix it]                          │
│ PREVENTION: [What to do differently next time]                  │
└────────────────────────────────────────────────────────────────┘
```

Failure-Recovery Boxes are derived from real practitioner failure experience — not invented. They must be validated by the domain expert on the panel (Construction Authority for trades; Craft Educator for craft skills).

### Page-Band Targets

| Book Size | Chapter Count | Target Page Count | Quick-Win Chapter |
|---|---|---|---|
| Compact | 8–12 chapters | 80–150 pages | Ch. 3 |
| Standard | 13–20 chapters | 180–250 pages | Ch. 3 |
| Extended | 21–30 chapters | 280–350 pages | Ch. 3 (or Ch. 4 with operator approval) |

### Front Matter (Mandatory Order)

1. **Title Page** — Title, author name (First Name, Middle Initial. Surname), imprint line.
2. **Copyright Page** — Copyright line + year + author; all-rights-reserved; reproduction prohibition; disclaimer (skill instruction, individual results vary, professional consultation recommended for licensed-trade topics); liability notice; trademark acknowledgment; edition statement; imprint.
3. **Table of Contents** — Live Word field. Lists all chapters and major subchapters with page numbers.
4. **Preface** — Exactly one page. Why this skill matters and what this book does differently. Voice Persona register.
5. **How to Use This Book** — Exactly one page. Explains the Procedure Architecture (step format, Decision Point Boxes, Failure-Recovery Boxes, safety callout types), how to use the Chapter Checkpoints, and the Quick-Win milestone in Chapter 3.
6. **Introduction** — Page 1 (visible pagination starts here). Covers: who this book is for (prerequisites stated explicitly), what the reader will be able to do after completing it, a list of tools and materials the reader needs before starting, workspace and safety setup for the skill domain, and an honest overview of the learning curve.

**Disclaimer Standard for Licensed-Trade Topics (HOWTO-TRADE):** The disclaimer must state that electrical, plumbing, gas, and structural work may require permits and licensed contractors in the reader's jurisdiction. This disclaimer must appear on the Copyright Page AND at the opening of every relevant chapter.

### Back Matter (Mandatory)

- **Conclusion** — 1.5 pages. Reader has achieved [outcome from Step 0-D]. Next skill milestones. Community and continuing education resources.
- **Appendix** — Must include: Skill Progression Checklist (self-assessment tool the reader uses chapter by chapter); Tools & Materials Master List (consolidated reference); Troubleshooting Quick Reference (symptom → cause → solution matrix for all common failures in the book); Safety Reference Card (all safety rules for the skill domain in one scannable list); Glossary of Terms (all technical vocabulary used in the book defined in plain language); Resource Directory (professional associations, further reading, online communities — generic, not brand-specific endorsements); Measurement & Conversion Charts (where applicable).

---

## Interior Design

**Trim Size:** 8.5 × 11 inches. All margins: 0.7 inches. Gutter increase only for books above 500 pages.

**Font:** Times New Roman throughout.

**Body Text:** 11pt (standard); 13pt (seniors/large-print signal). Justified.

**Line Spacing:** 1.15 (standard); 1.5 (senior/large-print/workbook).

**Chapter Headings:** 16pt, BLOCK CAPITAL LETTERS, center aligned, primary accent color.

**Subchapter Headings:** Title Case, left aligned, bold, secondary accent color.

**Procedure Title Line:** 13pt, Title Case, bold, left aligned, primary accent color. Separated from body by a rule in secondary accent color.

**Step Numbers:** Bold. Steps left aligned. One action per step enforced at typesetting stage.

**Safety Callout Box:**
```
┌─ SAFETY ────────────────────────────────────────────┐
│ [Safety instruction in bold. At the exact hazard    │
│  step — never in front matter alone.]               │
└────────────────────────────────────────────────────┘
```
Red-tinted border and header. White fill.

**Decision Point Box:** Primary accent color border, light-fill background, tabular if/then layout.

**Failure-Recovery Box:** Secondary accent color border, Symptom / Cause / Correction / Prevention structured layout. Italic symptom text, bold correction steps.

**Tip Box** (name governed by Design Signature — Pro Tip / Field Note / Trade Wisdom / Instructor's Note): Left accent bar in primary color, light-fill, 10pt italic.

**Chapter Checkpoint Box** (end of every chapter): Bulleted summary of reader capabilities now acquired. Secondary accent color fill, checkmark prefix.

**Step Images:** One realistic photograph per step, immediately below the step text. No vectors, clip art, cartoons, or illustrations. If not image-capable: [STEP IMAGE PROMPT] block in standard format.

**Visual Continuity:** Consistent hands, tools, materials, lighting, workspace background across all steps of one procedure.

**Design Signature:** Six dimensions (palette family, callout treatment, chapter opening ornament, title page composition, callout naming set, voice persona). Announced in configuration. Logged to register. No repeat.

---

## Content Rules

### The Fatal Flaw to Avoid

**Procedures that cannot be executed as written by the declared reader.** If a step requires knowledge not taught earlier in the book, a tool not listed in the Materials block, or a judgment call not guided by a Decision Point Box, the procedure is broken. A broken procedure in a how-to book is a publication defect that triggers 1-star reviews. Every procedure is validated by attempting to trace a complete mental execution path as a first-time practitioner at the declared skill level.

### Hard Constraints

1. **Quick-Win by Chapter 3 is non-negotiable.** The reader must produce a tangible, demonstrable result of the skill by the end of Chapter 3. If the subject matter requires more groundwork, restructure so the simplest executable sub-task arrives by Chapter 3, even if the full skill arc extends to Chapter 15.

2. **Procedures are executable as written.** No step may assume knowledge not taught in a prior chapter. No step may list a tool not in the Pre-Step Materials block. No step may require a judgment that is not guided by a Decision Point Box.

3. **Decision Point Boxes are mandatory at every procedural fork.** A fork is any point where two or more different next actions are possible depending on a condition. Guiding the reader through forks is the primary value of a how-to book.

4. **Failure-Recovery Boxes are mandatory after every procedure.** They are not optional "bonus content." They represent the practitioner's diagnostic knowledge and are the key differentiator between a how-to book and a blog post.

5. **Safety callouts at point of hazard, not only in the Introduction.** The Introduction may contain a general safety overview. Every hazardous step must also carry its own Safety Callout Box.

6. **Licensed-trade disclaimer in the Copyright Page AND in relevant chapters.** Electrical, gas, plumbing, and structural topics require jurisdiction-specific licensing warnings at both locations.

7. **No step may skip a measurement.** Any instruction involving dimension, temperature, pressure, voltage, weight, or time must include the specific value. "Apply enough adhesive" is not an acceptable instruction. "Apply a 3 mm bead of adhesive along the full length of the joint" is.

8. **Outcome promise must be specific and achievable.** The outcome stated in the subtitle and Introduction must be achievable by a reader who follows every instruction in the book. Overpromising ("master carpentry in 30 days") when the book's scope cannot deliver that outcome is a liability and a review risk.

9. **Chapter Checkpoints are mandatory at the end of every chapter.** No chapter ends without a 3–5-bullet summary of what the reader has now acquired.

10. **Anti-AI language strictly enforced.** Prohibited: "In today's world," "It's important to note," "Let's dive in," "Here's what you need to know," "Moving forward," "In conclusion," "The bottom line," superlatives without evidence. Required: Practitioner-native direct instruction, specific measurements, honest failure acknowledgment, concrete examples from the skill domain.

11. **No undefined technical terms.** Every technical term used in the book must be defined at first use in the body text AND in the Glossary appendix.

12. **Both metric and imperial measurements.** Target marketplace determines which is primary (US: imperial primary; UK/AU/EU: metric primary). No exceptions.

---

## QA Checklist

### Gate 1 — Pre-Creation Foundation

- [ ] Trademark Clearance Report completed; verdict CLEAR or operator-approved CAUTION
- [ ] All subtitle candidates passed trademark screen
- [ ] Skill Domain code assigned
- [ ] Audience and prerequisite floor documented
- [ ] Outcome promise identified and is specific + achievable
- [ ] Quick-Win Deliverable identified and confirmed achievable by Chapter 3
- [ ] Competitor analysis complete; market gaps identified
- [ ] Auto-configuration announced (pathway, page band, visual density, font, spacing, Design Signature)
- [ ] Expert panel confirmed for domain (Construction Authority for HOWTO-TRADE, etc.)
- [ ] Applicable safety standards identified (OSHA, CPSC, ANSI, NEC, EPA) for the domain
- [ ] Licensed-trade disclaimer requirement confirmed (yes/no) and drafted if required

### Gate 2 — Real-Time Content Development (Per Chapter)

- [ ] Chapter Learning Objective stated at chapter open (one sentence, measurable)
- [ ] Every procedure has a Pre-Step Materials block listing all tools and quantities before Step 1
- [ ] Every step contains exactly one action verb and one instruction
- [ ] Decision Point Boxes present at every procedural fork
- [ ] Failure-Recovery Boxes present after every complete procedure
- [ ] Safety Callout Boxes present at every hazard step (not only in Introduction)
- [ ] Step images / STEP IMAGE PROMPT blocks present for every step
- [ ] No undefined technical terms introduced without definition
- [ ] Measurements are specific (no "enough," "adequate," or "as needed")
- [ ] Both metric and imperial measurements present for every measurement
- [ ] Anti-AI language protocol enforced — no prohibited phrases
- [ ] Chapter ends with Chapter Checkpoint (3–5 bullets)

### Gate 3 — Post-Chapter Review (Instructional Design Audit)

- [ ] Instructional Design Authority confirms every procedure is executable by a reader at the declared skill level
- [ ] Domain expert (Construction Authority / Craft Educator / other) confirms technique accuracy
- [ ] Mental execution trace completed: a first-time reader at the declared level can follow every step without external knowledge
- [ ] Quick-Win Chapter (Chapter 3 or designated chapter) delivers a tangible, demonstrable reader result — confirmed
- [ ] All Decision Point Boxes cover all realistic conditions; no uncovered fork left open
- [ ] Failure-Recovery Boxes derived from real practitioner failure patterns — confirmed by domain expert
- [ ] Safety callouts validated against applicable OSHA/CPSC/ANSI standard — no callout is missing, no callout is incorrect
- [ ] Licensed-trade disclaimer present in chapter if required
- [ ] Chapter word count and page estimate within page-band targets

### Gate 4 — Final Certification Before KDP Upload

- [ ] Zone 1 (Foundation & Quick Win): outcome promise introduced, prerequisites stated, Quick Win delivered by Chapter 3
- [ ] Zone 2 (Core Skill Expansion): chapters sequence without prerequisite gaps — each chapter's skills are fully supported by prior chapters
- [ ] Zone 3 (Mastery & Continuation): advanced techniques, troubleshooting synthesis, next-steps guidance present
- [ ] Front matter complete: Title Page → Copyright Page → TOC → Preface → How to Use This Book → Introduction
- [ ] Preface exactly one page; How to Use This Book exactly one page; Conclusion exactly 1.5 pages
- [ ] Licensed-trade disclaimer on Copyright Page (if required)
- [ ] All seven Appendix elements present: Skill Progression Checklist, Tools & Materials Master List, Troubleshooting Quick Reference, Safety Reference Card, Glossary, Resource Directory, Measurement & Conversion Charts
- [ ] Visible page numbers start at Introduction (page 1); front matter unnumbered
- [ ] Design Signature consistent across all chapters
- [ ] Author name consistent (Title Page, Copyright Page, all metadata)
- [ ] KDP categories confirmed correct
- [ ] No prohibited AI-pattern language found in any chapter
- [ ] Safety accuracy: 100% — all callouts validated against applicable professional standards
- [ ] All technical terms defined in body text at first use and in Glossary appendix

---

## KDP Positioning

### Amazon Category Tree

**Primary Category:**
Books > [Domain-specific] — How-To category placement depends on the skill domain.

| Domain Code | Primary Amazon Category | Secondary Category |
|---|---|---|
| HOWTO-TRADE | Books > Home & Garden > Home Improvement & Design | Books > Reference > Handbooks & Manuals |
| HOWTO-CRAFT-SKILL | Crafts, Hobbies & Home > [relevant sub-category] | Books > Reference > Handbooks & Manuals |
| HOWTO-GARDEN | Crafts, Hobbies & Home > Gardening & Landscape Design | Books > Science & Nature > Nature & Ecology |
| HOWTO-COOK-BAKE | Books > Cookbooks, Food & Wine > Cooking by Ingredient | Books > Cookbooks, Food & Wine > Baking |
| HOWTO-DIGITAL | Books > Computers & Technology > [relevant sub] | Books > Business & Money > Skills |
| HOWTO-BUSINESS | Books > Business & Money > Small Business & Entrepreneurship | Books > Reference > Handbooks & Manuals |
| HOWTO-WELLNESS | Books > Health, Fitness & Dieting > Exercise & Fitness | Books > Self-Help > Personal Transformation |
| HOWTO-CREATIVE | Books > Arts & Photography > [relevant sub] | Books > Reference > Handbooks & Manuals |
| HOWTO-OUTDOOR | Books > Sports & Outdoors > Outdoor Recreation | Books > Reference > Survival & Emergency Preparedness |
| HOWTO-GENERAL | Books > Reference > Handbooks & Manuals | Books > Education & Reference |

### KDP Description Formula

The description **leads with the outcome promise and the reader's ability gap it solves.**

1. **Hook:** State the specific thing the reader will be able to do after completing this book — concrete, not vague.
2. **Audience identification:** Who this book is specifically for (skill level, background, what they've tried before that hasn't worked).
3. **Structural differentiator:** Quick-win by Chapter 3; Decision Point Boxes at every fork; Failure-Recovery after every procedure — name these features.
4. **Feature bullets** (5–7 bullets): Step-by-step procedures for [N] techniques, Decision Point Boxes for [N] situations, Failure-Recovery guidance for [N] common problems, safety callouts embedded at the hazard step, both metric and imperial measurements, Skill Progression Checklist, Troubleshooting Quick Reference.
5. **Anti-generic close:** A specific, concrete statement of what the reader will have achieved — not "start your journey" or "take the first step."

### Metadata Signals

- **Keywords (7 slots):** "how to [skill]", "[skill] for beginners", "[skill] step by step", "complete guide to [skill]", "[skill] book", "[skill] techniques", "[skill] guide [audience]."
- **Series framing:** If the title scope is beginner-only and the skill has an intermediate and advanced tier, flag series potential at configuration for operator decision.

---

## Key Rules — Do NOT Break

1. **A tangible skill win must be achievable by the end of Chapter 3.** No structural exception. If the subject genuinely requires more groundwork, find the earliest demonstrable sub-skill and make it Chapter 3's outcome.

2. **Every procedure is executable as written by the declared reader.** No external knowledge, no unlisted tools, no uncovered decision points. This is the core quality contract of a how-to book.

3. **Decision Point Boxes are mandatory at every procedural fork.** "Use your judgment" is not an acceptable instruction in a how-to book for beginners or intermediates.

4. **Failure-Recovery Boxes are mandatory after every procedure.** Not in the appendix only — in the chapter, after the procedure, and inside steps at high-failure points.

5. **Safety callouts live inside the step where the hazard occurs.** A general safety section in the Introduction does not satisfy this requirement.

6. **Licensed-trade topics carry a jurisdiction disclaimer on the Copyright Page AND in every applicable chapter.**

7. **Every measurement is specific.** No "adequate amount," "as needed," "a little," or "enough." Every measurement appears in both metric and imperial.

8. **Every technical term is defined at first use in the body text and in the Glossary appendix.**

9. **The outcome promise must be achievable by following the book.** The subtitle's promise is a contractual statement to the reader. Overpromising is a review liability.

10. **Chapter Checkpoints are mandatory at the end of every chapter.** 3–5 bullets. No exceptions.

11. **The anti-AI language protocol is non-negotiable.** Practitioner-native instruction voice throughout. No prohibited phrases. No generic transitions. No enthusiasm without evidence.

12. **The Design Signature must be logged before the TOC gate and must not repeat any of the last five entries in the register.** Consecutive books in the same domain must differ on at least three of six dimensions and must not share a primary accent color.

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
