# AIRF 2.0 Textbook Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Academic & Professional Textbook niche skill (OV-TEXT, source framework
   UTF 1.0; also the default template for any title with no dedicated overlay).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master, Subdiscipline/Applied-Practice Specialist, Curriculum &
  Learning-Design Specialist, Visual & Information-Design Director, Accuracy/Evidence/Safety/QA
  Specialist (SKILL.md "Expert Panel"). Voice is singular; no credential attributed to the pen name.
- **Discipline Adaptation Engine** — nine configured domains (Medical, STEM, Business, Humanities,
  Law, Engineering, Education, Arts, Trade/Vocational), each with panel emphasis, evidence standard,
  and risk regime; Engineering Domain Directive overrides defaults (SKILL.md "Discipline Adaptation
  Engine" + "Engineering Domain Directive").
- **Phase 0** — Title Clearance Gate, subject/domain detection, subtitle generation, auto-config,
  TOC lock & gate (SKILL.md "Phase 0 — Title Analysis").
- **Chapter Formula** — opener → Learning Objectives box → 3-5 numbered sections → feature boxes →
  visuals at fixed points → assessment block → chapter close (SKILL.md "Book Architecture").
- **Front/Back Matter** — ordered structure, disclaimer core, answer key, glossary, references,
  index, About the Author (SKILL.md "Front Matter" / "Back Matter").
- **Interior Design** — trim, margins, Times New Roman, two-color scheme, Learning Objectives box,
  tables, figures, image prompts, page numbering, print prep (SKILL.md "Interior Design").
- **Content Rules** — zero fabricated citations, transformation law, quantitative verification,
  standards dating, domain risk regimes, calibrated language, accessibility (SKILL.md "Content Rules").
- **KDP positioning** — category tree, description lead, metadata signals (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Title Clearance Gate runs first, always.
2. Discipline Adaptation Engine is mandatory (detect, configure panel + risk regime, state it).
3. Engineering domain: NO practice questions; deeper exposition; min 23 pp/chapter; 400-550 total; image per subchapter.
4. Never fabricate a citation, source, credential, or quotation.
5. Interior is locked (8.5x11, 0.7in margins, Times New Roman, justified, two-color, unique primary+accent pairing).
6. Learning objectives are Bloom-aligned, measurable, and assessment-traced ("understand"/"know" banned).
7. Where assessment exists, back matter carries a complete worked answer key plus a glossary.
8. Transformation law (concepts transfer; words, examples, problems, cases, figures, structure do not).
9. Every planned visual lands at its exact teaching point.
10. All quantitative content independently verified (recalculated math, tested code, checked units, dated standards).
11. Pen name is First M. Last, fictional, honorific-free, never reused; bio never claims credentials.
12. Structural and visual signatures rotate across the catalog.
13. No em dashes; no bullet lists in narrative; justified body; language lock; operator output in English.
14. As the default template, map any unclassified title to the nearest of the nine domains and inherit its regime.

**Deterministic checks** for the computable rules (domain validity, subtitle length, per-chapter and
total page bands, objective/section/feature-box counts, visual-level bucket, word-count ranges,
answer-key coverage, engineering image points) are implemented in `genie_textbook.py`; validation
gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
