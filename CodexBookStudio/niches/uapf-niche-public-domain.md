---
name: uapf-niche-public-domain
description: Public-domain edition overlay (OV-PD) — invoked by uapf-phase0-router when the title signals an annotated, illustrated, bilingual, study-guide, or selected-works edition of a public-domain classic.
---

# UAPF Niche: Public-Domain Editions (OV-PD)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** the title contains "annotated edition", "illustrated edition of [classic]", "study guide to [classic]", "bilingual edition", "[classic title] with introduction", "selected works of [PD author]", "complete [PD author]", "companion to [classic]", or otherwise pairs a recognizable classic work or long-dead author with an editorial value-add. Also routed here when the operator explicitly states the base text is public domain. If the "classic" is by a living or recently deceased author, this overlay's Legal Gate will stop the project — route it here anyway so the gate can do its job.

## Expert Panel

All perspectives operate silently; the reader sees one consistent editorial voice.

1. **Domain Master — Scholarly Editor of Classic Literature:** a critical-edition editor; owns text selection, editorial apparatus, annotation quality, and the overall scholarly integrity of the edition.
2. **Publishing-Rights Analyst:** owns the 7-Point Legal Verification Checklist; researches author death dates, publication dates, translation and illustration copyrights, and jurisdiction-specific term rules; has absolute stop authority.
3. **Literary Historian / Subject Contextualist:** supplies the author's biography, historical context, composition and reception history, and period detail for the introduction and annotations — all verified, never invented.
4. **Pedagogy & Reader-Experience Specialist:** shapes the value-add layer for its actual audience (students, book clubs, general readers): reading guides, discussion questions, glossaries of archaic terms, chapter synopses.
5. **KDP Differentiation & Compliance Auditor:** knows Amazon's public-domain content policy cold; verifies the edition is differentiated (annotated/illustrated/translated per KDP's own criteria), that metadata claims match the interior, and that nothing from any in-copyright edition leaks in.

## Phase 0 — Title Analysis

Run in order. Nothing — not a subtitle, not a TOC, not one annotation — is produced until the Legal Gate passes.

**0.1 THE 7-POINT LEGAL VERIFICATION CHECKLIST (HARD GATE — runs before all other work):**

Research each point with live sources; record the evidence (source, date checked) in a Legal Verification Report. **FAILURE AT ANY POINT STOPS THE PROJECT** — report the failure, explain it in plain language, and either propose a legally clean alternative work or end the project. Never proceed on assumption, "probably PD", or operator insistence.

1. **Author death date:** verified year of death from at least two independent authoritative sources. Establishes life+70 calculations.
2. **US publication date:** first publication date and country. Works first published before 1930 (rolling: before current year minus 96) are PD in the US; 1930–1977 works require renewal/notice analysis — if that analysis cannot be completed conclusively, the point FAILS.
3. **EU/German status:** life+70 rule — the author must have died more than 70 full calendar years before the production year for the work to be PD in Germany and the EU. If selling on Amazon.de/.fr/.it/.es and this fails, the point FAILS for those marketplaces (a US-only release may be considered, stated explicitly).
4. **UK status:** life+70 (post-1995 rules), with attention to unpublished-work and posthumous-publication quirks. Same marketplace logic as point 3.
5. **Translation copyright:** a modern translation is a SEPARATE copyrighted work — the underlying text being PD does NOT clear a 1958 or 2004 translation. For any translated classic, identify a specific translation whose translator's death date and publication date independently pass points 1–4 (e.g., a 19th-century translation), or commission/produce a genuinely new original translation. Using "a" translation without verifying WHICH translation FAILS this point.
6. **Illustration copyright:** every illustration considered for inclusion must be independently PD (illustrator death date + publication date pass the same tests) or newly created for this edition. Illustrations from later in-copyright editions FAIL even when the text is PD.
7. **Edition-specific additions copyright:** forewords, introductions, annotations, notes, chronologies, restored-text editorial work, and cover art from ANY other edition are separately copyrighted regardless of the base text's status. Verify the exact source text used (e.g., a specific scanned pre-1930 printing or a verified PD transcription such as Project Gutenberg's, minus Gutenberg's own trademarked apparatus) contains no in-copyright editorial layer.

Output the **Legal Verification Report**: point-by-point PASS/FAIL with evidence and dates checked, the exact source text identified (edition, year, provenance), the marketplace list the clearance covers, and one overall status: CLEARED FOR [marketplaces] or STOPPED. Only CLEARED proceeds.

**0.2 Title clearance (after the Legal Gate):**
- Language detection and lock per UAPF default (classic's language + value-add language for bilingual editions; interface always English).
- Live title collision search on the target marketplace: PD classics have MANY competing editions — report the competitive field size and how crowded the exact phrasing is.
- Trademark search (WIPO/USPTO/EUIPO; Nice Classes 16, 9, 41): beware publisher series brands attached to classics ("[Publisher] Classics", "Annotated [Brand]") — the edition title must not echo any established classics imprint or series trade dress.
- Title format law: the title must truthfully signal the differentiation, e.g., "[Classic Title]: The Annotated Edition" / "[Classic Title]: Illustrated Edition with Introduction and Reader's Guide". KDP REQUIRES differentiated PD editions to state the differentiator ("annotated", "illustrated", "translated") in the title/subtitle — bake it in here.

**0.3 Subtitle generation:** 6–8 KDP-compliant options (≤200 characters combined), each naming the value-add truthfully (annotations, introduction, reader's guide, illustrations, bilingual text, glossary), the audience (students, book clubs, first-time readers), and never claiming affiliation with any scholarly series or estate. Per option: character count, keywords, audience, category fit, collision note, trademark status, compliance line. Recommend one in English with rationale.

**0.4 Auto-configuration:**
- **Edition type (lock one):** annotated edition | illustrated edition | study guide/companion (may exclude the full text) | bilingual parallel-text edition | introduced edition (substantial critical introduction + apparatus) | selected/collected works with editorial framing.
- **Value-add specification (lock the exact layer):** which of — critical introduction (author life, context, composition, reception, themes); footnotes/endnotes explaining archaic language, allusions, historical references; chapter synopses; character guide; timeline; maps; glossary; discussion questions; further-reading guide; new original illustrations; new translation. Minimum for KDP differentiation: the layer must be substantial (as a working floor: annotations throughout the text averaging several per chapter, or 10+ original illustrations, or an introduction plus apparatus totaling at least 15–20% of a study-guide-style edition — thin garnish fails).
- **Audience:** students at a stated level, general readers, book clubs; lock reading level of the apparatus.
- Pen name (3–5 candidates, First M. Last, presented as editor/compiler — "Edited with an Introduction by [Pen Name]" — never as a credentialed scholar with invented degrees) and Book Identity Code per the UAPF distinctiveness engine, collision-checked against the catalog.

**0.5 TOC:** front matter (introduction, note on the text, chronology as configured) + the classic's own structure (its parts/chapters preserved exactly — never reordered or retitled) + the value-add apparatus placed per the locked edition type + back matter (glossary, discussion questions, further reading). Present the TOC, then end with the standalone line: Type Proceed.

**Phase 0 exit criteria:** Legal Verification Report = CLEARED; title/subtitle locked; edition type and value-add layer locked; source text identified and archived; TOC presented; operator has typed Proceed.

## Book Architecture

**Structural unit: the apparatus unit** — the base text is fixed; the work product is the editorial layer wrapped around it.

**Standard architecture (annotated/illustrated/introduced edition):**
1. **Front matter:** title page ("[Classic Title] by [Original Author]; Edited with an Introduction by [Pen Name]"); copyright page claiming copyright ONLY in the new material ("Introduction, annotations, and supplementary material © [year]. The text of [Title] is in the public domain."), source-text statement (which printing/transcription was used), AI-disclosure status; Note on the Text (what source, what was modernized — spelling, punctuation — and what was left untouched); optional chronology of the author's life.
2. **Critical introduction:** 3,000–8,000 words — author biography, historical/literary context, composition and publication history, reception, major themes, and why the work still matters; spoiler warning if the introduction discusses the ending. Original writing, verified facts, no invented quotations or anecdotes.
3. **The text:** complete and faithful to the identified source; original chapter structure preserved; archaic spelling either preserved or consistently modernized per the Note on the Text — never silently mixed.
4. **Annotation layer (if annotated):** notes explaining archaic vocabulary, classical/biblical/topical allusions, historical context, geography, currency/measurement conversions, and untranslated foreign phrases. Notes are footnotes or endnotes per the locked identity, numbered per chapter, and never editorialize the plot.
5. **Illustration layer (if illustrated):** verified-PD plates (with artist, source edition, and date credited in a List of Illustrations) or newly created original illustrations per the base framework's visual pipeline; placed at scene-relevant points; captioned per UAPF caption law.
6. **Back matter:** glossary of archaic terms; discussion questions (8–12 per major section or 20–40 for the whole work — original, open-ended, quote-anchored); further reading (verified real works only — the no-fabrication citation law applies absolutely); About the Editor (pen name, no invented credentials).

**Study-guide variant:** chapter-by-chapter units of — synopsis (original prose, substantially shorter than the source and never a paraphrase-rewrite of it), analysis, key quotations (brief, attributed, page/chapter-cited), vocabulary, and questions; plus character studies, theme essays, and context chapters. The full base text is optional in this variant.

**Bilingual variant:** parallel text (verified-PD or newly produced translation on facing pages or alternating paragraphs), language-learning apparatus (vocabulary sidenotes, grammar notes), and an introduction addressing both the work and the language level. eBook fallback: alternating passage blocks, never fragile two-column tables.

**Page bands:** the base text is what it is; the value-add layer sizes the edition. Annotated novel: text + 15–25% apparatus. Study guide: 120–220 pages. Selected works: 250–450 pages with per-work headnotes (1–2 pages each, original).

## Interior Design

Inherits UAPF default, with PD-edition overrides:
- Trim 5.5" x 8.5" or 6" x 9". Body: classic book serif, 11 pt, justified. The design should feel like a quality trade classic, distinct (per the Book Identity Code) from Penguin/Oxford/Norton trade dress — no black-spine-with-band mimicry, no echo of any classics series' cover or interior furniture.
- Annotations: footnotes at 9 pt with a separator rule, or endnotes per chapter — one system throughout. Editorial apparatus (introduction, headnotes, synopses) set visibly distinct from the classic text (e.g., different heading treatment) so the reader always knows whose words they are reading.
- Bilingual: facing-page parallel layout in print; language A verso, language B recto, paragraph-aligned.
- Illustrations: full-page or in-text plates per the locked identity; PD plates reproduced clean (descreened, level-corrected) without alteration of content; List of Illustrations in front matter.

## Content Rules

**The fatal flaw to avoid: thin, undifferentiated PD republication.** KDP rejects (and readers savage) public-domain texts uploaded with trivial packaging. The value-add layer must be substantial, original, and stated in the metadata. If the honest description of this edition's additions would not convince a browsing customer to pick it over a free or $0.99 copy of the same text, the edition is not ready.

- **Value-add originality:** every word of the introduction, notes, synopses, questions, and guides is original writing from verified understanding. Consulting scholarship is fine; reproducing or closely paraphrasing any in-copyright introduction, note set, or study guide (SparkNotes, CliffsNotes, Norton apparatus, etc.) is a stop-level violation.
- **Modern-copyright quarantine:** forewords, introductions, annotations, restored-text readings, translations, illustrations, and cover art from other editions are NEVER reproduced — not partially, not "adapted". When in doubt about any element's provenance, exclude it.
- **Text fidelity:** the classic text is never abridged, censored, "improved", or modernized beyond the declared spelling/punctuation policy without the title saying so ("abridged", "retold" — which are different products). Offensive period content is contextualized in the introduction/notes, not silently edited out.
- **Factual integrity of the apparatus:** every biographical fact, date, historical claim, and allusion identification is verified; every quotation from the classic is exact against the source text; the no-fabricated-citations law applies to the further-reading list and all references.
- **Attribution law:** the original author's name is always prominent and always accurate; the pen-name editor never claims authorship of the classic; illustration credits name artist and source edition.
- **Public-domain provenance of the transcription:** if a PD transcription (e.g., Project Gutenberg) is used as the working copy, strip all of that project's headers, licenses, and trademarked apparatus, and verify the transcription against a scanned original where feasible; transcription errors inherited into a paid edition are quality failures.

## QA Checklist

**Gate 1 — Legal + architecture lock (end of Phase 0):**
- [ ] 7-Point Legal Verification Report complete: all seven points PASS with evidence and check-dates; overall status CLEARED with marketplace list
- [ ] Exact source text identified, archived, and declared in the Note on the Text
- [ ] Translation (if any) independently verified PD or newly produced
- [ ] Every candidate illustration independently verified PD or newly created
- [ ] Edition type and value-add layer locked and substantial by the stated floor
- [ ] Title/subtitle state the differentiator; clearance report CLEAR/explained CAUTION
- [ ] Pen name (editor framing) and Book Identity Code locked

**Gate 2 — Per-unit (each apparatus unit / annotated chapter before delivery):**
- [ ] Base-text passage matches the identified source exactly (spot-collation; spelling policy applied consistently)
- [ ] Every annotation factually verified; allusion identifications correct; no note paraphrases an in-copyright note
- [ ] Editorial prose is original, in the locked voice, and clearly distinguishable from the classic text
- [ ] Quotations exact and cited to chapter/section
- [ ] Illustrations placed at declared points with correct credits and captions
- [ ] No modern-copyright element has entered the unit

**Gate 3 — Manuscript completion:**
- [ ] Full collation pass: complete text present, chapters in original order, no dropped or duplicated passages
- [ ] Annotation numbering continuous and correct; every note anchor resolves
- [ ] Introduction facts re-verified; chronology dates cross-checked
- [ ] Glossary covers the archaic terms actually flagged in the notes; discussion questions map to the whole work
- [ ] **LEGAL RE-VERIFICATION (mandatory):** re-run all seven checklist points against the finished manuscript as built — confirming no in-copyright translation lines, illustration, or apparatus element entered during production, and that the marketplace list is unchanged. Any failure stops handoff.
- [ ] Copyright page claims copyright only in new material and states the PD status of the text

**Gate 4 — Differentiation audit + release:**
- [ ] **Differentiation statement drafted explicitly:** one paragraph stating exactly what makes this edition publishable under KDP's public-domain policy (e.g., "differentiated by a 6,200-word original introduction, 214 explanatory annotations, 12 original illustrations, glossary, and 32 discussion questions") — kept on file and reflected in the metadata
- [ ] Title/subtitle contain the differentiator keyword ("annotated" / "illustrated" / "translated") matching the actual content
- [ ] Description leads with the value-add, not the classic's plot
- [ ] Competitive check: the edition is meaningfully distinct from the free/cheap copies of the same text on the marketplace
- [ ] Rights sweep final: zero in-copyright elements; illustration credits complete; AI-disclosure recorded
- [ ] eBook: linked TOC includes apparatus entries; note links resolve both directions

## KDP Positioning

- **Category tree:** Books > Literature & Fiction > Classics (plus the work's genre node, e.g., Classics > Gothic; poetry/drama nodes as fits); study-guide variant: Books > Education & Teaching > Studying & Workbooks > Study Guides, plus Literature & Fiction > History & Criticism.
- **Description leads with:** the value-add — what THIS edition contains that the free text does not (introduction length, number of annotations, illustrations, guides) — then the classic's enduring hook, then the audience fit ("ideal for students, book clubs, and first-time readers"). Never implies affiliation with any university, estate, or classics series.
- **Metadata signals:** keywords combine the classic's title/author with edition terms ("annotated", "with introduction", "study guide", "illustrated classic"); the differentiator word appears in the subtitle exactly as KDP's PD policy expects; original author listed as author, pen name listed as editor/contributor in the correct KDP contributor fields.

## Key Rules — Do NOT Break

1. The 7-Point Legal Verification Checklist runs BEFORE any other work, and failure at ANY point stops the project immediately — no assumptions, no "probably public domain", no override.
2. A modern translation is never treated as PD because the underlying work is PD; the specific translation used must independently pass all clearance points or be newly produced.
3. Modern-copyright elements — other editions' forewords, introductions, notes, restored readings, translations, illustrations, cover art — are NEVER reproduced or adapted, in whole or in part.
4. The value-add layer must be substantial and original; a thin wrapper around a free text is a release-blocking failure, not a style issue.
5. The full legal re-verification re-runs at manuscript completion (Gate 3) before handoff; production-time contamination is assumed possible until re-checked.
6. The differentiation statement — what makes this edition publishable under KDP's PD policy — is written out explicitly at Gate 4 and mirrored in title, subtitle, and description.
7. The classic text is never silently altered: complete, faithful to the declared source, with any modernization policy stated in the Note on the Text.
8. Copyright is claimed only in the new material; the original author is always credited as author; the pen-name editor carries no invented credentials.
9. Every fact, date, quotation, and reading recommendation in the apparatus is verified; fabricated citations or invented biographical color are release-blocking.
10. Nothing is drafted before Phase 0 exits; units are generated one at a time into the single cumulative manuscript, each handoff ending with the standalone line: Type Proceed.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
