---
name: uapf-niche-business
description: Business & Money niche overlay (OV-BIZ) — invoked by uapf-phase0-router when title/format signals indicate business, personal finance, investing, entrepreneurship, career, or money-related nonfiction. Applies AIRF 2.0 Business and Money Edition controls: R3 mandatory, no income/return promises, math-audited worked examples, jurisdiction-labeled tax content.
---

# UAPF Niche: Business & Money (OV-BIZ)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Business-and-Money-Edition/` (config, validation, phases, and deterministic ops in `genie_business.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Business and Money Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title contains (in any language, after internal translation) any of: business, money, finance, investing, side hustle, entrepreneur, freelancing, small business, personal finance, budgeting, career, real estate, marketing, sales, passive income — or close synonyms and compounds (wealth, debt, credit, saving, retirement, startup, e-commerce, negotiation, salary, taxes, accounting, cash flow, dividend, stock market, crypto/cryptocurrency, franchising, dropshipping, rental property, landlord, resume/CV, job search, pricing, branding, copywriting, affiliate). Format signals: how-to money guides, investing primers, business handbooks, career guides, financial workbook-adjacent prose titles. If the title is a pure blank ledger/planner (low-content), route to the low-content pipeline instead; if it is an exam-prep finance title (CPA, CFA, Series 7), route to OV-EXSIM with OV-BIZ as secondary advisory overlay.

**Framework of record:** AIRF 2.0 Business and Money Edition (28-category system). This skill is the self-contained operating profile; where a conflict arises, the latest explicit user instruction wins, then this skill, then UAPF defaults.

**Non-negotiable posture for the entire pipeline: R3 (highest risk regime) is MANDATORY for every OV-BIZ title, regardless of how harmless the topic appears.** A leadership book and a crypto book both run R3. R3 means: every factual, legal, tax, and numerical claim is verified against a current source before it ships; every time-sensitive figure is dated; every worked example is recomputed; compliance gates cannot be waived.

---

## Expert Panel

Simulated review lenses only. Never describe these as review by an actual licensed adviser, CPA, attorney, or other credentialed professional unless a real, documented reviewer was engaged. Accuracy percentages are internal targets, not guarantees.

1. **Financial Educator (Domain Master)** — owns pedagogy, sequencing, worked-example design, and reader-centered voice. Ensures the book teaches methods and mechanisms, not outcomes; ensures every strategy is framed as an option with trade-offs, never a personal recommendation.
2. **Consumer-Protection & Compliance Reviewer** — enforces earnings-claims rules (FTC-style substantiation standards), the guaranteed-outcome ban, scam-pattern education where the category exposes readers to predators, and the prohibited-misrepresentation list. Vetoes any urgency, scarcity, or pressure framing around money decisions.
3. **Tax & Regulatory Accuracy Lens** — owns jurisdiction identification, "as of" dating, the Dynamic-Facts Verification Log, regulator sourcing (IRS/SEC, HMRC/FCA, BaFin, AMF/ACPR, ATO/ASIC, SEBI/RBI, etc., per target marketplace), and the year-stamped vs. evergreen edition decision.
4. **Venture & Cash-Flow Realist** — audits business and side-hustle content for failure-rate honesty, total-cost transparency, platform-dependency disclosure, licensing/legal-structure flags, and realistic timelines. Kills every overnight-success narrative.
5. **Evidence & Math Auditor** — independently recomputes every worked numerical example, verifies every statistic/rate/threshold against its dated source, checks chart honesty (zero-based axes or clearly labeled), and enforces the real-company/living-person protocol.

---

## Phase 0 — Title Analysis

### 0.1 Title Intake (verbatim law)
- Record the supplied title **character for character**: identical capitalization, spelling, punctuation, spacing, word order. Never title-case, correct, translate, or restyle it anywhere it appears (cover, title page, copyright page, headers, TOC, metadata, reports). Even an apparent typo is preserved unless the user explicitly approves a correction.
- Detect the title language → this is the manuscript language. All system reports remain in English.
- Translate internally for classification only.
- Identify likely reader, target Amazon marketplace, and — critically for this niche — the **tax and legal jurisdiction** that will ground all money, tax, and legal content. State the jurisdiction explicitly in the Phase 0 report.

### 0.2 Title Clearance (elevated trademark screen)
Business & Money carries elevated trademark exposure: financial brands, banks, fintech products, certification bodies (CPA, CFA, CFP, ACCA, EA), and famous investment methods are heavily registered and actively defended.
- Search: exact title; distinctive words alone and combined; singular/plural/spelling/phonetic variants; translated equivalents; similar series names, financial brands, fintech products, courses, coaching services, certification marks, software, and media properties.
- Use the official register for the target jurisdiction plus an international database when appropriate. Record live search date, databases, search strings, results, goods/services.
- Output GREEN / YELLOW / RED with a plain-English risk explanation and the reminder that this is a **preliminary risk screen, not legal clearance**.
- On YELLOW/RED: keep the exact title, explain the concern, offer safer alternatives preserving the seed words. Never replace the title automatically.

### 0.3 Subject Analysis and Category Tier
Classify into one primary tier (plus optional secondary), which controls voice, evidence level, disclaimer text, and referral language:

| Tier | Typical subjects | Control emphasis |
|---|---|---|
| **Regulated Financial** (highest) | investing, securities, retirement, crypto, insurance, credit repair, debt, taxes | Education-only framing, dated jurisdictional facts, balanced risk disclosure, scam education, strict referral language, no personal recommendations |
| **Financial Guidance** | budgeting, saving, personal finance, money habits | Strong evidence, shown assumptions and math, realistic timelines, structural honesty about income and costs |
| **Venture** | startups, side hustles, freelancing, small business, real estate operations, passive income models | Failure-rate honesty, total-cost transparency, legal-structure/licensing flags, platform-dependency disclosure |
| **Organizational** | leadership, management, HR, careers | Evidence-aware practice, jurisdiction-labeled employment law, ethical people-topic handling |
| **Commercial** | marketing, sales, branding, pricing, negotiation | Advertising-standards awareness, consent-based persuasion, honest dated market/salary data, no manipulative playbooks |
| **Analytical** | economics, accounting, business analysis, business history | Named and dated standards, verified filings, defamation caution for real companies/persons |

Risk escalators (raise scrutiny even in lower tiers): securities, tax positions, debt, credit repair, cryptocurrency, insurance, retirement products, legal structures, franchising commitments, or vulnerable audiences (readers in debt crisis, seniors, first-time investors). R3 applies to all tiers regardless.

### 0.4 Edition-Type Decision
Classify at intake and record it:
- **Year-stamped**: tax, retirement, allowance/contribution-limit-driven topics — carry the year in title or subtitle and plan the Annual Edition Update Pass (re-verify every Dynamic-Facts Log row, update figures/dates/dependent examples, recompute, refresh links, re-run gates; no rewrite, no architecture change, no new uniqueness audit).
- **Evergreen**: principles-led topics (leadership, negotiation, strategy) — still date all volatile figures and teach the method for finding current values.

### 0.5 Subtitle Generation (post-clearance only)
Generate **five** options. Each must: preserve the title verbatim; use natural, market-relevant, jurisdiction-sensitive language; state character count and primary appeal. **Prohibited in every subtitle:** guaranteed wealth, guaranteed/passive income promises, fixed-time financial freedom ("in 30 days"), market-beating returns, certain business success, tax elimination, "risk-free," and any specific earnings figure. Recommend the strongest option with rationale.

### 0.6 Auto-Configuration Output
The Phase 0 report (English) states: exact title (verbatim) • language • marketplace • jurisdiction • primary/secondary tier • risk regime (always R3) • edition type • trademark status • subtitle recommendation • typography selection (see Interior Design) • reference style (APA 7 default for management/marketing/careers/personal finance/behavioral economics; Chicago Author-Date for economics/analytics; Chicago Notes & Bibliography for business history/biography; jurisdiction-standard citation for statutes and tax authorities, always naming authority and year) • author pseudonym plan (random-name-generator sourced, First Name M. Surname, no credentials/designations ever, conflict-searched) • visual strategy. Then present the competitor research (below) and end with the exact continuation phrase per UAPF gating.

### 0.7 Competitor Research and Page Target
- 10 to 20 genuinely comparable **print** books on the primary marketplace; prefer current paperbacks. Record title, subtitle, author, date, format, page count, trim, reader, scope, table/worked-example density, visual density.
- Exclude: duplicate editions, Kindle page estimates, blank ledgers/planners/low-content, bundles, textbooks (unless matching), materially different audiences, and visibly outdated editions (stale tax years/rates) unless structurally instructive. Separate workbooks/planners/exam-prep/reference manuals when structures differ. Never let one outlier bestseller set the target.
- Compute mean, median, min, max, central range; **median preferred** when outliers exist. Recommend the final page target accounting for trim, font size, spacing, images/diagrams, tables, worked examples, front matter, 1.5-page conclusion, appendices, references.

---

## Book Architecture

### Structural Unit: the Chapter Formula (adaptive, never templated)
Each chapter begins on a new page and is designed for this specific book. Draw components as needed (not all per chapter):
1. Opening reader problem — a concrete money situation the reader recognizes.
2. Evidence-based explanation of the mechanism (how the thing actually works).
3. **Worked numerical example(s)** — assumptions stated, realistic figures in the target marketplace's currency and number/date conventions, arithmetic shown step by step, independently recomputed before the chapter is declared complete. Include losing and break-even scenarios where honesty requires them, never only winning scenarios.
4. Case scenario — real (public-record, protocol-compliant) or clearly labeled hypothetical/composite.
5. Practical method: numbered steps, checklists, scripts, decision tables/matrices.
6. Common mistakes and troubleshooting.
7. Risk notes, jurisdiction labels, and professional-referral pointers where the tier requires them.
8. Integrating close.

Diagrams/charts sit at every major quantitative explanation, comparison, and decision point; worked-example visuals sit directly beside the arithmetic they illustrate.

### Learning journey (adapt per title)
Foundation → mechanics → application → risk management → sustained practice. For Regulated Financial titles, weave risk education, jurisdiction notes, and referral integration through the sequence, not into one ghettoized chapter.

### Page bands
Set by competitor research (0.7), not fixed. Typical OV-BIZ bands: beginner personal-finance guides 140–200 pages; standard business/career titles 180–250; dense reference/analytical titles 220–300. The **compulsory image rule applies at ANY page count**: images are generated and inserted wherever the content needs them regardless of projected or final page count (global Rule 11; see Interior Design).

### Front matter (exact order)
1. Half-title (when appropriate) 2. Full title page 3. Copyright page 4. **Category-specific financial and legal disclaimer** 5. Dedication (optional) 6. Preface (~1 formatted page) 7. How to Use This Book (~1 formatted page) 8. Automatic TOC (live field, dot leaders, right-aligned numbers) 9. Introduction beginning on **visible Arabic page 1**.

Copyright page: copyright notice/year attributed to the pseudonym; all-rights-reserved; edition statement; financial-education disclaimer plus investment-risk statement where relevant; AI-image disclosure when required; **no publisher line, no ISBN, no placeholders** unless the user supplies real values.

### Back matter
- **Conclusion: approximately 1.5 formatted pages.** Integrates lessons, reinforces realistic expectations about money/risk/timelines, encourages continued application, introduces no new major method, includes professional-help guidance where the tier requires.
- **Appendices (practical value only, no filler):** choose from budgeting/cash-flow worksheets, decision checklists, negotiation and outreach scripts, comparison tables, formula references, glossary of financial terms, **rates-and-limits appendix concentrating all volatile figures**, jurisdiction-specific resource directories with dated links, consumer-protection and debt-help resources, recommended reading, printable summaries.
- References/resources in the selected citation style; scholarly, official/regulator, further-reading, and consumer-protection sources separated when clarity requires; all links verified immediately before finalization.

### Interior layout laws
- Body prose justified; lists, numbered steps, worked examples, worksheets, formulas, questions, and tables **left aligned**.
- No em dashes anywhere in the manuscript: commas, colons, or restructured sentences.
- Headings keep with following text; no clipped tables or images; no orphaned section titles.

---

## Interior Design

Inherits UAPF default DOCX engine with these OV-BIZ specifics:
- **Trim:** 6 x 9 in, **0.7 in margins** all sides (increase gutter only when binding requires).
- **Typeface:** Times New Roman throughout unless the user explicitly requests otherwise.
- **Body size/spacing decision table:** standard adult business titles 12 pt / 1.15; dense reference and accounting titles 11 pt / 1.15; beginner and senior-focused money guides 13 pt / 1.15. Announce the selection and rationale in English.
- **Headings:** Chapter = Heading 1, centered, 14 pt, bold, block letters. Subchapter = Heading 2, capitalized, left aligned. Heading 3 only when needed.
- Real Word styles, list styles, table styles, caption styles, citation tools, section breaks, TOC field, page-number fields. No visible front-matter page numbers; Introduction = page 1.
- **Color scheme:** print-grayscale-safe interior. Every chart must be legible in grayscale, use honest axis scaling starting from zero unless clearly labeled, and never visually exaggerate gains or shrink risks.
- **Visual system (adaptive):** labeled diagrams, charts, and tables are the *preferred* style for quantitative content; clean 2D line illustrations for process/structure; photographic imagery reserved for context, environment, and human application.
- **Compulsory image rule:** projected interior ≤ 179 pages → all necessary visuals are generated and inserted automatically, no separate permission awaited. ≥ 180 pages → still create necessary visuals, quantity-controlled. Every image ships either inserted (with caption + alt text) or as an `[IMG-XX]` placeholder plus a complete `image_manifest.md` row (slot ID, full self-contained English prompt, aspect ratio, DOCX location, content constraint, style). Alt text for charts includes the key numbers.
- **Marketplace conventions:** all money figures, grouping, and dates follow the target marketplace's conventions (decimal-comma markets, space-grouping markets, no-decimal yen, lakh-crore grouping, etc.). One convention per manuscript; cross-market comparisons label each figure with its currency code in its own format.

---

## Content Rules

### The Fatal Flaw to avoid: the promised outcome
The single flaw that kills an OV-BIZ book (and risks account-level KDP action) is **promising financial outcomes**: guaranteed returns, guaranteed income, "make $X in Y days," risk-free profit, certain business success, tax elimination, fixed-time wealth. This ban applies to the manuscript, subtitle, description, metadata, imagery, and A+ content. Any earnings figure that does appear must be truthful, substantiated, contextualized against typicality, and never framed as an expectation. Testimonials/case results must be real and verifiable or clearly labeled illustrative composites.

### Hard constraints
1. **R3 verification, always.** Every statistic, rate, threshold, allowance, deadline, platform fee, law, and marketplace fact is verified live at generation time against a current source and logged in the **Dynamic-Facts Verification Log** (one log per project; every time-sensitive figure gets a row before delivery).
2. **Math audit on every worked example.** Assumptions stated; realistic local figures; arithmetic shown; independently recomputed before the chapter closes; losing/break-even scenarios included where honest.
3. **Jurisdiction labeling.** Every legal, tax, and program-specific fact carries its jurisdiction and "as of [month, year]" dating. When a figure will change within the book's sales life, teach the method for finding the current value from the official source alongside the number. Sourcing starts with the jurisdiction's tax authority and principal financial regulators.
4. **Not-professional-advice disclaimer (required).** Every book states it provides educational information and does not replace individualized financial, investment, tax, legal, accounting, or insurance advice from a licensed professional who knows the reader's situation; names the relevant professional types for the tier; never implies the author holds credentials. Investment-touching books add: all investing involves risk including possible loss of principal; past performance does not guarantee future results.
5. **Options, not recommendations.** Strategies are presented as options with trade-offs. Never assess or recommend for the individual reader. State the situations outside the book's safe scope (insolvency, tax disputes, active litigation, complex estates, foreclosure, garnishment, fraud victimization, coerced financial control, gambling-pattern spending) and route those readers to qualified help; protective guidance overrides planned chapter flow.
6. **No pressure.** Plain, pressure-free language around money decisions; no manufactured urgency or scarcity anywhere.
7. **Scam-pattern education** wherever the category exposes readers to predatory schemes. Never promote MLM recruitment, pyramid structures, or predatory lending as wealth strategies.
8. **Content-standards compliance (catalogue-wide).** No case studies, business ideas, examples, or imagery centered on alcohol, pork, gambling, adult entertainment, or predatory lending. Interest-bearing products may be explained factually/educationally where needed for market literacy; include ethical alternatives (profit-sharing and equity-based instruments) where natural. No casino analogies or lottery-style wealth narratives.
9. **Real-company / living-person protocol.** Public-record facts only, verified against primary filings, court records, official statements, or multiple reputable sources; no motive attribution unless on the record; "reportedly"/"according to" on contested claims; no invented quotes, dialogue, or scenes; allegations stay allegations until adjudicated, with settlement vs. regulatory finding vs. conviction distinguished; private individuals anonymized or labeled composites; company names nominative only, no logos/trade dress in imagery; hypothetical businesses unmistakably fictional.
10. **No fabrication, ever:** credentials, licenses, designations (CPA/CFA/CFP/ACCA/EA), sources, statistics, returns data, legal clearance, ISBNs, publisher identities, reviews, rankings, client results, sales claims, or quotations attributed to real investors/executives.
11. **Voice.** Reader-centered "I see you" second person grounded in real money situations (debt shame, market fear, business failure) with "you may / perhaps / some readers find" hedging; natural contractions; varied sentence length; no hype filler (leverage, utilize, robust, optimize, revolutionary, game-changing, unlock as default words); trust earned through specificity: real numbers, named mechanisms, honest trade-offs. No em dashes.
12. **Uniqueness.** No two books (including series volumes) share chapter architecture, progression, opening patterns, worked-example sets, case scenarios, table designs, image arrangement, appendix package, or concluding emphasis. Keyword-swapping a prior manuscript fails the audit.
13. **Series rule** (Business & Money sells heavily in series): shared identity layer (series name, one reused pseudonym, cover system, trim/typography, front-matter order, appendix categories, shared glossary base, "Also in this series" page) but every volume passes the uniqueness audit at the content layer, gets its own trademark screen (series name + volume title), its own competitor research, and its own Dynamic-Facts Log.

---

## QA Checklist

### Gate 1 — Configuration Gate (after Phase 0, before TOC)
- [ ] Title recorded verbatim, character for character, in every artifact so far.
- [ ] Language, marketplace, and **jurisdiction** identified and stated.
- [ ] Trademark screen completed, dated, databases logged; status GREEN or user-acknowledged YELLOW/RED path.
- [ ] Tier + risk classification recorded; **R3 confirmed active**.
- [ ] Year-stamped vs. evergreen decision recorded.
- [ ] 10–20 valid comparables; exclusions applied; mean/median computed; page target justified (median-preferred).
- [ ] Typography, reference style, and visual strategy selected with rationale.
- [ ] Pseudonym generated (First Name M. Surname), conflict-searched, zero credentials attached.
- [ ] Five subtitles generated post-clearance; none contains an income/outcome promise; one recommended.

### Gate 2 — Structure Gate (TOC + front matter)
- [ ] TOC is a unique architecture for this title (not a reused outline); learning journey fits the tier; no duplicate chapter purposes.
- [ ] Regulated Financial titles: risk education, jurisdiction notes, and referral integration visible in the sequence.
- [ ] Page allocation sums to the competitor-informed target.
- [ ] Front matter in exact required order; disclaimer text matches the tier and names the right professional types; investment-risk statement present where relevant.
- [ ] Copyright page clean: no placeholder publisher/ISBN/credentials.
- [ ] Word skeleton: 6x9, 0.7 in margins, Times New Roman, real Heading styles, live TOC field, Introduction = visible page 1.

### Gate 3 — Per-Chapter Gate (every chapter, before "complete")
- [ ] **Math audit:** every worked example recomputed independently; assumptions stated; marketplace-correct currency/number/date conventions; losing/break-even scenarios where honesty requires.
- [ ] **Dynamic facts:** every time-sensitive figure verified live, "as of"-dated, jurisdiction-labeled, logged.
- [ ] No outcome promises, urgency, scarcity, personal recommendations, or pressure framing.
- [ ] Referral/out-of-scope language present where triggered.
- [ ] Real-company/living-person protocol satisfied for every named entity; hypotheticals labeled.
- [ ] Content-standards audit: no prohibited business models/imagery; ethical alternatives included where natural.
- [ ] All required visuals inserted (caption + alt text) or `[IMG-XX]` + manifest row complete; charts grayscale-legible, honest axes.
- [ ] Voice audit: no AI filler phrases, no em dashes, no recycled examples; body justified, lists/tables left aligned.

### Gate 4 — Release Gate (whole book)
- [ ] Title verbatim in every location including metadata and cover.
- [ ] Full Dynamic-Facts Verification Log complete: one row per volatile figure, all re-checked.
- [ ] All worked examples re-verified book-wide; cross-chapter numeric consistency.
- [ ] Language/currency/jurisdiction consistency: one convention throughout; cross-market figures labeled with currency codes.
- [ ] Disclaimer, earnings-claims compliance, and professional-boundary language final-checked in manuscript, subtitle, description, and imagery.
- [ ] Conclusion ≈ 1.5 formatted pages; appendices practically valuable; every resource link and program name verified current.
- [ ] TOC and all fields updated; page numbering correct from Introduction; no clipped tables, stretched images, broken headings, orphans; document rendered page by page and visually inspected.
- [ ] Uniqueness audit passed against catalogue (and against sibling series volumes).
- [ ] AI-image disclosure recorded where required; references confirmed real; no fabricated source anywhere.

---

## KDP Positioning

- **Category tree:** Books > Business & Money, then the deepest accurate subnode: Personal Finance (Budgeting & Money Management / Retirement Planning / Credit Repair), Investing (Introduction / Stocks / Real Estate), Small Business & Entrepreneurship (Home-Based / Franchises / New Business Enterprises), Job Hunting & Careers, Marketing & Sales, Real Estate, Economics, Management & Leadership, Accounting, Skills > Business Writing/Negotiation, as fits. Choose one primary + complementary secondary; never a deeper node the content does not honestly serve.
- **Description leads with the reader's problem and the book's method** — what the reader will understand and be able to do — never with income, returns, or lifestyle outcomes. State the jurisdiction/edition year for year-stamped titles ("United States, 2026 tax year" style) as a trust signal. Mention concrete deliverables: worked examples, worksheets, checklists, the rates-and-limits appendix.
- **Description compliance:** the earnings-claims rules apply verbatim to the description and A+ content — no guaranteed income, no "$X/month," no fixed-time promises, no cash-pile or luxury imagery. No fake credentials or "bestselling" claims.
- **Metadata signals:** keywords from real buyer vocabulary (the seed words + tier terms: "for beginners," "step by step," the jurisdiction, the year for year-stamped titles); manuscript-language metadata for non-English marketplaces; author = the series pseudonym with no credential suffixes; year-stamped titles refresh metadata every edition pass.
- **Pricing/format posture:** paperback-first at the competitor-informed page band; positioning grounded in the comparables research, not aspiration.

---

## Key Rules — Do NOT Break

1. **R3 is mandatory for every OV-BIZ title.** No tier, topic, or user shortcut downgrades verification.
2. **No return promises, income claims, or guaranteed outcomes** anywhere: manuscript, subtitle, description, metadata, imagery, A+. No "risk-free," no fixed-time wealth, no tax elimination.
3. **Math audit every worked example:** assumptions stated, arithmetic shown, independently recomputed, honest scenarios (including losses/break-even) where relevant.
4. **Jurisdiction-label and "as of"-date every tax, legal, and program fact**, log it in the Dynamic-Facts Verification Log, and teach the method for finding the current figure.
5. **The not-professional-advice disclaimer is required in every book**, tier-matched, naming the relevant licensed professionals; investment books add the loss-of-principal and past-performance statements.
6. **Preserve the supplied title verbatim, character for character, everywhere.** Never restyle it; even typos survive without explicit user approval.
7. **Options, never personal recommendations.** No urgency or pressure around money decisions; out-of-scope crisis situations route to qualified professionals, overriding chapter flow.
8. **Never fabricate:** credentials, designations, licenses, sources, statistics, returns data, client results, endorsements, ISBNs, publishers, legal clearance, or quotes from real people. The pseudonym is First Name M. Surname with nothing attached.
9. **Content standards are absolute:** no alcohol, pork, gambling, adult entertainment, or predatory-lending business models or imagery; no MLM/pyramid promotion; explain interest-bearing products educationally and include ethical alternatives where natural.
10. **Real companies and living persons: public record only**, attribution discipline, allegations stay allegations, no invented scenes or quotes, privates anonymized, no logos or trade dress.
11. **Charts tell the truth:** grayscale-legible, zero-based or clearly labeled axes, no cherry-picked windows, no wealth-flaunting imagery.
12. **No em dashes in the manuscript.** Body justified; lists, tables, worked examples, worksheets left aligned. Times New Roman, 6x9, 0.7 in margins, Introduction = page 1, live TOC.
13. **Uniqueness audit before delivery** — architecture, examples, scenarios, tables, visuals, appendices all novel, including against sibling series volumes.
14. **Trademark screen before subtitles**, elevated for financial brands and certification marks; result is a risk indicator, never legal clearance.
15. **Every title is built as an annually refreshable edition:** volatile figures concentrated in bounded tables/boxes/appendix, each paired with its official-source lookup method, so the edition update pass touches only logged facts, dates, dependent math, and end matter.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
