---
name: uapf-catalog-strategist
description: The "what should we publish next" brain — scores candidate projects, plans series arcs, balances the portfolio, and maintains the rolling publishing calendar that the operator approves before any project starts.
---

# UAPF Catalog Strategist

Genie's portfolio-planning skill for Pegasus Press. This skill answers one question with evidence: **what should we publish next, and why?** It converts everything the operation knows — catalog performance, niche discovery, series verdicts, arbitrage scans, seasonality, and production capacity — into a ranked, slotted, operator-reviewable publishing calendar.

Runs **monthly** (start of month, or alongside `uapf-daily-standup`'s monthly rollup) and **on request** — e.g. "Genie, plan next quarter", "what's next after this book?", "re-plan the calendar".

## Position in the UAPF Skill Family

| Sibling skill | Relationship |
|---|---|
| `uapf-kdp-niche-specialist` | Supplies niche-discovery reports, validation verdicts, series-detector verdicts, arbitrage scan results, and watchlist/BSR history. The strategist consumes; it does not re-run discovery. |
| `uapf-pen-name-manager` | Authority on niche ownership. Every slotted project must respect pen-name niche ownership before it lands on the calendar. |
| `uapf-publisher` | Receives the one-line brief when the operator green-lights a slotted project. |
| `uapf-launch-manager` | Launch timing feeds back into seasonality deadlines (a book must be live and reviewed before its seasonal window). |
| `uapf-backlist-optimizer` | Flags underperformers; a dormant-book refresh can enter the backlog queue as a low-effort candidate. |
| `uapf-daily-standup` | Surfaces calendar status and upcoming publish-by deadlines in the daily brief. |

## Inputs

Gather all six before scoring. Missing inputs are stated explicitly in the output ("no arbitrage scan newer than 60 days — translation candidates not scored"), never silently skipped or invented.

| # | Input | Source | What it contributes |
|---|---|---|---|
| 1 | Catalog performance | Watchlist / BSR history per live book (niche-specialist watchlists) | Which niches are proven for *us*; which books earn a sequel |
| 2 | Niche-discovery reports | `uapf-kdp-niche-specialist` DISCOVERY/VALIDATION outputs | Validated new-entry candidates with revenue bands |
| 3 | Series verdicts | Niche-specialist series detector | Which niches are series-driven (book 2+ compounds on book 1's audience) |
| 4 | Arbitrage scan results | Niche-specialist arbitrage scanner | Translation/marketplace-transfer opportunities (low effort, proven demand) |
| 5 | Seasonal publish-by calendar | Seasonality data per niche | Hard deadlines: a seasonal book published after its window is a wasted slot |
| 6 | Production capacity | Operator-set assumption (books/month) | How many slots exist per month. Never assume — if unset, ask the operator |

## Scoring Model

Score every candidate project on four axes. Show the component scores in the output, not just a total — the operator must be able to see *why* a project ranked where it did.

### 1. Expected Revenue
`niche revenue band × achievable share`. Achievable share is honest: a cold entry into a competitive niche takes a small share; book 3 of a performing series takes a large one. Cite the revenue band's source report and date.

### 2. Strategic Value
Ordered preference, strongest first:

1. **Series extension** in a performing, series-driven niche (compounds existing audience and brand)
2. **Proven-niche sequel/adjacent title** — we have live sales data proving demand
3. **Arbitrage/translation** of our own performer into a validated marketplace
4. **Format variant** of a performer (e.g. large print, workbook edition)
5. **New niche entry (validated)** — cold start, but discovery-backed
6. **New niche entry (unvalidated)** — does not get scheduled; route back to niche-specialist VALIDATION first

### 3. Effort Class
`translation < format variant < new book`. Also account for series setup overhead (book 1 of a planned series carries brand-system design cost that books 2-N inherit for free).

### 4. Seasonality Deadline Pressure
Work backwards from the seasonal buy window: publish-by date = window start − review-accrual lead time (coordinate with `uapf-launch-manager` assumptions). A candidate whose deadline is infeasible at current capacity scores zero for this cycle and is annotated for next year — do not slot books that will miss their window.

## Series Pipeline Logic

For any niche the series detector marks **series-driven**:

- Plan the **full series arc** (books 1 through N) as a program, not a sequence of one-off decisions.
- Define the shared brand system up front: pen name (via `uapf-pen-name-manager`), naming convention, cover system, numbering — so book 2 is recognizably a sibling of book 1.
- Slot book 1 normally; pencil books 2-N into the backlog with a trigger condition (e.g. "book 2 enters the active calendar when book 1 sustains BSR < X for 30 days or hits Y reviews").
- A series arc occupies future capacity — reflect that when scoring competing new entries.

## Portfolio Balance Rules

Applied *after* scoring, before slotting. Balance rules can demote a high-scoring project.

1. **No niche concentration** — do not let any single niche dominate the active calendar; a niche shock (new competitor, algorithm shift, seasonality miss) must never threaten the whole quarter.
2. **Spread across risk regimes** — mix proven-niche safety (sequels, translations) with a controlled ration of new-niche exploration each quarter. All-safe stagnates; all-new gambles the operation.
3. **Respect pen-name niche ownership** — a niche belongs to one pen name. Route projects to the owning pen name via `uapf-pen-name-manager`; a project needing a *new* pen name inherits that Phase 0 overhead in its effort class.
4. **Mind the no-repeat rules** — structure fingerprints and palette pairings must not repeat across the catalog; heavy clustering in one category exhausts differentiation headroom faster. Flag when a niche cluster is approaching it.

## Output: `catalog/publishing-calendar.md`

A single rolling document, regenerated each run (prior versions preserved by date in the file's changelog section).

**Section 1 — Slotted projects (next 3 months).** One entry per capacity slot:

- Month/slot, project name, pen name, niche
- Score breakdown (revenue / strategic / effort / seasonality)
- Rationale — 2-3 sentences citing the specific data (report, watchlist, verdict) that justifies the slot
- Publish-by deadline if seasonal
- **One-line pipeline brief**, ready to hand to `uapf-publisher` on approval: `Title direction: X | Marketplace | Language | pages`

**Section 2 — Backlog queue.** All remaining candidates ranked by score, each with a one-line rationale and its trigger condition (if any). This is the bench the calendar draws from when a slot opens or data changes.

**Section 3 — Assumptions and gaps.** Capacity setting used, input freshness (date of each source report), and any missing inputs.

## Workflow

1. **Trigger** — monthly schedule fires, or the operator asks for a plan/re-plan.
2. **Collect inputs** — all six sources; record the date of each. Ask the operator for the current capacity assumption if not on file.
3. **Build the candidate list** — series extensions due, validated new niches, arbitrage opportunities, format variants, backlist refreshes, plus carry-overs from the existing backlog queue.
4. **Filter** — drop unvalidated niches (route to VALIDATION), drop seasonal candidates with infeasible deadlines (annotate for next cycle), check pen-name ownership routing for every survivor.
5. **Score** — all four axes per candidate, components shown.
6. **Apply portfolio balance rules** — adjust slotting; document every demotion ("scored #2 but demoted: third consecutive slot in niche X").
7. **Slot and write** — fill 3 months of capacity, rank the rest into the backlog, write `catalog/publishing-calendar.md` with rationale and pipeline briefs.
8. **Present to operator** — summarize the slate and the biggest calls (what got in, what got cut, what's risky). Then stop.
9. **On approval** — when the operator green-lights a specific slot (or has issued an explicit standing instruction covering it), hand its one-line brief to the pipeline. Mark the slot APPROVED in the calendar.
10. **Re-score on new data** — when a niche report, series verdict, arbitrage scan, or meaningful watchlist shift lands, re-run scoring and flag calendar changes to the operator rather than silently reshuffling approved slots.

## Key Rules — Do NOT Break

1. **Every recommendation cites data.** Each slotted project names the specific report, watchlist, or verdict (with date) behind it. No "gut feel" slots.
2. **No project starts without operator go.** The calendar is a proposal; a slot becomes a live project only on the operator's explicit approval or a pre-existing explicit standing instruction. Genie proposes, the operator disposes.
3. **The calendar is a proposal document, not a work order.** Never treat a slotted-but-unapproved entry as authorization to begin production.
4. **Re-score when new data lands.** Stale rankings are worse than no rankings — but never silently reshuffle already-approved slots; surface the change and let the operator decide.
5. **Never slot an unvalidated niche.** Route it to `uapf-kdp-niche-specialist` VALIDATION first.
6. **Never slot a seasonal title that will miss its window.** Zero-score it for the cycle and annotate for next year.
7. **State missing inputs; never fabricate them.** A gap in the data is reported as a gap.
8. **Respect pen-name niche ownership on every slot** unless the operator explicitly overrides.
