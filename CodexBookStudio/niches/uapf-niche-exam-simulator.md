---
name: uapf-niche-exam-simulator
description: Exam simulator and practice question bank overlay (OV-EXSIM) — invoked by uapf-phase0-router when routing signals identify a title whose primary deliverable is a timed simulation bank rather than instructional chapters
---

# UAPF Niche: Exam Simulator and Practice Question Bank (OV-EXSIM)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/USGPF-2.9/` (config, validation, phases, and deterministic ops in `genie_exam_simulator.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=USGPF 2.9` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title or supplied context contains any of the following signals: question bank, practice exam, 500 questions, 600 questions, 750 questions, 1000 practice questions, full practice test, exam simulator, mock exam, practice test bank, simulated exam, timed practice sets, or any numeric quantity joined with "practice questions" or "practice tests" as the primary content promise of the title — and the content is NOT primarily instructional chapters with assessment as a supplement (that routes OV-STUDY).

---

## Expert Panel

**Domain Master — Subject Matter Expert and Certified Practitioner** (listed first; non-negotiable)
The Domain Master holds active or recent standing in the certification or licensure the book targets. All items, distractors, and rationales are reviewed by this expert before any set clears Gate 2. No item enters the bank without Domain Master sign-off on accuracy and on the single defensible correct answer.

**Exam Analyst — Examination Psychometrician**
Specialist in item construction, test blueprints, and the administered format of the target examination. Owns the Exam Format Evidence record, the bank blueprint type-mix, the run-cap settings, and the Score Interpretation Guide. Reviews the engine's answer-pattern audit results and approves the randomized sequence for each set.

**Instructional Designer — Assessment and Certification Specialist**
Designs the orientation section, the set pacing guidance, the timed-simulation instructions, and the score-interpretation rubric. Ensures that rationale paragraphs teach the principle rather than merely naming the key. Confirms that difficulty distribution within each set and across the full bank reflects the researched blueprint weighting.

**Compliance and Rights Editor**
Audits every item for the universal prohibitions: no verbatim content from secured or leaked actual exam items, no invented statistics or regulations, no pass-probability language in the Score Interpretation Guide, no trademark infringement, and no positional language that would create a shuffle pin. Runs the compliance sweep (em dashes, en dashes, apostrophes, AI voice) on every set.

**Technical Production Editor**
Owns the DOCX build: two-column layout integrity for both divisions, literal numbering compliance, answer-form consistency, column balance, folio accuracy, and zero direct-formatting drift. Runs the Answer Pattern Audit against the built file for every set and at Final QA.

---

## Phase 0 — Title Analysis

**Step 1 — Intake and Signal Verification**
Receive the title and the operator-supplied total question count. The total is the single operator-controlled setting for this niche; if it did not arrive with the title, request it as the only outstanding input before any other configuration proceeds. Confirm that the routing signals identified above are present in the title or supplied context and record the routing decision as OV-EXSIM with its evidence.

**Step 2 — Title Trademark Clearance (runs before any other output)**
Immediately on intake, scan the proposed title and every subtitle candidate live against the federal trademark register and the target marketplace. Record the Title Clearance record with sources and date. A clean result confirms the title is good to go. A conflict holds the title and is reported with sources; the Title Verbatim Law (module 2.10 of USGPF 2.9) governs: the system never alters the supplied title, never proposes a substitute, and the run holds for the operator's decision. Examination and certification names owned by administering bodies are used nominatively only; the Copyright page carries the non-affiliation statement required by module 2.7 naming the mark owner and disclaiming sponsorship, affiliation, and endorsement.

**Step 3 — Children's Category Research**
Research the title live for children's audience signals. If signals are present, the title routes OV-KIDS, not OV-EXSIM, and this skill yields to the children's overlay. Record the Children's Category record with sources and research date regardless of outcome.

**Step 4 — Exam Format Research (mandatory; blocks generation)**
This is the most critical Phase 0 step for OV-EXSIM. Before composing a single item, before drafting the bank blueprint, before generating subtitle candidates: run live web research on the named examination. Identify: the administering body or vendor; the question formats actually administered (single-best-answer, select-all-that-apply, ordered response, numeric entry, exhibit/drag-and-drop, scenario-based); the option count; the presence of multi-response types; any sectioning or time-limit structure; the topic domains and their blueprint weighting; the difficulty and reasoning style of official preparation materials. Record all findings, sources, and the research date in the Exam Format Evidence record. The evidence governs the profile and the bank blueprint; library profiles are starting benchmarks only, never substitutes for the research. If the examination is proprietary and undisclosed or the web is unreachable, apply the conservative four-option single-best-answer family profile, record the uncertainty, and do not allow any unverified format claim to enter reader-facing text.

**Step 5 — Language Detection and Profile Card**
Detect the language of the title. Lock the content language and regional variant for the entire manuscript in the Language Profile Card. American English governs when the card is United States English.

**Step 6 — Subtitle Composition**
Compose subtitle candidates under the Subtitle Composition Law (module 2.11 of USGPF 2.9): the subtitle states the total practice question count together with the words Practice Questions drawn from the operator-supplied total (e.g., "1000 Practice Questions"); the stated count must equal the configured total exactly; the subtitle contains letters, numerals, and spaces only; and the subtitle renders on the title page in no more than two lines at the locked subtitle size. Auto-select and lock the winner.

**Step 7 — Byline**
Fetch the Fake Name Generator service live. Format as First Name, Initial, period, Surname. Run the collision and impersonation check. Lock the byline with source, check result, and date. No credentials, affiliations, or invented biography attach to the pen name.

**Step 8 — Title Design Signature**
Compose the title's complete palette, heading accent treatment, box border treatment, table styling variant, title page arrangement, and figure style direction. Check against the Catalog Design Register for distinctness: no hex value repeats a registered palette, the primary hue stands perceptibly apart from every registered primary, and at least two non-color axes differ from the nearest registered title. Failing signatures regenerate until the gate clears.

**Step 9 — Assessment Plan**
Derive from the operator-supplied total under the locked profile's type mix: the set count, the questions per set, the per-set type distribution, the full-width item placements, the content-fixed pattern assignments (authored in at blueprint time), and the mapping of sets to topic domains in proportion to the researched blueprint weighting. Set the randomization seed and record it.

**Step 10 — Auto Configuration Package**
Record all outputs above: routed overlay (OV-EXSIM); Children's Category record; Exam Format Evidence record; Title Clearance record; Language Profile Card; Title Design Signature with catalog-distinctness result; locked profile identifier; subtitle winner; byline record; Format Specification Record; assessment plan with set-to-domain mapping; randomization seed; Delivery Mode record (RENDER on image-capable host, PROMPTS ONLY on prompt-only host); risk regime. Close the Package by asking whether to proceed with the bank blueprint, end with the exact standalone line: Type to proceed. Stop. Production begins only after a fresh Proceed.

---

## Book Architecture

**Front Matter (brief; OV-EXSIM override: orientation replaces instructional chapters)**

| Section | Purpose | Length |
|---|---|---|
| Title Page | Verbatim title, subtitle with question count, byline | 1 page |
| Copyright and Disclaimer | Non-affiliation statement naming exam owner; standard disclaimers; trademark ownership line | 1 page |
| Table of Contents | Native Word TOC field; levels 1 and 2; simulation sets and answer key sets both entered | 1 page |
| How to Use This Book | Brief orientation: exam format summary, timed-simulation instructions, score tracking, mark-and-return strategy, answer-key navigation | 1.5 pages (1.40 to 1.55 accepted band) |

**Body: Timed Simulation Sets**

The body of an OV-EXSIM title is the PRACTICE QUESTIONS division only; there are no instructional learning chapters. The structure follows the consolidated model of USGPF 2.9 Part VII and USGPF-Q Part IV:

- Division head: PRACTICE QUESTIONS (Heading 1, new page)
- Set subheads: Practice Exam 1 ... Practice Exam N (Heading 2; continuous, never new-page), each carrying its item range instruction in the Instr style
- Two-column layout for all standard item types (Part VII column geometry: two equal columns, 576 DXA separation, separator rule on)
- Full-width layout for scenario-based and exhibit items that cannot render in a column (continuous break before and after)
- Items numbered continuously 1 through the operator-supplied total across all sets; no restart at set boundaries (USGPF-Q Literal Numbering Law, module 3.4)
- Timing guidance line in the Instr style after each set subhead: item range, single-best-answer or profile-required instruction, and a suggested time budget derived from the researched exam's total time divided by item count

**Back Matter**

| Section | Purpose |
|---|---|
| ANSWERS AND EXPLANATIONS | Mirror of every Practice Exam N set; two-column layout; every item keyed with full distractor rationales |
| SCORE INTERPRETATION GUIDE | Descriptive performance bands; study strategy for each band; no pass-probability claims |
| APPENDIX A: Exam Blueprint Summary | Topic domains and their approximate weighting from the Exam Format Evidence record; sourced; disclaimed as subject to change |
| APPENDIX B: Time-Per-Question Budget | Calculation from the researched time limit and item count; pacing strategies |

**Sequence (full manuscript order)**
Title page; Copyright and Disclaimer; Table of Contents; How to Use This Book; PRACTICE QUESTIONS; ANSWERS AND EXPLANATIONS; SCORE INTERPRETATION GUIDE; APPENDIX A; APPENDIX B.

**Page-Band Targets**
How to Use This Book: 1.40 to 1.55 pages. Score Interpretation Guide: 1.40 to 1.55 pages. Practice Exam sets and Answer and Explanation groups: sized by item count and column fill; no artificial length padding. Total manuscript length emerges from the question count; do not target a page total by any means other than content.

---

## Interior Design

**Page Geometry:** Inherits UAPF default. Trim 8.5 by 11 inches. Margins 0.8 inch all four sides. Footer distance 0.6 inch. No running heads.

**Body Typography:** Times New Roman 11pt, 1.15 line spacing throughout. Assessment paragraph styles (QStem, QOpt, AnsNum, AnsExpl) are left-aligned; all other prose is fully justified. No text falls below 11pt in reader-facing content; 10pt is permitted only inside non-reader-facing scaffolding (image prompt specification lines).

**Color Tier:** PREMIUM COLOR, WHITE paper, for every print interior. Grayscale requires an explicit recorded operator override.

**Palette:** Title-specific under the Catalog Variation Law; no hex value repeats a registered palette. The Title Design Signature clears the distinctness gate before the Format Specification Record locks.

**Column Layout:** Both PRACTICE QUESTIONS and ANSWERS AND EXPLANATIONS render in two equal columns (the Two Column Law, USGPF-Q module 4.1). Column width 4680 DXA, separation 576 DXA, separator rule on.

**Table and Box Styling:** Inherits UAPF default (header row primary fill, white bold labels; alternating body rows; 0.5pt borders; cell padding 100 vertical 160 horizontal; all tables flush to 9936 DXA text width).

**Folio:** Visible page numbering begins at How to Use This Book as Arabic page 1; front matter (title page and copyright) carries no visible folio. Folio is always a live native page number field, never typed text.

---

## Content Rules

**Item Originality and Format Compliance**
Every item is original work. No actual administered examination item is sought, reproduced, or imitated item-for-item. Verbatim content from any source identified as a leaked or secured exam item is absolutely prohibited regardless of how it arrives. Every item is written to the researched format from the Exam Format Evidence record: option count, type mix, topic domain, difficulty register, and reasoning style match the evidence.

**The Single Defensible Correct Answer Rule**
Every standard item carries exactly one single defensible correct answer. The Domain Master confirms defensibility for every item before it enters the bank. An item with two arguable correct answers is a defect and is rewritten; "most correct" or "best of these" wording is used only when the researched exam genuinely uses that convention, and even then one option must be unambiguously superior by the rationale's evidence.

**Distractor Quality and Rationale Completeness**
Every rationale must address every distractor — not only state why the key is correct, but explain why each incorrect option is wrong. Distractors are drawn from real misconceptions, adjacent facts, and plausible near-misses in the subject domain; absurd throwaway options are defects. Rationale length: 50 words or fewer per entry. Content-based language only: rationales never reference option letters (positional language creates shuffle pins and flags the engine).

**No Pass-Probability Claims**
The Score Interpretation Guide describes performance bands in descriptive terms (e.g., "items in this range suggest mastery of domain X; review domain Y") and recommends study strategies. It does not predict pass/fail probability, percentage likelihood of passing the real exam, or any quantified equivalence between a score on this book's practice sets and a score on the actual administered examination. Those claims constitute unverifiable invented statistics under the universal prohibition.

**Timed-Simulation Fidelity**
Each Practice Exam set is formatted as a self-contained timed simulation: the Instr style line after the set subhead states the item range, the instruction convention used by the actual exam (e.g., "Choose the single best answer for each question"), and the suggested time budget. The item sequence within each set reflects the type mix and difficulty distribution of the researched exam blueprint; sets are not ordered easy-to-hard unless the researched exam format dictates it.

**Exhibit Items (Minimalism Law)**
An exhibit item is included only when the question genuinely cannot be tested without the figure — when the candidate must read a dimension, trace a pathway, interpret a depicted arrangement, or parse data that words cannot carry. An exhibit that merely illustrates what the stem already states is a defect and is removed. Every exhibit position is declared and justified in the bank blueprint. Diagram dimension labels use neutral letters (X, Y) and never A through D.

**Score Interpretation Guide Architecture**
Organize by performance band. For each band: the approximate score range as a fraction or percentage of the total item count; a descriptive label (e.g., strong command, developing command, foundational review needed); the topic domains where items are concentrated; and a study strategy recommendation pointing to specific appendices or external resources. Never: numeric pass-probability, cutoff-score equivalence, or any claim that a specific score predicts real-exam outcome.

**Content Standards Rule**
The catalog-wide content standards rule holds in every stem, option, explanation, scenario, and exhibit: no pork or pig derivatives, no alcohol in any form, no alcohol-centric scenarios, anywhere, including image content.

**Compliance Sweep (all reader-facing text)**
Zero em dashes; zero en dashes (ranges written with "to"); every apostrophe is the right single curly quotation mark; no AI voice phrasing; no meta-references to the production process; spelling and conventions follow the Language Profile Card.

---

## QA Checklist

**Gate 1 — Configuration and Bank Blueprint**
- [ ] OV-EXSIM routing signals confirmed and recorded
- [ ] Children's Category Research completed, record stored
- [ ] Exam Format Evidence record exists with live sources dated to this engagement
- [ ] Title Clearance record exists with sources and date
- [ ] Non-affiliation statement drafted for Copyright page naming the exam owner
- [ ] Language Profile Card locked
- [ ] Subtitle compliant: correct count, letters/numerals/spaces only, fits two lines
- [ ] Byline fetched live from FNG, collision check passed, locked
- [ ] Title Design Signature cleared distinctness gate
- [ ] Assessment plan complete: set count, questions per set, type distribution, domain mapping, content-fixed patterns assigned, randomization seed recorded
- [ ] Package closed; Proceed gate active
- [ ] Research Before Generation gate verified: Exam Format Evidence record exists, carries live sources, is cited by the profile and the plan; not one item or stem is written before this check passes
- [ ] Sets mapped to topic domains with blueprint-proportional weighting
- [ ] Per-set type distribution written from the researched formats
- [ ] Content-fixed correct-answer patterns authored in at blueprint time (before items are written)
- [ ] Exhibit positions listed: every position declared and justified under Exhibit Minimalism Law; default is zero
- [ ] Domain Master has reviewed blueprint coverage for completeness and accuracy
- [ ] Proceed gate active

**Gate 2 — Per-Set Format and Content Audit (runs after every set)**
- [ ] Stem Quality: every stem is a complete, self-contained question or statement; no double negatives; no trick constructions
- [ ] Distractor Quality: distractors are plausible, mutually exclusive, parallel in grammar and length to the key; no absurd throwaway options
- [ ] Single Defensible Correct Answer: Domain Master confirmation recorded for every item in the set
- [ ] Positional Language Absent: no "all of the above," "none of the above," option-letter references in stems or options (or pinning status recorded if unavoidable)
- [ ] Rationale Completeness: every rationale addresses every distractor; 50 words or fewer; content-based (no letter references)
- [ ] Exhibit Declarations: every declared exhibit embedded; no undeclared exhibit present
- [ ] Column Layout: two equal columns, separator rule, set subhead full-width
- [ ] Literal Numbering: question numbers and option letters are typed text in exact number-period-space and letter-period-space forms; no Word list auto-numbering on any assessment paragraph; numbering continuous from prior set
- [ ] Answer Form: AnsNum in number-period-space-Answer-colon-space-letter-closing-paren-space-option-text form; AnsExpl indented, Explanation-colon-space-reasoning
- [ ] Compliance Sweep PASS: em dashes absent, en dashes absent, curly apostrophes only, no AI voice
- [ ] Content Standards Check PASS
- [ ] Amazon Content Policy Scan PASS
- [ ] Answer Pattern Audit PASS (run against the built file): question count equals answer count; numbering continuous without gaps or duplicates; every standard item carries exactly the profile's option count; every answer entry matches the required form; distribution within tolerance; max run within effective cap; no doubled permutation or tripled alternation; explanation word counts within 50
- [ ] Rendered inspection: set pages rasterized and inspected; column balance, folio, margin alignment verified
- [ ] Proceed gate active

**Gate 3 — Randomization Engine and Answers Division**
- [ ] Engine run on the complete bank from the recorded seed
- [ ] Integrity check: text at each new key equals text at original key; option multisets match for every item
- [ ] Engine report delivered per set: before/after distributions, before/after max runs, items moved, pinned items listed, explanation flags listed, effective run cap and whether it was auto-raised, final sequence, multi-response inclusion counts
- [ ] Answer Pattern Audit re-run on the randomized output: PASS
- [ ] Two Option Law verified: any profile with a two-option in-sequence type carries run cap of at least 2 (shipped default 3); auto-raise logged and reported if triggered
- [ ] ANSWERS AND EXPLANATIONS division generated from the randomized bank mapping
- [ ] Practice Exam N subheads mirror the question division verbatim, one to one
- [ ] Both divisions in two-column layout; reference format audit PASS
- [ ] Numbering aligns: every answer entry number matches its question number across the full bank
- [ ] Score Interpretation Guide: no pass-probability claims; performance bands descriptive; study strategies reference appendices and sourced external resources only
- [ ] Proceed gate active

**Gate 4 — Back Matter, Assembly, and Final QA**
- [ ] Score Interpretation Guide length measured on render: 1.40 to 1.55 pages; corrections via substantive content only
- [ ] How to Use This Book length measured on render: 1.40 to 1.55 pages
- [ ] Appendix A: Exam Blueprint Summary sourced from Exam Format Evidence record; disclaimed as subject to change; no invented statistics
- [ ] Appendix B: Time-Per-Question Budget calculation shown; pacing strategies practical
- [ ] Suggested Readings (if included): real, verifiable sources only; no invented references
- [ ] Two-pass Contents gate: build, extract folios, write map, rebuild, re-extract, compare; printed equals actual for every entry; no "undefined" strings
- [ ] Folio is live native page number field, never typed text; front matter pages carry no visible folio
- [ ] Strip sweep: every IMAGE PROMPT block removed; opening and closing table tags balance; marker string absent
- [ ] Full gate register above re-run on the complete artifact
- [ ] Contrast verification: every foreground-background pair computes to at least 4.5:1
- [ ] Byline appears in exactly two interior locations: title page and copyright attribution; no credentials or invented biography
- [ ] Non-affiliation statement present on copyright page naming the exam owner
- [ ] Suggested Readings checked: every citation is real and verifiable
- [ ] No invented statistics, regulations, thresholds, or attributions anywhere in the manuscript including marketing surfaces
- [ ] Operator Zero Correction Standard: the delivered manuscript requires no manual formatting correction; the only manual task on a PROMPTS ONLY host is replacing prompt blocks with rendered images
- [ ] Release record written

---

## KDP Positioning

**Amazon Category Tree (primary):** Books > Test Preparation > [specific certification or exam family]
Examples: Books > Test Preparation > Professional > Contractor Licensing; Books > Test Preparation > Nursing > NCLEX; Books > Test Preparation > Real Estate

**Secondary Category:** Books > Education & Teaching > Higher Education > Test Preparation (when the exam targets academic or professional entrance); or Books > Reference > [subject domain] when the certification is niche.

**Description Lead:** The description leads with the total question count and the exam name (used nominatively), then the timed-simulation format, then the comprehensive rationale coverage, then the score interpretation feature. The non-affiliation disclaimer appears at the end of the description.

**Metadata Signals:**
- Title and subtitle carry the exam name nominatively and the exact question count
- Keywords target the exam name, the certification family, the question count, "practice test," "exam prep," "mock exam," and the topic domain
- The non-affiliation disclaimer in the description protects against trademark disputes with the administering body

**Back Cover (if applicable):** States the total question count prominently; lists the topic domains covered; names the simulation format; includes the non-affiliation statement. No invented endorsements, no invented pass rates, no invented statistics.

---

## Key Rules — Do NOT Break

1. **No verbatim secured exam content.** No actual administered examination item is reproduced, paraphrased closely, or imitated item-for-item. This is an absolute prohibition with no exception, regardless of source.

2. **Every item carries one single defensible correct answer.** Domain Master sign-off is required for every item. An item with two arguable correct answers is a defect and is rewritten before the set clears Gate 2.

3. **Every rationale addresses every distractor.** A rationale that only explains why the key is correct and is silent on the distractors is a defect. All four (or more) options receive a rationale component.

4. **No pass-probability claims anywhere.** The Score Interpretation Guide, the description, the back cover, and all marketing surfaces are free of any claim that a score on this book predicts, correlates to, or is equivalent to a score on the actual administered examination.

5. **Exam Format Research runs before the first item is written.** The Research Before Generation gate is invariant: live web research, Exam Format Evidence record with sources and date, profile lock, bank blueprint, then generation. No item, stem, option, or explanation is produced before the evidence record is recorded.

6. **No invented statistics, regulations, thresholds, or citations.** This rule covers everything: stem facts, distractor facts, rationale citations, Score Interpretation Guide claims, Appendix A blueprint percentages (sourced from the evidence record and disclaimed), and all marketing text.

7. **Continuous numbering across the full bank.** Questions run 1 through the operator-supplied total with no restart at set boundaries. Answer entries carry identical numbers to their questions. This is the Literal Numbering Law and it cannot be overridden by style or convenience.

8. **Two-column layout is mandatory for both divisions.** Both PRACTICE QUESTIONS and ANSWERS AND EXPLANATIONS render in two equal columns. Single-column answers are prohibited absent an explicit recorded operator instruction.

9. **Non-affiliation statement is mandatory on the Copyright page.** Any title that uses a protected examination or certification name in the title or subtitle carries the statement naming the mark owner and disclaiming sponsorship, affiliation, and endorsement.

10. **The Two Option Law holds.** Any profile whose in-sequence types include a two-option format carries a run cap of at least 2 (shipped default 3). The engine auto-raises and reports; it never ships silently below the floor.

11. **Exhibit minimalism.** Exhibits are exceptional. The default for every item, every set, and every bank is zero exhibits. An exhibit is included only when the item genuinely cannot be tested without the figure. Every exhibit position is declared and justified in the bank blueprint.

12. **The Answer Pattern Audit runs against the actual built file.** Structural checks and text-only review return UNVERIFIED; UNVERIFIED blocks advancement exactly as FAIL does.

## STUDY GUIDE FORMAT LAW (operator directive 2026-08-10 - NON-NEGOTIABLE)

Exemplar: the MEDSURG Certification Exam Prep volume (515 pp, 8.5x11, verified zero margin
violations). Every study-guide / exam-prep book follows this EXACT format. Color accents, panel
styling, and motifs still rotate per book (No-Two-Books-Alike); the structure and discipline below
never do.

1. COVER / TITLE PAGE - minimal and massive, one serif family, centered, no decoration:
   main title 36-90 pt bold sized by word length so the full title fits in AT MOST 4 lines
   (the exemplar: 3 lines at 90/48 pt). Short punchy titles take the top of the range;
   never break a word, never exceed 4 lines. Nothing else crowds the page.
2. FRONT MATTER - disclaimer page (educational resource, no exam-body affiliation, no guarantee
   of results) immediately after the cover; then a full dot-leader TABLE OF CONTENTS listing
   every chapter, every named topic, every Practice Questions set, and every Answers set.
3. BODY CHAPTERS - chapter title 20-22 pt bold ALL CAPS centered with a full-width rule beneath;
   topic subheadings 15-16 pt bold centered (major) or bold side-headings at body size (minor);
   body 11 pt serif JUSTIFIED single column; folio centered at the page bottom.
4. TABLES - a bold table caption line above the grid; bordered grid with bold header row;
   consistent cell padding; sized to the text block; never crossing a margin; never a stranded
   header row at a page break.
5. FIGURES - centered, with a bold caption directly beneath. Every label inside a figure must be
   a correctly spelled real term - a figure with garbled or invented labels is a QA FAILURE.
6. PRACTICE APPARATUS - consolidated at the BACK of the book as one "PRACTICE QUESTIONS AND
   ANSWERS" part (22 pt bold caps opener with rule):
   - Question sets numbered by chapter ("Practice Questions 1", 16 pt bold centered with rule).
   - Questions in TWO-COLUMN layout, 10 pt: numbered stem, then options A-D each on its own
     line. Board/exam style, one best answer, no all/none-of-the-above padding.
   - Each set's answers follow as a separate "Answers to Practice Questions N" section (16 pt
     bold centered with rule), ALSO two-column: "Answer: X) <option text>" then "Explanation:"
     with a rationale of TWO TO THREE LINES that teaches, never just restates. Answers are NEVER
     placed immediately after each question.
   - RANDOM, UNPREDICTABLE correct options (hard requirement): across every question set the
     correct letters must LOOK random to a reader scanning the key - roughly balanced across
     A-D, no long runs of one letter, no alternating or cyclic patterns (ABCDABCD...), no
     letter used for more than ~35 percent of a set, and no bias toward any single letter
     across the whole book. Verify the distribution before the set is accepted; regenerate the
     assignment if any pattern is detectable.
7. CONTAINMENT - single text block, approx. 0.7-0.8 in side margins at 8.5x11; nothing (text,
   table, rule, figure) crosses a margin anywhere in the book. The exemplar's bar: zero
   violations in 515 pages. render_qa.py on the rendered PDF is the mandatory gate.

## Textbook reference-bank standard applies (2026-08-14)

This niche is an educational/reference category: the HOUSE REFERENCE BANK
standard for textbooks and educational books (see uapf-niche-textbook,
"HOUSE REFERENCE BANK", derived from five catalog masters at
cover_db/_interiors/textbook/) is BINDING here on both engines and every
install: scholarly justified body, decimal-numbered sections, evidence and
key-concept panel families, shaded-header tables, labeled multi-panel
figures, professional front matter, one distinct accent system per book,
and NO TWO BOOKS with the same pattern. Niche-specific structures in this
skill (question banks, drills, exercises, entries) keep their own
architecture inside that quality bar.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
