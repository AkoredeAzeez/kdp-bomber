# AIRF 2.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Faith & Devotional niche skill (OV-FAITH).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Tradition Scholar (Domain Master), Scripture Copyright Specialist, Interfaith
  Sensitivity Reviewer, Trauma-Informed Pastoral Care Advisor, Publishing Rights and Permissions
  Auditor (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — tradition declaration (hard requirement), title clearance,
  day-count extraction, sub-genre classification, auto-configuration (SKILL.md "Phase 0").
- **Structural unit formulas** — Daily Devotional four-part sequence and the alternate formulas by
  sub-genre (SKILL.md "Book Architecture").
- **Scripture Copyright Protocol** — public-domain defaults, modern-translation limits and
  attribution, never silently switch (SKILL.md "Content Rules").
- **Tradition Fidelity / Theological Boundaries / R4 Grief Protocol** — doctrinal accuracy,
  interfaith respect, sacred-figure representation, no prosperity/healing/victim-blaming
  (SKILL.md "Content Rules").
- **KDP positioning** — tradition-specific category tree, description lead, metadata signals
  (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles; full text in SKILL.md "Key Rules — Do NOT Break")
1. Tradition declaration is mandatory before any generation begins.
2. A "90-Day Devotional" contains exactly 90 complete units (declared count is a hard contract).
3. Every devotional unit must have all four components in order (Scripture -> Reflection -> Prayer
   -> Application).
4. Default to public-domain scripture translations.
5. Every modern translation quotation carries the exact attribution line required by the rights
   holder.
6. No prosperity promises, no healing guarantees, no spiritual victim-blaming.
7. Doctrinal accuracy is non-negotiable.
8. No photorealistic depictions of sacred figures.
9. R4 grief protocol applies automatically for bereavement/suffering/spiritual-crisis topics.
10. Crisis and pastoral support resources must be verified live.
11. Interfaith respect is absolute.
12. No invented credentials, ministry history, church affiliations, or publications for the
    pseudonymous author.

**Deterministic checks** for the computable rules (declared-unit-count contract, part-partition
sum, reflection/prayer word bands, modern-translation verse limits, part-opener image count) are
implemented in `genie_faith.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
