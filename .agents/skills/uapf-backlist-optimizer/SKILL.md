---
name: uapf-backlist-optimizer
description: Quarterly health sweep of every published Pegasus Press title — metadata freshness, category validity, content staleness, pricing, and BSR trend — producing a prioritized backlist report and second-edition recommendations backed by data.
---

# UAPF Backlist Optimizer

The catalog does not stop earning attention after launch day. This skill is Genie's quarterly maintenance pass over **every published title**, keeping metadata competitive, content current, prices sane, and identifying which books deserve a second edition — and which are quietly dying.

It works from recorded data (WATCHLIST snapshots and METADATA ANALYZER output from **uapf-kdp-niche-specialist**, review data from **uapf-review-monitor**, royalty data from **uapf-royalty-reporter**) and produces recommendations, not silent changes.

## When to Run

| Trigger | Scope |
|---|---|
| Quarterly schedule (default) | Full catalog sweep |
| Operator request ("Genie, sweep the backlist") | Full catalog, or named titles |
| uapf-review-monitor escalates persistent complaints | Targeted check of that title |
| uapf-royalty-reporter flags a sales cliff | Targeted check of that title |

## Per-Book Checks

Run all five checks for every published title, in order.

### 1. Metadata Freshness

1. Re-run keyword opportunity scoring (via the METADATA ANALYZER approach from uapf-kdp-niche-specialist) against the book's current backend keywords, title/subtitle, and description.
2. Compare current scores against the scores recorded at publication (or last sweep).
3. If the market has shifted — new high-opportunity terms, or currently used terms gone cold — draft a refreshed keyword set and/or description.
4. **Any change to a live listing requires operator confirmation.** Present old vs new side by side with the scoring data that justifies each change.

### 2. Category Check

1. Verify each of the book's categories still exists in the KDP/Amazon category tree (Amazon prunes and renames categories regularly).
2. Verify the book actually appears in and is reachable through those categories.
3. If BSR data from watchlist history shows a better-fitting, lower-competition category, propose the move — with the BSR evidence attached.
4. Category changes are live-listing changes: operator confirmation required.

### 3. Content Staleness

Scan the manuscript (and description) for:

| Staleness signal | Example |
|---|---|
| Year markers | "2024 edition," "as of 2023," current-year statistics |
| Dated facts | Prices, laws, versions, records that have changed |
| Dead references | URLs, resources, organizations that no longer exist |
| Outdated standards | Superseded exam formats, guidelines, curricula |

Flag findings for edition refresh; do not silently rewrite content. Small fixes route to **uapf-correction-resume**; accumulated staleness feeds the second-edition framework below.

### 4. Price Check

1. Pull current pricing of the top competitors in the niche (watchlist snapshots plus a fresh look if stale).
2. Recompute royalty per unit at current KDP printing costs.
3. Flag titles priced far off the niche band, or whose margin has eroded below acceptable royalty.
4. Price changes are live-listing changes: operator confirmation required.

### 5. BSR / Sales Trend Classification

Using WATCHLIST snapshot history (uapf-kdp-niche-specialist) and royalty history (uapf-royalty-reporter), classify each title:

| Class | Definition | Default action |
|---|---|---|
| HEALTHY | Stable or improving BSR; steady sales | No action; keep monitoring |
| DECLINING | Sustained BSR worsening over 2+ snapshots / falling sales | Metadata refresh, price review, ads review (uapf-ads-manager) |
| DORMANT | Effectively no rank/sales for a full quarter | Candidate for second edition, repositioning, or deprioritization per uapf-catalog-strategist |

## Second-Edition Trigger Framework

Recommend a **second-edition project** when the accumulated evidence crosses thresholds across three axes:

| Axis | Source | Threshold signal |
|---|---|---|
| Staleness | Check 3 findings, accumulated across sweeps | Multiple dated facts / expired year markers / superseded standards |
| Review complaints | uapf-review-monitor correction tickets and complaint mix | Recurring actionable complaints that patching hasn't resolved |
| Sales decline | Check 5 classification | DECLINING for 2+ quarters, or DORMANT with a still-viable niche |

When two or more axes fire, write the recommendation into the backlist report with all supporting data. An approved second edition **routes back into the production pipeline as a new project** (via the orchestrator), with the old book registered as source material — it is not an in-place patch.

## Output

Write `catalog/backlist-report-[quarter].md` (e.g., `backlist-report-2026-Q3.md`) containing:

1. **Per-book status table** — one row per title: class (HEALTHY/DECLINING/DORMANT), metadata verdict, category verdict, staleness flags, price verdict, second-edition recommendation (Y/N).
2. **Prioritized action list** — ordered by expected impact: operator-confirmation items first (listing changes, price changes, second editions), then autonomous items (correction tickets, watchlist additions).
3. **Data appendix** — the BSR series, keyword scores, and citations backing every recommendation, each with source file and snapshot date.

Reports are cumulative history: never overwrite a prior quarter's report.

## Handoffs

| Finding | Route to |
|---|---|
| Metadata / category / price change approved | uapf-publisher (live-listing update) |
| Small content fixes | uapf-correction-resume → QA → uapf-publisher |
| Second-edition project approved | Production pipeline (new project, old book as source) |
| Portfolio-level positioning questions | uapf-catalog-strategist |
| Underperforming ads on DECLINING titles | uapf-ads-manager |

## Key Rules — Do NOT Break

1. **Live-listing changes always require operator confirmation** — keywords, description, categories, price. Genie proposes; the operator disposes.
2. **Every recommendation cites data** — BSR history with snapshot dates, keyword opportunity scores, competitor prices, review quotes. A recommendation without cited evidence is a hunch, and hunches do not go in the report.
3. **Append-only history.** Never overwrite past backlist reports, watchlist snapshots, or scoring records; each sweep adds to the record.
4. **Never silently rewrite content.** Staleness findings become flags and tickets, not stealth edits.
5. **Second editions are new projects**, routed through the full production pipeline with the old book as source — never in-place mutations of the live book.
6. **Classify every title every sweep.** No book is skipped because it is small or old; DORMANT is a finding, not an omission.
