---
name: uapf-royalty-reporter
description: Monthly P&L engine — builds per-book, per-pen-name, and whole-catalog profit reports from real KDP royalty data and ad spend, with a strict actuals-only policy (no estimated or fabricated revenue, ever).
---

# UAPF Royalty Reporter

Genie's finance skill for Pegasus Press. Produces the monthly profit-and-loss picture at three levels — **per book, per pen name, whole catalog** — by combining reported KDP royalties with recorded ad spend. Its defining discipline: **actuals only**. If a number was not reported by Amazon or recorded in our own logs, it does not appear as an actual.

Runs monthly (when the prior month's KDP data is complete — KDP finalizes with a lag, typically mid-month) and on request ("Genie, how did June do?", "P&L for pen name X").

## Position in the UAPF Skill Family

| Sibling skill | Relationship |
|---|---|
| `uapf-ads-manager` | Source of ad-spend actuals (ads-log / Ads console). Receives every book flagged **ad spend > royalties** for corrective action. |
| `uapf-backlist-optimizer` | Receives every book flagged **DORMANT** for refresh/retire evaluation. |
| `uapf-catalog-strategist` | Consumes pen-name and niche profit rollups as catalog-performance evidence for planning. |
| `uapf-kdp-niche-specialist` | Its watchlists track BSR-based *estimates* — useful for market context, never mixed unlabeled with reported actuals. |
| `uapf-daily-standup` | Surfaces the latest monthly P&L headline and outstanding data gaps. |

## Data Sources — Strict Preference Order

| Priority | Source | How | Notes |
|---|---|---|---|
| 1 | **KDP Reports dashboard** | Read via the built-in browser with the operator already logged in. Genie **never enters credentials** — if the session is logged out, stop and ask the operator to log in. | Orders, KENP page reads, and royalties per marketplace. Read-only navigation only. |
| 2 | **KDP report exports** (xlsx/csv) | Operator downloads reports to the watched folder; Genie parses them. | Preferred for archival months; exact figures, parseable offline. |
| 3 | **Neither available** | Report **NO DATA** for the affected book/month/marketplace. | Never estimate, interpolate, or backfill actuals. A NO DATA cell is a correct answer. |

Ad spend comes from the ads-log maintained by `uapf-ads-manager` (or the Ads console read the same way as source 1). Missing ad data is likewise marked NO DATA — a P&L with unknown ad spend says so rather than assuming zero.

## P&L Structure — Per Book

```
Royalties (print + eBook + KENP)
−  Ad spend
=  Net profit
```

Per-book table columns:

| Column | Content |
|---|---|
| Book / ASIN / Pen name / Niche | Identity (pen name and niche from `catalog/pen-names.json`) |
| Print royalties | Reported, per month |
| eBook royalties | Reported, per month |
| KENP royalties | Reported payout (see KENP notes below) |
| Ad spend | From ads-log / Ads console |
| **Net profit (month)** | Computed from the above actuals |
| **Net profit (lifetime)** | Running total from `finance/catalog-ledger.md` |
| Flags | AD-NEGATIVE / DORMANT / NO DATA (per source gaps) |

Plus a **per-marketplace breakdown** (.com, .co.uk, .de, etc.) beneath each book — royalties by marketplace and currency, converted to the reporting currency with the conversion rate and its date stated.

### KENP Notes

The per-page KENP royalty rate varies **every month** (set retroactively by the KDP Select Global Fund). Therefore:

- Use the **actual reported KENP royalty** from KDP Reports — never multiply page reads by a guessed or last-month per-page rate.
- Page reads without a finalized payout yet = royalty **PENDING**, reported as page-read counts only, clearly labeled.

## Catalog Rollup

1. **Profit by pen name** — each pen name's books aggregated; the brand-level view.
2. **Profit by niche** — feeds catalog strategy (which niches actually pay).
3. **Profit by month** — catalog trend line vs prior months (3-month and 12-month comparison where history exists).
4. **Flags with handoffs:**
   - **AD-NEGATIVE** — ad spend exceeded royalties this month → hand the book to `uapf-ads-manager` with the numbers.
   - **DORMANT** — negligible royalties across recent months with no active push → hand to `uapf-backlist-optimizer`.
   - **DATA GAP** — any book/month/marketplace where a source was unavailable → list for the operator to resolve (e.g. download the export).

## Outputs

| File | Nature | Content |
|---|---|---|
| `finance/pnl-[YYYY-MM].md` | One per month, immutable once the month is finalized | Full per-book tables, per-marketplace breakdowns, pen-name/niche/month rollups, flags, data-source notes, conversion rates used |
| `finance/catalog-ledger.md` | **Append-only** running ledger | One line per book per finalized month (royalties, ad spend, net); never rewrite history — corrections are appended as dated adjustment lines referencing the original entry |

## Workflow

1. **Trigger** — monthly close (after KDP finalizes the prior month) or operator request.
2. **Inventory the catalog** — enumerate live books from the pen-name registry / catalog records so no book is silently omitted.
3. **Pull royalty actuals** — source 1 (dashboard, operator logged in) or source 2 (watched-folder exports); note which source served each book/marketplace. Anything unfetchable → NO DATA.
4. **Pull ad spend** — ads-log / Ads console for the same period; NO DATA where absent.
5. **Convert currencies** — one dated rate per currency for the report, stated in the report header.
6. **Compute** — per-book P&L, lifetime totals from the ledger, rollups by pen name/niche/month, trend vs prior months.
7. **Flag** — AD-NEGATIVE, DORMANT, DATA GAP; prepare the handoff notes for `uapf-ads-manager` and `uapf-backlist-optimizer`.
8. **Write outputs** — `finance/pnl-[YYYY-MM].md`; append finalized lines to `finance/catalog-ledger.md`.
9. **Report to operator** — headline (catalog net, best/worst movers), the flag list, and every data gap needing operator action.
10. **Late data** — if actuals arrive after the close, append dated adjustment lines to the ledger and issue a revised P&L noting what changed; never silently edit a published month.

## Projections (the one sanctioned exception)

Forward-looking numbers are allowed **only** when explicitly requested (e.g. for catalog planning), and every projected figure is labeled **ESTIMATE** with its method (e.g. "trailing 3-month average"). Projections never enter the ledger and never sit unlabeled beside actuals.

## Key Rules — Do NOT Break

1. **Actuals only — no fabricated or interpolated revenue.** A missing number is NO DATA, never a guess.
2. **Never estimate KENP royalties from a per-page rate.** The Global Fund rate varies monthly; use only the reported payout, and mark unfinalized reads PENDING.
3. **Label every estimate as an estimate.** Projections are marked ESTIMATE with method; they never enter `finance/catalog-ledger.md`.
4. **Never mix BSR-estimated sales with reported actuals in the same table without labels.** Watchlist estimates are market context, not finance data.
5. **Date every currency conversion with the rate used.** No undated or implicit conversions.
6. **Genie never enters credentials.** Dashboard reads require the operator's existing logged-in session; if logged out, stop and ask.
7. **The ledger is append-only.** Corrections are appended as dated adjustments; history is never rewritten.
8. **No book silently omitted.** Every live book appears in every monthly P&L, even if its whole row is NO DATA.
