# CBF 2.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md` and the
global rules; this file indexes them so an agent knows exactly what to load and obey.

## Load, in order
1. `../../SKILL.md` — full children's-book niche skill (CBF 2.0 / OV-CHILD).
2. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Children's Publishing Director, Child Development & Literacy Specialist,
  Children's Book Art Director, Print Production Manager (KDP), Gatekeeper Advocate (SKILL.md
  "Expert Panel").
- **Phase 0 age-band lock** — Hands → Intent → Reading mode → Band lock; one band, one host
  profile; second lock where required (SKILL.md "Phase 0 — Title Analysis").
- **Book Architecture** — page/spread is the structural unit; page-band targets; narrative rhythm;
  Page-Turn Law; front/back matter; 10-page concept sample (SKILL.md "Book Architecture").
- **Interior Design** — trim & bleed geometry; color-has-a-job; typography floors and roles; layer
  stack; illustration system (model sheet + style bible) (SKILL.md "Interior Design").
- **KDP positioning** — category tree + age/grade fields, gatekeeper-first description, metadata
  signals, series-ready titling (SKILL.md "KDP Positioning").

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Age band drives EVERYTHING.
2. Picture-band books: 8.5 x 8.5 trim, full color, full bleed, illustration-led, large display type, body LEFT-ALIGNED.
3. Type floors are floors.
4. Text Supremacy.
5. Child-appropriateness battery is always on.
6. The gatekeeper is the buyer.
7. Diversity and representation without tokenism.
8. Read-aloud cadence tested for pre-reader bands.
9. Pattern, not product.
10. Bleed is geometry and correction propagates.

(Content-rule hard constraints 1-10 in SKILL.md "Content Rules" — Audience Supremacy,
Child-appropriateness battery, Diversity/representation, Read-aloud cadence, Decodability,
Original Transformation, Text Supremacy, White-Space Law, Continuity, State honesty — are also
binding.)

**Deterministic checks** for the computable rules (bleed page size, page parity + KDP minimum,
color-class threshold, band type-floor lookup, guest-insert cap) are implemented in
`genie_childrens.py`; validation gates in `validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
