# AIRF 2.0 Travel Edition — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full travel-guide niche skill (UTGF v3.0, Pegasus Press Edition).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

Governing order within a session: operator's current title-specific instruction > this skill >
UTGF v3.0 > companion master prompt > any older reference.

## Reasoning sections that govern generation (see SKILL.md)
- **Expert Panel** — Destination Travel Specialist (Domain Master), Travel Content Strategist,
  Print Layout & Typography Director, Legal/Compliance & Accuracy Officer, Image & Map Production
  Lead (SKILL.md "Expert Panel").
- **Phase 0 — Title Analysis** — Steps 1-8 (title lock, trademark, competitor benchmark, edition
  year, author identity, subtitle, auto-configuration, gate pause) (SKILL.md "Phase 0").
- **Book Architecture** — trim/canvas, deployment-aware page budget, column layout, eleven-point
  venue entry template, section dividers, 12 required chapter functions, front matter (SKILL.md
  "Book Architecture").
- **Interior Design** — Times New Roman hierarchy, two-accent color application, table standard,
  page numbering/section control (SKILL.md "Interior Design").
- **Content Rules** — volatile-fact dating, content restriction, entry containment, image rules,
  multi-map program + locked map style, QR rules, legal safeguards, appendix selection (SKILL.md
  "Content Rules").
- **KDP Positioning** — category tree, description strategy, metadata signals (SKILL.md "KDP
  Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Title fidelity is absolute (locked at Phase 0; only operator changes it).
2. Page budget is deployment-aware (studio-owner hard cap 100, never relaxed).
3. Two entries per page double-column layout; entry containment; 80-90% fill.
4. Every volatile fact carries an "as of [season year]" band; never invented.
5. The edition-year marker is mandatory.
6. Content restrictions are zero-tolerance (no alcohol, no pork imagery, in any form).
7. All maps are newly generated originals (gpt-image-2); never taken from third parties.
8. All QR codes tested from the final PDF.
9. Chapter openers are compulsory full-bleed originals; never reused.
10. The TOC is a live Word References automatic field.
11. Section-divider pages with full-width destination photographs are required.
12. No em dashes anywhere in book content.
13. Catalog uniqueness is enforced (unique cover, palette, opener, organization, fingerprint).
14. Production gates are hard stops; end with "Type Proceed."
15. Rolling master DOCX — never disconnected files.

**Deterministic checks** for the computable rules (competitor mean/median, target-page
recommendation, page budget + reserve, minimum map count, 12-function coverage) are implemented in
`genie_travel.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
