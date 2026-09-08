---
name: uapf-niche-history
description: History & Politics niche overlay (OV-HIST) — invoked by uapf-phase0-router when the title signals historical narrative, political analysis, biography of a historical figure, war, empire, revolution, or civilization.
---

# UAPF Niche: History & Politics (OV-HIST)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-History-Edition/` (config, validation, phases, and deterministic ops in `genie_history.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 History Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** Title or subject line contains any of the following signals — history, historical, politics, political, war, revolution, empire, civilization, biography (of a historical figure), ancient, medieval, modern history, political science, dynasty, colonialism, Cold War, independence, uprising, republic, monarchy, parliament, statecraft, diplomacy, military campaign, resistance, conquest, nation-building, social movement, civil rights (historical framing), ideology, totalitarianism, democracy, dictatorship, geopolitics.

---

## Expert Panel

Activate all four roles simultaneously at Phase 0. Each role reviews output independently before content advances.

1. **Domain Master — Period & Regional Historian**
   The lead authority for the book's specific historical period and geography. Responsible for chronological accuracy, sourcing standards, and interpretive framing. All factual claims are cleared through this role. If the book spans multiple periods or regions, note primary and secondary period specialties at intake.

2. **Historiographer**
   Reviews how the book positions itself within existing scholarship. Identifies the dominant historiographical schools relevant to the subject (e.g., Annales school, subaltern studies, Marxist historiography, diplomatic history, new military history). Ensures the book acknowledges major interpretive debates rather than presenting one school's consensus as universal fact. Guards against unacknowledged presentism — reading past events through contemporary moral or political frameworks without flagging the anachronism.

3. **Regional & Cultural Perspective Specialist**
   Ensures non-Western, subaltern, and marginalized voices are integrated where the subject demands it. Challenges Eurocentric or victor-centric framing. Flags when the book's scope silences groups who were present and affected. Not a DEI checkbox — a historiographical necessity. Active on all books regardless of subject geography.

4. **Narrative & Developmental Editor**
   Maintains readability, chapter flow, narrative momentum, and accessible prose without sacrificing scholarly rigor. Calibrates reading level and vocabulary to the stated audience. Flags passages that read as dry data dumps rather than engaged history writing. Ensures transitions between chronological sections carry explanatory connective tissue.

5. **Quotation Authentication Specialist** (activated when any direct quotation appears)
   Verifies every direct quotation attributed to a historical figure. Misattributed quotes are epidemic in popular history — this role cross-references primary sources, established critical editions, and reliable secondary scholarship before any quote is included in the manuscript. Applies the rule: if a quotation cannot be traced to a primary or high-confidence secondary source, it is omitted or flagged as "attributed to X; original source unverified."

---

## Phase 0 — Title Analysis

Execute all steps in order before any content generation begins.

### 0.1 — Title Integrity & Trademark Screen

- Confirm the exact title as provided. Do not alter it without explicit user instruction.
- Run trademark risk check: does the title duplicate an active, widely-recognized history title in the same subject space? Note any close conflicts and present them to the user.
- Confirm: is the title the working title only, or final? If working, flag that subtitle generation (Step 0.3) may need revision.
- Confirm manuscript language (default: English). If non-English, flag for localization handling.

### 0.2 — Sub-Niche Classification

Identify the primary sub-niche from the classification matrix below. Record it in the Intake Report. A single book may carry one primary and one secondary sub-niche.

| Sub-Niche Code | Sub-Niche Name | Examples |
|---|---|---|
| HIST-MIL | Military History | Battle histories, campaign narratives, military biography |
| HIST-POL | Political History & Political Science | Government systems, political movements, elections, ideologies |
| HIST-SOC | Social & Cultural History | Daily life, social movements, cultural shifts |
| HIST-BIO | Historical Biography | Lives of rulers, reformers, revolutionaries, thinkers |
| HIST-WLD | World & Comparative History | Civilizational surveys, cross-cultural comparison |
| HIST-REG | Regional & National History | Single-country or single-region narrative histories |
| HIST-ANC | Ancient & Classical History | Pre-medieval, classical civilizations |
| HIST-MED | Medieval History | 5th–15th century European and global |
| HIST-MOD | Early Modern History | 15th–18th century |
| HIST-CON | Contemporary & Modern History | 19th century–present |
| HIST-ORL | Oral & Indigenous History | Community-sourced, oral tradition, indigenous perspectives |
| HIST-DIP | Diplomatic & International History | Treaties, foreign policy, international relations |
| HIST-ECO | Economic History | Trade, finance, labor, industrialization |

### 0.3 — Subtitle Generation

Generate three subtitle options calibrated to:
- The confirmed sub-niche
- The primary audience (general reader vs. scholarly vs. student)
- The Amazon category target
- Keyword density for discoverability

Each subtitle must: (a) clearly signal the book's scope, (b) avoid hyperbole ("definitive," "complete," "ultimate" require exceptional justification), (c) not duplicate any major title already ranked in the target Amazon category.

Present all three options with rationale. User selects or instructs revision.

### 0.4 — Auto-Configuration

Record and lock the following before Phase I proceeds:

- **Period Scope:** [start year/era] to [end year/era]
- **Geographic Scope:** [regions, nations, or global]
- **Primary Sub-Niche:** [code from matrix]
- **Secondary Sub-Niche (if any):** [code or NONE]
- **Audience Calibration:** General / Academic / Student / Crossover
- **Tone Register:** Narrative / Analytical / Survey / Polemic (note: polemic requires explicit user instruction and disclosure)
- **Contested Status Flag:** YES/NO — does the subject include events, figures, or interpretations that are actively contested among historians? If YES, contested-event protocol is mandatory throughout.
- **Quotation Volume:** LOW (<5 direct quotes expected) / MEDIUM (5–20) / HIGH (>20). HIGH activates the Quotation Authentication Specialist for every chapter.
- **Primary Source Access:** Does the project include uploaded primary sources, archival documents, or research files? YES activates Hybrid Research mode.
- **Image Policy:** History books strongly benefit from maps, timelines, period illustrations, and document facsimiles. At intake, confirm: (a) will images be included, (b) will they be AI-generated, licensed, or public domain archival, (c) how many per chapter.
- **Page Target:** Based on comparable Amazon titles in the sub-niche. Standard range: 200–350 pages for general audience; 300–500 pages for comprehensive survey; 150–250 pages for focused narrative. Confirm at intake.

### 0.5 — Intake Report Output

Produce a structured Intake Report block before proceeding. Format:

```
INTAKE REPORT — OV-HIST
Title: [exact title]
Subtitle (selected): [subtitle]
Sub-Niche: [code] — [name]
Period Scope: [X to Y]
Geographic Scope: [X]
Audience: [General / Academic / Student / Crossover]
Tone Register: [Narrative / Analytical / Survey]
Contested Status: [YES — protocol active / NO]
Quotation Volume: [LOW / MEDIUM / HIGH]
Primary Source Access: [YES — Hybrid Research / NO — Direct/Web Research]
Image Policy: [included / excluded; type; count per chapter]
Page Target: [XXX pages]
Expert Panel Roles Activated: [list all 4 or 5]
```

User must confirm or correct the Intake Report before Phase I begins.

---

## Book Architecture

### Chapter Formula

History books under OV-HIST use one of three structural architectures depending on sub-niche and audience. Identify at Phase 0 and lock:

**Architecture A — Chronological Narrative** (default for HIST-MIL, HIST-REG, HIST-CON, HIST-ANC, HIST-MED, HIST-MOD)
- Introduction: Establishes scope, thesis, and reader orientation. 1,500–2,500 words. Does NOT summarize the book chapter by chapter — orients the reader to the historical problem.
- Chapters follow strict chronological sequence with clear date-range headers.
- Each chapter: one discrete chronological segment with a narrative arc (context → event → consequence).
- Chapter length: 3,500–6,000 words for general audience; up to 8,000 for academic.
- Chapter count: 8–16 chapters depending on page target.
- Conclusion: 1,500–2,000 words. Draws interpretive threads together. States what the history means — not merely what happened.

**Architecture B — Thematic Analysis** (default for HIST-POL, HIST-SOC, HIST-ECO, HIST-DIP)
- Introduction: Stakes the analytical claim. 1,500–2,500 words.
- Each chapter addresses one thematic pillar (e.g., economic forces, class structure, ideological shift, institutional change).
- Chapters are not strictly chronological but carry internal chronological logic.
- An opening chronological overview chapter (Chapter 1) is mandatory to anchor readers temporally before thematic analysis begins.
- Chapter length: 4,000–7,000 words.
- Conclusion: synthesizes themes and advances the book's central argument.

**Architecture C — Biographical Narrative** (default for HIST-BIO)
- Introduction: Places the subject in historical context. Why does this life matter to the history being told?
- Chapters follow the arc of the subject's life with contextual historical chapters intercalated as needed.
- Chapter count: 10–18 chapters.
- Each chapter carries a dual obligation: life events AND historical context. Neither strand dominates to the exclusion of the other.
- Conclusion: Legacy and historical significance. Not hagiography — assess the subject's failures and limits honestly.

### Structural Units

Every chapter must contain:
- **Opening Hook:** A specific scene, moment, quotation (authenticated), or document that draws the reader in. NOT a summary of what the chapter will cover.
- **Historical Context Block:** Establishes conditions prior to the chapter's main events.
- **Narrative/Analytical Core:** The chapter's primary content — events, arguments, evidence, analysis.
- **Primary Source Integration:** At least one direct engagement with primary source material per chapter (document, letter, speech, law, census, account). If no primary sources are available, secondary evidence must be cited explicitly.
- **Interpretive Commentary:** The author's voice synthesizing what the material means — not merely recounting facts.
- **Bridge/Transition:** Last paragraph carries the reader forward to the next chapter without summarizing the next chapter's content.

### Page-Band Targets

| Audience | Page Range | Word Count Equivalent |
|---|---|---|
| General Narrative | 200–280 pages | 60,000–85,000 words |
| Comprehensive Survey | 280–400 pages | 85,000–120,000 words |
| Academic Monograph | 300–500 pages | 90,000–150,000 words |
| Focused Short History | 150–220 pages | 45,000–65,000 words |

### Front Matter Requirements

All front matter items are mandatory unless marked optional:

1. Title Page (title, subtitle, author name — no publisher branding for KDP self-pub)
2. Copyright Page (year, author name, ISBN placeholder, "All rights reserved," disclaimer)
   - **Mandatory History Disclaimer:** "While every effort has been made to ensure historical accuracy, historiographical interpretation varies. Readers are encouraged to consult primary sources and additional scholarship. Views expressed in analytical passages represent the author's interpretation of available evidence."
3. Dedication (optional)
4. Acknowledgments (optional; mandatory if oral history contributors or archival institutions are cited)
5. Preface (1 page maximum — author's relationship to the subject, why they wrote it)
6. A Note on Sources / A Note on Terminology (mandatory when: the book uses contested terminology, transliterations, or anachronistic labels; the book relies substantially on a specific source type)
7. Table of Contents (auto-generated with correct Word heading hierarchy)
8. List of Maps / List of Figures (mandatory if images are included)
9. Introduction (begins on Arabic page 1)

### Back Matter Requirements

1. Conclusion (final body chapter — substantive, not a summary)
2. Epilogue (optional — used for "what happened next" material that falls outside the book's period scope)
3. Appendices (optional but recommended for: timelines, key figures lists, primary document excerpts, statistical tables)
4. Notes / Endnotes (mandatory when any factual claim requires citation; Chicago author-date or footnote style; confirm at intake)
5. Bibliography (mandatory; divided by: Primary Sources / Secondary Sources / Online & Archival Sources)
6. Glossary (mandatory when the book introduces 10+ specialized terms, foreign-language terms, or technical political/military vocabulary)
7. Index (note for KDP: full index is strongly recommended for non-fiction; provide index entry guidance)

---

## Interior Design

### Trim Size
- Standard: 6 x 9 inches (most common for narrative non-fiction and history on Amazon KDP)
- Alternative: 5.5 x 8.5 for shorter focused histories
- Academic: 7 x 10 for heavily illustrated or reference works

### Typography
- Body text: 11–12pt serif (Times New Roman, Garamond, or Georgia)
- Chapter titles: 18–22pt, bold
- Section headers within chapters: 14pt, bold
- Sidebars or callout boxes (if used): 10–11pt, set in box with subtle border
- Block quotations (extended primary source excerpts): indented 0.5 inch left and right, 10–11pt, single-spaced
- Footnotes/endnotes: 9–10pt

### Spacing & Layout
- Body text: 1.15–1.25 line spacing
- Chapter starts on new page (mandatory)
- No widow/orphan lines
- Running headers: book title (verso) / chapter title (recto)
- Page numbers: bottom center or bottom outside margin

### Maps & Visual Elements
- Maps are strongly recommended for military history, regional history, empire/colonial history, and any book covering territorial change.
- AI-generated map prompts: specify geographic scope, time period, key locations/boundaries, and label requirements.
- Placement: immediately before or within the chapter where the geography is discussed.
- Caption format: "Map [N]: [Descriptive Title]. [Time period if relevant]. [Source if licensed.]"
- Timelines: recommended for books spanning more than 50 years; placed in Appendix or Chapter 1.

### Color
- KDP standard: black and white interior (most economical and accessible)
- Premium color interior: only if maps or illustrations are central to the book's value proposition; significantly increases print cost
- Default recommendation: black and white body; advise color only when user confirms

### Sidebars & Callout Boxes (optional but recommended)
Use for: Key Figure Profiles, Primary Source Spotlights, Historiographical Debate Boxes, Timeline Inserts, "What Happened Next" context boxes.
Format consistently throughout the manuscript.

---

## Content Rules

### The Foundational Obligation
History books are non-fiction. Every factual claim — date, name, event, casualty figure, quotation, treaty term, election result — is subject to verification. Claims that cannot be substantiated must be flagged as uncertain, attributed to a specific source, or omitted.

### Contested Event Protocol (mandatory when Contested Status = YES)

When a topic, event, figure, or interpretation is actively debated among professional historians:

1. **Name the contest explicitly.** Do not choose one interpretation and present it as settled fact. Example: "Historians disagree about the primary causes of X. [School A] argues [position]. [School B] contends [position]. The evidence reviewed here suggests [author's assessment], though this remains a matter of ongoing scholarly debate."
2. **Present the strongest version of each major position.** Steel-man, do not straw-man, competing interpretations.
3. **Cite the interpretive tradition, not just a single scholar.** "The revisionist school, associated with [names], argues..." is more transparent than attributing an interpretation to one source.
4. **Flag at chapter level.** Each chapter that engages contested material opens with a brief acknowledgment of the interpretive complexity.
5. **Do not resolve what scholarship has not resolved.** The book may advance an argument, but must be transparent that it is an argument.

Examples of inherently contested subjects (activate protocol automatically):
- Causes of major wars (WWI, WWII, American Civil War)
- Genocide recognition and classification
- Colonial and imperial legacy assessments
- Revolutionary violence and terror (French Revolution, Russian Revolution, etc.)
- Historical figures with sharply divided legacies (Churchill, Stalin, Mao, Columbus, etc.)
- Electoral integrity claims in recent history
- Casualty and atrocity figures in disputed conflicts

### Quotation Authentication (mandatory for all quotations)

**The Rule:** Every direct quotation attributed to a historical figure must be traceable to a primary source or a high-confidence critical edition before inclusion.

**Process:**
1. State the quotation and the attributed source.
2. Identify the primary source (speech transcript, letter, diary, published work).
3. If the primary source is unavailable or the attribution is disputed, apply one of two options:
   - Option A: Omit the quotation entirely.
   - Option B: Include with explicit caveat: "Often attributed to [Name], though the original source has not been definitively established."
4. Never include a quotation because it is "famous" or "widely repeated" without verification. Misattributed quotes are common vectors of misinformation in popular history.

**High-Risk Misattribution Categories:**
- Quotes attributed to Lincoln, Churchill, Einstein, Twain, Gandhi, Mandela — these figures are among the most frequently misattributed in popular circulation.
- Translated quotations from non-English languages — verify the translation is from the original, not a secondary translation.
- Social media-era "historical quotes" — treat all such citations with high suspicion.

### Chronology Audit

Before any chapter is considered complete:
- Verify all dates are internally consistent across the manuscript.
- Cross-check event sequence: does the chapter's chronology align with established historical record?
- Flag anachronisms: are any technologies, institutions, or concepts attributed to a period before they existed?
- Confirm correct calendar system where relevant (Julian vs. Gregorian transition, non-Western calendar systems).

### Presentism Guard

**Definition:** Presentism is the error of applying contemporary moral, political, or cultural standards to past actors and events without acknowledging the anachronism.

**The Rule:** The book may and should make moral assessments of historical events and actors. It must not do so without acknowledging the historical context in which those actors operated. The assessment must be clearly framed as the author's interpretive position, not as an objective fact.

**Acceptable:** "By contemporary human rights standards, the treatment of enslaved people under [X system] constitutes severe and systematic abuse. Within [period] colonial discourse, however, this was normalized and legally sanctioned — a fact that complicates but does not excuse the historical record."

**Unacceptable:** Treating contemporary political debates as settled historical verdicts, or conversely, refusing to make any moral assessment of historical atrocities in the name of "objectivity."

### Audience Calibration

| Audience | Vocabulary | Citation Style | Narrative vs. Analysis Balance |
|---|---|---|---|
| General | Accessible prose, define technical terms | Endnotes optional; bibliography mandatory | Narrative-forward, analysis integrated |
| Academic | Technical vocabulary acceptable | Footnotes/endnotes mandatory; full bibliography | Analysis-forward, narrative as evidence |
| Student | Clear, scaffolded prose | Consistent citations, further reading lists | Balanced; pedagogical framing |
| Crossover | Accessible prose, scholarly rigor, minimal jargon | Endnotes preferred | Narrative-forward with analytical depth |

### The Fatal Flaw to Avoid

**Factual assertion without evidence base.** History books published without citation infrastructure (at minimum a bibliography; ideally notes) fail credibility standards and invite negative reviews on Amazon that destroy the title. Every book produced under OV-HIST must include at minimum a bibliography. Endnotes are strongly recommended for any claim that is not common knowledge.

The second fatal flaw: **narrative collapse into list-of-facts.** A history book that merely recites dates, names, and events without interpretive connective tissue is not history writing — it is a timeline. Every chapter must advance an argument or narrative arc.

---

## QA Checklist

### Gate 1 — Intake & Configuration Gate
Before any content is generated:

- [ ] Title confirmed and trademark-screened
- [ ] Subtitle selected and approved
- [ ] Sub-niche code locked in Intake Report
- [ ] Period and geographic scope defined
- [ ] Audience and tone register confirmed
- [ ] Contested Status flag set (YES/NO)
- [ ] Quotation Volume flag set (LOW/MEDIUM/HIGH)
- [ ] Primary Source Access confirmed
- [ ] Image policy confirmed
- [ ] Page target set
- [ ] Expert panel roles all activated
- [ ] Architecture (A/B/C) selected and confirmed
- [ ] Intake Report output produced and user-confirmed

### Gate 2 — Structure & Outline Gate
Before chapter writing begins:

- [ ] Table of Contents complete with all chapters, front matter, and back matter
- [ ] Chapter titles reflect period/theme scope (not generic: "Chapter 3: The War" is inadequate — use "Chapter 3: The Escalation of Conflict, 1914–1915")
- [ ] Page allocation per chapter reviewed against page target
- [ ] Image/map placement markers embedded in TOC
- [ ] Front matter and back matter structure confirmed
- [ ] Notes and bibliography style confirmed (Chicago, APA, or other)
- [ ] Chronological architecture: dates and sequence verified for internal consistency before writing
- [ ] Contested chapters identified and flagged in outline
- [ ] Quotation plan: known quotations listed and queued for authentication

### Gate 3 — Chapter Content Gate
Applied to every chapter before it advances:

- [ ] Opening hook is specific and engaging (not "In this chapter we will...")
- [ ] Historical Context Block present
- [ ] Primary source material integrated (minimum one engagement per chapter)
- [ ] All direct quotations authenticated or flagged per protocol
- [ ] Contested material handled per Contested Event Protocol
- [ ] Presentism Guard applied — anachronistic moral framings are either contextualized or removed
- [ ] Chronology audit: dates consistent with adjacent chapters and with historical record
- [ ] Regional/cultural perspective reviewed — whose voices are absent and why?
- [ ] Chapter ends with interpretive synthesis, not a list summary
- [ ] Bridge transition to next chapter present
- [ ] Word count within target range
- [ ] No factual claim made without a citable basis (note in endnote or attribute to source in text)

**Sub-niche-specific Gate 3 additions:**

*HIST-MIL — Military History:*
- [ ] Order of battle figures cross-checked (unit sizes, casualty counts are frequent error sites)
- [ ] Geographic descriptions consistent with verified maps
- [ ] Command structure accurately represented
- [ ] Technology and tactics are period-accurate (no anachronistic weapons or doctrine)

*HIST-POL — Political History:*
- [ ] Electoral results, vote counts, and seat distributions verified
- [ ] Constitutional and legal citations accurate
- [ ] Political party positions accurately represented without partisan framing
- [ ] Contemporary political analogies used sparingly and flagged as analogies, not equivalences

*HIST-BIO — Historical Biography:*
- [ ] Birth/death dates confirmed from primary sources
- [ ] Personal anecdotes traceable to memoir, diary, or contemporaneous account
- [ ] Psychological interpretation clearly framed as interpretation, not fact
- [ ] Subject's failures and contradictions addressed honestly (no hagiography)

*HIST-ORL — Oral & Indigenous History:*
- [ ] Oral testimonies cited by contributor name, date, and context of recording (with consent confirmed)
- [ ] Community review protocol noted (has the community reviewed content about their history?)
- [ ] Western academic framing does not override indigenous epistemological frameworks

### Gate 4 — Manuscript Completion Gate
Before Amazon KDP submission:

- [ ] All chapters complete and Gate 3 passed
- [ ] Chronology audit conducted across full manuscript — dates internally consistent
- [ ] Quotation master list: all direct quotations authenticated or appropriately caveatted
- [ ] All contested topics handled per protocol; no false consensus presented as settled
- [ ] Bibliography complete: primary sources, secondary sources, archival/online sources listed separately
- [ ] Endnotes/footnotes complete and formatted correctly
- [ ] Glossary complete (if applicable)
- [ ] All images/maps have captions and rights confirmed
- [ ] Disclaimer language on copyright page is present and correct
- [ ] Eight-reviewer critical analysis conducted (see Expert Panel); all Critical and Important issues resolved
- [ ] Front matter and back matter complete and in correct order
- [ ] Word count matches page target
- [ ] KDP metadata (description, keywords, categories) prepared

---

## KDP Positioning

### Amazon Category Strategy

Primary and secondary category placement by sub-niche:

| Sub-Niche | Primary Category | Secondary Category |
|---|---|---|
| HIST-MIL | Books > History > Military History | Books > History > [specific war/period] |
| HIST-POL | Books > Politics & Social Sciences > Politics & Government | Books > History > [relevant period] |
| HIST-SOC | Books > History > Social History | Books > Politics & Social Sciences > Social Sciences |
| HIST-BIO | Books > Biographies & Memoirs > Historical Biographies | Books > History > [relevant period/region] |
| HIST-WLD | Books > History > World History | Books > History > Ancient History / Medieval History (as fits) |
| HIST-REG | Books > History > [Americas / Europe / Asia / Africa / Middle East / etc.] | Books > History > [sub-period] |
| HIST-ANC | Books > History > Ancient History | Books > History > World History |
| HIST-MED | Books > History > Medieval History | Books > History > [Europe / Middle East / Asia] |
| HIST-MOD | Books > History > Early Modern History | Relevant regional category |
| HIST-CON | Books > History > Modern History | Books > History > [relevant region or war] |
| HIST-ORL | Books > History > Social History | Books > Politics & Social Sciences > Social Sciences > Anthropology |
| HIST-DIP | Books > History > Historical Study & Educational Resources | Books > Politics & Social Sciences > Politics & Government > International Relations |
| HIST-ECO | Books > Business & Money > Economic History | Books > History > [period] |

### Description Framework

Amazon book description structure for history titles (follows "Above the Fold / Below the Fold" principle):

**Above the Fold (first 200 characters — most critical):**
- Open with a hook that establishes historical stakes: a moment, a question, a paradox, or a claim about why this history matters now.
- Do NOT open with "This book..." or the book title.
- Signal the period and geography within the first sentence.

**Below the Fold (full description, ~400–600 words):**
Para 1: The historical problem or period — what happened and why it matters.
Para 2: What the book offers — its approach, the evidence it draws on, the angle it takes.
Para 3: Reader takeaways — what readers will understand after reading that they did not before.
Para 4 (optional): Praise structure or comparison — "Essential reading for fans of [comparable title/author]."
Close: Call to action with keywords naturally embedded.

**Description keywords to embed (select the most relevant):**
- Period-specific: ancient Rome, World War II, Cold War, Civil War, Renaissance, Enlightenment, etc.
- Theme-specific: military strategy, political power, social revolution, colonial history, etc.
- Audience signals: "accessible history," "narrative history," "comprehensive account," "scholarly yet readable"
- Format signals: "includes maps," "illustrated history," "with timeline," "fully cited"

### Backend Keywords (7 slots, 50 characters each)

Generate 7 backend keyword strings at Phase 0 based on sub-niche and title signals. Prioritize:
- Specific period + event combinations (e.g., "Western Front 1914 trench warfare")
- Geographic + thematic combinations (e.g., "Roman Empire fall political causes")
- Audience-intent phrases (e.g., "best history books for beginners", "history books adults")
- Question-format phrases readers search (e.g., "why did the Roman Empire fall")
- Comparable author signals if title is in a competitive space

---

## Key Rules — Do NOT Break

1. **Factual claims require a citable basis.** No history book produced under OV-HIST may contain a factual claim (date, person, event, statistic) that does not have a citable source. If the source is unavailable, the claim must be hedged explicitly: "According to some accounts..." or "Estimates vary, but..."

2. **Contested events must be presented WITH their contested status.** Presenting one historiographical interpretation as settled consensus when professional historians actively dispute it is a category error. The book may advance an argument — it must not disguise an argument as fact.

3. **Quotation authentication is mandatory.** Every direct quotation attributed to a named historical figure must be traceable to a primary or high-confidence secondary source before inclusion. Famous-but-unverified quotes are omitted or explicitly caveated. No exceptions.

4. **The chronology audit is not optional.** Before the manuscript advances past Gate 3, all dates and event sequences must be verified for internal consistency and accuracy against the historical record. Date errors in history books generate immediate negative reviews.

5. **Presentism must be guarded, not eliminated.** The goal is not to avoid moral judgment — historians make moral assessments and should. The goal is to contextualize judgments within their historical frame and to clearly identify analytical assessments as interpretations, not objective facts.

6. **All four expert panel roles must complete their review before Gate 3 closes.** No chapter is certified without input from the Domain Master, Historiographer, Regional Perspective Specialist, and Narrative Editor. When quotation volume is MEDIUM or HIGH, the Quotation Authentication Specialist review is also required.

7. **Architecture is locked at Phase 0 and does not change mid-manuscript.** Switching from chronological to thematic architecture mid-book creates structural incoherence. If the user wants to change architecture, stop, reissue the TOC, and restart from Gate 2.

8. **Bibliography is mandatory.** A history book without a bibliography is not a history book. A minimum bibliography of at least 15 sources is required for any book under 200 pages; proportionally more for longer works. Primary sources must be listed separately from secondary sources.

9. **Do not use secondary-source summaries as if they were primary-source access.** If the book is using a historian's account of what a primary source says, attribute it to the historian. Do not write "Caesar wrote that..." if the actual access is through a modern historian's translation and commentary — write "As [Modern Historian] translates Caesar's account..."

10. **No hagiography in biographical history.** Every historical biography must address the subject's failures, contradictions, and the limits of their influence or virtue. A biography that presents a historical figure as uniformly admirable without complication is not history — it is propaganda.

11. **Regional and subaltern perspectives are structural obligations, not optional additions.** If the book's subject involves colonized peoples, enslaved persons, occupied populations, or marginalized groups, those perspectives must be integrated into the narrative, not mentioned in passing or relegated to a single chapter.

12. **The Oral & Indigenous History sub-niche (HIST-ORL) requires additional ethics review.** Books drawing on oral testimony or indigenous community history must address consent, attribution, and community ownership of cultural knowledge. Do not proceed past Gate 2 for HIST-ORL projects without confirming the ethics and attribution framework.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
