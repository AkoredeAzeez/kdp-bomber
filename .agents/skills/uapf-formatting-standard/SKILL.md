---
name: uapf-formatting-standard
description: The consolidated master formatting standard for all Pegasus Press niches (operator directive 2026-08-13). Universal manuscript and typography rules, per-niche interior specifications, cover/wrap/A+ production rules, and the final preflight checklist. Applies to every book from both engines (Claude and Codex) unless a project's locked framework, approved TOC, exact count, audience, or explicit project instruction overrides a specific default.
---

# UAPF Consolidated Master Formatting Standard​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Operator directive 2026-08-13. These rules apply to every UAPF book unless a
project's approved framework specifies otherwise. PRECEDENCE: a project's
locked framework, approved Table of Contents, exact counts, audience, and
explicit project instructions always take priority over the general defaults
below. A saved per-niche client style profile (uapf-custom-formatting,
`state/custom_formatting/<niche>.json`) also outranks the general aesthetic
defaults below, but never the binding laws (premium bar, containment, type
floors, pagination/TOC, global hard rules). Standing operator directives (block-letter cover titles, premium
colorful interior, no em dashes, publisher/ISBN exclusions, content
restrictions) remain in force and are restated here where they apply.
Section numbering follows the operator's master document; sections 15 and 16
were absent from the source document and were drafted by Genie (approved by
the operator 2026-08-13). Niches without a dedicated section (fiction,
poetry, language, humor, popular-science, public-domain, reference) follow
section 1, their niche skill, and the nearest section by analogy.

## 1. Universal formatting instructions

Manuscript production:

* Use American English unless the title or marketplace requires another language.
* Preserve the approved Table of Contents exactly.
* Do not rename, remove, merge, reorder, or invent chapters.
* Continue from the precise stopping point without repeating completed material.
* Maintain one rolling manuscript containing all completed work.
* Place front matter before the main chapters.
* Deliver a fully editable DOCX and an inspected, print-ready PDF when requested.
* Embed all fonts and images.
* Use proper page breaks and section breaks; do not create spacing with repeated blank lines.
* Keep headings, tables, images, page numbers, headers, and footers consistent throughout.
* Avoid widows, orphans, clipped text, blank pages, font substitutions, and accidental pagination drift.
* Run final checks for margins, duplicated content, missing sections, incorrect numbering, image resolution, and answer-key accuracy.

Pagination and final Table of Contents law (operator directive 2026-08-14,
BOTH engines, Claude and Codex, every book):

* Page numbering starts at the Introduction: the Introduction's first page is
  page 1. Front matter before the Introduction (title page, copyright page,
  Table of Contents) carries no visible folio numbers.
* After the whole book is finished (all chapters merged, images inserted, back
  matter placed), REWORK the Table of Contents against the final rendered
  layout: every TOC entry must show the page number where that chapter or
  section actually begins in the final PDF. A TOC built or left from an
  earlier draft state is a release failure.
* Verify the reworked TOC on the RENDERED page: open the final PDF and check
  each entry's page number against the actual page; any mismatch is corrected
  and the check rerun before delivery. Update the DOCX TOC field so the
  editable file and the PDF agree.

Default typography:

* Body font: Times New Roman, 12 pt.
* Senior-facing books: generally 13 to 14 pt.
* Body alignment: justified, except children's books and layouts where left alignment improves readability.
* Line spacing: 1.15 or 1.5, depending on the niche and audience.
* Chapter headings: approximately 16 to 18 pt, bold, frequently in block capitals.
* Numbered subheadings: left aligned and hierarchically consistent.
* Use long, explanatory paragraphs where appropriate.
* Apply Word heading styles so the Table of Contents remains editable and clickable.

8.5 x 11 interior heading law (operator directive 2026-08-14; for every
8.5 x 11 trim book this overrides the default heading sizes above and any
smaller per-niche heading size):

* Chapter titles: BLOCK CAPITALS, bold, 28 pt or larger. Wrap and size the
  full title so it sits entirely inside the page margins; a chapter title
  touching or crossing a margin is a render-QA failure.
* Subchapter headings: 14 to 18 pt, and likewise never cut off by the margins.
* Introduction: approximately a page and a half, written to FILL its pages,
  substantive explanations occupying the full live text area, never a
  half-filled page of thin summary. (Prose-led 6 x 9 books keep the general
  2 to 3 page introduction target.)
* Both rules are verified on the RENDERED page as part of render-containment
  QA before any chapter preview or delivery.

Premium, professional, high-grade bar (operator directive 2026-08-13,
every niche, every book):

* Every interior must read as a top publisher's production, not a home-made
  document: consistent professional typography, precise alignment, even
  spacing rhythm, and the full premium colorful interior system (styled
  chapter openers, colored typographic hierarchy, tinted callout panels,
  styled tables, section header bars, white-space discipline) executed in
  the book's unique design fingerprint.
* Amateur tells are production failures: default-looking plain pages,
  inconsistent heading or caption styles, uneven spacing, misaligned tables
  or images, cramped margins, orphan headings, stray fragments, rivers of
  white space in justified text, decoration that crowds content, and any
  visual inconsistency between chapters.
* The bar is verified on the RENDERED page, never assumed from the source
  file: render-containment QA (render_qa.py) plus a page-by-page visual
  inspection of the PDF must pass before any preview or delivery. A book
  that fails is fixed and re-rendered, never shipped.
* This bar applies with equal force to every niche, from textbooks to
  journals; a niche's simpler layout is executed to the same standard of
  polish, and the niche's own section below plus its uapf-niche skill add
  requirements but never subtract from this bar.

General exclusions:

* Do not include "Pegasus Press."
* Do not insert an ISBN unless specifically instructed.
* Do not state that an author name was generated.
* Do not add references, chapter summaries, key terms, diagrams, or other supplementary sections when the approved structure excludes them.
* Do not change locked manuscript text or formatting while inserting images, except for natural pagination changes.

## 2. Academic, medical and professional textbooks

Examples: medical textbooks, engineering books, academic references, professional handbooks.

Interior specifications:

* Trim size: 8.5 x 11 inches.
* Target length: generally 400 to 550 pages.
* Each substantive chapter: normally at least 23 pages.
* Margins: approximately 0.7 inch, adjusted for binding where necessary.
* Body font: Times New Roman, 12 pt.
* Alignment: justified.
* Line spacing: usually 1.15 or 1.5.
* Chapter headings: 18 pt, bold, BLOCK CAPITALS.
* Numbered sections: left aligned.
* Learning objectives: numbered and placed at the beginning of each chapter when required.
* Use tables only when they materially improve comprehension.
* No diagrams or charts where the active academic/medical framework excludes them.
* Front-matter pages should not display folio numbers.
* Use continuous chapter and section numbering.
* References must use the required academic style and contain genuine, verifiable sources.
* Do not add chapter summaries, key terms, or references when the particular project has explicitly excluded them.

Production requirements:

* Linked Table of Contents using Heading 1 and Heading 2 styles.
* Proper captioning and numbering of approved tables and figures.
* Consistent headers and footers.
* Verify citations, cross-references, terminology, and clinical disclaimers.
* Visually inspect the rendered PDF page by page.

## 3. Study guides and exam-preparation books

Examples: PREACT, Regents examinations, professional certifications, Facharztpruefung books.

Interior specifications:

* Default trim: 8.5 x 11 inches.
* Content-driven page count unless a specific limit is approved.
* Body font: generally Times New Roman, 12 pt.
* Questions may use a clean two-column layout where the framework requires it.
* Answers and explanations must appear in a separate, clearly labeled section.
* Keep question numbering continuous and synchronized with the answer key.
* Exhibits must remain adjacent to the questions that use them.
* Do not split a question awkwardly across pages.
* Use clear hierarchy for: (1) domains or units, (2) chapters, (3) lessons, (4) practice sets, (5) answers and explanations.
* Follow the current official examination blueprint.
* Maintain the promised number of questions.
* Include learning plans, strategy sections, or diagnostic material only when listed in the approved TOC.
* For chapter-only study guides, do not generate practice questions, answer keys, explanations, or assessment sets.

Quality control:

* Verify question uniqueness and numbering.
* Confirm that every question has exactly one corresponding answer.
* Check calculations, dates, regulations, and exam specifications.
* Prevent answer clues from appearing unintentionally in question layouts.
* Keep tables and answer choices together whenever possible.

## 4. Cookbooks

Examples: sourdough, cottage-cheese, freezer-meal, high-protein, senior, cuisine-specific cookbooks.

Interior specifications:

* Typical trim: 8.5 x 11 inches when the book is photo-led or recipe-rich.
* Earlier framework profile: ordinarily no more than approximately 90 pages unless the approved recipe count requires a longer manuscript.
* Body font: generally 11 to 12 pt; 13 to 14 pt for senior cookbooks.
* Use a clear, repeatable recipe template.
* Keep each recipe title visually prominent.
* Use consistent sections such as: yield or servings; preparation time; cooking time; ingredients; instructions; nutrition information (when promised); storage or freezer instructions (when applicable); tips, substitutions, or variations.
* Keep ingredient lists left aligned.
* Number recipe instructions.
* Avoid splitting ingredient lists unnecessarily.
* Keep short recipes on one page or facing pages where practical.
* Recipe count must match the title and subtitle exactly.
* Use US measurements unless the marketplace or approved manuscript requires metric measurements.
* Ensure nutritional claims are qualified and internally consistent.

Images:

* Food photography should be high-resolution and realistically rendered.
* Images must be placed with their corresponding recipes or chapters.
* Use 300 DPI images for print.
* Maintain consistent lighting, color treatment, plating, and image proportions.
* Chapter-opening images may display the chapter title when requested.
* Avoid repetitive or obviously duplicated food images.

Final checks:

* Confirm all promised recipes are present.
* Check ingredient and instruction consistency.
* Verify cooking temperatures, times, yields, and nutritional values.
* Ensure photographs do not obscure text or enter unsafe margins.

## 5. Health, fitness, recovery and wellness books

Examples: hysterectomy recovery, surgery recovery, senior fitness, rehabilitation, mobility, wellness books.

Interior specifications:

* Common trim: 8.5 x 11 inches for activity-led or illustrated books; 6 x 9 inches may be used for prose-led wellness books.
* Senior-facing text: preferably 13 to 14 pt.
* Use generous line spacing and uncluttered pages.
* Keep paragraphs readable and avoid dense medical presentation.
* Use large, descriptive headings.
* Separate education, exercises, trackers, reflections, and activities clearly.
* Writing areas must be large enough for practical use.
* Include medical disclaimers and escalation guidance where appropriate.
* Avoid diagnosis, treatment guarantees, or unsupported health claims.
* Exercises must include safety instructions, modifications, and stopping conditions where necessary.
* Recovery timelines should be presented as general guidance, not guaranteed outcomes.

Recovery activity books:

* Use supportive, calm visual styling.
* Keep one principal activity or closely related activity set per page or spread.
* Ensure writing prompts, mood trackers, checklists, word puzzles, and gentle activities are readable.
* Answer keys must correspond exactly to puzzle numbering.
* Avoid overcrowded pages and visually stressful layouts.

## 6. Children's storybooks, fact books and early readers

Examples: first-day-of-school stories, confidence stories, science books, backyard-creature guides.

Interior specifications:

* Default trim: 8.5 x 11 inches.
* White paper unless another stock is required.
* Body text: approximately 12 to 16 pt, increasing for younger readers.
* Text alignment: left aligned with a ragged right edge.
* Use generous white space, wide margins, and comfortable line spacing.
* Use large, playful headings.
* Employ recurring themed icons and decorative motifs.
* Keep editable text separate from illustrations whenever possible.
* Use original illustrations and distinct motifs for each title.
* Give each title its own visual identity rather than recycling layouts.
* Use themed page numbers where appropriate.

Illustration treatment:

* Preferred styles: warm hand-drawn black and white; soft grayscale; premium color when the project requires it.
* Raster images: 300 DPI. Line art: preferably 600 DPI.
* Use 0.125-inch bleed when artwork extends to the page edge.
* Keep faces, hands, text, and important objects inside safe margins.
* Maintain a character bible so age, clothing, hair, skin tone, scale, and personality remain consistent.
* Use a page-level illustration ledger to prevent missing or duplicated artwork.

Production:

* Front matter first.
* Page or spread blueprint before final illustration placement.
* Back matter and answers after the main content where applicable.
* Deliver one merged editable DOCX and a visually inspected print-ready PDF.

## 7. Children's activity books and workbooks

Examples: "I Am 7/8/9 and Smart," screen-free workbooks, watercolor activities, preschool material, educational activity books.

Interior specifications:

* Default trim: 8.5 x 11 inches.
* Maximum framework profile: approximately 150 pages.
* Use premium color only when it materially supports the activity.
* Use black and white for activities that must be economical or easily printable.
* No bleed for text, grids, tracing, and ordinary write-in pages.
* Use larger writing-safe margins.
* One main activity per page unless the layout clearly supports more.
* Use child-friendly fonts and instructions.
* Keep directions short, specific, and placed immediately above the activity.
* Supply adequate writing, drawing, cutting, or coloring space.
* Maintain the exact promised activity count.
* Vary activity types while maintaining age appropriateness.
* Avoid duplicate prompts, repeated illustrations, and mechanically similar pages.

Exact-count projects: when a project specifies an exact total (such as 100
pages, 92 activities, 120 puzzles, or 150 activities), the completed
manuscript must match that number exactly.

Answers:

* Include answers only for activities that have objective solutions.
* Synchronize answer numbers and page references.
* Check every puzzle manually or computationally before publication.
* Ensure answer pages remain readable in grayscale.

## 8. Adult activity, puzzle, crossword and logic books

Examples: crossword books, word-search books, detective challenges, Krimi-Sudoku, mystery puzzles, suspect-elimination books.

Interior specifications:

* Default trim: 8.5 x 11 inches.
* Usually black and white.
* No bleed for grid- and text-based pages.
* Increase the inside margin according to final page count.
* Use approximately 300 PPI artwork; line art may be higher resolution.
* Embed all fonts.
* Make grids, clues, numbers, and answer spaces comfortably readable.
* Keep clues and their corresponding grids together.
* Avoid placing essential puzzle elements in the gutter.
* Use consistent puzzle numbering and difficulty labels.
* Ensure every puzzle has a correct, unique, and reproducible solution.
* Keep answers in a separate answer section unless the approved TOC says otherwise.
* Synchronize puzzle number, page number, and answer-key number.

Mystery and detective books:

* Preserve the approved number of cases, suspects, clues, and solutions.
* Track evidence consistently across narrative pages, worksheets, and solutions.
* Avoid accidental spoilers in headings, running headers, illustrations, or page previews.
* Distinguish case narrative, evidence, suspect records, deduction pages, and solution pages visually.
* German-language projects must use correct German typography, punctuation, quotation marks, capitalization, and compound words.

Final checks:

* Check duplicates and missing puzzles.
* Validate all solutions.
* Inspect small numbers and thin grid lines in the print PDF.
* Test grayscale readability.
* Run the manuscript through the KDP Previewer and inspect a printed proof where possible.

## 9. Workbooks for adults, education and professional development

Interior specifications:

* Common trim: 8.5 x 11 inches.
* Framework ceiling: approximately 150 pages unless overridden.
* Worksheet-dense structure with sufficient response areas.
* Keep instruction and response fields on the same page whenever practical.
* Use checkboxes, rating scales, tables, prompts, and trackers consistently.
* Avoid response lines extending into the gutter or trim area.
* Do not place decorative images where users need to write.
* Provide worked examples before complex exercises.
* Include answer support only where appropriate.
* Maintain accessibility through high contrast, readable type, and uncluttered design.

## 10. Craft, crochet, hobby and how-to books

Examples: crochet blankets, amigurumi, watercolor, gardening, home improvement, practical project books.

Interior specifications:

* Default trim: 8.5 x 11 inches.
* Maximum profile: approximately 150 pages.
* Organize content into tools, materials, techniques, projects, troubleshooting, and reference material.
* Each project uses a repeatable structure: skill level; finished dimensions; materials; tools; gauge or measurements; abbreviations; step-by-step instructions; assembly or finishing; troubleshooting; care instructions.
* Number all steps clearly.
* Place images or diagrams beside the relevant instructions.
* Do not separate a step from the image required to understand it.
* Use high-resolution close-ups for hands, stitches, joins, tools, and finished details.
* Use consistent measurement units and terminology.
* For crochet patterns, verify stitch counts, row counts, repeats, gauge, and finished measurements.
* Clearly identify whether US or UK crochet terminology is being used.

## 11. Repair manuals, mechanical handbooks and user guides

Examples: vehicle repair manuals, device guides.

Interior specifications:

* Common trim: 8.5 x 11 inches.
* Use a technical, highly structured layout.
* Organize procedures into: purpose; tools and parts; safety precautions; preparation; removal; inspection; installation; testing; troubleshooting.
* Use numbered procedural steps.
* Put warnings and cautions before the hazardous step.
* Use tables for specifications, fluids, torque settings, symptoms, and diagnostic results.
* Keep photographs or diagrams adjacent to their referenced steps.
* Provide figure numbers and captions consistently.
* Avoid splitting warnings, tables, and step sequences across pages.
* Verify model years, component variants, specifications, and units.
* Use high-resolution, technically accurate images rather than decorative artwork.

## 12. Self-help and personal development books

Interior specifications:

* Typical trim: 6 x 9 inches.
* Framework profile: normally no more than approximately 180 pages.
* Body font: Times New Roman, 11 to 12 pt.
* Alignment (operator directive 2026-08-14, BOTH engines): body paragraphs
  JUSTIFIED; bullet points and numbered lists LEFT-ALIGNED (ragged right),
  never justified.
* Line spacing (operator directive 2026-08-14): 1.5 throughout the body.
* Premium formatting to world trade-publishing standards: even spacing
  rhythm, no rivers in the justified text, hanging indents on lists, the
  full premium color system in the book's fingerprint, and render-QA
  verification on the page. Plain or uneven typesetting is a production
  failure.
* Use readable paragraph spacing and restrained decoration.
* Organize chapters around explanation, reflection, practice, and action.
* Use exercises and journaling prompts only where they support the chapter.
* Keep writing spaces large enough to use.
* Avoid clinical claims unless properly sourced and qualified.
* Maintain a supportive, practical, and nonjudgmental tone.

## 13. History, politics and biography

Interior specifications:

* Typical trim: 6 x 9 inches for general readership; 8.5 x 11 inches for textbook-style projects.
* Times New Roman, 12 pt, justified.
* Use a formal heading hierarchy.
* Chronologies, maps, tables, and source notes must be consistent.
* Distinguish fact, interpretation, quotation, and author analysis.
* Use real, verifiable sources.
* Apply one citation system consistently.
* Include captions and credits for archival material.
* Maintain accurate dates, names, locations, titles, and political terminology.
* Avoid unsupported claims or invented quotations.

## 14. Travel guides

Interior specifications:

* Typical trim: 8.5 x 11 inches.
* Framework profile: photo-led and ordinarily no more than approximately 100 pages unless a larger format is approved.
* Use short, navigable sections.
* Include clear hierarchy for destinations, neighborhoods, itineraries, transport, dining, accommodation, accessibility, and practical information.
* Maps must be original or properly licensed, legible, and geographically accurate.
* Use consistent icons and color coding.
* Place maps and photographs beside the relevant destination content.
* Provide captions and attribution where required.
* Verify operating information, transport routes, prices, entry requirements, and accessibility details close to publication.
* For image-only travel PDFs, compose pages at high resolution and inspect every rendered page before merging.

## 15. Journals, planners and guided notebooks

Examples: guided journals, gratitude journals, prayer journals, wellness and
habit trackers, planners, log books, keepsake and memory journals.

Interior specifications:

* Default trim: 6 x 9 inches; 8.5 x 11 inches only when a large-format
  planner or worksheet-style journal is explicitly approved.
* Undated unless a dated year is explicitly approved.
* Build the interior from a small set of repeating page templates (entry
  page, tracker, weekly review, milestone page) and keep every repetition
  pixel-consistent; template repetition is intentional, accidental
  duplication of prompt content is a defect.
* Prompts must be original, varied, and matched to the journal's promise;
  never recycle one title's prompt set into another.
* Writing areas are the product: ruled lines at a comfortable writing pitch
  (roughly 0.3 inch), fields large enough for real handwriting, and no
  response line ever entering the gutter or trim area.
* No bleed on write-in pages; decorative pages may bleed when approved.
* Keep ink coverage light so pages accept pen and pencil; test grayscale.
* Number days, weeks, or entries continuously and match the TOC exactly.
* Maintain the exact promised entry, prompt, or page count.
* Senior-facing journals: 13 to 14 pt prompts and generous spacing.
* Decorative motifs follow the book's unique design fingerprint; never place
  decoration where the reader needs to write.

Final checks:

* Verify template consistency page by page in the rendered PDF.
* Confirm entry numbering, tracker ranges, and any date math.
* Confirm writing-space usability at print size and grayscale readability.

## 16. Faith and devotional books

Examples: daily devotionals, prayer books, scripture study companions,
reflection and gratitude devotionals, faith-based encouragement titles.

Interior specifications:

* Typical trim: 6 x 9 inches.
* Daily structures (90-day, 365-day) numbered continuously; every day
  present, none duplicated, and the count must match the title's promise
  exactly.
* Use a consistent daily unit template, for example: day number and title;
  opening quotation or scripture; reflection body; prayer or meditation
  panel; application or journaling prompt.
* Scripture and sacred-text quotations must be reproduced exactly from the
  stated translation, with the translation named in the front matter and
  chosen so its licensing permits commercial reproduction (public-domain
  translations unless a license is held); never paraphrase a quotation while
  presenting it as the text.
* Attribute every quotation precisely (book, chapter, verse or equivalent).
* Keep the reverent, encouraging register consistent; no denominational or
  doctrinal claims beyond the approved scope of the book.
* Reflection and prayer panels use the book's tinted-panel styling and stay
  visually distinct from body text.
* Senior-facing devotionals: 13 to 14 pt body and generous line spacing.
* Writing prompts, when included, follow the journal rules in section 15.
* Reading plans, indexes of themes, or scripture indexes appear only when
  listed in the approved TOC.

Final checks:

* Verify every quotation against the stated translation, letter for letter.
* Confirm day numbering, plan references, and index accuracy.
* Confirm the daily-unit template renders identically across the book.

## 17. KDP front covers

Standard front-cover rules:

* Common size: 8.5 x 11 inches or a 2:3 portrait ratio, depending on the project.
* Print resolution: 300 DPI.
* Full bleed with no mockup frame, border, or presentation background.
* Maintain strong title-subtitle-author hierarchy.
* Title must remain legible at Amazon thumbnail size.
* Titles render in BLOCK CAPITALS (standing operator directive 2026-08-13, non-negotiable; a trademark's own letterform stays intact inside the block setting).
* Keep subtitle wording exactly as approved.
* Capitalize each major subtitle word when instructed.
* Include the correct author name.
* Keep text within safe margins.
* Use original, high-definition imagery.
* Do not reproduce a reference cover so closely that the result appears copied.
* Use reference covers for market cues, hierarchy, and positioning while creating a distinct design.
* Avoid using the same colors and compositions repeatedly across projects.
* Front title-page design may be made to match the final cover when requested.

## 18. Paperback wraps: back cover, spine and PDF

Production sequence:

1. Approve or finalize the front cover.
2. Determine trim size, page count, paper type, bleed, and binding.
3. Calculate the spine width.
4. Generate a matching back cover and spine.
5. Assemble the full wrap using the correct KDP template.
6. Export as a print-ready PDF.
7. Inspect all safe areas, bleed, spine centering, and trim boundaries.

Specific instructions:

* Do not estimate the spine before the final interior page count and paper type are known.
* The spine title and author name must be centered and readable where spine width permits.
* Keep all essential text outside the fold and trim zones.
* Remove the barcode placeholder when instructed and leave the area empty.
* Do not insert an ISBN.
* Match the front, spine, and back in color, texture, typography, and visual tone.
* Back-cover copy must remain concise and readable.
* The final paperback cover must be delivered in PDF format.

## 19. Amazon A+ Content

Standard package:

* Usually five separate modules.
* Preferred module size: 970 x 600 pixels.
* Some projects may use 1600 x 1000 pixels when specifically requested.
* RGB PNG format, approximately 300 DPI.
* Keep each image under 2 MB where required.
* Use authentic interior-page renders when showcasing book content.
* Maintain the cover's visual identity across all modules.
* Do not repeat the same composition five times.
* Recommended functional sequence: (1) book promise or hero module, (2) key benefits, (3) interior preview, (4) audience or usage experience, (5) closing value proposition.
* Keep text brief and readable on mobile.
* Avoid prices, star ratings, testimonials presented as customer reviews, unsupported superlatives, competitor comparisons, URLs, contact details, and prohibited promotional claims.
* Supply alt text and recommended upload order when requested.
* Deliver the five modules separately and as a ZIP when requested.

## 20. Final preflight checklist for every niche

Before a project is considered complete, verify:

* Correct title, subtitle, and author name.
* Approved TOC preserved exactly.
* Correct trim size, orientation, bleed, margins, and gutter.
* Correct font family, size, spacing, and alignment.
* Consistent headings, chapter openings, headers, footers, and folios.
* Front-matter folios handled correctly.
* Exact promised chapter, activity, puzzle, question, case, or recipe count.
* No missing, duplicated, renamed, or reordered content.
* All images embedded, sharp, correctly positioned, and at print resolution.
* Tables and write-in areas fit inside safe margins.
* Correct answer keys and page references.
* No clipped text, widows, orphans, blank pages, or font substitutions.
* Cover dimensions calculated from the final interior.
* Paperback wrap exported as print-ready PDF.
* Editable DOCX preserved where required.
* KDP Previewer and rendered-page inspection completed.
* A+ modules supplied separately in the requested dimensions.
* All deliverables use the final approved manuscript, not an earlier version.

## Large Print editions (operator directive 2026-08-16, all niches)

"Large Print" is its own search vertical on Amazon with weak competition,
and Genie's senior-type system already does most of the work. On "Genie,
make a large print edition of [Title]":

1. TYPE: body text 16 pt minimum (industry large-print floor; 18 pt for
   children's or low-vision focus), line spacing at least 1.4, in a
   high-legibility face. Headings, panels, tables, captions, and folios
   scale proportionally so the hierarchy is preserved. This SUPERSEDES
   the 12 pt default and the 13-14 pt senior floor for this edition.
2. LAYOUT: repaginate fully; content is never squeezed or cut to hold a
   page count. Density laws that conflict with 16 pt type (for example
   two recipes per page) relax to the nearest readable unit (one recipe
   per page) for this edition only. Render-containment QA runs at the
   large-print size.
3. EDITION IDENTITY: the phrase "Large Print" appears in the subtitle or
   edition line ONLY when the interior truly meets this spec (16 pt+).
   It is a separate KDP listing/edition with its own cover variant: same
   art, plus a clear "LARGE PRINT" band or badge rendered in the book's
   palette. Metadata (uapf-kdp-niche-specialist) targets large-print
   keywords honestly.
4. The original edition is never modified by making a large print one;
   both live side by side in the catalog and the pen-name registry
   records the pairing.

Ships in every pack (it is writing and formatting work); publishing the
edition remains gated as always.

## Unit-page density and anti-boilerplate law (operator directive 2026-08-17, BOTH engines)

Born from a failed needlepoint build (150 half-empty template-stamped pages).
Applies to every book built from repeating units (projects, recipes, puzzles,
exercises, entries):

1. PAGE DENSITY FLOOR: a unit page must FILL its live text area. If a unit's
   content ends above roughly 75% of the live page height, the layout is wrong:
   either enrich the unit (design notes, variations, tips specific to THAT
   unit) or repaginate to more units per page. A book of half-empty unit pages
   FAILS render QA regardless of margins.
2. NO TEMPLATE STAMPING: instructional steps, materials, and check lines must
   be written FOR THE SPECIFIC UNIT and reference its actual design, name,
   shapes, and colors. Identical step text repeated across units is a
   production failure; the editorial pass (duplicate-sentence and catalog
   checks) gates it mechanically.
3. DIAGRAM TRUTH: an instructional diagram must depict the design its unit
   names. A "banner" project shows a banner; an "initial" project shows a
   letterform. Diagrams are generated per design from that design's own
   geometry, never one template recolored. Any diagram-bearing book verifies
   in render QA that named design and drawn design correspond, unit by unit.
4. REAL-WORLD MATERIALS ONLY: materials lists use real, checkable
   specifications a reader can buy (color names, sizes, counts, tool names).
   Software-only identifiers such as hex color codes NEVER appear as
   purchasable materials. Unverifiable brand claims are also barred; generic
   truthful specs win.
5. Existing laws stack on top: 28 pt+ block chapter titles at 8.5x11, shaded
   unit header bars, no body run below the niche floor (meta lines included),
   count promises delivered exactly.

## UNIVERSAL ARCHETYPE LIBRARY (operator directive 2026-08-19, all niches, both engines)

Layout sameness across catalog books is a production failure in EVERY niche,
not only cookbooks. At design-fingerprint time, every book locks (a) ONE
chapter-opener archetype and (b) ONE structural-unit archetype for its niche's
repeating unit, records both in the Design Log, and no two catalog books in
the same niche may repeat the same opener + unit + palette-family combination.
Where a niche skill carries its own richer menu (cookbook A-L + nine openers;
crafts house architecture), the niche menu takes precedence; this library
covers every other niche. All archetypes obey the binding laws: premium
interior, containment, type floors, senior sizing, grayscale legibility,
image realism, and the niche's own gates.

### Opener / divider archetypes (any niche with chapter or section openers)
1. Photo/art-below: title band top, imagery beneath, intro under it.
2. Photo/art-above: full-width imagery, title on clean space BELOW, rule between.
3. Side-band: imagery in the left or right third; title in the clear column.
4. Full-bleed + text plate: edge-to-edge imagery, title on a solid plate.
5. Illustrated art: watercolor/gouache/ink/flat-vector subject art, title clear of it.
6. Motif frame: decorative subject-motif border, title centered in the clear field.
7. Collage grid: 3-4 thumbnails, title in its own band.
8. Minimalist spot art: small icon/illustration + large title + white space.
9. Text-on-image with contrast scrim: OCCASIONAL only, never a catalog default,
   legibility verified on the rendered page and in grayscale.
Title arrangement (band / plate / column / clean field) is a fingerprint axis.

### Structural-unit archetype menus by unit family
- **Project units** (crafts, howto, hobby): (P1) materials sidebar + steps
  dominant; (P2) full-width stacked with hero photo top; (P3) boxed card with
  header bar; (P4) magazine band (title+meta+photo band, content beneath);
  (P5) ledger typographic (hairline rules, no panels); (P6) two-tone split
  panel (specs reversed on color, steps on white).
- **Worksheet / exercise units** (workbook, study-guide): (W1) instruction
  band + open response field; (W2) two-column drill grid; (W3) boxed exercise
  cards; (W4) numbered ladder (progressive difficulty rail); (W5) journal
  frame (prompt top, lined/blank space dominant); (W6) checklist matrix.
  Usable response space always survives the archetype (niche law).
- **Q&A / exam units** (exam-simulator, study-guide): (Q1) classic stem +
  lettered options, answers sectioned at back; (Q2) two-column rapid-fire;
  (Q3) scenario card + question cluster; (Q4) table drill (stem | options |
  workspace); (Q5) flash-block (boxed single-question emphasis). Answer-section
  placement and option-rotation laws still bind.
- **Entry units** (reference, travel, facts, dictionary-style): (E1) header
  bar + fact table; (E2) side-tab entry with margin index; (E3) card grid
  (2-4 entries per page); (E4) narrative entry with stat sidebar; (E5) ledger
  list with hairline rules.
- **Prompt pages** (journal, low-content): (J1) top prompt + lined body; (J2)
  centered prompt + open space; (J3) framed page with corner motifs; (J4)
  split day/reflection panels; (J5) minimal footer-prompt with full open page.
- **Children's spreads** (childrens, childrens-facts): (K1) full-bleed art +
  text panel inside the safe zone; (K2) art page facing text page; (K3)
  vignette art islands with wrapped text; (K4) top art / bottom text bands;
  (K5) framed storybook page with border motif; (K6) fact-burst spread (large
  art + call-out fact bubbles). Text-safe zones always verified.
- **Prose chapters** (selfhelp, business, health-prose, history, biography,
  parenting, faith, popular-science, fiction): the unit is the chapter
  itself; variation locks a TYPOGRAPHIC SYSTEM instead: (T1) drop-cap opening
  + ornament section breaks; (T2) bold lead-in line + rule breaks; (T3)
  margin-note system; (T4) numbered-section system with colored numerals;
  (T5) pull-quote system (styled excerpts as visual anchors). Panel styles
  (tinted, bordered, icon-led) rotate as a second axis. Fiction uses T-menu
  plus scene-break glyph variation; its interior stays restrained per genre
  convention.

### Enforcement (MECHANICAL, via the fingerprint registry)
The locked archetypes are recorded in the Design Log and book_lock notes at
fingerprint time, and checked BY MACHINE against the whole catalog: before
drafting begins, run
`python .agents/skills/uapf-quality-gates/fingerprint_registry.py check
--niche <x> --opener <o> --unit <u> --palette-family "<family>"
--palette "<#hex,...>" [--cover <C#>]`
which exits 2 on any catalog collision (same niche + opener + unit + palette
family; same primary palette hex anywhere; same niche + cover composition +
palette family). On collision, vary the palette first, then the archetypes,
until the check exits 0. When the fingerprint locks, `register` the book (it
refuses collisions too). The registry lives at state/fingerprint_registry.json
(per-install, survives updates). Render QA verifies the finished book matches
its locked archetypes. The thumbnail-confusion test applies: two same-niche
catalog books viewed as thumbnails must never be mistaken for each other.

## PROSE-7 FORMATTING LAW (operator directive 2026-08-28, strictly prioritised)

Applies to selfhelp, faith, parenting, poetry, business, biography, history,
and outranks older defaults in this skill where they conflict.

- Trim 6 x 9; margins 0.7 in on ALL four sides; line spacing 1.5.
- Body 11-12 pt (13-14 pt for senior audiences), niche-standard serif.
- BLOCK paragraphs (no first-line indent, space between); body JUSTIFIED;
  bulleted/numbered lists LEFT-aligned; word spacing normal (hyphenate rather
  than stretch; never pad with spaces).
- ONE title page only, no half title. BLOCK-LETTER title: top line 22-24 pt,
  remaining lines 18-22 pt.
- Subtitle written to use Amazon's 200-character subtitle limit as fully as a
  natural, guideline-compliant subtitle allows.
- Copyright + Disclaimer SHARE ONE PAGE, ~10 justified lines each; no ISBN or
  publisher line ever.
- Chapter titles: max 4 words, never containing em dashes or hyphens.
- Page numbers begin at the Introduction; final TOC must match rendered pages.
- Land within 5% of the requested page/word count by CONTENT; no blank pages;
  nothing ever continues after the appendix.
- Tables span margin to margin, stopping exactly where body text stops.
- Figure prompts request LANDSCAPE images.
- ARCHETYPE LAW (all niches): every niche maintains a menu of AT LEAST 15
  archetypes that differ in STRUCTURE (opener, section-head style, panel
  style, header, ornament) as well as palette. No two catalog books share an
  archetype + palette combination. Structure must differ between books, not
  colors alone.

## PARAGRAPH LAW (operator directive 2026-08-30, every niche, both engines)

1. BLOCK PARAGRAPHS ONLY. No tab characters and no first-line indents
   anywhere in any manuscript, in any niche. Paragraphs separate with
   spacing, never indentation. `format_qa.py` (check F8) fails any
   indented paragraph mechanically.
2. FULL PARAGRAPHS, WORLD-STANDARD DEPTH. In prose and textbook chapters a
   body paragraph develops one thought to about TEN rendered lines before
   it breaks (roughly 120 to 150 words), especially in textbooks. Choppy
   2-3 sentence paragraph runs read as generated filler and are a
   production failure: run `format_qa.py <chapter.docx> --min-para-lines 10`
   on prose and textbook chapters (check F9 fails a chapter whose body
   paragraphs are more than 40 percent short). Legitimate short paragraphs:
   transitions, list lead-ins, captions, and dialogue where the niche has
   it; these are exempt automatically.
3. THE BAR IS WORLD-STANDARD TRADE FORMATTING. The rendered page must be
   indistinguishable from a top publishing house's typeset interior: the
   premium interior law executes the color system, this law makes the text
   itself read like edited trade prose. Both engines, Codex sessions
   included, are bound; a Codex-drafted chapter passes the same F8/F9
   checks before its preview ships.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
