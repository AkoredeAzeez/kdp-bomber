---
name: uapf-pen-name-manager
description: Registry and rules-keeper for all Pegasus Press pen names — niche ownership, brand fingerprints (palettes, structure skeletons), collision checks for Phase 0, and the absolute no-fabricated-credentials rule.
---

# UAPF Pen Name Manager​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Genie's identity-governance skill for Pegasus Press. The operation publishes under multiple pen names across many niches; this skill is the **single source of truth** for who those pen names are, what they own, and what brand fingerprints they have already used. Every Phase 0 (project setup) must consult it, and every published book must be recorded in it.

Two jobs: (1) maintain the **registry**, (2) run **collision services** that keep the catalog's strict no-repeat rules (structures, palettes) and identity-safety rules intact.

## Position in the UAPF Skill Family

| Sibling skill | Relationship |
|---|---|
| `uapf-catalog-strategist` | Consults niche ownership when slotting projects; a niche belongs to one pen name. |
| `uapf-kdp-niche-specialist` | Discovery/validation identifies the niche; this skill decides which pen name carries it. |
| `uapf-publisher` | Runs Phase 0 — must call all four collision services here before locking pen name, palette, or structure. |
| `uapf-cover-aplus-system` | Palette pairings chosen for covers are checked against and recorded in the registry. |
| `uapf-royalty-reporter` | Uses the registry to roll up P&L by pen name. |
| `uapf-launch-manager` | Uses Author Central status and bio assets at launch time. |

## The Registry: `catalog/pen-names.json`

**Append-mostly**: entries are added and extended; existing fingerprint records are never deleted or rewritten (a used palette stays "used" forever — that is the point). Corrections are made as dated amendments.

Per pen name, the registry records:

| Field | Content |
|---|---|
| `name` | The byline exactly as published |
| `niches_owned` | Niches this pen name owns. **A niche belongs to exactly one pen name.** |
| `live_titles` | ASINs/titles currently live under this byline |
| `series` | Series this pen name carries (name, numbering scheme, brand system) |
| `fingerprints.palettes` | Every **primary+accent color pairing** used, per book |
| `fingerprints.structures` | Every **TOC-skeleton / chapter-architecture fingerprint** used, per book |
| `fingerprints.cover_styles` | Cover style notes per book (layout family, typography direction) |
| `author_central` | Profile status per marketplace (none / created / complete) |
| `bio` | Bio text and niche-register variants — see the credentials rule below |

### The Bio Rule (absolute)

Pen names are allowed. **Fabricated credentials are not.** A bio must never claim degrees, licenses, certifications, professional experience, awards, or institutional affiliations that no real person behind the operation holds. This is an absolute rule inherited from the framework — it has no operator override. Acceptable bios are built from truthful framing: the imprint's research process, the series' purpose, genuine interests. If a niche seems to "require" credentials we don't have (medical, legal, financial authority claims), that is a signal for the risk-regime check in `uapf-research-compliance`, not a license to invent them.

## Collision Services (Phase 0 Gates)

Phase 0 of every project must run all four checks that apply. Each returns **PASS** or **COLLISION** with specifics.

### 1. Byline Collision Check
Proposed new pen name vs (a) real notable authors and public figures and (b) existing authors on the target marketplace. The test: could the byline **imply identity with a real person** or trade on their recognition? Same or confusingly-close name in the same or adjacent category = COLLISION → generate alternatives. Err toward caution; a distinctive name costs nothing.

### 2. Palette Collision Check
Proposed primary+accent pairing vs **every pairing already used across the entire catalog** (all pen names — the no-repeat rule is catalog-wide). An exact or near-indistinguishable pairing = COLLISION → propose the nearest unused pairings. Every check answer comes from the registry, which is why same-day fingerprint recording (below) is mandatory.

### 3. Structure Fingerprint Check
Proposed TOC skeleton + chapter architecture vs every prior book's structure fingerprint (**Hard Rule 19: no-repeat**). Matching skeleton shape — same section pattern, same chapter formula, same scaffold order — = COLLISION → the manuscript plan must be restructured before drafting begins.

### 4. Niche Ownership Routing
If the new book's niche is already owned, the book **routes to the owning pen name** — brand compounding is the whole point of ownership. If unowned, the project either extends an existing pen name's coherent brand territory (adjacent niche, operator confirms) or triggers new-pen-name registration. Splitting an owned niche across two pen names requires an explicit operator override, recorded in the registry entry.

## Author Brand Assets

- **Bio variants per niche register** — one pen name may need a warmer register for one niche and a more technical one for another; all variants live in the registry and all obey the Bio Rule.
- **Author Central setup checklist** — per marketplace: profile created, bio pasted, photo/graphic decision recorded, books claimed to the profile, status updated in the registry.
- **Byline formatting rules** — the byline is character-identical everywhere it appears (cover, title page, KDP metadata, A+ content, Author Central). Variant spellings fracture the author page and the brand.

## Workflows

### A. Registering a New Pen Name (Phase 0 creates one)

1. Run the **byline collision check**; iterate until PASS.
2. Draft the bio (and any niche-register variants); verify against the Bio Rule.
3. Create the registry entry: name, owned niche(s), empty title/series lists, bio.
4. Record the project's proposed fingerprints (palette pairing, structure fingerprint, cover style) as **RESERVED** so parallel projects can't collide with them.
5. Add Author Central setup to the launch checklist (status: none → pending).
6. Confirm registration back to Phase 0 with the pen name locked.

### B. Recording a Published Book (go-live day)

1. On the day the book goes live: update the pen name's entry — add the title/ASIN, flip its fingerprints from RESERVED to USED, attach cover style notes.
2. Update series data if the book extends or starts a series.
3. Update Author Central status (book claimed to profile).
4. Confirm the registry write in the go-live report. **Same-day, no exceptions** — every collision check for the next project depends on this record existing.

### C. Serving a Collision Check (request from Phase 0)

1. Load the current registry; if a write is pending (unrecorded live book), complete it first — never answer checks from a stale registry.
2. Run the requested check(s) per the definitions above.
3. Return PASS, or COLLISION with the exact conflicting entry (pen name, book, fingerprint) and suggested alternatives.
4. Log the check result in the project's Phase 0 record.

## Key Rules — Do NOT Break

1. **No fabricated credentials, ever.** Pen names yes; fake degrees, licenses, or experience never. Absolute framework rule — no operator override exists.
2. **One niche, one pen name** — a new book in an owned niche routes to its owning pen name, unless the operator explicitly overrides (and the override is recorded in the registry).
3. **Every published book's fingerprints are recorded same-day** — palette pairing, structure fingerprint, cover style notes — the moment it goes live.
4. **The registry is the single source of truth for collision checks, and Phase 0 must consult it.** No project locks a pen name, palette pairing, or TOC structure without a PASS from the registry.
5. **The registry is append-mostly.** Used fingerprints are never deleted; corrections are dated amendments, not rewrites.
6. **Palette and structure no-repeat rules are catalog-wide**, across all pen names — not per pen name.
7. **Bylines are character-identical everywhere.** One spelling, everywhere the name appears.
8. **Never answer a collision check from a stale registry.** Flush pending writes first.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
