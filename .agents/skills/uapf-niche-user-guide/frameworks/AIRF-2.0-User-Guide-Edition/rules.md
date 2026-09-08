# AIRF 2.0 User Guide Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full user-guide niche skill (OV-GUIDE).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning sections that govern generation (see SKILL.md)
- **Expert Panel** — Technical Communication & Documentation Authority (Domain Master),
  Instructional Design & Skills Transfer Authority, UI/UX & Product Analysis Specialist, Safety &
  Compliance Reviewer, Localization & Accessibility Authority. Panel Consensus Rule: Tech-Comm +
  UI/UX must jointly confirm terminology parity before Gate 3 (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — Steps 0-A trademark, 0-B product & version identification, 0-C
  product architecture, 0-D task analysis & chapter scope, 0-E audience, 0-F competitor, 0-G
  subtitle, 0-H auto-configuration (SKILL.md "Phase 0").
- **Book Architecture** — task-oriented architecture, chapter formula, procedure architecture,
  screenshot/diagram requirements, warning hierarchy, page-band targets, chapter sequence, front &
  back matter (SKILL.md "Book Architecture").
- **Interior Design** — trim/margins, Times New Roman hierarchy, procedure/step styling, UI-name
  bolding, keyboard-shortcut notation, warning/version/notice boxes, screenshot frames, Design
  Signature (SKILL.md "Interior Design").
- **Content Rules** — the Fatal Flaw (terminology mismatch + version drift) and the 12 Hard
  Constraints (SKILL.md "Content Rules").
- **KDP Positioning** — category tree by product type, description formula, metadata signals with
  mandatory version keyword (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Covered product version named on cover, Introduction first paragraph, and KDP metadata.
2. Terminology parity is absolute (every UI name matches the product exactly; no synonyms).
3. Task-oriented chapter organization is mandatory (never feature-organized).
4. One action per step; steps begin with an action verb.
5. All UI element names in steps appear in bold.
6. Warning hierarchy (DANGER/WARNING/CAUTION/NOTICE/VERSION NOTE) is the only advisory format.
7. Version Notes are mandatory at every step that differs from the prior major version.
8. The Copyright Page disclaimer is non-negotiable (version+date, no-affiliation, trademark ack,
   variance notice).
9. Screenshots must be current to the covered version.
10. Troubleshooting covers the top 10 documented user problems (researched, not generic).
11. The Interface Element Naming Index in the appendix is mandatory.
12. The anti-AI language protocol is non-negotiable (technical communication register throughout).

**Deterministic checks** for the computable rules (page-band / chapter-count classification and
validation, warning-level validity, front-matter order, appendix element count, troubleshooting
count) are implemented in `genie_user_guide.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
