---
name: uapf-kdp-niche-specialist
description: KDP market intelligence engine working like Publisher Rocket, BookBeam, and Helium 10 — niche discovery and validation, keyword research with demand scoring, competition analysis, BSR-to-sales estimation, category research, seasonality, and the 7 backend keywords. Use standalone to research a niche before choosing a title, or auto-invoked during Phase 0 to build the competitive frame and KDP metadata package for the current title.
---

# UAPF KDP Niche Specialist​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Market-research engine for Amazon KDP. Replaces Publisher Rocket / BookBeam / Helium 10 workflows with live research through WebSearch, WebFetch, and the built-in browser on the target Amazon marketplace.

## Modes

| Mode | Trigger | Output |
|---|---|---|
| **NICHE DISCOVERY** | Operator asks "find me a niche", "what should I publish next", or gives a broad topic | Ranked niche opportunity report |
| **NICHE VALIDATION** | Operator gives a specific niche/topic before committing to a title | Go / no-go verdict with demand, competition, and profitability scores |
| **TITLE INTELLIGENCE** | Auto-invoked in Phase 0 after `uapf-trademark-checker` clears the title | Competitive frame + keyword package + category picks for this book |
| **KEYWORD PACKAGE** | Metadata stage (or operator request) | 7 backend keyword slots + title/subtitle keyword recommendations |
| **ADS KEYWORDS** | Operator request, or after KEYWORD PACKAGE | 100–300 keyword Amazon Ads campaign list |
| **PRICE CHECK** | Auto during TITLE INTELLIGENCE; standalone anytime | Royalty table per price point; profitable-price verdict |
| **WATCHLIST** | Operator request ("track this niche/competitor") | Snapshot file + diff report vs. prior snapshots |
| **ARBITRAGE SCAN** | Operator request | Marketplace-by-marketplace opportunity table for a proven niche |
| **METADATA ANALYZER** | Auto-activates when the book is COMPLETED (final DOCX passed release QC); also on operator request | Professional book description + 7 backend keywords + 3 best categories, delivered as a separate DOCX |

All modes work on the LOCKED marketplace (default Amazon.com). Never change the operator's title — this skill informs positioning; it never renames anything.

---

## Core Method 1 — Keyword Research (Publisher Rocket pattern)

For each seed keyword (from the title, niche, or operator):

1. **Autocomplete harvest:** query Amazon search suggestions for the seed and each letter appendix ("keto cookbook a", "keto cookbook b", …) via the built-in browser or web search. Amazon's autocomplete IS live buyer demand — every suggestion is a real search phrase.
2. **Demand proxies (score each keyword 1–10):**
   - Autocomplete presence and position (appears early = higher volume)
   - Number of results returned for the exact phrase on Amazon ("under 1,000 results" = low competition supply)
   - Google Trends direction for the phrase (rising/flat/declining)
   - Presence of ads on the search results page (advertisers = commercial demand)
3. **Competition proxies (score each keyword 1–10, lower = easier):**
   - Average BSR of the top 5 organic results for the phrase
   - Average review count of the top 5 (under 150 reviews = beatable; 1,000+ = entrenched)
   - How many of the top 10 have the phrase in their TITLE (exact-match titles = harder)
   - Age of top results (all recent = active niche; all old = stale but rankable)
4. **Opportunity Score** = demand score × (11 − competition score). Report the top keywords ranked by opportunity.

## Core Method 2 — BSR-to-Sales Estimation (BookBeam pattern)

Convert Best Sellers Rank to estimated daily sales using the standard KDP estimation bands (books category, adjust per marketplace size):

| BSR (Books) | Est. sales/day |
|---|---|
| 1–100 | 500+ |
| 100–1,000 | 100–500 |
| 1,000–5,000 | 40–100 |
| 5,000–10,000 | 15–40 |
| 10,000–25,000 | 5–15 |
| 25,000–50,000 | 2–5 |
| 50,000–100,000 | 1–2 |
| 100,000–300,000 | 0.3–1 |
| 300,000+ | <0.3 |

- State these are ESTIMATES with real variance — never present as exact figures.
- For smaller marketplaces (.de, .co.uk, .ca, .com.au) divide bands by the marketplace factor (~3–5× smaller than .com).
- **Niche monthly revenue estimate** = Σ (top 10 competitors' est. daily sales × 30 × price × 0.6 royalty factor). Report as a band, not a number.

## Core Method 3 — Competition Analysis (Helium 10 pattern)

For the top 10 books in the niche/keyword, build the competitor table:

```
| # | Title (truncated) | Author | BSR | Est. sales/day | Price | Reviews | Rating | Pages | Pub date | Cover grade |
```

Then extract the **gap analysis**:
- **Review gaps:** what 1–3 star reviews complain about (too short, no images, outdated, poor formatting, missing topics) — these become the book's differentiators
- **Content gaps:** topics the bestsellers skip (compare their Look Inside TOCs)
- **Format gaps:** no large print edition? no workbook companion? no full-color option?
- **Price gaps:** clustering at $12.99? Room at $16.99 premium or $9.99 undercut?
- **Cover gaps:** dated/amateur covers in the top 10 = opportunity

## Core Method 4 — Category Research (Publisher Rocket pattern)

1. Identify 10–15 candidate Amazon browse categories for the niche (crawl category trees from competitor listings' "Best Sellers Rank" breadcrumbs).
2. For each category record: the #1 book's BSR, the #20 book's BSR, and the #100 book's BSR.
3. **Sales-to-#1 estimate:** the #1 book's BSR converted through the sales table = daily sales needed to top the category.
4. Rank categories by "reachability": categories whose #1 needs <10 sales/day are winnable launch categories; categories whose #20 needs <3 sales/day give a lasting bestseller badge shot.
5. Recommend 3 categories: one reachable (badge play), one mid-competitive (relevance), one high-traffic (visibility). KDP allows 3 category selections.

## Core Method 5 — Seasonality & Trend Check

- Google Trends on the niche's core phrase: 12-month and 5-year view — rising, seasonal, evergreen, or declining
- Seasonal niches (gift books, holiday, gardening, tax, back-to-school): report the demand window and the publish-by date (60+ days before peak for reviews to accumulate)
- Declining trends are a NO-GO flag in validation mode unless the operator overrides
- **Publish-by calendar:** for every seasonal niche in a report, compute the concrete publish-by date (peak start − 60 days) and list it — e.g., "Christmas crafts → publish by Oct 1; garden planners → publish by Jan 15"

## Core Method 6 — Amazon Ads Keyword Generator (Publisher Rocket AMS pattern)

Build a 100–300 keyword campaign list from four sources:

1. **Autocomplete at scale:** run the completion API over the seed + every letter appendix (a–z) + phrase extensions ("for", "over", "with", "beginners", "seniors", audience words). Dedupe.
2. **Competitor title/subtitle mining:** tokenize the top 20 competitor titles and subtitles into 2–4 word phrases; keep phrases appearing in 2+ titles (proven buyer language).
3. **Also-bought titles:** harvest book titles from competitors' carousels (Method 8) and tokenize the same way.
4. **Author names of top competitors** — top ad targets on Amazon (buyers searching an author see your ad). Competitor AUTHOR names are allowed in ADS targeting (unlike backend keywords, where they are prohibited).

Output format (ready to paste into an Amazon Ads campaign):
```
ADS KEYWORD LIST — [title] — [count] keywords — [date]
BROAD-MATCH CORE (20–40): [the opportunity-scored winners]
LONG-TAIL EXACT (50–150): [autocomplete + title-mined phrases]
AUTHOR/ASIN TARGETS (20–50): [competitor authors + ASINs for product targeting]
NEGATIVE KEYWORDS: [irrelevant overlap terms to exclude — e.g., "dvd" for a book campaign]
```
Written to `phase0/ads-keywords.md` in the project folder.

## Core Method 7 — Royalty & Price Calculator (KDP economics)

Compute per-format margin at candidate price points BEFORE committing to a format/length:

**Paperback printing cost (US marketplace, 2024+ rates — verify current rates when they matter):**
- B&W: $0.85 fixed + $0.012 × page count (109+ pages)
- Premium color: $0.89 fixed + $0.065 × page count (72+ pages) — was "standard color" tiers; verify current
- Royalty = (list price × 0.60) − printing cost
- Hardcover: $5.65 fixed + $0.012 × pages (B&W)

**eBook:** 70% royalty in the $2.99–$9.99 window (minus ~$0.10 delivery fee), 35% outside it.

Output table per candidate format:
```
PRICE CHECK — [pages] pages, [trim], [B&W/color]
| Price | Printing cost | Royalty | Margin % | Competitor position |
| $12.99 | $x.xx | $x.xx | xx% | undercuts median |
| $14.99 | ... | ... | ... | at median |
| $16.99 | ... | ... | ... | premium |
VERDICT: [profitable at competitive price? Color viable or B&W required? Page-count ceiling for target price?]
```
**Full-color books (cookbooks, travel, children's, crafts):** run this FIRST — color printing costs kill many niches at competitive price points; the niche skill's page target must respect the margin verdict.

## Core Method 8 — Also-Bought / Carousel Mining (adjacent-niche discovery)

From each top-10 competitor's product page, harvest every book title + ASIN from the recommendation carousels ("Customers also bought", "Products related to this item", "Customers who viewed this item also viewed", sponsored carousels included but labeled).

- **Adjacent niches:** cluster harvested titles by topic; a cluster that is NOT the seed niche = an adjacent niche the same buyers purchase → feed into NICHE DISCOVERY ranking.
- **Series signals:** repeated author/brand names across carousels = the niche's dominant publishers; their catalogs show what a winning series looks like.
- **Bundle signals:** products co-appearing (chart + book, journal + guide) = format-bundle opportunities.

## Core Method 9 — Reverse-ASIN Lookup (Helium 10 Cerebro pattern)

Given a competitor ASIN, reconstruct their keyword strategy from public data:

1. Fetch the product page: extract title, subtitle, series name, byline, categories (BSR breadcrumbs), and editorial/A+ section text.
2. Tokenize into candidate keywords (2–4 word phrases).
3. For each candidate, search Amazon for the phrase and record whether the target book ranks on page 1 — a page-1 rank means the keyword is working for them.
4. Output their working keywords ranked by our opportunity score → merge into KEYWORD PACKAGE and ADS KEYWORDS candidates.

## Core Method 10 — Format & KU Gap Analysis

For the top 10 competitors record: Kindle? Paperback? Hardcover? Spiral? Audiobook? Large print edition? Kindle Unlimited enrolled? A+ content present?

```
FORMAT COVERAGE — [niche]
| Format | Covered by | Gap? |
| Large print | 1/10 | YES — senior niche without large print is a real gap |
| Spiral-bound | 2/10 | possible premium format play |
| Audio | 0/10 | open |
| A+ content | 3/10 | merchandising edge available |
| KU enrollment | 8/10 | KU expected in this niche |
```
Format gaps feed the niche skill's format-profile decision and the KDP positioning stage. Autocomplete format hints ("...chart", "...large print", "...spiral") corroborate gaps with demand evidence.

## Core Method 11 — Series Opportunity Detector

- Detect series membership in the top 20 ("Part of: [series] (N books)" on product pages).
- Report: % of top books in a series, the largest series' size and breadth of topics, and whether standalone books still rank.
- **Verdict:** SERIES-DRIVEN niche (plan a multi-book brand from book 1: shared design system, cross-promotion in back matter, consistent byline) vs STANDALONE-VIABLE.
- Feeds catalog planning: a series-driven verdict means Phase 0 should reserve series-compatible titling and the interior color-scheme rotation should brand-match across the planned series.

## Core Method 12 — Competitor Watchlist & Review Velocity (BookBeam tracker pattern)

- **Snapshot:** save per-competitor {date, BSR, ratings count, rating avg, price, format list} to `watchlists/[niche]-watchlist.json` (project folder or the operator's UAPF_Projects root for cross-project niches).
- **Diff on re-run:** compare against every prior snapshot:
  - **Review velocity** = Δ ratings ÷ days elapsed. At typical review rates (~1 review per 100–200 sales), velocity × 150 ≈ monthly sales cross-check for the BSR estimate.
  - BSR trend (improving/declining), price changes, new formats added.
- **New-release radar:** re-run the niche search sorted by publication date; flag new entrants ranking fast (a book <90 days old with a Best Seller badge = the niche still rewards new entries — strong GO signal).
- Recommend a re-run cadence (weekly for pre-launch niches, monthly for tracking).

## Core Method 13 — International Arbitrage Scanner

For a niche proven on the home marketplace, check each candidate marketplace (.de, .co.uk, .fr, .it, .es, .ca, .com.au, .co.jp):

1. Translate the core keyword natively (not literally — use the phrase local buyers would type; verify with that marketplace's autocomplete API variant).
2. Record: result count, top-3 review counts, top-3 BSR (convert with the marketplace-size factor).
3. **Opportunity flag:** proven demand at home + thin supply abroad (few results, low review moats, weak covers) = translation/localization opportunity for the LANG-[code] pipeline.

```
ARBITRAGE SCAN — [niche] — [date]
| Marketplace | Local keyword | Results | Top review moat | Verdict |
| amazon.de | [German phrase] | 214 | 89 ratings | OPEN — strong opportunity |
| amazon.co.uk | ... | ... | ... | ... |
```
Feeds the multi-marketplace session planning and the LANG modifier decision.

---

## Core Method 14 — Metadata Analyzer (post-completion deliverable)

**Activates automatically when the book is completed** — i.e., the final manuscript DOCX exists and has passed release QC. Also runnable on operator request for an already-finished book.

Pulls from the records this skill already produced during Phase 0 (`phase0/kdp-market-intelligence.md`, `phase0/ads-keywords.md`, the trademark clearance report) plus the FINISHED manuscript itself (TOC, chapter titles, verified counts, differentiators actually delivered). If the Phase 0 records are missing or older than 30 days, re-run the needed research live before writing metadata — never write metadata from stale or absent data.

### 14.1 — Professional Book Description
Structure (KDP description field, 4,000 char max, using KDP-supported HTML tags `<b>`, `<i>`, `<br>`, `<ul>`/`<li>`, `<h4>`–`<h6>`):

1. **Hook line** (bold) — the buyer's problem or desire, mirroring the niche's proven buyer language from the keyword research
2. **Empathy/context paragraph** — speaks to the target reader identified in Phase 0 (or the gatekeeper for children's books)
3. **Promise paragraph** — what the book delivers, drawn from the TOC actually built
4. **Bulleted "Inside you'll discover" list** (5–8 bullets) — the strongest differentiators from the gap analysis THAT THE BOOK ACTUALLY CONTAINS; every verifiable count (recipes, exercises, questions, facts) stated exactly per Hard Rule 3
5. **Differentiation line** — what competitors miss (from review-gap mining), phrased positively, never naming competitors
6. **Audience line** — "Perfect for [audiences]" using searched phrases
7. **Call to action** — buy-button line appropriate to the niche's register

Compliance battery: no misleading claims, no guaranteed outcomes, no "bestseller/free/new", no competitor names or trademarks, no raw superlatives without verification, claims match the actual manuscript, risk-regime language rules applied (R2 health, R3 finance, R4 sensitive).

### 14.2 — Backend Keywords (final)
The 7 slots, refreshed against the FINISHED book: re-rank the Phase 0 keyword list by opportunity score, drop any term the manuscript doesn't actually support, cross-check against the trademark report, apply all KDP keyword rules (no title/subtitle repeats, no competitor names, no misleading terms, ≤50 chars per slot, mixed phrase clusters).

### 14.3 — Best Categories (final)
The 3 category picks from Method 4, re-verified live at completion time (category trees change): confirm each still exists via a live listing's breadcrumb, confirm reachability with current BSR data, and state the sales-to-#1 estimate per pick. One badge play, one relevance pick, one visibility pick.

### 14.4 — DOCX Deliverable
Produce a SEPARATE Word document — never inside the manuscript:

- **Filename:** `[BookTitle]_KDP_Metadata.docx` in the project folder
- **Machine-readable twin (required, 2026-08-15):** alongside the DOCX, write
  `publish_manifest.json` in the project folder — the single source of truth
  every platform upload reads first (uapf-publisher consumes it). Fields:
  exact_title, subtitle, author_pen_name, language, marketplace, description,
  backend_keywords (array of 7), categories (array), trim_size, page_count,
  interior_type, paper, bleed, price_recommendation (per marketplace where
  computed), files {manuscript_pdf, manuscript_docx, cover_wrap_pdf,
  aplus_dir}, ai_disclosure, isbn (null until assigned), series (null or
  {name, number}). Values are the FINAL approved ones, identical to the DOCX;
  file paths must exist on disk at write time. A book is not reported
  finished until BOTH the metadata DOCX and publish_manifest.json exist.
- **Contents, in order:**
  1. Title block — book title, subtitle, byline, marketplace, date generated
  2. BOOK DESCRIPTION — the formatted description exactly as it should read on Amazon, followed by a plain-text copy-paste block with the HTML tags visible for direct pasting into the KDP description field
  3. BACKEND KEYWORDS — a 7-row table (slot number, keyword string, character count)
  4. CATEGORIES — the 3 picks with full browse paths and reachability notes
  5. METADATA COMPLIANCE CHECKLIST — each compliance rule with pass status
  6. SOURCE NOTES — dates of the market data used, and what was re-verified live
- **Formatting:** Times New Roman, clean professional layout, headings styled, tables bordered — the operator should be able to open it and paste each field into KDP without edits
- Build with python-docx (or docx-js per environment); verify the file exists and report its absolute path. Never claim the DOCX exists unless it was actually written.



### NICHE DISCOVERY report
```
NICHE OPPORTUNITY REPORT — [broad topic] — [marketplace] — [date]
1. [niche] | Opportunity: [score] | Demand: [x/10] | Competition: [x/10] | Est. niche revenue: [$band/mo] | Season: [evergreen/seasonal] | Verdict: [STRONG/MODERATE/WEAK]
   Why: [one line — the gap that makes this winnable]
2. ...  (5–10 niches, ranked)
RECOMMENDED ENTRY: [niche] — [angle that exploits the identified gap]
```

### NICHE VALIDATION verdict
```
NICHE VALIDATION — [niche] — [marketplace] — [date]
Demand: [x/10 + evidence]     Competition: [x/10 + evidence]
Est. top-10 revenue: [$band/mo]     Trend: [rising/evergreen/seasonal/declining]
Entry difficulty: [reviews needed to compete, content bar, format bar]
VERDICT: GO / GO WITH ANGLE / NO-GO
Angle (if GO): [the specific differentiation that wins]
```

### TITLE INTELLIGENCE package (Phase 0 auto-mode)
Feeds directly into the niche skill's Phase 0 and the KDP positioning stage:
- Competitor table (top 10) with gap analysis
- Page-count and price band recommendation from competitor medians — validated by the PRICE CHECK royalty table (Method 7): the recommended page count and price must yield a positive, competitive margin for the required ink type
- 3 category recommendations with reachability data
- Keyword list ranked by opportunity score
- Differentiators to build into the TOC (from review-gap mining)
- Format & KU gap table (Method 10) and series verdict (Method 11)
- Initial watchlist snapshot saved (Method 12) so launch-time re-runs can diff
Written to `phase0/kdp-market-intelligence.md` in the project folder.

### KEYWORD PACKAGE (metadata stage)
```
7 BACKEND KEYWORD SLOTS (each ≤50 chars, no commas needed — phrases mix):
1. [phrase cluster]  ... 7. [phrase cluster]
TITLE/SUBTITLE KEYWORDS: [which cleared keywords belong in the subtitle]
RULES APPLIED: no title/author repeats, no competitor names, no "free/bestselling/new", no misleading terms, no trademark terms (cross-checked against uapf-trademark-checker report)
```

---

## Core Method 15 — Amazon A10 Algorithm Model

Every recommendation this skill makes must be A10-aware. A10 (the successor to A9) changed what ranks a book in Amazon search — encode these weightings into keyword, metadata, category, and launch advice:

### What A10 rewards (in rough order of weight)

1. **Organic sales velocity & conversion rate** — the heaviest signal. A book that converts searchers into buyers at a high rate climbs; a book with traffic but no conversion sinks. CONSISTENT daily sales beat one-day spikes — this shapes launch pacing advice (steady promo drip > single blast).
2. **Relevance** — exact-phrase match in title/subtitle is the strongest indexing signal, then backend keywords, then description text (A10 indexes description terms more than A9 did). Front-load the highest-opportunity phrase in the subtitle.
3. **Click-through rate from search results** — determined by cover thumbnail, title readability at thumbnail size, price vs neighbors, review count/stars. A listing that gets impressions but no clicks loses rank. This is why the gap analysis grades covers and price position.
4. **External (off-Amazon) traffic** — A10 weights it substantially MORE than A9. Traffic from Pinterest, YouTube, email lists, blogs, and social that lands on the listing and converts is a rank accelerator. Launch plans should include at least one external channel.
5. **Customer behavior signals** — engagement on the listing: add-to-carts, wishlist adds, Look Inside opens, low bounce. A+ content and a strong Look Inside sample (front matter + chapter 1 quality) directly feed this.
6. **Seller/author authority** — catalog depth under a byline, overall rating health, account longevity. Series and consistent pen-name catalogs (see uapf-pen-name-manager) compound authority; scattered one-offs don't.
7. **Impressions breadth** — presence in also-boughts, "related products", and category carousels. Category placement and early sales in reachable categories seed these placements.

### What A10 demoted (vs A9)

- **PPC weight is REDUCED:** ads still generate sales (which count), but ad-driven rank decays fast when ads stop. Treat ads as an organic-rank igniter, never the ranking strategy itself — sustained organic conversion holds position. (uapf-ads-manager applies this: watch organic rank alongside ad metrics; a book whose rank collapses when ads pause has an A10 relevance/conversion problem, not an ads problem.)
- **Keyword stuffing and irrelevant-keyword indexing** — A10 punishes listings that attract clicks but not conversions on a phrase. Never recommend a high-volume keyword the book can't genuinely convert on.

### How A10 changes each output of this skill

| Output | A10 rule applied |
|---|---|
| KEYWORD PACKAGE | Rank by opportunity score AND conversion plausibility — the book must genuinely satisfy the phrase's buyer intent, or ranking on it hurts long-term |
| Subtitle recommendations | Highest-converting exact phrase front-loaded; readable at thumbnail size |
| METADATA ANALYZER description | Written to convert — A10 indexes description terms AND conversion feeds rank; the description is a ranking asset, not just copy |
| Category picks | Reachable categories first — early category-bestseller placement seeds carousel impressions |
| TITLE INTELLIGENCE | Cover-grade and price-position columns exist because CTR is a ranking input; flag CTR risks explicitly |
| Launch advice (to uapf-launch-manager) | Steady-velocity pacing, at least one external-traffic channel, Look Inside quality check before launch |
| Ads advice (to uapf-ads-manager) | Ads ignite, organic sustains — pair every campaign recommendation with the organic conversion checklist |

## Data Collection Rules

- Use the built-in browser (`mcp__Claude_Browser__*`) for Amazon pages when logged-in browsing is available; WebSearch/WebFetch otherwise. Never fabricate a BSR, review count, or price — if a data point can't be read, mark it `n/a`.
- **PROVEN autocomplete method (tested 2026-08-03):** the in-page suggestion flyout may not render in the browser pane. Instead, from an amazon.com page run via `javascript_tool`:
  ```javascript
  const url = 'https://completion.amazon.com/api/2017/suggestions?limit=11&prefix=' + encodeURIComponent(prefix)
    + '&suggestion-type=KEYWORD&page-type=Search&alias=stripbooks&site-variant=desktop&version=3&event=onKeyPress&wc=&lop=en_US&mid=ATVPDKIKX0DER&plain-mid=1&client-info=amazon-search-ui';
  const d = await (await fetch(url)).json();
  d.suggestions.map(s => s.value)  // live buyer search phrases
  ```
  Works with letter-appendix and phrase-extension prefixes. Must be executed from an amazon.com page context (CORS).
- **PROVEN product-page extraction (tested 2026-08-03):** BSR, category ranks (`#N in [category]`), page count, publication date, rating, and author are all extractable from `document.body.innerText` with regex on the product page. Prices display in the local currency of the browsing IP — convert and label the conversion.
- Date-stamp every report; BSR data is volatile and expires within days.
- All estimates are labeled as estimates. Never promise sales or revenue to the operator.
- Respect the marketplace lock: research .de niches on amazon.de in German keywords, etc.

## Pipeline Integration

- **Phase 0:** `uapf-phase0-router` invokes TITLE INTELLIGENCE mode right after `uapf-trademark-checker` clears the title. The exact-title competitor list from the trademark checker seeds the competitor table.
- **TOC design:** the content-gap and review-gap findings are handed to the niche skill so promised differentiators actually appear in the TOC.
- **Metadata stage:** KEYWORD PACKAGE mode supplies the 7 backend slots and category picks to `uapf-kdp-assets` / KDP positioning.
- **Book completion:** METADATA ANALYZER (Method 14) auto-activates when the final manuscript passes release QC — it generates the description, final backend keywords, and re-verified categories, and delivers `[BookTitle]_KDP_Metadata.docx` alongside the manuscript. The completion report must list this DOCX as a deliverable.
- **Standalone:** the operator can invoke any mode directly at any time ("validate the chair yoga for seniors niche on Amazon US", "generate the metadata docx for [finished book]").

## Key Rules — Do NOT Break

1. NEVER change or suggest changing the operator's locked title — this skill informs positioning only.
2. NEVER fabricate market data. Unreadable data points are `n/a`, and the report says so.
3. All sales/revenue figures are labeled ESTIMATES with bands, never exact claims.
4. Keyword recommendations must pass the trademark screen — cross-check distinctive terms against the `uapf-trademark-checker` report before placing them in metadata.
5. Backend keywords follow KDP rules: no competitor names, no "free/best-seller/new release", no misleading claims, no terms already in title/subtitle.
6. Category recommendations must be real browse categories verified from live listings, not guessed paths.
7. Date-stamp every report; flag any data older than 7 days as stale before reuse.
8. Competitor author names may be used as ADS TARGETS only — never in backend keywords, title, subtitle, or description.
9. KDP printing-cost rates change — when a margin verdict is decision-critical (full-color niches especially), verify the current rate card live before locking format and price.
10. Watchlist snapshots are append-only history — never overwrite prior snapshots; diffs need them.
11. Arbitrage keywords must be natively translated buyer phrases (verified via the target marketplace's autocomplete), never literal dictionary translations.
12. Review velocity is a cross-check, not a primary estimate — report it alongside the BSR estimate, and flag when the two disagree materially.
13. The metadata DOCX is a SEPARATE file, never merged into the manuscript. Every claim and count in the description must match the FINISHED book exactly — the description is written from the manuscript that exists, not the plan.
14. METADATA ANALYZER never runs on an incomplete book — final DOCX must exist and have passed release QC (unless the operator explicitly requests an early draft, which is then labeled DRAFT in the file).
15. All ranking advice follows the A10 model (Method 15): conversion-plausible keywords only, ads as igniter never as strategy, steady velocity over spikes, external traffic in every launch plan.

## INTELLIGENCE UPGRADE (2026-08-15) — Methods 16 to 26

The upgrade turns the pattern library above into COMPUTED intelligence.
`market_math.py` (this folder) is the deterministic engine: bsr-sales,
print-cost, margin, niche-score, kw-difficulty. Sales figures are always
labeled ESTIMATES. EXTENSIVE DATA LAW: every mode collects the FULL dataset
(minimum 20 competitors for validation/title intelligence, top 10 fully
field-complete: title, subtitle, ASIN, BSR, price, page count, format,
reviews, rating, pub date, publisher type, cover style, A+ presence), and
every mode saves BOTH a human DOCX/report AND a machine-readable JSON twin
in the project research folder (or state/market_intel/ for non-project runs).
Raw page snapshots used for numbers are kept as production records.

### Method 16 — Quantified Sales & Revenue Model
For every competitor row, run market_math.py bsr-sales (their BSR, the
marketplace, their price) and add estimated units/day, units/month, and
gross revenue/month. Sum the top 10 for TOTAL NICHE REVENUE. Median and
mean both reported. Every table that shows a BSR must show the estimate
columns beside it.

### Method 17 — Composite Niche Score (A to F verdict)
After collecting the dataset, compute market_math.py niche-score from: the
top-10 median BSR, top-10 average review count, indie share of the top 10,
new entrants in the last 90 days, median price, and typical page count/ink.
NICHE VALIDATION now ends with the letter grade, the five component scores,
and the royalty-at-median-price figure. A grade of D or F requires an
explicit operator override to proceed to production.

### Method 18 — Keyword Difficulty Engine
For each candidate keyword: harvest Amazon autocomplete expansions (seed +
space + each letter a-z, collected in the browser), then for the keyword's
own results page record top-10 average BSR, average reviews, title density
(how many top-10 titles contain the exact phrase), and exact-title matches.
Run market_math.py kw-difficulty for the 0-100 score and band. Deliverable:
keyword_sheet.json + DOCX table ranked by opportunity (volume proxies vs
difficulty), minimum 30 scored keywords for a KEYWORD PACKAGE run.

### Method 19 — Category Intelligence
Map every plausible KDP category path for the book. For each: record the
current #1 book's BSR (the badge threshold), the #10 book's BSR (top-10
entry threshold), and compute the estimated sales/day needed for each via
bsr-sales. Flag GHOST categories (thresholds beatable at the book's
projected rank). Deliverable: category_intel.json + the 3 picks justified
by threshold math, not vibes.

### Method 20 — Seasonality Radar (niche level)
During validation, cluster the top 40 results' publication dates and review
spikes by month. Classify the niche: EVERGREEN, SEASONAL (name the peak
months), or EVENT-DRIVEN. For seasonal niches output a launch calendar:
manuscripts complete 10 weeks before peak, published 6 weeks before peak
(review runway). The classification is stored in the niche's JSON twin.

### Method 21 — SEASONAL KEYWORD TRACKER (state-backed, over time)
Tracks specific keywords month over month to catch seasonal demand waves.
- Commands: "Genie, track seasonal keyword [kw]" (add), "Genie, untrack
  seasonal keyword [kw]", "Genie, seasonal keywords report".
- Storage: state/keyword_seasonal/<slug>.json per keyword:
  { keyword, marketplace, added, snapshots: [ { date, autocomplete_variants,
  top10_avg_bsr, top10_median_price, top10_avg_reviews, new_releases_90d,
  badge_holder_bsr } ], classification, peak_months, notes }
- Cadence: snapshot each tracked keyword MONTHLY (piggybacking the weekly
  review sweep's browser session; a keyword is snapshotted if its last
  snapshot is 28+ days old). Never fabricate a snapshot; skipped months
  stay absent.
- Classification (after 3+ snapshots): compare top10_avg_bsr month over
  month; a 2x or greater seasonal swing marks SEASONAL with peak months
  where BSR is lowest; steady = EVERGREEN; single spike = EVENT. Also seed
  the obvious lexicon immediately (christmas, halloween, easter, summer,
  planner-year, valentine, thanksgiving, back to school, new year) with
  their known peaks, refined by data as snapshots accrue.
- Report: table of tracked keywords with trend arrows, classification,
  peak months, weeks-until-peak, and a PRODUCE-NOW flag when the 10-week
  manuscript lead time intersects an approaching peak. The standup surfaces
  PRODUCE-NOW flags automatically.

### Method 22 — Review-Gap Mining (complaints become the TOC)
For the top 5-8 competitors, read their critical reviews (1-3 star, newest
50 or all if fewer). Extract recurring complaints and unmet needs into
complaint_map.json: { complaint, frequency, example_quotes (short,
non-identifying), which_competitors }. Hand the map to
uapf-content-architecture: every high-frequency complaint must map to a
chapter, section, or feature of the new book's TOC, recorded in the TOC
rationale ("solves complaint #3"). This is the differentiation engine: the
market's own dissatisfaction designs the book. Quotes stay internal
research records; never quoted in the manuscript.

### Method 23 — Profit-First Filter (margin before approval)
Before any niche or title is approved: market_math.py margin at the niche's
median price with the planned page count, ink, and trim. Royalty under
$2.00/sale = THIN (flag, suggest price/pages/ink adjustments); at or below
$0 = LOSS (hard flag; color-interior margin traps named explicitly). The
margin verdict appears in NICHE VALIDATION, TITLE INTELLIGENCE, and PRICE
CHECK outputs. Verify live KDP print rates before a FINAL pricing decision.

### Method 24 — Localization Arbitrage 2.0 (pipeline-connected)
Extends Method 13: when an EN top seller has no equivalent on DE/FR/ES/IT
(search the translated head terms; require both absence of a direct
equivalent AND local demand signals), write the opportunity to
state/market_intel/localization_queue.json with the source niche's full
dataset. On operator approval, the entry feeds uapf-localization (for our
own catalog books) or the normal pipeline (for a fresh localized original).
Never translate or imitate a specific competitor's book; the opportunity is
the NICHE in that language, produced original per house law.

### Method 25 — Own-Catalog Learning Loop (private data moat)
Every published book gets state/catalog_performance/<asin>.json: launch
date, niche, keywords used, category picks, price, and weekly snapshots of
BSR, reviews, and (from KDP reports when the operator shares them) actual
units. ACTUALS-ONLY law applies: real numbers or none. Uses: (a) calibrate
the BSR curve — when actuals diverge from bsr-sales estimates, record the
observed ratio and apply it as a stated calibration factor in future
estimates; (b) score our own keyword and category picks against outcomes;
(c) feed niche-score with house-specific evidence ("we already rank in
adjacent niche X"). The loop makes every launch smarter than the last.

### Method 26 — Rising-Niche Alerts + Saturation Urgency
WATCHLIST upgrade. Weekly sweep (with the review sweep): for each watched
niche/category record new releases this week, their opening BSRs, and
Movers & Shakers appearances. Compute: RISING (accelerating demand,
improving BSRs among new entrants) and SATURATION URGENCY 0-100 (rate of
credible new entrants vs the niche's demand; 7+ credible entrants/90 days
in a mid-demand niche = act now or skip). Alerts surface in the standup:
"Rising: [niche] (+3 strong entrants, demand up); Urgency 72: [niche]
window narrowing."

### Upgrade integration rules
- TITLE INTELLIGENCE now always includes: revenue estimates (M16), keyword
  difficulty for the chosen keywords (M18), category thresholds (M19),
  margin verdict (M23), and seasonality classification (M20).
- NICHE VALIDATION now always ends with the A-F Niche Score (M17) and the
  full extensive dataset saved as JSON.
- Review-gap mining (M22) runs automatically between Phase 0 clearance and
  TOC design for every competitive niche.
- All state under state/ survives updates and never ships in packages.
- Estimates are labeled estimates, everywhere, without exception. No
  fabricated data points: a field that could not be collected is null with
  a note, never invented.

### Every install
Every method in this upgrade applies on every Community Edition install:
users get the full computed intelligence (revenue
estimates, Niche Score, keyword difficulty, category thresholds, margin
gates, review-gap mining, seasonal keyword tracker, rising-niche alerts)
with their own trackers stored under their install's state/ folder,
surviving every update. The extensive-data law, estimate labeling, and
actuals-only rules bind on client installs exactly as on the operator
master. STARTER installs do not include this skill; when a Starter user
asks for market intelligence, offer the PRO upgrade politely.

### Interactive dashboard law (2026-08-15, display requirement)
Tables and sheets are never the only output. Every KEYWORD PACKAGE, NICHE
VALIDATION, TITLE INTELLIGENCE, ARBITRAGE SCAN, and seasonal keywords report
ALSO generates an interactive dashboard from its JSON twin:

    python intel_dashboard.py <json-twin> [-o intel_dashboard.html]

The dashboard is a single self-contained offline HTML, STATIC-FIRST: every
chart is pre-rendered SVG with native hover tooltips, zero required
JavaScript, so it displays fully in the Claude Code side panel and any
script-blocked viewer (no network): keyword opportunity bubble map with GOLDMINE/CONTESTED quadrants
and hover detail, sortable top-keyword bars, seasonality lines with
crosshair for tracked keywords, a marketplace tile map shaded by estimated
revenue with hover, and a sortable data table. DELIVERY (operator directive
2026-08-15): open the dashboard in the user's system browser (Chrome) as
the PRIMARY rendering surface (`--open` flag, or `start <file>`); the
interactive layer is active there: rich cursor tooltips, view switching
(opportunity/difficulty/revenue), band filter chips, click-to-pin bubble
detail, sortable table, and the auto-written "What this means"
plain-language insights panel. Also send the file in chat as a secondary
copy; the static charts render in the side panel too. Deliver alongside
the DOCX and JSON. All figures inherit the estimate-labeling law;
the page itself states that revenue figures are estimates. Applies on PRO
and MAX client installs identically.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
