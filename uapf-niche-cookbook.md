---
name: uapf-niche-cookbook
description: Cookbook / recipe-collection overlay (OV-COOK) — invoked by uapf-phase0-router when the title contains recipe, cookbook, baking, cooking, cuisine, food, meals, kitchen, chef, or diet (recipe-format), or the format is recipe-collection.
---

# UAPF Niche: Cookbooks (OV-COOK)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in
> `frameworks/UCGF-1.0/` (config, validation, phases, deterministic ops in `genie_cookbook.py`).
> This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp
> `framework=UCGF 1.0` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** the title contains any of: *recipe, recipes, cookbook, baking, cooking, cuisine, food, meals, kitchen, chef*, or *diet* used in a recipe-collection sense (e.g. "Mediterranean Diet Recipes", "Keto Diet Cookbook"), or the declared format is **recipe-collection**. A diet title that is prose/education-only (no recipes promised) does NOT route here.

## INTERIOR FORMATTING STANDARDS (Operator-Confirmed 2026-08-14)

These rules are binding on BOTH the Claude engine and the Codex engine, on operator and client installs equally. They override any conflicting default in this skill, any framework template, or any prior instruction.

### 1. Chapter Titles — NO LABEL, ALL CAPS, 30 pt minimum
- **No label line above the title.** The small accent-color label (e.g., "Front Matter", "Guide", "Introduction") that previously appeared above the main chapter title is permanently removed. Chapter openers have ONE element: the title only.
- **ALL CAPS.** Every chapter title must be rendered fully uppercase.
- **30 pt minimum, bold, primary palette color.** Never below 30 pt.
- **No margin clip.** Title paragraph has zero left and right indent; word wrap is unrestricted. The title wraps within the text area and never overflows or clips at the margin.

### 2. Subheadings — 15 pt, bold, primary color
- **15 pt** (within the operator-confirmed 14–18 pt band), bold, primary palette color.
- No margin clip — same word-wrap rules as chapter titles.
- Space before: 14 pt; space after: 5 pt.

### 3. Introduction Page
- The Introduction chapter opener uses **"INTRODUCTION"** as the sole title. No thematic subtitle below it (e.g., never "INTRODUCTION" + "The Quiet Crisis in Your Kidneys"). One heading only.
- Length: **exactly 1.5 rendered pages** (~900–1000 words including callout panels). Pages must be visually full — no white space at the bottom of the final page.

### 4. Page Numbering — Front Matter Unnumbered, Body Starts at 1
- **Front matter is unnumbered.** IMG-00, copyright page, preface, how to use, and TOC carry no footer page number.
- **Numbered pages start at the Introduction page, at Arabic numeral 1.** Footer: centered, primary palette color, 10 pt Times New Roman.
- **DOCX implementation:** use a next-page section break before the Introduction paragraph. Section 1 (front matter) has `pgNumType fmt="none"` and an empty footer. Section 2 (body, starting at Introduction) has `pgNumType fmt="decimal" start="1"` and a footer with a `PAGE` field.

### 5. Table of Contents — Built Last, Accurate Page Numbers
- The TOC is assembled only after the complete book is written and all page counts are final. It is never built with estimated or placeholder page numbers in the delivered DOCX.
- **DOCX implementation:** a Word auto-TOC field (`TOC \o "1-3" \h \z \u`, `dirty="true"`) so the operator can update it in one click after any edit. The operator sees "Right-click and Update Field" instruction until the field is updated.

### 6. Subchapter Content Density — Minimum Half a Page per Section
- Within educational chapters, recipe chapters, and the appendix, content under each subheading must occupy at least half a page when rendered.
- Achieve via prose (200+ words) or prose combined with callout panels. Never leave thin content under a heading — expand or merge sections until the half-page floor is met.

### 8. Chapter-by-Chapter Build Order — Binding on Both Engines
- **Never build all recipe chapters at once.** Build one chapter at a time, deliver its DOCX preview, then automatically advance to the next chapter without waiting. This applies to recipe chapters and educational chapters alike.
- After delivering each chapter preview, immediately begin the next chapter without pausing.
- **No chapter number in recipe chapter dividers.** The chapter divider header bar shows the chapter TITLE only (e.g., "BREAKFAST", "SMOOTHIES"). Never include "Chapter One", "Chapter Two", or any chapter number label in recipe chapter headers. The title alone is sufficient.
- This rule is binding on BOTH the Claude engine and the Codex engine, on operator and client installs equally. It cannot be overridden by autopilot flags or any other instruction.

### 7. Educational Chapters — Minimum 3 Pages Each, with Important Concept Explanation
- **Every educational chapter that precedes the recipe chapters must be a minimum of three rendered pages.**
- **Each educational chapter must include, where possible, a dedicated section or callout panel that explains an important concept relevant to that chapter's topic** — for example, a "Key Concept" box, a mechanism explanation, a clinical principle, or a how-it-works breakdown that gives the reader genuine depth, not just a list.
- Target word count: approximately 1,500–1,800 words of body text plus panels per chapter to reliably reach 3 rendered pages at 11 pt TNR.
- This rule applies to both the Claude engine and the Codex engine, on operator and client installs equally.

### 9. Recipe Card Standard — Universal Professional Format (10-Book Synthesis, 2026)
**Derived from 10 operator-supplied reference books including: Kidney Disease Stage 4 Cookbook for African Canadians, High-Protein Mason Jar Salad Cookbook, Mediterranean Diet Cookbook for African Canadians (120 and complete editions), Salades en Bocal Hyperproteinées, Histaminarmes Kochbuch, Das 15-Minuten High-Protein Kochbuch, Heissluftfritteuse für Senioren ab 60, and the High-Protein Freezer Meals reference. Binding on BOTH engines, all installs. No two books share the same palette, layout fingerprint, or decorative system.**

**Universal patterns confirmed across all 10 books:** 2 recipes per page (half-page each); compact single meta line (Prep/Cook/Serves); ingredients as a clean bullet list; 3–4 numbered steps; nutrition as a single line at the bottom; running chapter header on every recipe page; STORAGE/SAFE note per recipe.

#### 9a. Recipe card anatomy (in order, top to bottom):
1. **Title bar** — recipe number + name in ALL CAPS, bold, on accent-colored background. Full page width.
2. **Description** — one italic line capturing the recipe's appeal (10 pt, gray).
3. **Meta line** — `Serves X | Prep X min | Cook X min | Total X min` (9 pt, italic, gray). One compact line only.
4. **Image placeholder** — compact shaded box; included in the overflow budget. Never omitted.
5. **2-column table** — Ingredients (left, panel-green bg) | Instructions (right, panel-amber bg). No visible borders.
6. **Storage line** — `STORAGE:` (bold, primary color) + one sentence on refrigerator and freeze life, written inside the instructions column after the last step.
7. **Optional RENAL TIP or SWAP line** — `RENAL TIP:` (bold, accent color) + one sentence of kidney-specific guidance, OR `SWAP:` + one practical substitution suggestion. Written inside the instructions column after the STORAGE line, only when genuinely useful. Not every recipe needs one.
8. **Per Serving bar** — single compact line: Cal | Protein | Carbs | Fat | Sodium | Potassium | Phosphorus, full width, panel-green bg, primary color text.

#### 9b. Instructions — compressed numbered steps (STEP COMPRESSION LAW, operator directive 2026-08-14):
- **Every step is ONE direct imperative sentence, maximum 15 words, fitting within TWO rendered lines** at the recipe body size. Multi-part actions are split into separate numbered steps, never packed into one.
- **Step anatomy within the 15 words:** action + the essential detail or doneness cue where it fits ("Cook onion in hot oil 4 to 5 minutes until translucent."). Tips, technique notes, and "why" context go in the recipe's optional "Note:" line ONLY, never inside steps.
- **Step count follows the recipe:** as many compressed steps as the method truly needs; split rather than pad.
- **Column fill:** the instructions column reaches its fill through the compressed steps plus the STORAGE line and the "Note:" line, never by padding steps. A step that overflows two rendered lines is a layout failure: rewrite it or split it before the chapter gate.
- **No overflow:** the entire recipe block — title bar, description, meta, image placeholder, 2-column table, and Per Serving bar — must fit within its half-page slot. Adjust step wording to fit. Never shrink type or spill into the next recipe's space.

#### 9c. Chapter divider pages — OPENER VARIATION LAW (operator directive 2026-08-19):
Chapter dividers must NEVER look the same from book to book. Each book locks ONE
divider archetype at fingerprint time from this menu (international cookbook
standards), and no two catalog cookbooks may share the same archetype + title
arrangement combination:

1. **Photo-below**: title band at top, hero image beneath, intro under the image (the former default; now one option among many).
2. **Photo-above**: full-width hero image at top, title on clean white BELOW the image, colored rule between, intro beneath.
3. **Side-band**: image occupies the left or right third of the page; title and intro sit in the clear column beside it, never on the image.
4. **Full-bleed + text plate**: edge-to-edge image with the title on a SOLID color plate/panel placed over or beside it (title on the plate, not raw on the photo).
5. **Recipe visual art**: illustrated food art instead of photography — watercolor, gouache, or ink line art of the chapter's dishes or ingredients; title on clean space clear of the art. (The illustration style is locked per book and counts as part of the fingerprint.)
6. **Ingredient motif frame**: a decorative border of ingredient motifs framing the page; title centered inside the clear field.
7. **Collage grid**: 3 or 4 dish thumbnails in a grid; title in its own band above or below the grid.
8. **Minimalist spot art**: small centered illustration or icon + large title + generous white space.
9. **Text-on-image**: title set directly on the photo with a contrast scrim. This is an OCCASIONAL archetype, never the default: text sitting on the image in every book is exactly the sameness this law kills. When used, legibility is verified on the rendered page and in grayscale.

Constant across ALL archetypes: chapter TITLE only (no chapter-number labels),
no recipe content on the divider, one-paragraph chapter introduction (11 pt,
justified) placed per the archetype, page break after (recipes begin on the
next page), and grayscale legibility. The title arrangement itself (top band /
below image / side column / plate) is a fingerprint axis and must vary across
the catalog.

#### 9d. Running page header on recipe pages:
- Every recipe page carries a running header: book title (abbreviated) left-aligned in small caps, primary color, 8 pt; page number right-aligned in primary color, 8 pt.
- Implemented as a Word section header linked to the body section.

#### 9e. Educational chapter callout style (reference standard):
- Bold ALL-CAPS label followed by a colon and a single space, then the callout body in the same paragraph. Example: `LEACHING RULE: Boil the vegetable in a large volume of water…`
- Light panel background (panel-green or panel-amber), 10 pt body text.
- No heavy border rules on callouts — the background shade is the only visual container.

#### 9f. No-two-books-alike constraint:
- The structural rules above are constant. The palette (primary + accent colors), the exact panel tones, the header bar styling, the decorative motifs, and the fingerprint arrangement are UNIQUE per book.
- This book's fingerprint: Deep Forest Green PRIMARY (#2D6A4F) + Warm Amber ACCENT (#E9A14D), amber title bars on recipes, green Per Serving bars, green header bars on chapter dividers.
- No future cookbook may share this exact combination.

---

## Expert Panel

1. **Executive Chef / Recipe Developer (Domain Master)** — owns recipe correctness: ingredient ratios, technique, temperatures, doneness cues, yield. Every recipe must execute exactly as written.
2. **Registered Dietitian / Nutrition Analyst** — owns Per Serving lines (USDA FoodData Central base values), theme-nutrient selection, meal-plan nutritional balance, and honest, non-medical claims.
3. **Cookbook Interior Designer** — owns the two recipe-card archetypes (compact two-column and full-width stacked), the two-color scheme, the locked food-photography style, divider composition, and fill discipline.
4. **Content-Standards Auditor** — silently screens every recipe, ingredient, substitution, meal plan, shopping list, and image concept for pork derivatives and alcohol in any form, including hidden carriers.
5. **KDP Category Strategist** — owns title-market intelligence, subtitle optimization, category-tree placement, and description copy.

## Phase 0 — Title Analysis

Execute in order the moment the title arrives, before any other work.

### 0.1 Title Clearance (Trademark + Market)

1. Web-search the quoted title + "trademark" and the quoted title + "book". Confirm the title contains no third-party brand or registered mark (banned examples: Instant Pot, Ninja, Ozempic, Whole30, Glucose Goddess, Weight Watchers).
2. Search the exact phrase, close variants, and main seed words in the target Amazon marketplace (cookbook category). Review the top current competitors for positioning, audience specificity, bestseller rank, review strength, recency, price, page count, and repeated keyword patterns.
3. Classify the supplied title: **STRONG / WEAK / SATURATED / RISKY** with concise evidence.
   - STRONG → preserve verbatim; it becomes the locked title.
   - WEAK / SATURATED / RISKY → extract the main seed words, generate 5–10 niched-down alternatives that **retain the seed words**, give each a reason and a score across demand, competition, buyer intent, differentiation, and trademark safety, then auto-select the highest-potential compliant option. No rank or sales guarantee is ever stated.
4. **Title Lock:** the selected title is immutable character-for-character across manuscript, TOC, cover handoff, metadata, and State Block.

### 0.2 Subject Analysis and Auto-Configuration

- **Language:** the dominant language of the locked title governs the entire book (recipes, education, meal plan, appendix, disclaimer). System-side communication stays English. RTL scripts trigger RTL paragraph direction at formatting; geometry is unchanged.
- **Recipe count:** read from the title (a title containing "90 Recipes" fixes it at 90). If absent, ask once, then proceed. The count drives the page budget.
- **Author identity:** pull one random identity live from fakenamegenerator.com, format *First I. Surname*, screen against the Author Log and against real chefs/authors/public figures. Place on cover, copyright page, and preface signature; append to the Author Log.
- **Theme nutrient:** derive from the diet/theme (e.g. anti-inflammatory → Omega-3; keto → Net Carbs; diabetic → Sugar; heart → Sodium). It ends every Per Serving line.
- **Categories:** ~8–12 single-noun categories (BREAKFAST, SMOOTHIES, SALADS, SOUPS, SEAFOOD, POULTRY, MAINS, SIDES, SNACKS, DESSERTS...). Compounds only when a chapter genuinely spans two classes. The set must cover breakfast, lunch, dinner, and snack so the meal plan can be assembled entirely from the book. No category below 6 or above 15 recipes.
- **Plan duration:** 30-day default; 60-day only when the title demands it.
- **Page budget and recipe layout (deployment-aware):** check for a `.genie_owner` marker file in the install root.
  - **Studio owner deployment** (`.genie_owner` present): the page count is hard-locked to 100 or below, and the archetype auto-rotates per book for No-Two-Books-Alike. Do not prompt.
  - **Client deployment** (no `.genie_owner`): ask the operator once for (a) the target or maximum page count (default 100; they may set it higher) and (b) the recipe layout, single-column full-width stacked (Archetype B) or double-column compact (Archetype A). Honor both for the whole book. Client installs never carry `.genie_owner`; the delivery installer does not create it.
- **Design DNA (no two cookbooks alike, expanded 2026-08-19):** compose a unique design fingerprint and log it in the Design Log. The fingerprint combines SIX axes: (1) recipe archetype (the twelve-option Recipe Arrangement Variation Law menu, A through L: compact two-column, full-width stacked, ingredient sidebar, magazine band, boxed card, centerline minimalist, icon-cue rail, photo banner, ledger, journal, two-tone split, plated focus); (2) a unique two-color palette (primary + accent); (3) chapter divider archetype (the nine-option Opener Variation Law menu: photo-below, photo-above, side-band, full-bleed + text plate, recipe visual art, ingredient motif frame, collage grid, minimalist spot art, occasional text-on-image with scrim) including the title arrangement; (4) divider imagery mode (food photography vs illustrated recipe art: watercolor / gouache / ink line); (5) step-numbering style (plain, oversized colored, or circled numerals); (6) meta-line format (pipe-separated, small-caps labels, or tag chips). No two catalog cookbooks may share the same palette, the same recipe-archetype + palette-family combination, or the same divider archetype + title arrangement; text-on-image dividers are never the default across consecutive books. On any collision, vary the palette first, then the archetypes, until the design is visibly distinct. Under the studio-owner deployment the fingerprint is auto-composed (auto-rotating both archetype menus); under a licensed client deployment the operator's stated preferences are honored and the other axes are varied for uniqueness.
- **Recipe set uniqueness:** fingerprint every proposed recipe (normalized title, principal ingredients, method, flavor profile, serving form) against the catalog Recipe Log. Exact copies, renamed copies, and near-duplicates are prohibited; a similar recipe must differ materially in at least three of: principal ingredient, technique, seasoning/sauce, texture/form, pairing, presentation.

### 0.3 Subtitle Generation

Generate four Amazon-optimized subtitle candidates internally; self-select the strongest and report only the winner with reasons. Criteria: primary search keyword early; recipe count stated explicitly; target audience or quantified benefit named; title + subtitle ≤ 150 characters (~125 ideal); no third-party brands, no em dashes, no all-caps words, no unverifiable medical promises.

### 0.4 Phase 0 Output

Report: trademark verdict, supplied title, seed words, market verdict + evidence, alternatives with scores (if generated), selected locked title + reason, subtitle, language, author, recipe count, categories, plan duration, theme nutrient, palette, page projection. Then present the TOC gate.

## Book Architecture

### Front-to-Back Sequence

1. Cover (cover pipeline handoff: title, subtitle, author, primary color, uniqueness constraint)
2. Full-page theme photograph (IMG-00: overhead flat-lay of hero ingredients, full-bleed)
3. Copyright page + medical disclaimer (framework template, translated if needed)
4. Preface — exactly one page, author voice, signed
5. How to Use This Cookbook — exactly one page (recipe anatomy, plan/appendix interlock, measurement conventions, USA/UK chart pointer)
6. Table of Contents — live Word auto-TOC, two columns, dotted leaders; front matter unnumbered, visible numbering starts at the Introduction
7. Introduction — three subsections: reader's problem with statistical hook (180–260 words); the science and its three levers (160–220 words); how to use (120–180 words)
8. Educational Chapter 1 — theme science: mechanisms, key nutrients, benefits, misconceptions; every claim carried by at least two named credible sources
9. Educational Chapter 2 — kitchen application: techniques, spice synergies, meal prep, storage, USDA-safe temperatures (poultry 165 F / 74 C, fish 145 F / 63 C, refrigeration ≤ 40 F / 4 C)
10. Recipe chapters — each opens on a full-page category divider, then recipe pages
11. Conclusion — exactly 1.5 pages, four movements: promise recapped with numeric targets; the plan's arc and outcomes; sustainable next steps; honest-review request
12. Appendix — food lists (Enjoy Freely / Eat in Moderation / Avoid); day-by-day meal plan (one table per week: Day | Breakfast | Lunch | Snack | Dinner, every cell a recipe from this book, weekly Goal line above, Nutrition Highlights beneath, weeks named on the Reset / Balance / Optimize / Sustain arc); weekly shopping lists grouped by store department with exact quantities and Replenish sections from week 2; USA and UK serving-measurement charts

### Structural Unit: the Recipe Page

**TWO RECIPES PER PAGE, and every recipe carries its own finished-dish photo.** A recipe never splits across a page. RECIPE ARRANGEMENT VARIATION LAW (operator directive 2026-08-19): the recipe arrangement must NEVER be the same from book to book. The book uses ONE archetype from this menu (international cookbook standards), chosen per book, recorded in the State Block, and no two catalog cookbooks may repeat the same archetype + palette-family combination:

- **Archetype A - Compact two-column.** Two equal columns, one complete recipe per column. Each recipe carries a bordered finished-dish photo, and the photo position alternates (one recipe photo-top, the other photo-bottom) for page rhythm. Each recipe plus its photo fills 80-90% of its column.
- **Archetype B - Full-width stacked.** Two recipes stacked, each spanning the full text width: a large finished-dish photo column on one side and the recipe text on a tinted panel on the other, with oversized stylized step numerals and an italic one-line dish description under the title.
- **Archetype C - Ingredient sidebar (French/Larousse style).** Two recipes stacked full-width; within each, ingredients sit in a narrow tinted side strip (left or right, locked per book) with the method dominant beside it; photo anchors the opposite corner.
- **Archetype D - Magazine band.** Two recipes stacked; each opens with a horizontal band carrying title + meta + photo thumbnail, ingredients and method side by side beneath the band in two sub-columns.
- **Archetype E - Boxed card.** Each recipe is a self-contained tinted card with a colored header bar (title + meta in the bar), two cards per page with white space between; photo inset top-right or top-left of its card, alternating.
- **Archetype F - Centerline minimalist (Scandinavian).** Airy, typographic: each recipe centered on its half of the page, thin hairline rule between the two recipes, centered title, ingredients as a narrow centered column, steps beneath; small rounded-corner photo inset; generous white space is the style.
- **Archetype G - Icon-cue rail.** A slim vertical accent rail beside each recipe carrying small technique and time icons (whisk, flame, clock) keyed to the steps; title and meta at top, ingredients left of the method, finished-dish photo as a top corner anchor. Modern meal-kit aesthetic.
- **Archetype H - Photo banner.** Each recipe opens with a full-width shallow landscape crop of the finished dish as a banner; title + meta on clean space directly UNDER the banner (never on it), ingredients and method in two sub-columns beneath.
- **Archetype I - Ledger (classic European).** Purely typographic, no tinted panels: ingredients set as a two-column quantity | item mini-table with hairline rules, method as compact numbered lines, photo bottom-anchored; elegant serif-forward look.
- **Archetype J - Journal.** Handbook feel: title with a decorative underline motif, meta as small tag chips, ingredients as a checklist with square glyphs, numbered method, photo in a framed keepsake-style border with a thin caption strip.
- **Archetype K - Two-tone split.** Bold color-blocking: each recipe splits into a solid-color panel (title, meta, and ingredients reversed in white on the book's primary color) and a white panel (method + photo). High contrast, modern trade look; grayscale legibility verified.
- **Archetype L - Plated focus.** The finished-dish photo is a round top-down plate crop at the top center of each recipe unit, title directly beneath, ingredients and method in two narrow columns below; the circular crop is the signature.

Every archetype keeps exactly two recipes per page, one photo per recipe, full step-compression and containment compliance; they differ in geometry and styling only. Select per the deployment page-and-layout policy (a licensed client may state a preference; the studio owner auto-rotates through the menu); never mix archetypes within one book. The menu exists to make catalog repetition impossible: with twelve arrangements crossed against palettes, no two cookbooks ever read as siblings.

Recipe anatomy (both archetypes), top to bottom:

- **Number + Title** — "N. Recipe Name", bold, primary color
- **Description** — one italic sentence on flavor and appeal (required in Archetype B, optional in A)
- **Meta line** — accent color, bold: Prep | Cook | Total | Servings | Difficulty
- **Ingredients** — accent-color label; bulleted, strictly in order of use; every quantity with a metric conversion in parentheses (1 tsp = 5 ml, 1 tbsp = 15 ml, 1 cup liquid = 240 ml; weights ingredient-specific from USDA gram equivalents, never a flat guess)
- **Method** — accent-color label; 3 to 5 steps as a fresh native Word numbered list **restarting at 1 for every recipe**; each step complete and detailed; temperatures as F with C in parentheses; doneness cues; set inside a panel tinted with the accent color
- **Per Serving** — primary color; calories to nearest 5, macros to nearest 1 g, ending with the theme nutrient (one decimal where meaningful)
- **Finished-dish photo** — one per recipe (manifest slot IMG-Rnn, see Image Production Contract), bordered, kept inside the trim-safe zone

Optional per recipe: a one-line italic "Storage" or technique "cue" note (used in Archetype B).

### Category Divider Page

One full page opens each recipe chapter (manifest slot IMG-D-<CATEGORY>),
composed per THIS BOOK'S locked divider archetype from the OPENER VARIATION
LAW (section 9c): photo-below, photo-above, side-band, full-bleed + text
plate, recipe visual art (watercolor/gouache/ink illustration of the
category's dishes), ingredient motif frame, collage grid, minimalist spot
art, or (occasionally, never as a default) text-on-image with a contrast
scrim. Constants for every archetype:

1. The divider imagery (photo or illustration) depicts the category's
   signature dish and/or ingredients in the book's locked imagery mode and
   palette, generated TEXT-FREE (any text lives in typeset elements, never
   inside the art).
2. The **category title** (title only, no chapter numbers) plus **one italic
   subtitle line** (a short evocative promise) are typeset per the locked
   title arrangement: band, plate, clear column, or clean field, as the
   archetype dictates. Text sits ON the image only in the text-on-image
   archetype, always on a scrim, always grayscale-verified.
3. Essential image detail stays inside the trim-safe zone; the composition
   must render identically legible in grayscale.
4. The archetype and title arrangement are fingerprint axes: they never
   repeat across catalog books (Design DNA law).

### Page-Band Targets

- Total length, front matter included: **honors the deployment page policy** (studio owner: hard-capped at 100; licensed client: the operator's chosen budget, default 100) at trim size.
- Governor formula: Pages = 6 (front matter) + 6 (intro + education) + C (dividers) + ceil(R / 2) (recipe pages, two per page) + 2 (conclusion) + A (appendix; 12 for 30-day plan, 20 for 60-day).
- On breach, compress in fixed order with operator warning before the last step: (1) appendix density, (2) educational depth (6 → 4 pages), (3) recipe count.

## Interior Design

- **Trim:** 8.625 x 11.25 in, 0.7 in margins, bottom-center page numbers. Full-color professional interior.
- **Body type:** **11 pt Times New Roman** (overrides the UAPF 12 pt default). Category titles and headings may use a complementary display treatment, but body, ingredients, and procedure text are 11 pt Times New Roman.
- **Color scheme:** exactly **two colors — primary + accent** — plus black body text. Primary carries category titles and major headings; accent carries chapter labels, procedure-box tint, rules, and small accents. Body text never takes color. **No two Pegasus catalog cookbooks share the same palette** — audit the Palette Log before locking; on collision, generate a new pair.
- **Layout template:** one of the two recipe archetypes (compact two-column or full-width stacked), chosen per book; a bordered finished-dish photo with every recipe; full-bleed dividers per the divider format; tables with consistent widths, repeating header rows, adequate padding, no split rows, no clipping or overflow.
- **DOCX build:** one fully formatted, editable Word .docx master with native styles, live auto-TOC, real numbering, deliberate section/page breaks, keep-together controls, and embedded print-quality images at every recipe, divider, and opener slot per the Image Production Contract. Plain text, Markdown, or PDF-only output fails.

## Image Production Contract

Every image is a numbered slot in `image_manifest.md` so the `uapf-flow-image-pipeline` generates and inserts each one. Images are never left as prose or placeholders; Rule 11 (images at any page count) applies.

### Slots (countable, gate-checkable)
- `IMG-00` - hero opener: overhead flat-lay of the book's signature ingredients, full-bleed.
- `IMG-D-<CATEGORY>` - one full-bleed divider photo per recipe chapter (e.g. `IMG-D-BREAKFAST`).
- `IMG-R01 ... IMG-Rnn` - one finished-dish photo per recipe, numbered to match the recipe number.

Each slot records `**Save as:**` (filename), `**Flow prompt:**` (text), and `**Caption/alt:**` (a short description for accessibility). Image count = 1 hero + (number of categories) dividers + (number of recipes) recipe photos. A missing, unnumbered, or unmatched slot is a Gate-3 failure.

### Food-photography style bible (lock once per book; apply to EVERY food image)
Fix these before generating image one, record them in the State Block, and repeat them verbatim inside every food prompt so the whole book looks like a single shoot:
- **Surface and props** (e.g. warm neutral stoneware on a stone or linen surface, sprigs of the theme's herbs, matte cutlery).
- **Lighting and angle** (e.g. soft natural daylight with gentle shadow; overhead or 45 degrees, chosen once).
- **Palette** echoing the book's two accent colors.
- **Realism**: appetizing, shallow depth of field, no text, no hands, no brand packaging.
- **Content restriction**: no pork, no alcohol, no wine glasses or beer, ever (silent, never labeled).
Divider photos use the same style at full-bleed (signature dish plus a few raw ingredients); the title band carries the text, so generated art stays wordless.

### Prompt template (per food slot)
"Professional [overhead|45-degree] food photography of [finished dish], [key visible components], on [locked surface and props], [locked lighting], appetizing, shallow depth of field, colors echoing [accent palette], no text, no hands, no packaging."

## Content Rules

- **THE FATAL FLAW to avoid: split recipes.** A recipe that breaks across columns or pages, or a procedure list that continues numbering from a previous recipe, destroys the product. Every recipe is one column, one page, steps 1–N self-contained.
- **Silent content exclusion:** **NO PORK and NO ALCOHOL** in any recipe, ingredient, substitution note, educational passage, meal plan, shopping list, or image concept. This includes hidden carriers: cooking wine, mirin, beer batter, wine vinegar, standard vanilla extract, liqueur flavorings, lard pastry, gelatin of unspecified origin, marshmallows/gummies, stock cubes, Worcestershire sauce, some soy sauces, commercial glazes, wine-brined olives, alcohol-based extracts. Substitute automatically: alcohol-free vanilla, apple cider or distilled vinegar, agar-agar, beef bacon or smoked turkey, broth + acid for deglazing. **The exclusion is never mentioned in reader-facing text** — no dietary or compliance labels, notes, or assurances anywhere the reader sees; the book simply never contains the excluded items.
- **Voice:** active, direct, technique-confident, zero filler. Substitution notes inline only when genuinely useful. Every recipe must execute exactly as written by a home cook.
- **No em dashes** anywhere in book content.
- **Nutrition honesty:** USDA FoodData Central base values; per serving = total ÷ servings; no unverifiable medical claims; educational claims carried by at least two named credible sources.
- **Meal-plan closure:** every meal-plan cell references a recipe that exists in this book, by its exact name.
- **Catalog uniqueness:** no recipe fingerprint collision, no palette collision, and no design-fingerprint collision with any prior Pegasus cookbook. Every cookbook must look visibly distinct from every other, not merely differ in palette.

## QA Checklist

**Gate 1 — Configuration (after Phase 0, before TOC):**
- [ ] Trademark verdict clean; title classified with evidence; locked title recorded verbatim
- [ ] Seed words preserved in any replacement title; alternatives scored if verdict was not STRONG
- [ ] Subtitle ≤ 150 chars combined, keyword early, recipe count stated, no brands/em dashes
- [ ] Author pulled, formatted, screened against Author Log and real persons
- [ ] Recipe count fixed; categories cover breakfast/lunch/dinner/snack, each 6–15 recipes
- [ ] Design fingerprint composed and logged; palette pair unique AND full design fingerprint (archetype + palette + divider + numerals + meta style) unique in catalog; recipe set fingerprinted with zero collisions
- [ ] Page projection within the deployment page budget (studio owner ≤ 100; licensed client = chosen budget) via Governor formula; recipe layout set per policy

**Gate 2 — Structure (after TOC + front matter):**
- [ ] TOC is a live auto-TOC listing every category (H1) and every recipe (H2)
- [ ] Preface exactly one page; How to Use exactly one page; copyright + disclaimer from template
- [ ] Theme opener (IMG-00) embedded as a finished full-page image, not a prompt or placeholder
- [ ] Front matter unnumbered; numbering starts at Introduction

**Gate 3 — Per-Chapter (after every recipe chapter):**
- [ ] Divider page (IMG-D-<category>) is full-bleed food photography with the centered title band (category title + italic subtitle); art wordless, no white margins
- [ ] Every page holds exactly two recipes in the book's chosen archetype; no recipe splits across a page; archetypes are not mixed within the book
- [ ] Every recipe carries its own finished-dish photo (IMG-Rnn), embedded, bordered, inside trim-safe; all food images share the one locked photography style
- [ ] Each recipe plus its photo fills its allotted space (80–90% in Archetype A); no sparse or overflowing recipes
- [ ] Every method list restarts at 1; no carried-over, skipped, or manually typed step numbers
- [ ] Silent exclusion audit: zero pork/alcohol items or hidden carriers; zero reader-facing mention of the exclusion; no alcohol or pork imagery in any photo
- [ ] Metric conversions present on every quantity; F (C) temperatures; doneness cues; Per Serving ends with theme nutrient
- [ ] Body text is 11 pt Times New Roman; only primary/accent colors used, body text black

**Gate 4 — Release (whole book):**
- [ ] Total pages within the deployment page budget; page-by-page render shows no overflow, blank pages, orphaned headings, broken tables, or displaced images
- [ ] Locked title matches character-for-character across cover handoff, title page, TOC, metadata, State Block
- [ ] Conclusion exactly 1.5 pages with all four movements and the honest-review request
- [ ] Meal plan: every cell resolves to a recipe in the book; tables have repeating headers, no split rows
- [ ] Shopping lists carry exact quantities, department grouping, Replenish sections from week 2
- [ ] Whole-book silent-exclusion re-scan passes; whole-book em-dash scan passes
- [ ] Image contract complete: IMG-00 hero + one IMG-D divider per category + one IMG-Rnn per recipe, all embedded and inside trim-safe; food images consistent in the locked photography style
- [ ] Design, palette, and recipe logs updated; the book is visibly distinct from every prior cookbook in the catalog; delivered as one premium editable DOCX

## KDP Positioning

- **Category tree:** Books > Cookbooks, Food & Wine > the closest matching sub-branch (e.g. Special Diet > Weight Loss; Regional & International > the cuisine; Baking > the format). Choose the deepest accurate node plus one adjacent node for the second category.
- **Description leads with:** the recipe count and the specific reader outcome ("120 quick anti-inflammatory dinners that..."), followed by what's inside (categories, meal plan, shopping lists, USA/UK charts), then the audience fit line. Never leads with the author or generic praise. No medical promises, no mention of exclusions.
- **Metadata signals:** recipe count in subtitle; seed words in the first backend keyword slots; audience qualifier (beginners, seniors, busy families) and format qualifiers (quick, one-pot, 30-minute) in remaining slots; large-trim full-color print settings declared; no brand terms anywhere in metadata.

## Key Rules — Do NOT Break

1. **Two recipes per page in the book's chosen archetype (compact two-column or full-width stacked): one complete recipe per unit, never split across a page, and archetypes never mixed within a book.**
2. **No pork, no alcohol, anywhere — and the exclusion is silent: never mentioned in any reader-facing text.**
3. **Each recipe plus its photo fills its allotted space (80–90% in Archetype A)** — rewrite to fit; never resize type or spill.
4. **A finished-dish photo accompanies every recipe.** All food images share one locked photography style, and every image is a numbered manifest slot (IMG-00 hero, IMG-D-<category> dividers, IMG-Rnn recipes), never a prompt or placeholder.
5. **Every recipe's procedure restarts numbering at 1** as a fresh native numbered list; numbering never continues across recipes.
6. **Body text is 11 pt Times New Roman**, not the 12 pt UAPF default.
7. **Exactly two colors (primary + accent) per book, and no two catalog cookbooks share the same palette OR the same overall design fingerprint** (archetype + palette + divider band + step numerals + meta style). Every cookbook looks visibly distinct. Body text stays black.
8. **Full-color professional interior** at 8.625 x 11.25 in; total length honors the deployment page policy (studio owner hard-capped at 100; licensed client sets the budget, default 100).
9. **Divider pages are full-bleed food photography with a centered title band** (category title in white serif caps plus one italic subtitle line); the art is wordless and embedded as a finished image, never a prompt or placeholder.
10. **The locked title is immutable** character-for-character once selected; seed words are preserved in any replacement title.
11. **Deliver one premium editable DOCX** with native styles, live auto-TOC, and page-by-page render QA — never plain text, Markdown, or PDF-only.
12. **No em dashes in book content; no third-party brands in title, subtitle, or metadata; no catalog recipe duplicates.**

## HOUSE REFERENCE BANK (2026-08-14)

Eight catalog masters are banked at `cover_db/_interiors/cookbook/` (local
only, never shipped): the 15-Minute High-Protein (DE), Air Fryer for Seniors
(DE), Mason Jar Salad, Kidney Stage 4 African-Canadians, two Mediterranean
African-Canadians editions, Mason Jar Salads (FR), and Cottage Cheese
masters. CONSULT THEM before designing any new cookbook: open 2 or 3 and
study a recipe page, a divider, and a front-matter page. On installs where
the bank folder is absent (client installs never receive it), the codified
standards below carry the full weight of the reference study; follow them
as written. Standards verified across the bank:

* Two proven RECIPE CARD ARCHETYPES; pick ONE per book at intake:
  (A) TWO-PER-PAGE compact card (Mason Jar style): numbered ALL-CAPS title
  with colored rule, one italic description line, inline meta line, photo in
  the left column with STORAGE and ALLERGENS beneath, tinted INGREDIENTS
  panel + tinted METHOD panel side by side, swap line, compact nutrition
  table. Both cards fully contained in their half-page slots.
  (B) ONE-PER-PAGE hero card (Cottage Cheese style): numbered ALL-CAPS title
  in accent color, italic description, large hero photo, 5-column shaded
  meta table (PREP | COOK | TOTAL | SERVES | DIFFICULTY) with colored header
  band, two-column INGREDIENTS/METHOD with colored caps headers, storage +
  swap strip, single-line PER SERVING nutrition bar. Under the density law
  the card must fill the page; expand method detail or panels, never leave
  the bottom half empty (older masters predate this law; do not copy their
  white space).
* DIVIDERS: full-bleed food photography montage with one solid color band or
  block panel carrying the category title in white serif BLOCK CAPS plus at
  most one italic tagline. TITLE ONLY, never a chapter number (the Kidney
  master's "CHAPTER 6" label is the retired pattern).
* Running header on recipe pages (small caps book title, centered or split
  with the folio) and numbered recipes across the whole catalog style.
* Every master uses a DIFFERENT two-color palette (teal+coral, maroon+
  textile warmth, terracotta, teal+cream). The bank proves the fingerprint
  law: match the QUALITY BAR and anatomy, never an existing book's palette
  or exact geometry.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
