---
name: uapf-niche-popular-science
description: Popular science overlay (OV-POPSCI) — invoked by uapf-phase0-router when the title targets a general reader with a science or nature topic (space, brain, physics, wildlife, climate, evolution, everyday chemistry, how natural phenomena work).
---

# UAPF Niche: Popular Science (OV-POPSCI)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** the title targets a general reader with a science topic — space and astronomy, the brain and mind, physics "for everyone", nature and wildlife, climate and earth systems, biology, evolution, chemistry in everyday life, "how [natural phenomenon] works", "the science of [everyday thing]", or a field guide to a natural subject. Signals: wonder-framing ("secrets", "hidden", "amazing"), everyday-relevance framing, explicit general-audience markers ("for everyone", "for the curious", "a beginner's guide to the universe"), and the ABSENCE of textbook markers (no course alignment, no exam prep, no problem sets). Titles with curriculum/certification claims route to the textbook framework instead; field guides route here on the field-guide variant.

## Expert Panel

All perspectives operate silently; the reader sees one consistent authorial voice.

1. **Domain Master — Research Scientist in the Detected Field:** a working scientist (astrophysicist, neuroscientist, ecologist, chemist, etc. as the title requires); owns factual accuracy, consensus classification, and the honest state of the field.
2. **Science Communicator / Explainer Craftsman:** in the tradition of the best explainers; owns the hook-to-wonder chapter arc, analogy construction (and the mandatory acknowledgment of where each analogy breaks), and narrative momentum.
3. **Evidence Historian & Methods Specialist:** owns the "HOW we know" layer — the experiments, observations, instruments, and reasoning behind every major claim; turns evidence into story without distorting it.
4. **Quantitative Fidelity Editor:** owns every number — humanizes scale comparisons while keeping the exact figure underneath; checks units, orders of magnitude, and rounding for truth-loss; verifies conversions.
5. **Nature & Taxonomy Verifier (activated for nature/wildlife/field-guide titles):** verifies species names, taxonomy, ranges, seasons, and conservation status against current authorities as of the production date.

## Phase 0 — Title Analysis

Run in order. Nothing is drafted until Phase 0 exits and the operator has typed Proceed.

**0.1 Title Clearance Gate (mandatory, first):**
- Language detection and lock per UAPF default (interface English; manuscript in the locked book language; English defaults to American English for Amazon.com).
- Live title collision search: search the target marketplace and open web for the exact title and dominant phrase; popular-science shelves recycle title patterns ("The Hidden Life of...", "A Brief History of...") — an exact collision with a bestseller is HIGH RISK for confusion even though descriptive.
- Live trademark search (WIPO baseline; USPTO/EUIPO as marketplace requires; Nice Classes 16, 9, 41): screen for TV/documentary franchise names, museum and institution brands, and famous-science-brand echoes; no implied affiliation with NASA, BBC, National Geographic, or any institution.
- Output the Title Clearance Report (Exact Title | Language | Confidence | Marketplace | Collision Result | Registers/Classes | Risk Rating | Good-to-Go | Required Revision). Only CLEAR or explained low-confusion CAUTION proceeds; HIGH RISK stops and triggers 6–10 cleared alternatives.

**0.2 Subject analysis:**
- Identify the field and subfield (astronomy/cosmology, neuroscience, particle physics, ecology, ornithology, climate science, evolutionary biology, chemistry...).
- **Central question inventory:** list the 10–20 genuine reader questions the title promises to answer ("Why is the sky dark at night?", "How does anesthesia work?"). These questions, not topics, will seed the chapter hooks.
- **Consensus map (drafted now, maintained throughout):** classify the territory the book will cover into three bands — ESTABLISHED (textbook-solid consensus), FRONTIER (active research, provisional findings), CONTESTED (genuine scientific disagreement, with the actual positions and their approximate standing in the field). Every major claim in the book will later carry one of these classifications.
- Audience calibration: curious general reader; assume zero prior coursework, full adult intelligence; no equations beyond the occasional celebrated one shown as an object of interest; all math carried by prose, analogy, and figures.
- Scope decision: broad-survey ("the universe") vs. deep-single-question ("why we sleep") vs. field-guide variant (see Book Architecture).

**0.3 Subtitle generation:** 6–8 KDP-compliant options in the book language (≤200 characters combined), each promising curiosity and comprehension honestly — no overclaims ("the definitive answer"), no mystical framing, no medical-benefit promises for brain/health-adjacent titles. Per option: character count, keywords, audience, category fit, market position, collision note, trademark status, compliance line. Recommend one in English with rationale.

**0.4 Auto-configuration:**
- **Structure model:** question-led chapters (default) | journey structure (scale ladder, timeline of the universe, a year in a landscape) | field-guide entry architecture (for identification titles).
- **Visual level:** MODERATE (15–25) or ABUNDANT (30–50) per the base framework's density rules; modality mix biased to explanatory diagrams, scale comparisons, and (for nature titles) accurate species illustration; exact data always built natively, never entrusted to image generation.
- Assessment architecture: none (popular science has no exercises); supplementary materials: glossary, further-reading list (real, verified titles only), and — for nature titles — seasonal/regional appendices.
- Pen name (3–5 candidates, First M. Last, science-writer tone, NO invented doctorates or institutional affiliations — the bio is a science writer, not a fabricated scientist) and Book Identity Code per the UAPF distinctiveness engine, collision-checked.

**0.5 TOC:** chapters mapped to the central-question inventory, each TOC entry annotated with its hook question, its consensus-band coverage, and its planned figure points (fixed now, per base-framework Module 3.6 discipline). Present the TOC, then end with the standalone line: Type Proceed.

**Phase 0 exit criteria:** title cleared; consensus map drafted; question inventory complete; structure model, visual level, pen name, and Book Identity Code locked; TOC presented; operator has typed Proceed.

## Book Architecture

**Structural unit: the explainer chapter**, built on the six-stage explainer architecture — every chapter runs the full sequence:

1. **Hook question:** open with the genuine question or arresting phenomenon the chapter answers — concrete, felt, and stated within the first page ("Every second, the Sun converts four million tons of matter into light. Where does it go?"). Never open with definitions or throat-clearing history.
2. **Intuition-building:** analogies and thought experiments that give the reader a working mental model BEFORE the mechanism. **Analogy law: every analogy must acknowledge where it breaks** — in the prose, at the point of use ("the rubber-sheet picture is useful, but unlike a sheet, spacetime isn't sitting inside a larger room it can sag into"). An analogy presented without its breaking point is a Gate 2 failure.
3. **Mechanism:** the actual how — accurate, stepwise, in plain language, using the intuition just built; technical terms introduced only when needed, defined on first use, and used consistently thereafter.
4. **Evidence story:** HOW we know, not just WHAT we know — the experiment, observation, instrument, or line of reasoning that established it, told as narrative (who wondered, what they did, what the data showed, what it ruled out). Every chapter carries at least one evidence story; a chapter of bare assertions fails the gate.
5. **Implications:** what it means — for the reader's daily life, for the field, for other chapters (cross-link), honestly bounded (no overreach from result to revolution).
6. **Wonder payoff:** close by widening the aperture — the open question, the scale shift, the "and this is happening right now above your head" turn. Earned wonder from the material itself, never mysticism pasted on.

**Chapter specs:** 3,500–5,500 words per chapter; 12–18 chapters; total 55,000–80,000 words. Chapters sequenced so mental models build (each chapter may assume only earlier chapters).

**Front matter:** title page; copyright page (copyright, AI-disclosure status, and a science-currency note: "The science in this book reflects published research and expert consensus as of [month year]"; for brain/health-adjacent topics add a not-medical-advice disclaimer per UAPF disclaimer law); brief introduction (the book's central promise and how to read it); TOC.

**Back matter:** glossary (every term the book defined); notes/further reading — real, verified sources only, organized by chapter (the no-fabricated-citations law applies absolutely: never invent a study, author, journal, year, or DOI; unverifiable support becomes "current consensus holds..." or a marked placeholder); index (print); About the Author (science-writer bio, zero invented credentials).

**FIELD-GUIDE VARIANT (identification titles — birds, trees, mushrooms, rocks, night sky...):**
- **Structural unit: the identification entry.** Fixed entry architecture, identical fields in identical order for every species/object: common name + scientific name (current taxonomy) | one-line diagnostic summary | **description** (size, shape, color, distinguishing marks, in field-observable order) | **habitat** | **season/timing** (occurrence, breeding, migration, fruiting, visibility as fits the subject) | **look-alikes** (each similar species named WITH the distinguishing feature that separates it) | notes (behavior, range, conservation status).
- Organization: taxonomic, seasonal, or visual-similarity grouping — locked at Phase 0; entries per page and figure treatment uniform throughout.
- Safety-critical guides (mushrooms/foraging): dangerous look-alikes are mandatory fields, warnings prominent, and the disclaimer explicitly bars eating anything on the book's authority alone.
- Front matter adds "How to Use This Guide" + anatomy/terminology primer; back matter adds checklist and seasonal/regional indexes.

## Interior Design

Inherits UAPF default, with pop-science overrides:
- Trim 5.5" x 8.5" or 6" x 9"; readable book serif at 11–11.5 pt, justified; generous leading — the page should feel like narrative, not reference.
- Figures per the base framework's visual pipeline: explanatory diagrams and scale comparisons favored; consistent Style Signature locked at the first figure; captions per UAPF caption law, referenced from prose by number; pure-white backgrounds for diagrams; charts built natively from verified data only.
- Occasional pull-quote or fact-box per the locked Book Identity feature system (renamed per-book, e.g., "Sense of Scale", "How We Found Out") — 3–5 devices maximum, used consistently.
- Field-guide variant: 5" x 8" or smaller portable trim permissible; entry layout grid locked and identical throughout; range/season indicators use colorblind-safe redundant encoding.

## Content Rules

**The fatal flaw to avoid: wonder purchased with inaccuracy.** The genre's besetting sin is the exciting sentence that is not quite true — the overclaimed study, the analogy taken literally, the frontier finding sold as settled fact, the number rounded into falsehood. Every rule below defends against it.

- **Consensus discipline (the load-bearing rule):** established science is stated confidently and plainly, with no false hedging. Frontier science is explicitly labeled as frontier ("a 2024 result, not yet replicated, suggests..."). Controversy is presented as the field actually holds it — the real positions, their actual standing, and what evidence would settle it — never as false balance between consensus and a fringe, and never flattened into fake certainty. Every major claim carries a consensus-band classification in the working notes.
- **Numbers humanized but EXACT underneath:** every quantity gets a graspable comparison AND keeps its true value on the page ("about 90 billion kilometers — roughly 600 times the Earth–Sun distance"). No rounding that loses truth: order-of-magnitude honesty is absolute; "millions" never stands in for billions; comparisons are themselves verified arithmetic (the Quantitative Fidelity Editor recomputes every one). Units correct and consistent; SI with familiar equivalents.
- **No mysticism dressed as science:** quantum mechanics licenses no claims about consciousness, healing, or manifestation; "energy", "frequency", and "vibration" are used only in their physical senses; no teleology in evolution ("in order to" is banned for adaptations — selection language only); wonder must come from what is true.
- **Evidence-story integrity:** experiments and discovery narratives are told accurately — real people, real dates, real results, verified; simplification may omit but never invent; myths of science history (lone-genius eureka distortions) are not repeated as fact.
- **Species/taxonomy currency:** for nature titles, every scientific name, classification, and conservation status is verified against current authorities as of the production date; recent reclassifications and splits are checked by name; the production date of taxonomic verification is recorded.
- **Health/brain boundary:** neuroscience and physiology titles never drift into diagnosis, treatment advice, or supplement claims; the UAPF medical-adjacent disclaimer applies.
- **Time-sensitive claims dated:** mission statuses, records ("the most distant object yet observed"), climate figures, and "current" counts carry their as-of date in text or notes.
- **Calibrated language throughout:** "proves" is reserved for mathematics; empirical results "show", "indicate", "are consistent with"; effect sizes and uncertainty acknowledged where they matter.

## QA Checklist

**Gate 1 — Architecture lock (end of Phase 0):**
- [ ] Title Clearance Report issued; CLEAR or explained CAUTION; no institutional-affiliation implication
- [ ] Central-question inventory complete; every chapter hook mapped to a real reader question
- [ ] Consensus map drafted: ESTABLISHED / FRONTIER / CONTESTED bands assigned to the planned territory
- [ ] Structure model locked (question-led / journey / field-guide); figure points fixed per chapter in the TOC
- [ ] Field-guide variant: entry field-architecture locked; species list verified against current taxonomy
- [ ] Pen name (no invented credentials) and Book Identity Code locked, collision-checked

**Gate 2 — Per-chapter (before each chapter is delivered):**
- [ ] All six explainer stages present: hook question, intuition-building, mechanism, evidence story, implications, wonder payoff
- [ ] Every analogy states where it breaks, at the point of use
- [ ] At least one evidence story (HOW we know) with verified people, dates, and results
- [ ] Every number verified exact; every humanizing comparison recomputed and true; no truth-losing rounding
- [ ] Consensus-band labels applied: frontier claims flagged as frontier in the prose; no false certainty, no false balance
- [ ] Zero mysticism-adjacent language; no teleology in evolutionary explanation
- [ ] Terms defined on first use and used consistently; chapter assumes only earlier chapters
- [ ] Figures inserted at fixed points, accurate, captioned, referenced in prose; Style Signature held
- [ ] Field-guide entries: all fields present in locked order; look-alikes each carry a distinguishing feature; safety warnings present where required

**Gate 3 — Manuscript completion:**
- [ ] Cross-chapter consistency: terms, values, and analogies used identically everywhere (one value for the speed of light, one spelling per species)
- [ ] Glossary complete against every defined term; further-reading list verified real, entry by entry — zero fabricated citations
- [ ] All time-sensitive claims dated; science-currency note on copyright page carries the correct month/year
- [ ] Nature titles: full taxonomy re-verification pass at production date; conservation statuses current
- [ ] Mental-model build order intact after any chapter revisions

**Gate 4 — Consensus-classification audit + release:**
- [ ] **Consensus-classification audit on every major claim:** walk the finished manuscript claim by claim against the consensus map; each major claim is verified ESTABLISHED-and-stated-plainly, FRONTIER-and-labeled, or CONTESTED-and-fairly-presented. Any frontier claim reading as settled fact blocks release
- [ ] Quantitative audit: spot-recompute the full comparison set; verify no unit or magnitude error survived revision
- [ ] Mysticism/overclaim sweep on the complete text, including title, subtitle, and description metadata
- [ ] Disclaimer present and adapted (medical-adjacent, foraging-safety, etc. as the topic requires); AI-disclosure recorded
- [ ] Rights sweep: figure sources clean, no institutional logos or implied affiliations, quotations within limits and attributed
- [ ] eBook linked TOC valid; index (print) built; About the Author credential-clean

## KDP Positioning

- **Category tree:** Books > Science & Math > [field node] (e.g., Astronomy & Space Science > Astronomy; Biological Sciences > Evolution; Physics; Earth Sciences > Climatology), and for accessible-wonder titles additionally the popular-treatment nodes (Science for Kids ONLY if genuinely juvenile — never for adult titles). Field guides: Science & Math > Nature & Ecology > Field Guides, plus the regional/taxon node.
- **Description leads with:** the best hook question in the book, asked directly to the browser ("Why does time slow down near a black hole? By the end of this book, you'll know — and you'll know how we found out."), then the promise of comprehension-without-prerequisites, then honest wonder. Never leads with credentials (there are none to claim), never overclaims certainty, never uses mystical framing.
- **Metadata signals:** all 7 keyword slots with reader-language phrases ("astronomy book for beginners", "how the brain works", "science gifts for curious adults", "backyard bird identification guide [region]"); no institution or franchise names in keywords; age range only if genuinely set; series field only for real series.

## Key Rules — Do NOT Break

1. Consensus discipline is absolute: established science stated confidently, frontier science labeled as frontier, controversy presented as the field actually holds it — no false certainty, no false balance.
2. Every chapter runs the full explainer architecture: hook question → intuition-building → mechanism → evidence story → implications → wonder payoff. No stage skipped.
3. Every analogy acknowledges where it breaks, in the prose, at the point of use.
4. Every chapter tells at least one HOW-we-know evidence story with verified people, dates, and results — never bare assertion, never invented history.
5. Numbers are humanized but EXACT underneath: every comparison recomputed and true; no rounding that loses truth; order-of-magnitude honesty is non-negotiable.
6. No mysticism dressed as science — no quantum-consciousness, energy-healing, manifestation, or teleological-evolution language anywhere, including metadata.
7. Species names, taxonomy, and conservation statuses are current to the production date for every nature title, and the verification date is recorded.
8. The consensus-classification audit runs claim-by-claim on the finished manuscript at QA; one frontier claim dressed as settled fact blocks release.
9. No fabricated citations, studies, or further-reading entries — ever; unverifiable support becomes attributed consensus language or a marked placeholder.
10. Nothing is drafted before Phase 0 exits; chapters are generated one at a time into the single cumulative manuscript, each handoff ending with the standalone line: Type Proceed. The pen name carries no invented degrees or affiliations.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
