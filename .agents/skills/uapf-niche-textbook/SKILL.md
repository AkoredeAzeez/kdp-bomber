---
name: uapf-niche-textbook
description: Academic and professional textbook overlay (OV-TEXT) — invoked by uapf-phase0-router when the title reads as a textbook ("textbook", "fundamentals of", "principles of", "introduction to [academic subject]", "for undergraduates/graduates/professionals") or the format is clearly educational/academic. Also the DEFAULT TEMPLATE for any niche with no dedicated framework.
---

# UAPF Niche: Academic & Professional Textbooks (OV-TEXT)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Textbook-Edition/` (config, validation, phases, and deterministic ops in `genie_textbook.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Textbook Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title is clearly an academic or professional textbook; contains "textbook", "fundamentals of", "principles of", "introduction to [academic subject]", "handbook of [discipline]", "a course in", "essentials of [discipline]", "for [undergraduate/graduate/professional/certification] students/candidates"; names a recognized academic or professional discipline as its core subject; or the format is clearly educational/academic (curriculum-aligned, exam-adjacent, competency-based, professional reference). **OV-TEXT is also the DEFAULT TEMPLATE: any title that matches no dedicated niche overlay is produced under this skill**, with the Discipline Adaptation Engine (below) configured to the closest domain.

Source framework: Universal Textbook Framework (UTF 1.0). This skill is self-contained; a UAPF session must be able to produce a complete, publication-quality textbook from this file alone.

---

## Expert Panel

All perspectives operate silently; the reader sees one consistent authorial voice. No panel credential is ever attributed to the pen name.

1. **Domain Master (Primary Subject Specialist)** — senior educator, researcher, or practitioner in the detected discipline; owns conceptual scope, terminology, notation, current standards, and subject accuracy. Listed first; final authority on all factual disputes.
2. **Subdiscipline / Applied-Practice Specialist** — supplies advanced niche knowledge, real-world constraints, current methods, complex cases, and professional context for the specific subfield (e.g., cardiology inside medicine, geotechnics inside civil engineering).
3. **Curriculum & Learning-Design Specialist** — controls learning progression, cognitive load, prerequisite scaffolding, Bloom-aligned objective writing, assessment validity, accessibility, and transfer.
4. **Visual & Information-Design Director** — fixes every visual point at outline stage, selects the correct modality per figure (photograph, diagram, cutaway, schematic, map, plot, code architecture, source facsimile), writes the image prompts, and verifies captions, labels, and accessibility.
5. **Accuracy, Evidence, Safety & Publishing QA Specialist** — performs fact checks, calculation and code checks, citation verification, safety/ethics sweeps, rights review, accessibility audit, and publication preflight; enforces the no-fabricated-citations rule.

### Discipline Adaptation Engine — Nine Configured Domains

Phase 0 detects the primary domain and swaps the Domain Master and Applied Specialist to match. Each domain carries its own panel emphasis, evidence standard, and risk regime:

| Domain | Domain Master Profile | Evidence / Standards Regime | Risk Regime |
|---|---|---|---|
| **Medical** | Physician-educator / clinical scientist | Current clinical guidelines, GRADE/Oxford CEBM, generic drug names only | HIGH — verify indications, contraindications, doses, guideline dates; never a prescribing authority |
| **STEM** (math, computing, natural sciences) | Research scientist / mathematician / software architect | Reproducibility: recalc every result, test code in named version, verify datasets and axes | MEDIUM — lab safety, security implications, edge cases documented |
| **Business** | Professor of management / practicing analyst | Verified data, dated market claims, calibrated language, no financial advice | MEDIUM — distinguish education from financial/investment advice |
| **Humanities** | Historian / literary scholar / philosopher | Source criticism, primary-source provenance, fair representation of contested interpretation | LOW — rights and cultural sensitivity |
| **Law** | Legal scholar | Precedential authority; jurisdiction, currency date, statute/case verification | HIGH — always state jurisdiction; never legal advice |
| **Engineering** | Practicing licensed engineer + engineering professor | Standards verification (codes, editions, units, tolerances, safety factors) | HIGH — safety-critical; see Engineering Domain Directive below |
| **Education** | Curriculum specialist / learning scientist | Learning-science evidence, curriculum framework alignment | LOW-MEDIUM — safeguarding where minors involved |
| **Arts** | Practicing artist-educator / art historian | Provenance, technique accuracy, rights-cleared cultural material | LOW — rights and attribution |
| **Trade/Vocational** | Master tradesperson / trades instructor | Current codes, competency frameworks, tool and PPE standards | HIGH — hazards, supervision, stop-work conditions, licensing boundaries |

### ENGINEERING DOMAIN DIRECTIVE (operator-mandated, overrides defaults)

When the detected domain is Engineering:

- **NO practice questions, quizzes, exercises, or end-of-chapter problem sets.** The assessment architecture is set to NONE. In place of assessment, every chapter carries **deeper technical exposition**: extended derivations, worked design walkthroughs, failure-mode analysis, standards commentary, and real-world application narratives.
- **Minimum 23 pages per chapter** (not the default 20-30 band floor).
- **Total book target: 400-550 pages.**
- **Every subchapter (every X.Y section) receives one realistic photographic image prompt** — photorealistic engineering subject matter (equipment, structures, materials, job sites, lab setups, components) rendered per the Interior Design and image-prompt rules below. No subchapter ships without its image point.
- Because there is no assessment, the back-matter answer key is omitted; the glossary, appendices (formulas, symbols, standards tables), references, and index remain mandatory.

---

## Phase 0 — Title Analysis

Run in order. Nothing is written until all Phase 0 steps complete and the operator approves the TOC.

### 0.1 Title Clearance Gate (mandatory, first)

1. **Language detection:** identify the dominant language of the exact title, state confidence, lock it for the entire manuscript. English title + no marketplace = American English for Amazon.com. All interface/status/analysis output stays in English regardless of book language.
2. **Marketplace detection:** infer the Amazon marketplace from title language and any operator signal; if language cannot be established, stop and ask only for the target language.
3. **Live title collision search:** search the target Amazon marketplace and open web for the exact title, dominant phrase, word-order variants, and materially similar textbook titles. A matching descriptive title is a discoverability risk to report, not an automatic block.
4. **Live trademark search:** WIPO Global Brand Database as cross-border baseline; USPTO (US), EUIPO/TMview (EU), or national office as appropriate. Search exact wording, dominant elements, variants, stems, translations, phonetic equivalents. Check at least Nice Class 16 (printed books), Class 9 (e-books/digital educational products), Class 41 (education/training/publishing services), plus any class tied to a branded term in the title. Consider famous marks and false-affiliation risk.
5. **Clearance rating:** exactly one of CLEAR / CAUTION / HIGH RISK / UNVERIFIED. Only CLEAR or an explained low-confusion CAUTION proceeds. HIGH RISK: stop, generate 6-10 safer alternatives preserving the concept, re-screen, recommend the strongest. UNVERIFIED is never reported as good to go. This is a publishing-risk screen, not a legal opinion.
6. **Output the Title Clearance Report** (English): Exact Title | Detected Book Language | Confidence | Inferred Marketplace | Collision Result | Registers and Classes Checked | Risk Rating | Good-to-Go Status | Required Revision if any.

### 0.2 Subject Analysis & Domain Detection

1. Identify the primary domain and map it to one of the nine Discipline Adaptation Engine domains (Medical, STEM, Business, Humanities, Law, Engineering, Education, Arts, Trade/Vocational). State the pick and one-line reason. If Engineering, activate the Engineering Domain Directive immediately.
2. Identify subdiscipline/niche (e.g., cardiology, machine learning, constitutional law, automotive technology).
3. Assess theory-to-application balance and scope type: broad survey, curriculum-aligned core text, specialized deep dive, lab/project manual, professional reference, or certification-adjacent text.
4. Calibrate the educational level: school / undergraduate intro / undergraduate advanced / graduate / professional-CE / vocational-technical / self-directed public learner. Lock reading level, prerequisites, mathematical demand, and depth.
5. Map content scope: the essential concepts, methods, standards, cases, procedures, or competencies that MUST be covered; the current curriculum, accreditation, certification, or licensing frameworks relevant to the level and marketplace; how time-sensitive claims will be sourced and dated.
6. Market positioning: assess leading and indie textbooks in the category for coverage, pedagogy, visual design, and complaints; identify the differentiation strategy (worked problems, visual learning, project-based, case-based, standards-current, professional application) that this title will truthfully claim.

### 0.3 Subtitle Generation

Generate 6-8 KDP-compliant subtitle options in the book language. For each: complete title+subtitle, combined character count (must be under 200), keywords targeted, target audience, category fit, market differentiation, collision note, trademark status, compliance line. Formats to draw from:

- "Master [Subject] through [Distinctive Approach] for [Target Learner]"
- "Complete Guide to [Topic] with [Worked Problems/Projects/Cases] for [Target Learner]"
- "[Discipline] [Subject]: From [Foundation] to [Application] for [Target Audience]"
- "Learn [Skill] from [Foundation] to [Practice] with [Projects/Examples]"

No misleading claims, guaranteed outcomes, fabricated credentials, false affiliations, keyword stuffing, or exam-name/brand use unless accurate, central, and non-affiliative. Conclude in English with one recommended option and rationale.

### 0.4 Auto-Configuration (no interrogation of the operator)

Select and state, with one-line reasons:

1. **Target audience** (locked from 0.2).
2. **Visual level:** MINIMAL (5-10) / MODERATE (15-25) / ABUNDANT (30-50) / EXTENSIVE (60+), plus the modality mix. Engineering domain: effectively EXTENSIVE, since every subchapter carries a photographic image point.
3. **Reference approach:** original research-informed synthesis by default; uploaded sources are used for coverage and verification only — arrangement, examples, pedagogy, and design come exclusively from this book's locked identity.
4. **Assessment architecture:** what the title and level require — retrieval questions, worked problems, end-of-section exercises, projects, labs, case analyses, or exam-style practice — all original items with complete verified solutions/rubrics. **Engineering domain: NONE (operator directive).**
5. **Supplementary materials:** only title-relevant back matter (glossary, symbol list, formula sheet, standards crosswalk, answer key, data tables, timeline, reference tables).

Also lock silently: the two-color scheme (see Interior Design — collision-check the pairing against the catalog; no two books share the same primary+accent pairing), feature-box set and custom names, chapter-opening style, section-flow pattern, heading treatment, and caption style. Rotate all of these across the catalog — no two books may share the same full structural and visual signature.

**Pen name:** generate 3-5 candidate fictional pen names in First M. Last form, no titles or honorifics ever (no Dr., Prof., MD, PhD), matched in tone to the discipline and book language, never reused across the catalog, screened for obvious Amazon author-name collisions where live access exists (otherwise marked UNVERIFIED).

### 0.5 TOC Lock & Gate

Present: configuration summary, recommended subtitle, pen-name candidates, and the complete locked Table of Contents (chapter + subchapter hierarchy, per-chapter planned image counts and teaching moments, per-chapter page targets, closing-section plan). Then stop at the Phase 0 gate per standard UAPF gate protocol. Nothing is generated until the gate clears.

---

## Book Architecture

### Chapter Formula (the structural unit)

Every chapter follows this skeleton, fleshed to the locked identity:

1. **Chapter opener (500-750 words, flowing prose):** opens in the locked style (authentic scenario, provocative question, phenomenon/data/artifact, historical entry, misconception correction, or design brief). No bullet lists in narrative.
2. **Learning Objectives box** (see Interior Design for the visual spec): 3-5 objectives, each **Bloom-aligned and measurable** — begin with an observable verb at the correct Bloom tier for the level (define/describe → apply/calculate/analyze → design/evaluate/synthesize), never "understand" or "know". Every objective must be **assessment-traced**: at least one end-of-chapter item, worked example, or (Engineering) exposition section demonstrably exercises it. In the Engineering domain, each objective traces to a specific exposition or worked-design section instead of an assessment item.
3. **3-5 major numbered sections (X.1, X.2, …):** each opens by establishing its purpose, teaches in original flowing prose with concrete newly created examples, includes worked examples with step-by-step reasoning, and closes with a short narrative synthesis. Section flow follows the locked pattern (foundation→model→application, problem→method→solution, theory→worked example→practice, etc.).
4. **Feature boxes:** the 3-5 devices locked at Phase 0 under book-specific custom names (e.g., worked example, safety alert, evidence check, misconception, method note, design challenge, code lab, professional tip, ethics lens, historical context, exam strategy). Deploy consistently at their planned frequency; 1-2 fully fictional, privacy-safe applied case studies per chapter.
5. **Visuals at fixed points:** every planned figure lands at its exact teaching point, preceded by at least one orienting paragraph, referenced by number in adjacent prose, captioned beneath. No two figures back-to-back without intervening prose. Engineering: one realistic photographic image point per subchapter, minimum.
6. **Assessment block** (where the assessment architecture calls for it): original questions/problems/cases matched to the learning objectives, with numbering that supports the back-matter answer key. **Omitted entirely in the Engineering domain**, replaced by extended technical exposition.
7. **Chapter close (500-750 words, flowing narrative):** consolidation in the locked style (key-point synthesis, worked integration, case resolution, concept map, or practice set) plus a narrative bridge to the next chapter.

### Page Bands

| Configuration | Per chapter | Chapters | Total book |
|---|---|---|---|
| Default textbook | 20-30 pages incl. visuals | 10-20 | 250-450 pages |
| **Engineering domain** | **min 23 pages** | 14-20 | **400-550 pages** |
| Compact professional reference | 15-22 pages | 10-14 | 200-300 pages |

### Front Matter (in order; lowercase roman numerals)

1. Title page — title, subtitle, pen-name byline (First M. Last, middle initial preserved), edition; composition follows the locked design identity.
2. Copyright page — notice, edition/printing, ISBN placeholder, AI-disclosure status where required, and the **discipline-adapted educational/liability disclaimer** (core text below, extended with the domain's risk language: medical, engineering, legal, financial, laboratory, workshop, fieldwork as applicable).
3. Table of Contents (linked) — lists Preface first, then every chapter heading with its meaningful subheadings (1.1, 1.2 …) and the actual closing sections used. Print page numbers must match the laid-out pages; eBooks use linked navigation.
4. List of Figures and List of Tables (recommended for image-rich texts); List of Abbreviations and Acronyms (strongly recommended).
5. Preface / How to Use This Book — audience, prerequisites, scope, conventions, pedagogy, assessment system, visual conventions, edition date, curriculum/professional alignment. Begins arabic page 1.

Disclaimer core (adapt per domain): educational/informational purposes only; not a substitute for qualified professional instruction, advice, supervision, certification, or jurisdiction-specific requirements; content is general and time-sensitive; readers must independently verify safety-critical facts, calculations, procedures, codes, and legal/financial information against current primary sources; author and publisher disclaim liability arising from use.

### Back Matter (in order)

1. Appendices appropriate to the title: formulas, symbols, standards/data tables, lab or field references, code listings, timelines, maps, reference tables.
2. **Complete answer key / worked solutions** for every assessment item in the book — mandatory wherever assessment exists (i.e., every domain except Engineering, which has no assessment). Solutions are worked, not answer-letters-only, and numbered to match the chapters.
3. **Glossary** — discipline-specific, mandatory, alphabetized, defined in original language at the book's reading level.
4. References / Bibliography — one consistent citation style (APA, Chicago, MLA, Harvard, IEEE, AMA, or Vancouver as fits the discipline); every entry real, complete, and verified.
5. Index (print).
6. About the Author — pen name, educational-author framing, zero fabricated credentials, degrees, licenses, affiliations, or awards.

---

## Interior Design

OV-TEXT specifies its own interior (overrides UAPF default):

- **Trim size: 8.5 x 11 in.** Margins: **0.7 in all around** (respect KDP gutter minimums at high page counts — if page count pushes the required gutter above 0.7", widen the inside margin only).
- **Typeface: Times New Roman throughout** — body, headings, captions, boxes, tables. Differentiation comes from size, weight, and color, never from font changes.
- **Two-color scheme:** one PRIMARY color and one ACCENT color, locked at Phase 0. **No two books in the catalog may share the same primary+accent pairing** — collision-check against the catalog log before locking. All color use in the book draws only from these two colors plus black text and white ground.
- **Body text:** 11-12 pt, **justified**, black. No em dashes anywhere in the content (use commas, colons, parentheses, or separate sentences). Natural flowing paragraphs; no bullet lists inside explanatory narrative.
- **Numbered section headings (X.Y form) set in bold ACCENT color.** Chapter titles larger (approx. 18-22 pt bold), styled per the locked identity in PRIMARY or ACCENT.
- **Learning Objectives box:** opens every chapter — a box filled with a light tint of the PRIMARY color, with a solid PRIMARY border, "Learning Objectives" heading in bold PRIMARY, objectives listed inside. This is the one sanctioned list structure in the chapter opening.
- **Tables:** header row filled with a light ACCENT tint, bold header text; clear units; linear, eBook-safe geometry (no nested tables or complex merged cells); notes outside the grid; source credit where required.
- **Feature boxes:** tinted or ruled using the two-color scheme, visually distinct from the Learning Objectives box, consistent throughout the title.
- **Figures:** pure white background (#FFFFFF) for diagrams, technical plates, and cutouts; consistent placed widths; caption beneath every figure ("Figure C.N: short headline", sentence case, max two lines, names — never describes — the figure); every figure referenced at least once in prose ("as shown in Figure 4.2"). File naming Fig_CC_NN.png. Dark-panel exceptions (X-ray/CT/MRI, dark UIs) sit inside a white margin on the white page.
- **Image prompts (when images are produced by prompt rather than inline generation):** each is a complete production-ready specification: educational framing line, exact subject with required/excluded elements, counts and laterality, verbatim quoted labels (8-12 max) with leader lines, modality and locked style signature, quality block, exclusions (no watermarks, logos, invented text, identifiable people). Engineering subchapter images are **realistic photographic** prompts: true materials, lighting, depth, scale, correct PPE, safe practice depicted — never unsafe shortcuts.
- **Page numbers:** footer; front matter in lowercase roman numerals; Preface begins arabic 1 and runs consecutively. Title page, copyright page, and TOC carry no visible number.
- **Print prep:** generate/export images at maximum resolution; 2x upscale to reach 300 DPI at placed size; verify white backgrounds read RGB 255/255/255. Never put DPI claims inside generation prompts (models output pixels, not DPI).
- eBook edition: reflowable with linked NCX/HTML TOC, no manual page numbers, lists and index as linked navigation.

---

## Content Rules

**The fatal flaw to avoid: a confidently wrong textbook.** A textbook's entire value is trustworthy accuracy. One fabricated citation, wrong equation, outdated standard presented as current, or mislabeled figure poisons the whole product and is a release-blocking failure — worse than any stylistic defect.

Hard constraints:

1. **Zero fabricated citations.** Never invent an author, title, journal, DOI, URL, statute, case number, standard number, dataset, ISBN, or quotation. If a source cannot be verified: attribute to general consensus in the text with no citation, or insert a clearly marked "Citation to Verify" placeholder. Maintain a Citations-to-Verify ledger across the build.
2. **Transformation, never transcription.** Concepts may transfer from sources; wording, examples, problems, cases, tables, figures, and structure may not. Read, close the source, write from understanding in new language, create new examples, then re-verify accuracy.
3. **Every quantitative element verified:** recalculate every worked example, check units and dimensional consistency (SI default with discipline-expected alternatives), verify significant figures, test code in the named language/version, verify every table value and chart against its data.
4. **Standards attributed and dated:** every law, code, guideline, classification, or specification names its issuing body, edition/version, jurisdiction, and effective date. Time-sensitive claims carry currency dates.
5. **Domain risk regimes enforced** (per the Discipline Adaptation Engine table): generic drug names in Medical; jurisdiction statements in Law; standards editions and safety factors in Engineering; PPE, hazards, and stop-work conditions in Trade/Vocational; education-not-advice boundaries in Business, Law, Medical.
6. **All people-centered cases fully fictional or de-identified** — never invented real testimony, real patients, real litigants, or fabricated provenance.
7. **Bloom-aligned, measurable, assessment-traced learning objectives** in every chapter (see Book Architecture). Objectives that nothing in the chapter exercises are a QA failure.
8. **Assessment originality:** every question, problem, and case is newly created — never copied or paraphrased from question banks or competitor texts — with complete worked solutions in the back-matter answer key. Engineering domain: no assessment at all (operator directive); the depth budget goes to exposition.
9. **Calibrated language:** distinguish fact, interpretation, hypothesis, convention, and contested claim; no guaranteed outcomes; state uncertainty and competing schools of thought fairly.
10. **Accessibility:** colorblind-safe encodings, color never the sole carrier of meaning, alt text for every figure, accessible table headers, readable contrast in both tint boxes.
11. **Language lock:** manuscript in the language detected from the title (regional standard from the marketplace); all operator-facing status output in English.
12. **No em dashes anywhere in manuscript content.**

---

## QA Checklist

### Gate 1 — Post-Phase 0 (before any writing)

- [ ] Title Clearance Report issued; rating CLEAR or explained CAUTION
- [ ] Domain detected and mapped to one of the nine engine domains; panel configured; Engineering Directive activated if applicable
- [ ] Subtitle locked, under 200 combined characters, compliance-checked
- [ ] Audience, visual level, reference approach, assessment architecture, supplementary materials all locked with reasons
- [ ] Two-color pairing locked and collision-checked against catalog (unique primary+accent)
- [ ] Structural signature (opener style, section flow, feature-box names, close style) locked and rotated vs. prior titles
- [ ] Pen name selected: First M. Last, no honorifics, not reused, collision-screened
- [ ] TOC complete: every chapter with subheadings, per-chapter image plan and page target; Engineering: min 23 pp/chapter and 400-550 total confirmed arithmetically
- [ ] Phase 0 gate passed per UAPF gate protocol

### Gate 2 — Per Chapter (every chapter, before merge)

- [ ] Opens in the locked opener style; 500-750 word opening; no narrative bullet lists
- [ ] Learning Objectives box present, styled to spec (PRIMARY tint + border); 3-5 objectives, Bloom-verb, measurable, each traced to an assessment item or (Engineering) exposition section
- [ ] Section headings numbered X.Y, bold ACCENT color, Times New Roman
- [ ] All planned figures present at their exact points; none skipped, deferred, or silently downgraded; captions beneath, max two lines, referenced in prose; white backgrounds verified
- [ ] Engineering: every subchapter has its realistic photographic image (or complete production prompt), chapter is 23+ pages, NO practice questions anywhere
- [ ] Non-Engineering: assessment items original, objective-mapped, numbered for the answer key
- [ ] Every calculation recalculated; every value, unit, and conversion checked; code tested where execution is claimed
- [ ] Standards/guidelines cited with issuing body, edition, date; domain risk regime language present where required
- [ ] All cases fictional/de-identified; no copied prose, examples, or structures; no em dashes
- [ ] Feature boxes used per plan, under this book's custom names
- [ ] Close in the locked style with narrative bridge; chapter appended once to the cumulative manuscript, never regenerated

### Gate 3 — Manuscript Complete (before formatting freeze)

- [ ] Front matter complete and ordered; roman/arabic numbering correct; TOC page numbers match layout
- [ ] Discipline-adapted disclaimer on copyright page, extended with domain risk language
- [ ] Back matter complete: appendices; **answer key with worked solutions covering 100% of assessment items** (where assessment exists); glossary; verified references in one consistent style; index; About the Author with no fabricated credentials
- [ ] Citations-to-Verify ledger resolved or explicitly surfaced to the operator
- [ ] Objective-to-assessment trace audit passes book-wide
- [ ] Structural conformance: no drift from the locked signature across chapters; figure numbering continuous per chapter; list of figures/tables matches actuals
- [ ] Total page count in band (Engineering: 400-550)
- [ ] Two-color discipline held: no third color anywhere; heading/box/table tints correct

### Gate 4 — Release (uapf-release-qc)

- [ ] PDF preflight: 8.5x11, 0.7" margins (plus gutter), fonts embedded, images 300 DPI at placed size, whites read 255/255/255
- [ ] eBook: linked TOC/NCX, no manual page numbers, tables reflow-safe
- [ ] Metadata (title/subtitle/author) exactly matches cover and interior title page; under 200 characters; category and keywords accurate
- [ ] AI-disclosure status recorded per KDP policy; rights review clean (no logos, trade dress, copyrighted figures, real-person likenesses)
- [ ] Final read of high-risk passages (medical/legal/engineering/financial) against the domain regime
- [ ] Catalog log updated: title, pen name, color pairing, structural signature, marketplace, language

---

## KDP Positioning

- **Category tree:** Education & Teaching > Schools & Teaching / Studying & Workbooks, or the discipline's own tree — Medical Books > [specialty]; Engineering & Transportation > Engineering > [branch]; Business & Money > [subject]; Law > [subject]; Science & Math > [subject]; Computers & Technology > [subject] — chosen to match the actual discipline and level, never manipulated. Prefer the deepest accurate node.
- **Description leads with** the learning promise and audience: what the reader will be able to do, at what level, via what pedagogy ("clear explanations, worked examples, and complete solutions" / for Engineering: "in-depth technical exposition, real-world design walkthroughs, and standards-current practice"). Then coverage highlights (chapter-level), then the supporting apparatus (objectives, glossary, answer key, figures), then the audience line (course students, certification candidates, practitioners, self-learners).
- **Metadata signals:** level keywords (undergraduate, graduate, professional, certification prep, self-study), subdiscipline terms real learners search, truthful apparatus claims (worked examples, practice problems with solutions, illustrated). Exam, curriculum, and software names only when accurate, central, and non-affiliative. No superlatives the content cannot support.
- 7 backend keywords: subject + level + apparatus + synonym variants; no repetition of title words, no competitor names, no brand terms.

---

## Key Rules — Do NOT Break

1. **Title Clearance Gate runs first, always.** No subtitle, TOC, or prose before a CLEAR or explained-CAUTION rating.
2. **Discipline Adaptation Engine is mandatory:** detect one of the nine domains, configure the panel and risk regime to it, and state the detection before configuration.
3. **Engineering domain: NO practice questions of any kind** (operator directive). Deeper technical exposition instead; minimum 23 pages per chapter; 400-550 total pages; a realistic photographic image (or complete production prompt) in every subchapter.
4. **Never fabricate a citation, source, credential, or quotation.** Unverifiable claims get consensus attribution or a flagged placeholder — never an invented reference.
5. **Interior is locked:** 8.5x11 trim, 0.7" margins, Times New Roman throughout, justified body, numbered section headings in bold ACCENT, Learning Objectives box in PRIMARY tint with PRIMARY border, accent-tinted table headers, strictly two colors — and **no two books in the catalog share the same primary+accent pairing**.
6. **Learning objectives are Bloom-aligned, measurable, and assessment-traced** in every chapter; "understand" and "know" are banned objective verbs.
7. **Where assessment exists, the back matter carries a complete worked answer key covering every item, plus a glossary.** A book with questions and no solutions does not ship.
8. **Transformation law:** concepts may transfer from sources; words, examples, problems, cases, figures, and structure may not. Arrangement belongs to this book's locked identity, never to a source.
9. **Every planned visual lands at its exact teaching point** — captioned beneath (two-line headline max), referenced in prose, white-background (or sanctioned dark-panel-in-white-margin), never skipped or falsely reported as complete.
10. **All quantitative content is independently verified:** recalculated math, tested code, checked units, dated standards with issuing body and edition.
11. **Pen name is First M. Last, fictional, honorific-free, never reused; the bio never claims credentials.** Panel expertise is never attributed to the pen name.
12. **Structural and visual signatures rotate across the catalog** — no two books share the same full combination of opener style, section flow, feature-box names, close style, and color pairing.
13. **No em dashes anywhere in manuscript content; no bullet lists inside explanatory narrative; body text justified; manuscript in the title's detected language; all operator-facing output in English.**
14. **As the default template:** when a title reaches this skill with no dedicated framework, run it exactly as above, mapping it to the nearest of the nine domains and inheriting that domain's panel, evidence standard, and risk regime.

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
