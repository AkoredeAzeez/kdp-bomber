---
name: uapf-niche-language
description: Language learning book overlay (OV-LANG) — invoked by uapf-phase0-router when routing signals identify a title teaching one language to speakers of another language
---

# UAPF Niche: Language Learning Book (OV-LANG)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/USGPF-2.9/` (config, validation, phases, and deterministic ops in `genie_language.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=USGPF 2.9` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title or supplied context contains any of the following signals: [Language] for [Language] speakers, phrasebook, vocabulary builder, grammar workbook, learn [language], [Language] in [time period] (e.g., "Spanish in 30 Days"), verb conjugation, conversational [language], [language] for beginners, [language] for travelers, [language] for kids (routes OV-KIDS instead if children's audience signals are confirmed), bilingual phrase guide, or any title whose primary deliverable is teaching communicative competence in a target language to speakers of a source language.

---

## Expert Panel

**Domain Master — Native-Speaker Linguist of the TARGET Language** (listed first; non-negotiable)
The Domain Master must be a native speaker of the language being taught (the TARGET language), not the language the reader already speaks (the SOURCE language). This role is the final authority on all target-language content: vocabulary, grammar explanations, dialogue authenticity, cultural accuracy, register labeling, and pronunciation guidance. No target-language content clears Gate 1 without Domain Master approval. If the session cannot confirm a qualified native-speaker Domain Master for the target language, production halts and is reported.

**Applied Linguist — Second Language Acquisition Specialist**
Specialist in communicative language teaching methodology, sequencing of grammar points, vocabulary load management across units, spaced repetition principles, and the pedagogical design of drills and exercises. Owns the unit architecture decisions, the pacing of the grammatical syllabus, and the difficulty gradient from unit to unit. Confirms that each unit's single grammar point is introduced at the appropriate stage in the learner's development.

**Cultural Consultant — Native Culture Bearer of the TARGET Language Region**
Provides and verifies all cultural notes. Cultural notes are factual, sourced, and specific to the declared regional variant (not generic pan-language generalizations). Reviews every dialogue for cultural plausibility: settings, interpersonal register, social conventions, and forms of address must reflect how native speakers of the declared region actually communicate. Flags any dialogue that would read as odd, offensive, or unnatural to a native speaker.

**Bilingual Copy Editor — Fluent in Both SOURCE and TARGET Languages**
Reviews every bilingual element: vocabulary glosses, grammar explanations (written in the SOURCE language, exemplified in the TARGET), translation notes, and the answer key. Catches errors in both directions: mistranslations into the target, incorrect source-language explanations of target-language rules, and inconsistencies between the vocabulary block and its appearances in dialogues and drills. Does not substitute for the Domain Master's native-speaker authority on the target language.

**Technical Production Editor**
Owns the DOCX build for this niche: bilingual table formatting, parallel-text alignment where used, the vocabulary-block table styling, the dialogue presentation format, the drill and exercise typography, and margin alignment. Confirms that non-Latin scripts (Arabic, Chinese, Cyrillic, Japanese, Korean, Hebrew, Devanagari, and others) render correctly in the built file and that right-to-left content is properly encoded and visually verified on the render.

---

## Phase 0 — Title Analysis

**Step 1 — Intake and Signal Verification**
Receive the title. Confirm that OV-LANG routing signals are present and record the routing decision. The title is accepted verbatim under the Title Verbatim Law.

**Step 2 — Direction Declaration (Phase 0 Hard Requirement)**
This step is mandatory and blocks all subsequent Phase 0 steps until resolved. Identify which language is the SOURCE (the language the reader already speaks) and which is the TARGET (the language being taught). The direction must be stated unambiguously: for example, "English to Spanish" (English is source, Spanish is target) or "Arabic for English speakers" (English is source, Arabic is target). If the title does not make the direction unambiguous, request clarification as the only outstanding input before any configuration proceeds. Record the direction as: SOURCE: [language, regional variant]; TARGET: [language, regional variant]. Both languages and both regional variants lock at this step and govern every element of the manuscript.

**Step 3 — Register Declaration**
Declare the register scope of the book: formal only, informal only, or both. If the title signals a specific context (business, travel, academic, everyday conversation), the register scope follows the signal. If both registers are included, every vocabulary item, dialogue line, and grammar exemplar is labeled with its register. Record the Register Scope in the Auto Configuration Package.

**Step 4 — Script and Typographic Profile**
Identify the script or scripts required by the target language. For non-Latin scripts: confirm that the document production system can render the script correctly; declare the font to be used for target-language text; confirm that right-to-left encoding is correctly handled if the script requires it; and add a render-verification step to every Gate 1 per-unit audit that rasterizes the pages and inspects the script rendering visually. Record the Script and Typographic Profile in the Auto Configuration Package.

**Step 5 — Pronunciation System Declaration**
Declare the pronunciation representation system used in this book: International Phonetic Alphabet (IPA), a simplified phonetic respelling system for the source-language reader, romanization (for non-Latin-script target languages, e.g., Pinyin for Mandarin, Romaji for Japanese, ALA-LC for Arabic), or a combination. Record the choice and apply it consistently throughout the manuscript. The Domain Master confirms that the pronunciation system is appropriate for the target language and regional variant.

**Step 6 — Title Trademark Clearance (runs before any other output to the operator)**
Immediately, scan the proposed title and every subtitle candidate live against the federal trademark register and the target marketplace. Record the Title Clearance record with sources and date. A conflict holds the title for the operator's decision; the system never alters the supplied title.

**Step 7 — Children's Category Research**
Research the title live for children's audience signals. If signals are present, the title routes OV-KIDS (with OV-LANG as a modifier for the language niche), and the children's overlay governs age-appropriate activity formats, reading level, and image style. Record the Children's Category record with sources and research date.

**Step 8 — Language Profile Card**
Lock the Language Profile Card. SOURCE: language, regional variant, script, typographic conventions, reader-facing string equivalents. TARGET: language, regional variant, script, typographic conventions, pronunciation system, register scope. The operating layer of the production system remains English (reports, audits, gate lines, package fields). Every reader-facing string in the manuscript is in the SOURCE language where the content is instruction or explanation, and in the TARGET language where the content is the language being taught; bilingual pairings are clearly presented. The compliance sweep adapts to the source language's typography.

**Step 9 — Subtitle Composition**
Compose subtitle candidates under the Subtitle Composition Law (module 2.11 of USGPF 2.9) as adapted for OV-LANG: the subtitle may lead with a communicative promise (e.g., "Master Everyday Conversations," "Build Essential Vocabulary," "From Zero to Conversational") rather than a question count, since language books may not have a fixed item count; alternatively, if the book includes a counted element (e.g., "1500 Essential Words and Phrases"), the count and noun appear in the subtitle. In all cases: letters, numerals, and spaces only; no more than two rendered lines at the locked subtitle size. Auto-select and lock the winner.

**Step 10 — Byline**
Fetch the Fake Name Generator service live. Format as First Name, Initial, period, Surname. Run the collision and impersonation check. Lock the byline. No credentials, language affiliations, or invented teaching experience attach to the pen name anywhere in the manuscript or on marketing surfaces.

**Step 11 — Title Design Signature**
Compose the title's complete palette under the Catalog Variation Law. Check against the Catalog Design Register for distinctness. Failing signatures regenerate until the gate clears.

**Step 12 — Unit Plan**
Draft the unit plan as the production contract: the number of units, each unit's communicative goal, the single grammar point assigned to each unit, the vocabulary domain, the dialogue scenario, the cultural note topic, and the drill types. The grammar points sequence logically from foundational to complex; no unit introduces more than one grammar point. The vocabulary load per unit stays within the researched norm for the audience level (typically 20 to 40 new items per unit for adult beginners). Record the unit plan and confirm with the Applied Linguist before proceeding to the Table of Contents.

**Step 13 — Auto Configuration Package**
Record all outputs: routed overlay (OV-LANG); Direction Declaration (source, target, both regional variants); Register Scope; Script and Typographic Profile; Pronunciation System Declaration; Children's Category record; Title Clearance record; Language Profile Card; Title Design Signature with catalog-distinctness result; subtitle winner; byline record; Format Specification Record; unit plan; Delivery Mode record. Close the Package by presenting the Table of Contents plan for confirmation, end with the exact standalone line: Type to proceed. Stop.

---

## Book Architecture

**Front Matter**

| Section | Purpose | Length |
|---|---|---|
| Title Page | Verbatim title, subtitle, byline | 1 page |
| Copyright and Disclaimer | Standard; notes that regional variants exist and the book reflects the declared variant | 1 page |
| Table of Contents | Native Word TOC field; levels 1 and 2; units and their sub-sections entered | 1 page |
| Introduction | How to use this book; pronunciation guide; script overview if non-Latin; note on regional variant; explanation of register labels; recommended study cadence | 1.40 to 1.55 pages |

**Body: Communicative Units**

Every unit follows the exact six-element architecture in this fixed order:

**Element 1 — Communicative Goal**
One boxed statement (COMMUNICATIVE GOAL box) naming what the learner will be able to do after completing this unit, written as a first-person capability: "I will be able to greet people and exchange basic personal information in formal and informal settings." The goal drives every subsequent element in the unit; content that does not serve the goal does not appear in the unit.

**Element 2 — Dialogue**
An authentic dialogue between two or more speakers in the target language, set in a plausible real-world scenario that exemplifies the communicative goal. Length: 8 to 16 speaker turns. Presentation: speaker label in the source language (e.g., "Maria:" or "Customer:"), followed by the target-language utterance, followed by a source-language translation on the next line in a lighter or italic style, followed (for non-Latin-script languages) by the pronunciation transcription on a third line. Register labels appear at the head of the dialogue (FORMAL, INFORMAL, or MIXED). The Domain Master certifies that the dialogue reads as natural to a native speaker of the declared regional variant.

**Element 3 — Vocabulary Block**
A two-column premium-color table: TARGET LANGUAGE WORD/PHRASE (with pronunciation if non-Latin) in the left column; SOURCE LANGUAGE TRANSLATION with register label (F for formal, I for informal) in the right column. 20 to 40 items per unit; every item that appeared in the dialogue is included; additional thematic items extending the communicative goal are added. Items are grouped by semantic category or part of speech within the table; the grouping is noted in the caption above the table. No invented words or forms; every entry is verified by the Domain Master.

**Element 4 — Grammar Point**
One grammar point per unit, no exceptions. The grammar explanation is written in the SOURCE language for clarity. It follows this internal structure: (a) the rule stated plainly in one or two sentences; (b) three to five example sentences in the target language, each followed by its source-language translation; (c) a common mistake note in a COMMON MISTAKE box if learners of this source-language background reliably make a specific error with this grammar point; (d) a brief note on how the point interacts with the unit's vocabulary and dialogue. The Applied Linguist confirms that the grammar point is sequenced appropriately and that the rule statement is accurate. The Domain Master confirms that the examples are natural and correct.

**Element 5 — Drills**
Three to five exercises that give the learner immediate practice with the vocabulary and grammar point of the unit. Drill types permitted: substitution drill (replace one element of a given sentence), translation drill (translate source-to-target or target-to-source), completion drill (fill in the missing word or phrase from a vocabulary prompt), question-and-answer drill (answer a target-language question using the unit vocabulary), and transformation drill (change a formal sentence to informal, or singular to plural, etc.). Each drill carries a clear instruction in the SOURCE language. The answer key for all drills appears in the back matter under the ANSWER KEY division, organized by unit and drill number. No fill-in-the-blank item is ambiguous (only one correct answer per blank, or all acceptable alternatives are listed in the key).

**Element 6 — Cultural Note**
A CULTURAL NOTE box of 100 to 150 words providing factual, specific, sourced cultural information relevant to the unit's communicative goal and scenario. Cultural notes describe customs, etiquette, social conventions, or regional facts that will help the learner interact appropriately with native speakers of the declared target region. The Cultural Consultant sources every note; no cultural claim is invented or generalized from stereotype. Sources are not cited inline but are recorded in the production ledger and verified at Gate 1. Prohibited: stereotyping, generalizations applied to all speakers of a language, political commentary, religious commentary not directly relevant to the communicative goal, and any content that would embarrass or demean any community.

**Unit Length Band:** Each unit runs 4 to 8 pages on the render, measured from the COMMUNICATIVE GOAL heading through the last line of the CULTURAL NOTE box. Shortfalls are corrected with substantive content (add vocabulary items, extend the dialogue, add a drill); overages are corrected by scope adjustment (trim vocabulary to the communicative goal, tighten dialogue). Neither is solved in the typography.

**Back Matter**

| Section | Purpose |
|---|---|
| ANSWER KEY | Answers to all drill items, grouped by unit and drill number; brief and unambiguous |
| GLOSSARY | Alphabetical bilingual two-column table: target-language terms (with pronunciation) in the left column, source-language definitions and register labels in the right; covers all vocabulary introduced across all units |
| APPENDIX A: Verb Conjugation Tables | For languages with complex conjugation systems; tables for the verb classes and tenses introduced in the units; sourced from standard grammars; Domain Master verified |
| APPENDIX B: Pronunciation Reference | Full pronunciation guide for the target language in the declared regional variant; IPA or the declared pronunciation system; all phonemes with source-language approximations and minimal-pair examples |
| APPENDIX C: Suggested Resources | Real, verifiable resources only: authoritative dictionaries, grammar references, official language institutions, reputable language-learning platforms, and where applicable the language's official standards body |

**Sequence (full manuscript order)**
Title page; Copyright and Disclaimer; Table of Contents; Introduction; Unit 1 through Unit N; ANSWER KEY; GLOSSARY; APPENDIX A; APPENDIX B; APPENDIX C.

---

## Interior Design

**Page Geometry:** Inherits UAPF default. Trim 8.5 by 11 inches. Margins 0.8 inch all four sides. No running heads.

**Body Typography:** Times New Roman 11pt, 1.15 line spacing, fully justified for prose. Left-aligned for dialogue utterances, vocabulary tables, drills, and the answer key. Target-language text in the body and in dialogue may require a secondary font if the script requires it; the secondary font is declared in the Script and Typographic Profile and used consistently.

**Bilingual Dialogue Presentation:** Speaker label bold; target-language utterance at full weight; source-language translation on the following line in italics or a distinguishing style (declared in the Title Design Signature); pronunciation line (if used) in a lighter weight below the translation. Consistent vertical spacing between turns: 120 twips before each speaker label.

**Vocabulary Block Tables:** Header row: primary fill, white bold labels — in the target language for the left column header, source language for the right. Body rows alternating white and F2F7FC. Caption above in the Caption style. Every table flush to 9936 DXA text width; columns sum exactly to the table width.

**Grammar Point Section:** Headed by a Heading 2 subchapter using the verbatim string "Grammar: [Point Name]" so it enters the Contents and is findable. Example sentences in the target language in bold or a distinguishing style; source-language translations in italic on the following line.

**Box Styles (UAPF default box anatomy):**
- COMMUNICATIVE GOAL box: theme color title bar; body states the first-person goal
- COMMON MISTAKE box: caution-tone color (declared in Title Design Signature); common error shown in target language with correction
- CULTURAL NOTE box: neutral accent color; 100 to 150 words; source citation recorded in production ledger, not printed inline
- EXAM TIP box: not used in OV-LANG (no exam; replaced by USAGE TIP box for register or idiomatic notes)
- USAGE TIP box: highlights idioms, regional usage, or false cognates

**Color Tier:** PREMIUM COLOR, WHITE paper. Grayscale requires an explicit recorded operator override.

**Non-Latin Script Rendering:** Verified visually on the rasterized render at every Gate 1 per-unit audit. Right-to-left text is encoded correctly (not visually approximated). Script rendering failure is FAIL at Gate 1 and blocks advancement.

**Folio:** Visible page numbering begins at the Introduction as Arabic page 1. Front matter carries no visible folio. Folio is always a live native page number field.

---

## Content Rules

**Native-Speaker Audit at Gate 1 — Zero Tolerance for Machine-Translation Artifacts**
Every target-language string in the manuscript — every dialogue turn, every vocabulary item, every grammar example sentence, every drill item, every answer key entry, every glossary entry, every cultural note — is audited by the Domain Master (native speaker of the target language) before the unit clears Gate 1. Machine-translation artifacts (awkward syntax, calqued expressions, unnatural collocations, wrong register, culturally foreign phrasings) are a Gate 1 FAIL. The Domain Master does not merely scan; they read every item for naturalness as a native speaker would encounter it. A unit with any machine-translation artifact is returned to revision and re-audited before it advances.

**Direction Discipline**
Explanations, instructions, drill prompts, cultural notes, and the answer key are written in the SOURCE language. The language being taught appears only as target-language content: dialogues, vocabulary items, grammar examples, and drills. The two languages are never mixed within a sentence of instruction; a sentence is either a source-language explanation or a target-language exemplar, never a hybrid.

**Register Labeling**
Every vocabulary item is labeled for register (F: formal; I: informal; N: neutral/both) in the vocabulary block table. Every dialogue is labeled at its head for overall register. Grammar explanations note when a rule applies differently across registers. The declared Register Scope governs: if the book is informal-only, formal-only items do not appear; if both are included, labeling is exhaustive and consistent throughout.

**Regional Variant Discipline**
The declared regional variant is applied consistently from first to last page. Variant-specific vocabulary, spelling, pronunciation, and social conventions reflect the declared region. Where a word or form differs significantly between variants (e.g., "vosotros" in Castilian Spanish vs. "ustedes" in Latin American Spanish), the declared variant's form is used and the variant difference is noted in a USAGE TIP box. The Cultural Consultant confirms regional accuracy for all cultural notes, scenarios, and social conventions.

**Grammar Point Sequencing**
No unit introduces more than one grammar point. Grammar points are sequenced by the Applied Linguist from foundational to complex across the unit arc. A grammar point is not introduced in a unit before the vocabulary needed to exemplify it has been introduced. No invented grammar rules, no oversimplifications that would mislead the learner about how native speakers actually use the language.

**Vocabulary Load Management**
20 to 40 new vocabulary items per unit for adult beginner-to-intermediate levels; the Applied Linguist sets the exact count per unit based on the audience level and the unit's communicative scope. Vocabulary items introduced in one unit are recycled in subsequent units (in dialogues, grammar examples, and drills) to support retention. No vocabulary item appears in the glossary without having been introduced in a unit.

**Pronunciation System Consistency**
The declared pronunciation system (IPA, romanization, simplified phonetic respelling) is applied to every new vocabulary item in the vocabulary block, to every new word in the dialogue that carries an unusual or non-transparent pronunciation, and to every grammar example sentence involving pronunciation-significant forms. The system is never mixed with an undeclared alternative.

**Cultural Note Standards**
Every cultural note is factual and specific: it names a specific custom, region, situation, or social fact, not a generalization about all speakers of the language. Notes are sourced in the production ledger. Stereotyping, political commentary, religious commentary beyond what is directly relevant to a communicative situation, and any claim that would demean any cultural group are prohibited. The Cultural Consultant approves every note.

**Drill Integrity**
Every drill item has one correct answer, or the answer key lists all acceptable alternatives. Ambiguous fill-in-the-blank items (where multiple answers are grammatically and semantically possible but the key lists only one) are defects and are rewritten. Drill items recycle the unit's vocabulary and grammar point and do not introduce new vocabulary without defining it.

**Content Standards Rule**
The catalog-wide content standards rule holds in every dialogue, vocabulary item, drill scenario, cultural note, and image prompt: no pork or pig derivatives, no alcohol in any form, no alcohol-centric scenarios or settings, anywhere, including image content. Dialogue scenarios that would naturally involve alcohol (restaurant ordering, social events) are set in contexts where non-alcoholic options are the default or where alcohol is not the focus.

**Compliance Sweep**
Zero em dashes; zero en dashes; curly apostrophes only; no AI voice phrasing; no meta-references to the production process in reader-facing text. The compliance sweep adapts to the source language's typography as specified in the Language Profile Card. For source languages other than English, the Language Profile Card governs the correct punctuation, quotation, and number conventions, and those conventions govern over the English defaults stated in this niche skill.

**No Invented Sources in Suggested Resources**
Every resource in Appendix C is real and verifiable: dictionaries published by named publishers, grammar references by named authors and publishers, official language institutions (e.g., Real Academia Espanola, Institut francais, Goethe-Institut), and reputable platforms with confirmed existence. No invented textbook titles, no invented authors, no invented institutions.

---

## QA Checklist

**Gate 1 — Configuration and Per-Unit Native-Speaker Audit**

*Configuration checks (run once, at Phase 0 close):*
- [ ] OV-LANG routing signals confirmed and recorded
- [ ] Direction Declaration completed: SOURCE language and regional variant locked; TARGET language and regional variant locked
- [ ] Register Scope declared and recorded
- [ ] Script and Typographic Profile declared; non-Latin font confirmed if required; right-to-left encoding plan confirmed if required
- [ ] Pronunciation System Declaration recorded
- [ ] Children's Category Research completed; if children's signals present, title routes OV-KIDS
- [ ] Title Clearance record exists with live sources and date; no conflict pending
- [ ] Language Profile Card locked
- [ ] Subtitle compliant: communicative promise or accurate count; letters/numerals/spaces only; two lines or fewer
- [ ] Byline fetched live from FNG; collision check passed; no credentials or invented biography; locked
- [ ] Title Design Signature cleared distinctness gate
- [ ] Unit plan drafted: communicative goal, grammar point, vocabulary domain, dialogue scenario, cultural note topic, drill types per unit; Applied Linguist reviewed
- [ ] Package closed; Table of Contents plan presented; Proceed gate active

*Per-unit native-speaker audit (runs after every unit; ALL target-language content is audited here):*
- [ ] Domain Master (native speaker of TARGET language) has read every target-language string in the unit: dialogue, vocabulary block, grammar examples, drills, drill answers
- [ ] Zero machine-translation artifacts: PASS (any artifact is FAIL; unit returns to revision and re-audits)
- [ ] Vocabulary items: all correct, all labeled for register, all matching the declared regional variant
- [ ] Grammar point: rule stated accurately; examples natural and correct; Domain Master confirmed
- [ ] Dialogue: natural and culturally plausible for the declared regional variant; Cultural Consultant confirmed
- [ ] Cultural note: factual, specific, sourced in production ledger; Cultural Consultant confirmed; no stereotyping
- [ ] Register labeling: exhaustive and consistent throughout the unit; correct against declared Register Scope
- [ ] Pronunciation transcription: applied to all new items; system is the declared system applied consistently
- [ ] Drill integrity: every item has one correct answer or all alternatives listed in the answer key; no ambiguous items
- [ ] Bilingual Copy Editor review: no mistranslations; grammar explanations accurate in source language; consistency between vocabulary block and appearances in dialogue and drills
- [ ] Compliance Sweep PASS: em dashes absent, en dashes absent, curly apostrophes only, no AI voice
- [ ] Content Standards Check PASS
- [ ] Amazon Content Policy Scan PASS
- [ ] Unit length measured on render: 4 to 8 pages; correction via substantive content or scope adjustment only
- [ ] Non-Latin script rendering verified on rasterized render if applicable
- [ ] Box anatomy: COMMUNICATIVE GOAL, vocabulary table, grammar section, drills, CULTURAL NOTE all present and correctly formatted
- [ ] Subchapter flow law: no unit heading stranded with fewer than six lines of opening text; keep-with-next binding confirmed
- [ ] Proceed gate active

**Gate 2 — Back Matter**
- [ ] ANSWER KEY complete: every drill item in every unit answered; grouped by unit and drill number; unambiguous
- [ ] GLOSSARY: every vocabulary item introduced across all units is present; alphabetically ordered; register labels consistent; Domain Master verified
- [ ] APPENDIX A (Verb Conjugation Tables): tables present for all verb classes and tenses introduced; sourced from standard grammars; Domain Master verified; no invented forms
- [ ] APPENDIX B (Pronunciation Reference): all phonemes of the target language in the declared regional variant covered; IPA or declared system; source-language approximations accurate
- [ ] APPENDIX C (Suggested Resources): every resource is real and verifiable; no invented titles, authors, or institutions
- [ ] Content Standards Check PASS across all back matter
- [ ] Compliance Sweep PASS across all back matter
- [ ] Proceed gate active

**Gate 3 — Two-Pass Contents and Assembly**
- [ ] Two-pass Contents gate: build with provisional folios; extract folios by heading; write map; rebuild; re-extract; printed equals actual for every entry; no "undefined" strings
- [ ] Folio: live native page number field; front matter pages carry no visible folio; Introduction is page 1
- [ ] Table of Contents entries: Introduction; every unit (Heading 1) and its six elements as subchapters (Heading 2); ANSWER KEY; GLOSSARY; each Appendix by full title
- [ ] Non-Latin script rendering re-verified on the full assembled artifact
- [ ] Strip sweep: no IMAGE PROMPT blocks in the delivered file (or prompt blocks are the intended deliverable on PROMPTS ONLY host and none are missing); opening and closing table tags balance; marker string absent
- [ ] Proceed gate active

**Gate 4 — Final QA**
- [ ] Full gate register above re-run on the complete artifact
- [ ] Contrast verification: every foreground-background pair computes to at least 4.5:1
- [ ] Byline appears in exactly two interior locations: title page and copyright attribution; no credentials or invented biography
- [ ] Suggested Resources (Appendix C): every citation confirmed real and verifiable
- [ ] No invented statistics, claims, or attributions anywhere in the manuscript or marketing surfaces
- [ ] Operator Zero Correction Standard: the delivered manuscript requires no manual formatting correction
- [ ] Release record written

---

## KDP Positioning

**Amazon Category Tree (primary):** Books > Foreign Language Study and Reference > [Target Language]
Examples: Books > Foreign Language Study and Reference > Spanish; Books > Foreign Language Study and Reference > Arabic; Books > Foreign Language Study and Reference > Japanese

**Secondary Category:** Books > Education & Teaching > Schools and Teaching > Language Arts > [target language family] when the audience is learners in an educational context; or Books > Travel > [Region] when the title is a phrasebook targeting travelers.

**Description Lead:** The description leads with the direction (source language to target language), the communicative promise (what the learner will be able to do after completing the book), the unit count or vocabulary/phrase count, the conversational and cultural focus, and the regional variant covered. The description names the declared regional variant to set accurate expectations.

**Metadata Signals:**
- Title and subtitle carry the target language name and the communicative promise
- Keywords target: the target language name, "[language] for [source language] speakers," "learn [language]," "[language] phrases," "[language] grammar," "[language] vocabulary," "conversational [language]," the declared regional variant when it is a significant search signal (e.g., "Brazilian Portuguese," "Castilian Spanish," "Levantine Arabic")
- The description and keywords avoid any claim of fluency or proficiency guarantees

**Back Cover (if applicable):** States the communicative promise prominently; lists the unit count and the total vocabulary or phrase count; names the regional variant; highlights the native-speaker-verified content and the cultural notes feature. No invented endorsements, no invented test scores, no claims of guaranteed fluency.

---

## Key Rules — Do NOT Break

1. **Direction Declaration is a Phase 0 hard requirement.** No subtitle candidates are composed, no unit plan is drafted, no byline is fetched, and no other Phase 0 step proceeds until the SOURCE language, TARGET language, and both regional variants are declared and locked. This rule has no exception.

2. **Domain Master must be a native speaker of the TARGET language.** The Domain Master is not the editor, not the Applied Linguist, not the session itself. Every target-language string in the manuscript requires Domain Master sign-off before the unit clears Gate 1. Fluency is not nativeness; this role requires a native speaker.

3. **Zero tolerance for machine-translation artifacts.** Any target-language string that reads as unnatural to a native speaker of the declared regional variant is a Gate 1 FAIL. The unit returns to revision and is re-audited. There is no partial pass.

4. **One grammar point per unit, no exceptions.** The Applied Linguist sequences the grammar syllabus. Introducing two or more grammar points in a single unit overloads the learner and violates the unit architecture. Surplus grammar content is moved to a subsequent unit or to a USAGE TIP box as supplementary context, not as a second grammar point.

5. **Register must be labeled exhaustively.** Every vocabulary item in the vocabulary block carries a register label (F, I, or N). Every dialogue carries a register label at its head. This rule exists because a learner who uses informal language in a formal context may cause serious social offense; the book is responsible for making register transparent.

6. **Regional variant discipline is absolute.** The declared regional variant governs every vocabulary item, every grammar example, every dialogue setting, and every cultural note. Content that belongs to a different regional variant is not used as a substitute and is not introduced without explicit labeling as a variant note.

7. **Unit architecture is fixed and sequential.** The six elements — Communicative Goal, Dialogue, Vocabulary Block, Grammar Point, Drills, Cultural Note — appear in this order in every unit. No element is omitted and no additional elements are inserted between them. The order exists because each element builds on the one before it pedagogically.

8. **No invented sources in Appendix C.** Every resource listed in Suggested Resources is real, verifiable, and confirmed to exist at the time of production. This is an extension of the universal prohibition on invented citations.

9. **Content standards rule is absolute throughout.** No pork, no alcohol, no associated scenarios, in any dialogue, vocabulary item, drill scenario, cultural note, or image. Language books frequently use food and social scenarios; every such scenario in this book is designed from the outset to comply with this rule, not retrofitted.

10. **Cultural notes are factual and specific, never stereotypical.** A cultural note describes a named practice, custom, or social convention with specificity. Notes that generalize about "all speakers of [language]" or that reduce a culture to a stereotype are defects. The Cultural Consultant is the final authority on cultural content.

11. **No credentials or invented biography for the byline.** The pen name receives no language credentials, no claimed teaching history, no claimed country of origin, no claimed level of fluency, and no claimed native-speaker status, on any surface of the book or its marketing.

12. **Non-Latin script rendering is verified visually on the rasterized render.** A script that appears correct in the source file may render incorrectly in the converted PDF. Visual verification on rasterized pages is a Gate 1 and Gate 4 requirement; text-only inspection returns UNVERIFIED and blocks advancement.

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
