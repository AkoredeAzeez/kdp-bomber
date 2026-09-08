# AIRF 2.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full poetry/affirmations/spoken-word niche skill (OV-POET).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Domain Master (Literary Poet & Craft Specialist), Originality Auditor,
  Cadence and Read-Aloud Editor, Emotional Arc Architect, Variety and Repetition Auditor
  (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — sub-genre classification; Emotional Arc Declaration (hard
  requirement); day-count extraction; form declaration; copyright/originality mode; auto-config
  (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — structural unit by sub-genre; section architecture mapped to the arc;
  variety quotas; page-band targets; front/back matter (SKILL.md "Book Architecture").
- **Interior Design** — 6x9 trim; typography per element; visual identity; white-space-as-design;
  word style map (SKILL.md "Interior Design").
- **Content Rules** — Absolute Originality Standard; Cliche Audit (Anti-AI Poetic Law); present-
  tense craft rules; repetition-with-variation; cadence/read-aloud; emotional-arc delivery; mental-
  health claim rules; the Fatal Flaw (365 entries = 12 recycled ideas) (SKILL.md "Content Rules").
- **KDP positioning** — poetry/self-help category trees, description lead, metadata signals
  (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (TITLES only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Emotional arc declaration is mandatory before any content is generated.
2. A "365 Daily Affirmations" book contains exactly 365 complete, distinct entries.
3. Absolute originality standard is non-negotiable.
4. The Cliche Audit is mandatory.
5. Variety quotas apply to all collections of 30 or more entries.
6. Present tense is mandatory for all affirmations.
7. All affirmations in first-person singular (unless second-person declared in Phase 0).
8. The cadence audit must sample at least 10% of entries from each section, read aloud.
9. No copyrighted poem or quote as an epigraph without confirmed rights and exact attribution.
10. No crisis-adjacent collection is complete without a disclaimer and verified crisis resources.
11. Images for poetry collections use abstract or painterly style, not literal illustration.
12. No invented publication history, literary awards, or MFA credentials for the pseudonym.

**Deterministic checks** for the computable rules (variety-quota lookup, 10% cadence sample size,
declared entry-count verification, day-number sequence, section count, poems-per-section, haiku
syllables) are implemented in `genie_poetry.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
