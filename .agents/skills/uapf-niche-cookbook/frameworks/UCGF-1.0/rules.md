# UCGF 1.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full cookbook niche skill.
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules (#1–#16).

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Executive Chef, Registered Dietitian, Interior Designer, Content-Standards
  Auditor, KDP Category Strategist (SKILL.md "Expert Panel").
- **Recipe-page structure & anatomy** — two archetypes, recipe never splits, method restarts at 1,
  Per Serving ends with theme nutrient (SKILL.md "Structural Unit: the Recipe Page").
- **Divider pages** — full-bleed photography + centered title band, wordless art (SKILL.md).
- **Design DNA / No-Two-Books-Alike** — five-axis fingerprint; palette + full fingerprint unique
  (SKILL.md "Design DNA"; global rule #9).
- **Food-photography style bible** — locked once per book, repeated in every food prompt.
- **KDP positioning** — category tree, description lead, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles; full text in SKILL.md "Key Rules — Do NOT Break")
1. Two recipes per page in the chosen archetype; never split; never mix archetypes.
2. No pork, no alcohol — silent, never named (global rule #1/#2).
3. Each recipe + photo fills its space (80–90% in Archetype A).
4. A finished-dish photo per recipe; every image a numbered manifest slot.
5. Every method restarts at 1.
6. Body 11 pt Times New Roman (overrides the 12 pt default).
7. Exactly two colors; no palette or fingerprint collision across the catalog.
8. Full-color interior at 8.625 × 11.25 in; page length honors deployment policy.
9. Full-bleed divider with title band; wordless embedded art.
10. Locked title immutable; seed words preserved in any replacement.
11. One premium editable DOCX with render QA.
12. No em dashes; no third-party brands; no catalog recipe duplicates.

**Deterministic checks** for the computable rules (pages, categories, image count, per-serving
rounding, budget) are implemented in `genie_cookbook.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
