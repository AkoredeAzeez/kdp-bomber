---
name: uapf-niche-study-guide
description: Study guide and exam prep overlay (OV-STUDY) — invoked by uapf-phase0-router when routing signals match this niche; produces syllabus-mirrored study guides with consolidated exam-style practice divisions under USGPF 2.9 / USGPF-C / USGPF-Q discipline.
---

# UAPF Niche: Study Guides & Exam Prep (OV-STUDY)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/USGPF-2.9/` (config, validation, phases, and deterministic ops in `genie_study_guide.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=USGPF 2.9` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title contains study guide, exam prep, test prep, revision guide, certification study, practice test, NCLEX, bar exam, USMLE, CPA, PMP, CompTIA, SAT, IELTS, TOEFL, or any named examination plus preparation (e.g. "Series 7 Preparation", "Plumbing License Exam Study Guide", "ACT Prep 2027"). Also routed here on subtitle or topic signals: "N Practice Questions", "pass the [exam]", "licensure", "certification review", "board review", "qualifying exam". If children's audience signals appear (for kids, an ages range, a grade level, preschool, kindergarten), the OV-KIDS sub-overlay of this niche governs with its recorded overrides (visual activities in-chapter, single ANSWER KEY division, age-band typography); everything not overridden in OV-KIDS holds as written below.

## Expert Panel

1. **Domain Master** — a veteran practitioner-instructor of the exact subject and examination family (e.g. NCLEX: senior nursing educator; CPA: practicing CPA and review-course author). Owns technical accuracy of every chapter, table, threshold, and calculation, and confirms every practice item is answerable from its mapped chapter alone.
2. **Psychometrician / Item-Writing Specialist** — owns item construction: stem quality, distractor plausibility and parallelism, option-length balance, answer-key randomization and distribution, run caps, pattern guards, and the fifty-word teaching explanations.
3. **Official-Syllabus Auditor** — holds the researched Exam Format Evidence and Examination Scope Evidence records; verifies the chapter plan mirrors the administering body's actual content outline/blueprint and weighting, and runs the syllabus-coverage audit at every gate.
4. **Exam-Prep Pedagogue** — owns the learning architecture: objectives, Exam Tip and Common Mistake boxes, the two-pass study method, pacing discipline, error-log doctrine, and the study-cycle guidance in Preface, Introduction, and Conclusion.
5. **Regulatory & Marketplace Compliance Reviewer** — owns trademark nominative use, the non-affiliation statement, jurisdiction disclaimers, the marketplace-integrity modifier for region-locked exams, and the ban on reproducing or imitating secure examination items.

## Phase 0 — Title Analysis

Run these steps in order; every configurable setting resolves automatically to the best available option with no choice menus. The **total practice question count is the single operator-supplied setting** and arrives with the title; if absent, request it as the only outstanding input before configuring.

1. **Title verbatim intake.** Accept the supplied title exactly as given, character for character. Never rewrite, re-case, re-punctuate, truncate, or substitute it at any stage — configuration, manuscript, cover, metadata, marketing. Only an explicit operator instruction changes a title.
2. **Title trademark clearance (immediate, live).** Scan the proposed title and every subtitle candidate against the trademark register and the target marketplace: identical/confusingly similar marks, protected brand elements, series names, confusable existing titles. Record the Title Clearance record with sources and scan date. A clean result is "good to go"; a conflict is reported once, plainly, with sources, as an advisory for the operator — production continues with the title verbatim. Examination and certification names (NCLEX, CPA, PMP, CompTIA, SAT, IELTS, TOEFL, USMLE, etc.) are used **nominatively only**; whenever a protected exam name appears in the title or subtitle, the copyright page carries a non-affiliation statement naming the mark owner and disclaiming sponsorship, affiliation, and endorsement.
3. **Audience category research (routing).** Research the title live for children's audience signals; a children's classification routes the OV-KIDS overrides. Otherwise the title is OV-STUDY (or OV-EXSIM for pure exam-simulator products). Record the Children's Category record with sources and research date.
4. **Exam Format Research (mandatory, live, before any profile decision).** Research the named examination on the current web: administering body or vendor, question formats actually in use, option counts and labels, presence of multi-response / true-false / numeric / ordered / exhibit item types, sectioning, instruction conventions, difficulty and reasoning style. Lock the Exam Format Profile from that evidence; the shipped profile library is a starting benchmark, never a substitute for research. Record the Exam Format Evidence record with sources and date. Where evidence is inconclusive or the exam is proprietary/undisclosed, apply the conservative family profile, record the uncertainty, and put no unverified format claim in reader-facing text. **Actual examination items are secure, protected material and are never sought, reproduced, or imitated item for item; every question is original work written to the researched format.**
5. **Examination Scope Research (chapter plan evidence).** From the same live research, capture the official content outline or blueprint: topic domains, their weighting, cross-cutting skill families, and the jurisdictional frame. The chapter plan maps forward to this blueprint — never to a generic topic list.
6. **Marketplace-integrity modifier (region-locked exams).** If the exam is administered only in specific jurisdictions or regions (state contractor licenses, state bar exams, region-locked certifications, country-specific exams like IELTS band frameworks per jurisdiction), record the target marketplace and jurisdiction in the configuration package; the Introduction, disclaimer, and metadata must state the jurisdictional frame honestly, the disclaimer must carry the jurisdiction-variance sentence, Suggested Readings must include the correct jurisdiction's candidate information bulletin, and KDP marketplaces where the exam does not exist are not targeted with implied local relevance.
7. **Subtitle generation (Subtitle Composition Law).** Generate five candidates, auto-select and lock the winner. Every candidate: (a) states the total practice question count with the words "Practice Questions" (e.g. "600 Practice Questions"), matching the configured total exactly; (b) contains letters, numerals, and spaces only — no punctuation mark or symbol of any kind; (c) renders on the title page in at most two lines at the locked subtitle size. Any change to the total regenerates the subtitle. (OV-KIDS may count "Practice Activities" instead.)
8. **Language Profile Card.** The language of the title determines the language of the book; lock the content language, regional variant, script, typographic conventions, and reader-facing string equivalents. The operating layer (reports, audits, gate lines) stays English.
9. **Title Design Signature (Catalog Variation Law).** Generate the title-specific palette plus heading, box, table, title-page, and figure treatments; clear it against the Catalog Design Register (no repeated hex values, perceptibly distinct primary hue, at least two non-color axes different from the nearest registered title). Regenerate on collision; register at release.
10. **Byline (FNG Law).** Fetch a name live from the Fake Name Generator service (equivalent random-name site as recorded fallback); retain the name only, format First Name, Initial, period, Surname; run the collision and impersonation check; lock with source and date. No credential, title, degree, or biography ever attaches to the pen name, anywhere.
11. **Assessment plan.** Derive set count and questions per set from the operator-supplied total under the locked profile's type mix; map sets to chapters and mastery outcomes in proportion to the researched blueprint weighting; record the randomization seed.
12. **Auto Configuration Package.** Record all of the above plus: trim and length evidence, the Format Specification Record, the visual plan, the delivery mode record (RENDER on an image-capable host, PROMPTS ONLY on a prompt-only host, detected automatically), the research pathway, the risk regime with disclaimer template selection, and the Preliminary Cover Data Card. Close by asking whether to proceed with the table of contents, end on the Proceed gate, and stop.

## Book Architecture

**Manuscript sequence (locked):** Title page; Copyright and Disclaimer; Table of Contents; PREFACE; INTRODUCTION (the exam orientation unit — always first before any content chapter); the learning chapters; PRACTICE QUESTIONS; ANSWERS AND EXPLANATIONS; CONCLUSION; GLOSSARY; SUGGESTED READINGS; APPENDICES. Nothing inserted or omitted without a recorded amendment; no back-matter item exists merely to add pages.

**Exam orientation first.** The INTRODUCTION is the exam orientation chapter and precedes every content chapter: what the examination is and where it sits in the qualification process; the exam's content structure per the Examination Scope Evidence record with the canonical topic lists; format generalities stated without invented specifics (testing centers, time limits, board-set passing standards, open vs closed book variance); how the guide maps to the blueprint (forward study, backward review); the practice-set philosophy as a diagnostic instrument; the cross-cutting skill families; the recommended study cycle ending in back-to-back full sets; and the jurisdiction-notes close. No image prompts in the Introduction. Length 1.40 to 1.55 rendered pages (same band for Preface and Conclusion).

**Chapter formula (structural unit — the chapter template):**
1. Chapter title — Heading 1, BLOCK CAPITALS, new page.
2. LEARNING OBJECTIVES box — immediately after the title, opening with the exact line "After completing this chapter, you will be able to", then three to six numbered verifiable capabilities.
3. Introductory prose — two or more paragraphs of comprehensive instruction (never summary), framing the territory, why examiners test it, how the subchapters fit.
4. HOW TO USE THIS CHAPTER box — reading order, the table/figure to study first, and the timed conditions for the chapter's associated practice set.
5. Subchapters — Heading 2, each three or more substantive paragraphs moving definition → mechanism/rule → applied example → examiner relevance; EXAM TIP boxes at tested distinctions; COMMON MISTAKE boxes at predictable errors; captioned premium-color data tables; content figures at exact anchors.
6. KEY POINTS box — three to six bulleted essentials closing the chapter.
7. Floors: at least two captioned data tables and at least two content figures per chapter.

**Chapter-to-syllabus mapping.** Chapters mirror the OFFICIAL syllabus/blueprint structure of the administering body — domains, weighting, and order taken from the Examination Scope Evidence record, never a generic topic list. The Contents contract states each chapter's subchapters and mastery outcomes.

**Page bands:** every learning chapter measures six to ten rendered pages; the learning chapters as a whole measure fifty to sixty rendered pages (plan targets fifty-two to fifty-eight), and **sixty pages is an absolute ceiling** — sixty-one or more is a blocking FAIL at the Chapters Total Length gate. Shortfalls corrected with substantive content or an added blueprint chapter; overages by scope adjustment; never in the typography. Preface, Introduction, and Conclusion each 1.40 to 1.55 pages measured on the render.

**Practice divisions (consolidated model):** all practice sets appear consecutively after the learning content; a separate ANSWERS AND EXPLANATIONS division follows the final set; answers never adjacent to their questions. Both divisions render in two equal columns (576 DXA / 0.4 inch separation, separator rule on). Division heads (PRACTICE QUESTIONS, ANSWERS AND EXPLANATIONS) are Heading 1 on new pages; set subheads and answer-group subheads are Heading 2 in continuous sections that never open a new page, using the verbatim mirrored string "Practice Question N" in both divisions, both entering the Contents. Every chapter's tested territory is covered by its mapped set(s), so every chapter ends its arc in exam-style practice; the HOW TO USE THIS CHAPTER box directs the reader to that timed set. Question numbering is continuous, 1 through the operator-supplied total, across the whole division (per the locked reference exemplar); answer entries carry identical numbers. Question blocks are indivisible (keep chains); a block that will not fit moves whole to the next column.

**Question block form:** stem in QStem style — number, period, single space, stem text, hanging indent; options in QOpt — capital letter, period, single space, option text, unbroken alphabetical order, each on its own line, letters as literal typed text (never Word auto-numbering). **Answer entry form:** AnsNum — number, period, space, "Answer:", space, key letter, closing parenthesis, space, full text of the correct option exactly as printed in the question; AnsExpl — "Explanation:", space, reasoning, indented a quarter inch, at most fifty words, teaching the WHY. Multi-response keys list every correct letter with text joined by semicolons; numeric keys state value with unit.

**Front matter:** no visible folio anywhere in front matter; visible Arabic numbering begins at 1 on the Introduction, no later restart; folio is a live page-number field, never typed text. Title page: title dominant at 48pt bold BLOCK CAPITALS primary color (at most three lines), subtitle 14pt black (at most two lines), byline 14pt bold name only; nothing else — no publisher, logo, ISBN or placeholder, edition line, credential, or ornament; everything inside the margins, no bleed. Copyright page: copyright block, reproduction prohibition, edition line, trademark ownership sentence, non-affiliation statement where required, and the composite educational + jurisdiction disclaimer; no ISBN, publisher name, LCCN, or cataloguing block.

**Back matter:** Conclusion at measured length (never opening "In conclusion"); Glossary as an alphabetical two-column premium-color table; Suggested Readings from real, verifiable sources only, always including the jurisdiction's candidate information bulletin; the appendix trio — Appendix A: Examination Day Checklist (~10 items), Appendix B: subject calculation quick reference (plain safe notation), Appendix C: key thresholds and values quick reference cross-referenced to governing standards. Every appendix has a Heading 1 title "Appendix X: Title" and enters the Contents.

**Table of Contents:** native Word References-tab TOC field on built-in Heading 1/Heading 2 styles, dot-leader toc styles (level one 12pt, level two 11pt indented 360 DXA, right tab at 9936 DXA), cached result shipped, update-on-open enabled, never manually formatted, closed only by the two-pass pagination gate. Entries: Introduction; every chapter with subchapters; Practice Questions with set entries; Answers and Explanations with set entries; Conclusion; Glossary; Suggested Readings; each Appendix. Front matter items do not appear.

## Interior Design

Inherits UAPF default discipline with these niche-locked values:

- **Trim:** 8.5 x 11 in (12240 x 15840 DXA); margins 0.8 in all sides; footer distance 0.6 in; gutter 0; text width 9936 DXA; no running heads anywhere.
- **Body:** Times New Roman 11pt, fully justified prose, 1.15 line spacing (line 276 AUTO) everywhere; primary reading text never below 11pt (10pt only in non-reader-facing scaffolding). Assessment styles (QStem, QOpt, AnsNum, AnsExpl, Instr) are left aligned, never justified.
- **Headings:** chapter/division/matter heads Heading 1 — 22pt bold BLOCK CAPITALS centered, primary color, new page; subchapters Heading 2 — 16pt bold Capitalized, left aligned, flowing with the text under the six-line floor (page break only when fewer than six lines of opening text would fit beneath the heading). All heading appearance lives inside the style definitions — Styles Discipline Law: a bold paragraph without the Heading identifier is a pseudo-heading defect.
- **Color:** COLOR TIER = PREMIUM COLOR, PAPER = WHITE, always; monochrome only by recorded operator override. Title-specific palette under the Catalog Variation Law; every text/fill pair computed to at least 4.5:1 contrast on actual file values; failing pairs darkened, never shrunk; color never carries meaning alone (every colored element also carries a text label). Exhibit line art may remain functional black.
- **Boxes:** full-width two-row tables (9936 DXA): theme-color title bar with white BLOCK CAPITAL 11pt bold label; tinted body at 11pt/1.15; 1pt theme borders; cant-split on both rows. The five boxes: LEARNING OBJECTIVES, HOW TO USE THIS CHAPTER, EXAM TIP, COMMON MISTAKE, KEY POINTS.
- **Data tables:** primary-fill header row with white bold labels; alternating tinted body rows; 0.5pt neutral borders; caption above in Caption style, "Table N.n  Title"; header repeats across pages; exact margin alignment — every full-width element spans exactly 9936 DXA flush to both margins.
- **Images:** content figures — photorealistic, full text width, ~6.9 x 3.8 in, 300+ effective DPI, "Figure N.n" captions, anchored where their subject is taught; question exhibits — clean black-on-white labelled line diagrams, column width ~3.2 x 2.4 in, "Figure QS.n" captions, dimension labels X and Y and never A through D, placed first in their question block, under the Exhibit Minimalism Law (default zero; include only when the item is genuinely untestable without the figure, each declared and justified in the blueprint). Delivery mode per host: RENDER (generate and embed at the anchor during drafting, no prompt blocks ever shipped) or PROMPTS ONLY (exhaustively descriptive five-field IMAGE PROMPT blocks — 100+ words for content figures, 60+ for exhibits — as the deliverable). Strip sweep before any reader-facing export.

## Content Rules

**The fatal flaw to avoid:** a study guide whose chapters are a generic textbook topic list rather than a mirror of the official syllabus, with practice questions bolted on that neither match the real exam's item formats nor teach anything in their answers. Symptoms: chapters that summarize instead of teach; questions from memory instead of researched format; answer lines that name the key without the WHY; exploitable answer patterns (BBBB..., strict alternation); invented pass rates, statistics, or "official" claims. Every mechanism below exists to kill this flaw.

1. **Comprehensive Instruction Law.** Chapters teach to mastery and never summarize. Testable depth standard: a candidate can answer the chapter's associated practice items from the chapter alone.
2. **Syllabus mirroring.** The chapter plan is taken from the researched official blueprint — domains, weighting, order. No unverified scope claim ships; where evidence is inconclusive, the conservative subject convention applies and the uncertainty is recorded.
3. **Research before generation.** Not one item, stem, option, or explanation is written before the Exam Format Evidence record exists with live, dated sources. The invariant sequence: title and count in → web confirmation → evidence record → profile lock → assessment plan → blueprint → generation.
4. **Item originality and fidelity.** Every item is original work written to the researched format — matching the real exam's option counts, item types (single best answer, SATA/multi-response, true/false, numeral combination, ordered response, numeric entry, scenario/PBQ as the evidence dictates), instruction conventions, difficulty and reasoning style. Real exam items are never sought, reproduced, or imitated.
5. **Stem and distractor quality.** Stems complete and self-contained; no trick constructions or double negatives. Distractors plausible, mutually exclusive, parallel in grammar and length, drawn from real misconceptions; no absurd throwaways; no positional language (all/none of the above, letter references) so items stay shuffle-safe; balanced option lengths; numeric options logically ordered in the exam's units.
6. **Explanations teach the WHY.** Every explanation teaches the rule, mechanism, or calculation that makes the key correct, in fifty words or fewer, content-based (never referencing option letters), never a restatement that the key is correct. Calculations shown compactly in plain safe notation.
7. **Answer randomization engine.** Balanced quotas per set (within one of even) with cross-set rotation; depth-first sequencing under the run cap (default 1; two-option types auto-raise to at least 2, default 3, reported never silent); pattern guards — no four-letter permutation doubled, no two-letter alternation tripled; pinning detection on positional language; atomic key regeneration so key and options never desynchronize; recorded seed for reproducibility; explicit error over best-effort sequence.
8. **Compliance sweep.** Zero em dashes; zero en dashes (ranges written with "to"); curly apostrophes only; conventions per the Language Profile Card; measurements in the units the target exam uses.
9. **No invented anything.** No invented citations, statistics, quotations, studies, guidelines, laws, standards, thresholds, pass rates, awards, or attributions — anywhere, including stems, options, explanations, and marketing surfaces. Suggested Readings are real and verifiable.
10. **Anti-AI-voice law**; no meta references to the production process; the phrase "this book is written for" never appears in front matter.
11. **Content standards rule (catalog-wide).** No pork or pig derivatives, characters, or references; no alcohol in any form or alcohol-centric scenarios — in any stem, option, explanation, scenario, example, or image.
12. **Jurisdiction honesty.** Jurisdiction-sensitive facts stated only at the level the evidence supports; the disclaimer carries the jurisdiction-variance language; the reader is always directed to the candidate bulletin and licensing board for current requirements.

## QA Checklist

**Gate 1 — Configuration and Contents Contract (Phase 0/I):**
- [ ] Title accepted verbatim; Title Clearance record with sources and scan date; non-affiliation statement queued if a protected exam name appears.
- [ ] Exam Format Evidence record exists with live sources dated to this engagement; profile locked from evidence (Research Before Generation gate).
- [ ] Examination Scope Evidence record exists; chapter plan mirrors the official blueprint with domains and weighting; syllabus-coverage map recorded chapter by chapter.
- [ ] Marketplace-integrity modifier recorded for region-locked exams (jurisdiction, marketplace, bulletin source).
- [ ] Subtitle states the exact question count with "Practice Questions", letters/numerals/spaces only, two rendered lines max.
- [ ] Byline fetched live, collision-checked, locked; Title Design Signature cleared against the Catalog Design Register; Language Profile Card locked; assessment plan maps sets to chapters with seed recorded.

**Gate 2 — Per-Chapter (after every chapter):**
- [ ] Template complete: title, Learning Objectives box (exact lead line), intro prose, How to Use This Chapter box, subchapters with Exam Tip/Common Mistake boxes, ≥2 captioned tables, ≥2 content figures, Key Points close.
- [ ] Comprehensive instruction verified: ≥3 substantive paragraphs per subchapter, definition → mechanism → applied example → examiner relevance; chapter's practice items answerable from the chapter alone.
- [ ] Chapter measures 6 to 10 rendered pages; running chapters total projected against the 60-page absolute ceiling; scope adjusted immediately on a breached projection.
- [ ] Syllabus-coverage progress: chapter maps to its blueprint domain; no domain silently dropped or merged.
- [ ] Proofreader, consistency auditor, content policy scan, per-chapter format audit with rendered inspection, embedded-figure gate (RENDER host) or anchored prompt blocks (PROMPTS ONLY host); subchapter six-line floor verified on the render; boxes unsplit; tables flush to margins; chapter preview delivered.

**Gate 3 — Assessment (per set, engine run, answers division):**
- [ ] Item-format fidelity check: every item's type, option count, labels, and instruction conventions match the Exam Format Evidence record; full-width types break the columns correctly.
- [ ] Set-to-chapter mapping honored; item difficulty mix follows the researched blueprint weighting; pure recall the minority.
- [ ] Answer Pattern Audit PASS on the actual built file: question count equals answer count; numbering continuous without gaps or duplicates; literal typed numbering (never list fields); options in unbroken letter order each on its own line; answer form "N. Answer: X) option text" with text matching the question exactly; every entry carries an Explanation ≤50 words; distribution within tolerance; run cap held; no doubled permutation or tripled alternation; expected two-column sections present.
- [ ] Randomization integrity check PASS: text at new key equals text at old key, option multisets match, seed recorded, pins and flags and any auto-raised cap reported.
- [ ] Exhibit Minimalism verified both directions: every declared exhibit embedded, no undeclared or merely illustrative exhibit; dimension labels never A through D.

**Gate 4 — Final QA and Release:**
- [ ] Syllabus-coverage audit (mandatory): every blueprint domain of the Examination Scope Evidence record is covered by a chapter and tested by mapped items in proportion to its weighting; any gap is a blocking FAIL.
- [ ] Item-format fidelity re-check across the full bank against the evidence record.
- [ ] Two-pass Contents gate: printed folios equal actual for every entry, complete map, zero "undefined" residue; style integrity (no pseudo-headings) before every Contents pass.
- [ ] Section lengths re-verified: Preface/Introduction/Conclusion 1.40 to 1.55; chapters total 50 to 60 pages.
- [ ] Contrast computed ≥4.5:1 on actual file values; compliance characters absent; table/margin alignment exact; front matter folio-free; Arabic numbering from Introduction with no restart; live folio fields.
- [ ] Strip sweep executed: no IMAGE PROMPT marker, balanced table tags, no symlinks, no embedded PDF.
- [ ] Marketplace integrity: non-affiliation statement present where required; jurisdiction disclaimer complete; candidate bulletin in Suggested Readings; no implied local relevance in marketplaces where the exam does not exist.
- [ ] Byline appears exactly twice (title page, copyright), name only, no credentials; truthful status vocabulary throughout — PASS only after actual file and rendered page inspection; UNVERIFIED blocks as FAIL.

## KDP Positioning

- **Category tree:** primary under Education & Teaching > Test Preparation (then the exam family: Professional, Graduate School, College & High School, Citizenship, English as a Second Language as fits); secondary in the subject vertical (e.g. Medical Books > Nursing > Reviews & Study Guides for NCLEX; Business & Money > Accounting for CPA; Computers & Technology > Certification for CompTIA). For trade licenses, Engineering & Transportation or Home Improvement per subject convention.
- **Description leads with:** the exact practice question count and official-syllabus alignment — "N exam-style practice questions with full teaching explanations, mapped to the current [exam] content outline" — then the consolidated practice + separate answers structure, the balanced randomized keys (no exploitable patterns), the study-method apparatus (objectives, exam tips, common mistakes, error-log method), and the jurisdiction frame stated honestly. No invented pass rates, endorsements, or "official" claims; nominative exam naming only.
- **Metadata signals:** keywords built from exam name + "practice questions", "study guide", "exam prep", "test prep", "[year] review", format terms the evidence supports (e.g. "SATA questions" for NCLEX); the subtitle's question count restated; region-locked exams carry jurisdiction keywords and never target irrelevant marketplaces. A+ Content follows the UAPF cover/A+ system with the locked Title Design Signature.
- **AI disclosure and rights records** per the UAPF release governance; the trademark advisory record is available in the release record.

## Key Rules — Do NOT Break

1. **Exam orientation first.** The Introduction is the exam orientation unit and always precedes every content chapter: what the exam is, its official structure, how the guide maps to the blueprint, and the study method.
2. **Chapters mirror the OFFICIAL syllabus.** The chapter plan is taken from the live-researched content outline/blueprint of the administering body — domains, weighting, order — never from a generic topic list. No unverified scope claim ships.
3. **Research before generation, always.** No item, stem, option, or explanation is written before the Exam Format Evidence record exists with live, dated sources. Question formats are never assumed, never hardcoded, never written from memory.
4. **Every chapter ends in exam-style practice.** Every chapter's tested territory closes in exam-style items: each chapter maps to its practice set(s) in the consolidated PRACTICE QUESTIONS division (mirrored "Practice Question N" answer groups; answers never adjacent to questions), and the chapter's How to Use This Chapter box directs the reader to that timed set. (OV-KIDS: in-chapter Practice Time sections with a single back-matter ANSWER KEY.)
5. **Answer explanations teach the WHY.** Every explanation teaches the rule, mechanism, or calculation in ≤50 words, content-based, never letter-referencing, never a bare restatement of the key.
6. **Syllabus-coverage audit is mandatory.** At Final QA, every blueprint domain must be covered by a chapter and tested in proportion to its weighting; a gap is a blocking FAIL.
7. **Item-format fidelity check at QA.** Every item's type, option count, labels, and instruction conventions are verified against the Exam Format Evidence record at the set audits and again at Final QA.
8. **Marketplace-integrity modifier for region-locked exams.** Jurisdiction stated honestly in Introduction, disclaimer, and metadata; correct candidate bulletin cited; no implied relevance in marketplaces where the exam does not exist; non-affiliation statement whenever a protected exam name appears in the title or subtitle.
9. **Never reproduce or imitate real exam items.** Secure examination material is never sought, reproduced, or imitated item for item; every question is original work written to the researched format.
10. **Randomization discipline.** Balanced keys via the engine (quota rotation, run caps, pattern guards, pinning, atomic key regeneration, recorded seed); the Answer Pattern Audit must PASS on the actual built file before any set is presented and at Final QA; the Two Option Law is absolute.
11. **The title is verbatim; the count is the single setting.** The operator-supplied title is never altered; the total practice question count is the only operator-supplied setting and the subtitle states it exactly with "Practice Questions" in letters, numerals, and spaces only.
12. **Length bands are met in scope, never typography.** Chapters 6 to 10 pages; chapters total 50 to 60 with 60 an absolute ceiling; Preface/Introduction/Conclusion 1.40 to 1.55 pages; never solved by shrinking type, compressing spacing, or narrowing margins.
13. **Truthful status and the Proceed gate.** PASS only after inspection of the actual file and rendered pages; UNVERIFIED blocks exactly as FAIL; every phase transition announces what comes next, ends on the standalone Proceed gate line, and stops.
14. **No invented facts, no credentials, no scaffolding shipped.** No invented statistics, citations, thresholds, or pass rates anywhere; the pen-name byline carries no credential or biography; the strip sweep guarantees no IMAGE PROMPT block ever reaches the reader-facing file.

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
