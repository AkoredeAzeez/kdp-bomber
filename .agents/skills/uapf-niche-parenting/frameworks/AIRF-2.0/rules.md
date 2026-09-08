# AIRF 2.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full parenting / pregnancy / family niche skill (OV-PARENT).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Pediatric/Developmental Domain Master, Perinatal & Maternal Health
  Specialist, Child & Adolescent Psychologist, Reassurance-with-Honesty Editor, Family Systems &
  Relationship Therapist (SKILL.md "Expert Panel").
- **Phase 0 title analysis** — sub-genre classification, marketplace + Active Medical Authority
  lock, title clearance, age-range extraction, auto-configuration (SKILL.md "Phase 0").
- **Stage-based architecture** — per sub-genre chapter shapes (trimester / month band / age band /
  developmental theme / method domain) and separate baby-name entry format (SKILL.md "Book
  Architecture").
- **When to Call the Professional box** — structural requirement in every health-adjacent chapter
  (SKILL.md "'When to Call the Professional' Box").
- **Milestone range presentation** — mandatory range-with-threshold format (SKILL.md "Milestone
  Range Presentation").
- **Reassurance-with-honesty voice** — anxious reader; no false cheer, no alarm (SKILL.md "Content
  Rules").
- **Interior design & typography** — 6x9, TNR, box/callout treatments (SKILL.md "Interior Design").
- **KDP positioning** — category tree, description lead, metadata signals (SKILL.md "KDP
  Positioning").

## Hard rules — Do NOT break (titles; full text in SKILL.md "Key Rules — Do NOT Break")
1. Active Medical Authority declared in Phase 0 and held throughout; US/UK guidelines never mixed.
2. Every developmental milestone presented as a range with an upper consultation threshold.
3. "When to Call the Professional" boxes are structural, not optional.
4. Safe-sleep guidance reflects the current Active Medical Authority recommendation; verify live.
5. Immunization schedules not reproduced in full; direct to the live current resource.
6. Baby-name etymologies sourced or labeled uncertain; invented etymologies prohibited.
7. Reassurance-with-honesty voice mandatory; false cheer and unnecessary alarm both fail.
8. Neurodiversity acknowledged wherever development, behavior, or learning is discussed.
9. Postpartum depression/anxiety are medical conditions requiring clinical referral.
10. No legal advice about divorce, custody, or family law.
11. Crisis and support resources verified live; never carried static from other projects.
12. No invented credentials for the pseudonymous author.

**Deterministic checks** for the computable rules (When-to-Call box indicator count, image
chapter-opening image auto-rule at any page count, sub-genre page-band membership) are implemented in
`genie_parenting.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
