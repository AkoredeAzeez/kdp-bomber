---
name: uapf-niche-activity
description: Activity, puzzle, and coloring book overlay (OV-ACT) — invoked by uapf-phase0-router when the title or format signals puzzles, sudoku, word search, crossword, maze, coloring book, activity book, logic puzzle, kakuro, dot-to-dot, or any puzzle/activity/coloring format.
---

# UAPF Niche: Activity, Puzzle & Coloring Books (OV-ACT)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** the title or brief contains any of: *puzzle, puzzles, sudoku, word search, crossword, maze, mazes, coloring book, colouring book, activity book, logic puzzle, kakuro, dot-to-dot, connect the dots, brain games, brain teasers, hidden pictures, spot the difference, cryptogram, word scramble, trivia book, riddles* — or the requested format is puzzle/activity/coloring rather than prose. This overlay governs any book whose value is delivered through interaction (solving, drawing, coloring, writing-in) rather than reading.

---

## Expert Panel

1. **Puzzle Engineer (Domain Master)** — designs every activity from structured source data; owns solvability, uniqueness, difficulty calibration, and the answer ledger. Final authority on whether a puzzle ships.
2. **Activity-Book Art Director** — owns the visual system: line weight, contrast, page rhythm, coloring-page quality, safe text zones, and the three-layer page model (background art / exact overlay text / answer-bearing marks).
3. **Print Production Specialist** — owns trim, bleed, margins, single-sided budgeting, gutter safety for writing/cutting activities, ink-mode fidelity (no gray-on-gray collapse), and KDP preflight.
4. **Audience & Accessibility Editor** — routes children / teens / adults / seniors / accessible editions; enforces reading load, motor demand, print size, contrast, and safety-language rules for the locked audience.
5. **QA Test-Solver** — independently solves puzzles from the printed page (not the source data), audits answer-key synchronization, hunts duplicates, and verifies the difficulty arc actually plays as promised.

---

## Phase 0 — Title Analysis

### 0.1 Title clearance
- Preserve the supplied title exactly; never rewrite the concept without operator approval.
- Trademark scan: reject or flag titles leaning on protected properties (branded characters, game trademarks such as "Scrabble", "Wordle", "Rubik's", licensed franchises). Generic mechanic names (sudoku, crossword, word search, maze) are safe.
- Claims scan: strip or soften any medical/therapeutic promise in title or subtitle ("prevents dementia", "cures anxiety", "boosts IQ"). Permitted claims are descriptive only: *large print, high contrast, progressive difficulty, answer key included, short independent sessions*.

### 0.2 Subject analysis — classify before configuring
Determine, from the title alone plus any brief:

**A. Dominant activity family** (exactly one; up to three supporting families):
mixed activity | coloring/visual art | pre-writing/fine motor | early learning | mazes | visual search (hidden objects / spot-the-difference) | word puzzles (word search, crossword, scramble, cryptogram) | number/logic (sudoku, kakuro, calcudoku, logic grid) | trivia/riddles | dot/grid drawing (dot-to-dot, grid copy) | paper/social games | creative writing prompts | crafts/experiments | wellness/cognitive support | seasonal/cultural/event | story-driven deduction/mystery.
The dominant family controls structure, validation, answer treatment, and marketing promises. Hybrids still declare one dominant route.

**B. Language-Independence Classification (mandatory — record in the contract):**
- **Language-independent:** mazes, sudoku, kakuro, dot-to-dot, coloring pages, spot-the-difference, hidden pictures, grid drawing, most number/logic puzzles. Only instructions and front matter need localization; puzzle bodies port across editions.
- **Language-dependent:** word searches, crosswords, word scrambles, cryptograms, trivia, riddles, creative-writing prompts, deduction stories. These must be **rebuilt from a locale-specific word bank / fact base per edition — never mechanically translated** from a finished grid.
- Mixed books record the classification per item in the manifest. This classification drives the localization plan, the marketplace strategy (language-independent books can multi-market cheaply), and the duplicate-scan scope.

**C. Audience band:** children (with age band) / teens / adults / seniors / accessible-cognitive-support. Audience routing changes mechanics, reading load, typography, motor demand, safety language, and answer presentation — it is not a label.

### 0.3 Subtitle generation
Generate 3–5 subtitle candidates that state, concretely: puzzle count ("200 Puzzles"), difficulty span ("Easy to Expert"), audience ("for Adults", "for Kids Ages 6–8"), and one differentiator (large print / with solutions / travel size / progressive levels). Every number in the subtitle becomes a **locked count promise** that must reconcile with the page map. Never promise a count the architecture cannot deliver.

### 0.4 Auto-configuration
| Setting | Default |
|---|---|
| Interior page count | **Exactly 100 pages** (96–104 even only with documented manufacturing/category reason) |
| Trim | 8.5 × 11 in (activity/coloring); 6 × 9 in permissible for compact travel puzzle books |
| Ink | B&W interior default; color only when the concept requires it (raises unit cost) |
| Bleed | No, unless full-page coloring/scene art requires it |
| Single-sided | **Yes for coloring books** (budget blank reverse pages from the start); No for write-in puzzle books on suitable paper |
| Difficulty | Progressive arc (see Content Rules) |
| Answer policy | Full solutions section, mandatory for every answer-bearing activity |
| Production mode | 10-page representative sample first when requested or references supplied; then full book |

Assign `project_id` and `edition_id`, freeze the contract, and record risk flags: young audience + small print/dense grids; senior edition + low contrast/tiny keys; count promise accidentally including front matter or answer pages; image-dependent puzzle whose solution wasn't encoded before image generation; coloring/cut-out pages conflicting with duplex assumptions.

---

## Book Architecture

### Structural unit: the **Puzzle Unit**
Every activity is one manifest-backed unit: `item_id` + instruction text + source data + puzzle body + (visual asset if any) + canonical answer + difficulty rating + page assignment. No puzzle exists on a page before it exists in the manifest.

### Default 100-page map (puzzle-dominant book)
| Pages | Content |
|---|---|
| p1–p4 | Front matter: title page, copyright, "How to Use This Book" (with worked example for any non-obvious mechanic), difficulty legend / contents |
| p5–p84 | Activity area — 80 pages of puzzles in a controlled difficulty arc |
| p85–p98 | Solutions section — every answer-bearing item, keyed by item ID and final page number |
| p99 | Progress tracker / completion certificate |
| p100 | Notes page |

### Coloring-book variant (single-sided)
p1–p4 front matter; then 45–48 full coloring designs each backed by a blank reverse (budgeted from the start — the true design count is stated honestly in metadata); closing test-color page + certificate. No solutions section required; a thumbnail index may replace it.

### 10-page sample map
p1 title/ownership; p2 premise/promise; p3 how-to-use; p4 legend/worked example; p5–p8 four representative activities (prototype the *hardest* mechanics here); p9 capstone; p10 solutions/explanation.

### Count reconciliation (before drafting a single page)
Build a count ledger: promised items + items per page + solution entries + blank backs + front matter + closing pages = exact approved page total. **Never count** title pages, copyright, instructions, answer pages, blank backs, dividers, or certificates as puzzles. A page holding multiple mini-activities counts each only when it has its own distinct instruction, input, and expected response.

### Layout laws
- Answer-bearing content lives in the layout layer (exact editable text, grids, marks) — never trapped inside generated imagery.
- Writing/coloring/cutting zones never enter the gutter; preserve generous safe margins beyond KDP technical minimums.
- Solutions are grouped at the back (never on the facing page of the puzzle), rendered legibly at print scale — miniature keys must survive B&W printing.

---

## Interior Design

Inherits UAPF default typography engine, with these OV-ACT overrides:
- **Trim:** 8.5 × 11 in default; design at final trim from page one.
- **Three-layer page model:** (1) generated background/illustration art, (2) exact overlay text — instructions, clues, page numbers — as live layout text, (3) answer-bearing marks (grids, letters, numbers, dots, coordinates) placed deterministically from source data. Flatten only after all text and answer verification passes.
- **Typography by audience:** children — large rounded sans, minimal words per instruction; adults — clean sans/slab hierarchy; seniors/large-print — 14 pt+ body, 16 pt+ grid characters, high contrast, uncrowded keys.
- **Grids:** high-contrast rules, cells sized for handwriting (sudoku cells ≥ 0.4 in at trim for standard editions, larger for large-print), consistent stroke weights book-wide.
- **Color scheme:** B&W interiors must be designed for B&W — no gray-on-gray, no color-dependent clues. Coloring pages: crisp closed line art, consistent line weight, no gray fills competing with the colorist.
- **Imagery:** generated per the UAPF image pipeline, one asset per call, with the object/difference ledger held *outside* the image; reject outputs with unintended extra clues, illegible objects, broken continuity, or low contrast. 300 ppi effective at print size.

---

## Content Rules

### The fatal flaw: an unsolvable or wrongly-keyed puzzle
One word search with a missing word, one sudoku with two solutions, one maze with no exit, or one answer key that doesn't match its puzzle destroys the book's single promise and earns 1-star reviews that kill the listing. Therefore: **every answer-bearing activity is generated from structured source data, and its answer is generated from that same data — never reconstructed by eye from the finished page.**

### Hard constraints
1. **Manifest-first generation.** Word puzzles: curated locale word bank → grid → placements → answer coordinates. Mazes: topology → start/finish → solution route → uniqueness rule. Number/logic: formal constraints → givens → complete solution → uniqueness result. Visual search: object/difference ledger with exact counts and locations. Trivia: claim → authoritative source + date → canonical answer + acceptable wording. Dot-to-dot: coordinate sequence → bounds → intended figure.
2. **100% solvability.** Every puzzle must be formally checked solvable, and uniqueness verified wherever uniqueness is promised (sudoku/kakuro/logic always promise it).
3. **Complete solutions section.** Every answer-bearing item appears in the back matter, keyed by item ID and final page number. Visual activities get annotated visual answers (circled objects, drawn maze route); deduction/riddle/trivia items get concise reasoning; legitimate alternate answers recorded only when the activity truly permits them.
4. **Difficulty arc.** Progressive and honest: open gentle, ramp deliberately, close challenging. Rate difficulty from reading load + rule complexity + visual density + working-memory demand + motor precision + solve time — **never from age alone**. Label bands (Easy/Medium/Hard or ★ system) consistently; a "progressive difficulty" subtitle claim must be demonstrable in the page order.
5. **Puzzle-type diversity quotas.** In mixed/variety books, no single supporting mechanic exceeds ~40% of activity pages; rotate cognitive and visual demand so no two adjacent spreads repeat the identical mechanic+theme combination. Single-mechanic books (pure sudoku etc.) instead vary within the mechanic: grid seeds, difficulty, and variants.
6. **No duplicates, no filler.** Run a duplicate-puzzle scan via manifest content hashes: no repeated grids, repeated word lists (or >50% word overlap between word searches), recycled clues with cosmetic changes, or re-used maze topologies. No decorative pages counted as activities.
7. **Accidental-string audit.** Word search grids and scrambles must be scanned for accidental offensive words in every declared direction — mandatory for children's books, required for all.
8. **Instructions with worked examples** for any non-obvious mechanic, written at the audience's reading level. A child must be able to start a puzzle without an adult explaining it; a senior must never squint at the rules.
9. **Language-dependent content is rebuilt per locale**, never translated in-grid. Language-independent content ports with localized instructions only.
10. **Safety and claims:** no medical/therapeutic outcome claims; cognitive benefits framed as "practice opportunities" only. Crafts/experiments carry age-appropriate safety notes. Content is culturally reviewed for the target marketplace.

---

## QA Checklist

### Gate 1 — Contract & Architecture (before any content)
- [ ] Title preserved; trademark and claims scan passed
- [ ] Dominant family + supporting families locked; Language-Independence Classification recorded
- [ ] Audience band locked with accessibility route where applicable
- [ ] Page map totals exactly 100 (or documented 96–104 exception); count ledger reconciles promised count vs. activity pages vs. solution budget vs. blank backs
- [ ] Single-sided budget explicit for coloring/cut-out content; subtitle numbers match the ledger
- [ ] Risk register written; contract frozen with project_id/edition_id

### Gate 2 — Manifest & Sample (before full generation)
- [ ] Every planned item has a manifest row with source data created *before* page design
- [ ] 10-page sample (when required) demonstrates premise, instructions, ≥4 substantive activities, visual system, and answer loop — hardest mechanics prototyped here
- [ ] Visual specification locked; generated sample images pass the acceptance criteria (ledger match, no unintended clues, contrast, safe text zones)
- [ ] Originality audit vs. any references: functional completeness high, expressive similarity low; zero reference pixels in project assets

### Gate 3 — Full Content Validation (before layout freeze)
- [ ] **100% solvability audit:** every item formally validated per mechanic — word search targets all in-bounds in declared directions; crossword lengths/entries/crossings agree; every maze finish reachable with promised path rule; sudoku/logic solutions valid and unique; spot-the-difference/hidden-object counts match approved images; cryptogram mappings round-trip; trivia sourced with date; dot-to-dot sequences complete, in-bounds, produce the intended figure; deduction cases fair, disclosed, single-culprit
- [ ] **Duplicate-puzzle scan** passed on content hashes (grids, word lists, topologies, clue sets)
- [ ] Difficulty arc audited by test-solve: labels match actual solve experience; progression is monotone within sections
- [ ] Diversity quotas met; no adjacent mechanic+theme repeats
- [ ] Accidental offensive-string scan passed on all letter grids
- [ ] Independent test-solve of a representative sample plus all expert/uniqueness-claim items from the *rendered page*, not the source data
- [ ] Human QA: ambiguity, reading level, cultural fit, print-scale visibility, response-space adequacy, enjoyment

### Gate 4 — Layout, Solutions Sync & Preflight (before print-ready status)
- [ ] Post-pagination synchronization audit: item ID ↔ final page number ↔ answer entry ↔ visual asset ↔ locale — zero mismatches
- [ ] **Complete solutions section:** every answer-bearing item present, correctly keyed, legible at print size; visual answers annotated
- [ ] Exact page count and promised activity count confirmed on the final PDF; no accidental blanks, duplicates, placeholders, crop marks, watermarks, or residual reference material
- [ ] Nothing clipped or trapped in the gutter; writing/coloring zones respect safe areas; blank backs positioned as budgeted
- [ ] Images at 300 ppi effective; fonts embedded with full locale glyph coverage; B&W pages verified for grayscale fidelity
- [ ] Cover wrap generated only after final interior locked; metadata claims match the files; AI-content disclosure recorded; live KDP previewer passes; proof ordered where risk warrants

---

## KDP Positioning

- **Category tree:** children's titles → *Books > Children's Books > Activities, Crafts & Games > Activity Books* (or *Games > Mazes / Word Games* per dominant family). Adult puzzle titles → *Books > Humor & Entertainment > Puzzles & Games > [Sudoku / Crossword / Word Search / Logic & Brain Teasers]*. Adult coloring → *Humor & Entertainment > Puzzles & Games > Coloring Books for Grown-Ups*. Large-print/senior editions also target *Puzzles & Games > Large Print* signals.
- **Description leads with the promise numbers:** puzzle count, difficulty span, and audience in the first line ("200 large-print word search puzzles with full solutions — easy to challenging, made for relaxed daily solving"). Then: what's inside (mechanic mix, progression, solutions section), format facts (trim, large print, single-sided), and a descriptive-claims-only benefits line.
- **Metadata signals:** keywords built from mechanic + audience + qualifier combinations (e.g., "sudoku large print seniors", "word search for kids ages 6-8", "logic puzzles adults hard"); subtitle carries the count and difficulty claims; A+ Content shows real interior spreads including one solutions page to prove the answer key exists.
- **Never claim in metadata** what Gate 4 hasn't verified in the files — counts, difficulty labels, "large print", and "solutions included" are all audited claims.
- One language-market edition = one product with its own edition_id, rebuilt language-dependent content, and its own verified print configuration.

---

## Key Rules — Do NOT Break

1. **Manifest before page.** Every answer-bearing activity is built from structured source data stored in the manifest; the answer key is generated from that same data, never reconstructed from the finished page.
2. **100% solvability, audited twice.** Every puzzle is formally validated solvable (and unique where promised) before pagination, and re-audited for ID↔page↔answer synchronization after final composition.
3. **Complete solutions section always** for answer-bearing books — every item keyed by ID and final page number, legible at print scale, with visual answers annotated.
4. **Classify language-independence at Phase 0** and rebuild all language-dependent puzzles from locale word banks per edition; never mechanically translate a finished grid.
5. **Exactly 100 interior pages** by default; 96–104 even pages only with a documented reason; the count ledger must reconcile before drafting.
6. **Count promises are sacred:** front matter, instructions, answer pages, blank backs, and certificates are never counted as puzzles; single-sided blank backs are budgeted from the start.
7. **Honest, progressive difficulty arc** rated on cognitive/visual/motor load — never on age alone — with labels that survive independent test-solving.
8. **Diversity quotas and duplicate scan:** no mechanic over ~40% of a variety book, no adjacent mechanic+theme repeats, and zero duplicate grids/word lists/topologies by content hash.
9. **Answer-bearing marks live in the layout layer,** never inside generated images; flatten only after text and answer verification.
10. **Original everything:** wording, datasets, clue structures, grids, art, names, and compositions. Competitor material defines function and genre only — never expression.
11. **Scan every letter grid for accidental offensive strings** in all declared directions before layout freeze.
12. **No medical or therapeutic claims** anywhere in the book or listing; descriptive, file-supported claims only.
13. **Not print-ready until every gate passes** — content, visual, answer, localization, accessibility, and KDP preflight — with evidence, not intention.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
