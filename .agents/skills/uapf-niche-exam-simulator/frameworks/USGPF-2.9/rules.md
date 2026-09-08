# USGPF 2.9 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full exam-simulator / question-bank niche skill (OV-EXSIM).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (SME/Certified Practitioner, listed first), Exam Analyst
  (Psychometrician), Instructional Designer, Compliance and Rights Editor, Technical Production
  Editor (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — ordered configuration; the total question count is the single
  operator-supplied setting; Exam Format Research blocks generation (SKILL.md "Phase 0").
- **Book Architecture** — brief front matter; body is the PRACTICE QUESTIONS division only (no
  instructional chapters); timed simulation sets; back matter (Answers, Score Interpretation Guide,
  Appendix A blueprint, Appendix B time budget); locked manuscript sequence (SKILL.md "Book Architecture").
- **Interior Design** — trim/margins, body type, color, two-column geometry, tables, folio
  (SKILL.md "Interior Design"). Projected in `config.json`.
- **Content Rules** — item originality, single defensible answer, distractor/rationale
  completeness, no pass-probability, timed-simulation fidelity, exhibit minimalism, score-guide
  architecture (SKILL.md "Content Rules").
- **KDP Positioning** — category tree, description lead, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. No verbatim secured exam content.
2. Every item carries one single defensible correct answer.
3. Every rationale addresses every distractor.
4. No pass-probability claims anywhere.
5. Exam Format Research runs before the first item is written.
6. No invented statistics, regulations, thresholds, or citations.
7. Continuous numbering across the full bank.
8. Two-column layout is mandatory for both divisions.
9. Non-affiliation statement is mandatory on the Copyright page.
10. The Two Option Law holds (two-option cap ≥2, default 3).
11. Exhibit minimalism (default zero; declared and justified).
12. The Answer Pattern Audit runs against the actual built file (UNVERIFIED blocks as FAIL).

**Deterministic checks** for the computable rules (assessment split, key-quota balance, run-cap
resolution, pattern guards, numbering integrity, explanation word cap, subtitle validity,
time-per-question budget, section-length band) are implemented in `genie_exam_simulator.py`;
validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
