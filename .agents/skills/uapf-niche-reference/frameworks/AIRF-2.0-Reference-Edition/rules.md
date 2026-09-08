# AIRF 2.0 Reference Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Adult Reference & Trivia (OV-REF) niche skill.
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (lead), Trivia/Quiz Mechanics Specialist, Reference & Information
  Architecture Specialist, Adult Nonfiction Copy Editor, KDP Metadata & Positioning Strategist
  (SKILL.md "Expert Panel").
- **Phase 0 title analysis** — sub-type classification, count-claim audit, superlative inventory,
  audience/depth calibration, domain verification scope, auto-configuration, Book Lock
  (SKILL.md "Phase 0 — Title Analysis").
- **Entry-unit architecture per sub-type** — Fact-Cluster Unit (REF-FACT), Question-Answer Pair +
  round architecture (REF-TRIVIA), Ranked Entry + stated criteria (REF-LIST), Lookup Entry +
  lookup-first organization (REF-REF) (SKILL.md "Book Architecture").
- **Interior design** — trim/geometry, three font roles, type floors, alignment, color scheme
  (SKILL.md "Interior Design").
- **The fatal flaw** — a verification machine in entertainment clothing; certainty beats polish
  (SKILL.md "Content Rules — The Fatal Flaw").
- **KDP positioning** — category tree, description strategy, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Every entry dual-source verified before Gate 2.
2. Volatile superlatives dated inline in the body text.
3. The count claim in the title is a contractual promise.
4. No padding.
5. REF-FACT: the WHY note is not optional.
6. REF-TRIVIA: every question passes the single-answer defensibility rule.
7. REF-TRIVIA: answers are physically separated from questions.
8. REF-LIST: ranking criteria are stated before the list begins.
9. REF-LIST: entry length must be consistent.
10. REF-REF: organization serves the user who is looking something up.
11. The duplicate-entry scan is required at Gate 2 and must clear before Gate 3.
12. Adult depth is not optional in REF-FACT.
13. State Honesty rule.
14. Correction propagation applies fully.
15. Never route adult trivia or reference content to children's categories.

**Deterministic checks** for the computable rules (count-claim achievability, page-count/even,
round architecture, entry-length consistency) are implemented in `genie_reference.py`; validation
gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
