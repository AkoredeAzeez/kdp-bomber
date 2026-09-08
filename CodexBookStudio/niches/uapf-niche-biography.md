---
name: uapf-niche-biography
description: Biography, Memoir & True Crime niche overlay (OV-BIO) — invoked by uapf-phase0-router when routing signals match a single life, collective profiles, personal memoir, as-told-to narrative, or true crime case.
---

# UAPF Niche: Biography, Memoir & True Crime (OV-BIO)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** Title or subject line contains any of the following signals — biography of [person], memoir, life of [person], true crime, [person]'s story, 50 women who, 100 people who, collective biography, murder of [victim], criminal case, the [criminal] story, killer, detective, unsolved, cold case, as told to, my life, my journey, I survived, confession of, the making of [person], portrait of [person], inside the mind of, remembered, untold story of, the woman who, the man who, [name]'s secret, [name] unmasked, [name] revealed.

**Boundary with OV-HIST:** If the subject is historical (deceased before 1920, primarily known through primary sources and archival scholarship), route to OV-HIST (HIST-BIO sub-niche). If the subject is living, recently deceased (post-1920), or the book is a memoir, route here. When in doubt and the book's primary value proposition is historical context rather than personal life, route to OV-HIST. When the primary value is the individual human story, route here.

---

## Expert Panel

Activate all five roles simultaneously at Phase 0. Each role reviews output independently before content advances.

1. **Domain Master — Subject Researcher & Biographer**
   The lead authority on the book's specific subject, era, and field. Responsible for accuracy of biographical facts, chronological integrity, source quality, and interpretive framing. All factual claims about the subject's life, actions, statements, and relationships are cleared through this role. For collective biographies, verifies each profile individually against available sources. For True Crime, verifies all case facts against court records and credentialed journalism.

2. **Legal & Privacy Counsel**
   Reviews all content involving living persons, private individuals, and recently deceased subjects for defamation risk, privacy violations, and fair comment standards. Mandatory for any living subject, any person who has not voluntarily entered public life, any content making specific allegations of criminal conduct or moral failing. Clears statements of opinion as opinion, not fact. Flags any passage that could constitute defamation per se (false statements of fact that damage reputation). Active for all memoir content where third parties appear as named individuals.

3. **Narrative & Developmental Editor**
   Maintains readability, chapter flow, emotional resonance, and accessible prose. Ensures biography and memoir achieve the balance between factual authority and narrative compulsion that the genre demands. Flags passages that read as dry data-recitation rather than engaged life-writing. Guards against hagiography (uncritical celebration) and hatchet jobs (uncontextualized attack). For True Crime, guards against sensationalism and ensures narrative momentum serves understanding, not voyeurism.

4. **Fact-Checker & Source Authenticator**
   Verifies every checkable claim — dates, names, places, events, statistics, outcomes, relationships. Applies OV-HIST quotation authentication rules to every direct quotation attributed to a named person. Constructs and maintains the Source Ledger (see QA Checklist). Flags claims that rest on a single unverified source. For memoir, notes claims made in first person that depend solely on the author's recollection and flags any where corroborating evidence is available and should be cited.

5. **Dignity & Ethics Reviewer**
   Mandatory activation for: all True Crime modules; any biography or memoir involving crime, abuse, trauma, or victimization; any book involving minors; any book where private individuals appear in the narrative. Runs the True Crime Dignity Battery (see Content Rules) against all relevant content. Reviews portrayals of victims, survivors, and marginalized individuals for dignity, proportionality, and humanity. Guards against perpetrator glorification and victim instrumentalization. Reviews ongoing legal proceedings for proper allegation language. Active for all books in this niche.

---

## Phase 0 — Title Analysis

Execute all steps in order before any content generation begins.

### 0.1 — Title Integrity & Trademark Screen

- Confirm the exact title as provided. Do not alter it without explicit user instruction.
- Run trademark and duplication check: does the title duplicate a currently active, widely-recognized biography, memoir, or true crime title featuring the same subject? Note any close conflicts and present them to the user.
- Confirm: is this the working title or final title? If working, flag that subtitle generation (Step 0.3) may need revision after module and sub-niche locking.
- Confirm manuscript language (default: English). If non-English, flag for localization handling.
- For collective biographies: confirm the exact count stated in the title (e.g., "50 women"). This count is locked — the manuscript must deliver exactly that many profiles.

### 0.2 — Module & Sub-Niche Classification

Identify the primary module (Biography, Memoir, or True Crime) and the specific sub-niche code. Record in the Intake Report. A book may carry one primary and one secondary sub-niche code.

**Module 1 — Biography**

| Sub-Niche Code | Sub-Niche Name | Description |
|---|---|---|
| BIO-SNG | Single-Subject Biography | Full or period biography of one person; cradle-to-grave or defined life chapter |
| BIO-COL | Collective Biography | Multiple subjects profiled under a unifying criterion (role, era, achievement, geography) |
| BIO-HIS | Historical Biography (recent) | Subject deceased post-1920; primarily secondary sources; living witnesses possible |
| BIO-LIV | Living Subject Biography | Subject is currently alive; heightened legal and privacy review required throughout |
| BIO-AUT | Authorized Biography | Written with subject's cooperation or estate approval; access advantages and potential bias risks |
| BIO-UNA | Unauthorized Biography | Written without subject's cooperation; all claims must rest on verifiable public record |

**Module 2 — Memoir**

| Sub-Niche Code | Sub-Niche Name | Description |
|---|---|---|
| MEM-AUT | Autobiography / Self-Written Memoir | Author narrates own life or a defined chapter of their own life |
| MEM-ATO | As-Told-To Memoir | Ghost-written or collaboratively written in the subject's first-person voice; collaborator must be disclosed |
| MEM-PER | Persona Memoir | Memoir written through a constructed or significantly shaped narrative voice; disclosed as persona or creative nonfiction |

**Module 3 — True Crime**

| Sub-Niche Code | Sub-Niche Name | Description |
|---|---|---|
| TC-NRT | True Crime Narrative | Single case, book-length deep dive |
| TC-COL | True Crime Collective | Multiple cases organized by theme, era, geography, or investigator |
| TC-ADT | True Crime Adapted | Content adapted or expanded from podcast, documentary, or prior published investigation; IP clearance required |

### 0.3 — Subject Status & Risk Classification

Record all that apply:

**Subject Status:**
- [ ] Subject is deceased (historical or recent)
- [ ] Subject is living — Legal & Privacy Counsel mandatory for every chapter
- [ ] Subject is a minor or was a minor at the time of events covered — Minor Protection Protocol mandatory
- [ ] Subject is a private individual who has not voluntarily entered public life — heightened privacy review
- [ ] Subject is a public figure — fair comment standard applies to their public role; private life requires separate justification for inclusion

**Contested Status:**
- [ ] Subject's legacy, actions, or character are actively disputed — contested framing protocol mandatory
- [ ] Book makes allegations of criminal, unethical, or significantly harmful conduct — allegation language and sourcing standards mandatory
- [ ] Subject or related parties are currently involved in litigation — Litigation Protocol active (see Content Rules)

**True Crime Flags (complete for Module 3 only):**
- [ ] Case status: RESOLVED / ONGOING / COLD / CONTESTED VERDICT
- [ ] Victims identified by name — Dignity Battery active
- [ ] Minors involved as victims, suspects, or witnesses — Minor Protection Protocol mandatory
- [ ] Perpetrator convicted / acquitted / awaiting trial / unknown — lock allegation language accordingly
- [ ] Case involves sexual violence — additional sensitivity and naming restrictions apply

### 0.4 — Subtitle Generation

Generate three subtitle options calibrated to:
- The confirmed module and sub-niche
- The primary audience (general reader, true crime enthusiast, literary memoir reader, scholarly)
- The Amazon category target
- Keyword density for discoverability

Each subtitle must: (a) clearly signal the book's scope and subject, (b) avoid hyperbole ("definitive," "explosive," "shocking," "scandalous" require exceptional justification and will trigger review), (c) not duplicate any major title already ranked in the target Amazon category, (d) for True Crime, not sensationalize or prejudge unresolved legal matters.

Present all three options with rationale. User selects or instructs revision.

### 0.5 — Auto-Configuration

Record and lock the following before Phase I proceeds:

- **Module:** [Biography / Memoir / True Crime]
- **Sub-Niche Code:** [from matrix]
- **Subject Name(s):** [full name(s) as they appear in the manuscript]
- **Subject Status:** [deceased / living / minor involved]
- **Contested Status:** [YES — protocol active / NO]
- **Case Status (True Crime only):** [Resolved / Ongoing / Cold / Contested]
- **Authorized/Unauthorized (Biography only):** [Authorized / Unauthorized]
- **Disclosure Required (Memoir only):** [Collaborator name / Persona disclosure statement]
- **Audience Calibration:** [General / Literary / True Crime enthusiast / Academic]
- **Architecture Selected:** [BIO-A / BIO-B / BIO-C / MEM-A / MEM-B / TC-A / TC-B — see Book Architecture]
- **Quotation Volume:** [LOW (<5) / MEDIUM (5–20) / HIGH (>20)]
- **Source Access:** [Primary sources available / Secondary sources only / Court records / Research files uploaded]
- **Image Policy:** [Included / Excluded; type; estimated count per chapter]
- **Page Target:** [XXX pages — see page-band targets]
- **Exact Profile Count (BIO-COL only):** [locked number]
- **Expert Panel Roles Activated:** [list all active roles]

### 0.6 — Intake Report Output

Produce a structured Intake Report block before proceeding. Format:

```
INTAKE REPORT — OV-BIO
Title: [exact title]
Subtitle (selected): [subtitle]
Module: [Biography / Memoir / True Crime]
Sub-Niche: [code] — [name]
Subject: [name(s)]
Subject Status: [deceased / living / minor involved / private individual]
Contested Status: [YES — protocol active / NO]
Case Status (TC only): [Resolved / Ongoing / Cold / Contested]
Authorized/Unauthorized (BIO only): [Authorized / Unauthorized]
Disclosure Required (MEM only): [YES — statement: X / NO]
Audience: [General / Literary / True Crime / Academic]
Architecture: [code and name]
Profile Count (BIO-COL only): [exact number — matches title]
Quotation Volume: [LOW / MEDIUM / HIGH]
Source Access: [type]
Image Policy: [included / excluded; type; count]
Page Target: [XXX pages]
Expert Panel Roles Activated: [list all 5 or notation if one is not needed]
Legal Flags: [list any; or NONE]
Dignity Battery: [ACTIVE — TC/victim content present / STANDBY — activate if content warrants]
```

User must confirm or correct the Intake Report before Phase I begins.

---

## Book Architecture

### Module 1 — Biography Architectures

**Architecture BIO-A — Cradle-to-Grave Chronological** (default for BIO-SNG, BIO-LIV, BIO-AUT, BIO-UNA when covering a full life)

- Introduction: Why does this life matter? Places the subject in the context that makes their story urgent now. Does NOT summarize the book chapter by chapter. Establishes the author's interpretive stance without reducing the subject to a thesis. (1,500–2,500 words)
- Chapters follow the arc of the subject's life chronologically, one defined period per chapter.
- Chapter 1 typically covers origins, family, formative context — the world into which the subject was born.
- Final body chapter covers the subject's last period, death (if deceased), or present state (if living).
- Each chapter carries a dual obligation: life events AND the historical, cultural, or professional context in which they occurred. Neither strand eliminates the other.
- Chapter length: 4,000–7,000 words (general audience); up to 9,000 for expanded treatment.
- Chapter count: 10–18 chapters depending on page target.
- Conclusion: Assessment of the life — legacy, significance, honest reckoning with failures and contradictions. Not hagiography. Not a summary. An interpretive verdict.

**Architecture BIO-B — Thematic Biography** (use when thematic exploration reveals more than strict chronology; suitable for complex or multi-faceted subjects)

- Introduction: Stakes the interpretive claim about the subject's life — what is the lens through which this life is being read?
- Chapter 1 (mandatory): A chronological orientation chapter establishing the basic arc of the subject's life so readers can navigate the subsequent thematic exploration without being lost temporally.
- Each subsequent chapter addresses a thematic dimension of the subject's life (e.g., "The Politician," "The Father," "The Revolutionary," "The Artist in Exile").
- Within each thematic chapter, internal chronological logic is maintained.
- Chapter count: 8–14 chapters.
- Conclusion: Synthesizes the thematic strands. What does the full picture of this life amount to? How does each theme inflect the others?

**Architecture BIO-C — Collective Profile Unit** (mandatory for BIO-COL; see also Collective Biography rules under Content Rules)

- Introduction: Frames the collection. Why these specific people? What criterion unites them? What portrait of a field, era, or category of human achievement do the profiles collectively paint? (1,500–2,500 words)
- Each profile follows a mandatory four-part unit structure:
  1. **Hook** — A specific moment, statement, achievement, or defining characteristic that immediately establishes why this person belongs in this collection. Not a birth-date opening. Arresting and specific. (150–300 words)
  2. **Life** — Biographical grounding: origins, formative experiences, context. Who were they before they became notable? (300–600 words, scaled to overall profile length)
  3. **Contribution** — The specific work, achievement, discovery, act, or impact that earns their place in this collection. The most substantive section. (400–800 words, scaled)
  4. **Legacy** — What endures. How the world changed because of them. Modern relevance or current standing. (200–400 words)
- Profile length must be consistent within ±10% across all subjects. No subject may receive a profile more than 2x the length of the shortest profile without documented editorial justification.
- Profile count must match the title claim exactly. "50 Women" = 50 profiles. This is verified at Gate 4.
- A brief header for each profile is standard: Name, Dates (birth–death or birth–present), Field/Role.
- Conclusion/Afterword: Draws threads across the collection. What does this group, taken together, reveal? (1,000–1,500 words)

### Module 2 — Memoir Architectures

**Architecture MEM-A — Linear Narrative Memoir** (default for MEM-AUT and MEM-ATO covering a defined life arc, crisis-and-recovery, journey, or career)

- Prologue or Opening Scene (optional but strongly recommended): Places the reader inside a defining moment — not necessarily the beginning chronologically. Creates an emotional entry point. (500–1,200 words)
- Introduction or Author's Note: Establishes the author's present-day perspective and the stakes of the story being told. Why is this being written now? What changed? (800–1,500 words)
- Chapters follow the chronological arc of the period being narrated. Each chapter is a defined segment of the journey.
- Chapters alternate between scene (showing) and reflection (the author's current understanding of past events). The reflection voice is consistently in the present tense or clearly marked temporal distance from the scene.
- Chapter length: 3,500–6,000 words.
- Chapter count: 10–16 chapters.
- Closing Chapter or Epilogue: The author's present-day state. What was learned. What changed. Not a tidy resolution if none exists — honest ambiguity is acceptable and often preferable to false closure.

**Architecture MEM-B — Thematic/Episodic Memoir** (for memoirs organized around themes, recurring experiences, places, relationships, or non-chronological reflections)

- Introduction: Frames what these episodes or themes add up to. What portrait of a life, family, or experience emerges from this arrangement?
- A chronological orientation section (brief, 500–1,000 words) is recommended early to anchor readers temporally.
- Each chapter is a self-contained episode or thematic exploration that can be read independently while contributing to the cumulative whole.
- Internal chronology within each chapter is maintained even if chapters jump across time.
- Chapters are arranged in an intentional editorial order that builds emotional and thematic resonance rather than mere chronology.
- Conclusion: Synthesis — what do these episodes mean in aggregate?

### Module 3 — True Crime Architectures

**Architecture TC-A — Single Case Narrative** (default for TC-NRT)

- **Structure Law:** The book does NOT open with the crime or with the victim's death. It opens with the world — the community, the era, the relationships — into which the crime irrupted.
- Introduction: Context-setting. The place, time, and community. The human beings who were there. (1,500–2,500 words)
- Chapter 1: The Victim(s) as people — their lives, relationships, work, identity. Introduced as human beings, not as crime cases.
- Chapter 2: The World Around the Crime — social, economic, institutional context that shaped the conditions.
- Middle chapters: The investigation, evidence, legal proceedings — in chronological order, sourced to court records and credentialed journalism.
- Penultimate chapter: Verdict, resolution, or ongoing status with current information dated.
- Final chapter: Aftermath and legacy — what changed (or didn't) in the community, the law, the investigation of similar cases.
- Conclusion: The author's reflective stance. What does this case reveal about larger systems, institutions, or human behavior? (1,000–1,500 words)
- Total length: 60,000–90,000 words for standard single-case narrative.

**Architecture TC-B — Case Portfolio** (for TC-COL and TC-ADT covering multiple cases)

- Introduction: Frames the organizing principle. Why these cases? What do they have in common — geography, era, crime type, investigator, outcome pattern? What does studying them together reveal that individual cases do not? (1,500–2,500 words)
- Each case section follows a mandatory consistent sub-structure:
  1. Context (the world before the crime)
  2. The People (victims introduced as people first)
  3. The Crime (factual account, sourced)
  4. The Investigation (law enforcement, legal proceedings)
  5. The Outcome (verdict, resolution, or current status)
  6. The Significance (what this case contributed to law, investigation, public understanding)
- Case sections must be approximately equal in length (±15%).
- Dignity Battery applied to each case individually.
- Conclusion: Cross-case synthesis — what the portfolio reveals collectively.

### Page-Band Targets

| Module / Audience | Page Range | Word Count Equivalent |
|---|---|---|
| Biography — General Reader | 220–320 pages | 65,000–95,000 words |
| Biography — Comprehensive (Long Life or Era) | 300–450 pages | 90,000–135,000 words |
| Collective Biography (profiles ×50–100) | 180–280 pages | 55,000–85,000 words |
| Memoir — Standard | 200–280 pages | 60,000–85,000 words |
| Memoir — Extended | 260–360 pages | 78,000–108,000 words |
| True Crime — Single Case | 230–320 pages | 68,000–95,000 words |
| True Crime — Case Portfolio | 220–350 pages | 65,000–105,000 words |

### Front Matter Requirements

1. Title Page (title, subtitle, author name — no publisher branding for KDP self-pub)
2. Copyright Page (year, author name, ISBN placeholder, "All rights reserved," plus mandatory disclaimers — see below)
3. Dedication (optional)
4. Acknowledgments (required when: sources, archives, interviewees, or legal counsel contributed; for MEM-ATO, collaborator is acknowledged here AND on cover)
5. Author's Note or A Note on Sources (mandatory when: book makes contested claims, reconstructs scenes, or relies on a specific source category; for True Crime, must note source types used and any exclusions)
6. A Note on Methodology (recommended for unauthorized biography and all True Crime)
7. Table of Contents (auto-generated with correct Word heading hierarchy)
8. List of Photographs / List of Figures (mandatory if images are included)
9. Introduction or Prologue (begins on Arabic page 1)

**Mandatory Copyright Page Disclaimers by Module:**

*Biography (all):*
"Every effort has been made to verify the accuracy of biographical facts. Where evidence is uncertain or contested, this has been noted in the text. The views expressed in analytical passages represent the author's interpretation of available evidence."

*Biography — Living Subject (BIO-LIV, BIO-AUT, BIO-UNA):*
"Statements made about living persons reflect the author's understanding of verifiable public record. Where allegations or interpretations are offered, they are clearly identified as such. This work does not constitute a legal finding."

*Memoir (all):*
"This is a work of memoir. It reflects the author's present recollection of experiences over time. Dialogue and scenes have been rendered to the best of the author's memory. Some names and identifying details of private individuals have been changed to protect their privacy."

*Memoir — As-Told-To (MEM-ATO):*
"Written with [Collaborator Full Name]. [Subject Name]'s story has been rendered in first person through a collaborative process. Dialogue and scenes reflect the subject's recollection and have been reconstructed from memory and available records."

*True Crime (all):*
"This work is based on court records, official statements, and credentialed journalism. Some names of private individuals have been changed or omitted. Individuals referred to as suspects or accused persons in ongoing or contested proceedings are presumed innocent unless a court of law has determined otherwise. The author does not intend to prejudge any person or proceeding."

### Back Matter Requirements

1. Conclusion or Epilogue (substantive — not a summary; the author's final interpretive word)
2. Afterword (optional — "where are they now" material or subsequent developments post-manuscript completion)
3. A Note on Sources / Author's Note on Research (mandatory for biography and true crime; explains how the book was researched, what types of sources were consulted, and what was unavailable)
4. Appendices (optional but recommended for: timelines, key figure lists, case chronologies, document excerpts, selected correspondence)
5. Notes / Endnotes (mandatory for biography and true crime; Chicago style preferred; every claim that is not personal recollection or common knowledge requires a note)
6. Bibliography (mandatory for biography and true crime; organized by: Primary Sources / Secondary Sources / Court Records & Official Documents / Journalism / Online & Archival Sources)
7. Index (strongly recommended for biography and true crime; not required for memoir)

---

## Interior Design

### Trim Size
- Standard for biography and memoir: 6 x 9 inches
- Compact for shorter memoirs or collective profiles: 5.5 x 8.5 inches
- Photo-heavy or illustrated biography: 7 x 10 inches

### Typography
- Body text: 11–12pt serif (Times New Roman, Garamond, or Georgia)
- Chapter titles: 18–22pt, bold
- Profile headers (BIO-C only): 14–16pt, bold; sub-header with dates in 12pt regular
- Section headers within chapters: 14pt, bold
- Block quotations (extended first-person passages or documented statements): indented 0.5 inch left and right, 10–11pt, single-spaced
- Reconstructed scenes: standard body text; immediately preceded by a label (see Content Rules)
- Footnotes/endnotes: 9–10pt

### Spacing & Layout
- Body text: 1.15–1.25 line spacing
- Chapter starts on new page (mandatory)
- Profile units (BIO-C): a consistent horizontal rule or section break between each profile
- No widow/orphan lines
- Running headers: book title or subject name (verso) / chapter title (recto)
- Page numbers: bottom center or bottom outside margin

### Photographs & Captions
- Photographs of the subject(s) are expected in most biography and true crime titles.
- Caption format: "[Name], [context/date]. [Credit/Source if required.]"
- For True Crime: photographs of victims are permitted only if they are dignified portraits or publicly available images that the victim's family has consented to (note consent confirmation in Source Ledger). No crime scene photographs of victims.
- All photographs placed in a grouped plate section (standard) or inline (for premium formatted editions).

### Color
- KDP standard: black and white interior (most economical)
- Black and white photograph plates: standard and acceptable
- Color plates: only when photographs are central to the book's value proposition; confirm with user; significantly increases print cost

---

## Content Rules

### The Foundational Obligation

Biography and memoir are non-fiction. Every verifiable factual claim — date, name, event, statement, relationship, outcome — is subject to verification. Claims that cannot be substantiated must be flagged as uncertain, attributed explicitly to a source, or omitted. In memoir, the author's personal recollection is the primary source for personal experience, but checkable external facts (public events, dates, other people's documented actions) must still be verified against the record.

---

### Rule 1 — No Invented Dialogue

**The Absolute Rule:** No invented, imagined, or AI-generated dialogue appears in any nonfiction module (Biography, Memoir, True Crime) without being explicitly labeled as a reconstruction.

**What "invented dialogue" means:** Any spoken or written exchange that is not documented in a primary source (recorded, transcribed, witnessed in a contemporaneous account, reproduced in memoir by a participant). This includes:
- Conversations reconstructed from memory that the author was not present for
- Exchanges reconstructed from one participant's account without corroboration
- "Plausible" conversations that might have occurred based on the historical record

**What is permitted:**
- Direct quotations from documented sources (audio, transcript, diary, memoir, contemporaneous account) — cite the source
- Dialogue reproduced from the author's own memory in memoir, labeled as memory: "As I remember it, he said..."
- Reconstructed dialogue that is explicitly labeled (see Rule 2)

**The prohibition extends to:** interior monologue attributed to third parties ("She must have thought..."), emotional states attributed as fact to persons the author did not directly observe ("He felt betrayed"), and motivation stated as established fact when it is interpretation ("Her decision was driven by jealousy").

---

### Rule 2 — Reconstructed Scenes Must Be Labeled

When a scene is reconstructed from available evidence rather than direct documentation, it must be labeled as a reconstruction at the point of introduction in the text.

**Acceptable labeling language (use in running text, not footnotes):**
- "Based on [source], the scene likely unfolded as follows:"
- "Witnesses later described what happened in the moments before:"
- "Drawing on [documents/accounts], we can reconstruct the sequence:"
- "In her memoir, [Name] recalled the conversation this way:"
- "Court records and witness statements describe the following:"

**Unacceptable:** A scene presented in present-tense or past-tense narration with full sensory detail as if the author has direct access to events they could not have witnessed, without any label distinguishing the reconstruction from documented fact.

**For True Crime specifically:** Reconstructed scenes of the crime itself require double sourcing — the reconstruction must rest on court-record evidence or credentialed forensic journalism, and must be labeled. A crime scene cannot be "dramatized" beyond what evidence supports.

---

### Rule 3 — Living Persons Protocol

All content referencing living persons is subject to the following:

**Public Figures (persons who have voluntarily entered public life):**
- Their public roles, public statements, public conduct, and publicly documented actions may be described and analyzed.
- Opinion and interpretation are permitted when clearly identified as opinion/interpretation and grounded in factual basis.
- Private life, relationships, health, and conduct not in the public record require: (a) the person's consent, or (b) direct relevance to the book's subject matter and documented evidence.
- Satire and criticism are protected; false statements of fact presented as true are not.

**Private Individuals:**
- People who have not voluntarily entered public life receive maximum privacy protection.
- Minimize naming: use first names only, composites, or changed identifying details when the individual's specific identity is not necessary to the story.
- Never include addresses, workplaces, physical descriptions, or other information that could identify or locate a private individual without their consent.
- If a private individual is central to the narrative (e.g., the author's family member in a memoir), note in Author's Note that some identifying details have been changed.

**Allegation Language:**
- Any statement that a living person committed a crime, engaged in misconduct, or acted unethically must use allegation language unless: (a) a court of competent jurisdiction has so found, or (b) the person has publicly admitted it.
- "Allegedly," "according to [source]," "was accused of," "prosecutors contend" — use these formulations consistently throughout.
- Do not alternate between allegation language and definitive language for the same claim within the same manuscript.

**Litigation Protocol:**
- If the subject of the book, or any individual named in the book, is currently a party to litigation related to the book's subject matter, the Legal & Privacy Counsel role must review every passage referencing that person before it advances past Gate 3.
- Do not characterize the outcome of ongoing litigation.

---

### Rule 4 — OV-HIST Quotation Authentication (Inherited — Mandatory)

Every direct quotation attributed to a named person — historical or living — must be traceable to a primary source or high-confidence secondary source before inclusion.

**Process:**
1. State the quotation and the attributed source.
2. Identify the primary source (recorded statement, published interview, diary, letter, published work, court transcript).
3. If the primary source is unavailable or attribution is disputed:
   - Option A: Omit the quotation entirely.
   - Option B: Include with explicit caveat: "Often attributed to [Name], though the original source has not been definitively established."
4. Never include a quotation because it "sounds right," is widely circulated, or appears on a quotes website without tracing it to its origin.

**High-Risk Misattribution Categories (OV-BIO additions):**
- Quotes attributed to subjects through third-hand biographical sources without primary documentation
- "Deathbed" statements reported by a single witness
- Interview quotes reproduced from secondary summaries rather than the original interview
- Social media posts that may have been deleted, edited, or fabricated
- Paraphrased statements presented as direct quotations

---

### Rule 5 — True Crime Dignity Battery

The Dignity Battery is a mandatory multi-point audit applied to all True Crime content (TC-NRT, TC-COL, TC-ADT) and to any biography or memoir chapter where crime, violence, victimization, or abuse are described. Each point must pass before content advances.

**Battery Check 1 — Victim Humanity First**
Every victim named in the text must be introduced first as a person (life, relationships, identity, what they cared about) before being introduced as a victim or case subject. The book does not lead with the circumstances of a victim's death, injury, or victimization when first introducing them to the reader.
- PASS: Victim is introduced with biographical context establishing them as a full human being before the crime is described.
- FAIL: Victim's identity is defined entirely or primarily by how they died or were harmed.

**Battery Check 2 — No Gore-Lingering**
Crime scene details, injuries, suffering, and death are described only to the extent required for evidentiary or narrative clarity. The text does not dwell on, elaborate, or return to graphic physical details beyond what serves the reader's understanding of the case.
- PASS: Violence is described with appropriate factual precision; the text moves on.
- FAIL: The text returns to or elaborates graphic detail beyond what the narrative requires; the writing is voyeuristic or sensationalistic.

**Battery Check 3 — Minor Protection**
Minors (persons under 18 at the time of the events described) who are victims, witnesses, suspects, or peripheral figures:
- Are not named unless they are now adults who have publicly waived anonymity (document this in Source Ledger).
- Are referred to as "a minor," "a teenager," "[first name only if adult and public]."
- Minor suspects tried as juveniles are never named under any circumstances.
- Minor victims of sexual offenses are never named under any circumstances, even if their names appear in public records.
- PASS: All minors referenced without identifying information, or with documented adult-waiver of anonymity.
- FAIL: Minor identified by name without documented adult-waiver.

**Battery Check 4 — Ongoing Case Language**
If the case is unresolved, subject to appeal, or subject to active legal proceedings:
- All references to suspects or accused persons use allegation language throughout (see Rule 3 Allegation Language).
- Presumption of innocence is stated explicitly in the Author's Note or Introduction.
- The text does not present a guilty verdict for a matter not legally adjudicated.
- Case status and date of last known legal action are noted in the Intake Report and Author's Note.
- PASS: Allegation language used consistently; case status accurately represented; presumption stated.
- FAIL: Definitive guilt language used for unresolved matters; case status misrepresented.

**Battery Check 5 — Source Integrity**
All factual claims about the case rest on permitted source types only:
- Permitted: Court records, indictments, trial transcripts, appellate decisions, sentencing documents (public record); named reporters at publications with editorial standards and fact-checking processes; official law enforcement or prosecutorial statements; academic criminology research; victim or survivor statements publicly shared.
- Prohibited: Anonymous sources presented as authoritative; social media speculation presented as evidence; unmoderated forum theories; unverified podcast or YouTube content as primary sourcing; tabloid claims not corroborated by permitted sources.
- PASS: All factual claims traceable to permitted source types in Source Ledger.
- FAIL: Factual claims resting on prohibited source types.

**Battery Check 6 — Family & Survivor Dignity**
Living family members of victims and survivors of crimes are treated with dignity:
- Their emotional states, motives, and responses are described only when they have been publicly shared by the family/survivors themselves.
- Speculation about family members' internal experiences or motives beyond public record is prohibited.
- Contact with family members or survivors for research purposes is noted in the Acknowledgments or Author's Note.
- PASS: Family and survivor treatment consistent with public record; no unverified speculation.
- FAIL: Speculation about family/survivor internal states or motives presented as fact.

**Battery Check 7 — No Perpetrator Glorification**
The book does not provide a platform that glorifies, romanticizes, eroticizes, or celebrates the perpetrator or the crime.
- Perpetrators may be analyzed psychologically, criminologically, and contextually. Their lives, motives, and actions may be examined in depth.
- The framing of the analysis does not position the perpetrator as a tragic hero, antiheroine, or romantic figure.
- The book does not use marketing or cover language that positions the perpetrator as a glamorous or compelling identity.
- PASS: Perpetrator treated as subject of rigorous analysis; no glorification in text or framing.
- FAIL: Perpetrator romanticized, glamorized, or presented as admirable for their crimes.

---

### Rule 6 — Collective Biography Profile Integrity

- The exact count stated in the title must match the exact count of complete profiles in the manuscript. Counted and verified at Gate 4.
- Each profile must include all four structural units (Hook → Life → Contribution → Legacy). A profile missing any unit is incomplete and must be revised before Gate 3 closes.
- Profile lengths must be internally consistent. If profiles vary significantly, a documented editorial rationale is required.
- No subject is excluded because their story is "too similar" to another — the selection criterion is applied equally; any exclusion after titling requires the title count to be revised.
- The introduction must explicitly state the selection criterion and how it was applied.
- Profiles must not assume reader familiarity with the subject — each profile is self-contained.

---

### Rule 7 — Hagiography & Hatchet Job Prohibition

Biography and memoir are served poorly by both uncritical celebration and uncontextualized attack.

**Hagiography** (the uncritical celebration of a subject): Every biographical subject produced under OV-BIO must have their failures, contradictions, and the limits of their influence or virtue acknowledged and examined. A biography that presents a subject as uniformly admirable without complication is not biography — it is promotional material.

**Hatchet Job** (uncontextualized or disproportionate negative treatment): Every negative characterization, allegation, or critical assessment of a subject must: (a) rest on documented evidence, (b) acknowledge context and complexity, (c) allow for the subject's own perspective where it is documented.

**The Standard:** The reader should finish the book understanding a full human being in full complexity, not a saint or a villain.

---

### Rule 8 — Memoir Voice Integrity

**As-Told-To (MEM-ATO):**
- The collaborator's presence must be disclosed on the cover ("with [Name]" or "as told to [Name]"), in the copyright notice, and in the Acknowledgments.
- The narrative voice must be consistent throughout with the subject's documented personality, speech patterns, and expressed views.
- Scenes and dialogue must reflect the subject's memory, not the collaborator's interpolation. Where the collaborator has reconstructed material from research, this must be noted.

**Persona Memoir (MEM-PER):**
- A persona memoir that narrates a real person's story through a constructed or significantly shaped voice must be disclosed as such in the Author's Note.
- The Author's Note must make clear: what is based on documented fact, what is narrative reconstruction, and what is the author's creative interpretation.
- A persona memoir that presents entirely invented material as autobiographical is a work of fiction and must be categorized as such. Do not use this sub-niche to misrepresent fiction as memoir.

---

### Rule 9 — Chronology Audit (Inherited from OV-HIST)

Before any chapter is certified complete:
- Verify all dates are internally consistent across the manuscript.
- Cross-check event sequence: does the chapter's chronology align with documented record?
- Flag anachronisms: are technologies, institutions, relationships, or concepts attributed to a period before they existed?
- Confirm age-at-event calculations for the subject (birth year + event year = age check).
- For collective biographies: verify dates for every individual profiled — birth, death, and key events.
- For True Crime: verify all dates against court records and official documentation.

---

### The Fatal Flaws to Avoid

**Fatal Flaw 1 — Unsubstantiated Factual Assertion:** Biography and true crime books published without citation infrastructure fail credibility standards and generate immediate negative reviews. Every checkable claim requires a citable source. Notes and a bibliography are mandatory for biography and true crime.

**Fatal Flaw 2 — Narrative Collapse into Chronological List:** A biography that merely recites dates, relationships, and events without interpretive connective tissue is a timeline, not a life. Every chapter must advance a portrait of the subject — who they were, how they changed, what their choices reveal.

**Fatal Flaw 3 — Dignity Failure in True Crime:** A true crime book that treats victims as plot devices, lingers on gore, or glorifies perpetrators will receive community backlash that destroys discoverability. The Dignity Battery is not optional.

**Fatal Flaw 4 — Invented Dialogue Presented as Fact:** Invented or reconstructed dialogue presented without labeling as such is a journalistic and ethical failure that exposes the publisher to criticism and, for living persons, potential legal liability.

---

## QA Checklist

### Gate 1 — Intake & Configuration Gate
Before any content is generated:

- [ ] Title confirmed and trademark/duplication-screened
- [ ] Subtitle selected and approved
- [ ] Module (Biography / Memoir / True Crime) locked
- [ ] Sub-niche code locked in Intake Report
- [ ] Subject name(s) confirmed
- [ ] Subject status determined (deceased / living / minor involved)
- [ ] Contested Status flag set (YES — protocol active / NO)
- [ ] True Crime: Case Status locked (Resolved / Ongoing / Cold / Contested)
- [ ] Authorized/Unauthorized determination (Biography only)
- [ ] Disclosure requirement determined and language drafted (Memoir only)
- [ ] Allegation Language Protocol activated if living persons or unresolved cases involved
- [ ] Dignity Battery status set (ACTIVE / STANDBY)
- [ ] Quotation Volume flag set (LOW / MEDIUM / HIGH)
- [ ] Architecture selected and confirmed
- [ ] BIO-COL: exact profile count locked and matches title
- [ ] Source access type confirmed
- [ ] Image policy confirmed
- [ ] Page target set
- [ ] All expert panel roles activated
- [ ] Mandatory disclaimers drafted and approved for copyright page
- [ ] Intake Report produced and user-confirmed

### Gate 2 — Structure & Outline Gate
Before chapter or profile writing begins:

- [ ] Table of Contents complete with all chapters, front matter, and back matter
- [ ] Chapter/profile titles reviewed — no generic placeholders (e.g., "Chapter 4: Early Life" without period specification)
- [ ] Page allocation per chapter reviewed against page target
- [ ] Front matter and back matter structure confirmed with all mandatory elements
- [ ] Notes and bibliography style confirmed (Chicago preferred; confirm at intake)
- [ ] Chronological architecture: key dates and event sequence verified for internal consistency before writing
- [ ] Contested passages identified and flagged in outline
- [ ] Quotation plan: known quotations listed and queued for authentication
- [ ] BIO-COL: profile list finalized; count confirmed against title; all four structural units mapped for each profile
- [ ] True Crime: source ledger template established; permitted source types confirmed; Dignity Battery criteria reviewed
- [ ] Reconstructed scene plan: any planned scene reconstructions noted in outline with intended sourcing
- [ ] Image/photograph placement markers embedded in outline

### Gate 3 — Chapter/Profile Content Gate
Applied to every chapter or profile before it advances:

**Universal checks (all modules):**
- [ ] Opening hook is specific, arresting, and grounded in documented fact — not invented
- [ ] No invented dialogue — all quoted speech traceable to documented source
- [ ] Any reconstructed scenes are labeled per Rule 2
- [ ] All direct quotations authenticated per Rule 4 or explicitly caveated
- [ ] Living persons content reviewed by Legal & Privacy Counsel role
- [ ] Allegation language used consistently for all unproven claims
- [ ] Chronology audit passed: dates internally consistent, age-at-event calculations correct
- [ ] Chapter/profile ends with interpretive substance, not a list summary
- [ ] Word count within target range
- [ ] Source Ledger updated: all factual claims in this chapter/profile logged with source type and citation

**Module 1 — Biography additions:**
- [ ] Subject introduced as a full human being — strengths and failures both present
- [ ] No hagiography: subject's failures and contradictions acknowledged
- [ ] No hatchet job: negative characterizations grounded in evidence and context
- [ ] BIO-LIV / BIO-AUT / BIO-UNA: Legal & Privacy Counsel sign-off on every chapter
- [ ] BIO-COL: profile includes all four units (Hook → Life → Contribution → Legacy); length within ±10% of cohort
- [ ] Psychological interpretations clearly framed as interpretation, not fact

**Module 2 — Memoir additions:**
- [ ] Author's voice consistent throughout; for MEM-ATO, voice consistent with subject's documented personality
- [ ] First-person scene vs. present-day reflection clearly distinguished (tense signals or explicit framing)
- [ ] Third parties appearing as named individuals reviewed for privacy implications
- [ ] External checkable facts verified against public record
- [ ] MEM-ATO: collaborator's interpolations noted and distinguished from subject's stated memory

**Module 3 — True Crime additions (all seven Dignity Battery checks applied to each chapter):**
- [ ] Battery Check 1 — Victim Humanity First: PASS / FAIL
- [ ] Battery Check 2 — No Gore-Lingering: PASS / FAIL
- [ ] Battery Check 3 — Minor Protection: PASS / FAIL
- [ ] Battery Check 4 — Ongoing Case Language: PASS / FAIL
- [ ] Battery Check 5 — Source Integrity: PASS / FAIL (all sources in Source Ledger are permitted types)
- [ ] Battery Check 6 — Family & Survivor Dignity: PASS / FAIL
- [ ] Battery Check 7 — No Perpetrator Glorification: PASS / FAIL
- [ ] All seven Battery Checks = PASS before chapter advances. Any FAIL requires revision and re-check.

### Gate 4 — Manuscript Completion Gate
Before Amazon KDP submission:

- [ ] All chapters/profiles complete and Gate 3 passed individually
- [ ] **Source Ledger Audit:** Complete source ledger reviewed for all chapters. All factual claims logged with source type and citation. Uncited claims resolved (source added, claim hedged, or claim removed). True Crime: all sources confirmed as permitted types.
- [ ] **Dignity Battery Full-Manuscript Pass (True Crime and victim/crime content):** All seven Battery checks run across the complete manuscript, not just chapter-by-chapter. Any cross-chapter pattern failures (e.g., consistent gore-lingering across multiple chapters that passed individually) resolved.
- [ ] **Chronology Audit Full-Manuscript Pass:** Dates verified for internal consistency across all chapters. Age-at-event calculations correct. For BIO-COL: dates verified for every profiled subject.
- [ ] **Quotation Master List:** All direct quotations listed; each authenticated or explicitly caveated; any unverifiable quotes removed or caveated.
- [ ] BIO-COL: exact profile count verified against title count — must match exactly.
- [ ] All living persons content reviewed and cleared by Legal & Privacy Counsel role.
- [ ] Allegation language consistent throughout manuscript — no drift to definitive language for unresolved claims.
- [ ] All invented dialogue — zero instances in the manuscript. Run search for: "he said," "she said," "they said," "replied," "answered," "responded" — verify each is sourced.
- [ ] All reconstructed scenes labeled per Rule 2 — verify label language is present.
- [ ] Minor Protection Protocol verified — no undisclosed minors named.
- [ ] Mandatory copyright page disclaimers present and correct for the book's module.
- [ ] MEM-ATO: collaborator disclosure present on cover, copyright page, and Acknowledgments.
- [ ] Bibliography complete (Biography/True Crime): Primary Sources / Secondary Sources / Court Records & Official Documents / Journalism — listed separately.
- [ ] Notes/Endnotes complete and formatted.
- [ ] Author's Note on Sources/Methodology present and complete.
- [ ] All photographs have captions and rights confirmed. True Crime: no undignified victim images.
- [ ] Front matter and back matter complete and in correct order.
- [ ] Word count matches page target.
- [ ] All five expert panel roles have completed their reviews for this manuscript; all Critical and Important issues resolved.
- [ ] KDP metadata (description, keywords, categories) prepared.

---

## KDP Positioning

### Amazon Category Strategy

| Sub-Niche | Primary Category | Secondary Category |
|---|---|---|
| BIO-SNG (general) | Books > Biographies & Memoirs > Specific Groups | Books > Biographies & Memoirs > Historical (if historical figure) |
| BIO-SNG (political) | Books > Biographies & Memoirs > Leaders & Notable People > Political Leaders | Books > Politics & Social Sciences > Politics & Government |
| BIO-SNG (arts) | Books > Biographies & Memoirs > Arts & Literature | Books > Arts & Photography > [relevant field] |
| BIO-SNG (science/tech) | Books > Biographies & Memoirs > Professionals & Academics > Scientists & Researchers | Books > Science & Math > [field] |
| BIO-SNG (sports) | Books > Biographies & Memoirs > Sports & Outdoors | Books > Sports & Outdoors > [sport] |
| BIO-SNG (business) | Books > Biographies & Memoirs > Rich & Famous | Books > Business & Money > [field] |
| BIO-COL | Books > Biographies & Memoirs > Specific Groups | Books > [field of subjects — History / Science / Arts] |
| BIO-HIS | Books > Biographies & Memoirs > Historical | Books > History > [relevant period/region] |
| BIO-LIV | Books > Biographies & Memoirs > Leaders & Notable People | Books > [subject's field] |
| MEM-AUT / MEM-ATO | Books > Biographies & Memoirs > Memoirs | Books > Biographies & Memoirs > Specific Groups (if subject group is identifiable) |
| MEM-PER | Books > Biographies & Memoirs > Memoirs | Creative Nonfiction sub-category if available |
| TC-NRT / TC-COL | Books > Biographies & Memoirs > True Accounts > True Crime | Books > Mystery, Thriller & Suspense > True Crime |
| TC-ADT | Books > Biographies & Memoirs > True Accounts > True Crime | Books > Mystery, Thriller & Suspense > True Crime |

### Description Framework

**Above the Fold (first 200 characters — most critical):**
- Biography: Open with the subject's defining moment or the historical paradox their life represents. Do NOT open with "This book..." or the subject's birth year.
- Memoir: Open with the emotional stakes. What did the author face? Why does it matter to the reader?
- True Crime: Open with the human impact — the community, the loss, the question the case raises. Do NOT open with the crime or gore.
- Signal the subject and genre within the first sentence. Mystery about who or what the book is about kills conversion.

**Below the Fold (full description, 400–600 words):**
Para 1: The subject and what makes their story compelling — biography (who they were and why they mattered), memoir (what the author faced and what they found), true crime (what happened and why this case).
Para 2: What the book delivers — approach, evidence, access, angle. For biography: what new sources or perspectives this brings. For memoir: the arc and what readers will experience. For true crime: the investigation's depth and what the book reveals.
Para 3: Reader takeaways — what the reader will understand, feel, or know after reading.
Para 4 (optional): "For readers of [comparable title or author]" comparison — activates recommendation algorithms and signals the book's shelf position.
Close: Call to action with keywords naturally embedded.

**Description keywords by module (select most relevant):**

*Biography:* biography, life of [name], true story of [name], compelling biography, narrative biography, [subject's field] biography, biography of [historical/political/arts] figure, authorized biography, untold story of [name]

*Memoir:* memoir, true story, personal memoir, [subject's experience] memoir, survivor memoir, inspiring memoir, first-person account, life story, autobiography

*True Crime:* true crime, murder, investigation, cold case, unsolved, detective, criminal case, true crime story, real crime, court case, justice, [crime type] true crime, [location] murder, serial killer (only if accurate and documented)

### Backend Keywords (7 slots, 50 characters each)

Generate 7 backend keyword strings at Phase 0 based on sub-niche and title signals. Prioritize:
- Subject + field combinations (e.g., "women scientists biography stories")
- Audience-intent phrases (e.g., "best biographies women leaders", "inspiring memoirs addiction recovery")
- Comparable author/title signals (e.g., "books like [comparable title]")
- Event or era combinations (e.g., "Cold War spy biography true story")
- True Crime: crime type + location/era combinations (e.g., "1970s serial killer investigation book")
- Emotion or outcome phrases readers search (e.g., "survival memoir true story hope")

---

## Key Rules — Do NOT Break

1. **No invented dialogue in nonfiction.** Every direct quotation in Biography, Memoir, and True Crime must be traceable to a documented source. Reconstructed dialogue is labeled as reconstruction. This rule has no exceptions and no workarounds.

2. **Reconstructed scenes require labels.** Any scene reconstructed from evidence rather than direct documentation must be explicitly labeled as a reconstruction at the point it appears. Unlabeled reconstruction is misrepresentation.

3. **Living persons require Legal & Privacy Counsel review on every chapter.** No chapter involving a living person advances past Gate 3 without the Legal & Privacy Counsel role completing its review. Allegation language must be used consistently for all unproven claims.

4. **All seven Dignity Battery checks must pass for True Crime content.** A single FAIL on any Battery check requires revision and re-check. The Battery is applied chapter-by-chapter at Gate 3 and full-manuscript at Gate 4. No True Crime manuscript advances to KDP without a full-manuscript Battery pass.

5. **Victims are human beings first, cases second.** In True Crime and any biography or memoir involving victimization, the victim is introduced as a full person before being described as a victim. The book never reduces a person to the means of their harm.

6. **Minors are never named without documented adult-waiver of anonymity.** Persons who were under 18 at the time of events covered — whether victims, suspects, or witnesses — are not identified by name. Minor victims of sexual offenses are never named regardless of adult status.

7. **OV-HIST quotation authentication rules are mandatory here.** Every direct quotation attributed to any named person — living or deceased — must be traceable to a primary source. Famous-but-unverified quotes are omitted or explicitly caveated. This applies with equal force to biography, memoir, and true crime.

8. **Chronology audit is mandatory before Gate 3 closes on any chapter.** Dates, ages, event sequences, and timeline consistency are verified for every chapter. Date errors in biography generate immediate negative reviews.

9. **Collective biography profile count must match title count exactly.** If the title states "50 women," there are exactly 50 profiles. This is non-negotiable. The count is verified at Gate 4.

10. **Collective biography profiles must include all four structural units.** Hook, Life, Contribution, and Legacy are mandatory for each profile. A profile with a missing unit is incomplete. Profiles must be within ±10% of each other in length without documented editorial rationale.

11. **No hagiography. No hatchet job.** Every biographical subject — however admired or reviled — is presented as a full human being in full complexity. Uncritical celebration and uncontextualized attack are both editorial failures.

12. **As-Told-To collaborators must be disclosed.** Failure to disclose a ghost-writer or collaborator on a memoir is a misrepresentation to readers. Disclosure appears on the cover, copyright page, and Acknowledgments.

13. **Source Ledger is a production document, not a reference.** The Source Ledger is completed for every chapter before Gate 3 closes. It is not written retrospectively at Gate 4. A claim that cannot be sourced when it is written cannot be retroactively sourced — it must be hedged or removed at the time of writing.

14. **Bibliography and notes are mandatory for biography and true crime.** A biography or true crime book without citation infrastructure is not credible nonfiction. Minimum bibliography of 20 sources for books under 250 pages; proportionally more for longer works. Notes/endnotes for all non-obvious factual claims.

15. **True Crime source integrity admits no prohibited sources.** Court records, named journalism, and official statements are the sourcing floor for true crime factual claims. Social media speculation, anonymous sources, and unverified online content are prohibited as primary sourcing regardless of how widespread they are.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
