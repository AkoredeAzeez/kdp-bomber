# AIRF 2.0 Humor Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey. Where this
projection and `SKILL.md` ever disagree, **`SKILL.md` wins**.

## Load, in order
1. `../../SKILL.md` — full Humor & Comedy / Gift Books niche skill (OV-HUMOR).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert Panel** — Humor Domain Master, Cultural-Calibration Specialist, Sensitivity Reader,
  Interior Design Auditor, KDP Metadata Strategist (SKILL.md "Expert Panel").
- **Phase 0 matrix & rubric** — AUD-OCC-PAIN slot, title/subtitle formulas, five-criteria scoring
  (SKILL.md "Phase 0 — Title Analysis").
- **Chapter beat blueprint** — opener, quote page, hook, escalation, list device, honest turn,
  warm closing beat, optional value element (SKILL.md "Book Architecture").
- **Humor registers** — five registers, one per book, locked at Phase 1 (SKILL.md "Content Rules").
- **Joke-type diversity & segment guardrails** — per-chapter quotas; audience-specific guardrails.
- **Interior design** — locked Playfair Display / Lato pair, black-and-white line art only, image
  placement quotas, image-prompt grammar (SKILL.md "Interior Design").
- **KDP positioning** — category tree, description formula, keyword pools (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Content restrictions, no exceptions (no alcohol, pork, gambling-positive; comfort props tea/coffee/chocolate).
2. Anti-advice voice doctrine (no programs, validate then permit rest; never instructs).
3. One humor register per book, locked at Phase 1; no tonal drift.
4. Joke-type diversity quotas; no device repeats within a chapter.
5. Humor punches at situations and systems, never at people or groups.
6. Cultural-calibration; jokes re-created for non-EN markets, never literally translated.
7. No real private individuals.
8. Fake attribution format is exact (Name Initial., age, absurd chapter-related job title).
9. Quote-page job titles never repeat across the catalog within a language.
10. Trim 6x9 in; extent 80-120 pages hard cap.
11. Typography pair locked (Playfair Display + Lato); named styles only.
12. Interior black and white only; cover is the only color surface.
13. Image constraints clause mandatory on every image prompt.
14. Em dashes banned catalogue-wide.
15. Gate discipline is blocking ("Type Proceed." ends every phase and chapter).
16. Rolling manuscript only (one growing DOCX).
17. Front matter order locked; folios start at the Introduction as printed page 1.
18. No selling points on covers; title and subtitle only on the front.
19. Mascots must vary across the catalog.
20. State discipline (never claim an external operation occurred unless it did).
21. Uniqueness (no shared title/subtitle; no two covers alike; job titles unique per language).
22. Originality attestation (each book written fresh; reference class is style source only).

**Deterministic checks** for the computable rules (rubric scoring, title/subtitle char limit,
keyword char limits, chapter count, page band, value-element budget, per-chapter image quotas,
word-count bands) are implemented in `genie_humor.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
