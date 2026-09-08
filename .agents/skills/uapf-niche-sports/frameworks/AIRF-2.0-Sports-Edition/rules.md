# AIRF 2.0 Sports Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full Sports & Outdoors niche skill (OV-SPORT).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (per sub-niche credential baseline), Sports Medicine & Injury
  Prevention Authority, Youth Coaching & Pedagogy Specialist, Outdoor Safety & Field Operations
  Authority, Regulatory & Licensed-Activity Compliance Officer (SKILL.md "Expert Panel").
- **Phase 0 title analysis** — Steps 0.1-0.8: sub-niche routing, trademark screen, special title
  checks, competitor page-count decision, audience profiling (S1-S6), pen name, Pre-TOC Report
  (SKILL.md "Phase 0 — Title Analysis").
- **Skill-Progression Architecture** — four stages per skill family (SKILL.md "Chapter Formula").
- **Coaching Session-Plan Module** — session template + age-band progression tables (SKILL.md
  "Additional Module: Coaching Session-Plan").
- **PREPARATION SPINE** — gear, conditions, navigation, leave-no-trace (SKILL.md "Additional
  Module: PREPARATION SPINE").
- **FIELD-SAFETY BATTERY** — life-safety cluster, named authorities, high-stakes disclaimer
  (SKILL.md "Additional Module: FIELD-SAFETY BATTERY").
- **Regulatory Dating / MKT Modifier** — jurisdiction + date labels, verification CTA (SKILL.md
  "Regulatory Dating and MKT Modifier").
- **OV-HEALTH R2 inheritance** — training-program contraindication/progression protocol (SKILL.md
  "OV-HEALTH R2 Inheritance").
- **Interior design & typography** — 8.5x11, segment-driven body type, palette + fingerprint
  (SKILL.md "Interior Design").
- **KDP positioning** — category tree, description strategy, metadata signals (SKILL.md "KDP
  Positioning").

## Hard rules — Do NOT break (titles; full text in SKILL.md "Key Rules — Do NOT Break")
1. SR2: every skill family completes all four Skill-Progression stages; a missing stage is a Gate 3 HOLD.
2. Drill standards measurable at three levels (beginner/intermediate/advanced).
3. PREPARATION SPINE precedes all technique content in outdoor/fishing/hunting/survival titles; never an appendix.
4. FIELD-SAFETY BATTERY mandatory for survival/bushcraft/hunting; named authority sourcing; no bravado; high-stakes disclaimer throughout.
5. MKT modifier on all hunting/fishing regulatory content: jurisdiction + date + verification CTA; unverifiable content is a Gate 4 HOLD.
6. OV-HEALTH R2 applies without modification to all training programs.
7. Gear recommendations brand-generic throughout; certification standards may be named, manufacturers may not.
8. Youth content meets USOC Safe Sport standards.
9. Performance-outcome claims are qualified.
10. Exact user-supplied title preserved at every stage.
11. Coaching Session-Plan Module + age-band tables mandatory in every coaching skill-family chapter.
12. No fabricated endorsements, governing-body approvals, or tour/association affiliations.
13. PREPARATION SPINE navigation section must include the bailout-route identification requirement.
14. Stage-4 fault catalog names faults as observable symptoms, not jargon labels.
15. Manuscript not marked print-ready until all four gates pass on evidence.

**Deterministic checks** for the computable rules (session-plan block minutes and 100% sum,
skill-progression stage/level/fault counts, 10% weekly mileage ceiling, segment-driven body point
size, sub-niche page-band membership, Pre-TOC 19-item count) are implemented in `genie_sports.py`;
validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
