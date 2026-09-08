# USGPF 2.9 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full study-guide / exam-prep niche skill (OV-STUDY; OV-KIDS sub-overlay).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master, Psychometrician / Item-Writing Specialist, Official-Syllabus
  Auditor, Exam-Prep Pedagogue, Regulatory & Marketplace Compliance Reviewer (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — the ordered configuration steps; the total question count is the
  single operator-supplied setting (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — locked manuscript sequence; exam-orientation Introduction first; chapter
  template; chapter-to-syllabus mapping; consolidated practice divisions; question/answer forms;
  front/back matter; TOC contract (SKILL.md "Book Architecture").
- **Interior Design** — trim/margins, body type, headings, color, boxes, tables, images, columns
  (SKILL.md "Interior Design"). Projected in `config.json`.
- **Content Rules** — the fatal flaw and the twelve mechanisms that kill it (SKILL.md "Content Rules").
- **KDP Positioning** — category tree, description lead, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Exam orientation first.
2. Chapters mirror the OFFICIAL syllabus.
3. Research before generation, always.
4. Every chapter ends in exam-style practice.
5. Answer explanations teach the WHY (≤50 words).
6. Syllabus-coverage audit is mandatory.
7. Item-format fidelity check at QA.
8. Marketplace-integrity modifier for region-locked exams.
9. Never reproduce or imitate real exam items.
10. Randomization discipline (engine, run caps, pattern guards, Two Option Law, recorded seed).
11. The title is verbatim; the count is the single setting.
12. Length bands are met in scope, never typography.
13. Truthful status and the Proceed gate.
14. No invented facts, no credentials, no scaffolding shipped.

**Deterministic checks** for the computable rules (assessment split, key-quota balance, run-cap
resolution, pattern guards, page-band and ceiling checks, subtitle validity, chapter floors,
explanation word cap) are implemented in `genie_study_guide.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
