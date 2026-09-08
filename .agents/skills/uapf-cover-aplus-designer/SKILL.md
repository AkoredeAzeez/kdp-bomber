---
name: uapf-cover-aplus-designer
description: The master cover and A+ design system, built from a 2026-08 study of 1,273 best-selling Amazon covers (independent and traditional publishers) across all 29 UAPF niches. Produces high-quality KDP covers (Cover Law v2, dual-engine) and 970x600 A+ modules (A+ Law v2, Codex single-engine). Use for any cover concept, cover build, or A+ Content design.
---

# Pegasus Cover and A+ Designer​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Design covers and A+ Content that belong on the best-seller shelf of their niche
and outsell it. Grounded in a live Amazon pattern study (2026-08-11 to 13):
1,273 covers banked in `cover_db/` across all 29 UAPF niches, blending
independent (KDP) and traditional publishers per niche. **The AI engine
generates the artwork AND renders every piece of cover and A+ text inside
the design** (covers: Cover Law v2 dual-engine; A+: A+ Law v2, Codex
single-engine). Local scripts never set cover type; they only scale and
finish.

## Codex engine (THE DEFAULT for all cover and A+ production, operator directive 2026-08-13)

Codex is the DEFAULT generation engine for every cover and A+ job, whichever
agent is active. Proven 2026-08-13 on a full front + wrap + 5-module run:
files land directly in the book folder, strings are self-verified letter by
letter with automatic retries, and no browser or API key is needed. The
Codex CLI and the Codex VS Code extension are the same engine (same ChatGPT
sign-in, same native gpt-image-2 tool, same AGENTS.md). When CLAUDE is the
active agent, it drives Codex headlessly with the brief piped via stdin, in
TWO PHASES with different sandboxes (security split, operator-approved
2026-08-13):

- **Phase 1, GENERATION — `codex exec --sandbox workspace-write`.** This
  phase reads the brief and the banked third-party references and generates
  every image into the book folder with the native gpt-image-2 tool (which
  works fine in this sandbox). Because it is the only phase exposed to
  third-party content, it stays mechanically fenced: writes confined to the
  workspace, no arbitrary program execution.
- **Phase 2, FINISH + QA — `codex exec --sandbox danger-full-access`.** This
  phase touches ONLY Genie-generated artifacts from phase 1 (never bank
  images or other third-party content): cover_wrap.py --finish to the print
  PDF, A+ scale-and-crop to exact 970x600 files, and render_qa.py plus the
  letter-by-letter and containment checks. Full access exists solely so the
  local Python gates run inside the session, keeping production fully
  self-contained.

The full-access sandbox is NEVER used for a session that reads third-party
or external content; anything needing live web research stays with Claude.
As soon as a manuscript passes release QC and its metadata DOCX exists, the
cover and A+ package is produced immediately; nothing waits for a browser.
Same brief, same design law, same block-letter / photoreal / text-containment
/ premium-finish / No-Two-Books-Alike rules; only the generator call differs:

1. References: `python .agents/skills/uapf-cover-db/cover_db.py pick --niche
   <niche> --count 3` (no browser needed; the bank is local). Attach the
   picked images to read the shared pattern and text treatment.
2. Write the comprehensive prompt per this skill and the book's palette.
3. Generate with Codex's NATIVE gpt-image-2 image tool (built into Codex's
   ChatGPT account session; no API key, no separate billing): front cover at
   2:3 portrait (1024x1536), A+ masters at 3:2 landscape (1536x1024), saved
   into the book folder as real files. If the native tool is unavailable in
   a given session, generation WAITS or falls to the operator-led ChatGPT
   web project. The scripted openai-package/OPENAI_API_KEY path is RETIRED
   (operator directive 2026-08-15): Codex's built-in image capability is the
   only automated generator; no API key is ever used or required.
4. Verify every string letter by letter at full size and thumbnail; iterate
   (max 4 passes) exactly as in the main workflow.
5. Finish the wrap locally: `cover_wrap.py --finish` with the final page
   count. QA gate below applies unchanged.

Only if NEITHER the native gpt-image-2 tool NOR the scripted alternate is
available does Codex queue the cover as `needs_premium_regen` (same queue as
interior fallbacks) and report it; placeholder-grade covers are never
delivered as final.

## Position in the pipeline

This is the MASTER cover and A+ skill: it owns art direction, concepts, the
design law, and the QA gate, and it supersedes the art-direction role of the
older cover skills. The others remain its sub-steps:

- **uapf-cover-db** supplies banked references (`cover_db.py pick`); when the
  niche bank is thin, **uapf-cover-reference** runs its live research workflow
  and banks what it downloads.
- **uapf-chatgpt-cover-pipeline** is the operator-led ALTERNATIVE engine
  (ChatGPT Image 2.0 in the browser, "Pegasus Covers" project) for
  interactive art-direction sessions; the DEFAULT engine is Codex (section
  above).
- **uapf-cover-canva-build** stays the alternative wrap-assembly path when the
  operator chooses Canva.
- **uapf-kdp-assets** consumes the finished A+ masters for the listing package.

## Inputs (ask for any that are missing, never invent them)
1. Exact title, subtitle, author name, spelled and cased exactly.
2. Niche (from `book_lock.md` when the project exists).
3. Trim size, FINAL page count, paper type (spine math needs all three).
4. Back-cover copy or the manuscript to write it from.
5. 2-3 reference covers: `cover_db.py pick --niche <x> --count 3`, an existing
   `cover_refs/` folder, or operator-supplied images.

## Design law (applies to every cover and every A+ module)
- **Exact strings.** Title, subtitle, and author WORDING appears verbatim
  (Title Preservation Law). A single wrong or missing character is a
  production failure. Verify letter by letter after generation; regenerate
  on any error.
- **Titles in BLOCK LETTERS, always (operator directive 2026-08-13,
  non-negotiable).** Every cover title renders in block capitals in every
  niche. The only permitted exception is a trademark's own letterform
  convention inside the block setting (iPHONE, not IPHONE or iPhone).
  Subtitles and chips may use mixed case when the references support it.
- **Comprehensive prompts (operator directive 2026-08-13).** Every
  generation prompt must specify EVERY aspect of the cover: canvas and
  aspect, full scene with photographic detail (subjects, wardrobe, props,
  setting, lighting, camera feel), complete typography (every line's face
  style, size relationship, colour, placement), every chip/badge/motif with
  exact colours, footer, margins, and the full negative list (no logos, no
  trade dress, no extra badges, no misspellings). Nothing is left for the
  generator to improvise.
- **Photorealism.** People, hands, devices, and settings must look like real
  photography: natural skin texture, believable hands and fingers, real
  lighting and depth of field. Illustration styles are used only where the
  niche pattern calls for them (e.g. children's, humor cartoons).
- **Text treatment follows the bank.** The typography of every text element
  (case style, serif/sans character, weight, colour emphasis, arrangement)
  is derived from the shared-pattern analysis of the picked `cover_db/`
  references plus the niche row below. There is no fixed house cover font;
  a text treatment that ignores the reference analysis is a design failure.
- **Title sizing.** The full title occupies at most FOUR lines, sized to the
  band 36-90 pt (at 8.5x11; scale to trim). Key words largest, connectors
  smaller. Never break a word; never reword to fit.
- **Complete text containment (operator directive 2026-08-13).** No word,
  letter, or text element is EVER cut off, clipped, or partially hidden on
  any cover, wrap panel, or A+ module: nothing touches or crosses the image
  edge, the trim or fold lines, or the final crop zone, and no element
  overlaps text. Because generation sizes rarely match final frames exactly,
  every composition keeps ALL text inside the final crop-safe zone (wrap:
  the finisher's crop tolerance plus print safe margins; A+: the 970x600
  frame) with comfortable clearance. A single clipped character is a
  production failure: recompose and regenerate, never ship a crop that
  touches text.
- **Premium finish bar (operator directive 2026-08-13).** Every cover and
  A+ module must look like it came from a top publisher's design studio:
  balanced composition with aligned grids and consistent spacing, cohesive
  colour harmony, crisp edges and clean type rendering, consistent lighting
  and shadows across composed elements, high-detail photorealism where
  photography is used. Amateur tells are QA failures: muddy gradients,
  mismatched shadows, warped anatomy or objects, blurry or aliased type,
  crowded layouts, decoration that serves no function.
- **Thumbnail first.** Amazon sells at ~100 px wide. The title must read and
  the concept must carry at thumbnail size. Judge every design at thumbnail
  before full size.
- **No-Two-Books-Alike.** Palette, composition, and type treatment must differ
  from the last five Pegasus covers; background base colour never repeats
  within a five-cover window. Record the design fingerprint.
- **Truthful covers.** No invented badges ("Best Seller", award seals), no
  fabricated counts or claims. Factual content counts (for example a real
  question count) are permitted where the niche convention expects them.
- **Content restrictions (enforced silently, never named):** no pork or pig
  imagery, no alcohol (no wine glasses, bottles, bars), no gambling imagery.
  Wholesome and family-safe throughout.
- **No publisher name** anywhere reader-facing. Author is the pen name only.
- **No em dashes** in any cover, back copy, or A+ text.
- **No real brands or trade dress** (logos, product shapes, celebrity faces).

## Per-niche pattern library (from the 2026-08 study of the banked covers)
Use the niche's row as the default art direction; the banked refs picked for
the book refine it. All 29 niches are covered; the refs always win a conflict
because they are newer than this summary.

**cookbook.** Hero food photography rules: either ONE overhead hero dish
(traditional style, generous negative space, clean field) or a bright grid of
4-8 finished dishes framing central type (indie style). Warm appetizing light.
Titles: friendly bold serif or mixed serif/script lockups; whites, creams, or
one saturated field colour (yellow, teal, red). Author photo only for
personality brands. Benefit subtitle line is normal.

**study-guide / exam prep.** Deep navy or dark field, MASSIVE condensed
white/yellow acronym title (the exam name IS the cover), yellow accent bars,
year chip ("2026-2027"), checkmarked feature list, red accents. Factual counts
(practice questions, tests) are the niche convention. High contrast, zero
subtlety. Pegasus house exemplar (MEDSURG 90/48 pt minimal) stays the default
for our study guides; use the busy convention only on operator request.

**selfhelp.** Type-driven. One or two flat colours (green, orange, yellow,
black, cream), title huge and plainspoken, often a single witty visual motif
(tangled line, coffee splash, small icon-scale illustration). Zero photography
of people. Subtitle states the promise plainly. NYT-style credibility strip
only if truthful.

**childrens.** Full-bleed warm illustration; the character(s) make eye contact
or engage in the action; hand-lettered or rounded playful title integrated
into the scene; bright saturated skies, greens, blues. Title words stacked
with size variation. Illustration style must be consistent with the interior.

**travel.** Full-bleed destination photography with saturated colour (golden
hour, teal water, red rock) and clean white or coloured type bands; publisher
colour-block header convention (orange/blue bar) reads "guidebook" instantly;
big numerals for list-driven titles ("50 States, 5000 Ideas"). Spiral-bound
look and map motifs are shelf cues.

**business.** Flat bold colour field (white, black, one saturated hue), title
enormous and declarative, one small iconic motif at most (brain, coin, knot).
Serif = authority, sans = modern. Subtitle carries the promise. Very high
thumbnail legibility.

**health / fitness.** Two families: (a) instructional: bold condensed caps on
black/dark field with orange/yellow accents, demonstrator photo mid-exercise,
feature chips (niche convention, keep truthful); (b) anatomy/reference:
clean white/light field with anatomical illustration. Seniors titles: calm
palettes, readable type, real older adults depicted respectfully.

**history.** Period photography, painterly scenes, or archival texture; serif
caps titles, restrained palettes (sepia, navy, oxblood, charcoal); single
strong artifact or portrait as focal object; subtitle as a promise of scope.
Gravitas over decoration.

**journal / low-content.** The cover IS the product: flat decorative field
(one warm colour, florals, celestial pattern, or bold typographic poster),
title centered in elegant serif, script, or chunky display; interior promise
in a small band ("A guided journal", "5-minute practice"). Texture (linen,
foil-look) reads premium. No photography.

**crafts.** Bright yarn/material photography (the material is the hero),
finished-project collage or grid, cheerful saturated palette, rounded friendly
type, step-by-step promise chips (truthful only). Process photos of hands at
work signal "you can learn this".

**activity / puzzle.** Saturated single-colour or starburst fields (purple,
orange, teal), chunky display-caps title, LARGE PRINT banner chips, sample
puzzle vignettes as a montage, factual count chips ("175+ activities").
Spiral-bound look reads "workbook you use". Kraft-paper hand-lettered variant
for the gift register.

**biography / memoir.** The subject IS the cover: full-bleed portrait (often
black-and-white or muted), the NAME huge, sometimes larger than the title,
letterspaced serif caps, bestseller strip at top. Famous single names support
a type-only cover on a flat or black field. Restraint reads as credibility.

**childrens-facts.** NatGeo convention: saturated yellow or blue field,
explosive photo collage of animals and objects, a GIANT numeral as the hero
("1,000", "5,000"), thick outlined bubble caps, circular photo insets.
Younger band: flat friendly cartoon illustration with rounded type.

**exam-simulator.** Brand bar at top, massive acronym in white or yellow on a
dark or fully saturated field (navy, red, yellow, pink), year-range chip,
checkmarked feature list with real counts (questions, tests, flashcards),
platform/colour-edition badges. Busier than the study-guide row; truthful
counts are the currency of the shelf.

**faith / devotional.** Two families: (a) faux-leather cover look with gold
foil ornament, debossed script-plus-serif lockup, classic gift feel; (b) calm
scene or soft flat field (florals, watercolor, sky) with elegant serif or
script title. Warm quiet palettes (brown, terracotta, blush, sky blue),
author name prominent. Serenity over salesmanship.

**fiction.** Full-bleed atmospheric art or photography; the mood signals the
genre: stark type over an unsettling detail (thriller), a figure from behind
in period dress (historical), painterly or botanical decoration (book club).
Large serif or elegant display title, author name big (the brand), bestseller
strip or pull quote. Rich saturated or moody palettes.

**howto (DIY / garden / workshop).** The subject material is the hero: bright
photography or flat illustration of tools, produce, or projects; green and
earth palettes for garden, kraft and wood for workshop. Bold condensed caps,
ribbon/banner chips with truthful counts ("50 projects"), step-by-step
promise lines. DK-style clean white grid variant for reference-grade.

**humor.** Flat bold colour field (red, blue, kraft), typographic joke title
in chunky or typewriter type, ONE deadpan visual gag (a single photo or
cartoon), parody-of-a-serious-genre framing. Restraint sells the irreverence.

**language.** Stacked caps with the LANGUAGE NAME largest, two-tone type
(yellow/white on red, purple, navy), promise chips ("in 30 days", "3 books in
1", level chip "A1-A2"), flat cultural motifs or a world-map device, bonus
banners. Indie convention is busy; traditional publishers run cleaner
two-colour typographic covers.

**medical (professional/nursing).** Publisher-grade: abstract scientific
texture or gradient field (crystalline, mosaic, marbled), clean humanist
serif/sans title lockup, edition chip, author strip along the top, publisher
bar at the foot. The indie certification-prep variant follows the
exam-simulator row instead (dark field, yellow accents, count chips).

**parenting.** Two families: (a) warm flat field (yellow, teal, coral) with
hand-drawn childlike illustration or speech-bubble motif and friendly mixed
hand-lettering; (b) clinical-trust: clean field, large clear sans, medical
authority cues. Emotion words picked out in accent colour; truthful
credibility strips are the norm.

**poetry.** Type-first elegance in two registers: (a) minimal, small lowercase
serif or script title on cream or black with one delicate line-art motif;
(b) ornate anthology, dark field with gold botanicals, feather, or floral
frame. Restrained palettes; whitespace is the luxury cue.

**popular-science.** Big idea = big type: flat saturated field or cosmic
photography, huge clean sans/serif title, ONE iconic motif (head silhouette,
butterfly, planet), bestseller strip, subtitle carries the promise. DK
visual-guide variant: full-bleed photographic subject under clean white type.

**public-domain / classics.** The cover sells the EDITION, not the story:
deluxe hardbound object design, ornamental gold-foil frames and motifs on
deep jewel fields (navy, oxblood, black, cream), engraved or woodcut-style
scenes, consistent series geometry. Premium finish cues everywhere.

**reference.** Trust-brand convention: primary-colour blocking (red, yellow,
blue, green), the CATEGORY as the giant title ("Dictionary", "Thesaurus",
"Encyclopedia"), edition and feature bullet list, brand seal or roundel.
Crisp and information-dense, zero atmosphere. DK visual variant: photo grid
on white.

**sports.** Two families: (a) archival or action photography full-bleed
(stadium light, an iconic moment) with condensed caps and varsity/team-colour
accents (orange, yellow on navy, black); giant numerals for anniversary and
history titles; (b) instructional: calm course or field photography, serif
title, quiet composition (the golf school).

**textbook.** Publisher-grade: full-bleed concept photograph (a person in
action, often with a scientific overlay) or clean editorial illustration;
light humanist sans title lockup at top or bottom; edition chip and author
strip; publisher colour bar. Indie study-companion variant: bright field,
chunky caps, count chips.

**user-guide.** The device IS the cover: large product image or screenshot on
a white or flat field, giant device name and version numeral, accessibility
promise chips ("LARGE PRINT", "step-by-step", "full color"), smiling users
mid-use for the seniors band, very high contrast type. Pegasus constraint on
this shelf: our device forms stay generic, no trade dress, logos, or official
renders.

**workbook.** Function-forward: the practice format is visible on the cover
(ruled or dotted lines with sample lettering, worksheet snippets), chunky
slab or display title naming the exact skill, page-count and feature chips,
high-contrast panel blocks on dark or bright fields. Therapy workbooks run
calmer: soft-focus field, clean serif, a concrete plan promise ("a 7-week
plan").

## Cover workflow (ChatGPT is the engine)
1. **Brief.** Assemble inputs + the 2-3 refs. State the shared winning pattern
   of the refs in one paragraph (composition, colour, imagery, mood) PLUS an
   explicit text-treatment line: title case style, serif/sans character,
   weight, colour emphasis, and arrangement observed across the refs. Every
   concept and generation prompt must carry this text treatment.
2. **Concepts.** Write THREE distinct concepts (A/B/C) that each fit the shelf
   pattern and differ from each other and from the last five Pegasus covers.
   Operator picks one (or autopilot picks the strongest and says why).
3. **Front cover generation.** ChatGPT Image 2.0 generates at 2:3 portrait
   with the exact title, subtitle, and author text rendered in the design,
   in the bank-derived text treatment and exact casing. No other generator
   and no local typography compositing is ever used for a cover. Inspect at
   full size AND thumbnail. Verify every string letter by letter. Iterate
   (max 4 passes) on spelling, crowding, margin violations, contrast.
4. **Full wrap.** Get exact dimensions from the KDP cover calculator (or the
   fallback math: spine = pages x 0.002252 in bw-white / 0.0025 cream /
   0.002347 colour; width = 0.125 + trim + spine + trim + 0.125; height =
   trim + 0.25). Have ChatGPT extend the chosen front into one continuous
   back + spine + front wrap at that aspect: back copy laid out clean, spine
   text (title + author) only if pages >= 100, a clear light 2 x 1.2 in
   barcode zone bottom-right of the back, nothing important within 0.375 in
   of any edge, no text within 0.0625 in of the spine folds.
5. **Finish.** Run the finisher at
   `%LOCALAPPDATA%\FlowPipeline\kdp_cover_wrap.py --finish <config> <wrap.png>`
   (mirror: `CodexBookStudio/scripts/cover_wrap.py`) to scale
   to exact print pixels and export the print PDF. ONLY `--finish` mode is
   used for covers: it scales without touching the design. The scripts' full
   compose mode (local Times typography over art) is not a cover path; text
   belongs to ChatGPT and the bank-derived treatment. The deliverable is ALWAYS
   the single continuous wrap PDF. Record the fingerprint (palette, motif,
   type treatment) in the catalog log.

## A+ Content system (970 x 600 px masters)

**DENSE INFOGRAPHIC LAW (operator correction 2026-08-13, from the live A+
study).** Live study of best-seller A+ sections (banked at
`cover_db/_aplus/`) shows the winning convention is NOT flat photo posters:
every module is a DESIGNED INFOGRAPHIC with structured components. Every
Pegasus module must be built from this component kit, in the cover's palette
and type family, block-letter headlines:

- **Two-tone headlines**: main words in the principal colour (or white on
  dark), one or two key words picked out in the accent colour, optional
  accent underline.
- **Icon chips and cards**: benefits and features NEVER appear as plain text
  lines; each sits in a rounded card or chip with a small circular icon,
  bold block-letter label, and 3-8 word micro-copy beneath.
- **3D book render**: the hero module shows the PHYSICAL book (the real
  front cover on a 3D paperback render), not just a scene.
- **Open-book mockup**: the interior module shows a photoreal open spread
  with believable styled pages (steps, panels, figures) matching the real
  interior system.
- **Badge roundels**: truthful edition badges only (for example LARGE PRINT)
  as circular seals; never invented awards.
- **Pill banners**: a rounded full-width or centered pill carries the
  module's closing caption line.
- **Numbered plan graphics**: when the book has a sequence (a practice plan,
  steps, units), render it as a connected numbered timeline.
- **Integrated photography**: photoreal people from the book's audience
  appear INSIDE the composition (cut into panels, beside cards), never as a
  lone background.
- **Rich backgrounds**: saturated brand-colour fields, soft gradients, or
  blurred lifestyle scenes with colour overlay; never plain white voids.

Before designing any A+ set, pull real shelf references from the A+ bank:
`python .agents/skills/uapf-cover-db/aplus_db.py pick --niche <x> --count 4`
and study them next to this component kit (fall back to the nearest stocked
niche while the bank is still filling).

**One module = one image = one file (operator directive 2026-08-13).** Every
module is GENERATED as its own separate image, composed for the 970x600
frame (generate at the nearest supported landscape size with all critical
content inside the 1.617:1 crop zone, then finish to exactly 970x600), and
DELIVERED as its own separate PNG file. Modules are never combined onto one
canvas, sheet, or strip at any stage: not in generation, not in delivery,
and not in operator previews (preview modules as individual files).

Produce 3 to 5 modules, each 970x600, compositions all distinct. Standard
functional sequence (per uapf-formatting-standard section 19):
1. **Hero**: 3D book render + two-tone promise headline + 2-3 icon chips +
   badge roundel + short subline.
2. **Benefits**: headline + 4-6 icon benefit cards in a grid + integrated
   audience photo + pill caption.
3. **Interior preview**: open-book mockup of real-looking pages + 2-3 labels
   naming actual sections + accent headline.
4. **Plan / feature deep-dive**: numbered timeline or central diagram with
   icon cards around it (whatever the book's true structure supports).
5. **Closing value**: warm audience scene + two-tone value headline + author
   line or truthful edition badges.
Text rules: A+ policy allows no prices, no ratings or review quotes, no
"best seller" claims, no competitor references, no URLs. Keep text short and
large: it is read on a phone. All imagery obeys the design law above.

**Back cover follows the same language**: two-tone block-letter headline,
icon-chip bullets (never plain dashes), a small interior-page or open-book
mockup where space allows, background continuous with the front cover's
world, optional truthful badge, generous clear barcode zone. A flat
text-only back is a design failure on this shelf.
Codex's native gpt-image tool generates each module at 3:2 landscape with
all text rendered in the design, matching the reference set's exact type
treatment (A+ Law v2 below governs and supersedes on any conflict). Finish
by center-cropping and resizing onto the exact 970x600 canvas.

## QA gate before delivery (cover and A+)
- [ ] Every string exact, including casing: title, subtitle, author, back
      copy, module captions
- [ ] No text cut off anywhere: every word fully visible with clearance
      inside the final crop zone on the cover, every wrap panel, and every
      A+ module (check after finishing/cropping, not just on the raw image)
- [ ] Premium finish: composition, type rendering, lighting, and photoreal
      quality pass the top-publisher bar; no amateur tells
- [ ] Text treatment matches the banked-reference analysis recorded in the
      brief; generated by ChatGPT Image 2.0, no local typography compositing
- [ ] Thumbnail test passed (cover) / phone-width test passed (A+)
- [ ] No excluded content, no invented badges or claims, no brands
- [ ] Wrap PDF at exact calculator dimensions; barcode zone clear
- [ ] Palette differs from the last five covers; fingerprint recorded
- [ ] No em dashes anywhere

## PREMIUM HD + REFERENCE ORIGINALITY LAW (operator directive 2026-08-15)

1. PREMIUM, HIGH DEFINITION, always. Every generated cover and A+ image is
   produced at the highest available generation quality and must be crisp at
   full KDP print resolution (300 DPI at trim: a 6x9 front is 1800x2700 px
   minimum, an 8.5x11 front is 2550x3300 px minimum; A+ masters exactly
   970x600 but generated oversize and downscaled clean). Soft focus, upscale
   blur, artifacts, muddy text edges, or low-res sources are production
   failures: regenerate, never ship a soft image.
2. REFERENCES INSPIRE, NEVER GET COPIED. The cover bank exists to teach the
   niche's conventions: study the picked references for their STYLE, their
   typography treatment (fonts, weights, arrangement), their palette norms,
   and their composition patterns, then create an ORIGINAL cover in that
   spirit. Similar is good; identical is forbidden:
   - never reproduce a specific reference's artwork, photo, scene, or
     layout one-to-one;
   - the generated imagery may resemble the genre look but must be clearly
     its own image side by side with every picked reference;
   - before finalizing, compare the candidate against the picked references
     and against the catalog (No-Two-Books-Alike): if it could be mistaken
     for any of them at thumbnail size, redo it with a different scene,
     angle, or arrangement.
3. This law binds BOTH engines and every install, and applies to fronts,
   wraps, spines, and every A+ module.

## OPERATOR-UPLOADED REFERENCE COVERS (operator directive 2026-08-15)

The operator may upload a specific cover image and ask for "something
similar or better". ACCEPT AND FOLLOW that instruction; it takes priority
over the bank pick for that book:

1. Treat the upload as the PRIMARY reference: analyze its style, palette,
   typography treatment, composition, mood, and imagery approach, and
   produce an original cover in that spirit at equal or higher quality
   (Premium HD law applies in full).
2. "Better" means: sharper execution, stronger thumbnail impact, cleaner
   typography hierarchy, richer premium finish, while keeping what makes
   the reference work.
3. Originality still governs third-party uploads: similar but never
   near-identical, no copied artwork or one-to-one layout clone, and never
   any logo, brand mark, series trade dress, or author branding from the
   reference. The thumbnail-confusion test applies.
4. When the operator states the upload is their OWN (Pegasus/catalog)
   cover, a direct improvement of that same design is allowed on their
   instruction; No-Two-Books-Alike then applies against the rest of the
   catalog, not against the book's own prior cover.
5. All standing cover laws still bind: exact title preservation, block
   letter titles, comprehensive photoreal prompts, text containment
   verified post-crop, and the wrap geometry.

## POST-COMPLETION COVER GEOMETRY (operator directive 2026-08-15)

When a cover is produced after the book is finished (the normal flow:
covers immediately after release QC):

1. USE THE BOOK'S EXACT TRIM. Read the locked trim size, the FINAL rendered
   page count, and the paper/ink type from the finished project
   (book_lock.md and the final PDF), never a projection or default.
2. MEASURE WITH THE KDP COVER CALCULATOR FIRST. Before generating anything,
   open Amazon's KDP Cover Calculator (kdp.amazon.com/cover-calculator) in
   the browser, enter the binding, trim, page count, and paper type, and
   record the official full-wrap dimensions: total width and height with
   bleed, spine width, and the template measurements. These OFFICIAL
   numbers govern; cross-check the local wrap math (cover_wrap.py /
   kdp_cover_wrap.py) against them and on any mismatch the calculator
   wins. Save the measurements in the project's cover records.
3. DELIVER ALL FOUR PIECES: the FRONT cover, the BACK cover, the SPINE, and
   the assembled full PAPERBACK WRAP as a print-ready PDF at the exact
   calculator dimensions (with bleed, barcode zone respected). The front
   also ships as the marketing image. Premium HD, containment, and every
   standing cover law apply to each piece.

## HARDCOVER (CASE LAMINATE) EDITIONS (operator directive 2026-08-16)

On "Genie, hardcover edition of [Title]" (or when the launch plan calls
for one), produce a KDP case-laminate hardcover alongside the paperback:

1. TRIM CHECK FIRST, LIVE. KDP hardcover supports a narrower trim list
   than paperback (historically 5.5x8.5, 6x9, 6.14x9.21, 7x10, and
   8.25x11 inches) and a narrower page-count range. Verify the CURRENT
   supported trims and page range live on KDP before committing. If the
   book's locked trim is unsupported (8.5x11 books map to 8.25x11),
   surface the nearest supported trim to the operator and re-lock their
   choice for the hardcover edition only; the paperback keeps its trim.
2. MEASURE WITH THE KDP COVER CALCULATOR IN HARDCOVER MODE. Case laminate
   geometry is NOT paperback geometry: it adds board wrap, hinge, and a
   much larger total canvas. The calculator's hardcover numbers govern;
   never reuse paperback wrap math.
3. SAME ART, NEW GEOMETRY. The hardcover wrap re-lays the approved cover
   art onto the hardcover template: identical art direction, block-letter
   title system, and palette, so the editions are visibly one book.
   Deliver front, back, spine, and the full case-laminate wrap PDF.
4. INTERIOR: identical to the paperback interior file unless the trim
   changed, in which case re-render and re-run render-containment QA at
   the hardcover trim.
5. LISTING: hardcover publishes as an additional format on the SAME
   listing, at a higher list price (typically +7 to +10 USD over
   paperback; margins are better). Price recommendation comes from
   market_math against hardcover printing cost. The publish click
   remains operator-confirmed per book, per format.

Hardcover is a PRO+ cover capability (the wrap is cover work); publishing
the edition itself is MAX (uapf-publisher gates apply).

## COVER COMPOSITION ARCHETYPES (operator directive 2026-08-19, catalog anti-sameness)

Covers are where catalog sameness costs sales: buyers see them side by side as
thumbnails. Every cover locks ONE composition archetype at cover time, recorded
in the fingerprint registry, and NO two catalog books in the same niche may
repeat the same composition + palette-family combination.

The menu:
- **C1 Title-top stack** — title block across the top third, art below it.
- **C2 Title-bottom band** — art fills the top two-thirds, solid color band
  across the bottom carrying title + subtitle.
- **C3 Centered plate** — full art with a central solid plate/panel holding the
  title block.
- **C4 Side stack** — vertical title column down the left or right edge (solid
  or tinted), art in the remaining field.
- **C5 Full-bleed + top band** — edge-to-edge art with a slim solid band at the
  top for the title.
- **C6 Framed** — art inside a framed field; title lives in the border zone
  (top or bottom), classic trade look.
- **C7 Split panel** — hard horizontal or vertical split between a solid color
  panel (title side) and an art panel.
- **C8 Typographic hero** — large block-letter type IS the cover; art reduced
  to an accent or spot element behind or beside it.

Rules that ride with every archetype: the block-letter title law and 4-line
sizing law bind unchanged; title text always sits on a solid or plated field
with verified contrast (never raw on busy art); thumbnail legibility is checked
at Amazon search-result size; the spine and back re-use the locked composition
language. MECHANICAL CHECK: before finalizing a cover, run
`python .agents/skills/uapf-quality-gates/fingerprint_registry.py check --niche
<x> --cover <C#> --palette-family "<family>" --palette "<#hex,...>"` and vary
on collision (palette first, then composition); register the final choice with
the book's registry entry. Binds BOTH engines; cover work remains PRO+.

## COVER LAW v2 (operator directive 2026-08-29, REPLACES the previous flow)

The compositor-first flow and bank-first referencing are retired as defaults.

1. REFERENCE HUNT, LIVE: search Amazon Books on the book title's lane. Screen
   candidates by rating/reviews AND by eye (a 5.0 with one review does not
   qualify a weak design). Pick the BEST THREE and SHOW them AS IMAGES
   (operator directive 2026-08-29): download each reference cover image and
   DELIVER the actual image files in chat (file delivery, not links, not
   descriptions) together with each book's rating and what makes its design
   work, BEFORE any generation begins. The operator must be able to see with
   their own eyes what the covers are being modeled on. Then bank all three
   into cover_db with design notes. Author-photo covers are never references
   (no real person to photograph; AI portraits passed as real people are
   banned).
2. PATTERN READ: extract the shared pattern (composition, surface, palette,
   type zone, badges, props). The EXACT TYPE SYSTEM of the best reference may
   be copied: letterforms, script/serif/sans hierarchy, letter-spacing,
   dashes, badge shape and placement, author position. The WORDS, the
   subject, and the palette stay ours: pattern copied, book not cloned.
3. ONE BRIEF, WRITTEN AS A REAL PHOTOGRAPH: editorial language, natural
   light, real textures and imperfections; "flat", "vector", or mechanical
   output is a failure. Every piece of cover text is in the brief VERBATIM
   (exact title per the Title Preservation Law, subtitle, author, badge
   text) with "spelled exactly as given". Content laws ride silently: no
   pork or alcohol in any scene, no prohibited claims, no fabricated
   bestseller badges or credentials.
4. DUAL-ENGINE GENERATION: the same brief produces a COMPLETE cover (type
   included) on BOTH engines: Codex and ChatGPT via the logged-in browser.
   The operator compares both and picks the winner. No cover ships unseen.
   CODEX SPEED LAW (operator directive 2026-08-29): every Codex image call
   (covers AND A+ modules) runs through the FAST IMAGE RUNNER in this folder:
   `python .agents/skills/uapf-cover-aplus-designer/codex_fast_image.py
   --brief <brief.txt> --out <file.png> [--image <exact_cover.png>]`.
   It generates in a clean room (state/codex_imgroom, 4-line AGENTS.md) so
   Codex never loads the 70KB Genie law file, forces
   model_reasoning_effort=low (the image model is separate, quality is
   unaffected: proven 76s for a full 1536x1024 editorial photo vs 3+ minutes
   before), pipes the brief via stdin (argv quoting mangles multiline briefs
   on Windows and hangs codex on stdin), and runs --ephemeral with the
   sandbox-block rescue built in. Never run a bare `codex exec` from the
   Genie root for an image: the global config's xhigh reasoning makes it
   crawl. When both engines generate, fire them CONCURRENTLY, not one after
   the other.
5. QA BEFORE SHIP: verify every word on the image is spelled exactly right
   (never trust AI-rendered type blind), title legible at thumbnail size,
   nothing overlapping or cut off. Record the pattern + palette pair in the
   design fingerprint: it may not repeat within a niche. The winner then
   gets print-resolution upscale and the KDP wrap (cover_wrap.py +
   render_qa.py in the full-access phase, Genie-generated artifacts only).

PREMIUM DESIGN BAR (operator directive 2026-08-29): every cover must read as
a design-studio product, never a homemade one. Enforced twice, in the brief
and at QA:

- THE BRIEF ART-DIRECTS LIKE A TRADE PUBLISHER. It must specify: ONE
  dominant focal element (never a collage of equals); a designed type
  LOCKUP with strong size contrast between title words, tight professional
  kerning and letter-spacing, at most two typefaces plus one accent script;
  a restrained palette of two to three colors in deep or desaturated hues
  (never pure RGB primaries); the type sitting on a calm zone or plated
  field with consistent margins; editorial photography lighting with real
  materials and visible texture; balanced negative space.
- AMATEUR TELLS, banned in every brief's negative list: bevels, outer
  glows, drop-shadow soup, default-font look, rainbow or 2010-style
  gradients, clip art, plastic AI sheen, stretched or squashed type,
  cluttered edges, elements touching the trim, more than three type
  families, centered-everything with uniform sizes.
- QA JUDGES BEFORE THE OPERATOR SEES. Before any candidate is delivered in
  chat, LOOK at it and judge it against the amateur-tells list AND against
  the best banked reference: if any tell is present, or the design reads
  visibly weaker than the reference it is meant to beat, REGENERATE first
  with the brief tightened. The operator only ever compares premium
  candidates; showing an amateur-looking cover is itself a production
  failure.

FALLBACKS: if live Amazon search is unavailable (Codex failover, scraping
breakage), use `cover_db.py pick --niche <x> --count 3` and log it. If
AI-rendered type repeatedly misspells, fall back to textless art +
cover_compose.py (retired as default, kept for exactly this).

COVER DB IS DEMOTED: no install-time seeding, no completion gates, no
scheduled whole-bank refresh. It grows organically from step 1's banking and
serves as the fallback and pattern-notes library.

## A+ LAW v2 (operator directive 2026-08-29, REPLACES the previous A+ flow)

Proven and operator-approved on the self-help and cookbook rounds. Where this
law and the older A+ system text above disagree, THIS LAW WINS.

1. EXACTLY FIVE MODULES per book. Never three, never four; five distinct
   compositions in the standard functional arc (hero mockup + benefits,
   food/subject collage + promise panel, tile grid of labeled benefits,
   lifestyle scene + promise + mockup, closing call-to-action + mockup), bent
   to what the reference set actually does in the niche.
2. REFERENCES, LIVE AND INDIE: search Amazon in the book's niche and pull the
   A+ section of INDEPENDENTLY PUBLISHED best sellers only (traditional
   publisher A+ is styled for brand catalogs, not KDP shelves). Prefer
   references whose modules are natively 970x600. Show the picked reference
   modules to the operator in chat, then bank them:
   `python .agents/skills/uapf-cover-db/aplus_db.py bank --niche <x> --json
   <asin-to-urls.json>`. The bank (`cover_db/_aplus/`) is the fallback when
   live search is unavailable, same demoted status as cover_db.
3. COPY THE EXACT FONTS, WRITE BETTER TEXT: the reference set's exact type
   system is copied (letterforms, condensed/italic caps ribbons, rounded
   sans, case, weights, badge and panel shapes, dashed borders, layout
   skeleton). The COPY is ours and must be better: sharper benefit lines,
   concrete counts from the real book (recipe/project/chapter counts),
   nothing generic. Palette is OURS (the book's fingerprint palette), foods
   and scenes are ours, and the content laws ride silently (no pork or
   alcohol in any scene, no em dashes, no prices, no ratings or review
   quotes, no "best seller" claims, no fabricated awards, badges, quotes, or
   AI portraits passed as real people).
4. THE EXACT GENERATED COVER IN EVERY MOCKUP: any module showing the book
   (hero, lifestyle, closing) uses the EXACT final cover image as an attached
   input, never a re-imagined lookalike:
   `codex exec --sandbox workspace-write --image="<final_cover.png>" ...`
   (the equals form; the bare `-i` flag is greedy and swallows the prompt).
   The brief says "reproduce this exact cover faithfully, including all its
   text". A mockup whose cover text drifts from the real cover FAILS QA.
5. SIZE: every delivered module is EXACTLY 970x600 px. Generate at 3:2
   landscape (1536x1024) with every text element and key subject at least 8
   percent away from the top and bottom edges, then center-crop to the
   970:600 ratio and LANCZOS-resize to 970x600. A crop adjustment over 10
   percent means the wrong file was picked up; stop and verify dimensions.
6. ENGINE: CODEX SINGLE-ENGINE IS THE LAW for A+ (operator directive
   2026-08-29). Unlike covers (dual-engine compare), A+ modules are generated
   by Codex's native gpt-image tool only (`codex exec --sandbox
   workspace-write`, model_reasoning_effort=low). The ChatGPT browser is NOT
   part of the A+ flow: it proved unreliable at this volume (frozen tabs,
   storage-quota modals, download collisions). If a future session tries
   ChatGPT for A+ and hits ANY friction, it stops and sticks to Codex.
7. QA BEFORE DELIVERY: on every finished 970x600 file verify (a) every word
   spelled exactly as briefed, (b) mockup cover matches the real cover
   letter for letter, (c) no text or key element clipped by the crop,
   (d) all five compositions distinct. Deliver as five separate PNG files
   (one module = one image = one file), named
   `<ENGINE>_<niche>_moduleN.png`, and show them to the operator.

Binds BOTH engines and every install tier where A+ work is available.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
