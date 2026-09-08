---
name: uapf-niche-childrens-facts
description: CBF 2.0 production overlay for children's nonfiction fact books — invoked by uapf-phase0-router when routing signals match amazing facts, children's encyclopedias, fun facts, did you know, or nonfiction topic books for young readers ages 5-12.
---

# UAPF Niche: Children's Nonfiction Fact Books (OV-CFACT)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/CBF-2.0/` (config, validation, phases, and deterministic ops in `genie_childrens_facts.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=CBF 2.0` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title or concept contains "facts for kids", "amazing facts about [topic]", "children's encyclopedia", "fun facts", "did you know", "[topic] for young readers" (nonfiction context), "101 facts", "100 things", "everything about", "kids' guide to [topic]", or describes a nonfiction knowledge-acquisition book — not a narrative story — for an audience ages 5-12. The defining signal is that the primary unit of content is a *fact*, not a story beat.

**Governing standard:** The Children's Book Framework, CBF 2.0 (July 2026 KDP edition), specialization overlay OV-CFACT
**Parent overlay:** OV-CHILD — all OV-CHILD rules, laws, and gatekeeper requirements are inherited in full. Where OV-CFACT adds or tightens a rule, the tighter rule governs.
**Authority order:** Child safety and law > Factual accuracy and dual-source verification > Locked age band and reading mode > User's explicit brief > CBF 2.0 stable rules + OV-CFACT content rules > Live platform requirements > Reference-derived patterns > Operator assumptions

---

## Expert Panel

| Role | Function in this book |
|---|---|
| **Children's Nonfiction Editor / Fact Accuracy Director** *(Domain Master)* | Fact verification against dual sources, superlative auditing, dated-record management, count-claim enforcement, curiosity-logic sequencing, age-banded vocabulary calibration, on-page gloss placement, Wow Callout review |
| **Subject-Matter Expert (Topic-Specific)** | Domain authority for the book's topic (e.g., zoologist for animals, astronomer for space, geologist for earth science); confirms that every anchor fact and supporting cluster reflects current scientific or scholarly consensus; flags outdated data |
| **Children's Nonfiction Art Director** | Fact-spread layout design, diagram and infographic integration, photo or illustration treatment per spread, sidebar and callout-box visual hierarchy, label and caption typography, themed spread cohesion |
| **Children's Readability and Vocabulary Specialist** | Age-band vocabulary audit, stretch-word identification, on-page gloss writing, sentence-length compliance, Quick Quiz answer accuracy and difficulty calibration, read-aloud test for AB-1 and AB-2-L1 fact books |
| **Child Safety, Accuracy, and Diversity Reviewer** | Child-appropriateness battery, sensitive-topic handling (e.g., animal death, human body, war history), diversity and representation in examples and illustrations, KDP content-policy compliance, AI-disclosure check, gatekeeper (parent/teacher/librarian) description review |

---

## Phase 0 — Title Analysis

### Step 1 — Age-Band and Complexity Signal Extraction

Parse the title, subtitle, concept brief, and any stated audience. Lock the age band before any production decision is made. For fact books, also lock the *knowledge depth level* (KD-1 through KD-3), which governs fact complexity, vocabulary, and on-page gloss density.

| Signal found | Locked band | Reading mode | Knowledge depth |
|---|---|---|---|
| Ages 4-6, "my first facts", simple one-fact-per-page, high-illustration | **AB-1** (3-5) | Adult performs; child listens | KD-1: one concrete fact per spread, no abstractions |
| Ages 5-8, "fun facts", "beginning nonfiction", level 1-2 reader | **AB-2-L1/L2** (6-8) | Child decodes with support | KD-1: short fact clusters, concrete examples only |
| Ages 6-9, "did you know", "amazing facts", "101 facts" | **AB-2-L2/L3** (7-9) | Child decodes with support | KD-2: 4-6 facts per spread, one concept requiring analogy |
| Ages 8-12, "children's encyclopedia", "everything about", "ultimate guide" | **AB-3** (9-12) | Independent silent reading | KD-3: 6-8 facts per spread, cause-effect, comparison, statistics |
| "for young readers" (nonfiction, topic-driven) | Age stated or default AB-2 | Match stated age | Match KD level to band |

### Step 2 — Profile Routing

OV-CFACT always routes to host profile **CB-FACT** within the OV-CHILD system. Confirm:

1. The primary unit of content is a *fact*, not a story event. If a narrative character or story arc carries the learning, route to CB-CONCEPT or CB-PIC instead.
2. A CB-FACT book may include a light narrative frame (e.g., a child explorer character) as a guest device occupying no more than one-sixth of pages. The frame never displaces fact content.
3. Lock trim: **8.5 x 11** is strongly preferred for CB-FACT — it is the format readers expect and the one that accommodates fact-spread layouts, diagrams, sidebars, and callout boxes without crowding. Accept 8.5 x 8.5 for square-format fact books with illustrative (not photographic) content only.

### Step 3 — Fact-Count Claim Audit (Title-Level)

Many children's fact books carry an explicit count claim in the title ("100 Amazing Facts", "101 Things", "500 Facts About Animals"). This claim is a contractual promise to the buyer.

- Extract the count claim from the title.
- Record it in the Book Lock as **FACT COUNT CLAIM: [N]**.
- The final manuscript must contain **at least [N] individually numbered, verified facts**.
- Do not count the same fact twice (e.g., restated in a callout box and in body text) unless each version adds distinct information.
- If no count claim exists, set **FACT COUNT CLAIM: NONE** — but still count and log total facts produced.

### Step 4 — Subject Domain and Superlative Inventory

Identify the topic domain. Flag all titles, subtitles, and concept notes containing superlative language ("biggest", "smallest", "fastest", "deepest", "most", "first", "oldest", "heaviest"). Record each superlative as a **Superlative Claim** requiring verification and dating at Gate 2.

| Superlative risk level | Examples | Required action |
|---|---|---|
| **Volatile** — records change frequently | Fastest animal alive, tallest building, most expensive thing | Verify against a dated source; add "(as of [year])" inline in the text |
| **Semi-stable** — changes rarely | Largest ocean, highest mountain, deepest lake | Verify against a current reference; add date if plausible to change within 5 years |
| **Fixed** — cannot change | First dinosaur discovered, oldest known star | No date required, but source must be cited |

### Step 5 — Topic Sequencing Plan (Curiosity Logic)

Children's fact books must be sequenced by *curiosity logic*, not academic taxonomy. Academic taxonomy orders content by classification (e.g., mammals before reptiles before birds). Curiosity logic orders content so each section answers the question a child naturally asks next.

Draft a section sequence plan following this scaffold before manuscript begins:

1. **Familiar anchor** — Start with a subject the child already knows or can picture (e.g., "You already know that sharks have lots of teeth...").
2. **Surprising escalation** — Reveal something that overturns the child's assumption about the familiar subject ("But did you know a shark can have up to 3,000 teeth at once?").
3. **Exotic extension** — Move outward to related subjects the child has heard of but doesn't know well.
4. **Wild frontier** — End sections (or the book) with the most exotic, record-breaking, or mind-bending facts.

Document the section sequence in the Book Lock as the **Curiosity Map** before writing begins.

### Step 6 — Auto-Configuration

Once band, profile, and knowledge depth are locked, auto-configure without asking (state assumptions):

- **Trim size:** 8.5 x 11 (default CB-FACT). Accept 8.5 x 8.5 only with justification.
- **Bleed page size (KDP formula):** 8.625 x 11.25 for bleed; state if non-bleed.
- **Type floor:** AB-1: 18-24 pt; AB-2-L1/L2: 14-18 pt; AB-2-L3: 13-15 pt; AB-3: 11-14 pt. Fact callouts and Wow Callout boxes: minimum 16 pt regardless of band (these must be easily scannable by a browsing child).
- **Word budget per spread:** KD-1: 30-80 words per spread; KD-2: 80-180 words per spread; KD-3: 150-300 words per spread. Wow Callout adds up to 30 words. Quick Quiz adds up to 40 words.
- **Fact density per spread:** KD-1: 1-2 facts; KD-2: 4-6 facts; KD-3: 6-8 facts. Never exceed 8 facts per themed spread regardless of band — excess facts belong in a new spread.
- **Color mode:** Full color premium. Fact books are a visual product; monochrome is not acceptable for this niche.
- **Bleed:** Set bleed flag ON. CB-FACT pages typically use illustrated or photographic backgrounds that extend to trim.
- **Gloss density:** KD-1: 0-1 stretch word per spread; KD-2: 1-3 stretch words per spread; KD-3: 2-4 stretch words per spread. Every stretch word receives an on-page gloss.
- **Read-aloud test flag:** ON for AB-1 and AB-2-L1. OFF from AB-2-L2 upward.

### Step 7 — Subtitle Generation

Generate 3 subtitle candidates that:
- State the age promise plainly (gatekeepers need this immediately)
- Hint at the volume or scope of content ("Over 100 Incredible Facts", "A Kid's Guide to [Topic]")
- Signal the nonfiction register — avoid fictional or story-like language in the subtitle
- Include a benefit or emotional hook ("Amaze Your Friends", "Learn, Explore, Discover")

### Step 8 — Mandatory Book Lock Output

Before any manuscript or art production, output a formatted Book Lock:

```
BOOK LOCK — OV-CFACT / CB-FACT
Title:
Subtitle (chosen):
Age band:
Knowledge depth level (KD-1 / KD-2 / KD-3):
Reading mode:
Trim size:
Ink / paper: Full color premium
Bleed:
Target page count:
Fact count claim (from title):
Minimum verified facts to produce:
Facts per spread (target range):
Word budget per spread:
Type floor (body):
Type floor (callouts / Wow box):
Gloss density per spread:
Alignment: Left-aligned (body); centered permissible for callout labels only
Color mode: Full color
Topic domain:
Curiosity Map (section sequence, 4-8 sections):
Superlative inventory (list every superlative claim from title/concept):
Gatekeeper (buyer) persona:
Child-safety battery: PENDING
Read-aloud cadence test: PENDING / NOT APPLICABLE
Dual-source verification protocol: ACTIVE
```

---

## Book Architecture

### The Fact-Spread Unit (Structural Atom of OV-CFACT)

Every themed spread in a CB-FACT book is built from the same structural unit. This unit may occupy one page or two facing pages depending on trim and fact density. The unit components in order:

```
[1] SPREAD HEADER
    - Theme title ("The Fastest Animals on Earth")
    - Optional subhead or teaser question ("Can anything outrun a cheetah?")
    - Section/chapter marker (if applicable)

[2] ANCHOR FACT
    - The single most important or most surprising fact on this theme
    - Visually dominant: larger type, set apart, or accompanied by the spread's primary illustration
    - Stated in one concise sentence at band-appropriate vocabulary
    - Source-verified; superlative claims dated inline if volatile

[3] SUPPORTING CLUSTER
    - 3-7 additional facts related to the anchor fact
    - Arranged by curiosity pull (most surprising or record-breaking first within the cluster)
    - Each fact is one sentence; maximum two sentences for KD-3 only
    - Each stretch word receives an on-page gloss immediately adjacent (not in a remote glossary)
    - Numbered if the book uses a running fact count; unnumbered otherwise

[4] WOW CALLOUT
    - One standout micro-fact, statistic, or comparison that makes a child gasp or laugh
    - Visually distinct: isolated in a box, starburst, or speech-bubble graphic element
    - Maximum 30 words
    - May be the same class of fact as the anchor but presented in a more dramatic register
    - ("A blue whale's heart is so big a child could crawl through its arteries!")

[5] QUICK QUIZ (optional — use on 30-50% of spreads, not every spread)
    - 1-3 questions testing recall of facts from THIS spread only
    - Answers placed immediately adjacent (upside-down text, small flip box, or footnote within the same spread — never "see page X" for a fact-level quiz)
    - Questions are multiple-choice (AB-2) or open-recall (AB-3)
    - Difficulty is calibrated: at least one question is answerable by a child who read the spread once
```

### Section Architecture

Organize the book in 4-8 thematic sections. Each section contains 4-10 themed spreads. Section architecture:

```
[A] SECTION OPENER PAGE
    - Large header naming the section theme
    - One evocative image (full-page or dominant half-page)
    - A teaser sentence or question that frames the curiosity hook
    - Section page range or spread count (optional but helpful for older readers)

[B] FACT SPREADS (4-10 per section)
    - Each spread follows the Fact-Spread Unit above
    - Spreads ordered by curiosity logic within the section
    - Record-breaking or most-exotic spread is last in the section, not first

[C] SECTION BRIDGE (optional, KD-3 only)
    - 1-2 sentences connecting this section's theme to the next section
    - Planted as the final sentence of the last spread in the section
    - Functions as a page-turn motivator
```

### Page-Count Targets

| Knowledge depth | Age band | Typical page count | Minimum facts |
|---|---|---|---|
| KD-1 | AB-1 | 24-32 pages | 10-20 facts |
| KD-2 | AB-2 | 48-80 pages | 50-100 facts |
| KD-3 | AB-3 | 80-128 pages | 100-200 facts |

- Page count must be even (KDP requirement).
- If the book carries a count claim (e.g., "100 Facts"), the page count must accommodate that count without padding — plan the architecture before writing.
- KDP minimum: 24 pages.
- Standard color activates at 72 pages; books under 72 pages use premium color — budget accordingly.

### Front Matter Requirements

1. **Title / ownership page** — dominant title, topic illustration (relevant subject, not a generic child character), age-range badge, one motif family.
2. **Copyright page** — standard KDP placement.
3. **Contents page** — required for all CB-FACT titles. List sections and page numbers. For count-claim titles, a "How to Use This Book" note is strongly recommended.
4. **Introduction / Welcome spread** — 1-2 pages. Frames the curiosity hook for the whole book. Addresses the child directly. Introduces any navigation system (fact numbers, section colors, quiz markers).
5. **Author / source note** — required in back matter (see below).

### Back Matter Requirements

1. **Glossary** — all stretch words defined in plain language. Cross-referenced to spread if useful.
2. **Source list** (age-appropriate format) — minimum 2 sources per major fact claim. Format for child audience: no dense academic citation, but list the source name, organization, or URL with access year.
3. **Index** — required for KD-3 (AB-3) titles. Recommended for KD-2 titles over 64 pages.
4. **Further Reading / Explore More** — 3-5 child-appropriate websites, documentaries, or books for each main section theme.
5. **Did You Know? Fast-Facts Summary** (optional) — a single-page summary of the most remarkable facts from the book. Functions as a "share with friends" page and increases perceived value.

### Interior Layout Laws for CB-FACT

- **No orphan facts.** A fact that appears alone on a page with no thematic context is prohibited. Every fact lives inside a themed spread unit.
- **Sidebar law.** Sidebars (narrow vertical or horizontal boxes containing supplementary information) may appear on no more than 40% of spreads. They must be visually subordinate to the anchor fact and supporting cluster — never more prominent than the main spread content.
- **Diagram and infographic law.** Diagrams (labeled anatomical drawings, scale comparisons, maps, timelines) may replace the anchor-fact illustration on a spread. When a diagram is used, every label must be real typeset text — never generated lettering. The diagram must have a title and a scale indicator where relevant.
- **Photo vs. illustration consistency.** Lock one treatment at Book Lock: illustrated throughout, or photographic throughout, or a documented mixed treatment (e.g., illustrated characters + photographic backgrounds). Do not alternate randomly.
- **Navigation system.** If the book uses running fact numbers, the counter must be visible and consistent on every fact-bearing spread. Use a small badge, icon, or number field in a fixed position per template.

---

## Interior Design

### Trim and Page Geometry

| Format | Trim | Bleed page size (KDP) | Notes |
|---|---|---|---|
| CB-FACT standard | 8.5 x 11 | 8.625 x 11.25 | Default for all OV-CFACT titles |
| CB-FACT square | 8.5 x 8.5 | 8.625 x 8.75 | Illustrated content only; confirm with user |

### Typography System

**Three font roles (required — same as OV-CHILD with OV-CFACT additions):**

1. **Display face** — section headers, spread headers, Wow Callout labels, fact-number badges. Energetic, bold, child-readable. One family per book.
2. **Body / learning face** — anchor fact, supporting cluster body text, Quick Quiz text. Open letterforms, generous x-height. Must be commercially licensed and embedded.
3. **Utility / gloss face** — on-page glosses, source notes, index, contents entries, captions, labels in diagrams. A quieter weight or the body face at reduced size. Must be embedded.

**OV-CFACT type floors:**

| Age band / KD | Body floor | Callout / Wow floor | Gloss floor | Caption floor |
|---|---|---|---|---|
| AB-1 / KD-1 | 18-24 pt | 20 pt | 14 pt | 12 pt |
| AB-2-L1/L2 / KD-1-2 | 14-16 pt | 16 pt | 12 pt | 11 pt |
| AB-2-L3 / KD-2 | 13-15 pt | 15 pt | 11 pt | 10 pt |
| AB-3 / KD-3 | 11-14 pt | 14 pt | 10 pt | 9 pt |

- Wow Callout and Quick Quiz text must NEVER fall below their callout floor — these are the elements a browsing child reads first.
- Gloss text is the minimum permitted size; do not reduce further even if a gloss is long — edit the gloss instead.

**Alignment:**
- Body and cluster: left-aligned always.
- Spread headers and Wow Callout: centered is acceptable.
- Captions: left-aligned, flush with their associated image.
- Index, glossary: left-aligned.
- Never full-justify body copy at AB-1 or AB-2. Full justification at AB-3 requires explicit user approval.

### Fact-Spread Layout Template

```
PAGE GEOMETRY (8.5 x 11 bleed trim, double-page spread shown as single page template):

LAYER 1: Bleed background (color field, illustrative scene, or photographic image — extends to media edge)
LAYER 2: Quiet zone / opaque panel (reserved for body text zones BEFORE art generation)
          - Anchor fact zone: upper or center-dominant region, minimum 25% of page
          - Cluster zone: secondary region, may be multi-column at KD-3
          - Padding: 0.25 in around all body text; 0.20 in around captions
LAYER 3: Spread header (real typeset text — display face)
LAYER 4: Anchor fact text (real typeset — body/learning face, larger weight)
LAYER 5: Supporting cluster text (real typeset — body/learning face, standard weight)
          - Running fact-number badge (if count-claim book)
LAYER 6: On-page glosses (real typeset — utility/gloss face, visually linked to stretch word by line or color)
LAYER 7: Wow Callout box (isolated graphic element; real typeset inside; never use generated lettering)
LAYER 8: Quick Quiz box (if used on this spread; real typeset; answer text inverted or hidden)
LAYER 9: Sidebar (if used; must be visually subordinate; real typeset)
LAYER 10: Diagram / infographic labels (real typeset only; no AI lettering)
LAYER 11: Caption text (real typeset — utility face)
LAYER 12: Section color band / navigation element (folio, section marker — inside trim)
```

**Text-zone reservation law:** Every illustration or photograph brief must state the exact reserved zone in proportional language BEFORE the image is generated or commissioned. If art violates the reserved zone, regenerate or add an opaque panel. Never shrink type or reduce padding to accommodate art.

### Color System

**Full color is the only permitted mode for OV-CFACT.** Monochrome and selective-color are prohibited — fact books compete on visual richness and cognitive engagement.

**Section color coding:** Assign one accent color per thematic section. Use this color on section openers, fact-number badges, Wow Callout boxes, and section navigation elements throughout that section. The accent color must:
- Pass AA contrast against white and the book's paper color
- Be distinctly different from every other section's accent (use hue, not just shade)
- Remain consistent within its section; never bleed into adjacent sections

**Palette lock (record at Book Lock):**
- Background / paper color
- Primary body text ink color (typically near-black, not pure #000000 for print softness)
- Section accent colors (one per section, 4-8 total)
- Wow Callout box color (may be a warm neutral or the section accent at reduced saturation)
- Diagram fill colors (limited palette; ensure accessibility)
- Illustration / character palette (if illustrated)

**Accessibility check:** Run a colorblind simulation on all diagrams and section color bands before Gate 3. Critical information conveyed by color alone must be reinforced by label, pattern, or shape difference.

---

## Content Rules

### The Fatal Flaw to Avoid

**Unverified or outdated facts.** Children's nonfiction fact books are where sloppy facts hide and propagate. A child who memorizes an incorrect "amazing fact" from your book and shares it at school has been harmed. A parent who discovers an error will review-bomb the title. Every factual claim — especially superlatives, statistics, and count claims — must be dual-source verified before the manuscript is considered complete. This is the single most important content rule in OV-CFACT. No other production quality compensates for factual errors.

### Dual-Source Verification Protocol

Every fact that appears in a CB-FACT manuscript must be verified against **two independent, authoritative sources** before manuscript lock. A source is authoritative if it meets one of these criteria:
- A peer-reviewed publication or institution (university, national museum, national laboratory)
- A major reference database or encyclopedia (Britannica, National Geographic, Smithsonian, BBC Earth)
- An official government or scientific agency dataset (NASA, USGS, WWF, WHO, NOAA)
- A recently published nonfiction book for adults or older children with a cited bibliography

**Not acceptable as a sole source:** Wikipedia (acceptable as a secondary corroborating source only), unsourced blog posts, AI-generated content, social media posts, and children's books from other publishers (circular sourcing).

**Verification log:** For every fact, record:
```
FACT [N]: [exact text of the fact as it will appear in the book]
SOURCE 1: [name, URL or publication, access date or publication year]
SOURCE 2: [name, URL or publication, access date or publication year]
SUPERLATIVE FLAG: [YES — volatile / YES — semi-stable / YES — fixed / NO]
DATE STAMP IN TEXT: [required if volatile / recommended if semi-stable / not required if fixed]
VERIFIED BY: [operator / domain expert / pending]
```
The verification log is a required deliverable at Gate 2. No manuscript may clear Gate 2 without a complete verification log.

### Superlative Audit

All superlative claims ("the biggest", "the smallest", "the fastest", "the most", "the first", "the last known", "the only") require individual audit entries:

1. **Verify the claim** against a source dated within the last 3 years for volatile records.
2. **Add a date stamp** inline in the text for volatile and semi-stable superlatives: "the fastest land animal (as of 2025)", "the tallest building in the world (as of 2026)".
3. **Flag for next edition** — volatile superlatives that are likely to change within 2 years should be noted in an internal revision flag, not surfaced in the book but recorded in production notes.
4. If a superlative claim cannot be verified in two sources within the last 5 years, the superlative must be softened to a qualified statement ("one of the fastest", "among the largest known") or removed.

### Number Lock

All quantities, statistics, dimensions, and counts appearing in the manuscript are subject to Number Lock at Gate 2:

- Every number is verified in the verification log.
- Approximate quantities use explicit hedging in the text: "about", "roughly", "scientists estimate", "more than".
- Exact numbers never appear without a source confirming precision.
- Fact count claims in the title are reconciled against the actual numbered count in the manuscript — the manuscript count must equal or exceed the title claim.
- Unit consistency: do not mix metric and imperial within a single fact. Choose the system appropriate for the target audience locale; provide conversion for the other system in parentheses or a gloss.

### Age-Banded Vocabulary

**Vocabulary tiers:**

| Age band / KD | Vocabulary standard | Stretch-word limit per spread | On-page gloss required |
|---|---|---|---|
| AB-1 / KD-1 | Sight words + simple nonfiction nouns | 0-1 per spread | Yes, always, immediately adjacent |
| AB-2-L1/L2 / KD-1-2 | Common words + introduced topic terms | 1-2 per spread | Yes, immediately adjacent |
| AB-2-L3 / KD-2 | Grade 2-4 vocabulary + topic vocabulary | 2-3 per spread | Yes, immediately adjacent |
| AB-3 / KD-3 | Grade 4-6 vocabulary + technical terms | 2-4 per spread | Yes for technical terms; optional for grade-level stretch |

**On-page gloss placement rules:**
- Gloss appears on the SAME spread as the stretch word — never "see glossary on page X" as a substitute for in-context definition.
- Gloss is visually linked to the stretch word: inline parenthetical, a subscript gloss line below the sentence, or a margin gloss with a connecting element.
- Gloss text must be shorter than the sentence containing the stretch word.
- The glossary in back matter is ADDITIONAL to on-page glosses — it is a reference tool, not a replacement.

**Concrete example law:** Every abstract concept introduced in a fact book must be followed immediately by a concrete analogy or example that a child in the target band can visualize. Abstract → Concrete is the required sequence. Do not introduce an abstract concept and then move to the next fact without anchoring it.

Example (KD-2): "A blue whale's heart weighs as much as a small car. That's about the weight of a Honda Civic — sitting inside a living creature!"

### Curiosity-Logic Sequencing Rules

- **Never open a section with the rarest or most technical fact** — open with the fact a child has already half-heard but gets wrong, then surprise them with the correction.
- **The Wow Callout is not the first thing written** — it is selected from the supporting cluster after the cluster is complete. It is the fact that caused the writer to gasp. If no fact in the cluster caused a gasp, the cluster needs better facts.
- **Quick Quiz questions must not test trivia a child cannot recall after one reading.** Questions that require memorizing exact numbers from the text (e.g., "What is the exact wingspan of the albatross in centimeters?") are inappropriate unless the number is the entire point of the spread and is prominently featured. Prefer process questions ("Why does a shark keep growing new teeth?") and big-picture recall ("What is the fastest land animal?").
- **The final spread of the book should deliver the most astonishing fact in the entire manuscript.** Save the absolute best for last — this is what a child will run to tell their parent.

### Child-Appropriateness Battery — OV-CFACT Extensions

In addition to all OV-CHILD child-appropriateness requirements, run these OV-CFACT-specific checks:

1. **Death and predation.** Animal predation and death are facts of nature and appropriate for this genre. Handle with factual neutrality (not graphic), age-calibrated language, and no gratuitous detail. For AB-1 titles, avoid graphic predation entirely. For AB-2+, factual descriptions without visceral detail are acceptable.
2. **Human body topics.** For fact books about the human body, digestion, reproduction topics (if included), or disease: calibrate clinical language to age band. AB-1: focus on naming parts and basic functions. AB-2: bodily processes are fine; reproduction topics require careful language. AB-3: accurate biological terminology with clear, non-sexualized framing.
3. **Historical atrocity and conflict.** Fact books about history, wars, or disasters must acknowledge human suffering without exploitative detail. Age-appropriate framing requires that the facts of harm be acknowledged (honesty) without dwelling on graphic suffering (protection).
4. **Environmental anxiety.** For fact books about climate, endangered species, or environmental change: present facts honestly, but end each relevant section with an action, a hopeful development, or an example of recovery. Children's fact books that end in unresolved dread are inappropriate for the genre.
5. **Scary or disturbing animals/phenomena.** "Did you know?" fear-based content (e.g., venomous spiders, parasites, extreme weather) is appropriate for this genre but must be calibrated: AB-1: avoidance of content likely to cause sleep disturbance. AB-2: scary facts with contextualizing safety information ("You are very unlikely to encounter..."). AB-3: full factual treatment.

---

## QA Checklist

### Gate 1 — Title Analysis and Book Lock

- [ ] Age band locked (AB-1 / AB-2-L1 / AB-2-L2 / AB-2-L3 / AB-3) with signal evidence stated
- [ ] Knowledge depth level locked (KD-1 / KD-2 / KD-3)
- [ ] Reading mode confirmed (adult performs / child decodes with support / independent)
- [ ] Host profile confirmed as CB-FACT
- [ ] Trim size locked: 8.5 x 11 (default) or 8.5 x 8.5 with justification
- [ ] Ink / paper confirmed: full color premium
- [ ] Target page count set and even; KDP minimum 24 confirmed
- [ ] Fact count claim extracted from title and recorded; minimum fact production target set
- [ ] Superlative inventory complete (all superlatives in title and concept noted and flagged)
- [ ] Curiosity Map (section sequence) drafted and recorded in Book Lock
- [ ] Facts-per-spread target range confirmed within OV-CFACT limits (max 8 per spread)
- [ ] Word budget per spread confirmed by knowledge depth
- [ ] Type floors recorded for body, callout/Wow, gloss, and caption — all above minimums
- [ ] Alignment rule recorded (left-aligned body; centered permissible for headers/callouts only)
- [ ] On-page gloss density per spread recorded
- [ ] Color mode: full color confirmed; section accent colors planned (4-8)
- [ ] Bleed flag: ON; bleed page dimensions recorded
- [ ] Fact-spread unit components understood and documented
- [ ] Front matter and back matter checklist recorded (glossary, source list, index requirement, etc.)
- [ ] Navigation system (running count, section color band, etc.) specified
- [ ] Gatekeeper (buyer) persona recorded
- [ ] Dual-source verification protocol: ACTIVE
- [ ] Child-safety battery: PENDING
- [ ] Read-aloud cadence test flagged (ON for AB-1 and AB-2-L1 / NOT APPLICABLE for AB-2-L2+)
- **GATE 1 STATUS: PASS / FAIL / PENDING**

### Gate 2 — Manuscript and Fact Verification

- [ ] All sections complete per Curiosity Map; section order follows curiosity logic (familiar → exotic)
- [ ] Every themed spread follows the Fact-Spread Unit structure: spread header + anchor fact + supporting cluster + Wow Callout + optional Quick Quiz
- [ ] Fact count verified: total individually numbered facts equals or exceeds the title count claim
- [ ] No fact appears on a page without thematic context (no orphan facts)
- [ ] Verification log complete: every fact has two independent authoritative sources recorded
- [ ] Superlative audit complete: every superlative claim verified; volatile superlatives dated inline in text
- [ ] Number lock complete: all quantities, statistics, and dimensions verified and hedged appropriately; unit consistency confirmed
- [ ] Concrete-example law: every abstract concept followed immediately by a concrete analogy
- [ ] Curiosity-logic sequencing: each section opens with familiar/surprising, ends with exotic/record-breaking
- [ ] Quick Quiz questions answerable from spread content; answers immediately adjacent to questions; no "see page X" answers for quiz
- [ ] Age-banded vocabulary audit: stretch-word count per spread within limits
- [ ] On-page glosses written and placed on every spread containing a stretch word
- [ ] Glossary in back matter complete and consistent with on-page glosses
- [ ] Source list in back matter written (minimum 2 sources per major fact; child-appropriate format)
- [ ] Index complete (required AB-3 / KD-3; recommended KD-2 over 64 pages)
- [ ] Further Reading list complete (3-5 entries per section theme)
- [ ] Word count per spread within band limits
- [ ] Type floor confirmed throughout: body, callout/Wow, gloss, and caption all above minimums
- [ ] Left-alignment confirmed; no full justification at AB-1 or AB-2 without explicit approval
- [ ] Read-aloud cadence test PASSED (AB-1 and AB-2-L1) or NOT APPLICABLE
- [ ] Child-appropriateness battery PASSED: all OV-CHILD checks plus OV-CFACT extensions (death/predation calibration, age-appropriate human body language, historical sensitivity, environmental framing, scary-content calibration)
- [ ] Final spread delivers the most astonishing fact in the book
- [ ] Front matter complete: title/ownership page, copyright, contents, introduction/welcome
- [ ] Back matter complete: glossary, source list, index (if required), Further Reading, optional Fast-Facts summary
- **GATE 2 STATUS: PASS / FAIL / PENDING**

### Gate 3 — Interior Design, Art, and Layout

- [ ] Section accent colors assigned (one distinct hue per section; all pass AA contrast)
- [ ] Colorblind simulation run on all diagrams and section color bands; no critical distinction conveyed by color alone
- [ ] All fact-spread layouts follow the 12-layer template order; no body text layer below the quiet-zone/opaque-panel layer
- [ ] Text-zone reservation confirmed: every illustration / photo brief stated the exact reserved zone BEFORE art was generated or commissioned
- [ ] Quiet zones and opaque panels present on all text-bearing pages; no body text on unprotected art texture
- [ ] All spread headers, anchor fact text, cluster text, Wow Callout text, Quick Quiz text, gloss text, captions, and labels are real editable typeset type — no AI-generated lettering anywhere in the manuscript
- [ ] All diagram labels are real typeset text with a title and a scale indicator where relevant
- [ ] Sidebar law: sidebars on no more than 40% of spreads; all sidebars visually subordinate to anchor fact
- [ ] Photo vs. illustration treatment: consistent throughout per Book Lock decision; no random alternation
- [ ] Navigation system: running fact-number badge (if count-claim book) visible and consistently positioned across all fact-bearing spreads
- [ ] Font roles: display face, body/learning face, and utility/gloss face applied correctly and consistently
- [ ] Type padding: minimum 0.25 in around body text; 0.20 in around captions and gloss text
- [ ] Panel edges clear of character heads, hands, eye lines, and essential props
- [ ] Bleed art extends to media edge on all bleed pages; no white sliver at trimmed edge
- [ ] Outside-edge parity: odd pages bleed right, even pages bleed left
- [ ] Critical content (text, key diagram labels) inside trim and 0.5 in safe zone
- [ ] Grayscale proof of every colored text page: distinctions survive without hue
- [ ] Accessibility: no critical information conveyed by color alone in any diagram
- [ ] Thumbnail view review: rhythm, section color logic, hierarchy, visual flow, no source-identifying resemblance to references
- [ ] 100%-render review: type, padding, panel edges, tangencies, art defects, diagram labels, navigation badges, folios, trim safety
- [ ] Spread view review: gutter, paired-page rhythm, page-turn direction, section header dominance
- [ ] Originality: thumbnail comparison against any supplied reference pages — no source-identifying resemblance
- **GATE 3 STATUS: PASS / FAIL / PENDING**

### Gate 4 — Production, Preflight, and Pre-Release

- [ ] Page count is even and within KDP's supported range for 8.5 x 11 full-color
- [ ] Premium color costing confirmed for books under 72 pages; standard color confirmed for 72+ pages
- [ ] Fact count final reconciliation: numbered facts in final PDF equal or exceed title claim
- [ ] Superlative audit re-confirmed on final text: all volatile superlatives dated; no undated volatile superlative in final manuscript
- [ ] Verification log confirmed as complete and available for internal record
- [ ] PDF export is fixed-layout with correct bleed page dimensions on every page
- [ ] MediaBox and BleedBox cover the full bleed page; TrimBox identifies the trim with correct parity offset
- [ ] CropBox does not hide bleed; no crop marks, registration marks, printer slugs, or comments in export
- [ ] All fonts embedded; no missing or substituted glyphs
- [ ] All placed images at minimum 300 DPI at placed size; no stretched or low-resolution enlargement
- [ ] No hidden layers, watermarks, or nonprinting objects
- [ ] Text extraction or preflight confirms real type throughout; no AI lettering
- [ ] Physical proof ordered and reviewed: actual trim (8.5 x 11 confirmed), paper weight, full-color saturation on all section accent colors, gutter behavior on double-page spread diagrams, Wow Callout legibility at actual print size
- [ ] KDP AI-disclosure requirement met (if AI tools used for any images or text)
- [ ] Child-safety battery re-confirmed at final state
- [ ] All gate statuses current with evidence; no gate claimed PASS without current evidence
- **GATE 4 STATUS: PASS / FAIL / PENDING**

**A book is not complete until Gate 4 STATUS is PASS with physical-proof evidence and fact-count reconciliation is on record.**

---

## KDP Positioning

### Amazon Category Tree

OV-CFACT titles compete in children's nonfiction. Select two categories from:

**Primary (select the most specific):**
- Books > Children's Books > Education & Reference > Science > General
- Books > Children's Books > Education & Reference > Science > Zoology
- Books > Children's Books > Education & Reference > Science > Astronomy & Space Science
- Books > Children's Books > Education & Reference > Science > Earth Sciences
- Books > Children's Books > Education & Reference > History
- Books > Children's Books > Education & Reference > Geography & Cultures
- Books > Children's Books > Education & Reference > Geography & Cultures > Animals
- Books > Children's Books > Animals > Mammals
- Books > Children's Books > Animals > Reptiles & Amphibians
- Books > Children's Books > Animals > Birds, Butterflies & Bugs
- Books > Children's Books > Animals > Marine Life
- Books > Children's Books > Animals > Dinosaurs & Prehistoric Creatures

**Secondary (supporting discoverability):**
- Books > Children's Books > Education & Reference > Almanacs & Encyclopedias
- Books > Children's Books > Science, Nature & How It Works

**Do not route to:**
- Fiction or story categories even if a narrative frame character is present
- Activity book categories unless activities constitute more than one-third of the book

### Description Strategy

The buyer is a parent, teacher, librarian, or gift-buyer — NOT the child. The description must pass the gatekeeper trust test before it appeals to the child's curiosity.

**Lead with (in this order):**
1. The knowledge promise and age-appropriateness signal ("Packed with 100+ verified amazing facts about [topic], designed for curious kids ages 8-12")
2. The Wow Hook — one standout fact from the book that will make the adult think "my kid would love this" ("Did you know a mantis shrimp can punch with the force of a bullet?")
3. The scope and structure: sections, fact-spread format, Quick Quiz elements, and any interactive features
4. The educational confidence statement: source verification, curriculum alignment if applicable, or expert authority
5. Bulleted feature list: page count, full-color illustrations, running fact numbers, glossary, index, For Ages X-Y
6. A gatekeeper call-to-action: "A perfect gift for curious young minds" or "Great for independent reading or classroom use"

**Never lead with** a plot summary, the child's perspective, "This book is about...", or a list of the book's table of contents topics. Gatekeepers skim for trust and value signals.

### Metadata Signals

- **Title field:** Include the primary keyword naturally ("Amazing Facts About Sharks: 100 Wild Truths for Kids Ages 8-12")
- **Subtitle field:** Age range + scope promise + one benefit ("Over 100 Verified Facts with Photos, Diagrams, and Did-You-Know Surprises")
- **Keywords (7 fields):** Topic + "for kids" or "for children" combinations; "amazing facts" + topic; "children's encyclopedia" + topic; "nonfiction books for kids ages [X-Y]"; "did you know books for kids"; "fun facts [topic]"; grade-level nonfiction phrases ("3rd grade nonfiction", "4th grade science books")
- **Series field:** Complete for every book in a series (e.g., "Amazing Facts Series"); drives Also Bought and series page placement
- **Author name:** Consistent across the series; a nonfiction pen name with a credibility signal ("Dr.", "[Subject] Expert") if applicable and truthful

---

## Key Rules — Do NOT Break

1. **Every fact is dual-source verified before the manuscript clears Gate 2.** No exception. Children's fact books are where sloppy facts propagate into young readers' permanent memory. A beautiful book with wrong facts is a liability, not a product.

2. **Superlatives must be verified and volatile superlatives must be dated inline.** "The fastest", "the biggest", "the deepest" claims that can change must carry "(as of [year])" in the text. Undated volatile superlatives will become wrong.

3. **The title count claim is a contractual promise.** A book titled "100 Amazing Facts" must contain at least 100 individually countable, verified facts. Count them before Gate 2. Padding a fact cluster to hit a number by splitting one fact into two similar sentences is prohibited.

4. **Fact-spread maximum is 8 facts.** Never exceed 8 facts in a single themed spread regardless of page size or knowledge depth. Cognitive overload is the enemy of retention. If a theme has more than 8 interesting facts, create a second themed spread on the same theme.

5. **Topic sequencing follows curiosity logic, not academic taxonomy.** Never organize a fact book by scientific classification order. Organize it by what a child wants to know next. Familiar → Surprising → Exotic is the spine.

6. **On-page glosses appear on the same spread as the stretch word.** "See glossary" is not a substitute for an on-page gloss. A child encountering an unfamiliar word will not flip to the back — they will skip the word and miss the fact.

7. **No Quick Quiz answers on a different page.** Quiz answers must be on the same spread as the questions. "Turn to page 47 for answers" breaks the cognitive loop of fact-test-confirmation that makes Quick Quiz educationally effective.

8. **Full color is the only permitted mode.** OV-CFACT titles compete on visual richness. Monochrome and selective-color treatments are prohibited. Budget for premium color from the outset.

9. **Diagrams require real typeset labels only.** No AI-generated lettering appears in any diagram, scale comparison, anatomical illustration, map, or infographic. Every label is real editable type. Every diagram has a title.

10. **The Wow Callout is selected from the facts, not invented.** The Wow Callout is the most astonishing fact in the supporting cluster, dramatized in language. It is not a made-up "fun exaggeration" or a fictional comparison. It must be as rigorously sourced as every other fact on the spread.

11. **Abstract facts must be followed immediately by a concrete example.** A child who reads "a neutron star has a density of 10^17 kg/m3" will not retain that fact. A child who reads "a neutron star is so dense that a teaspoon of it would weigh more than all the humans on Earth combined" will remember it forever. Concrete examples are not decoration — they are the mechanism of retention.

12. **The final spread is the best fact in the book.** Save the most astonishing, most shareable, most gasping fact for the final spread. This is what a child will repeat at dinner. It is also the fact most likely to be quoted in a review.

13. **All OV-CHILD non-negotiable rules apply.** Type floor, full-bleed geometry, real typography, text-zone reservation before art generation, character continuity, gatekeeper-first description copy, correction propagation, and state honesty are all inherited from OV-CHILD without modification. Where OV-CFACT tightens a rule (e.g., full-color requirement, dual-source verification), OV-CFACT governs.

14. **Correction propagation applies to fact corrections.** If a fact is corrected after Gate 2, the verification log must be updated, the on-page gloss may need revision, the Quick Quiz question testing that fact must be re-checked, and the back-matter source list and glossary must be reconciled. A fact correction reopens Gate 2 and all downstream gates for the affected spread.

15. **State Honesty rule.** Never claim verification, a proof order, a category search, or a source check occurred unless it did. Every gate reports PASS, FAIL, PENDING, NOT RUN, or UNVERIFIED with one line of evidence.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
