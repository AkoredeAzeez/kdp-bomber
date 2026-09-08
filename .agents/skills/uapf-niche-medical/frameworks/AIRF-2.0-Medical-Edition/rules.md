# AIRF 2.0 Medical Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey. Where this
projection and `SKILL.md` disagree, `SKILL.md` wins.

## Load, in order
1. `../../SKILL.md` — full OV-MEDT niche skill (specializes OV-TEXT).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.
3. OV-TEXT base skill for any point not overridden here.

## Reasoning sections that govern generation (see SKILL.md)
- **Expert Panel** — Senior Clinical Educator; Biomedical Sciences Educator; Nursing & Allied
  Health Curriculum Specialist; Clinical Evidence & Patient Safety Specialist; Medical Learning
  Design Director (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — ten steps incl. title preservation, Eponym Audit, jurisdiction,
  trademark clearance, learner calibration, five-dimension auto-config, Book Identity Code + palette,
  subtitles, pen names, Type Proceed (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — trim/margins, page-band floors, page-to-word calibration, chapter
  formula, Medical Feature Box System, chapter distribution, front/back-matter sequences.
- **Interior Design** — OV-TEXT interior table, Learning Objectives Box calibration, figure
  placement under Hard Rule 22, formulary framing, DOCX automation.
- **Content Rules** — R2 dual-source verification, 100% accuracy floor, drug/pharmacology rules,
  eponym stripping, Medical Safe-Vocabulary Protocol, six-part image recipe, clinical case rules,
  language/voice, citation integrity, mandatory disclaimer, content standards, fatal flaw.
- **KDP Positioning** — category tree, description structure, metadata signals.

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Preserve the exact title verbatim in every location.
2. Complete the Eponym Audit in Phase 0 before the TOC is locked.
3. R2 mandatory — dual-source verification on all clinical claims.
4. NO practice questions, review questions, or graded assessment items anywhere, ever.
5. Minimum 23 pages per chapter; 400-550 pages total.
6. Hard Rule 22 — no diagrams, schematics, or flowcharts anywhere.
7. Per-subchapter photorealistic image — mandatory.
8. Medical Safe-Vocabulary Protocol applies to every image prompt without exception.
9. Generic drug names only, with pharmacological class in brackets at first use per chapter.
10. Dosing context carries the mandatory formulary verification sentence, in full, every time.
11. 100% accuracy floor on contraindications, red-flags, life-threatening interactions, criteria.
12. Never fabricate a citation or any clinical source identifier.
13. Mandatory full clinical disclaimer on the copyright page; condensed reminder where required.
14. No fabricated pen-name credentials anywhere.
15. TWO-COLOR scheme: catalog-unique PRIMARY + ACCENT, applied consistently.
16. No em dashes anywhere in the manuscript.
17. Content-standards compliance throughout.
18. Book Identity Code must include the `+OV-MEDT` suffix and be unique in the catalog.
19. Type Proceed is the only valid continuation language at every gate.
20. This skill specializes OV-TEXT; where they conflict, OV-MEDT governs.

**Deterministic checks** for the computable rules (subtitle length, page floors, chapter word
budget, objectives count, feature-box selection, image slots, label max) are implemented in
`genie_medical.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
