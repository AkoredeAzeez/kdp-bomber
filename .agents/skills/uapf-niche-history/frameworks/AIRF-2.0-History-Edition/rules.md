# AIRF 2.0 History Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey. Where this
projection and `SKILL.md` ever disagree, **`SKILL.md` wins**.

## Load, in order
1. `../../SKILL.md` — full History & Politics niche skill (OV-HIST).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert Panel** — Domain Master (Period & Regional Historian), Historiographer, Regional &
  Cultural Perspective Specialist, Narrative & Developmental Editor, and Quotation Authentication
  Specialist (activated when quotations appear) (SKILL.md "Expert Panel").
- **Phase 0 intake** — title/trademark screen, 13-code sub-niche matrix, subtitle generation,
  auto-configuration, Intake Report (SKILL.md "Phase 0 — Title Analysis").
- **Chapter architectures** — A chronological, B thematic, C biographical; structural units per
  chapter (hook, context block, core, primary-source integration, interpretive commentary, bridge)
  (SKILL.md "Book Architecture").
- **Content protocols** — Foundational Obligation, Contested Event Protocol, Quotation
  Authentication, Chronology Audit, Presentism Guard, Audience Calibration (SKILL.md "Content Rules").
- **Interior design** — trim options, serif typography, block-quote and note formatting, maps and
  timelines, sidebars (SKILL.md "Interior Design").
- **KDP positioning** — category strategy by sub-niche, above/below-the-fold description, backend
  keywords (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Factual claims require a citable basis.
2. Contested events must be presented WITH their contested status.
3. Quotation authentication is mandatory.
4. The chronology audit is not optional.
5. Presentism must be guarded, not eliminated.
6. All four expert-panel roles must complete review before Gate 3 closes (plus quotation specialist when MEDIUM/HIGH).
7. Architecture is locked at Phase 0 and does not change mid-manuscript.
8. Bibliography is mandatory (>= 15 sources under 200 pages; proportionally more; primary listed separately).
9. Do not use secondary-source summaries as if they were primary-source access.
10. No hagiography in biographical history.
11. Regional and subaltern perspectives are structural obligations, not optional additions.
12. HIST-ORL requires additional ethics review (consent, attribution, community ownership).

**Deterministic checks** for the computable rules (quotation-volume class, bibliography minimum,
glossary trigger, chapter-count bounds per architecture, page/word bands, keyword char limits) are
implemented in `genie_history.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
