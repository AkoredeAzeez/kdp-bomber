---
name: uapf-ads-manager
description: Creates and optimizes Amazon Ads campaigns for published Pegasus Press books via advertising.amazon.com — campaign architecture from the niche keyword list, break-even ACOS math from real royalty data, weekly optimization loop, and an append-only ads log; no money is ever spent without explicit operator confirmation.
---

# UAPF Ads Manager

Genie's Amazon Advertising skill. It operates the Amazon Ads console (advertising.amazon.com) through the built-in browser to build, monitor, and optimize Sponsored Products campaigns for Pegasus Press books. The operator must already be logged in to the ads console; Genie never enters credentials or payment information — if a login or payment screen appears, stop and hand control to the operator.

**A10 alignment:** Amazon's A10 algorithm weights PPC-driven sales LESS than A9 did — ad-driven rank decays fast when ads stop. Ads are an organic-rank IGNITER, never the ranking strategy. Therefore: track the book's ORGANIC search rank for its core keywords alongside every ad metric; if rank collapses whenever ads pause, diagnose it as a listing conversion/relevance problem (cover CTR, price position, description, Look Inside) and flag it — more ad spend is the wrong fix. See `uapf-kdp-niche-specialist` Core Method 15 for the full A10 model.

## HARD SAFETY GATE — Read First

**Creating campaigns, raising budgets, and raising bids spend the operator's real money.**

| Action | Gate |
|---|---|
| Launch any new campaign | **Explicit operator confirmation required**, with the exact daily budget stated in the confirmation request (e.g., "Launch auto campaign for ASIN B0XXXX at **$5.00/day**? Confirm.") — no launch until a clear yes |
| Increase any campaign budget | **Explicit operator confirmation required**, with old → new daily budget stated |
| Set or raise an account/portfolio budget cap | **Explicit operator confirmation required** |
| Enable a paused campaign | **Explicit operator confirmation required** (it resumes spend) |
| Bid changes (up or down) within an operator-approved budget cap | May proceed without per-change confirmation, but **every change is logged and reported** in the weekly report |
| Bid decreases, pausing campaigns/targets, adding negatives | May proceed (these reduce or contain spend); logged |
| Entering credentials or payment details | **PROHIBITED — never.** Operator does this personally |

Confirmations are per-action: approval of one campaign's budget is not approval of the next. If the operator sets a standing cap (e.g., "total ad spend max $15/day across this book"), record it, date-stamped, in `advertising/ads-log.md`, and operate bids/negatives freely under it — but any change that would raise total configured daily budgets above the cap goes back to the operator.

## Inputs

| Input | Source |
|---|---|
| ADS KEYWORDS list (100–300 terms, tiered) | `uapf-kdp-niche-specialist` |
| Competitor ASINs for product targeting | `uapf-kdp-niche-specialist` niche report |
| Royalty per unit at current price (PRICE CHECK) | `uapf-kdp-niche-specialist` |
| ASIN, formats, price, launch date | `uapf-publisher` / `uapf-launch-manager` handoff |
| Timing (when to start, when to scale) | `uapf-launch-manager` launch plan |

If the ADS KEYWORDS list or PRICE CHECK data is missing, request it from `uapf-kdp-niche-specialist` before building anything.

## Campaign Architecture (per book)

Four Sponsored Products campaigns per book, named `PP-{ShortTitle}-{Type}-{YYYYMMDD}`:

| # | Campaign | Targeting | Purpose | Starting budget | Starting bid |
|---|---|---|---|---|---|
| 1 | Auto (discovery) | Amazon auto-targeting, all 4 match groups on | Discover converting terms/ASINs Amazon finds | $5/day | Suggested bid or ~$0.35–$0.50 |
| 2 | Broad research | Broad match, top 50–100 terms from ADS KEYWORDS | Widen the funnel, find phrasing variants | $5/day | ~$0.40–$0.60 |
| 3 | Exact performance | Exact match, top 20–40 proven/high-intent terms | Profitable scale on known winners | $5–$10/day | ~$0.50–$0.75, per-keyword |
| 4 | Product targeting | Competitor ASINs + relevant categories | Show on competitor pages / also-bought | $5/day | ~$0.35–$0.50 |

Notes:
- Budgets above are *recommendations to present to the operator* — nothing launches until the operator confirms each campaign with its exact daily budget.
- Start bids near Amazon's suggested-bid midpoint; books usually convert at lower CPCs than general retail, so err low and raise on data.
- One ad group per campaign at launch; keep structure simple until data justifies splitting.
- The exact campaign starts thin and grows via weekly harvesting from auto/broad.

## Automation tooling (deterministic; run these, never do the math by hand)

The strategy below is executed through three tools in this folder so every
book gets the same rigor, fast:

- `ads_math.py breakeven|bands|budget --royalty R --price P [--monthly M]` -
  computes the exact break-even ACOS, the phase target bands, and a
  4-campaign budget split with a realistic launch outcome. Use it at setup
  and whenever price or royalty changes.
- `ads_analyzer.py <search-term-report.csv> --royalty R --price P
  [--phase launch|transition|profit] [--project <book folder>]` - the weekly
  engine. The operator exports the search-term report from
  advertising.amazon.com (one CSV); this reads it and applies the loop rules
  MECHANICALLY, emitting the ranked action list: HARVEST winners, NEGATE
  waste (>10 clicks, 0 orders), BID UP / BID DOWN, WATCH, plus blended ACOS
  vs the book's break-even. Spend actions are marked PROPOSE (operator
  confirms); spend-reducing actions are safe to apply and logged. Writes
  `advertising/ads-analysis-<date>.md`.
- `AMAZON_ADS_FOR_BEGINNERS.md` - the plain-English client primer. Offer it to
  any client new to ads BEFORE building campaigns; most KDP authors have never
  run ads and this prevents the money-losing mistakes.

The numbers the tools produce are read from the client's REAL exported report;
the honest-data and money-gate rules below bind every tool output exactly as
they bind manual work. `ads_analyzer.py` proposes; it never spends.

WEEKLY CADENCE: the automation calendar carries a `weekly-ads-optimization`
job (uapf-ads-manager). Each week Genie prompts the client to export the report
and drop it in, runs the analyzer, applies safe changes, and proposes the rest.

## Break-Even ACOS

Compute from the book's *actual* royalty (PRICE CHECK data), never a generic figure:

```
Break-even ACOS = royalty per unit ÷ list price
```

Example: $14.99 paperback with $4.23 royalty → break-even ACOS = 4.23 / 14.99 = **28.2%**.

| Phase | Target ACOS band | Rationale |
|---|---|---|
| Launch (days 1–30) | Up to ~1.5–2× break-even (deliberately unprofitable) | Buying velocity, reviews, also-boughts, organic rank |
| Transition (days 30–60) | At or slightly above break-even | Ads wash their face while organic grows |
| Profit phase (60+) | Below break-even (e.g., 60–80% of it) | Ads contribute margin |

For KU-enrolled books, note in reports that page-read royalties are not attributed in the ads console, so console ACOS *overstates* true ACOS — state this caveat rather than adjusting numbers by guesswork.

## Weekly Optimization Loop

Run every 7 days per active book (align with `uapf-launch-manager` checkpoints during launch):

1. **Pull data.** In the ads console, open the search-term report / targeting views for the last 14–30 days (clicks need time to attribute; never optimize on <7 days of data). Read the real numbers from the console — never estimate or recall them.
2. **Harvest winners.** Any search term or ASIN with ≥1 order and sane ACOS in auto/broad → add as exact match (or product target) in the performance campaign, then add it as negative-exact in the source campaign so the exact campaign owns it.
3. **Cut waste.** Rule: any search term with **clicks > 10 and 0 orders** → add as negative (negative-exact for specific terms, negative-phrase for clearly irrelevant themes). Terms with 5–10 clicks and 0 orders: bid down and watch one more week.
4. **Adjust bids** (within the approved cap): winners (ACOS below target band, winning impressions) +10–20%; losers (ACOS above band with orders) −10–20%; no-impression keywords +15% or note that bid may need operator-approved budget headroom.
5. **Check budget pacing.** Campaigns hitting their daily cap before mid-day with good ACOS → propose a budget increase to the operator (gated). Campaigns spending nothing → check bids/eligibility.
6. **Log every change** in `advertising/ads-log.md` (see Outputs) — date, campaign, entity, old value → new value, reason.
7. **Write the weekly report** — spend, sales, ACOS vs the book's break-even, changes made, proposals awaiting operator confirmation.

## Scale / Kill Rules

| Situation | Action |
|---|---|
| Campaign ACOS below target band for 2+ consecutive weeks, hitting budget cap | Propose budget increase (operator confirmation with exact new figure) |
| Exact keyword: 3+ orders, ACOS below break-even | Bid up; candidate for its own single-keyword treatment if it dominates |
| Campaign: spend > 3× royalty of one unit with 0 orders over 30 days | Pause campaign, report to operator |
| Keyword/target: clicks > 10, 0 orders | Negative/pause (per loop rule) |
| CTR < 0.15% at 1,000+ impressions | Targeting-relevance problem — refine terms; if book-wide, flag cover/title/price to operator |
| Whole-book ads unprofitable after 60 days despite optimization | Recommend kill or minimal-maintenance mode to operator with the numbers |

### Metrics Reference (typical books benchmarks)

| Metric | Weak | Acceptable | Strong |
|---|---|---|---|
| CTR | < 0.15% | 0.2–0.4% | > 0.5% |
| CVR (orders/clicks) | < 5% | 8–12% | > 15% |
| CPC (books) | > $1.00 | $0.30–$0.70 | < $0.30 with impressions |
| Impressions/week per campaign | < 500 (starved) | 2,000–10,000 | 10,000+ with held CTR |

Benchmarks are context: always evaluate ACOS against **this book's** break-even, not these generic bands.

## Console Operation Notes

- Work at advertising.amazon.com in the built-in browser; verify the correct account/marketplace is active before touching anything.
- If logged out, or any credential, 2FA, or payment prompt appears: **stop immediately** and ask the operator to complete it.
- After every change, verify the console reflects it (re-read the row) before logging it as done.
- Screenshot or copy the key report figures into the log so reports are auditable.

## Outputs

| File | Content |
|---|---|
| `advertising/ads-log.md` | **Append-only** dated history: every campaign created (with confirmed budget and who confirmed), every bid/negative/budget change, every operator confirmation, standing caps. Never rewrite or delete past entries — corrections are new entries. |
| `advertising/weekly-report-{YYYY-MM-DD}.md` | Weekly loop output: metrics table, ACOS vs this book's break-even, changes made, pending proposals |

## Key Rules — Do NOT Break

1. **No money is spent without explicit operator confirmation.** Every campaign launch, every budget increase, every re-enable of a paused campaign is confirmed by the operator with the exact daily budget stated. A recommendation is not a confirmation; silence is not a confirmation.
2. **Never enter credentials or payment information** in the ads console or anywhere else. Login and billing are the operator's alone.
3. **`advertising/ads-log.md` is append-only.** Never edit or delete historical entries; corrections are appended as new dated entries.
4. **Never fabricate metrics.** Every number in a log or report is read from the ads console (or an exported report) at a stated date. If data is unavailable, write "data unavailable" — never estimate silently.
5. **Report ACOS against the book's actual break-even ACOS** computed from its real PRICE CHECK royalty — never against generic industry targets.
6. **Bid changes stay inside the operator-approved budget cap**; anything that would push configured daily spend above the cap goes back to the operator first.
7. **Date-stamp every entry, change, confirmation, and report.**
8. **Optimize on sufficient data only** — minimum 7 days and meaningful clicks before harvesting, negating, or re-bidding; attribution lag is real.
9. **Per-action confirmations do not generalize.** Approval for one campaign, one budget, one book never carries over to another.
