# CBF 2.0 — Reasoning / instruction rules (index)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These rules are NOT copied here (single source of truth). They live in `../../SKILL.md`, the parent
OV-CHILD skill, and the global rules; this file indexes them so an agent knows exactly what to load
and obey.

## Load, in order
1. `../../SKILL.md` — full children's-nonfiction-fact-book niche skill (CBF 2.0 / OV-CFACT).
2. `../../../uapf-niche-childrens/SKILL.md` — parent overlay OV-CHILD (inherited in full; where
   OV-CFACT tightens a rule, the tighter rule governs).
3. `../../../uapf-global-rules/SKILL.md` + `AGENTS.md` global hard rules.

## Authority order (SKILL.md header)
Child safety and law > Factual accuracy and dual-source verification > Locked age band and reading
mode > User's explicit brief > CBF 2.0 stable rules + OV-CFACT content rules > Live platform
requirements > Reference-derived patterns > Operator assumptions.

## Reasoning rules that govern generation (see SKILL.md sections)
- **Expert panel** — Nonfiction Editor/Fact Accuracy Director, Subject-Matter Expert, Nonfiction
  Art Director, Readability & Vocabulary Specialist, Child Safety/Accuracy/Diversity Reviewer.
- **Phase 0** — age-band + knowledge-depth lock; CB-FACT routing; fact-count claim audit;
  superlative inventory; Curiosity Map; auto-configuration; mandatory Book Lock block.
- **Book Architecture** — the Fact-Spread Unit (header, anchor, cluster, Wow Callout, Quick Quiz);
  section architecture; page-count targets; front/back matter; interior layout laws.
- **Interior Design** — trim geometry; three font roles + OV-CFACT type floors; 12-layer
  fact-spread template; full-color section accent coding; accessibility.
- **Content Rules** — dual-source verification protocol; superlative audit; Number Lock;
  age-banded vocabulary + on-page gloss; curiosity-logic sequencing; appropriateness extensions.
- **KDP Positioning** — nonfiction category tree, gatekeeper-first description, metadata signals.

## Hard rules — Do NOT break (titles only; full text in SKILL.md "Key Rules — Do NOT Break")
1. Every fact is dual-source verified before Gate 2.
2. Superlatives verified; volatile superlatives dated inline.
3. The title count claim is a contractual promise.
4. Fact-spread maximum is 8 facts.
5. Topic sequencing follows curiosity logic, not academic taxonomy.
6. On-page glosses appear on the same spread as the stretch word.
7. No Quick Quiz answers on a different page.
8. Full color is the only permitted mode.
9. Diagrams require real typeset labels only.
10. The Wow Callout is selected from the facts, not invented.
11. Abstract facts must be followed immediately by a concrete example.
12. The final spread is the best fact in the book.
13. All OV-CHILD non-negotiable rules apply.
14. Correction propagation applies to fact corrections.
15. State Honesty rule.

**Deterministic checks** for the computable rules (fact-count reconciliation, facts-per-spread cap,
sidebar ratio, page parity + KDP minimum, color-class threshold, bleed page size, type-floor
lookup, dual-source count) are implemented in `genie_childrens_facts.py`; validation gates in
`validation.json`.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
