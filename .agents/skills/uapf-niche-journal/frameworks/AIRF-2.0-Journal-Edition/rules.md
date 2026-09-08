# AIRF 2.0 Journal Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Low-Content & Guided Journals niche skill (OV-LOWC).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Low-Content Publishing Master, Subject-Matter Practitioner, Interior Layout
  Designer, KDP Metadata & Category Strategist, Clinical/Sensitivity Reviewer (Tier 3 R2+)
  (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — trademark/risk screen, language lock, Tier classification, subject
  analysis, risk-regime assignment, dated/undated, subtitle engine, auto-configuration
  (SKILL.md "Phase 0 — Title Analysis").
- **Page System spec** — repeating unit(s), repetition count with arithmetic, special pages; the
  chapter is replaced by the page system (SKILL.md "Book Architecture").
- **Field-label reality test / spread logic / page-count bands** (SKILL.md "Book Architecture").
- **Interior design** — trim by context, margins/gutter, typography tiers, true typeset rules,
  black-ink default, native Word tables (SKILL.md "Interior Design").
- **KDP positioning** — function-first category tree, title-position formula, description lead,
  backend keywords, pricing posture (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles; full text in SKILL.md "Key Rules — Do NOT Break")
1. The page system replaces the chapter.
2. The unit is the product (absolute unit fidelity).
3. Field labels must survive the practitioner test.
4. Undated by default (dated only on explicit operator declaration).
5. Tier 3 prompts obey the subject overlay's risk regime; no treat/cure/diagnose claims.
6. The 7-entry walkthrough audit is mandatory at Gate 3.
7. Spread logic is locked book-wide.
8. Risk regimes: R0 for Tiers 1-2 (strengthened for medical logs); R1-R4 by subject for Tier 3.
9. The KDP title position carries function + audience + format.
10. True typeset rules only (no underscores or dot-runs).
11. Catalogue hard rules bind fully (content restrictions, em-dash ban, fakenamegenerator author
    names, catalogue-wide visual uniqueness).
12. Every gate ends with Type Proceed.

**Deterministic checks** for the computable rules (subtitle char limits, page-total arithmetic vs
tier band, line-spacing writability, spread/verso-recto parity) are implemented in
`genie_journal.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
