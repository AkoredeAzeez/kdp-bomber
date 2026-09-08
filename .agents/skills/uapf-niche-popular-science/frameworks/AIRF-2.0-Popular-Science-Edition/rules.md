# AIRF 2.0 Popular Science Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Popular Science (OV-POPSCI) niche skill.
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (research scientist in the detected field), Science Communicator,
  Evidence Historian & Methods Specialist, Quantitative Fidelity Editor, Nature & Taxonomy Verifier
  (nature/field-guide titles) (SKILL.md "Expert Panel").
- **Phase 0 title analysis** — Title Clearance Gate, subject analysis, central-question inventory,
  consensus map, subtitle generation, auto-configuration, TOC + Proceed gate (SKILL.md "Phase 0").
- **Explainer chapter architecture** — the six-stage sequence hook question -> intuition-building ->
  mechanism -> evidence story -> implications -> wonder payoff (SKILL.md "Book Architecture").
- **Field-guide variant** — fixed identification-entry field architecture; safety-critical
  look-alikes (SKILL.md "Book Architecture — FIELD-GUIDE VARIANT").
- **Interior design** — trim, book serif at 11-11.5 pt justified, native-built figures, Style
  Signature, 3-5 feature devices (SKILL.md "Interior Design").
- **The fatal flaw** — wonder purchased with inaccuracy (SKILL.md "Content Rules").
- **KDP positioning** — category tree, description hook, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Consensus discipline is absolute (established stated plainly, frontier labeled, controversy fairly presented).
2. Every chapter runs the full six-stage explainer architecture; no stage skipped.
3. Every analogy acknowledges where it breaks, in the prose, at the point of use.
4. Every chapter tells at least one HOW-we-know evidence story with verified people, dates, results.
5. Numbers humanized but EXACT underneath; no truth-losing rounding; order-of-magnitude honesty.
6. No mysticism dressed as science; no quantum-consciousness / energy-healing / teleology language, including metadata.
7. Species names, taxonomy, and conservation statuses current to the production date; verification date recorded.
8. The consensus-classification audit runs claim-by-claim at QA; one frontier claim dressed as settled fact blocks release.
9. No fabricated citations, studies, or further-reading entries — ever.
10. Nothing drafted before Phase 0 exits; chapters generated one at a time; each handoff ends "Type Proceed"; pen name carries no invented credentials.

**Deterministic checks** for the computable rules (chapter/manuscript word budgets, subtitle char
limit, six-stage completeness, visual-level band, field-guide entry completeness) are implemented in
`genie_popular_science.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
