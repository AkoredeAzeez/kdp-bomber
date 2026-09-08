# AIRF 2.0 Public Domain Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full public-domain niche skill (OV-PD).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Scholarly Editor, Publishing-Rights Analyst (absolute stop authority),
  Literary Historian, Pedagogy & Reader-Experience Specialist, KDP Differentiation & Compliance
  Auditor (SKILL.md "Expert Panel").
- **7-Point Legal Verification Checklist** — the hard gate that runs before all other work; each
  point researched with live sources and recorded with evidence (SKILL.md "0.1").
- **Title clearance & format law** — differentiator required in title/subtitle per KDP PD policy
  (SKILL.md "0.2").
- **Auto-configuration** — edition type; value-add layer; audience; pen-name editor framing;
  Book Identity Code (SKILL.md "0.4").
- **Book Architecture** — apparatus unit as structural unit; standard vs study-guide vs bilingual
  variants; page bands (SKILL.md "Book Architecture").
- **Interior Design** — trade-classic feel distinct from Penguin/Oxford/Norton trade dress;
  footnote/endnote system; bilingual facing pages (SKILL.md "Interior Design").
- **Content Rules** — value-add originality; modern-copyright quarantine; text fidelity; factual
  integrity; attribution; PD-transcription provenance (SKILL.md "Content Rules").
- **KDP positioning** — category tree, value-add-led description, differentiator keywords
  (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. The 7-Point Legal Verification Checklist runs BEFORE any other work; failure at ANY point stops the project.
2. A modern translation is never treated as PD because the underlying work is PD.
3. Modern-copyright elements from other editions are NEVER reproduced or adapted, in whole or in part.
4. The value-add layer must be substantial and original; a thin wrapper is release-blocking.
5. The full legal re-verification re-runs at manuscript completion (Gate 3) before handoff.
6. The differentiation statement is written out explicitly at Gate 4 and mirrored in title/subtitle/description.
7. The classic text is never silently altered; modernization policy stated in the Note on the Text.
8. Copyright is claimed only in the new material; original author always credited; editor carries no invented credentials.
9. Every fact, date, quotation, and reading recommendation is verified; fabricated citations are release-blocking.
10. Nothing drafted before Phase 0 exits; units generated one at a time into the single cumulative manuscript, each handoff ending with the standalone line: Type Proceed.

**Deterministic checks** for the computable rules (US rolling-cutoff term math, life+70 term
math, value-add differentiation floor) are implemented in `genie_public_domain.py`; validation
gates in `validation.json`. Term math is a *screening aid*, not legal advice — the analyst's
verified sources and stop authority remain authoritative.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
