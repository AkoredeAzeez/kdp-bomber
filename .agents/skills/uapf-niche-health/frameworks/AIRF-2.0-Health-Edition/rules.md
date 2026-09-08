# AIRF 2.0 Health Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Health, Fitness & Wellness niche skill (OV-HEALTH).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Integrative Movement & Wellness Authority (lead), Clinical Exercise
  Physiologist, Sub-Niche Specialist, Adaptive & Accessibility Specialist, Evidence & Claims
  Auditor (SKILL.md "Expert Panel"). Most conservative credible position wins any safety conflict.
- **Phase 0 — Title Analysis** — exact-title lock, trademark/clearance screen, sub-niche detection
  (A-J), audience profiling, competitor research + page decision, compliant subtitle, pen name
  (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — structural spine; Chapter 1 medical-clearance; foundations; technique core;
  program; troubleshooting; conclusion; back matter (SKILL.md "Book Architecture").
- **The Technique Unit** — name → purpose → contraindications-before-instructions → setup →
  exact execution variables → universal modifications → common errors → step-by-step image sequence
  (SKILL.md "The Technique Unit").
- **Interior Design & Premium Design System** — trim, audience typography, safety callouts, styled
  openers, technique header bars, tinted panels, grayscale legibility (SKILL.md "Interior Design").
- **Content Rules & evidence hierarchy** — established/preliminary/traditional/consensus/uncertain
  labeling; no outcome claims (SKILL.md "Content Rules").
- **KDP positioning** — category tree, capability-language description, compliant metadata
  (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. R2 is mandatory and non-waivable.
2. Chapter 1 is the medical-clearance and safety chapter.
3. Contraindications before instructions in every single Technique Unit.
4. No weight-loss promises, no medical-outcome claims, no diagnosis, no prescription — anywhere.
5. Universal modifications (seated / standing-supported / adaptive) for every technique.
6. Evidence hierarchy transparent (established / preliminary / traditional / consensus / uncertain).
7. Most conservative credible interpretation wins every safety-critical source conflict.
8. Never invent credentials, expert review, clinical validation, or endorsements.
9. Exact title preserved; trademark screen before subtitle/TOC; protected program names never generic.
10. Exact prescription variables in every instruction, plus warning signs and stop-exercise rules.
11. Cultural respect is a quality gate (correct pinyin/Sanskrit with translation, no appropriation).
12. Images show safe, anatomically correct form only.
13. No two books alike (unique design fingerprint verified before formatting).
14. Senior-audience titles get 13-14 pt body text, 1.5 spacing, grayscale-legible callouts.
15. Every exercise gets a step-by-step image SEQUENCE (min 3 panels), never a single pose image.
16. Premium interior is mandatory.

**Deterministic checks** for the computable rules (competitor count, page-band membership, technique
panel minimum and book image count, audience typography) are implemented in `genie_health.py`;
validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
