# USGPF 2.9 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full language-learning niche skill (OV-LANG).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (native speaker of the TARGET language, listed first,
  non-negotiable), Applied Linguist, Cultural Consultant, Bilingual Copy Editor, Technical
  Production Editor (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — 13 ordered steps; Direction Declaration is the blocking hard
  requirement (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — front matter; six-element communicative unit; back matter sequence
  (SKILL.md "Book Architecture").
- **Interior Design** — page geometry, bilingual dialogue presentation, vocabulary-block tables,
  grammar section, box styles, non-Latin script rendering (SKILL.md "Interior Design").
- **KDP positioning** — Foreign Language Study category tree, description lead, metadata signals
  (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Direction Declaration is a Phase 0 hard requirement.
2. Domain Master must be a native speaker of the TARGET language.
3. Zero tolerance for machine-translation artifacts.
4. One grammar point per unit, no exceptions.
5. Register must be labeled exhaustively.
6. Regional variant discipline is absolute.
7. Unit architecture is fixed and sequential (six elements, fixed order).
8. No invented sources in Appendix C.
9. Content standards rule is absolute throughout (no pork, no alcohol, no associated scenarios).
10. Cultural notes are factual and specific, never stereotypical.
11. No credentials or invented biography for the byline.
12. Non-Latin script rendering is verified visually on the rasterized render.

**Deterministic checks** for the computable rules (vocabulary load, dialogue turns, grammar-point
count, drill count, cultural-note length, unit page band, glossary/answer-key totals, subtitle,
byline locations) are implemented in `genie_language.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
