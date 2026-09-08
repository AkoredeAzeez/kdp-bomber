# AIRF 2.0 Workbook Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey. Where this
projection and `SKILL.md` disagree, `SKILL.md` wins.

## Load, in order
1. `../../SKILL.md` — full OV-WORK niche skill (derived from UWGF v1.7).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning sections that govern generation (see SKILL.md)
- **Expert Panel** — Domain Master; Instructional Designer; Assessment & Answer-Key Auditor; Print
  Layout Engineer; KDP Compliance Officer (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — trademark/risk screen, language lock, niche analysis, subtitle
  engine, auto-configuration, page-budget validation, specification gate (SKILL.md "Phase 0").
- **Book Architecture** — the Practice Unit (10-page fixed formula), three difficulty bands,
  70-80% worksheet share, six-type exercise library, response-space sizing, question/answer
  integrity, labelled images, front matter, Introduction, Conclusion, back matter, page bands.
- **Interior Design** — trim/margins, typography, B&W-safe table law, grayscale visual identity,
  difficulty-band markers.
- **Content Rules** — the answer-key fatal flaw, key/exercise parity, text cap, difficulty honesty,
  niche adaptation profiles, catalogue hard rules, delivery/gating.
- **KDP Positioning** — category tree, description structure, backend keywords, metadata signals.

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. 10 pages per chapter, exactly. Cut text, never exercises, to hit it.
2. Three difficulty bands in every unit (Foundation, Development, Mastery), printed and ramped.
3. Complete answer key with worked solutions is mandatory; an incomplete key is a release block.
4. B&W-safe tables only: white cells, black half-point borders, header shading <=15% gray, no
   color fills, all table text left-aligned, native Word objects only.
5. Body text fully justified; lists left-aligned; Times New Roman; no em dashes anywhere.
6. 8.5 x 11 primary trim, 0.7-inch margins, 150-page hard cap validated before the TOC.
7. 70-80% worksheets in every chapter; explanatory text capped at 0.5 pages per section; at least
   three exercise types per unit.
8. Trademark-screen the title before anything else; never use protected exam/certification/curriculum
   brand names.
9. Gate everything: one phase per message, rolling DOCX re-delivered, every gated message ends with
   the exact line "Type Proceed", no advancement without it.
10. Catalogue hard rules bind: absolute content restrictions with compliant substitutions, per-title
    grayscale-safe visual uniqueness, pen name from fakenamegenerator.com in First Name, Initials.
    Surname format, and title-language manuscript with English operator output.

**Deterministic checks** for the computable rules (10-page unit, band count, worksheet share,
exercise-type count, page budget/max chapters, unit-component page sums, subtitle length, copyright
component words) are implemented in `genie_workbook.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
