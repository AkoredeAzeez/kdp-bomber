# AIRF 2.0 How-To Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey. Where this
projection and `SKILL.md` ever disagree, **`SKILL.md` wins**.

## Load, in order
1. `../../SKILL.md` — full how-to niche skill (OV-HOWTO).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning sections that govern generation (see SKILL.md)
- **Expert Panel** — Master Instructional Design & Skills Transfer Authority (Domain Master),
  Construction & Home Systems Authority, Master Multi-Craft Educator, Environmental Science &
  Sustainable Living Expert, Safety & Compliance Reviewer; plus the Panel Consensus Rule
  (SKILL.md "Expert Panel").
- **Skill Domain classification** — ten domain codes drive panel, safety standards, and box types
  (SKILL.md "Phase 0", Step 0-B).
- **Outcome-ordered chapters & Three-Zone structure** — Zone 1 (Foundation & Quick Win),
  Zone 2 (Core Skill Expansion), Zone 3 (Mastery & Continuation) (SKILL.md "Book Architecture").
- **Chapter formula & Procedure Architecture** — numbered procedures, one action per step,
  Pre-Step Materials, Expected Result, failure-recovery guidance (SKILL.md "Procedure Architecture").
- **Decision Point Boxes / Failure-Recovery Boxes / Safety Callout Boxes / Chapter Checkpoints**
  (SKILL.md "Book Architecture", "Interior Design").
- **Content Rules** — the Fatal Flaw (procedures not executable as written), hard constraints,
  anti-AI language protocol.
- **KDP Positioning** — domain category tree, description formula, metadata signals.

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. A tangible skill win must be achievable by the end of Chapter 3.
2. Every procedure is executable as written by the declared reader.
3. Decision Point Boxes are mandatory at every procedural fork.
4. Failure-Recovery Boxes are mandatory after every procedure.
5. Safety callouts live inside the step where the hazard occurs.
6. Licensed-trade topics carry a jurisdiction disclaimer on the Copyright Page AND in every applicable chapter.
7. Every measurement is specific, in both metric and imperial.
8. Every technical term is defined at first use in the body text and in the Glossary appendix.
9. The outcome promise must be achievable by following the book.
10. Chapter Checkpoints are mandatory at the end of every chapter.
11. The anti-AI language protocol is non-negotiable.
12. The Design Signature must be logged before the TOC gate and must not repeat the last five register entries.

**Deterministic checks** for the computable rules — book-size classification, Quick-Win chapter
(min of Chapter 3 and ceil(20% of chapters)), Three-Zone boundaries, page-band membership, and the
seven-element appendix completeness — are implemented in `genie_howto.py`; validation gates in
`validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
