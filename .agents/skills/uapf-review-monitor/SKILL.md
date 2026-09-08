---
name: uapf-review-monitor
description: Read-only Amazon review intelligence for published Pegasus Press books — captures new reviews, mines complaints into actionable categories, opens correction tickets, and reports rating trends. Never responds to, solicits, or manipulates reviews.
---

# UAPF Review Monitor

Genie's post-publication listening post. This skill periodically reads the Amazon review page of every published Pegasus Press book, records what real readers are saying, converts recurring complaints into concrete correction work, and tracks rating health over time.

This skill is **strictly read-only intelligence**. It observes the market; it never touches it.

## When to Run

| Trigger | Behavior |
|---|---|
| Weekly schedule (default) | Full sweep of every published book's review page |
| Operator request ("Genie, check reviews") | Full sweep, or a single named book if specified |
| After uapf-publisher confirms a book went live | Add the book to the monitored set; first check ~14 days later |
| Before a uapf-daily-standup or backlist sweep needs fresh data | Targeted refresh of stale books only |

## Data Model

All review data lives under `reviews/` and is **append-only**.

| File | Contents |
|---|---|
| `reviews/[book]-reviews.json` | Append-only log of captured reviews: rating, date, review title, review text, capture timestamp, marketplace |
| `reviews/[book]-trend.md` | Rolling rating-trend report (regenerated each sweep; source data never edited) |
| `reviews/correction-tickets/` | One markdown ticket per triggered correction |
| `reviews/last-check.json` | Per-book timestamp of the most recent successful check |

Never edit or delete an existing review record. If a review disappears from Amazon, note the disappearance in a new record — do not remove the original.

## Workflow

1. **Load the monitored set.** Read the published-books list (from the catalog / uapf-publisher records) and `reviews/last-check.json`. Determine which books are due.
2. **Open each book's review page** in the built-in browser. Sort by most recent. Page through until you reach reviews already captured (match on date + title + rating + text prefix).
3. **Capture new reviews.** For each new review record: star rating, review date, review title, full review text, verified-purchase flag if visible, and the capture timestamp. Append to `reviews/[book]-reviews.json`. Never paraphrase into the data file — store the actual text.
4. **Classify each negative review (1–3 stars)** using the complaint taxonomy below. A single review may carry multiple categories.
5. **Run the correction-trigger check** (see below). Open correction tickets where thresholds are met.
6. **Regenerate the rating-trend report** for each checked book: average rating over time, review velocity (reviews/week), rating distribution, and complaint-category mix by month.
7. **Update `reviews/last-check.json`** and report the sweep summary to the operator (new reviews, notable ratings, tickets opened).

## Complaint Taxonomy

| Category | Type | Examples |
|---|---|---|
| TYPOS-ERRORS | Actionable | Spelling, grammar, duplicated text, wrong numbering |
| FORMATTING-LAYOUT | Actionable | Broken tables, margins, tiny fonts, TOC errors, image placement |
| MISSING-CONTENT | Actionable | "No answer key," "chapter promised in description absent," thin sections |
| FACTUAL-ERRORS | Actionable (high severity) | Wrong facts, outdated standards, incorrect answers |
| COVER-EXPECTATION | Actionable | Book content doesn't match cover/title/description promise |
| PRINT-QUALITY | Actionable (route to print settings review) | Faded ink, bleed problems, binding — verify whether it's our file or Amazon's printer |
| TASTE | Non-actionable | "Not my style," disagreement with approach |
| SHIPPING-FULFILLMENT | Non-actionable | Late delivery, damaged in transit, wrong item shipped |

Non-actionable complaints are still recorded and counted in trend reports — they are simply never grounds for a correction ticket.

## Correction Trigger

A correction ticket is opened when **either**:

1. The **same actionable category** appears in **2 or more reviews** for the same book, OR
2. **Any FACTUAL-ERRORS complaint appears even once.**

### Correction Ticket Workflow

1. Create `reviews/correction-tickets/[book]-[date]-[category].md` containing:
   - Summary of the complaint in plain language
   - **Verbatim quotes of every triggering review** (with date and rating) — tickets must cite the actual review text, never a summary alone
   - Affected sections/chapters, as best as the review text allows you to localize
   - Recommended fix and severity (FACTUAL-ERRORS = high)
2. Hand the ticket to **uapf-correction-resume**, which locates and fixes the manuscript issue through the production pipeline.
3. After the fix passes QA (uapf-release-qc / chapter gates as applicable), hand the corrected files to **uapf-publisher** for re-upload.
4. **Re-upload requires explicit operator confirmation.** Present the ticket, the fix diff summary, and the QA result; do not trigger the KDP re-upload until the operator says yes.
5. Record ticket status transitions (OPEN → IN-FIX → QA-PASSED → AWAITING-OPERATOR → RE-UPLOADED) by appending to the ticket file.

## Rating-Trend Report

Per book, each sweep regenerates `reviews/[book]-trend.md` with:

- **Average trend** — running average rating, month over month, with direction arrow
- **Velocity** — new reviews per week; flag sudden spikes or dead stops
- **Complaint mix** — actionable vs non-actionable share, and category breakdown over time
- **Watch flags** — e.g., average dropped below 4.0, or actionable share exceeded 30%

Trend outputs feed uapf-daily-standup, uapf-backlist-optimizer (second-edition triggers), and uapf-kdp-niche-specialist.

## Amazon TOS Boundary — Explicit

This skill **never**:

- Responds to, comments on, or votes on any review
- Solicits reviews from anyone, by any channel
- Contacts, identifies, or attempts to identify reviewers
- Reports reviews to Amazon or attempts to have reviews removed
- Interacts with the listing in any way beyond reading publicly visible pages

Reading public review pages for intelligence is permitted; every form of review manipulation violates Amazon's Community Guidelines and KDP terms and risks account termination. If the operator asks for any of the above, refuse and explain this boundary.

## Key Rules — Do NOT Break

1. **Read-only.** Never respond to, solicit, or manipulate reviews, and never contact reviewers — no exceptions, including operator requests.
2. **Append-only data.** Never edit or delete captured review records; corrections and disappearances are logged as new entries.
3. **Never fabricate.** No invented reviews, ratings, quotes, or trend numbers. If a page could not be read, record the failure — do not fill the gap.
4. **Tickets cite verbatim review text.** A correction ticket without the actual triggering quotes is invalid.
5. **Trigger thresholds are fixed:** 2+ reviews with the same actionable complaint, or 1 factual-error complaint. Do not open tickets on weaker evidence; do not ignore threshold hits.
6. **Re-uploads require operator confirmation.** The pipeline may fix and QA autonomously, but nothing goes back to KDP without an explicit yes.
7. **Non-actionable complaints never trigger corrections** — but they are always recorded and counted.
