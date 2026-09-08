---
name: uapf-niche-travel
description: Niche overlay for premium destination travel guides — invoked by uapf-phase0-router when routing signals match OV-TRAVEL titles.
---

# UAPF Niche: Travel Guides (OV-TRAVEL)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Travel-Edition/` (config, validation, phases, and deterministic ops in `genie_travel.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Travel Edition` into the `book_lock.md` classification line (global rule #16).

**Governing framework:** Universal Travel Guide Framework v3.0 (UTGF v3.0) — Pegasus Press Edition, July 2026. This skill is the authoritative niche overlay. It supersedes any conflicting default UAPF rule for OV-TRAVEL titles. The governing order within a session is: operator's current title-specific instruction > this skill > UTGF v3.0 > companion master prompt > any older reference.

**Routed here when** the title or description contains any of the following signals (case-insensitive):
- travel guide
- destination
- city guide
- trip to [place]
- exploring [place]
- visitor's guide
- tourist guide
- travel companion
- road trip
- backpacking guide

---

## Expert Panel

| Role | Responsibility |
|---|---|
| **Domain Master — Destination Travel Specialist** | Final authority on destination accuracy, coverage depth, regional chapter logic, itinerary validity, cultural accuracy, and content-standards compliance. Reviews every content gate. |
| **Travel Content Strategist** | Competes the title against Amazon marketplace benchmarks, optimises chapter sequencing and venue selection, and ensures the experience hierarchy (Ultimate Experiences > itineraries > district chapters) delivers clear reader value. |
| **Print Layout & Typography Director** | Enforces the two-column entry containment law, section-divider page placement, 80-90% fill targets, safe-area compliance, Times New Roman hierarchy, and two-accent color application across chapter openers, tables, and sidebars. |
| **Legal, Compliance & Accuracy Officer** | Runs trademark/marketplace clearance, content-standards compliance sweeps, volatile-fact dating audits, non-affiliation language checks, QR-code verification, and the disclaimer completeness gate. |
| **Image & Map Production Lead** | Directs full-bleed chapter opener generation, inline image placement, original map creation (ChatGPT Image 2.0 (gpt-image-2)), QR-code generation, and the image uniqueness fingerprint check. |

---

## Phase 0 — Title Analysis

Execute every step below in order and in full before drafting the Table of Contents or any manuscript content. Report all findings in one concise English configuration brief, then stop with the exact standalone gate phrase:

**Type Proceed**

### Step 1 — Title Lock and Language Identification
- Lock the operator's exact supplied main title. Do not rewrite, shorten, optimize, translate, or replace it.
- Identify the destination (city, region, country, route, or theme).
- Identify the content language from the title language. All operator-facing messages remain in English regardless of content language.
- Flag if the title implies a specific audience (seniors, families, solo travelers, backpackers) — this affects body size and line-spacing selection.

### Step 2 — Trademark and Marketplace Clearance
Perform a risk-screening search (not legal advice) covering:
- Relevant trademark registers: USPTO + WIPO at minimum; add CIPO, UK IPO, EUIPO, or destination-country national registry when market or destination warrants.
- General web search for identical or confusingly similar travel guide titles.
- Amazon title listings for the primary marketplace aligned to the content language.
- Publisher catalogs and obvious series conflicts.
- Destination-authority names, national tourism board names, park or attraction brands, and transport brand names that could imply official affiliation.

Report verdict as one of: **CLEAR**, **CAUTION** (add non-affiliation plan), or **HIGH RISK** (report and hold at gate for operator direction). Never alter the title automatically.

### Step 3 — Amazon Competitor Page Benchmark
Research at least 10 (target 20) relevant paperback travel guides on the primary Amazon marketplace:
- Prioritize same-destination guides; use closely similar regional guides if too few direct matches exist.
- Record: title, publisher type where visible, publication date, paperback page count, price, star rating, and format pattern.
- Exclude: blank journals, notebooks, standalone maps, and formats with non-comparable page counts.
- Compute mean and median page count. Median carries more weight when outliers distort the average.
- Recommend a competitive target near the market median, within the deployment page budget (studio owner: hard 100; client: their chosen cap). Keep at least 2 pages in reserve.
- When the competitor median exceeds the page budget: compress intelligently through concise writing, selective venue coverage, efficient tables, and tighter information hierarchy. The studio-owner cap of 100 is never relaxed.
- When competitor median is substantially lower: align with the market while retaining all required front matter, chapter openers, conclusion, and appendix.

### Step 4 — Edition-Year Marker
- Confirm the current publication year for the copyright page and metadata.
- Record the season-year band for volatile-fact labels (e.g., "as of Summer 2026"). This label is applied to all prices, hours, visa rules, transport routes, entry requirements, and reservation systems throughout the manuscript.
- The edition-year marker is mandatory. It may not be omitted.

### Step 5 — Author Identity
- Open https://www.fakenamegenerator.com/ and obtain a random author name.
- Format as: First Name, Initial(s). Surname — for example, "Lena J. Okafor" or "Matthew R. D. Clarke."
- Use this name consistently on the copyright page and in all metadata.
- Do NOT place the author name on the front cover unless the operator explicitly overrides the standing travel-guide convention.

### Step 6 — Subtitle Generation
- Generate 3-5 candidate subtitles that add the search keywords the locked title lacks: destination synonyms, itinerary day-counts (3, 7, 14 days), "maps," "things to do," audience terms (families, first-timers, road-trippers), and the edition year.
- Example shape: "The Complete [Year] Visitor Companion with 3, 7 and 14 Day Itineraries, Original Maps, Top Experiences and Family-Friendly Planning."
- Subtitle rules: factual only (no "bestselling," no invented awards or rankings), no trademarked series names or brand comparisons, consistent with the alcohol-free positioning (no nightlife or bar-crawl keywords), and carries the edition-year marker.
- Recommend one subtitle; the operator selects or overrides at the gate. The main title itself is never modified.

### Step 7 — Auto-Configuration Selection
After intake analysis is complete, select and lock the following configuration and record it in the phase report:

**Body size:** 11 pt (general audience) or 12 pt (accessible). Use 13-14 pt when the title explicitly targets seniors or the elderly.

**Line spacing:** 1.15 (default when page cap or content density requires) or 1.5 (when accessibility benefits and ledger permits).

**Two-accent color palette:** Select two destination-inspired, high-contrast, CMYK-safe, non-neon accent colors.
- Accent A: darker structural color — chapter-title panels, Heading 2, sidebars, rules, map labels.
- Accent B: brighter supporting color — table headers, itinerary bands, highlights, cover title fields.
- Derive colors from the destination's architecture, landscape, textiles, vegetation, stone, sky, or cultural color language. Do not default to teal-and-orange. No two Pegasus Press titles may share the same palette.
- Record HEX values, approximate CMYK values, title-panel text color, pale tint values, and palette fingerprint in the production ledger.

**Cover concept:** High-resolution realistic destination photograph with unique title arrangement. Solid color title field permitted; shape, location, proportion, photo crop, and supporting details must be distinctive from all prior Pegasus Press titles.

**Chapter map:** Adapt chapter names to the destination while preserving the 12 required functional blocks (see Book Architecture below).

**Image program:** Full-bleed chapter opener for every major chapter; inline images approximately one per substantial subsection; a full map set — one destination overview plus one dedicated map per district/area chapter (minimum 4 to 5 maps; see Map Rules); QR codes for all featured venues. Total image and map counts recorded in ledger.

**Page ledger target:** Record estimated page allocation per chapter. Maintain running ledger through all phases.

**Deployment mode:** always ask the operator to choose the trim (6 x 9 or 8.5 x 11) at this step. If a `.genie_owner` marker is present (studio owner), lock the page cap to 100 and use two-column entries. If absent (licensed client), also confirm the operator's page budget, body size, and one- or two-column entry preference.

**Catalog uniqueness fingerprint:** Cover composition, palette, chapter-opener treatment, regional organization, map style, table style, image sequence. Confirm no duplicate with prior Pegasus Press travel titles.

### Step 8 — Gate Pause
Present the complete configuration report in English and stop. The report must include:
- Title lock confirmation and language
- Recommended subtitle plus alternates
- Trademark verdict and any non-affiliation notes
- Competitor benchmark: sample titles, mean, median, recommended target page count
- Author name
- Body size, line spacing, palette (both accents with HEX), cover concept summary
- Chapter map (numbered list)
- Estimated page ledger
- Edition-year / season-year band
- Catalog uniqueness fingerprint

Then output the exact standalone gate phrase:

**Type Proceed**

---

## Book Architecture

### Trim Size and Canvas
- **Trim choice (ask at Phase 0, no silent default):** ask the operator to choose the trim, and lock it in the configuration report. Ask for BOTH the studio-owner and client deployments. Bleed enabled on KDP either way.
  - **6 x 9 inches** (standard travel-guide trade format): production canvas 6.125 x 9.25 in; safe-area margins 0.5 in; full-bleed opener resolution 1838 x 2775 px.
  - **8.5 x 11 inches** (large format): production canvas 8.625 x 11.25 in; safe-area margins 0.7 in; full-bleed opener resolution 2588 x 3375 px.
- **Canvas behavior:** full-bleed photographs and chapter opener backgrounds extend to all outer canvas edges; non-bleed text pages use the same document page size for stability. All body text, tables, headings, QR labels, captions, and page furniture stay inside the chosen trim's safe-area margins.
- **Gutter:** confirm the final inside margin against the KDP gutter requirement before release; increase when required without reducing any outer safe margin below the chosen trim's safe margin.

### Page Budget (deployment-aware)
Check for a `.genie_owner` marker file in the install root.
- **Studio owner deployment** (`.genie_owner` present): hard cap of **100 physical pages** including all unnumbered front matter, chapter opener pages, maps, numbered content, conclusion, appendix, and blank pages. Never exceed 100; keep a 2-page reserve, so target 96-100.
- **Client deployment** (no `.genie_owner`): at Phase 0 ask the operator for the target or maximum page count (default near the competitor median, commonly 100-110, adjustable higher) and for their formatting preferences (trim size, body size, and whether venue entries run one or two columns). Honor their choices; compress intelligently to their budget.
Maintain a running page ledger after every phase with pages used, reserve remaining, and projected final count.

### Column Layout
| Page Type | Column Setting |
|---|---|
| Introduction pages | Single-column |
| Chapter opener pages | Single-column (full-bleed image) |
| Main travel content | Two-column (default) |
| Full-width lead paragraphs | Single-column insertion within two-column section |
| Wide tables, orientation maps, selected photographs | Single-column insertion within two-column section |

Use section breaks instead of manual tabbing. No heading, venue entry, or short list may be stranded at the bottom of a column without its first supporting lines (Keep with next, Keep lines together, controlled page breaks).

### Structural Unit — Venue / Experience Entry (Eleven-Point Template)
Every featured venue or experience uses this exact run-in structure. Each entry is designed to occupy **half a two-column page** (one of two entries per column-pair per page), achieving 80-90% page fill.

```
[1]  VENUE NAME (bold, Heading 3 style)
[2]  Area / District label | Cost band | Best Time to Visit  (meta line — italic or Accent B)
[3]  Address or location reference
[4]  Quick Facts table (2-column inline table: Operating Hours / Budget / Time Required / Accessibility / Best For)
[5]  Main description paragraph (justified, 3-5 sentences)
[6]  Insider Tip or Highlight callout (sidebar or indented block)
[7]  Reservation Note (where applicable)
[8]  Seasonal / closure note banded with "as of [season year]"
[9]  Inline photograph (1 per entry where space and usefulness justify)
[10] Original map reference or QR code to Google Maps web listing
[11] Volatile-fact band: all prices, hours, visa rules, route times, entry conditions labelled "as of [season year]"
```

**Two-entry-per-page law:** Venue/experience entries are laid out two per page in a double-column format. Entry containment is mandatory — an entry must not break across a page break mid-content. If an entry cannot fit in its half-page slot, carry it to the top of the next page as a pair. Aim for 80-90% fill on every content page; do not leave large white gaps.

### Section Divider Pages
Each major section transition (between district chapters, between the Ultimate Experiences block and the Itineraries block, etc.) receives a **full-width destination photograph** on a dedicated divider page. The divider carries:
- Full-bleed realistic photograph filling the chosen trim's production canvas (6.125 x 9.25 in at 6 x 9, or 8.625 x 11.25 in at 8.5 x 11)
- Section title on a solid Accent A or Accent B panel (centered, Heading 1 style, BLOCK LETTERS, 16 pt bold)
- Panel and title text remain within the 0.5-inch safe area
- No page number on the divider if within the front matter; divider pages within the numbered section count toward the physical page cap

### Exact Chapter Sequence (12 Required Functions)
Adapt chapter names to the destination; every functional block below must appear and be easy to locate:

| # | Function | Notes |
|---|---|---|
| 1 | Introduction and What To Expect | Single-column; sets scene, destination overview, reader expectations |
| 2 | Orientation Maps and Neighborhood / District Overview | Original generated maps; neighborhood quick-reference |
| 3 | Ultimate Experiences Guide | 15-20 top experiences; each uses full eleven-point entry template |
| 4 | Essential Itineraries and Planning | 3-day, 7-day, 14-day styled tables; budget summaries |
| 5-7 | Three Destination-Specific Regional / District / Route / Theme Chapters | Tailored to destination; two-column venue entries |
| 8 | Scenic Road Trips and Day Trips | Route tables, estimated drive times, day-trip venue entries |
| 9 | Where To Stay | Organized by area and budget tier (budget / mid-range / luxury) |
| 10 | Where To Eat | By category; seafood, vegetarian, pork-free emphasis |
| 11 | Transportation, Safety, Weather, Customs, Accessibility | Practical reference tables; no invented data |
| 12 | Emergency Contacts, Essential Phrases, Fast Facts | Phrase table, emergency number table, conversion chart |

**Back matter (counted in page cap):**
- Conclusion: approximately 1.5 pages — warm farewell, itinerary flexibility encouragement, brief honest-review request. No new major factual material.
- Appendix: destination-specific practical add-ons (see Content Rules for full list).

### Front Matter (Unnumbered)
Front matter is unnumbered and does not display a footer page number. It must feel premium and deliberate.

| Item | Page Count |
|---|---|
| Interior title or half-title page | 1 page |
| Copyright and disclaimer page | 1 page |
| Preface | Exactly 1 page |
| How To Use This Guide | Exactly 1 page |
| Table of Contents | 1-2 pages |
| Introduction chapter opener (full-bleed) | 1 page (transitions to numbered section) |

A **next-page section break** is inserted immediately before the Introduction. Visible Arabic numbering restarts at 1 at the Introduction. Footers unlinked from front matter.

---

## Interior Design

### Typography Hierarchy
All interior typography uses **Times New Roman** as the sole font family. No alternative interior fonts without explicit operator override.

| Element | Size | Style | Alignment |
|---|---|---|---|
| Heading 1 (chapter titles) | 16 pt | Bold, BLOCK LETTERS | Centered |
| Heading 2 (subchapters) | 13-14 pt | Bold, Capitalised | Left-aligned |
| Heading 3 (venue names / section labels) | 11-12 pt | Bold | Left-aligned |
| Body paragraphs | 11-12 pt (or 13-14 pt seniors) | Regular, justified | Justified |
| Table text, lists, addresses, quick-reference | Match body size | Regular | Left-aligned (never justified) |
| Captions | 9-10 pt | Italic or regular | Centered or left-aligned (consistent throughout book) |
| Page numbers | 9 pt | Regular | Bottom center |

**Paragraph rules:**
- No first-line indent on body paragraphs.
- Substantial, coherent paragraph blocks — avoid excessive one-sentence paragraphs.
- No em dashes anywhere in book content. Use commas, colons, parentheses, or ordinary hyphens.
- Bullets, numbered lists, checklists, step sequences, table text, addresses, and quick-reference material are left-aligned and never justified.

### Color Application
- **Accent A (darker):** Chapter-title panels, Heading 2 text, sidebar borders, rules, selected map labels, section divider title panels.
- **Accent B (brighter):** Table header rows (with white bold text), itinerary band headers, highlight callouts, cover title field, Quick Facts table headers.
- **Pale tint of Accent A or B:** Alternating table rows, sidebar backgrounds, callout backgrounds.
- **Body text:** Black on white or near-white backgrounds only.
- Every color choice must pass print-safety check: confirm contrast for white or black title text over the selected accent; avoid neon values; test important fills in grayscale to confirm information reads in print.

### Page Numbering and Section Control
- Front matter: no visible page numbers.
- Introduction onward: Arabic numerals, Times New Roman 9 pt, bottom center, restarting at 1.
- Section breaks control column changes, chapter openers, and front-matter/body-content separation.
- Neither the visible page number nor the physical page count may exceed the deployment page budget (studio owner: 100).

### Table Design Standard
All itinerary, budget, transport, phrase, weather, and conversion tables use:
- Accent B header rows with white bold text
- Alternating pale-tint rows
- Explicit fixed column widths
- Repeating header rows on multi-page tables
- Left-aligned cell text (never justified)
- Table header repetition enabled in Word

---

## Content Rules

### Volatile Fact Dating (Mandatory)
All prices, opening hours, visa rules, entry requirements, transport routes, ferry schedules, reservation systems, park fees, and border crossing conditions must be:
1. Verified from current primary or highly reliable official sources immediately before drafting.
2. Verified again during release QA.
3. Labelled in the text with the band: **"as of [season year]"** (e.g., "as of Summer 2026").
Do not invent exact hours, prices, or addresses. Where conditions vary or are uncertain, use a dated range or direct the reader to the official source via a tested QR code.

### Content Restriction — No Exceptions
- Never recommend, feature, depict, or link to bars, pubs, breweries, wineries, distilleries, cocktail lounges, drinking tours, tastings, or any alcohol-centred venue, dish, image, activity, or QR destination.
- Nightlife content means: live music, museums, cultural venues, family attractions, night markets, stargazing, evening walks, sunset viewpoints, and other alcohol-free entertainment only.
- Dining content avoids pork-based dishes. Emphasize seafood, vegetarian, and clearly described alternatives.
- This restriction applies without exception to: itineraries, maps, budgets, venue lists, captions, QR codes, chapter images, inline images, image generation prompts, and cover concepts.

### Entry Containment Law
- Venue/experience entries must not break mid-content across a page break.
- Two entries per page in double-column layout is the target fill structure.
- 80-90% page fill is the target. Large white gaps at the bottom of pages are a layout defect.
- When an entry cannot complete within its half-page slot, carry the entire entry to the next page.

### Image Rules
**Manifest slots (image contract):** every image is a numbered slot in `image_manifest.md`, each carrying `**Save as:**`, `**Prompt:**`, and `**Caption/alt:**`. Slot naming and generator: **photo slots** - `IMG-COVER` (cover), `IMG-OP-<SECTION>` (full-bleed chapter openers), and `IMG-<VENUE>` (inline venue and experience photos) - are generated in **Google Flow** via `uapf-flow-image-pipeline`. **Map slots** - `IMG-MAP-<NAME>` (original labeled maps) - are generated in **ChatGPT Image 2.0 (gpt-image-2)**, which renders the labeled illustrated maps that Flow does not. Lock a destination photography style once (season, light, palette, viewpoint) and repeat it verbatim in every photo prompt so the book stays coherent. A missing or unnumbered slot is a Gate-3 failure.
- Full-bleed chapter opener for every major chapter: unique realistic photograph filling the chosen trim's production canvas, clearly representing the chapter subject.
- Every inline image is realistic, sharp, relevant, culturally accurate, and unique — never reused from another chapter or another Pegasus Press title.
- All images must be free of: baked-in text, logos, watermarks, official seals, identifiable faces, alcohol, pork imagery, unsafe behavior, and inaccurate landmark combinations.
- Minimum resolution for chapter openers: 1838 x 2775 px at 6 x 9, or 2588 x 3375 px at 8.5 x 11. Inline images use high-resolution realistic photography.
- Images generated without text; chapter title and solid Accent A/B panel added in Word so spelling, translation, and TOC behavior remain controlled.
- When image generation is unavailable: insert a correctly sized placeholder and provide a complete manual generation prompt covering subject, destination, composition, camera viewpoint, lens feel, foreground, midground, background, lighting, season, weather, palette, cultural accuracy, resolution, central negative space, and all exclusions. Then continue to the phase gate.

### Map Rules
- All maps are original illustrations — never downloaded, screenshotted, traced, cropped, or adapted from Google Maps or any third-party map provider.
- Generate every map with ChatGPT Image 2.0 (gpt-image-2) as a brand-new original asset.
- Maps must be clearly labeled, simplified for print readability, and accompanied by a statement in the book that they are schematic.
- Every map reference in the book has a corresponding QR code directing the reader to the current Google Maps web listing of the relevant area or venue.

**Multi-map program (standard, not optional).** A single overview map is never sufficient. Every travel guide ships a *set* of maps:
- **One destination overview** (`IMG-MAP-OVERVIEW`) — the whole city/region broken into its named districts, for first-orientation. Placed in the orientation chapter.
- **One dedicated map per major district / area chapter** (`IMG-MAP-<DISTRICT>`) — a focused map of that area showing its labeled landmarks, key streets, the relevant river/coast, transit lines and stations, and a **dotted suggested walking or visiting route** connecting the chapter's sights. Placed at the head of that district's chapter.
- **Themed maps** whenever they help the reader and the page budget allows: itinerary route maps, food/market maps, transit maps, a sub-area or trail map for any district large or dense enough to warrant its own detail. Add **as many as the content warrants** — there is no upper cap beyond the page budget.
- **Minimum count = overview + one per district section** (a standard guide carries **4 to 5 maps at minimum**); scale up freely from there. A book with only one map is a Gate-3 map failure.

**Deployment-aware count.**
- **Studio owner** (`.genie_owner` present, ≤100 pages): fit the full map set inside the page cap — overview plus one per district; if district count is high, merge the smallest adjacent areas onto a shared map rather than dropping the per-district map program.
- **Client** (no marker): the client chooses page count and layout; scale the map set up with the page budget — one per district as the floor, then add as many themed, sub-area, and detail maps as the destination warrants until the page budget is reached.

**One locked map style across the whole book.** Fix a single cartographic style once and repeat it verbatim in every map prompt so the set reads as one hand: titled header block (map name + destination + map type), thin decorative border, soft pastel district fills on a warm cream ground, navy serif place labels, vermilion location pins, soft-blue water, hand-drawn landmark icons, dotted route lines, a compass rose, and a scale bar. **All labels in the book's language, correctly spelled — proof every map for text errors and regenerate or patch any misspelling before it ships.** Each map is a numbered `IMG-MAP-<NAME>` slot in the image manifest (see Image Rules); the map set is part of the book's uniqueness fingerprint, so no two titles reuse the same map style or arrangement.

### QR Code Rules
- Print size: 0.75-1.0 inch square with a clear quiet zone and adequate contrast.
- Scan every QR code from the final PDF at normal viewing size before delivery.
- Replace any redirect, dead link, or link that opens the wrong venue.
- Place QR codes beside the related entry or image without covering faces, landmarks, captions, or important photo detail.

### Legal and Ethical Safeguards
- Do not reproduce protected logos, official seals, copyrighted map screenshots, or official trade dress.
- Use non-affiliation language whenever the title or content names a park, authority, tourism board, event, attraction, transport brand, or commercial service that could appear official.
- Use non-identifiable people in generated images unless a properly licensed model image is deliberately supplied.
- Do not make medical, legal, immigration, safety, or accessibility guarantees. Use informational disclaimers and current official sources.
- Describe local customs, religious sites, safety, clothing, photography, and access requirements accurately and without stereotyping.
- Do not include fabricated quotations, testimonials, awards, bestseller claims, or review counts.

### Content the Fatal Flaw to Avoid
**Fatal flaw: Invented or unverified volatile facts presented without dating disclosure.**
Presenting specific prices, hours, or entry requirements as current fact without the "as of [season year]" band — or worse, inventing data — is the single most damaging error in a travel guide. It creates reader safety risk, refund exposure, and negative reviews. Every volatile fact must be sourced and dated. No exceptions.

### Appendix Selection
Choose and customize the most useful add-ons for the specific destination. Do not repeat the same appendix in every title. Options include:
- Printable packing checklist with climate and activity variations
- Trip budget planner and daily spending log
- Custom itinerary planner and reservation tracker
- Emergency information card and important-number worksheet
- Phrase cards and pronunciation quick guide
- USA and UK measurement, temperature, clothing-size, and currency conversion tables
- Accessibility planning checklist
- Seasonal, tide, trail, ferry, driving, border, pilgrimage, or festival planner as the destination requires
- QR-code index and map index

---

## QA Checklist

### Gate 1 — Configuration Complete (Phase 0)
- [ ] Exact operator title locked; no alteration made.
- [ ] Content language confirmed; all operator messages in English.
- [ ] Trademark clearance verdict recorded (CLEAR / CAUTION / HIGH RISK).
- [ ] Non-affiliation plan documented where CAUTION or HIGH RISK applies.
- [ ] Amazon competitor benchmark complete: minimum 10 titles, mean and median computed, recommended target page count within the deployment page budget.
- [ ] Author name generated from fakenamegenerator.com and formatted correctly.
- [ ] Subtitle candidates generated (3-5); recommended subtitle recorded with edition year and compliant keywords.
- [ ] Edition-year and season-year band confirmed and recorded.
- [ ] Two-accent palette selected with HEX, CMYK, and tint values; print-safety check passed; no duplicate with prior Pegasus Press titles.
- [ ] Body size and line spacing locked.
- [ ] Chapter map (12 functions) confirmed and adapted to destination.
- [ ] Estimated page ledger produced with allocation per chapter.
- [ ] Catalog uniqueness fingerprint recorded.
- [ ] Gate phrase delivered: "Type Proceed."

### Gate 2 — Front Matter and TOC Complete
- [ ] Interior title/half-title page uses exact locked title.
- [ ] Copyright page includes: copyright year, author name, All Rights Reserved, edition, Pegasus Press imprint, ISBN placeholder, third-party notice, non-affiliation statement, travel-information disclaimer, transportation/activity disclaimer, health/accessibility advisory, map and QR notice.
- [ ] Preface occupies exactly one page.
- [ ] How To Use This Guide occupies exactly one page; explains chapter flow, itinerary tables, Budget Impact, Time Required, Accessibility, map conventions, QR use, seasonal cautions, alcohol-free positioning.
- [ ] TOC generated through Word References automatic field (not typed page numbers); Heading 1, 2, 3 styles used; dotted leaders; right-aligned page numbers; indented Heading 2 entries; styled in Times New Roman.
- [ ] Next-page section break before Introduction; Arabic numbering restarts at 1; footer unlinked from front matter.
- [ ] Introduction chapter opener page generated with full-bleed image and Heading 1 title panel.
- [ ] Physical page count within cap; reserve confirmed.
- [ ] Page ledger updated.
- [ ] Gate phrase delivered: "Type Proceed."

### Gate 3 — Main Content Complete (All 12 Functions)
- [ ] All 12 functional content blocks present and easy to locate.
- [ ] Two entries per page double-column layout observed throughout venue/experience sections.
- [ ] Entry containment law upheld — no entry breaks mid-content across page break.
- [ ] 80-90% page fill achieved on all content pages (no large white gaps).
- [ ] All entries use the eleven-point template: Area/Cost/Best Time meta line + Quick Facts table + volatile-fact band.
- [ ] Every volatile fact (prices, hours, visa rules, transport times, entry conditions) labelled "as of [season year]."
- [ ] Section-divider pages inserted at major section transitions with full-width destination photograph and Accent A/B title panel.
- [ ] Three-day, seven-day, and fourteen-day itinerary tables present; Accent B header rows; alternating tint rows; explicit column widths; repeating headers.
- [ ] Budget summaries, transport tables, phrase tables, weather tables, conversion charts present and correctly formatted.
- [ ] Content-standards sweep passed: no alcohol, no pork imagery, no alcohol-centred venues in any itinerary, map, caption, image, or QR destination.
- [ ] All chapter openers have unique full-bleed realistic photographs with Accent A/B title panels inside the safe area.
- [ ] Inline images approximately one per substantial subsection; all unique, realistic, text-free, logo-free, watermark-free, face-free, alcohol-free, pork-free.
- [ ] All maps original (generated with ChatGPT Image 2.0 (gpt-image-2)); not sourced from Google Maps or third-party providers.
- [ ] Full map set present: one destination overview plus one dedicated map per district/area chapter (minimum 4 to 5 total, scaled to page budget); a single-map book fails this gate.
- [ ] Every map proofed for label spelling and correctness; misspellings regenerated or patched; one locked map style used across the whole set.
- [ ] QR codes present beside featured venues; 0.75-1.0 inch square with clear quiet zone; tested from mock PDF.
- [ ] Conclusion present; approximately 1.5 pages; warm farewell; honest-review request; no new major factual material.
- [ ] Appendix present with destination-appropriate add-ons selected.
- [ ] Physical page count within cap; reserve confirmed.
- [ ] Gate phrase delivered: "Type Proceed."

### Gate 4 — Release QA (Final)
- [ ] Physical page count within the deployment page budget (studio owner: 100 or fewer) with no hidden blank pages.
- [ ] Visible Arabic numbering starts at Introduction page 1 and runs continuously through the Appendix.
- [ ] Neither visible page number nor physical page count exceeds the deployment page budget.
- [ ] Live TOC resolves correctly: dotted leaders, correct hierarchy, correct page numbers — no manually typed entries, no placeholder text.
- [ ] Every listed Heading in TOC exists in the document; every page number resolves.
- [ ] Preface exactly one page; How To Use This Guide exactly one page.
- [ ] Conclusion approximately 1.5 pages.
- [ ] Every major chapter begins with a unique realistic full-bleed image and centered solid Accent A/B title panel.
- [ ] All text and title panels within the 0.5-inch safe area; only photographs and approved color fields extend to bleed.
- [ ] All images sharp, relevant, realistic, unique, culturally accurate, and free of text, logos, watermarks, alcohol, and pork imagery.
- [ ] All maps original and newly generated; schematic disclaimer present in book.
- [ ] All QR codes scan correctly from the final PDF at normal print viewing size; no dead links, no redirects, no wrong venues.
- [ ] Title unchanged from operator's exact supplied version; trademark verdict recorded.
- [ ] Non-affiliation language present where required.
- [ ] All volatile facts labelled "as of [season year]"; none invented; sources current as of production date.
- [ ] Edition-year marker present on copyright page and in metadata.
- [ ] Author name consistent on copyright page and in metadata; not on cover (unless operator override).
- [ ] Body font Times New Roman; heading hierarchy correct; list alignment correct; line spacing matches intake configuration.
- [ ] Two-accent color palette applied consistently; print-safety confirmed.
- [ ] No em dashes anywhere in book content.
- [ ] Content-standards final sweep: no alcohol, no pork, no non-compliant venues, images, or QR destinations.
- [ ] Legal, source-currency, spelling, grammar, and punctuation sweeps passed.
- [ ] DOCX and PDF render cleanly: no clipping, overlap, split headings, broken tables, stranded headings, or missing glyphs.
- [ ] Rolling master DOCX delivered (not disconnected chapter files); live TOC and page-number fields updated.
- [ ] Catalog uniqueness fingerprint confirmed; no duplicate of prior Pegasus Press title.

---

## KDP Positioning

### Amazon Category Tree
Primary categories (English-language titles):
- Books > Travel > Destination Guides
- Books > Travel > [Continent] > [Country/Region]

Secondary categories based on destination specificity:
- Books > Travel > Special Interest > Adventure
- Books > Travel > Special Interest > Family Travel
- Books > Travel > Budget Travel
- Books > Travel > Road Travel

Select the two most specific and highest-traffic categories for the destination after confirming with Amazon's current category browser.

### Description Strategy
The KDP description leads with:
1. **The destination hook** — one sentence naming the destination and its primary draw (e.g., "Discover [Destination] — [key attraction or theme] — through the most practical and complete guide available for [year].")
2. **The reader-value proposition** — what this guide solves (planning overwhelm, unfamiliar destination, family travel logistics).
3. **Format proof points** — two-column layouts, original maps, QR codes, three itinerary lengths, pork-free dining coverage, tested venue entries.
4. **Trust signals** — volatile facts dated to the current season-year, disclaimer transparency.
5. **Call to action** — "Grab your copy and start planning your [Destination] trip today."

Use relevant keyword phrases naturally in the description:
- "[Destination] travel guide [year]"
- "[Destination] travel guide for [audience] [year]"
- "[Destination] trip planner"
- "[Destination] city guide"
- "[destination] family travel guide"
- "family travel [destination]"

### KDP Metadata Signals
- **Title field:** Exact operator title (locked; never altered for SEO without explicit operator instruction).
- **Subtitle:** Operator-approved subtitle; if auto-generated in Phase 0 from the framework, include key destination name, year, and primary benefit.
- **Keywords (7 slots):** Rotate through: [destination] travel guide, [destination] travel [year], [destination] trip planner, [destination] family travel guide, [destination] city guide, [destination] vacation guide, [destination] tourist guide.
- **Language:** Set to the content language of the book.
- **Publication date:** Current year per the copyright page.

---

## Key Rules — Do NOT Break

1. **Title fidelity is absolute.** The operator's exact supplied main title is locked at Phase 0. Never rewrite, shorten, optimize, translate, or replace it — even if it appears risky — without explicit operator instruction. A clearance concern is reported; the title is changed only by the operator.

2. **Page budget is deployment-aware.** Under the studio-owner deployment (`.genie_owner` present) the hard cap is 100 physical pages and is never relaxed. Under a licensed client deployment the operator sets the page budget (default near the competitor median) and formatting preferences. Compress intelligently when content pressure builds.

3. **Two entries per page double-column layout is mandatory in venue/experience sections.** Entry containment is non-negotiable — entries must not break mid-content across page breaks. 80-90% page fill is the target on all content pages.

4. **Every volatile fact must carry a "as of [season year]" band.** Prices, opening hours, visa rules, transport routes, entry requirements, and reservation systems are time-sensitive. They must be verified from current primary sources and dated. Never invent or present unverified volatile facts as current fact.

5. **The edition-year marker is mandatory.** It appears on the copyright page and in KDP metadata. It may not be omitted.

6. **Content restrictions are a zero-tolerance rule.** No alcohol, no pork imagery, no alcohol-centred venue, dish, activity, image, caption, map, QR destination, or cover concept — in any form, at any point in the manuscript, deliverables, or production prompts. No exceptions.

7. **All maps must be newly generated originals.** Using ChatGPT Image 2.0 (gpt-image-2). Never download, screenshot, trace, crop, redraw from, or otherwise take another party's map because of copyright risk. Every map in the book is a brand-new original created specifically for the title.

8. **All QR codes must be tested from the final PDF.** At normal print viewing size. Scan every code. Replace any dead link, redirect, or wrong-venue destination before delivery.

9. **Chapter openers are compulsory full-bleed originals.** Every major chapter begins with a unique realistic full-bleed photograph. Never reuse an opener image, viewpoint, landmark crop, or opener composition from another chapter or another Pegasus Press title. Generate images without baked-in text; add the title panel in Word.

10. **The TOC must be a live Word References automatic field.** Never type page numbers into the TOC. Never fake headings with direct bold formatting. All navigational headings must be real Word Heading styles (Heading 1, 2, 3) restyled in Times New Roman. The delivered DOCX must open with resolved, correct TOC entries.

11. **Section-divider pages with full-width destination photographs are required** at all major section transitions. These count toward the physical page cap.

12. **No em dashes anywhere in book content.** Use commas, colons, parentheses, or ordinary hyphens as alternatives.

13. **Catalog uniqueness is enforced.** Every OV-TRAVEL title receives a unique cover composition, image sequence, palette, chapter-opener treatment, regional organization, and visual fingerprint. No two Pegasus Press travel guides may look the same.

14. **Production gates are hard stops.** Complete all tasks within an approved phase, including automatic image generation, then stop with the exact gate phrase "Type Proceed." Do not advance to the next phase without the operator's explicit instruction.

15. **Rolling master DOCX — never disconnected files.** Maintain one rolling master Word document from front matter through Appendix. Do not deliver disconnected chapter files as the primary manuscript.

## HOUSE REFERENCE BANK — TRAVEL GUIDES (2026-08-14)

Six catalog masters are banked at `cover_db/_interiors/travel/` (local only,
never shipped): Japan, Yosemite, Utah National Parks, Acadia, Iceland, and
New Orleans. BINDING for every travel guide on BOTH engines (Claude and
Codex) and on every install; where the bank folder is absent (client
installs never receive it), the codified standards below carry the full
weight of the reference study. CONSULT the masters where present: open 2 or
3 and study a section banner page, a feature-panel spread, and a photo
divider.

Standards verified across the bank:

* HEAVILY ILLUSTRATED 90-100 page guides: photography on half to nearly all
  pages; full-bleed scenic photo pages as chapter/section dividers; inline
  destination and food photography stacked within columns.
* TWO-COLUMN BODY with justified prose, 11 to 13 pt; bold section heads;
  large ALL-CAPS centered section banners in the book's accent color (the
  New Orleans "NIGHTLIFE AND ENTERTAINMENT" form).
* TINTED FEATURE PANELS: column-width or full-height colored panels carrying
  a spotlight subject (a restaurant, a district, a trail) with bold lead-in
  phrases; each book runs its own panel color family.
* DIRECTORY ENTRY PATTERN: venue and site entries with the name in bold
  (address in parentheses) followed by bold lead-in labeled lines: Price
  Range:, Atmosphere:, Operating Hours:, Cultural Value:, Unique Feature:,
  and similar, chosen per book.
* RUNNING HEADER band with the guide title in the accent color; visible
  folio (the "Page 41" centered form or a corner folio).
* ONE ACCENT SYSTEM PER BOOK, NO REPEATS: the masters run teal, orange-red,
  green, and other distinct systems. NO TWO TRAVEL GUIDES share the same
  palette, panel family, banner treatment, or layout fingerprint
  (No-Two-Books-Alike, operator restated 2026-08-14).
* TRIM (operator confirmed 2026-08-14): every travel guide is 8.5 x 11
  inches. The banked masters run smaller 6 x 9 family trims; apply their
  PATTERN (banners, panels, two-column body, directory entries,
  photography) scaled up to the 8.5 x 11 page, where the binding heading
  law also governs (chapter titles in BLOCK LETTERS at 28 pt or larger,
  subchapter headings 14 to 18 pt, nothing cut off). The masters' trim is
  never copied.

## MAPS (operator directive 2026-08-14, every travel guide)

* MINIMUM FOUR MAPS per travel guide, placed where they serve the reader:
  a destination overview map early in the book, plus regional or area maps,
  itinerary or route maps, and district, park, or trail maps as the
  destination demands. More than four whenever the content calls for it;
  four is the floor, never the target.
* GENERATION: maps are produced with the image engines. CODEX (native
  gpt-image-2) is the default map generator, and Google Flow
  (uapf-flow-image-pipeline) is used where necessary, following each
  engine's image timing (Codex inline while drafting; Claude engine after
  all chapters are merged). Map prompts are comprehensive: region shape,
  key locations, routes, label text spelled exactly, style, palette tie-in
  to the book's accent system.
* STYLE AND HONESTY: maps are styled orientation and planning maps in the
  book's design fingerprint, not survey-grade cartography. Geography must
  be faithful: real places, correct relative positions, correct names
  verified against research sources; never invent a place, road, or label.
  Every label must be legible and spelled correctly on the rendered page.
* LAWS THAT APPLY: margin and caption law (each map is a numbered Figure
  C.N with a caption beneath), containment verified in render QA, and the
  No-Two-Books-Alike law (each guide's maps carry that book's unique
  palette and motif treatment).
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
