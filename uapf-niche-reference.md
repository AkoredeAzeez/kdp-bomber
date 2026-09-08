---
name: uapf-niche-reference
description: Adult Reference & Trivia niche overlay (OV-REF) — invoked by uapf-phase0-router when routing signals match fact books, trivia books, almanacs, quiz books, list books, or quick-reference handbooks for adult readers.
---

# UAPF Niche: Adult Reference & Trivia (OV-REF)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Reference-Edition/` (config, validation, phases, and deterministic ops in `genie_reference.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Reference Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title or concept contains any of the following signals — "1000 facts", "trivia", "quiz book", "almanac", "facts about [topic]", "pub quiz", "list of greatest", "100 greatest", "word origins", "quick reference", "bar trivia", "ultimate trivia", "did you know" (adult framing), "encyclopedia of", "complete guide to", "record breakers", "history of [topic] in facts", "the ultimate [topic] quiz", "everything you need to know about", "[number] things you didn't know", "book of lists", "ranked and rated", "top [number]", "greatest [topic] of all time", or any nonfiction adult title whose primary unit of content is a discrete fact, question-answer pair, ranked entry, or reference lookup — NOT a narrative or argument.

**Governing standard:** UAPF Activity & Puzzle Book Framework, Version 1.0 (July 2026), specialization overlay OV-REF
**Verification spine:** Inherits OV-CFACT dual-source verification protocol at adult depth and scale
**Authority order:** Factual accuracy and dual-source verification > Locked book type and entry-unit architecture > User's explicit brief > UAPF stable rules + OV-REF content rules > Live KDP platform requirements > Reference-derived patterns > Operator assumptions

---

## Expert Panel

Activate all five roles simultaneously at Phase 0. Each role reviews output independently before content advances to the next gate.

| Role | Function in this book |
|---|---|
| **Domain Master — Subject Authority & Fact Verification Director** *(lead)* | Lead authority for the book's subject domain. Verifies every fact, claim, and answer against dual independent authoritative sources. Audits all superlatives, records, and rankings. Manages the verification log. Makes the final call on disputed claims, borderline answers, and cut decisions. |
| **Trivia and Quiz Mechanics Specialist** | Designs and audits question-answer pair architecture for trivia and quiz sub-types: question defensibility, single-answer rule, difficulty ladder, round architecture, scoring system, answer-separation discipline, and group-play usability. Also reviews list-entry criteria consistency and ranked-entry defensibility. |
| **Reference & Information Architecture Specialist** | Governs lookup-first organization for reference handbook sub-types. Audits entry length consistency, index completeness, cross-reference accuracy, table and chart structure, and navigation system. Ensures the book functions as a tool, not just a reading experience. |
| **Adult Nonfiction Copy Editor & Style Director** | Adult prose calibration — confident, direct, varied sentence rhythm. Flags padding, hedging, repetition, and tonal inconsistency. Audits the "WHY behind the fact" depth requirement. Ensures adult voice throughout: no dumbed-down language, no condescension, no jargon without explanation. |
| **KDP Metadata and Positioning Strategist** | Amazon category selection, description copy, keyword strategy, and competitive positioning. Confirms count claims in titles are commercially competitive and achievable. Reviews subtitle for clarity, discoverability, and compliance with KDP rules. |

---

## Phase 0 — Title Analysis

Execute all steps in order before any content generation begins. Output the Book Lock before Phase I proceeds.

### Step 1 — Sub-Type Classification

Classify the book into exactly one primary sub-type. The sub-type determines the entry-unit architecture, structural rules, and gate-specific audit requirements that govern the entire production. Record the sub-type in the Book Lock. A book may carry a secondary sub-type when a minor portion of its pages (under 25%) follows a different architecture — document this explicitly.

| Sub-Type Code | Sub-Type Name | Primary Signal | Entry Unit |
|---|---|---|---|
| REF-FACT | Adult Fact Book | "facts about", "1000 facts", "amazing facts", "did you know" (adult), "everything about", "almanac" | Anchor-fact + supporting cluster + WHY depth note |
| REF-TRIVIA | Trivia / Quiz Book | "trivia", "quiz book", "pub quiz", "bar trivia", "ultimate trivia", "quiz night" | Question-answer pair, organized into rounds |
| REF-LIST | List / Ranking Book | "100 greatest", "list of greatest", "top [N]", "ranked and rated", "book of lists", "greatest [topic] of all time" | Ranked entry with stated criteria and consistent entry depth |
| REF-REF | Quick Reference Handbook | "quick reference", "word origins", "at a glance", "pocket guide", "encyclopedia of" (lookup-first) | Lookup entry with index-first navigation |

**If the title contains both trivia and ranking signals** (e.g., "The Ultimate 100 Greatest Pub Quiz Book"), classify as the sub-type that dominates the page architecture. Mixed books carry a primary sub-type for gate purposes; secondary sub-type rules apply to those pages only.

### Step 2 — Title Integrity and Count-Claim Audit

1. Confirm the exact title as provided. Do not alter it without explicit user instruction.
2. Extract any explicit count claim from the title ("1000 Facts", "100 Greatest", "500 Questions"). Record it as **COUNT CLAIM: [N]** in the Book Lock.
3. If a count claim is present: calculate whether the claimed count is achievable within the target page range using the entry density specified for this sub-type (see Book Architecture). If it is not achievable, flag the conflict immediately — do not proceed until the user resolves it by adjusting the count claim or the page target.
4. If no count claim is present: record **COUNT CLAIM: NONE** and still track the total entry count at Gate 2.
5. Run a trademark and competitive uniqueness screen: does the title duplicate an active high-ranking title in the same Amazon category? Note conflicts and present to user before proceeding.

### Step 3 — Superlative and Record Inventory

Scan the title, subtitle, concept brief, and any supplied outline for superlative language ("greatest", "best", "most", "first", "last", "oldest", "youngest", "heaviest", "fastest", "longest", "richest", "deadliest", "largest", "smallest"). Record every superlative as a Superlative Claim requiring verification and dating at Gate 2.

| Superlative risk tier | Definition | Required treatment |
|---|---|---|
| **Volatile** | Records that change on a human timescale (sports records, wealth rankings, attendance records, population counts, technology achievements) | Verify against a dated source; add "(as of [year])" inline in the text |
| **Semi-stable** | Records that rarely change but could (geographic superlatives, species records, historical firsts confirmed by ongoing archaeology) | Verify against a current reference; add "(as of [year])" if plausible to change within 5 years |
| **Fixed** | Historical records that cannot change by definition (first person to walk on the moon, year a war ended, original publication date of a novel) | No date required, but dual-source citation must be on record |

### Step 4 — Audience and Depth Calibration

OV-REF targets adult readers. Confirm the adult audience is unambiguous. If the title or concept reveals a younger target audience, halt and re-route to OV-CFACT or OV-CHILD.

Adult depth calibration applies across all sub-types:

- **Fact books (REF-FACT):** Every anchor fact must be accompanied by the WHY — the mechanism, cause, historical context, or consequence that makes the fact intellectually satisfying rather than merely surprising. A children's fact book says "A blue whale's heart is the size of a small car." An adult fact book adds WHY: what cardiac output that requires, how it evolved, and what it reveals about the scaling laws of mammalian biology. The WHY note is not optional — it is the structural differentiator from children's content and from social-media trivia.
- **Trivia books (REF-TRIVIA):** Questions may assume adult general-knowledge literacy. Difficulty ladders within rounds span beginner-accessible to genuinely specialist. Scoring systems are designed for group play and pub-quiz hosting.
- **List books (REF-LIST):** Criteria for ranking must be stated explicitly and applied consistently. Adult readers will interrogate the ranking methodology — a list without stated criteria is an opinion dressed as reference. A list with stated criteria is a defensible editorial argument.
- **Reference handbooks (REF-REF):** Organized for lookup, not linear reading. Adult users expect index-first navigation, cross-references, and consistent entry structure across every page. Inconsistency in entry structure is the fatal flaw for this sub-type.

### Step 5 — Subject Domain and Verification Scope

Identify the subject domain. Flag all domains that carry elevated verification risk:

| Domain | Elevated verification risks |
|---|---|
| Sports | Records change frequently; disputed records common; governing-body rule variations affect records |
| Science and medicine | Consensus shifts; new discoveries supersede earlier records; preprint vs. peer-reviewed distinction matters |
| Politics and law | Jurisdiction-specific; contested interpretations; inflammatory framing risk |
| History | Disputed events, contested attributions, evolving historiography |
| Popular culture | Attribution errors are endemic (misquotes, misattributed firsts, disputed chart positions) |
| Economics and business | Numbers are vintage-dependent; comparisons require inflation adjustment |
| Geography | Borders and names change; disputed territories require neutral framing |
| Food and beverage | Origin claims are frequently contested; "first" claims require careful qualification |

Record the domain, the elevated risks identified, and the verification protocol adjustments for this book in the Book Lock.

### Step 6 — Auto-Configuration

Once sub-type and domain are locked, auto-configure the following without asking the user (state all assumptions):

- **Trim size:** 6 x 9 default for REF-FACT and REF-LIST. 5.5 x 8.5 acceptable for REF-TRIVIA and REF-REF where portability is a selling point. 8.5 x 11 for reference handbooks with tables, charts, or visual layouts.
- **Ink / paper:** Black and white interior standard for REF-TRIVIA, REF-LIST, and REF-REF. Black and white with section color dividers acceptable for REF-FACT at no cost increase if color sections are limited to covers and divider pages. Full color only if the brief explicitly requires it.
- **Bleed:** ON for REF-FACT books with illustrated or photographic spreads. OFF for text-dominant REF-TRIVIA and REF-LIST. Confirm with user if ambiguous.
- **Target page count:** 100-200 pages for REF-TRIVIA and REF-LIST. 150-300 pages for REF-FACT and REF-REF. All page counts must be even.
- **Dual-source verification protocol:** ACTIVE for all sub-types.
- **Volatile-fact date-stamp protocol:** ACTIVE for all sub-types.
- **Superlative audit:** ACTIVE for all sub-types.

### Step 7 — Subtitle Generation

Generate three subtitle candidates that:
1. Signal the sub-type and scope immediately ("Over 1,000 Verified Facts About...", "The Ultimate Pub Quiz Book with 500+ Questions", "Ranked and Rated: The 100 Greatest...")
2. State the audience or occasion ("Perfect for Trivia Night", "The Adult Fan's Complete Reference", "For Curious Minds")
3. Include at least one keyword phrase that matches likely Amazon search behavior for this category
4. Avoid hyperbole that cannot be substantiated ("The World's Most Complete...", "The Definitive..." unless genuinely defensible)

Present all three options with rationale. User selects or instructs revision.

### Step 8 — Mandatory Book Lock Output

Before any content generation, output the formatted Book Lock:

```
BOOK LOCK — OV-REF
Title:
Subtitle (chosen):
Sub-type (REF-FACT / REF-TRIVIA / REF-LIST / REF-REF):
Secondary sub-type (if applicable, and page %):
Target audience: Adult
Domain:
Elevated verification risks (from Step 5):
Count claim (from title):
Minimum entries to produce:
Trim size:
Ink / paper:
Bleed:
Target page count:
Entry density (entries per page):
WHY-depth requirement: ACTIVE (REF-FACT) / NOT APPLICABLE (other sub-types)
Round architecture (REF-TRIVIA only): [rounds × questions per round]
Scoring system (REF-TRIVIA only):
Ranking criteria (REF-LIST only):
Superlative inventory (list every superlative in title and concept):
Dual-source verification protocol: ACTIVE
Volatile-fact date-stamp protocol: ACTIVE
Disputed-answer protocol: ACTIVE
Duplicate-entry scan: PENDING (Gate 2)
Full-entry verification audit: PENDING (Gate 2)
KDP category targets:
```

---

## Book Architecture

### REF-FACT: Adult Fact Book Architecture

**The Structural Atom — Fact-Cluster Unit**

Every themed section in a REF-FACT book is built from Fact-Cluster Units. A unit occupies one page or one facing-page spread depending on trim and entry density.

```
[1] SECTION / THEME HEADER
    - Theme title (clear, factual, not clickbait)
    - Optional subhead framing the intellectual territory ("Why the Human Brain Is Still Science's Greatest Puzzle")

[2] ANCHOR FACT
    - The single most interesting, counterintuitive, or important fact in this cluster
    - Stated in one to three sentences of confident adult prose
    - Must include the WHY: the mechanism, cause, historical context, or consequence
      ("The Great Wall of China is NOT visible from space with the naked eye —
      its width (15-30 feet) is comparable to a human hair from the Moon's distance.
      The myth originated in a 1932 Ripley's Believe It or Not! claim made decades
      before any human reached orbit to disprove it.")
    - Dual-source verified; volatile superlatives dated inline

[3] SUPPORTING CLUSTER
    - 3-8 additional facts expanding on or contrasting with the anchor
    - Each fact includes its own WHY note (one sentence minimum for adult depth)
    - Arranged by intellectual pull (most counterintuitive or consequential first within the cluster)
    - Each item is a distinct fact — not a restatement, elaboration, or sub-clause of another
    - All dual-source verified; volatile claims dated

[4] DEPTH SIDEBAR (optional — use on 25-40% of clusters)
    - A longer contextual note (50-150 words) that goes deeper on one dimension
      of the anchor fact: the history behind it, the science, the controversy, or
      the human story
    - Visually distinct (boxed, indented, or shaded) but subordinate to the anchor
    - Not a replacement for the WHY note — an extension of it

[5] SOURCE REFERENCE
    - Inline or footnote-style, matching the book's citation style
    - Required for claims that a skeptical adult reader would immediately question
    - Not required on every line — required on all superlatives, statistical claims,
      and counterintuitive facts
```

**Section Architecture**

Organize in 5-12 thematic sections. Each section contains 4-15 Fact-Cluster Units. Sections ordered by thematic logic (not alphabetically unless the sub-genre convention demands it).

**Page-Count and Entry-Density Targets**

| Trim | Entries per page (approx.) | Target page count | Minimum entries for 200-claim title |
|---|---|---|---|
| 6 x 9 | 1.5-2 entries per page | 120-160 pages | At least 120 pages |
| 5.5 x 8.5 | 1.5 entries per page | 140-180 pages | At least 140 pages |
| 8.5 x 11 | 2-3 entries per page | 100-140 pages | At least 100 pages |

**Front Matter Requirements**

1. Title / half-title page
2. Copyright page (KDP standard placement)
3. Table of contents with section names and page numbers
4. Introduction (1-3 pages): frames the book's intellectual ambition, its verification standard, and the WHY-depth commitment. Adult readers buying a fact book want to know they are getting something more rigorous than a social-media listicle — the introduction is where this promise is made explicit.
5. How to Use This Book (optional but recommended for REF-FACT books over 200 pages)

**Back Matter Requirements**

1. Sources / Bibliography — all sources used in verification, formatted consistently (Chicago, APA, or a simplified but consistent format). Adult readers expect this. Its absence signals low-quality content.
2. Index — required for all REF-FACT books over 150 pages. Strongly recommended for all others.
3. Further Reading — 5-10 titles or resources per major section theme (optional but adds perceived value)
4. Acknowledgements (optional)

---

### REF-TRIVIA: Trivia / Quiz Book Architecture

**The Structural Atom — Question-Answer Pair**

Every question is a discrete, self-contained entry:

```
[Q] QUESTION
    - One clear, unambiguous question
    - Single-answer defensible: the question has exactly one answer that a
      knowledgeable reader cannot credibly dispute
    - Disputed questions are either resolved (with the dispute noted in the
      answer) or removed
    - No "trick" questions that rely on a technicality not present in
      the question text
    - Difficulty-coded if the round uses a difficulty ladder

[A] ANSWER
    - The correct answer, stated plainly
    - 1-3 sentences of bonus context: why this answer is correct, or one
      surprising elaboration that rewards the reader for getting it right
    - Page-flip separated from the question (see Answers-Separation Discipline)
    - For disputed or jurisdiction-dependent answers: note the primary answer
      and the qualifier ("In the US — in the UK, the answer is...")
```

**Round Architecture**

The round is the structural unit of a REF-TRIVIA book. Every trivia book must follow a round architecture — a collection of questions organized into themed groups of fixed length. Do NOT produce a trivia book as an undifferentiated list of questions.

```
[ROUND] THEMED ROUND
    - Round title that clearly signals the theme
    - Fixed question count per round (choose one and apply consistently):
      * Standard: 10 questions per round
      * Extended: 20 questions per round
      * Mini: 5 questions per round (for lightning rounds or specialist rounds)
    - Difficulty ladder within every round:
      * Questions 1-3: accessible (general knowledge, widely known)
      * Questions 4-7: moderate (requires genuine familiarity with the topic)
      * Questions 8-10: specialist (rewards deep knowledge; acceptable to get wrong)
    - Total rounds: 10-50 rounds per book depending on target page count
    - Theme variety: no two adjacent rounds share the same primary theme
```

**Answers-Separation Discipline**

The physical separation of questions and answers is not a formatting preference — it is the mechanism that makes a trivia book usable for group play. Violating it produces a book that cannot function as a quiz host tool.

Rules:
1. All answers are collected in a dedicated Answers section, separated by a minimum of 5 pages from the corresponding questions.
2. Answers section uses the identical round number and question number as the questions section for exact correspondence.
3. The question pages carry no answer-revealing information whatsoever — no footnotes, no inverted text at page bottom, no answer previews.
4. Answers may appear at the end of each chapter (chapter-level separation) or in a single consolidated back section (book-level separation). Both are acceptable. The user selects the separation model at Book Lock; it is then applied consistently throughout.
5. Answer pages include the round title and question number for easy reference.

**Scoring System**

Every REF-TRIVIA book must include a scoring system for group play:

```
SCORING SYSTEM (document in the book's introduction)
- 1 point per correct answer (base system)
- Difficulty bonus (optional): 2 points for specialist-tier questions (8-10)
- Round score: total points in that round
- Final score: sum of all round scores
- Score interpretation guide:
  * [score range]: "Trivia Novice — Keep Studying"
  * [score range]: "Solid Contender"
  * [score range]: "Pub Quiz Regular"
  * [score range]: "Trivia Expert — Are You a Professional?"
```

Include the scoring guide in the introduction and on a summary page before or after the answers section.

**Page-Count and Entry-Density Targets**

| Format | Questions per page | Target rounds | Target questions | Target page count |
|---|---|---|---|---|
| 5.5 x 8.5 | 8-10 Q per page | 25-50 rounds | 250-500 questions | 120-200 pages |
| 6 x 9 | 10-12 Q per page | 30-50 rounds | 300-600 questions | 100-160 pages |

**Front Matter Requirements**

1. Title / half-title page
2. Copyright page
3. Table of contents (list all round titles with page numbers)
4. Introduction: how to run a quiz night, the scoring system, group-play tips (2-4 pages)

**Back Matter Requirements**

1. Answers section (if not interspersed by chapter) — clearly indexed by round and question number
2. Score tally sheet (reproducible, or print-and-use format)
3. Blank round score card template (optional but commercially popular)

---

### REF-LIST: List / Ranking Book Architecture

**The Structural Atom — Ranked Entry**

Every ranked entry has three mandatory components:

```
[N] RANK NUMBER + ENTRY NAME
    - Clear, unambiguous identification of the ranked subject
    - Consistent naming convention across all entries (formal name, common name, or mixed — lock one convention and apply it throughout)

[CRITERIA SCORE / EVIDENCE]
    - 1-3 sentences stating WHY this entry holds this rank
    - Must reference the STATED CRITERIA (see below) — not a vague assertion ("It is simply the greatest")
    - For records and statistics: cite the specific figure and source
    - For qualitative rankings: cite the editorial criteria applied

[CONTEXT NOTE]
    - 2-4 sentences of broader context: historical significance, cultural impact, defining characteristic, or the runner-up that was narrowly displaced
    - Consistent length across all entries (see Entry Length Consistency rule)
```

**The Stated Criteria Requirement**

A REF-LIST book without stated ranking criteria is not a reference book — it is an opinion column. The criteria must be stated explicitly, and they must be applied consistently to every entry.

Before the ranked list begins, the book must contain a Ranking Methodology note that states:
1. What dimensions were used to rank entries (e.g., commercial impact + critical reception + cultural influence + longevity)
2. How those dimensions were weighted (equal weighting, or a stated hierarchy)
3. The source universe (e.g., "All films released theatrically between 1920 and 2024" — not "all films ever")
4. Any deliberate exclusions and why (e.g., "Documentary films are excluded; they are ranked separately")
5. The date as of which the rankings were determined

**Entry Length Consistency Rule**

All entries in a REF-LIST book must be within 20% of the same word count. An entry at rank 1 receiving 300 words while an entry at rank 87 receives 40 words signals incomplete research and creates a structurally weak book. If some entries have substantially more interesting material, the excess goes into a Depth Note sidebar — but the base entry length remains consistent.

**Page-Count and Entry-Density Targets**

| Entries | Words per entry | Approximate pages (6 x 9) |
|---|---|---|
| 50 entries | 150-250 words each | 80-120 pages |
| 100 entries | 100-180 words each | 100-160 pages |
| 200 entries | 60-100 words each | 100-140 pages |
| 500 entries | 25-50 words each | 100-150 pages |

**Front Matter Requirements**

1. Title / half-title page
2. Copyright page
3. Table of contents (optional for straightforward numbered lists; required for sectioned lists)
4. Introduction: the ranking methodology note (full criteria, source universe, exclusions, and date)
5. How to Disagree With Us (optional but commercially effective — invites reader engagement and preempts hostile reviews)

**Back Matter Requirements**

1. Honorable Mentions / The Next 50 (optional — commercially popular in list books)
2. Index (required for lists over 100 entries)
3. Sources / Bibliography
4. About the Ranking Panel (if rankings were determined by a panel rather than a single author)

---

### REF-REF: Quick Reference Handbook Architecture

**The Structural Atom — Lookup Entry**

Every lookup entry follows a fixed template established in the Book Lock and applied without variation:

```
[ENTRY HEADER]
    - Term, name, date, or subject (bold, consistent size and weight across all entries)
    - Pronunciation guide (for vocabulary and word-origin handbooks)
    - Classification tag (for encyclopedic handbooks that need filtering, e.g., [BIOLOGY], [HISTORY])

[CORE DEFINITION / DESCRIPTION]
    - 1-4 sentences, depending on entry scope
    - Consistent length across all entries (within 30% of target entry word count)
    - Written for lookup, not linear reading — the user is scanning for a specific answer

[USAGE EXAMPLE or CONTEXT NOTE]
    - One example, illustration, or historical context line
    - Required for all word-origin and vocabulary handbooks
    - Optional for encyclopedic reference handbooks

[CROSS-REFERENCE]
    - "See also: [related entry]" (when a cross-reference adds genuine value)
    - Do not cross-reference mechanically — only cross-reference when the related entry is genuinely illuminating
```

**Lookup-First Organization**

The defining rule of REF-REF is that organization serves the user who is LOOKING SOMETHING UP, not the user reading from page 1. This means:
- Alphabetical organization is the default unless the subject domain has a stronger organizational logic (chronological for timelines, taxonomic for field guides)
- Tab-indexed sections (simulated in print with dark-edged dividers) where the book exceeds 200 pages
- A comprehensive index is not optional — for REF-REF it is a core deliverable
- Cross-references within entries reduce lookup friction when two terms are closely related

**Page-Count and Entry-Density Targets**

| Entries | Words per entry | Approximate pages (6 x 9) |
|---|---|---|
| 200-500 entries | 40-80 words each | 100-200 pages |
| 500-1000 entries | 20-50 words each | 120-200 pages |
| 1000+ entries | 15-30 words each | 200-300 pages |

**Front Matter Requirements**

1. Title / half-title page
2. Copyright page
3. How to Use This Book (required — explains the organization system, entry template, cross-reference conventions, and index)
4. Table of contents (for sectioned handbooks; optional for purely alphabetical books)

**Back Matter Requirements**

1. Comprehensive index — required, no exceptions
2. Quick-reference tables or summary charts (optional but high value for many REF-REF sub-types)
3. Sources / Bibliography
4. Abbreviations and symbols key (if used)

---

## Interior Design

### Trim and Page Geometry

| Sub-Type | Default Trim | Bleed Page (KDP) | Notes |
|---|---|---|---|
| REF-FACT | 6 x 9 | 6.125 x 9.25 | Accept 5.5 x 8.5 if portability is the brief |
| REF-TRIVIA | 5.5 x 8.5 | 5.625 x 8.75 | Pub-quiz portability preferred; accept 6 x 9 |
| REF-LIST | 6 x 9 | 6.125 x 9.25 | Standard adult trade nonfiction format |
| REF-REF | 6 x 9 or 8.5 x 11 | See KDP table | 8.5 x 11 only if tables or charts require it |

All page counts must be even. KDP minimum 24 pages (all sub-types will far exceed this).

### Typography System

**Three font roles (required across all OV-REF sub-types):**

1. **Display face** — section headers, round titles (REF-TRIVIA), chapter openers. Bold, high contrast, adult appropriate. Not novelty or decorative — adult nonfiction readers expect seriousness.
2. **Body face** — anchor facts, question text, ranked-entry body, lookup-entry definitions. High legibility at 10-12 pt. Commercially licensed, embedded. Generous x-height for long-form reading.
3. **Utility face** — source references, sidebars, captions, index, cross-references. A quieter weight or size variant of the body face. Must be embedded.

**Type floors for adult readers:**

| Element | Minimum size |
|---|---|
| Body text | 10 pt |
| Question text (REF-TRIVIA) | 11 pt |
| Answer text (REF-TRIVIA) | 10 pt |
| Section / round headers | 14 pt |
| Sidebar / source reference | 9 pt |
| Index text | 9 pt |
| Running header / folio | 9 pt |

**Alignment:**
- Body and entry text: left-aligned throughout. Never full-justify in an adult reference book — ragged right is standard and reads faster for reference material.
- Section headers and round titles: left-aligned or centered (lock one style and apply consistently).
- Index: left-aligned, hanging indent for sub-entries.

### Layout Template

**REF-FACT spread (6 x 9):**
```
- Outside margins: 0.75 in
- Inside margins: 0.75 in (adjust to KDP gutter table for final page count)
- Top margin: 0.75 in (running header zone above)
- Bottom margin: 0.75 in (folio below)
- Sidebar column (when used): 1.5-2 in, right-aligned, separated by 0.125 in rule
- Source reference: 8-9 pt, set 0.25 in below cluster text, above folio
```

**REF-TRIVIA spread (5.5 x 8.5):**
```
- Outside margins: 0.625 in
- Inside margins: 0.75 in
- Top margin: 0.625 in
- Bottom margin: 0.625 in
- Questions: numbered list, 1.5 line spacing for fill-in-game-night use
- Answer section: distinct visual zone (gray rule top, "ANSWERS" header) or separate back section
```

**REF-LIST and REF-REF:** Follow the same margin geometry as REF-FACT at the appropriate trim. Entry headers must be consistently and visually distinct from entry body text across every page.

### Color Scheme

**Black and white is the standard mode for all OV-REF sub-types.** Full color is only appropriate when:
- The cover and back are full color and the interior is spot-color (single accent color for section dividers, entry headers, or round number chips)
- The user's brief explicitly specifies full-color interior

**If spot-color is used:**
- One accent color maximum across the full interior
- Applied consistently to section/round headers, entry number chips, and ruled dividers
- Must pass AA contrast against white paper at all sizes

---

## Content Rules

### The Fatal Flaw — OV-REF

**An OV-REF book is a verification machine in entertainment clothing.** The reader buys it for fun; they keep it, gift it, and review it well because nothing in it is wrong. When entertainment polish and factual certainty conflict, certainty wins — rewrite or cut.

**The fatal flaw in adult reference and trivia books is unverified, outdated, or defensively vague content presented as authoritative fact.** An adult reader who catches an error in a fact book will leave a one-star review. A pub-quiz host who uses a question with a disputed answer will be challenged publicly and blame the book. A reader who finds that your "100 Greatest" list has no stated ranking criteria will dismiss the entire book as personal opinion. Every fact, every answer, and every ranked entry must be verifiable, dated where volatile, and defended by stated criteria where qualitative.

### Dual-Source Verification Protocol (Adult Depth)

Every factual claim, question-answer pair, ranked entry, and lookup definition in an OV-REF manuscript must be verified against two independent, authoritative sources before manuscript lock.

**Authoritative source criteria (adult standard):**
- A peer-reviewed publication, academic press book, or institutional report
- A major reference database or established encyclopedia (Britannica, Merriam-Webster, Oxford DNB, Guinness World Records for records specifically)
- An official government, scientific, or sporting body dataset or rulebook
- A high-quality trade nonfiction book with a cited bibliography (not another uncited trivia book)
- An established national newspaper of record (for historical claims confirmed in reporting)

**Not acceptable as a sole source:** Wikipedia (acceptable as a secondary corroborating pointer to primary sources only), uncited trivia websites, social media posts, AI-generated content, other uncited trivia or fact books (circular sourcing), and personal blogs.

**Verification log (required — maintained throughout production, submitted at Gate 2):**

```
ENTRY [N]: [exact text of the fact, question, or entry as it will appear in the book]
SUB-TYPE FIELD: [anchor fact / supporting fact / question / answer / ranked entry / lookup definition]
SOURCE 1: [name, URL or publication, access date or publication year]
SOURCE 2: [name, URL or publication, access date or publication year]
SUPERLATIVE FLAG: [YES — volatile / YES — semi-stable / YES — fixed / NO]
DATE STAMP IN TEXT: [required if volatile / recommended if semi-stable / not required if fixed or NO]
DISPUTED FLAG: [YES — dispute noted in text / NO]
DUPLICATE CHECK: [CLEAR / CONFLICT WITH ENTRY N]
VERIFIED BY: [operator / domain expert / pending]
```

The verification log is a required deliverable at Gate 2. No manuscript may clear Gate 2 without a complete verification log covering every entry.

### WHY-Depth Requirement (REF-FACT Only)

Every anchor fact and every supporting cluster fact in a REF-FACT book must include the WHY note. The WHY note is the mechanism, cause, historical context, or consequence that elevates the fact from a trivia fragment to an intellectually satisfying insight.

**Test for WHY-depth compliance:** After reading the fact and its WHY note, can an adult reader explain not just WHAT the fact states, but WHY it is the case — in their own words, to another adult? If the answer is no, the WHY note is insufficient.

**Examples:**

Insufficient (fact only): "The Eiffel Tower grows taller in summer."

Compliant (fact + WHY): "The Eiffel Tower is approximately 15 cm taller in summer than in winter — because the iron expands when heated. The 7,300 tonnes of iron in the tower's structure follow standard thermal expansion: for every 1 degree Celsius of temperature rise, the metal expands by about 0.0000117 times its length. Paris summers can push the tower's temperature 40 degrees above its winter baseline, producing the measurable height difference."

### Single-Answer Defensibility Rule (REF-TRIVIA)

Every question in a REF-TRIVIA book must have exactly one answer that a knowledgeable, reasonable adult cannot credibly dispute. A question fails this test if:
- Two legitimate answers exist and the question does not specify which is sought
- The answer depends on a jurisdiction, time period, or governing body that is not specified in the question
- The answer has been superseded by a more recent event and the question does not indicate the time frame
- The answer is contested among experts without resolution

**Disputed questions: resolve or cut.** For questions where a genuine dispute exists that can be resolved (e.g., "Which country won the most gold medals at the 1936 Olympics?" — answer varies depending on whether you count United Germany as one or two entities), note the dispute and its resolution in the answer text. For questions where no resolution is possible, cut the question and replace it.

**Never use questions that rely on a technicality not visible in the question text.** A question that seems to have answer A but technically has answer B because of a rule or qualification not stated in the question is a trap, not a trivia question. Traps alienate readers and destroy pub-quiz trust.

### Stated Criteria Requirement (REF-LIST)

No ranked list may be published without a Ranking Methodology note that appears before the list begins (see Book Architecture above). The methodology note is not a disclaimer — it is a central content commitment. It must be written with the same care as the list itself.

**Criteria must be:**
- Specific (not "we considered everything important" — name the dimensions)
- Consistent (the same criteria applied to entry 1 must apply to entry 100)
- Honest about subjectivity (qualitative rankings carry editorial judgment — state this openly)
- Dated (rankings are as of a specific date; volatile rankings must note this)

### Volatile Fact Date-Stamping

All volatile superlative claims and statistics that are likely to change within 5 years must carry an inline date stamp: "(as of [year])" or "(current as of [year])". The date stamp appears in the body text, not only in the source reference.

**Volatile categories that always require date-stamping in OV-REF:**
- Population figures
- Sports records (individual and team)
- Wealth and economic rankings
- Attendance and viewership records
- Technology firsts and superlatives
- Box office records
- Any ranking derived from a dataset with an annual or frequent update cycle

### Duplicate-Entry Scan

Before Gate 2, run a full duplicate-entry scan across the entire manuscript:
- No fact may appear twice in different phrasings as two separate numbered entries
- No question may test the same specific knowledge as another question in the same book (a REF-TRIVIA book may have two questions about Shakespeare, but they must not share the same correct answer)
- No ranked entry may appear twice in a list under different names or aliases without explicit cross-referencing
- In REF-REF: no lookup term may have two separate entry blocks — consolidate duplicates into a single authoritative entry with cross-references

The duplicate scan result is recorded in the verification log and reported at Gate 2.

### Count Claim Exactness

A book titled "1000 Facts About History" must contain at least 1000 individually countable, verified facts. A book titled "500 Trivia Questions" must contain at least 500 individually verifiable question-answer pairs.

Rules:
- Count every entry before Gate 2; record the count in the verification log.
- Do not count the same fact twice (restated in a sidebar and in body text = 1 fact).
- Do not count section headers, introductory paragraphs, source references, or back-matter content as entries toward the count claim.
- If the count is short, add verified entries before Gate 2. Do not pad by splitting one fact into two near-identical sentences.
- If the count is short by more than 10%, flag to the user before proceeding.

---

## QA Checklist

### Gate 1 — Title Analysis and Book Lock

- [ ] Sub-type locked (REF-FACT / REF-TRIVIA / REF-LIST / REF-REF) with signal evidence stated
- [ ] Secondary sub-type identified if applicable (and page % documented)
- [ ] Exact title confirmed; count claim extracted and recorded
- [ ] Count claim achievability confirmed against entry density and page target
- [ ] Trademark and competitive uniqueness screen run; conflicts noted
- [ ] Superlative inventory complete (all superlatives in title and concept flagged by tier)
- [ ] Domain identified; elevated verification risks documented
- [ ] Adult audience confirmed; OV-CFACT or OV-CHILD re-route check clear
- [ ] WHY-depth requirement status: ACTIVE (REF-FACT) / NOT APPLICABLE (other sub-types)
- [ ] Round architecture documented (REF-TRIVIA): rounds × questions per round × difficulty ladder
- [ ] Scoring system documented (REF-TRIVIA): point values, interpretation guide
- [ ] Ranking methodology note drafted (REF-LIST): criteria, weighting, source universe, exclusions, date
- [ ] Lookup entry template documented (REF-REF): header fields, body length, cross-reference rules
- [ ] Answers-separation model selected (REF-TRIVIA): chapter-level or book-level back section
- [ ] Trim size locked; bleed status confirmed
- [ ] Ink / paper mode locked (B&W standard / spot color / full color with justification)
- [ ] Target page count set and even
- [ ] Entry density (entries per page) documented and consistent with count claim
- [ ] Dual-source verification protocol: ACTIVE
- [ ] Volatile-fact date-stamp protocol: ACTIVE
- [ ] Disputed-answer protocol: ACTIVE (REF-TRIVIA) / ACTIVE for disputed records (all sub-types)
- [ ] Duplicate-entry scan: PENDING Gate 2
- [ ] Three subtitles generated; user selection recorded
- [ ] KDP category targets identified
- [ ] Book Lock output complete
- **GATE 1 STATUS: PASS / FAIL / PENDING**

### Gate 2 — Manuscript and Verification

- [ ] All sections complete; section order follows stated organizational logic
- [ ] Total entry count verified against count claim; count meets or exceeds the title promise
- [ ] Every anchor fact includes a WHY note meeting the adult-depth standard (REF-FACT)
- [ ] Every question passes the single-answer defensibility rule (REF-TRIVIA)
- [ ] Every ranked entry references stated criteria explicitly (REF-LIST)
- [ ] Every lookup entry follows the locked template without deviation (REF-REF)
- [ ] Verification log complete: every entry has two independent authoritative sources recorded
- [ ] Superlative audit complete: every superlative verified; volatile superlatives dated inline in text
- [ ] Volatile-fact date stamps present on all entries in volatile categories
- [ ] Duplicate-entry scan complete: no fact, question, or entry appears twice; scan result recorded
- [ ] Disputed questions resolved with dispute noted in answer text, or removed (REF-TRIVIA)
- [ ] Round architecture confirmed: all rounds have the correct fixed question count (REF-TRIVIA)
- [ ] Difficulty ladder confirmed within every round (REF-TRIVIA)
- [ ] Answers-separation discipline confirmed: no answer-revealing information on question pages (REF-TRIVIA)
- [ ] Scoring system and interpretation guide present in introduction (REF-TRIVIA)
- [ ] Ranking methodology note present before the list; criteria applied consistently to every entry (REF-LIST)
- [ ] Entry length consistency confirmed: all entries within 20% of target word count (REF-LIST)
- [ ] Lookup entries confirm consistent template application across every page (REF-REF)
- [ ] Index drafted (required REF-REF all sizes; required REF-FACT and REF-LIST over 150 pages)
- [ ] Sources / bibliography present and formatted consistently
- [ ] Front matter complete: title page, copyright, table of contents, introduction (required for all sub-types)
- [ ] Back matter complete per sub-type requirements
- [ ] No padding: no entry that is a restatement, sub-clause, or near-duplicate of another entry
- [ ] Adult prose audit: confident voice, no dumbing-down, no condescension, varied sentence rhythm
- [ ] All volatile records confirmed against a source dated within the last 2 years; older sources flagged
- **GATE 2 STATUS: PASS / FAIL / PENDING**

### Gate 3 — Interior Design, Layout, and Typography

- [ ] Trim size and page geometry match Book Lock; all pages at correct bleed dimensions
- [ ] All fonts are commercially licensed and embedded; no missing or substituted glyphs
- [ ] Type floors met on every page: body 10 pt, questions 11 pt, headers 14 pt, sidebar/index 9 pt
- [ ] All body and entry text is left-aligned (not full-justified)
- [ ] Section headers and round titles consistently styled (either left-aligned or centered throughout — not mixed)
- [ ] Entry headers are visually distinct from entry body text on every page
- [ ] Running fact-number or entry-number device (if used) is consistent and correctly positioned across all pages
- [ ] Sidebar law: sidebars on no more than 40% of pages; all sidebars visually subordinate to main entry
- [ ] Answers section is visually distinct from questions section (REF-TRIVIA); no answer visible on question page
- [ ] Spot-color or full-color elements (if used): consistent; pass AA contrast check at all sizes
- [ ] No critical information conveyed by color alone (colorblind accessible)
- [ ] Margins and gutters consistent throughout; gutter width appropriate for page count per KDP table
- [ ] Folios (page numbers) and running headers: correct, consistent, present on all appropriate pages
- [ ] Index formatted correctly: alphabetical, hanging indent for sub-entries, page numbers accurate
- [ ] No placeholder text, no watermarks, no crop/registration marks in the body pages
- [ ] Thumbnail-view review: visual rhythm consistent; section breaks legible; no anomalous pages
- [ ] 100% render review: all text layers above image/background layers; no type obscured
- **GATE 3 STATUS: PASS / FAIL / PENDING**

### Gate 4 — Preflight and Pre-Release

- [ ] Page count is even and within KDP's supported range for the selected trim and ink mode
- [ ] Final entry count reconciliation: verified count in final PDF equals or exceeds count claim
- [ ] Superlative audit re-confirmed on final text: all volatile superlatives dated; no undated volatile claim
- [ ] Verification log confirmed as complete; available for internal record; no entry flagged UNVERIFIED
- [ ] Duplicate-entry scan result on file; zero duplicates confirmed in final manuscript
- [ ] Disputed-answer log on file (REF-TRIVIA): all disputes resolved or entries removed
- [ ] PDF export is fixed-layout at correct bleed dimensions on every page
- [ ] MediaBox and BleedBox cover the full bleed page; TrimBox identifies the trim correctly
- [ ] No crop marks, registration marks, printer slugs, or comments in export
- [ ] All fonts embedded; all glyphs render correctly (including any special characters in index or foreign words)
- [ ] All images (if any) at minimum 300 DPI at placed size
- [ ] No hidden layers, watermarks, or nonprinting objects in final PDF
- [ ] Text extraction confirms real editable type throughout; no rasterized text blocks
- [ ] KDP AI-disclosure requirement met if AI tools were used in content or image generation
- [ ] Physical proof ordered and reviewed: trim, paper weight, text legibility at actual print size, gutter usability, B&W contrast on all entries
- [ ] KDP category and metadata confirmed final: category tree, keywords, description, count claim in title matches actual count
- [ ] All gate statuses current with evidence; no gate claimed PASS without evidence on record
- **GATE 4 STATUS: PASS / FAIL / PENDING**

**A book is not production-ready until Gate 4 STATUS is PASS with physical proof evidence and verification log on record.**

---

## KDP Positioning

### Amazon Category Tree

Select two categories for each OV-REF title. Choose the most specific available node as the primary category.

**REF-FACT and REF-TRIVIA — primary options (select the most specific):**
- Books > Humor & Entertainment > Trivia
- Books > Humor & Entertainment > Puzzles & Games
- Books > Reference > Almanacs & Yearbooks
- Books > Reference > Encyclopedias & Subject Guides
- Books > Reference > Words, Language & Grammar
- Books > History > World
- Books > History > [Region-specific]
- Books > Science & Math > History of Science
- Books > Sports & Outdoors > [Sport] > History & Trivia
- Books > Arts & Photography > History & Criticism

**REF-LIST — primary options:**
- Books > Humor & Entertainment > Pop Culture
- Books > Arts & Photography > History & Criticism > Films
- Books > Sports & Outdoors > [Sport] > History & Trivia
- Books > Music > History & Criticism
- Books > Reference > Encyclopedias & Subject Guides

**REF-REF — primary options:**
- Books > Reference > Encyclopedias & Subject Guides
- Books > Reference > Words, Language & Grammar
- Books > Reference > Almanacs & Yearbooks
- Books > Reference > Atlases & Maps (for geographic handbooks)

**Secondary category:** Add a second category that covers the subject domain specifically (e.g., if a trivia book focuses on film, add a film-specific category as secondary to Trivia as primary).

### Description Strategy

Adult reference and trivia buyers are self-purchasers or gift-buyers. The description must address two buyers simultaneously: the person who wants it for themselves (curiosity, entertainment, self-improvement) and the person buying it as a gift (pub quiz night, book gift, birthday, novelty).

**Lead with (in this order):**

1. The count and scope promise — stated clearly and confidently ("Contains 500 expertly verified trivia questions across 50 themed rounds, covering history, science, pop culture, sports, and more")
2. The format and usability hook — how the book is actually used ("Perfect for pub quiz hosting, game nights, and family challenges — with a built-in scoring system and complete answer section")
3. The quality differentiator — what makes this fact book more rigorous than the competition ("Every fact is dual-source verified. Volatile records are dated. No unsubstantiated trivia-website claims.")
4. A sample question, fact, or ranked entry that demonstrates the book's quality and makes the buyer want to know the answer
5. Bulleted feature list: question count or fact count, round/section count, difficulty range, scoring system, answer format, page count, trim
6. The occasion and audience call-to-action ("The ideal gift for history buffs, quiz night regulars, or anyone who thinks they know everything")

**Never lead with** "This book is about..." or a list of categories. Adult buyers scan for trust and entertainment value, not a table of contents.

**Title field metadata:** Include the primary keyword naturally. Examples:
- "1000 Amazing History Facts: A Verified Adult Fact Book from Ancient Rome to the Modern World"
- "The Ultimate Pub Quiz Book: 500 Trivia Questions in 50 Themed Rounds with Answers"
- "The 100 Greatest Films of All Time: Ranked, Rated, and Explained"

### Metadata Signals

- **Keywords (7 fields):** Lead with format keywords ("trivia book for adults", "fact book", "pub quiz book", "quiz night book") + topic ("history trivia", "science facts", "pop culture quiz") + occasion ("gift for men", "game night book", "stocking stuffer") + count signal ("1000 facts", "500 questions") + secondary descriptors ("verified facts", "ultimate trivia", "adult quiz book")
- **Series field:** Complete if the book is part of a series; drives Also Bought placement and repeat-purchase behavior
- **Author name:** Adult reference books benefit from a credible pen name or institutional author credit where applicable. A trivia book attributed to "The Pub Quiz Experts" reads differently from a book attributed to "J. Smith." Choose the positioning that fits the brand.

---

## Key Rules — Do NOT Break

1. **Every entry — every fact, every question-answer pair, every ranked item, every lookup definition — is dual-source verified before Gate 2.** No exception for "obvious" facts. The most obvious facts are the ones most often wrong in published trivia books. "Obvious" is not a source.

2. **Volatile superlatives must be dated inline in the body text.** Not only in the source reference. Not only in a footnote. In the sentence itself: "(as of [year])". A sports record that was accurate when the book was written but has since been broken will produce a one-star review if there is no date qualifier.

3. **The count claim in the title is a contractual promise.** A "1000 Facts" book contains at least 1000 individually countable, verified facts. Count them before Gate 2. The count is confirmed against the final PDF at Gate 4. No count claim may be used in the title until the manuscript achieves that count.

4. **No padding.** Splitting one fact into two near-identical sentences to hit a count target is prohibited. A fact about the height of Mount Everest and a fact about the discovery of Mount Everest's height are two facts. A fact about Mount Everest's height and a slightly rephrased restatement of the same height figure are one fact counted twice — this is padding and it degrades the product.

5. **REF-FACT: the WHY note is not optional.** An adult fact book that states WHAT without explaining WHY is a social-media post, not a book. The WHY note is required on every anchor fact and every supporting cluster fact. If the WHY cannot be determined from authoritative sources, the fact is cut or demoted to a passing reference.

6. **REF-TRIVIA: every question passes the single-answer defensibility rule before it enters the manuscript.** Disputed questions are resolved with the dispute noted, or removed. Trick questions that rely on unlisted technicalities are not trivia — they are traps. Traps go in the trash, not the book.

7. **REF-TRIVIA: answers are physically separated from questions.** No answer-revealing information appears on the question page. Not in footnotes, not upside-down at the bottom, not in a margin gloss. The separation model chosen at Book Lock is applied consistently to every round in the book.

8. **REF-LIST: ranking criteria are stated before the list begins.** A list without stated criteria is an opinion column. The ranking methodology note is not a disclaimer — it is a primary content commitment. Every entry must reference the stated criteria; no entry may rely on vague authority ("It is simply the greatest").

9. **REF-LIST: entry length must be consistent.** All entries are within 20% of the same word count. Entries that received more research do not receive proportionally more words — use a Depth Note sidebar for the excess. The list reads as a unified product, not as a collection of some entries the author cared about and some they did not.

10. **REF-REF: organization serves the user who is looking something up.** The organization logic (alphabetical, chronological, taxonomic) is locked at Book Lock and applied without exception. An index is not optional for REF-REF — it is a core deliverable, as essential as the entries themselves.

11. **The duplicate-entry scan is required at Gate 2 and must clear before Gate 3.** No manuscript advances to layout with unresolved duplicate entries. In a 1000-fact book, duplicate detection is the difference between 1000 verified facts and 900 verified facts and 100 variations on 50 of them.

12. **Adult depth is not optional in REF-FACT.** Adult readers buying a fact book have already seen every "top-10 facts" social-media carousel. The book earns its price point because it goes deeper — the WHY, the context, the mechanism, the consequence. Books that fail the adult-depth standard compete on price alone and lose to free internet content.

13. **State Honesty rule.** Never claim a verification pass, a source check, a proof order, or a duplicate scan was completed unless it was. Every gate reports PASS, FAIL, PENDING, NOT RUN, or UNVERIFIED — with one line of supporting evidence. A gate claimed PASS on assumption rather than evidence is a failed gate.

14. **Correction propagation applies fully.** If a fact is corrected after Gate 2, the verification log must be updated, the WHY note must be re-evaluated, any question testing that fact in a companion REF-TRIVIA book must be re-checked, the source list must be reconciled, and the duplicate scan must be re-run for that entry. A fact correction reopens Gate 2 for the affected entries and all downstream gates.

15. **Never route adult trivia or reference content to children's categories.** If a competing title in the same subject is categorized under Children's Books, that is not a reason to dual-categorize an adult title there. OV-REF books are adult products. They belong in adult reference, humor, or subject-specific adult categories.

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
