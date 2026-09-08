---
name: uapf-trademark-checker
description: Run the mandatory title trademark and collision clearance gate the moment a title and marketplace are known — live trademark register searches, Amazon collision search, risk rating, and a decision gate that blocks HIGH RISK titles before any manuscript work begins. Invoked automatically by uapf-phase0-router and usable standalone across every UAPF niche skill.
---

# UAPF Trademark & Title Clearance Checker​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Universal, niche-independent clearance gate. Runs IMMEDIATELY after the title is received and the marketplace is detected — BEFORE subtitle generation, routing confirmation, or any content work. Every UAPF niche skill inherits this gate; none may skip it.

## When this skill runs

- **Automatically:** `uapf-phase0-router` invokes it as Step 1 of Phase 0, right after title receipt and marketplace inference.
- **Standalone:** the operator may invoke it directly to clear a candidate title before starting a project.
- **Re-run triggers:** title change, subtitle addition that introduces a new distinctive term, marketplace change, or series/brand promotion of an existing title.

## Inputs

| Input | Source | Required |
|---|---|---|
| Exact title | Operator's message | Yes |
| Marketplace | Operator's message, or inferred from title language (default: Amazon.com / US) | Yes |
| Subtitle candidates | Phase 0 (when available) | No — re-run on distinctive terms |
| Pen name / byline | Phase 0 (when available) | No — check if distinctive |

## Step 1 — Language & Marketplace Lock

1. Detect the dominant natural language of the exact title; state confidence.
2. Infer the regional standard from the marketplace (en-US for Amazon.com, en-GB for .co.uk, de-DE for .de, etc.).
3. If the title is English and no marketplace is given, default to American English for Amazon.com.
4. Lock the language and marketplace for all subsequent checks — the registers searched depend on this lock.

## Step 2 — Live Amazon Title Collision Search

Search the target Amazon marketplace AND the open web for:

- The exact title
- The dominant phrase (the distinctive 2–4 word core)
- Close word-order variants
- Materially similar titles in the same category

**Rule:** a matching descriptive title is NOT automatically prohibited, but it is a discoverability and confusion risk that must be reported with the ASIN/link of the closest collision.

**Exact-title matches (TITLE PRESERVATION LAW):** when one or more books with the EXACT same title are found on the marketplace, do NOT change, adjust, or "improve" the operator's title in any way — the title as given is locked. Instead, list each exact-title competitor as market intelligence:

```
EXACT-TITLE COMPETITORS FOUND: [count]
1. Author Name: [author] | BSR: [Best Sellers Rank] | Ratings: [number of ratings] | Format: [paperback/hardcover/Kindle] | ASIN: [asin]
2. Author Name: [author] | BSR: [Best Sellers Rank] | Ratings: [number of ratings] | Format: [paperback/hardcover/Kindle] | ASIN: [asin]
...
```

An exact-title descriptive match is a CAUTION at most (differentiation happens through the subtitle, cover, and positioning), never an automatic HIGH RISK — HIGH RISK is reserved for trademark conflicts, not title collisions. The competitor list feeds Phase 0 competitive analysis (page counts, pricing bands, positioning gaps).

## Step 3 — Live Trademark Register Search

Search the official registers for the locked marketplace. Use WebSearch/WebFetch against these sources:

| Marketplace | Primary register | URL pattern |
|---|---|---|
| All (baseline) | WIPO Global Brand Database | branddb.wipo.int |
| Amazon.com (US) | USPTO TESS | tmsearch.uspto.gov |
| Amazon.de / EU | EUIPO / TMview | euipo.europa.eu, tmdn.org |
| Amazon.co.uk | UK IPO | gov.uk/search-for-trademark |
| Amazon.ca | CIPO | ised-isde.canada.ca |
| Amazon.com.au | IP Australia | search.ipaustralia.gov.au |
| Amazon.co.jp | J-PlatPat | j-platpat.inpit.go.jp |

Search each of:
- Exact wording of the title
- Dominant/distinctive elements (ignore purely generic words like "guide," "book," "complete")
- Spacing and punctuation variants
- Stems and plural/singular forms
- Translations into the marketplace language
- Phonetic equivalents
- Confusingly similar marks

**Nice Classes to examine (minimum):**
- **Class 16** — printed books and publications
- **Class 9** — downloadable e-books, educational digital products
- **Class 41** — education, training, publishing, online educational services
- Any class connected to a distinctive branded term appearing in the title

**Beyond identical classes:** consider famous-mark dilution and false-affiliation risk — a famous mark in ANY class (e.g., a tech brand, a toy brand, a sports league) inside a title is a risk even if no Class 16 registration exists.

## Step 4 — Eponym & Protected-Name Screen

- Personal names of living or recently deceased individuals: check right-of-publicity risk and marketplace-specific rules.
- Exam boards, certification bodies, product names, franchise names: usable only nominatively ("for the NCLEX-RN Exam" style), never in a way implying sponsorship. Flag any use for the niche skill's trademark scrub.
- Medical eponyms follow OV-MEDT stripping rules — flag them for the niche skill.

## Step 5 — Risk Rating & Decision Gate

Assign EXACTLY ONE rating:

| Rating | Meaning | Action |
|---|---|---|
| **CLEAR** | No live/pending relevant marks; no material Amazon collision | Proceed automatically |
| **CAUTION** | Similar marks exist but confusion is unlikely (different goods, weak/descriptive overlap) | Proceed with the explanation recorded in the decision log |
| **HIGH RISK** | Live mark on the dominant element in a relevant class, famous-mark conflict, or false-affiliation exposure | **STOP.** No subtitle or manuscript work. Generate 6–10 safer alternative titles preserving the operator's concept, re-run this gate on each, recommend the strongest cleared option |
| **UNVERIFIED** | Registers unreachable or search inconclusive | Never describe as "good to go." Report exactly which registers could not be checked, proceed only on explicit operator instruction, and record the gap |

**Hard rules:**
- Only CLEAR or an explained, low-confusion CAUTION may proceed automatically.
- HIGH RISK always stops the pipeline — this gate outranks autopilot self-approval.
- UNVERIFIED must be reported honestly; never claim a pass for a register that was not actually searched.

## Step 6 — Clearance Report (always output in English)

```
TITLE CLEARANCE REPORT
Exact Title:            [title]
Detected Book Language: [language] (confidence: [high/medium/low])
Marketplace:            [Amazon marketplace]
Search Date:            [date]
Amazon Collision:       [none / closest match + link]
Exact-Title Competitors: [none / count + per-competitor list: Author Name, BSR, Ratings, Format, ASIN]
Registers Searched:     [list with classes]
Registers Unreachable:  [list or "none"]
Relevant Matches:       [mark, owner, class, status, similarity — or "none"]
Risk Rating:            [CLEAR / CAUTION / HIGH RISK / UNVERIFIED]
Good-to-Go:             [YES / YES WITH NOTE / NO]
Required Revision:      [none / details]
```

Write the report to the project's Phase 0 records (`phase0/trademark-clearance.md` in the project folder) so later phases and the KDP metadata stage can cite it.

## Step 7 — Handoff

- **CLEAR / CAUTION:** return control to `uapf-phase0-router`, which continues to subtitle generation and niche skill invocation. Pass the cleared dominant terms so the subtitle compliance battery avoids introducing new risks.
- **HIGH RISK:** present the alternative titles and stop. The pipeline resumes only when the operator picks a cleared title.
- **UNVERIFIED:** queue as a blocker per BACKGROUND_BLOCKER_HANDLING — continue only niche-independent work (no metadata, no cover, no title-bearing assets) until resolved or overridden.

## Legal boundary

This is a preliminary publishing-risk screen, not a legal opinion or guarantee. For any title intended as a series name, imprint, course brand, or major commercial identity, recommend qualified trademark counsel — and record that recommendation in the report.

## Key Rules — Do NOT Break

0. **TITLE PRESERVATION LAW:** the operator's title is NEVER changed, reworded, or "improved" because exact-title competitors exist. Exact matches are reported as a competitor intelligence list (Author Name, BSR, Number of Ratings, Format, ASIN) — nothing more. The ONLY event that can pause a title is a genuine HIGH RISK trademark conflict, and even then the operator chooses; the system never silently substitutes a title.
1. This gate runs BEFORE any subtitle, byline, TOC, or content work — no exception in any niche.
2. Never claim a register was searched when it was not reachable — report UNVERIFIED honestly.
3. HIGH RISK stops the pipeline even in full autopilot mode. It is never self-approved.
4. Famous marks are a risk in ANY Nice class — do not clear a title just because Class 16 is empty.
5. Re-run the gate whenever the title, subtitle's distinctive terms, or marketplace changes.
6. The clearance report is a permanent Phase 0 production record — always write it to the project folder.
7. Nominative fair use ("for the [exam/product]") must be flagged to the niche skill for its trademark scrub — cleared here does not mean unrestricted use in metadata.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
