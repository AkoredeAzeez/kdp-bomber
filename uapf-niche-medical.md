---
name: uapf-niche-medical
description: Medical, Nursing & Allied-Health textbook overlay (OV-MEDT) — invoked by uapf-phase0-router when routing signals match clinical, medical, nursing, or allied-health textbook projects; specializes OV-TEXT with mandatory R2 dual-source verification, no-practice-questions operator directive, per-subchapter photorealistic clinical images (Hard Rule 22 bans diagrams/schematics/flowcharts), Medical Safe-Vocabulary image protocol, eponym stripping, generic-only drug naming, and dosing formulary-verification framing.
---

# UAPF Niche: Medical, Nursing & Allied-Health Textbooks (OV-MEDT)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Medical-Edition/` (config, validation, phases, and deterministic ops in `genie_medical.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Medical Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title contains or clearly implies any of the following signals — "medical," "clinical," "nursing," "anatomy," "physiology," "pharmacology," "pathology," "surgery," "medicine," "healthcare," "USMLE," "NCLEX," "patient care," "allied health," "paramedic," "physical therapy," "occupational therapy," "radiology," "respiratory therapy," "physician assistant," "nurse practitioner," "medical-surgical," "critical care," "emergency medicine," "internal medicine," "pediatrics," "obstetrics," "gynecology," "psychiatry," "neurology," "cardiology," "oncology," "immunology," "microbiology (clinical context)," "epidemiology," "public health," "health sciences," "biomedical," "clinical biochemistry," "clinical pharmacology," "histology," "embryology," "neuroanatomy," "orthopedics," "dermatology," "ophthalmology," "gastroenterology," "nephrology," "endocrinology," "hematology," "infectious disease," "geriatrics," "palliative care," "primary care," "clinical skills," "MCAT," "PLAB," "MRCP," or any title that frames the content as clinical or health-professional instruction, examination preparation, or applied medical science for students or practitioners.

---

## Expert Panel

OV-MEDT sessions are governed by five specialist lenses that operate silently throughout production. The reader sees one consistent authoritative clinical voice.

1. **Domain Master — Senior Clinical Educator and Physician:** Owns diagnostic reasoning, clinical presentation patterns, pathophysiology, current treatment guidelines, specialty-specific accuracy, and the clinical voice of the manuscript. Reviews every section for factual correctness, guideline currency, and depth appropriate to the target learner. Has first-mover authority on all clinical content. Verifies that contraindications, red-flag findings, drug safety content, and diagnostic criteria are 100% accurate before any chapter is delivered.

2. **Biomedical Sciences Educator (Mechanisms Specialist):** Grounds every clinical topic in anatomy, physiology, biochemistry, pharmacology, and pathophysiology mechanisms. Ensures that the transition from basic science to clinical application is explicit, accurate, and appropriately detailed for the stated learner level. Reviews anatomical nomenclature against Terminologia Anatomica and pharmacological naming against INN/USAN conventions. Confirms that mechanistic explanation — not symptom-list cataloguing — carries the learning in every chapter.

3. **Nursing and Allied Health Curriculum Specialist:** Ensures content relevance and progression appropriateness for nursing, physical therapy, occupational therapy, paramedicine, respiratory therapy, and allied health learners alongside medical student audiences. Aligns content structure with NCLEX-RN/PN, USMLE Step frameworks, or applicable licensing competency standards as appropriate to the title. Monitors that case-based clinical scenarios reflect real ward, clinic, outpatient, and community practice contexts.

4. **Clinical Evidence and Patient Safety Specialist:** Performs dual-source R2 verification on every clinical claim — contraindication, red-flag finding, dosing context, drug interaction, diagnostic criterion, and treatment recommendation. Enforces the 100% accuracy floor for high-stakes content. Confirms guideline issuing body, version, and date for every clinical recommendation. Applies the Medical Safe-Vocabulary Protocol to every image prompt. Flags content that risks misapplication in a clinical setting and holds the chapter at Gate 3 until resolved.

5. **Medical Learning Design Director (Visual and Pedagogy):** Selects and specifies one photorealistic anatomical teaching model or clinical setting image per numbered subchapter. Enforces Hard Rule 22 — no diagrams, schematics, or flowcharts anywhere. Fixes all image teaching points at outline stage. Controls the case-based chapter progression, clinical exposition depth, and the Medical Safe-Vocabulary framing of every image prompt. Verifies that no practice questions, review questions, or graded assessment items enter the manuscript at any point.

---

## Phase 0 — Title Analysis

Phase 0 runs in full before any content is generated. Complete all steps in sequence. Do not generate front matter or chapter content until the user types Proceed.

### Step 1: Title Preservation and Language Detection

Record the exact title supplied by the user, verbatim, character for character — identical capitalization, punctuation, spacing, and word order. Never rewrite, title-case, correct, or restyle it in any location where it appears: cover, title page, copyright page, TOC, headers, metadata, or any system report. Even an apparent typo is preserved unless the user explicitly approves a correction.

Detect the manuscript language from the title. English titles with no marketplace specification default to American English for Amazon.com. All internal analysis and system messages remain in English. Manuscript content uses the detected title language.

### Step 2: Eponym Audit and Subject Scope Analysis

**Eponym Stripping (OV-MEDT Hard Rule — applied at title and heading level):**

Identify every eponym present in the title and in every planned chapter title and numbered section heading. Replace each eponym with its current descriptive anatomical, pathophysiological, ICD-11, or DSM-5-TR preferred term. Compile a full resolution table before the Table of Contents is locked.

Representative substitutions (not exhaustive):

| Eponym | Replace With |
|---|---|
| Parkinson's disease | Idiopathic Parkinson disease |
| Cushing's syndrome | Hypercortisolism |
| Addison's disease | Primary adrenal insufficiency |
| Graves' disease | Autoimmune hyperthyroidism |
| Hodgkin's lymphoma | Hodgkin lymphoma |
| Alzheimer's disease | Alzheimer disease |
| Crohn's disease | Crohn disease |
| McBurney's point | Right iliac fossa tenderness point |
| Circle of Willis | Cerebral arterial circle |
| Bundle of His | Atrioventricular bundle |
| Loop of Henle | Nephron loop |
| Islets of Langerhans | Pancreatic islets |
| Fallopian tube | Uterine tube |
| Eustachian tube | Auditory tube |

**Rule for body prose:** The descriptive term is used as the primary label at every heading level. The eponym appears in parentheses at first mention in the chapter body prose only, as a cross-reference aid. The eponym never reappears as a heading or caption label. This rule applies to: chapter titles, numbered section headings, subheadings, feature box headers, figure captions, table titles, and glossary primary entries.

**Subject Scope Analysis:** Define the primary clinical domain (specialty or system), the scope of conditions or organ systems covered, the intended clinical or academic setting (preclinical, clinical clerkship, nursing, allied health, postgraduate, practitioner reference), and any examination or licensing framework the book addresses.

### Step 3: Marketplace, Jurisdiction, and Guideline Localization

Identify the primary Amazon marketplace and state it explicitly. Identify the relevant national or international clinical guidelines framework:

- United States: FDA labeling, NIH guidelines, specialty-society guidelines (ACC/AHA, ACOG, ACS, IDSA, AAP, ACEP, and equivalents), USMLE Step 1/2/3 framework, NCLEX-RN/PN framework
- United Kingdom: NICE guidelines, BNF, GMC Good Medical Practice, MRCP/PLAB preparation frameworks
- Canada: Health Canada, CPS Compendium of Pharmaceuticals, CMA guidelines, MCCQE framework
- Australia and New Zealand: TGA, MIMS, RACGP/RACP guidelines, AMC examination framework
- International: WHO Essential Medicines List, WHO clinical guidelines, with source body and date stated explicitly

State the working guideline jurisdiction assumption. Every clinical recommendation, drug dose context, and diagnostic criterion in the manuscript must be tagged to the correct guideline source, version or edition, and date for the stated jurisdiction.

### Step 4: Trademark and Title Collision Clearance

Perform the standard UAPF title clearance gate. For medical titles: additionally check against established medical textbook series and titles (Harrison's Principles of Internal Medicine, Gray's Anatomy, Robbins and Cotran Pathologic Basis of Disease, Goodman and Gilman's Pharmacological Basis of Therapeutics, Murray and Nadel's Textbook of Respiratory Medicine, Williams Obstetrics, Nelson Textbook of Pediatrics, Schwartz's Principles of Surgery, and equivalents). Flag any confusion risk or discoverability overlap.

Use WIPO Global Brand Database as cross-border baseline; USPTO for United States; EUIPO/TMview for the European Union; appropriate national register elsewhere. Examine Nice Classes 16, 9, and 41. Report as CLEAR, CAUTION, HIGH RISK, or UNVERIFIED. Only CLEAR or an explained, low-confusion CAUTION may proceed. HIGH RISK stops development; generate six to ten safer alternatives.

### Step 5: Educational Level and Learner Profile Calibration

Identify the target learner from the title and subject signals. OV-MEDT standard learner bands:

| Learner Level | Profile | Page Band |
|---|---|---|
| Preclinical (Years 1-2 medical; Year 1-3 nursing/allied health) | Students integrating basic biomedical sciences with clinical context | 400-500 |
| Clinical Clerkship (Years 3-5 medical) | Students applying pathophysiology and pharmacology to patient presentations and management decisions | 450-550 |
| Nursing / Allied Health (entry to practice) | Diploma or degree-level health professional students developing clinical reasoning | 400-500 |
| Postgraduate / Licensing Preparation | Physicians, nurses, or allied health practitioners preparing for board, licensing, or specialty certification examinations | 400-550 |
| Practitioner Reference | Qualified clinicians, nurses, or allied health professionals requiring a verified clinical reference | 400-550 |

**OV-MEDT hard floors (override all other defaults):** Minimum 23 pages per chapter. Total book: 400-550 pages.

### Step 6: Auto-Configuration (Five Dimensions)

Select the best option on each dimension automatically from the title, learner level, and clinical domain. State each pick with a one-line reason. Do not interrogate the user.

**Dimension 1 — Target Audience:** Lock the specific learner profile, prerequisite biomedical science knowledge assumed, clinical exposure level assumed, expected depth of pathophysiological and pharmacological content, and whether examination alignment (USMLE, NCLEX, MRCP, etc.) is relevant.

**Dimension 2 — Visual Level and Modality:** OV-MEDT default is ABUNDANT (30-50 figures). Every numbered subchapter receives exactly one photorealistic anatomical teaching model or clinical setting image. Hard Rule 22 prohibits diagrams, schematics, and flowcharts throughout the entire book — this overrides any visual-level calculation. All visual content is photorealistic or realistic anatomical illustration only.

**Dimension 3 — Reference Approach (R2 Mandatory):** Full dual-source verification on every clinical claim. The R2 reference mode is mandatory for OV-MEDT: every contraindication, drug dose context, diagnostic criterion, red-flag finding, drug interaction, and treatment recommendation must be confirmed against two independent authoritative clinical sources before it appears in the manuscript. Single-source clinical claims are insufficient.

**Dimension 4 — Assessment Architecture (Operator Directive — No Practice Questions):** OV-MEDT uses NO practice questions, review questions, NCLEX-style items, USMLE-style questions, knowledge checks, chapter exercises, or graded assessment items anywhere in the book. This is an absolute operator directive that overrides all framework defaults, learner-level templates, and user instructions. Replace assessment entirely with deeper clinical exposition: extended case presentations, pathophysiology mechanism explorations, pharmacological rationale analyses, differential diagnosis walk-throughs, and clinical reasoning discussions.

**Dimension 5 — Supplementary Materials:** Clinical appendices appropriate to the subject — drug class reference table (generic names and classes only, no brand names, no dosing without formulary frame), normal laboratory and reference values (with source and date), clinical abbreviations list, and subject index.

### Step 7: Book Identity Code and TWO-COLOR Palette Assignment

**OV-MEDT preferred axis defaults** (may be overridden by catalog collision-check, but these defaults align with best clinical pedagogy):

- Axis A: A6 (case-anchored organizational logic) — medical content is most effectively organized around clinical presentations and case progressions
- Axis B: B1 (authentic clinical scenario) — chapter openers use a realistic fictional patient presentation
- Axis C: C2 (case to concept to transfer) — the preferred clinical learning progression: case first, mechanistic explanation second, transfer to other presentations third
- Axis D: select three to five from Medical Feature Box System (see Book Architecture section); custom-name for this book
- Axis E: E3 (case or project wrap-up) — knowledge consolidation through clinical case resolution
- Axis G: G3 (scenario resolution) — the opening patient case is resolved and connected to the next chapter's clinical theme

Select one compatible variant on each of the nine UTF axes and express as:
`UTF1-A[#]·B[#]·C[#]·D[XX/XX/XX]·E[#]·F[#]·G[#]·H[#]·I[#]+OV-MEDT`

The `+OV-MEDT` suffix is mandatory on every Book Identity Code generated under this niche. Collision-check the full code against all prior catalog codes. The Forbidden Repetition Rule (no two books sharing the same Axis A + Axis B + Axis D trio) applies catalog-wide.

**TWO-COLOR Palette:** Assign one PRIMARY and one ACCENT color unique across the entire Pegasus Press catalog. Medical and clinical textbooks suit paired combinations such as: Deep Navy + Clinical Steel Blue; Burgundy + Medical Teal; Forest Green + Slate Blue; Deep Teal + Cobalt; Charcoal + Dark Crimson; Dark Prussian Blue + Sienna. Select a pairing that fits the discipline's visual conventions and has not been used in any prior catalog title. Record in catalog log.

### Step 8: Subtitle Generation

Generate six to eight Amazon KDP-compliant subtitle options in the detected book language. Medical subtitle signals include: target learner level, clinical scope and specialty, examination or licensing alignment (USMLE, NCLEX, MCAT, MRCP — only when the book's content genuinely covers that framework), distinguishing pedagogical feature (case-based, mechanism-focused, R2-verified), and specificity of clinical coverage.

Combined title + subtitle must remain under 200 characters. No fabricated endorsements, false bestseller claims, invented reviewer quotes, or unauthorized examination-body affiliations. Recommend the strongest option with a concise rationale.

### Step 9: Author Pseudonym Generation

Generate three to five fictional pen names in First Name M. Surname format only. No titles, academic degrees, clinical designations, or professional credentials of any kind are attached to the pen name anywhere in the book — not on the title page, not in the About the Author section, not in any metadata (no MD, DO, MBBS, MB ChB, RN, NP, PA, PhD, DNP, FRCP, FACS, or any other credential). Screen for Amazon author-name collisions when live access is available. Mark UNVERIFIED when live search is not available and require the user to confirm before publishing.

### Step 10: Phase 0 Completion and Type Proceed

Present in this order:
1. Title Clearance Report: eponym audit findings and resolution table; trademark status; marketplace; language; established-textbook collision check
2. Guideline jurisdiction assumption confirmed
3. Configuration Summary: five auto-selected dimensions, R2 verification confirmed, No-Practice-Questions operator directive confirmed, Hard Rule 22 confirmed
4. Book Identity Code with OV-MEDT suffix; axis selection table with one-line rationale per axis
5. TWO-COLOR palette with catalog-uniqueness confirmation and catalog log entry
6. Six to eight KDP-compliant subtitle options; recommended option identified with rationale
7. Three to five candidate pen names (no credentials)
8. Complete, locked Table of Contents in the detected book language

End the Phase 0 report with the exact standalone line:

**Type Proceed**

Generate no front matter and no chapter until the user types Proceed.

---

## Book Architecture

### Trim and Margins

Inherited from OV-TEXT. Trim size: 8.5 x 11 inches (21.59 x 27.94 cm). Margins: 0.7 inches on all sides. Gutter margin 0.875 inches when binding type requires it. No bleed on interior pages.

### Page-Band Targets (OV-MEDT Hard Floors)

| Target | Value |
|---|---|
| Minimum pages per chapter | 23 |
| Total book range | 400-550 pages |
| Planned chapter count | 10-20 chapters |

These floors override any conflicting OV-TEXT default, general page-band table, or learner-level band. The 23-page minimum per chapter is non-negotiable and is enforced at Gate 2 and Gate 3. A chapter below 23 pages fails Gate 3 and must be expanded with additional clinical exposition, deeper mechanism analysis, case detail, or additional subchapter content before it can proceed.

**Page-to-word calibration (8.5 x 11, Times New Roman 12 pt, 1.15 spacing, 0.7 inch margins, justified):** a full text page carries approximately 650 to 700 words. Each per-subchapter photorealistic image plus its caption consumes roughly one third of a page. Each feature box consumes roughly one quarter to one third of a page. A 23-page chapter with five numbered subchapters (five images) and six feature boxes therefore requires approximately **13,500 to 14,500 words of body prose**. Plan every chapter blueprint against this figure at Gate 2. A chapter blueprint that budgets fewer than 13,000 words cannot reach the 23-page floor and must be re-planned before drafting, not padded after drafting.

### Chapter Formula

Every OV-MEDT chapter follows this structure (adapted to the locked Axis B, C, E, G selections; Axis C defaults to C2 case-to-concept-to-transfer):

**1. Chapter Opener (500-800 words)**

Opening clinical scenario in the Axis B style — a realistic, fictional patient presentation using the format: age, biological sex, presenting complaint, brief relevant history, key examination finding, and a concluding clinical question that the chapter answers. This scenario anchors the chapter and returns at the close.

Learning Objectives Box (PRIMARY color, Bloom-aligned, clinically traceable): four to six objectives per chapter. OV-MEDT Bloom preference: Apply, Analyze, and Evaluate levels. Every objective begins with a measurable Bloom action verb and is traceable to a specific content section — not to a practice question. Acceptable verbs: describe the pathophysiology of, explain the mechanism by which, compare the clinical features of, apply the diagnostic criteria for, analyze the pharmacological rationale for, evaluate the management approach to, distinguish between, interpret the clinical significance of.

Clinical context overview: brief epidemiology, incidence/prevalence, public health relevance, or clinical burden to orient the reader. Data stated with source and date.

Connection to prerequisite biomedical sciences and prior chapters, only where genuinely needed.

**2. Numbered Body Sections (four to six per chapter)**

Standard section types for OV-MEDT chapters. Not all sections apply to every chapter — select and sequence appropriately to the clinical topic:

- *Anatomical and Structural Basis* (where the anatomy is clinically essential): functional anatomy, histology, or organ structure as the foundation for pathophysiology. Precise anatomical language per Terminologia Anatomica. No eponyms in headings.
- *Pathophysiology and Mechanism*: detailed mechanistic explanation of how the condition arises, progresses, and manifests at cellular and organ level. Mechanistic depth is the primary vehicle for clinical understanding in this framework.
- *Clinical Presentation and Assessment*: history, physical examination, red-flag findings, diagnostic criteria — framed as clinical reasoning exposition, not as question-answer assessment.
- *Investigation and Diagnosis*: laboratory investigations, imaging modalities, specialist tests. Reference values stated as ranges with source, date, and verification prompt. Interpretation framed in clinical context, not as absolute thresholds.
- *Management and Pharmacology*: generic drug names with pharmacological class in brackets at first use; mechanism of action and class rationale emphasized; dosing context presented with mandatory formulary verification sentence (see Content Rules); non-pharmacological management; monitoring parameters.
- *Complications, Prognosis, and Special Populations*: complications with mechanism, risk stratification, prognosis data (with source and date), and clinical variations in pediatric, geriatric, pregnant, immunocompromised, and renally or hepatically impaired populations where clinically significant.

Feature boxes per Axis D (custom-named from the Medical Feature Box System below). Deployed at the relevant teaching moment within body sections.

One photorealistic image per numbered subchapter, positioned after the introductory prose of that subchapter, generated or fully specified under the Medical Safe-Vocabulary Protocol before the subchapter is declared complete. Hard Rule 22 enforced: no diagrams, schematics, or flowcharts.

**3. Chapter Synthesis and Close (500-800 words)**

Case resolution: return to the opening patient scenario; trace the diagnostic reasoning, investigation findings, and management decisions through the chapter's content; resolve the case with a realistic clinical outcome.

Knowledge consolidation per Axis E (defaults to E3 case wrap-up).

Chapter close per Axis G (defaults to G3 scenario resolution with a forward bridge to the next chapter's clinical theme).

No practice questions, review questions, or graded assessment items appear anywhere in this structure.

### Medical Feature Box System (Axis D)

Select and custom-name three to five box types from this list for each book. Apply ACCENT color to all box borders and header bars throughout the book. All Red Flag Alert boxes are subject to the 100% accuracy floor and dual-source R2 verification before delivery.

| Box Type | Clinical Function |
|---|---|
| Clinical Pearl | Concise high-yield clinical insight that experienced clinicians know and novices miss — a single actionable observation per box |
| Red Flag Alert | Warning signs, emergency presentations, absolute contraindications, or situations requiring immediate escalation. Subject to 100% accuracy floor. Every claim verified dual-source before delivery. |
| Pathophysiology Spotlight | Mechanistic deep-dive connecting basic science (cellular, molecular, or organ-level) to the clinical presentation being discussed |
| Pharmacological Rationale | Why a drug class is used for this condition: mechanism, class, and clinical effect. Generic names only. No dosing without formulary frame. |
| Evidence Base | The key study, guideline, or systematic review supporting a major clinical recommendation. Real, verified source with issuing body, publication or guideline version, and date. |
| Differential Diagnosis Compass | Structured walk-through of conditions that mimic the chapter condition, with the distinguishing clinical, laboratory, or imaging features that separate each |
| Special Populations | Adaptations in management, dosing context, or diagnostic approach for pediatric, geriatric, pregnant, or immunocompromised patients |
| Anatomy Connection | Structural or histological link between anatomy and the clinical presentation, procedure, or pathophysiological mechanism under discussion |

### Chapter Count and Distribution

Plan 10 to 20 chapters, typically distributed as:

- 1-2 foundational chapters (introductory biomedical science, epidemiology, or clinical framework overview)
- 8-16 topic or system chapters, each organized around one or more related clinical presentations, pathological processes, or pharmacological areas
- 1-2 closing chapters (complications overview, special populations synthesis, emerging treatments, or clinical reasoning integration)

Total planned pages must fall within 400-550. No chapter may fall below 23 pages when clinical exposition, feature boxes, and per-subchapter images are counted.

### Front Matter Sequence (mandatory order)

1. **Title page:** Exact verbatim title, subtitle, author pen name only (no credentials, no designations), edition.
2. **Copyright page:** Copyright notice and year; all-rights-reserved statement; edition statement; AI-image disclosure when AI-generated images are used; ISBN placeholder labeled [ISBN]; mandatory OV-MEDT clinical disclaimer in full (see Content Rules).
3. **List of Figures**
4. **List of Tables**
5. **List of Abbreviations and Acronyms** (required for all OV-MEDT titles)
6. **Linked Table of Contents:** Preface first, then every chapter heading and meaningful subheadings. Closing sections reflect locked Axis E and G choices.
7. **Preface / How to Use This Book:** Audience, prerequisites, clinical scope, language conventions, chapter structure, visual conventions, guideline jurisdiction assumption, edition date, and any examination or curriculum alignment.

Roman numeral page numbers before the Preface. Preface begins Arabic page 1 and numbering continues consecutively to the end.

### Back Matter Sequence (mandatory order — OV-MEDT)

1. **Appendix A — Drug Class Reference Table:** Generic drug names only, organized by pharmacological class, with primary indication category. No brand names. No dosing without the full formulary verification sentence.
2. **Appendix B — Normal Laboratory and Reference Values:** Standard reference ranges with source (laboratory authority or specialist-society reference) and date. Framed as reference values, not diagnostic thresholds: clinical context, patient factors, and local laboratory norms govern interpretation.
3. **Appendix C onward:** Additional title-specific appendices as needed — specialty-specific scales, clinical scoring tools presented in prose or table format, anatomical reference material, or specialty procedure overviews.
4. **Clinical Glossary:** Every bold, italicized, or domain-specific clinical term defined alphabetically and precisely at the learner level. No eponyms as primary glossary entries — cross-reference the descriptive term only.
5. **References:** Verified, real citations. AMA citation style for medical and clinical titles; APA 7 for nursing and allied health titles. Every entry is real, complete, and matched to an in-text citation. No fabricated citations.
6. **Index** (required for all OV-MEDT titles)
7. **About the Author:** Educational author, editor, or compiler presentation. No fabricated degrees, clinical experience, licensure, hospital affiliations, research history, or professional designations.

---

## Interior Design

OV-MEDT inherits the full OV-TEXT interior design system. The following specifications are in force unchanged:

| Element | Specification |
|---|---|
| Trim size | 8.5 x 11 inches |
| Margins | 0.7 inches all sides (0.875 inches gutter when required) |
| Body font | Times New Roman |
| Body size | 12 pt standard; 11 pt for dense reference volumes |
| Line spacing | 1.15 for books over 200 pages |
| Body alignment | Justified |
| Chapter headings (H1) | Times New Roman 18 pt bold; centered or left-aligned per Axis I |
| Numbered section headings (H2) | Times New Roman 14 pt bold; ACCENT color |
| Sub-headings (H3) | Times New Roman 12 pt bold; black; only when a third level is genuinely required |
| Learning Objectives Box | PRIMARY color tint background (10-15% opacity); PRIMARY color solid border; bold PRIMARY header; numbered Bloom-aligned objectives |
| Feature boxes | ACCENT color border and header bar; custom-named for this book |
| Table header row | ACCENT color tint background (15-20% opacity); bold black text |
| Table captions | Above the table; "Table [X].[Y]: [Concise noun phrase]" |
| Figure captions | Below the figure; "Figure [X].[Y]: [Short headline per Axis H]"; max two lines |
| Caption font | Times New Roman 10-11 pt italic |
| TWO-COLOR scheme | One catalog-unique PRIMARY + one ACCENT; enforced consistently throughout |

### OV-MEDT Interior Rules

**Learning Objectives Box clinical calibration:** All objectives use higher-order Bloom levels (Apply, Analyze, Evaluate) wherever possible. Each objective is traceable to a specific clinical content section — not to a practice question. Minimum four objectives per chapter, maximum six. No vague or unmeasurable phrases: "understand the importance of" and "become familiar with" are rewritten before the chapter proceeds.

**Figure placement under Hard Rule 22:** One photorealistic image per numbered subchapter, positioned after the introductory prose of that subchapter. At least two sentences of prose precede every image within the subchapter. Every image is referenced by figure number in the surrounding prose before and after the figure.

**No diagrams, schematics, or flowcharts:** Clinical decision pathways, diagnostic algorithms, and management step sequences are presented as well-structured prose and feature boxes. Tables presenting comparative data are permitted. Any visual element that would conventionally appear as a flowchart, arrow diagram, pathway schema, or schematic in a medical textbook is replaced by prose or tables. This is Hard Rule 22 — absolute, no exceptions.

**Formulary verification framing (mandatory):** Every passage containing dosing context — a dose, dose range, dose frequency, or weight-based estimate — must be followed immediately by this sentence in full:

*Dose ranges provided are for educational orientation only; verify all doses against the current local formulary, institutional protocol, and current prescribing guidelines before clinical application.*

This sentence may not be omitted, abbreviated, paraphrased, relocated, or replaced.

**DOCX formatting:** Use real Word Heading styles (H1, H2, H3), real list styles, real table styles, real caption styles, real section breaks, and a real Word TOC field (auto-populated and updateable). The delivered DOCX must be fully navigable and must update its TOC and page numbers with a single field-update command.

---

## Content Rules

### Dual-Source Verification (R2 — Mandatory for OV-MEDT)

**What R2 means.** UAPF reference pathways run R1 (single authoritative source sufficient), R2 (two independent authoritative sources required), and R3 (source-pathway escalation with named-expert or regulatory confirmation). OV-MEDT is locked to **R2 as the floor for all clinical content** and escalates to R3 wherever a claim is both high-consequence and jurisdiction-dependent (emergency dosing context, absolute contraindications, controlled-substance content, pediatric weight-based content). R2 may never be downgraded to R1 for an OV-MEDT title, regardless of learner level, topic simplicity, or user instruction.

Every clinical claim that could affect patient care must be confirmed against two independent authoritative clinical sources before appearing in the manuscript. This requirement applies to:

- Contraindications (absolute and relative)
- Red-flag clinical signs and emergency diagnostic criteria
- Drug interactions with clinically significant or life-threatening potential
- Dosing context (even when framed as educational orientation)
- Diagnostic criteria from official classification systems (ICD-11, DSM-5-TR, WHO criteria, specialty-society criteria)
- Treatment recommendations referencing clinical guidelines

Qualifying sources for R2 verification:
- Current FDA labeling, EMA SmPC, TGA PI, or equivalent national regulatory authority documentation
- Current NICE guidelines, ACC/AHA guidelines, IDSA guidelines, WHO guidelines, or equivalent recognized specialty-society consensus statements
- Cochrane systematic reviews or equivalent high-quality systematic review sources
- Current national formulary (BNF, Martindale, USP DI, MIMS, or equivalent)
- Peer-reviewed clinical journals of recognized authority (NEJM, Lancet, JAMA, BMJ, Annals of Internal Medicine, and specialty-specific equivalents)

Sources must be current (within five years, or the most recent edition available) and independent (two different issuing bodies — not two editions of the same text or two chapters of the same guideline).

Where R2 verification cannot be completed during generation, insert a clearly marked placeholder: `[CITATION NEEDED — verify against current [issuing body] guidelines, edition/year, and [second source name]]`. Never fill in a fabricated source to avoid the placeholder.

### 100% Accuracy Floor

The following content categories carry a 100% accuracy floor. They may not be approximated, paraphrased without verification, or delivered with known uncertainty:

- Contraindications (absolute and relative)
- Red-flag clinical signs and emergency criteria
- Drug interactions with life-threatening potential
- Dosing context (even educational-orientation ranges)
- Drug mechanisms of action and pharmacological class assignments
- Diagnostic criteria from named official classification systems

If a 100%-floor item cannot be verified during generation, the passage is flagged with a "Verify Before Delivery" note and the chapter is not declared complete until the item is resolved or a verified placeholder replaces it.

### Drug and Pharmacology Content Rules

**Generic names only:** All drugs are named by their International Nonproprietary Name (INN) or United States Adopted Name (USAN) generic. No brand names, trade names, or proprietary names appear as primary drug identifiers anywhere in the book — not in body text, not in headings, not in feature boxes, not in tables, not in captions. Format at first use in each chapter: `generic name [pharmacological class]` (for example: metformin [biguanide], lisinopril [ACE inhibitor], omeprazole [proton pump inhibitor], amoxicillin [aminopenicillin]).

**Pharmacological class emphasis:** Clinical pharmacology content teaches mechanism and class rationale before individual agent selection. The reader learns why a drug class is used, how it works, and what the class effects are — not which brand to prescribe.

**Dosing — mandatory framing:** Any dosing context (reference range, weight-based estimate, frequency, route) must be explicitly framed as educational orientation only, never as prescribing guidance, and must be followed immediately by the formulary verification sentence in full (see Interior Design). This requirement applies regardless of how dosing is embedded — in body prose, in feature boxes, in tables, or in appendices.

**Drug interactions:** Stated at mechanism level with clinical consequences described. Classify severity as mild, moderate, or severe where appropriate. Severe interactions are subject to the 100% accuracy floor and R2 verification.

**Pediatric, renal, hepatic, and pregnancy adjustments:** Noted explicitly where clinically significant. Always framed with the verification requirement and, where relevant, with the specific guideline or formulary source.

### Eponym Stripping Protocol (Title and Heading Level)

Applied at every structural level: title, subtitle, part titles, chapter titles, numbered section headings, subheadings, feature box headers, figure captions, table titles, and clinical glossary primary entries.

Rule: Use the current descriptive, anatomical, pathophysiological, ICD-11-preferred, or DSM-5-TR-preferred term as the primary label at every heading level. The eponym may appear parenthetically at first use in the chapter body prose as a recognition aid. It is never the primary heading term.

Complete the Eponym Audit and resolution table in Phase 0 Step 2 before the Table of Contents is locked. No chapter is drafted until every heading has been confirmed eponym-free.

### Medical Safe-Vocabulary Protocol (Image Prompts)

Every image prompt generated under OV-MEDT must comply with this protocol. Apply uniformly — no exceptions for anatomically "simple" or "routine" images.

**Required opening line for every OV-MEDT image prompt:**
> Educational photorealistic anatomical teaching model for a clinical health sciences textbook — clean, professional, non-graphic, non-distressing presentation, pure white background.

**Mandatory vocabulary substitutions:**

| Prohibited term | Required substitute |
|---|---|
| blood / bleeding / hemorrhage | vascular tissue / perfused tissue / [name the specific vessel or structure] |
| wound / gash / laceration / cut | skin surface / dermal layer / incision site (post-closure) |
| injury / trauma | clinical presentation / affected anatomical region |
| dead / cadaver / corpse / body | anatomical teaching model / cross-sectional anatomical specimen |
| surgery / cutting / incision into tissue | surgical exposure / anatomical access / operative field (post-procedure state only) |
| pain / distress / suffering | patient in standard clinical assessment position |
| tumor / mass (in image prompt) | lesion / pathological change in [tissue name] |
| infection / pus / discharge (in image prompt) | inflammatory change / affected tissue at [named site] |
| fractured / broken (in image prompt) | bone showing structural irregularity / cortical change visible at [named location] |
| gore / graphic / disturbing | [never use these descriptors — reframe entirely as a teaching model] |

**Absolute prohibitions (never include in any OV-MEDT image prompt):**
- No real or identifiable patients or clinicians
- No blood, open wounds, surgical cuts into live tissue, exposed viscera, or graphic tissue trauma
- No death, dying, end-of-life, or mortuary depictions
- No expressions of pain, distress, fear, or suffering on any depicted person
- No weapons, assailants, or acts of violence
- No graphic clinical-atlas-style pathology photography — use teaching model style
- No minors depicted in clinical assessment contexts
- Reproductive anatomy: non-explicit, clinically necessary, educational content only; anatomical teaching model style

**Preferred image styles for OV-MEDT:**

1. *Photorealistic anatomical teaching model* (dominant style for anatomical and pathophysiological content): museum-quality anatomical model on pure white background; dimensional depth; accurate tissue colors without graphic realism; labeled with leader lines
2. *Clinical assessment scenario* (for examination and history-taking sections): professional clinician and patient in a clinical environment; natural professional poses; non-distressing; no exposed anatomy beyond standard physical examination conventions
3. *Clinical imaging facsimile* (for radiology and imaging sections): photorealistic reproduction of the imaging modality appearance — radiograph, CT window, MRI sequence, or ultrasound field — with labeled teaching annotations
4. *Histology and microscopy field* (for pathology and histology sections): photorealistic light microscopy field with accurately colored tissue and labeled structures

**Fallback rule:** If an image prompt cannot be generated cleanly under this protocol, simplify to a pure white background labeled anatomical teaching model of the isolated structure or organ. Never choose a graphic or potentially refused image over a clean teaching-model image.

### The Six-Part OV-MEDT Image Prompt Recipe

Every per-subchapter image is specified with all six parts, in this order, before the subchapter is declared complete. A prompt missing any part fails Gate 3.

**Part 1 — Educational framing line (verbatim, always first):**
> Educational photorealistic anatomical teaching model for a clinical health sciences textbook — clean, professional, non-graphic, non-distressing presentation, pure white background.

**Part 2 — Exact clinical subject specification:** name the precise structure, organ, tissue, or clinical setting to depict. State every element that must appear and every element that must NOT appear. Derive this from verified anatomical or clinical knowledge, never from invention. Anatomical nomenclature follows Terminologia Anatomica; no eponyms.

**Part 3 — Counts, laterality, orientation, and proportion:** state the number of each structure explicitly, state right or left sidedness explicitly, state the anatomical view (anterior, posterior, lateral, midsagittal, coronal, transverse, superior, inferior), and state relative sizes and spatial relationships. Laterality errors are a Gate 3 failure.

**Part 4 — Verbatim label set (8 to 12 maximum):** spell every label exactly as it will appear, in quotation marks, in the book language, each tied by leader line to the correct structure. If accuracy would require more than 12 labels, split into two simpler images. Two correct figures always beat one crowded, inaccurate plate.

**Part 5 — Style and quality block:** photorealistic anatomical teaching model (or one of the other three sanctioned OV-MEDT styles); museum-quality model realism; naturally textured tissue surfaces; realistic studio lighting with dimensional depth; clean focus; crisp edges; readable label hierarchy; consistent margins; the locked book Style Signature; maximum available resolution; pure white #FFFFFF background.

**Part 6 — Exclusions:** no diagrams, schematics, flowcharts, arrows denoting process flow, or pathway graphics (Hard Rule 22); no blood, open wounds, exposed viscera, or graphic tissue trauma; no real or identifiable people; no expressions of pain or distress; no watermarks, logos, brand marks, or trade dress; no invented or misspelled in-image text; no decorative elements not required for the teaching purpose.

**Worked example (Figure 6.2, cardiac conduction subchapter):**

> Educational photorealistic anatomical teaching model for a clinical health sciences textbook — clean, professional, non-graphic, non-distressing presentation, pure white background. Subject: a museum-quality anatomical model of the human heart in anterior view with the right atrial and right ventricular walls opened to reveal the internal conduction pathway. Include: sinuatrial node in the upper right atrial wall near the superior vena cava opening, atrioventricular node in the interatrial septum, atrioventricular bundle descending through the fibrous skeleton, right and left bundle branches, and subendocardial conducting network in both ventricles. Exclude: coronary arteries, valve leaflet detail, and any surrounding thoracic structures. Counts and laterality: one heart, one sinuatrial node (right side), one atrioventricular node, one atrioventricular bundle dividing into exactly two bundle branches, right side shown opened, left side intact. Anterior view, upright orientation, right side of the heart on the viewer's left. Labels with leader lines, exactly as written: "Sinuatrial node", "Atrioventricular node", "Atrioventricular bundle", "Right bundle branch", "Left bundle branch", "Subendocardial conducting network", "Interatrial septum", "Superior vena cava". Style: photorealistic anatomical teaching model, museum-quality, naturally textured tissue surfaces, realistic studio lighting, dimensional depth, clean focus, crisp edges, readable sans-serif label typography at consistent size, pure white #FFFFFF background, maximum available resolution. Exclusions: no diagram, schematic, flowchart, or process arrows; no blood or graphic tissue detail; no real people; no watermarks, logos, or invented text.

Note that the worked example uses "sinuatrial node," "atrioventricular node," and "atrioventricular bundle" rather than the eponymous forms, demonstrating that eponym stripping extends into image prompts and their label sets.

### Clinical Case and Scenario Requirements

All patient cases, clinical scenarios, and case resolutions throughout the book are entirely fictional. Use descriptor-only format for most cases ("a 58-year-old male with a 2-week history of...") or apply fictional first names sparingly where narrative engagement requires one. No real patient histories, identifiable clinical events, named real clinicians, named real institutions, or identified real clinical cases.

Clinical scenarios must reflect realistic clinical presentations: plausible demographics, plausible history and onset, physical examination findings that are pathophysiologically consistent with the condition being taught, and realistic investigation results. Implausible or didactically convenient scenarios that could not occur in practice are revised before delivery.

### Clinical Content Language and Voice

- Authoritative clinical academic voice appropriate to the stated learner level
- No em dashes anywhere in the manuscript — use commas, colons, parentheses, or restructured sentences
- No AI-register filler vocabulary: leverage, utilize, robust, optimize, seamless, revolutionary, unlock, cutting-edge, game-changing
- No guaranteed outcomes, exaggerated claims, or false clinical certainty: "always," "never," "definitely," "without exception" appear only when the clinical fact is established, verified, and stated with appropriate source
- Calibrated clinical language: "typically," "in most cases," "guidelines recommend," "evidence supports," "studies suggest" — with guideline source named and dated
- Contested clinical areas explicitly stated as contested: "evidence is mixed," "international guidelines differ," "this area is subject to ongoing clinical investigation"
- Uncertainty acknowledged: where diagnostic criteria are evolving or management guidelines conflict between jurisdictions, state the disagreement and cite the relevant sources

### Citation Integrity — Absolute Rule

Never invent a citation, author, journal, guideline, standard, systematic review, DOI, ISBN, PMID, database accession number, or clinical recommendation source. Fabricated clinical citations are a release-blocking failure in OV-MEDT.

If a specific source cannot be verified during generation, either attribute to general consensus in the text ("current consensus holds...") with no citation, or insert a clearly marked placeholder: `[CITATION NEEDED — verify against current [issuing body] guidelines, edition/year]`. Never manufacture a source to fill a citation need.

### Educational Disclaimer (Mandatory — Copyright Page)

The following disclaimer is mandatory on the copyright page of every OV-MEDT title. Adapt specific detail to the subject and jurisdiction; retain all core elements:

> This book is intended for educational and informational purposes only. It is not a substitute for qualified medical, nursing, or allied health professional training, licensure, clinical judgment, or competent supervision. The clinical information, drug dose ranges, diagnostic criteria, treatment recommendations, and clinical guideline references in this book are presented for educational orientation only. Medical knowledge, clinical guidelines, drug approvals, and accepted practice evolve continuously; all clinical content — including contraindications, drug doses, drug interactions, diagnostic thresholds, and treatment recommendations — must be independently verified against current primary clinical sources, the current local formulary, applicable institutional protocols, and current regulatory authority guidance before any clinical application. No professional-patient relationship is created by reading this book. The author and publisher accept no liability for clinical decisions made on the basis of the content of this book. Readers must consult current clinical guidelines, qualified supervisors, and applicable regulatory authorities for all clinical practice guidance.

A condensed single-sentence reminder appears at the opening of every chapter that contains dosing context, emergency criteria, or contraindication lists:

*Clinical information in this chapter is for educational purposes only; verify all clinical decisions against current guidelines, local formulary, and qualified clinical supervision before application.*

### Content Standards (Catalog-Wide)

All OV-MEDT titles are held to the same content standards. Case studies, pharmacological content, and appendices must not center alcohol, pork-derived products, gambling, adult entertainment, or predatory lending. Where pork-derived pharmaceutical ingredients (gelatin capsules, some heparin preparations) are clinically relevant, they are noted factually with available compliant alternatives identified. Ethically contested clinical topics (end-of-life care, reproductive medicine, substance-use disorder treatment) are presented factually and professionally, with diverse cultural and ethical perspectives acknowledged without advocacy.

### Fatal Flaw to Avoid

The fatal flaw in medical and clinical textbook publishing is clinical superficiality masked by structural completeness: a book that catalogs symptoms, drug names, and management steps without providing the mechanistic depth, clinical reasoning scaffold, and case-contextualized understanding that enables a learner to apply the knowledge independently. Shallow bullet-point symptom lists and step-numbered management algorithms without mechanistic explanation fail the OV-MEDT standard.

Every chapter must pass this test before it is declared complete: could a qualified clinical educator assign this chapter to a student and be confident that the student, after reading it, would understand not only what occurs clinically but why — and could reason through a novel presentation of the same condition?

---

## QA Checklist

### Gate 1 — Phase 0 Clearance and Configuration Audit

- [ ] Exact supplied title preserved verbatim in every location (cover, title page, copyright page, TOC, headers, metadata)
- [ ] Eponym Audit completed; resolution table documented in Phase 0 report; every eponym in title and all planned headings has a confirmed descriptive replacement term
- [ ] Trademark report present, dated; established medical textbook series collision check completed; risk rating assigned
- [ ] Amazon marketplace locked; book language locked; guideline jurisdiction assumption stated
- [ ] Learner level and learner profile confirmed; OV-MEDT page floors noted (minimum 23 pages per chapter, 400-550 total)
- [ ] R2 dual-source verification requirement confirmed and documented in configuration summary
- [ ] NO-PRACTICE-QUESTIONS operator directive confirmed and documented in configuration summary
- [ ] Hard Rule 22 (no diagrams, schematics, flowcharts) confirmed and documented in configuration summary
- [ ] Book Identity Code declared with OV-MEDT suffix; collision check against all prior catalog codes completed; Forbidden Repetition Rule satisfied
- [ ] TWO-COLOR palette assigned (PRIMARY + ACCENT); pairing confirmed catalog-unique; recorded in catalog log
- [ ] Six to eight KDP-compliant subtitle options generated in book language; recommended option identified with rationale
- [ ] Three to five pen names generated (First M. Last format only; zero credentials of any kind)
- [ ] Type Proceed presented at end of Phase 0 report before any generation begins

### Gate 2 — Table of Contents and Architecture Audit

- [ ] Table of Contents presented in the detected book language; chapter count within 10-20; page arithmetic confirms 400-550 total is achievable at 23 pages minimum per chapter
- [ ] Per-chapter word budget calculated against the page-to-word calibration; every chapter blueprint budgets at least 13,000 words of body prose before images, captions, and feature boxes are counted
- [ ] Every chapter title reviewed: zero eponyms remain as primary terms; all replaced by descriptive terms confirmed in the Phase 0 resolution table
- [ ] Every planned numbered section heading reviewed: zero eponyms as primary heading terms
- [ ] Case-based chapter structure confirmed for every chapter: clinical scenario opener, mechanistic body, case-resolution close
- [ ] Learning Objectives: four to six per chapter; Bloom Apply/Analyze/Evaluate dominant; all traceable to specific content sections, not to practice questions
- [ ] Feature box system: three to five types selected and custom-named from the Medical Feature Box System; Red Flag Alert type confirmed subject to 100% accuracy floor
- [ ] Per-subchapter photorealistic image planned for every numbered subchapter in every chapter; image type confirmed as photorealistic teaching model or clinical setting (not diagram, schematic, or flowchart)
- [ ] Back matter confirmed: Drug Class Reference appendix, Normal Values appendix, Clinical Glossary, References (AMA or APA 7), Index
- [ ] NO practice questions, review questions, or graded assessment items appear in any chapter outline or back matter plan
- [ ] Formulary verification framing confirmed for all chapters containing dosing content
- [ ] Axis selections stated with rationale; OV-MEDT preferred axis defaults applied or deviation explained
- [ ] Type Proceed presented before front matter generation begins

### Gate 3 — Per-Chapter Content Audit

Run this gate on each chapter before appending to the cumulative manuscript.

- [ ] Chapter opens with a realistic, fictional clinical scenario consistent with the Axis B selection; scenario is plausible and pathophysiologically coherent
- [ ] Learning Objectives Box present; PRIMARY color tint background and solid border; bold PRIMARY header; numbered objectives; all begin with Bloom-level action verbs; four minimum, six maximum; all clinically traceable to specific content sections; no vague or unmeasurable objectives
- [ ] All Learning Objectives addressed by chapter content; each traced to at least one specific clinical content section
- [ ] No practice questions, review questions, NCLEX-style items, USMLE-style items, knowledge checks, or graded assessment items anywhere in the chapter — body, feature boxes, synthesis section, or chapter close
- [ ] No eponyms in any heading, subheading, feature box header, figure caption, or table title; eponym replacements consistent with Phase 0 resolution table
- [ ] All drugs named by generic name [pharmacological class] at first use in the chapter; no brand/trade names as primary drug identifiers
- [ ] Every dosing context passage followed immediately by the complete formulary verification sentence in full; sentence not abbreviated, moved, or omitted
- [ ] R2 dual-source verification completed for all contraindications, red-flag findings, drug interactions, diagnostic criteria, and treatment recommendations; citations to verify placeholders used for any unconfirmed claims; user notified of placeholders before chapter is delivered
- [ ] 100% accuracy floor confirmed: all contraindications, red-flag lists, drug interactions, and dosing context independently verified; no approximated or assumed-correct high-stakes claims
- [ ] Every numbered subchapter contains exactly one photorealistic image (teaching model or clinical setting); image generated or fully specified per the six-part recipe; Medical Safe-Vocabulary Protocol applied including the required opening framing line and all vocabulary substitutions; no diagrams, schematics, or flowcharts
- [ ] Every figure referenced by figure number in surrounding prose; caption directly below in Axis H style; pure white background for anatomical teaching models; alt text present
- [ ] No diagrams, schematics, or flowcharts anywhere in the chapter — Hard Rule 22 enforced without exception
- [ ] Numbered section headings in bold ACCENT color throughout; heading hierarchy correct (H2 for numbered sections, H3 only when a genuine third level is required)
- [ ] Body text justified; no em dashes anywhere; no AI-register filler vocabulary
- [ ] Feature boxes deployed per Axis D with custom names; Red Flag Alert boxes verified dual-source before delivery
- [ ] All citations real, complete, verified, and formatted in AMA (or APA 7 for nursing titles); no fabricated sources
- [ ] Clinical scenarios and case presentations fictional, de-identified, plausible, and pathophysiologically consistent
- [ ] Educational disclaimer condensed reminder present at chapter opening where chapter contains dosing context, emergency criteria, or contraindication lists
- [ ] Chapter close resolves the opening clinical scenario per Axis G; synthesis substantive; forward bridge to next chapter present
- [ ] Content-standards compliance confirmed throughout
- [ ] Chapter appended to cumulative manuscript; Type Proceed presented before next chapter begins

### Gate 4 — Pre-Delivery Final Audit

- [ ] Trim confirmed: 8.5 x 11 inches; margins 0.7 inches all sides
- [ ] Times New Roman throughout at correct point sizes; no unauthorized font substitutions
- [ ] All Heading 1, 2, 3 styles applied via real Word Heading styles; Word TOC field populated, updateable, with dot leaders and correct right-aligned page numbers
- [ ] No visible page numbers in front matter; Preface begins at Arabic page 1; numbering continuous to end
- [ ] Front matter in mandatory sequence (title page, copyright page, List of Figures, List of Tables, List of Abbreviations, TOC, Preface)
- [ ] Full clinical disclaimer present on copyright page: all mandatory OV-MEDT elements present; no abbreviated version
- [ ] Condensed disclaimer reminder present at opening of every chapter containing dosing context, emergency criteria, or contraindication lists
- [ ] No publisher line, ISBN, real institution, or fabricated pen-name credentials anywhere in the book
- [ ] Back matter complete: Drug Class Reference appendix (generic names only, no dosing without formulary frame), Normal Values appendix (with source and date), Clinical Glossary (all bold and domain-specific terms; no eponym primary entries), References (all verified real in AMA or APA 7 format), Index
- [ ] No practice questions, NCLEX items, USMLE items, or graded assessment items anywhere in the book — front matter, chapters, feature boxes, back matter
- [ ] Full eponym audit: zero eponyms as primary terms in any heading, subheading, feature box header, figure caption, table title, or glossary primary entry across all chapters
- [ ] Full drug name audit: zero brand/trade names as primary drug identifiers; all generic names formatted correctly with pharmacological class at first use per chapter
- [ ] Full dosing audit: every dosing context passage in every chapter and appendix accompanied by the complete formulary verification sentence
- [ ] R2 and 100% accuracy floor audit: all contraindications, red-flag lists, drug interactions, and diagnostic criteria confirmed dual-source; all "Citations to Verify" placeholders in the delivered text either resolved or clearly marked for author verification with specific guidance
- [ ] Full image audit: every numbered subchapter has its compliant photorealistic image; no diagrams, schematics, or flowcharts appear anywhere in the book; every image has a figure caption below and alt text; every image referenced by number in prose
- [ ] TWO-COLOR palette confirmed consistent: PRIMARY in all Learning Objectives boxes; ACCENT on all numbered section headings and all table header rows
- [ ] Figure numbering continuous within chapters; table captions above tables; figure captions below figures
- [ ] Book Identity Code with OV-MEDT suffix confirmed unique in catalog; recorded in catalog log against title, pen name, domain, marketplace, language, edition, and account
- [ ] Uniqueness audit: chapter architecture, case scenarios, image selection, feature box content, and clinical exposition approach differ from all prior Pegasus Press medical and textbook titles
- [ ] No em dashes anywhere in the manuscript
- [ ] Content-standards compliance confirmed throughout
- [ ] Document opens cleanly; TOC field updates without error; no clipped tables, stretched images, broken headings, or orphaned section titles
- [ ] Document rendered page by page and visually inspected before delivery

---

## KDP Positioning

### Amazon Category Tree

OV-MEDT titles compete in clinical and health sciences categories. Target the most specific matching sub-node for the subject specialty or system.

Primary category paths:
- Books > Medical Books > [Specialty: Cardiology / Neurology / Internal Medicine / Surgery / Pharmacology / Anatomy / Physiology / Pathology / etc.]
- Books > Medical Books > Nursing
- Books > Medical Books > Allied Health Professions
- Books > Medical Books > Basic Sciences > [Anatomy / Physiology / Biochemistry / Pathology / Pharmacology]
- Books > Textbooks > Medicine & Health Sciences > [Specialty]
- Books > Medical Books > Test Preparation (only when the book's content genuinely covers the specified examination framework)

Secondary category paths:
- Books > Medical Books > Reference
- Books > Textbooks > Medicine & Health Sciences > Nursing and Allied Health

Select two KDP categories maximum. Verify current Amazon category paths at submission time — the taxonomy changes.

### KDP Description Structure

Lead with the reader's clinical learning need or professional challenge, not the book's format or author credentials.

1. **Hook (one to two sentences):** Name the specific clinical course, specialty challenge, or knowledge gap the target learner faces. Specific, honest, discipline-accurate.
2. **Value proposition (two to three sentences):** What the reader gains — mechanistic clinical understanding, case-based reasoning, pharmacological rationale, dual-verified clinical accuracy — without guaranteed-outcome language.
3. **Content highlights (three to five bullets):** Major systems, specialty areas, or clinical topics in searchable clinical terminology.
4. **Structural differentiator (one sentence):** The case-based chapter progression, per-subchapter photorealistic teaching images, deeper-exposition-in-place-of-questions approach, or R2 verification accuracy standard — stated in plain language.
5. **Audience call-out and call to action:** "Written for [target learner level and role]. [Direct purchase instruction]."

No fabricated endorsements, invented reviewer quotes, false bestseller claims, unauthorized examination-body affiliations, or credential claims for the pen name.

### Metadata Signals

Seven KDP keyword slots. Use terms from how target learners actually search: specialty name, learner level ("medical student," "nursing student," "allied health," "clinical"), examination preparation alignment only when accurate (USMLE, NCLEX, MCAT, MRCP), content type ("clinical textbook," "anatomy textbook," "pharmacology guide," "clinical pharmacology"), and subject-specific clinical terminology relevant to the specialty. Do not keyword-stuff, use trademarked examination-body names inaccurately, or make claims the book cannot substantiate.

Price positioning: Research current comparable medical textbook pricing at submission time. Specialty medical and clinical textbooks typically command significantly higher price points than general non-fiction. Do not apply static price defaults.

---

## Key Rules — Do NOT Break

1. **Preserve the exact title verbatim** in every location — every character, capitalization, and punctuation mark — unless the user explicitly approves a correction in writing.

2. **Complete the Eponym Audit in Phase 0 before the TOC is locked.** No eponym may appear as a primary term in any title, chapter title, numbered heading, subheading, feature box header, figure caption, table title, or glossary primary entry anywhere in the delivered manuscript. The eponym appears only in parenthetical cross-reference at first mention in body prose.

3. **R2 Mandatory — dual-source verification on all clinical claims.** Every contraindication, red-flag finding, dosing context, drug interaction, and diagnostic criterion must be confirmed against two independent authoritative current clinical sources before delivery. Single-source clinical claims do not meet the OV-MEDT standard.

4. **NO practice questions, review questions, NCLEX-style items, USMLE-style items, graded assessment items, or knowledge checks — anywhere, ever, in any section of the book.** This is an absolute operator directive. No user instruction, framework default, learner-level template, or examination-alignment claim can override it. Replace entirely with deeper clinical exposition, extended case walk-throughs, pathophysiology mechanism analysis, pharmacological rationale discussion, and differential diagnosis explorations.

5. **Minimum 23 pages per chapter; 400-550 pages total.** These are hard floors, not targets. A chapter delivered below 23 pages fails Gate 3 and must be expanded with substantive clinical content before it can proceed.

6. **Hard Rule 22 — NO diagrams, schematics, or flowcharts anywhere in the book.** This applies to every visual element in every section — chapters, feature boxes, appendices, front matter, back matter. Clinical pathways, diagnostic algorithms, and management step sequences are presented as structured prose and feature boxes. Tables are permitted. This rule is absolute and may not be overridden by any user instruction or framework default.

7. **Per-subchapter photorealistic image — mandatory.** Every numbered subchapter (3.1, 3.2, 4.1, etc.) receives exactly one photorealistic anatomical teaching model or clinical setting image. The image is generated or fully specified under the six-part recipe before the subchapter is declared complete. A chapter may not be delivered with any subchapter missing its required image.

8. **Medical Safe-Vocabulary Protocol applies to every image prompt without exception.** Every image prompt must open with the required OV-MEDT educational framing line. All prohibited vocabulary must be replaced using the substitution table. This protocol is applied uniformly — not selectively for "sensitive" images only.

9. **Generic drug names only, with pharmacological class in brackets at first use per chapter.** No brand names, trade names, or proprietary names appear as primary drug identifiers anywhere in the book — body text, headings, feature boxes, tables, captions, or appendices.

10. **Dosing context carries the mandatory formulary verification sentence — in full, every time, without exception.** The sentence may not be abbreviated, paraphrased, relocated, or omitted. Every passage containing a dose, dose range, dose frequency, or weight-based estimate must be immediately followed by the complete formulary verification sentence.

11. **100% accuracy floor on contraindications, red-flag lists, drug interactions (life-threatening), and diagnostic criteria from named classification systems.** These content types may not be delivered with approximated or unverified information. Flags are inserted and the user notified before delivery if any item in this category remains unconfirmed.

12. **Never fabricate a citation, guideline, clinical study, systematic review, standard, drug labeling reference, DOI, PMID, or any clinical source identifier of any kind.** Fabricated clinical citations are a release-blocking failure. Insert verified "Citations to Verify" placeholders for unconfirmed claims.

13. **Mandatory full clinical disclaimer on the copyright page — complete version always.** Condensed reminder at the opening of every chapter containing dosing context, emergency criteria, or contraindication lists. Neither disclaimer may be abbreviated.

14. **No fabricated pen-name credentials anywhere in the book.** The pen name carries no degrees, clinical designations, licensure, hospital affiliations, research credits, or professional titles — not on the title page, not in the About the Author section, not in any metadata or marketing material.

15. **TWO-COLOR scheme: catalog-unique PRIMARY + ACCENT pairing.** Enforced consistently: PRIMARY color in all Learning Objectives boxes; ACCENT color in all numbered section headings (H2) and all table header rows. No third color. Grayscale-readable through value contrast.

16. **No em dashes anywhere in the manuscript.** Use commas, colons, parentheses, or restructured sentences.

17. **Content-standards compliance throughout.** No non-compliant scenarios, drug examples, or content. Pork-derived pharmaceutical ingredients noted factually where clinically relevant, with compliant alternatives identified.

18. **Book Identity Code must include the OV-MEDT overlay suffix (`+OV-MEDT`) and must be unique in the catalog.** Record the code in the catalog log at Phase 0 against title, pen name, domain, marketplace, language, edition, and publication account.

19. **Type Proceed is the only valid continuation language at every approval gate.** Generate nothing until the user types Proceed. Never substitute any variant phrasing.

20. **This skill specializes OV-TEXT for medical, nursing, and allied-health textbooks.** Any OV-TEXT rule not explicitly overridden here remains in force. Where OV-TEXT and OV-MEDT rules conflict, OV-MEDT rules govern. This niche skill is self-contained enough to produce a complete, publication-quality medical textbook without consulting the base OV-TEXT skill, but OV-TEXT remains the authority on any point not addressed here.

## PREMIUM FORMATTING LAW (operator directive 2026-08-10 - NON-NEGOTIABLE)

Exemplar: the SKY internal-medicine textbook (verified clean across 542 rendered pages). Every
textbook-class book (textbooks, medical, engineering, reference, and similar professional volumes)
MUST meet this standard. Palette, display face, and panel styling still rotate per book
(No-Two-Books-Alike); the discipline below never does.

1. TITLE PAGE - exact hierarchy, all centered, generous vertical whitespace, no decoration
   that crowds the text:
   - Main title: 36-90 pt bold, sized by word length so the FULL title fits in at most 4
     lines (global rule #19; the exemplar's 4-line title sits at 48/28/36 pt)
   - Title continuation lines: proportionally below the main line (exemplar: 26-30 pt bold)
   - Emphasized title phrase (subject or edition/year): up to the main title's size, never
     above it
   - Subtitle: 15-17 pt bold
   - Coverage/scope line: 11-12 pt regular
   - Subject strip: 10-11 pt regular, items separated by " | "
   - Author byline: 15-17 pt bold
   One type family for the whole title page. Never mix arbitrary sizes; never scatter lines.
2. BODY - one serif family throughout; body 11-13 pt JUSTIFIED (SENIOR-AUDIENCE titles: 13-14 pt body, never below 13 pt - global rule #18); section headings ~14 pt bold on
   a consistent style; panel labels bold at body size. Even spacing between words and lines:
   no rivers of white space, no stretched-out justified lines, no orphan headings, no stray
   fragments separated from their paragraph ("scattered text" is a hard render-QA failure).
3. MARGINS AND CONTAINMENT - a single text block per page (approx. 0.9-1.0 in side margins at
   8.5x11). NOTHING - text, table, rule line, panel border, figure - may cross the margin or
   touch the page edge. The exemplar shows zero violations in 542 pages; that is the bar.
4. TABLES - always inside the live text area, sized to the text block, header row styled,
   consistent cell padding, no overflowing columns, no table split so that a lone header or a
   single row is stranded on a page.
5. VERIFICATION IS MANDATORY - render_qa.py (AGENTS rule #17) must pass on the RENDERED PDF
   before any preview or delivery: margin containment, table containment, and scattered-text
   checks. A book that fails is not presented, not shipped, not published - fixed first.

## HOUSE REFERENCE BANK — TEXTBOOKS AND EDUCATIONAL BOOKS (2026-08-14)

Five catalog masters are banked at `cover_db/_interiors/textbook/` (local
only, never shipped): Advanced Clinical Scenarios in Surgery, ATLS Textbook,
Dental Assisting, Essentials of Periodontal Instrumentation, and Advanced
Principles of Clinical Cardiology. This standard is BINDING FOR EVERY
TEXTBOOK AND EDUCATIONAL BOOK across the catalog (textbook, medical,
study-guide, exam-simulator, reference, user-guide, language and related
education niches), on BOTH engines (Claude and Codex) and on every install.
Where the bank folder is absent (client installs never receive it), the
codified standards below carry the full weight of the reference study.
CONSULT the masters where present: open 2 or 3 and study a body page, a
table page, an imaging/figure page, and the front matter.

Standards verified across the bank:

* SCHOLARLY BODY: Times New Roman 11 to 12 pt, justified, dense substantive
  paragraphs (never thin listy filler); decimal-numbered section headings
  (11.8 style) in bold, hierarchically consistent. The binding 8.5 x 11
  heading law still governs chapter titles (BLOCK LETTERS, 28 pt or larger)
  and subchapter sizes (14 to 18 pt); the masters' smaller chapter heads are
  the retired pattern.
* EVIDENCE / CLINICAL PANELS: tinted callout panels with a colored border
  and a bold colored ALL-CAPS lead-in (the ATLS "EVIDENCE SPOTLIGHT:" form):
  literature-grounded spotlights, key-concept boxes, clinical pearls, safety
  warnings. At least two visually distinct panel families per book.
* TABLES: shaded header row in the book's principal color with white text,
  alternating row tints on longer tables, bold numbered captions (Table C.N
  per chapter); the global margin/caption law governs placement.
* FIGURES AND IMAGING STRIPS: multi-panel labeled figures (the ATLS X-ray
  strip form): each panel carries its own caption bar; annotation arrows and
  labels where they teach; Figure C.N numbering per chapter.
* FRONT MATTER: professional apparatus in the accent color: List of
  Abbreviations with hairline rules, styled TOC, preface; roman folios in
  front matter and the binding pagination law for the body (page 1 at the
  Introduction).
* ONE ACCENT SYSTEM PER BOOK, NO REPEATS: each master runs one distinct
  accent color system (maroon, dark teal, blue, and so on). NO TWO BOOKS
  SHARE THE SAME PATTERN: every new book gets its own palette, panel
  family, table treatment, and figure style within this anatomy
  (No-Two-Books-Alike, operator restated 2026-08-14).
* DENSITY: the older masters occasionally leave large trailing white space;
  that is the retired pattern. The current density laws govern: pages are
  filled, sections carry real content, and render QA verifies the page.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
