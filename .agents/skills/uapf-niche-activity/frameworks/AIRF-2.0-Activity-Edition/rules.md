# AIRF 2.0 Activity Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full activity/puzzle/coloring niche skill (OV-ACT).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Puzzle Engineer, Activity-Book Art Director, Print Production Specialist,
  Audience & Accessibility Editor, QA Test-Solver (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — title clearance, subject analysis (dominant family, mandatory
  Language-Independence Classification, audience band), subtitle generation, auto-configuration
  (SKILL.md "Phase 0 — Title Analysis").
- **Structural unit: the Puzzle Unit** — manifest-backed item_id + instruction + source data +
  body + asset + canonical answer + difficulty + page assignment (SKILL.md "Book Architecture").
- **Page maps** — 100-page puzzle-dominant map, single-sided coloring variant, 10-page sample map,
  count reconciliation ledger (SKILL.md "Book Architecture").
- **Three-layer page model & layout laws** — art / overlay text / answer-bearing marks; answer marks
  never trapped in imagery; gutter-safe zones; solutions grouped at back (SKILL.md "Interior Design",
  "Layout laws").
- **KDP positioning** — category tree by family/audience, promise-number description lead, audited
  metadata claims (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Manifest before page (answer key from source data, never reconstructed from the finished page).
2. 100% solvability, audited twice (uniqueness where promised; re-audit ID↔page↔answer sync).
3. Complete solutions section always for answer-bearing books.
4. Classify language-independence at Phase 0; rebuild language-dependent puzzles per locale.
5. Exactly 100 interior pages by default (even 96–104 only with documented reason).
6. Count promises are sacred (front matter/instructions/answers/blank backs/certificates never counted).
7. Honest, progressive difficulty arc rated on cognitive/visual/motor load, never age alone.
8. Diversity quotas and duplicate scan (no mechanic > ~40%; no adjacent repeats; zero dup grids/lists/topologies).
9. Answer-bearing marks live in the layout layer, never inside generated images.
10. Original everything (wording, datasets, clue structures, grids, art, names, compositions).
11. Scan every letter grid for accidental offensive strings in all declared directions.
12. No medical or therapeutic claims anywhere in the book or listing.
13. Not print-ready until every gate passes, with evidence not intention.

**Deterministic checks** for the computable rules (page-count validity, count-ledger reconciliation,
sample-map validity, diversity quota, word-list overlap, difficulty-arc monotonicity, single-sided
coloring budget) are implemented in `genie_activity.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
