---
name: uapf-niche-childrens
description: Children's book overlay (CBF 2.0) — invoked by uapf-phase0-router when the title targets ages 0-12, contains children's, kids', picture book, board book, early reader, middle grade, or bedtime story signals, or the audience is clearly young children.
---

# UAPF Niche: Children's Books (OV-CHILD)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/CBF-2.0/` (config, validation, phases, and deterministic ops in `genie_childrens.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=CBF 2.0` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title or brief targets ages 0-12; contains "children's," "kids'," "picture book," "board book," "early reader," "chapter book," "middle grade," "bedtime story," "read-aloud," "toddler," "preschool," or a grade band K-6; or the subject/voice is unmistakably aimed at young children even without an explicit age marker. This overlay implements The Children's Book Framework (CBF 2.0) inside the UAPF pipeline: interior-led production, age-band supremacy, text-safety, purposeful color, bleed geometry, and evidence-based gates.

## Expert Panel

1. **Children's Publishing Director (Domain Master)** — 25+ years in trade children's publishing; owns age-band routing, profile selection, category conventions, and the final "would a bookstore shelve this?" judgment.
2. **Child Development & Literacy Specialist** — validates vocabulary load, sentence length, decodability, reading-mode fit (adult performs / child decodes / child reads alone), and read-aloud cadence for pre-reader bands.
3. **Children's Book Art Director** — owns character model sheets, style bible, page architecture, text-safe zones, color mode, typography floors, and thumbnail/100% visual QA.
4. **Print Production Manager (KDP)** — owns trim, bleed geometry, page-box parity, ink/paper economics (premium vs. standard color), font embedding, preflight, and physical-proof review.
5. **Gatekeeper Advocate (Parent/Teacher/Librarian proxy)** — runs the child-appropriateness battery, checks representation and diversity for authenticity, and audits the KDP description and metadata from the buyer's (adult's) point of view.

## Phase 0 — Title Analysis

### 0.1 Title clearance
- Search Amazon (Books > Children's Books) for the exact title and close variants. Children's shelves are crowded with near-identical concept titles ("My First...", "Goodnight...", "The Little...") — require clear differentiation in subtitle, character, or hook.
- Trademark/IP screen: children's titles frequently collide with protected characters, toy brands, TV properties, and classic-series trade dress. Reject any title, character name, or motif that is source-identifying of a protected property. Public-domain fairy-tale material is usable but must be transformed, not retold verbatim.
- Confirm the title makes its **age promise legible at a glance** (a parent scanning thumbnails must instantly know roughly who it's for).

### 0.2 Subject analysis and age-band lock (THE critical step)
Age band drives EVERYTHING. Classify in this exact order and lock before anything else:
1. **Hands first** — if the child's primary action is writing, solving, coloring, tracing, or prompted recording, route to a function-led profile (CB-WORK, CB-ACT, CB-COLOR, CB-JOURNAL).
2. **Intent second** — story experience routes to CB-PIC / CB-ER / CB-CHAP; knowledge acquisition routes to CB-CONCEPT / CB-FACT.
3. **Reading mode third** — adult performs, child decodes with support, or child reads fluently alone. For the ages 5-7 overlap: adult performs → picture-book spec; child decodes → early-reader level spec.
4. **Band lock last** — lock exactly ONE band; add reading level (L1-L4), school grade, or edition where the profile requires a second lock.

| Band | Ages | Reading mode | Word budget | Per-page load | Body type floor |
|---|---|---|---|---|---|
| AB-0 (board/baby) | 0-2 | Adult reads | 0-200 total | 2-8 words/page | 24-36 pt |
| AB-1 (picture) | 3-5 | Adult performs | 200-800 total | 1-3 sentences/spread | 18-24 pt |
| AB-2 (early reader) | 6-8 | Child decodes (lock L1-L4 or grade) | by level | short controlled sentences | 14-18 pt |
| AB-3 (chapter/middle grade) | 9-12 | Independent | by profile | full paragraphs, honest stakes | 11-14 pt |

Host profiles: CB-BOARD, CB-PIC, CB-CONCEPT, CB-ER, CB-CHAP, CB-FACT, CB-WORK, CB-ACT, CB-COLOR, CB-JOURNAL. **One book, one host profile.** Guest inserts (an activity spread in a picture book, etc.) obey the host's architecture and never exceed one-third of pages.

### 0.3 Subtitle generation
- Speak to the **gatekeeper** (parent/teacher/librarian), because the adult is the buyer. The subtitle carries the age promise and the benefit: "A Bedtime Story for Ages 3-5," "An Early Reader About Kindness (Level 2)," "A Funny Chapter Book for Kids 8-12."
- Include the explicit age range or level whenever the title itself doesn't signal it.
- Never promise educational outcomes you don't deliver, and never use fear-based or shaming hooks.

### 0.4 Auto-configuration (Book Lock)
Emit a Book Lock recording: concept, child promise, age band + second lock, reading mode, host profile, trim, page target, ink/paper, bleed on/off, total word budget, type floor, art-to-text ratio, color mode (full / selective / monochrome), language and direction, originality transformations chosen, and deliverables. Irreversible choices (age band, trim, language direction) require operator confirmation; noncritical gaps get a stated conservative assumption. Present the Book Lock, then proceed on PROCEED.

## Book Architecture

### Structural unit: the page/spread, not the chapter
Children's books are **page-architected**. Every page receives a functional role BEFORE art direction: title/ownership, contents, welcome, chapter opener, text-only, mixed narrative, full-scene, function page (activity/worksheet), or closing. Each page's spec fixes: role, word budget, text zone, art zone, color mode, page-turn job, bleed instruction, and folio rule.

### Page-band targets (KDP paperback minimum is 24 pages; verify live at release)
- **AB-0 board-style (printed as paperback):** 24-28 pages, one idea per page/spread.
- **AB-1 picture book:** 32 pages standard (24 min); ~12-14 story spreads plus front/back matter.
- **AB-2 early reader:** 32-48 pages; controlled chapters of 2-6 pages each.
- **AB-3 chapter book:** 64-120 pages; **middle grade:** 120-200+ pages; chapter formula: hook opening line → one escalating scene → soft cliff or emotional beat at chapter end.
- **Function books (workbook/activity/coloring/journal):** 60-110 pages; every function page self-contained and completable; child working areas at least 0.75 in from the gutter.

### Narrative rhythm (story profiles)
- Alternate load: never stack dense text pages back-to-back; follow a heavy page with visual relief.
- Escalate visibly: each scene changes the child's situation, knowledge, emotion, or task; repetition must accumulate (rule of three), not stall.
- **Page-Turn Law:** every narrative page creates forward motion; questions, partial reveals, motion, and gaze point toward the outside edge; never place the answer before the turn.
- End softly or decisively — the last page must feel intentional.

### Front matter (minimal — children's books earn trust fast)
- **Title/ownership page (page 1 or first recto):** one dominant title, one restrained supporting line, character anchor placed away from the title, one motif family, and (where age-appropriate) a functional ownership field with a real writing line. Max two font families. Must pass thumbnail AND 100% review.
- Copyright page: compact; include AI-content disclosure status per KDP policy.
- Contents page only where it helps the child navigate (early reader/chapter/fact/workbook); single consistent entry marker, page numbers on one right-aligned edge.
- Welcome page (function books): direct, reassuring second-person language and open space.

### Back matter
- Story bands: optional "The End" closing beat, author note to grown-ups, or discussion questions for parents/teachers.
- Fact/workbook bands: answer key (workbooks), glossary in child language, certificate-of-completion page where fitting.
- Series hook page ("More adventures with...") if a series is planned.

### 10-page concept sample blueprint (when a sample is requested before full production)
1 title/ownership; 2 contents; 3 welcome; 4 chapter opener; 5 text setup; 6 first illustrated action; 7 text bridge with hook; 8 choice/interaction; 9 payoff; 10 closing/reflection. Label it a concept sample — NOT a KDP-ready interior.

## Interior Design

Niche-specific — does NOT inherit the UAPF default. CBF 2.0 interior law applies.

### Trim and geometry
- **Picture-band books (AB-0, AB-1, and illustration-led AB-2): 8.5 x 8.5 in square trim, full-bleed interior.** Bleed page size = trim + 0.125 in width, + 0.25 in height (8.625 x 8.75). If ANY page bleeds, the entire PDF is built at bleed size. Odd pages carry the outside bleed extension on the right, even pages on the left; MediaBox/BleedBox cover the full bleed page, TrimBox marks trim with correct parity; export with NO crop marks.
- AB-3 chapter/middle grade: 5.25 x 8 or 6 x 9, typically black interior, no bleed.
- Workbook/activity: 8.5 x 11.
- Critical text and detail at least 0.5 in inside trim; child writing areas at least 0.75 in from the gutter.

### Color
- Picture bands: **full color** interior (premium color at short page counts — standard color currently starts at 72 pages; verify live and price accordingly).
- Color Has a Job: lock full color, selective color, or monochrome at Book Lock; in selective mode, spend the strongest color on the title page and the action/payoff beats. Never alternate color randomly. Grayscale-proof every colored text page.
- Palette lock: record paper, primary, secondary, accent, ink, skin, hair, clothing, and recurring-prop swatches; skin tones and wardrobe stay consistent across every page and every recolor pass.

### Typography
- Three font roles: one display face (titles/short labels only), one child-readable body face, one calm utility face (folios/contents). Max two families visible on any page.
- Type floors by band (see table above) — NEVER go below the floor to fit copy; edit, reflow, or add a page instead.
- Leading at least 1.3 (1.4-1.6 for learning text). **Body copy is LEFT-ALIGNED — never justified.** No hyphenation at early-reader L1-L2. No all-caps body text. Phrase-aware line breaks; never strand one short word.
- All type is **real, editable, embedded typography** set above the art. Art is generated wordless; any AI lettering is removed before layout.

### Layer stack (every illustrated page)
Bleed background → quiet zone or opaque paper panel → real typography → controlled accents → folio. Body copy sits on a uniform quiet zone or opaque panel with ≥0.20 in padding (0.25-0.35 in for emerging readers). No face, hand, action clue, prop, foliage, hair, or shadow edge behind body text. Panel edges may not slice through a head, hair, hand, eye line, or essential prop.

### Illustration system
- Before page one: character model sheet (front/side/three-quarter/back at equal scale; neutral/happy/worried/surprised/active expressions; exact skin/hair/eye/wardrobe/prop swatches; relative height chart) and style bible (rendering, line, lighting, horizon, palette, environmental logic).
- Every illustration prompt states the reserved text zone in exact proportional language ("upper 32 percent, full width, plain warm ivory, no figures or objects") and requires wordless art.
- Inspect every image for anatomy, continuity, style match, background logic, reserved-zone compliance, incidental lettering, IP resemblance, aspect ratio, and 300+ DPI at placed size.

## Content Rules

**The fatal flaw to avoid: writing for the adult instead of the child — or letting art fight the text.** A children's book fails when its vocabulary, sentence length, humor, or moralizing pitches above the locked band, or when body copy sits on busy art. Children's text exists to be performed, decoded, understood, or done — not to impress an adult with complexity.

Hard constraints:
1. **Audience Supremacy.** Every word, layout, type, color, and illustration decision derives from the ONE locked age band and reading mode. Vocabulary, sentence structure, and emotional stakes must sit inside the band.
2. **Child-appropriateness battery — ALWAYS ON.** No graphic violence, sexual content, substance glamorization, profanity, dangerous imitable acts presented without consequence, body-shaming, or fear-based instruction. Peril and honest emotion are allowed at band-appropriate intensity (AB-3 may carry real stakes; AB-0/AB-1 resolve warmly). Health/safety facts must be accurate and non-frightening.
3. **Diversity and representation without tokenism.** Cast characters with varied skin tones, family structures, abilities, and settings as ordinary reality, not as labeled lessons. Representation is drawn in the model sheets and held by the continuity lock — never a one-page gesture. Avoid stereotyped names, dialect mockery, and cultural costume clichés.
4. **Read-aloud cadence (AB-0/AB-1, and any rhyming text).** Every page is tested by reading aloud: natural breath points, no tongue-stumbles, rhythm supports the page turn. Rhyme only if the meter is genuinely clean throughout — abandoned or forced rhyme fails Gate 2. Repetition/refrain is a feature; use it deliberately.
5. **Decodability (AB-2).** Lock a level L1-L4 or grade; control sentence length, phonic complexity, and sight-word load to that level consistently — no difficulty spikes.
6. **Original Transformation.** Studied competitor patterns must be transformed through at least three dimensions (cast/world, motif vocabulary, grid/scale, palette, typography, pacing, interaction). No copied wording, characters, scenes, distinctive motifs, trade dress, or near-identical page sequence.
7. **Text Supremacy.** If art and text compete, text wins — quiet zone or opaque panel, always.
8. **White-Space Law.** A text-bearing children's page must breathe; fix density by editing, reflow, or a new page — never by shrinking type below the band floor.
9. **Continuity.** Recurring characters, wardrobe, scale, props, lighting, and rendering style are locked before page production and rechecked after every image change.
10. **State honesty.** Gates report PASS / FAIL / PENDING / NOT RUN / UNVERIFIED with evidence; never claim a check ran when it didn't.

## QA Checklist

### Gate 1 — Book Lock & Architecture (before drafting)
- [ ] Exactly one age band + reading mode + host profile locked; second lock (level/grade/edition) present where required
- [ ] Title cleared (search + trademark/IP screen); subtitle carries age promise to the gatekeeper
- [ ] Trim, page target, ink/paper, bleed, color mode, word budget, and type floor recorded in Book Lock
- [ ] Page map assigns every page a role, word budget, text zone, art zone, color mode, page-turn job, bleed instruction, folio rule
- [ ] If references were studied: Reference Pattern Report + Style Lock exist and 3+ originality transformations are named
- [ ] Character model sheet and style bible complete before any page art

### Gate 2 — Manuscript (per page/spread, then whole book)
- [ ] Word count per page within band budget; total within Book Lock budget
- [ ] Vocabulary, sentence length, and stakes inside the locked band; AB-2 level consistency verified
- [ ] Read-aloud pass performed for AB-0/AB-1 and all rhyming text (cadence, breath points, clean meter)
- [ ] Page-Turn Law: every narrative page pushes forward; no answer revealed before the turn; ending intentional
- [ ] Child-appropriateness battery passed; representation authentic, no tokenism or stereotype
- [ ] Originality audit: no copied wording, characters, scenes, or source-identifying sequence

### Gate 3 — Art, Layout & Typography (per page, then thumbnail sheet)
- [ ] Every image wordless; all lettering is real embedded type; no AI pseudo-text remains
- [ ] Text zones honored: quiet zone/opaque panel, ≥0.20 in padding, no detail behind body copy, clean panel edges
- [ ] Type at or above band floor, leading ≥1.3, body copy left-aligned, no justified text, no all-caps body
- [ ] Character/world continuity verified against model sheet on every page; anatomy and tangency audit clean
- [ ] Color mode consistent with lock; palette lock held; grayscale proof of colored text pages passes
- [ ] Thumbnail sheet: rhythm, hierarchy, color distribution OK; no source-identifying resemblance to references
- [ ] 100% render: no collisions, clipping, or trim-unsafe critical content; spread view: gutter and paired-page balance OK

### Gate 4 — Print & Release (whole book)
- [ ] Even page count; ≥24 pages; page count vs. color-ink economics verified against live KDP values
- [ ] Entire PDF at correct bleed size (picture bands: 8.625 x 8.75 for 8.5 x 8.5 trim); parity-correct trim boxes; no crop marks
- [ ] All fonts embedded with commercial/embedding rights; images ≥300 DPI at placed size
- [ ] Critical content ≥0.5 in inside trim; child working areas ≥0.75 in from gutter; no white slivers at edges
- [ ] Cover wrap matches final page count/spine; age range on cover/description matches the locked band
- [ ] AI-content disclosure recorded per KDP policy; live KDP specs recon rechecked and dated
- [ ] Physical proof ordered and inspected (color, trim, gutter swallow, panel edges) — proof is the color authority
- [ ] Any correction reopened its gate and all downstream gates, with fresh evidence

## KDP Positioning

- **Category tree:** Books > Children's Books > [subject], matched to band — e.g., Children's Books > Growing Up & Facts of Life; > Early Learning; > Animals; > Literature & Fiction > Chapter Books (AB-3); plus Kindle category equivalents. Set the **age range and grade range fields precisely to the locked band** — this is a primary ranking and browse signal for children's books.
- **The description speaks to the GATEKEEPER.** The parent/teacher/librarian is the buyer. Lead with the child benefit through adult eyes: what the child will feel, learn, or do; the age fit; read-aloud or independent-reading suitability; and reassurance signals (gentle bedtime wind-down, classroom-friendly, screen-free activity). Then one short taste of the story voice. Close with format facts: age range, page count, trim, full-color where true.
- **Metadata signals:** keywords pair audience + occasion + subject ("bedtime stories for toddlers," "kindergarten graduation gift," "early reader level 2 animals"). Never keyword-stuff protected brands or competitor titles. Seasonal/gift framing (birthday, holiday, first day of school) where honest.
- Series-ready titling (repeatable character/world naming pattern) when a series is planned; children's buyers are the most series-loyal segment on the platform.

## Key Rules — Do NOT Break

1. **Age band drives EVERYTHING.** Lock one band (board / picture / early reader / chapter / middle grade) and one reading mode before production; every content, type, color, layout, and art decision derives from it.
2. **Picture-band books: 8.5 x 8.5 trim, full color, full bleed, illustration-led on every page, large display type** — and body copy **LEFT-ALIGNED, never justified.**
3. **Type floors are floors.** AB-0 24-36 pt, AB-1 18-24 pt, AB-2 14-18 pt, AB-3 11-14 pt. Never shrink below the floor to fit; edit, reflow, or add a page.
4. **Text Supremacy.** Body copy sits on a quiet zone or opaque panel; no faces, hands, props, or texture behind text; art is generated wordless and all lettering is real embedded type.
5. **Child-appropriateness battery is always on.** No content outside the band's emotional or safety envelope; imitable danger is never shown without consequence.
6. **The gatekeeper is the buyer.** Cover, subtitle, description, and metadata speak to the parent/teacher — with the exact age range stated.
7. **Diversity and representation without tokenism** — built into model sheets and continuity locks, never a labeled one-page gesture.
8. **Read-aloud cadence tested for pre-reader bands** (AB-0/AB-1); rhyme only with clean meter throughout.
9. **Pattern, not product.** References teach page function and proportion only; every adopted pattern is transformed through 3+ dimensions; thumbnail-scale resemblance audit before release.
10. **Bleed is geometry and correction propagates.** One bleeding page means the whole file is bleed-sized with parity-correct boxes and no crop marks; every correction reopens its gate and all downstream gates; report gate status only with current evidence.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
