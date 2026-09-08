# AIRF 2.0 Biography Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Biography, Memoir & True Crime niche skill (OV-BIO).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules (#1–#16).

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Subject Researcher & Biographer (Domain Master), Legal & Privacy Counsel,
  Narrative & Developmental Editor, Fact-Checker & Source Authenticator, Dignity & Ethics Reviewer
  (SKILL.md "Expert Panel").
- **Phase 0** — title integrity, module/sub-niche classification, subject/case status, subtitle
  generation, auto-configuration and Intake Report (SKILL.md "Phase 0 — Title Analysis").
- **Architectures** — BIO-A/B/C, MEM-A/B, TC-A/B; the BIO-COL four-unit profile
  (Hook → Life → Contribution → Legacy) (SKILL.md "Book Architecture").
- **Interior design** — trim options, typography, plate/caption handling, dignified victim imagery
  (SKILL.md "Interior Design").
- **Content rules** — foundational obligation and Rules 1–9, the Dignity Battery, and the Fatal
  Flaws (SKILL.md "Content Rules").
- **KDP positioning** — category strategy, description framework, backend keywords (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. No invented dialogue in nonfiction.
2. Reconstructed scenes require labels.
3. Living persons require Legal & Privacy Counsel review on every chapter.
4. All seven Dignity Battery checks must pass for True Crime content.
5. Victims are human beings first, cases second.
6. Minors are never named without documented adult-waiver of anonymity.
7. OV-HIST quotation authentication rules are mandatory here.
8. Chronology audit is mandatory before Gate 3 closes on any chapter.
9. Collective biography profile count must match title count exactly.
10. Collective biography profiles must include all four structural units.
11. No hagiography. No hatchet job.
12. As-Told-To collaborators must be disclosed.
13. Source Ledger is a production document, not a reference (completed before Gate 3 closes).
14. Bibliography and notes are mandatory for biography and true crime (min 20 sources under 250 pages).
15. True Crime source integrity admits no prohibited sources.

**Deterministic checks** for the computable rules (quotation-volume bucketing, BIO-COL profile-count
match, four-unit completeness, ±10%/2x length consistency, per-unit word budgets, bibliography source
floor) are implemented in `genie_biography.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
