---
name: uapf-launch-manager
description: Generates and executes a 30-day KDP launch plan for a newly published Pegasus Press book — pricing strategy, KDP Select decision, promo scheduling, TOS-compliant review generation, launch checklist, and day-7/14/30 checkpoint monitoring.
---

# UAPF Launch Manager

Genie's post-publication launch skill. When a book goes live on Amazon, this skill turns the first 30 days from "uploaded and forgotten" into a structured, monitored launch campaign. It plans, it checklists, it monitors, and it reports — but it never spends money or changes prices without the operator saying so.

**A10 alignment (governs every launch plan):** Amazon's A10 algorithm rewards CONSISTENT organic sales velocity over one-day spikes, weights EXTERNAL (off-Amazon) traffic heavily, and ranks on conversion — so every launch plan (1) paces promotion as a steady drip across the 30 days rather than a single blast, (2) includes at least one external-traffic channel (Pinterest, YouTube, email, blog, social) pointing at the listing, and (3) verifies the Look Inside sample and A+ content are conversion-ready before promotion starts. See `uapf-kdp-niche-specialist` Core Method 15 for the full A10 model.

## When This Skill Triggers

| Trigger | Source | Action |
|---|---|---|
| Book confirmed live (ASIN assigned) | Handoff from `uapf-publisher` | Auto-generate the 30-day launch plan and present it to the operator |
| "Launch plan for [book]" / "start the launch" | Operator request | Generate or resume the launch plan for the named title |
| Day 7 / 14 / 30 of an active launch | Calendar checkpoint | Produce a checkpoint report with go/adjust recommendations |
| Mid-launch anomaly (BSR collapse, review problem) | Watchlist data via `uapf-kdp-niche-specialist` | Flag to operator with a recommended adjustment |

## Relationship to Sibling Skills

| Skill | What launch-manager gets from / gives to it |
|---|---|
| `uapf-publisher` | Receives the live-book handoff: ASIN, list price, format(s), categories, publish date |
| `uapf-kdp-niche-specialist` | Pulls KU-enrollment data for the niche (KDP Select decision), PRICE CHECK royalty data (price-step planning), ADS KEYWORDS list (handed onward to `uapf-ads-manager`), and WATCHLIST snapshots (monitoring) |
| `uapf-ads-manager` | Hands off the "start ads" step — launch-manager decides *when*, ads-manager decides *how* and gets its own operator confirmations |
| `uapf-cover-aplus-system` | Hands off A+ Content creation and submission |
| `uapf-review-monitor` | Consumes its review counts/ratings for milestone tracking during the 30 days |
| `uapf-royalty-reporter` | Supplies sales/royalty actuals for the checkpoint reports |

## Workflow 1 — Generate the 30-Day Launch Plan

1. **Confirm the book record.** Verify ASIN, live formats (ebook/paperback/hardcover), current list price, publish date, and niche. If any is missing, query `uapf-publisher` output or ask the operator. Do not plan against assumed data.
2. **Pull market intelligence.** From `uapf-kdp-niche-specialist`: the niche's KU-enrollment rate, PRICE CHECK royalty table for the book's price points, and the ADS KEYWORDS list. Date-stamp the data used.
3. **Draft the pricing strategy** (see Pricing section). Present it as a *proposal* — every price change in it is marked `[OPERATOR CONFIRMATION REQUIRED]`.
4. **Run the KDP Select decision framework** (see below). Output a recommendation with the niche data cited. Enrollment itself happens only on explicit operator instruction.
5. **Schedule promotions.** If (and only if) the book is enrolled in KDP Select, propose free-day or Countdown Deal windows (see Promo Scheduling).
6. **Schedule ads start.** Default: day 1, low-budget auto campaign via `uapf-ads-manager`; scale trigger at 3–5 reviews. Note that all ad spend gets its own confirmation inside that skill.
7. **Insert the launch checklist** (Workflow 2) with owners and target days.
8. **Write the plan** to `publishing/launch-plan.md` in the book's project folder, date-stamped, with the day-by-day table below filled in.
9. **Present the plan to the operator** and record which confirmation-gated items were approved, deferred, or declined. Update the plan file to reflect the decisions.

### Day-by-Day Sequence (template)

| Day | Action | Gate |
|---|---|---|
| 0 (live) | Verify listing renders correctly (look inside, cover, categories, keywords); take launch-day WATCHLIST snapshot | — |
| 0–1 | Claim/update Author Central profile; add book to author page | — |
| 1 | Start low-budget auto ad campaign (hand to `uapf-ads-manager`) | Operator confirms budget |
| 1–2 | Introductory price live (if approved); note step-up date in plan | Operator confirms price |
| 2–3 | Add book to Goodreads; create/attach series page if applicable | — |
| 3–5 | Submit A+ Content (hand to `uapf-cover-aplus-system`) | — |
| 7 | **Checkpoint 1**: BSR, reviews, sales, ad read-out; go/adjust call | — |
| 7–10 | If KDP Select: first promo window candidate (Countdown or free days) | Operator confirms |
| 10–14 | Harvest early ad data; scale ads if review threshold met | Operator confirms budget increase |
| 14 | **Checkpoint 2**: trend vs day 7; price step-up decision point | Operator confirms any price change |
| 15–25 | Steady state: monitor watchlist, respond to review milestones, second promo window if warranted | Gated as above |
| 28–29 | Prepare day-30 report; pull royalty actuals from `uapf-royalty-reporter` | — |
| 30 | **Checkpoint 3**: full launch retrospective; handoff to steady-state monitoring | — |

## Pricing Strategy

- **Introductory price option:** launch at a lower price (e.g., $0.99–$2.99 ebook) to buy velocity and early reviews, then step up to the target price in 1–2 increments (typical step points: day 7–10 and day 14–21). Use PRICE CHECK data to show the royalty at each step (note the 35%/70% ebook royalty boundary at $2.99).
- **Straight-to-target option:** launch at the long-term price when the niche's buyers are price-insensitive or the book is print-led.
- Present both with projected royalty per unit at each price. **Every price change — including the initial discounted price and every step-up — requires explicit operator confirmation before Genie touches the KDP price fields.** Record each confirmation, with date, in the plan file.

## KDP Select Decision Framework

Recommend **Select (KU)** when the niche's market-intelligence data shows high KU enrollment among top competitors (page-reads niches: genre fiction, activity/puzzle books, short-read nonfiction) and the operator has no wide-distribution plans for the ebook.

Recommend **Wide** when competitor KU enrollment is low, the book is print-dominant, buyers are libraries/institutions, or the operator sells on other platforms.

Rules:
1. Always cite the actual KU-enrollment figures from `uapf-kdp-niche-specialist`'s niche report — never a generic assumption. If no data exists, request a fresh niche pull before recommending.
2. Select requires ebook exclusivity to Amazon for 90-day auto-renewing terms — state this trade-off explicitly in the recommendation.
3. **Enrollment is executed only on explicit operator instruction.** The skill recommends; the operator decides.

## Promo Scheduling (KDP Select books only)

Per 90-day enrollment period a book gets **either up to 5 free promotion days or one Kindle Countdown Deal — not both**.

- **Free days:** best in weeks 2–3 of launch, run 2–3 consecutive days, paired with an ad push; goal is KU-borrow tail and also-bought seeding.
- **Countdown Deal:** best once the book has 5+ reviews and a stable BSR (typically day 14+); preserves 70% royalty during the discount. Countdown requires the book to have been at its list price for 30 days prior on some marketplaces — check eligibility in the KDP dashboard before proposing dates.
- Propose specific dates in the plan; scheduling them in KDP is a paid-promo-adjacent action and gets operator confirmation.

## Review Generation — TOS-Compliant Only

Amazon's review policies are absolute. The ONLY tactics this skill uses or recommends:

- **Back-matter review-ask page** in the book itself (a polite, no-incentive request with the review link) — coordinate insertion with `uapf-manuscript-builder`/`uapf-formatting-engine` before final upload of future titles, or via content update.
- **Author Central** profile fully set up so the author looks legitimate.
- **Organic audience prompts** the operator controls (newsletter, social) — drafted on request, never sent by Genie without approval.
- Time and patience.

**PROHIBITED — never do, never recommend, refuse if asked:** paid reviews, incentivized reviews (free product/gift cards/entries in exchange), review swaps with other authors, review-service vendors, family/close-associate reviews, and asking anyone to change or remove a critical review. These violate Amazon TOS and risk account termination. If the operator requests any of these, decline and cite this section.

## Workflow 2 — Launch Checklist

Track in the plan file with status boxes:

1. [ ] Listing verified live and correct (ASIN: ____, date: ____)
2. [ ] Author Central profile claimed/updated; book attached to author page
3. [ ] A+ Content submitted (handed to `uapf-cover-aplus-system`) — submission date: ____
4. [ ] Book added to Goodreads (and LibraryThing if operator uses it)
5. [ ] Series page created on Amazon (if book is part of a series)
6. [ ] Launch-day WATCHLIST snapshot taken (via `uapf-kdp-niche-specialist`)
7. [ ] Ads started (`uapf-ads-manager` engaged, budget confirmed by operator)
8. [ ] Pricing plan decisions recorded (approved / declined per step)
9. [ ] KDP Select decision recorded (enrolled / wide, per operator instruction)

## Workflow 3 — Launch Monitoring and Checkpoints

1. Use the WATCHLIST (via `uapf-kdp-niche-specialist`) to snapshot BSR, price, review count, and rating on days 0, 7, 14, 21, 30 at minimum.
2. Track milestones: first sale, first review, 5 reviews, 10 reviews, BSR under the niche's top-competitor median.
3. At **day 7, day 14, and day 30**, write a checkpoint report to `publishing/launch-checkpoint-day{N}.md` containing: date-stamped metrics table (vs prior checkpoint), sales/royalty actuals (from `uapf-royalty-reporter`), ad summary (from `uapf-ads-manager`'s log), review status (from `uapf-review-monitor`), and a **GO / ADJUST recommendation** with specific proposed changes — each spend- or price-affecting proposal marked `[OPERATOR CONFIRMATION REQUIRED]`.
4. Day-30 report additionally includes a launch retrospective: what worked, what to change for the next title in this niche, and the steady-state monitoring cadence going forward.

## Outputs

| File | Content |
|---|---|
| `publishing/launch-plan.md` | The full date-stamped 30-day plan, checklist, decisions log |
| `publishing/launch-checkpoint-day7.md` | Checkpoint 1 report |
| `publishing/launch-checkpoint-day14.md` | Checkpoint 2 report |
| `publishing/launch-checkpoint-day30.md` | Checkpoint 3 report + retrospective |

## Key Rules — Do NOT Break

1. **Every price change requires explicit operator confirmation** — introductory price, every step-up, every discount. No exceptions, ever.
2. **Every paid promotion requires explicit operator confirmation** with the cost stated before scheduling — ads (via `uapf-ads-manager`'s own gate), Countdown Deals, any third-party promo.
3. **Never violate Amazon review TOS.** No paid, incentivized, swapped, or solicited-from-associates reviews. Refuse such requests and cite the Review Generation section.
4. **KDP Select enrollment only on explicit operator instruction** — the skill recommends with cited niche data; it never enrolls on its own judgment.
5. **Date-stamp everything** — plans, snapshots, checkpoints, decisions, confirmations. An undated metric or decision is worthless for the retrospective.
6. **Cite real data, never invent it.** KU-enrollment claims come from the niche specialist's report; sales come from `uapf-royalty-reporter`; reviews from `uapf-review-monitor`. If data is missing, say so and request it.
7. **One promo type per 90-day Select period** — 5 free days OR one Countdown Deal, never plan both in the same enrollment period.
8. **Record operator decisions in the plan file** the moment they are made — approved, deferred, or declined — so any later session can resume the launch without re-asking.
