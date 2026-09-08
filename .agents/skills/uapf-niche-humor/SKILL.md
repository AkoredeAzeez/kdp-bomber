---
name: uapf-niche-humor
description: Niche overlay for Humor & Comedy / Gift Books (OV-HUMOR) — invoked by uapf-phase0-router when title or format signals match humor, comedy, joke books, or audience-specific gift books.
---

# UAPF Niche: Humor & Comedy / Gift Books (OV-HUMOR)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-Humor-Edition/` (config, validation, phases, and deterministic ops in `genie_humor.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 Humor Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** title or brief contains joke book, humor, funny, comedy, laugh, wit, hilarious, parody, gift book for [audience], gag book, anti-advice, survival guide (humor register), or the format is clearly entertainment/gift rather than instructional; OR audience-plus-occasion matrix slot resolves to a humor register per the UHSGF segment playbooks.

**Authority stack (highest first):** Standing Pegasus Press hard rules > UHSGF v2.0 > UAPF 2.4 > craft judgment. Where this overlay is silent, UAPF 2.4 applies. Where they conflict, OV-HUMOR wins.

---

## Expert Panel

1. **Humor Domain Master** — owns joke craft, register consistency, banned-humor enforcement, and the per-chapter humor quality gates. Reviews every chapter for laugh density, device variety, and fatal-flaw avoidance before the gate passes.
2. **Cultural-Calibration Specialist** — validates that all jokes, comfort props, daily-life references, fake-attribution names, and idioms are authentic for the target marketplace. Flags anything that reads as a literal translation rather than a re-created joke. Required for every non-EN build and for EN-AU, EN-CA, EN-UK localisations.
3. **Sensitivity Reader** — checks every chapter, list item, quote, image prompt, cover concept, and metadata field against the punching-down prohibition, the stereotype harmful-reinforcement rule, and the protected-characteristic guardrails. Flags and rewrites before gate.
4. **Interior Design Auditor** — enforces the locked typography pair, image placement quotas, style-only formatting, section-break folio logic, and the image prompt grammar. Confirms black-and-white line art only, no color interior, and no direct manual formatting anywhere in the DOCX.
5. **KDP Metadata Strategist** — owns category path selection, keyword pool hygiene, listing description formula, pricing band compliance, and A+ module plan. Confirms no trademarked terms, no competitor names, and no flagged-publisher terms in any metadata field.

---

## Phase 0 — Title Analysis

### 0.1 Matrix slot assignment
Every concept is defined by three axes: Audience x Occasion x Pain Point. Assign the slot ID in the format AUD-OCC-PAIN (e.g., WOMEN-BDAY-STRESS, NURSE-XMAS-BURNOUT). The slot ID anchors every working file, the evidence record, and the state ledger.

**Audience library (working set, not a cap):** Women, Men, Couples, Moms, Dads, New Moms, New Dads, Grandmas, Grandpas, Seniors, Retirees, Teens, College Students, Graduates, Best Friends, Sisters, Brothers, Introverts, Overthinkers, Night Owls, Dog Moms, Cat People, Plant Parents, Nurses, Teachers, Doctors, Managers, Accountants, Lawyers, HR Professionals, IT Professionals, Engineers, Drivers, Chefs, Servers, Retail Workers, Remote Workers, Freelancers, Small Business Owners.

**Occasion library:** Birthday, Milestone birthday (30/40/50/60), Christmas, Secret Santa, Mother's Day, Father's Day, Valentine's Day, Galentine's, Anniversary, Retirement, Graduation, New job, Job survived one year, Baby shower, New home, Get well soon, Just because, Long-distance friendship, Thank you, Apology adjacent.

**Pain point library:** Stress, burnout, no time for yourself, mental load, decision fatigue, no sleep, mornings, meetings, inbox overwhelm, housework that never ends, adulting, aging, forgetfulness, diet culture fatigue, gym guilt, social battery, saying no, comparison spiral, perfectionism, procrastination, kids' chaos, teenage drama, empty nest, retirement identity shift, coworker chaos, shift work, customer-facing exhaustion.

### 0.2 Title and subtitle drafting
Draft three candidate titles with subtitles per slot.

**Title formula:** Cheeky, audience-true statement, 3 to 8 words, speakable aloud in one breath.

**Subtitle formula:** Humor plus honesty positioning + gift trigger + audience pain point. Always carry a gift keyword phrase (e.g., "a gift for women who have everything except time for themselves"; "the honest survival guide for exhausted nurses").

**Hard limit:** Combined title plus subtitle must stay within 200 characters (KDP metadata field).

### 0.3 Trademark clearance
Run a trademark check on every candidate title before proceeding. Record results in the evidence record. No candidate with an active trademark conflict advances to Phase 1. This is a blocking hard rule.

Confirm title language equals content language. No English titles on non-English listings.

### 0.4 Competitor scan
Scan the top 20 organic results on the target marketplace for the audience plus humor keyword set. Record: BSR spread, review counts and ages, cover patterns, price band (category norm USD 7.99 to 14.99 or market equivalent), page counts, and publication dates.

Validate that at least one reachable Humor category and one Self-Help category exist with a realistic top-100 entry point.

### 0.5 Scoring rubric
Score the slot on five criteria: Demand (0-3), Differentiation (0-3), Seasonal Fit (0-1), Price Band Health (0-1), Category Access (0-2). Maximum 10 points.

- 7 or more with no zero in Demand or Differentiation: proceed.
- 5 to 6: proceed only with a documented angle justification.
- 4 or below: kill the slot, file the evidence for future reuse.

### 0.6 Seasonal timing
Reviews compound over 6 to 8 weeks. Never launch a seasonal title inside its final three weeks before the peak. State the seasonal window and the manuscript-locked-by date.

Key seasonal windows: Christmas (lock by mid-October), Mother's Day (lock by late March), Valentine's Day (lock by late December), Father's Day (lock by late April).

### 0.7 Auto-configuration on proceed
On proceeding past Phase 0, immediately run Phase 1 auto-configuration. Claude auto-selects every production option: audience segment, humor register, body size, line spacing, mascot or art-set decision, pen name (sourced from fakenamegenerator.com, format: First Name, Initial(s). Surname), three KDP categories, and seven draft keywords. Present one Auto-Configuration Package, then gate.

### 0.8 Evidence record output
The Phase 0 artifact holds: slot ID, three candidates with trademark results, competitor table, category paths considered, rubric scores, price band, seasonal target, and the kill-or-proceed decision with one paragraph of reasoning. Store with the state ledger. Never discard, including for killed slots.

End Phase 0 with: Type Proceed.

---

## Book Architecture

### Chapter formula
**Chapters:** 8 to 12 chapters. Every chapter follows the locked 5.9 beat blueprint in sequence:

1. **Opener page:** UH Chapter Label style, 24 pt BLOCK-LETTER Heading 1 centered, followed by UH Chapter Subtitle joke (in italics beneath). Whitespace does the rest. No body text on this page.
2. **Quote page:** Minimum one full quote page per chapter, placed immediately after the opener. Geometry: oversized black quotation marks upper left; the quote in UH Quote style, 2 to 4 short lines, maximum 18 words; a thin black rule; fake attribution in the exact form: Name Initial., age, absurd chapter-related job title. The quote is an original joke written for the book, never sourced from real people. Ages range 25 to 70 and vary across the book.
3. **Hook:** 2 to 3 body paragraphs installing the situation with one strong specific image. 120 to 180 words.
4. **Subchapter 1 (Heading 2, ALL-CAPS left):** Escalation of the situation. 150 to 220 words with one inline image.
5. **List device (UH List, left aligned):** 3 to 6 items, each a self-contained joke. Device types: "Signs that...", survival rules, honest translations, top fives. Left aligned always.
6. **Subchapter 2 (Heading 2, ALL-CAPS left):** The turn. The honest paragraph arrives here: one sincere beat inside the humor. 150 to 220 words with one inline or spot image.
7. **Closing beat (UH Closing Beat style, centered italic):** One warm permission line. Never cynical. This is the only place warmth is permitted to outweigh humor.
8. **Optional value element:** Mini quiz, checklist, or fill-in. At most one per chapter, at most four per book total.

**Chapter body length:** 600 to 900 words. Chapters carry visual weight, not word bulk.

### Structural unit
Humor Gift Book structural unit = Chapter unit (not recipe or project). Each chapter is a complete comedic arc: situation installed, escalated, turned honest, and closed warm.

### Page-band targets
- **Target extent:** 80 to 120 pages. Hard cap 120. Never exceed.
- **Trim size:** 6 x 9 in. All titles, all segments. No exceptions.
- **Body size:** 11 to 12 pt standard builds. Senior/elderly builds: 13 to 14 pt.
- **Line spacing:** 1.15 (default, protects the page cap at maximum image density) or 1.5. Claude recommends at Phase 1. Senior builds always 1.5 paired with larger body size.

### Front matter order (locked, all unnumbered)
1. Half-title art page: hand-lettered title treatment on the white page.
2. Copyright page: (a) letterspaced-caps edition block, centered: edition line plus month and year, localized; (b) copyright line with pen name; (c) all-rights-reserved text; (d) humor disclaimer — states the book is a work of humor, all quotes, names, ages, and job titles are invented, and it is not medical, psychological, or professional advice; (e) imprint line; (f) ISBN placeholder. Entire block centered.
3. Dedication: one short humorous paragraph, maximum 30 words.
4. Preface: exactly one page, in the book's voice, ending on a welcome, not a promise.
5. How to Use This Book: exactly one page. In-voice anti-rules as a short left-aligned numbered list: read in any order, no homework, skipping allowed, laughing counts, closing the book is permitted. Ends: "that is the whole system."
6. Table of Contents (see below).
7. Introduction: printed page 1. The anti-advice manifesto, what this book is and is not, and a what-awaits-you block. 350 to 500 words plus one spot image.

**Folio rule:** Front matter carries no page numbers. Folios begin at the Introduction as printed page 1 (automatic PAGE field, bottom center, in the body section only).

### Back matter order
- Conclusion: exactly one page. Enough-for-today energy; the one permitted callback lands here; warm close.
- Author bio: under the pen name, 60 to 90 words, in-voice, fictional persona consistent with the pen name.
- Review request page: one final joke plus one honest, unincentivized ask. Neutral ask only; no incentives, no instructions about star ratings.

### Table of contents specification (locked)
- Header: bold Lato, localized ("Contents" / "Inhalt" / market equivalent), thin rule beneath, left aligned.
- One entry per chapter: UH Ghost Numeral beside the entry; entry line as chapter number, middle dot, and chapter title in UH TOC Entry style; the one-line subtitle joke beneath in UH TOC Description.
- No page numbers in the TOC. Chapter numbers plus folio system carry navigation.
- Fits one page at up to 10 chapters; at 11 to 12 chapters may run 2 pages with balanced breaks.
- Built entirely on Word machinery, never manually formatted.

---

## Interior Design

### Typography (locked)
- **Display / serif elements:** Playfair Display (SIL Open Font License, free for commercial use, extended-Latin coverage).
- **Body / subheads / lists:** Lato (same license).
- **Japanese builds only:** Noto Serif JP (display) and Noto Sans JP (body).
- **Chapter headings:** 24 pt, BLOCK-LETTER (all caps), Heading 1 style, centered.
- **Subchapter headings:** ALL-CAPS, Heading 2 style, left aligned.
- **Body text:** justified, 11 to 12 pt (13 to 14 pt senior builds).
- **Lists:** left aligned always, never justified.
- **Closing beat:** centered italic, UH Closing Beat style.
- **Quote page text:** UH Quote style, 2 to 4 lines, max 18 words per quote.
- **Em dashes:** banned catalogue-wide. Use commas, parentheses, or a semicolon instead.

### Trim and color
- Trim: 6 x 9 in.
- Interior: plain white pages, black text. No background colors, tints, or shaded panels anywhere in the interior. Generous whitespace throughout.
- Color is banned from the interior. The cover is the only color surface in the book.

### Margins and gutter
House margins exceed KDP minimums deliberately; the extra air is part of the product. Mirrored margins on. Gutter value confirmed at final page count during the whole-book format pass (Phase 3c).

### Image system: black and white line art only
**Style A:** Minimalist continuous-line spot art. Dividers, margin accents, section breaks, tiny visual jokes. Single-weight line, no shading.

**Style B:** Detailed character line illustration with hatched shading and an expressive face. Theme characters, full-page moments, margin peek-ins that interact with the text.

Light grey wash accents are permitted sparingly. Color interior images are banned absolutely.

**Image placement quotas per chapter (minimum):**
- 2 inline images
- 2 spot images
- 1 quote page illustration
- 1 optional full-page image

Density is maximum: as many images as the content supports. Text-only pages are the exception. Every image relates to the title theme and carries a joke or a wink. Decoration without humor is filler and fails the audit.

### Image prompt template (mandatory when generation unavailable)
Every planned image is represented at its exact manuscript location by a bracketed prompt in UH Image Prompt style, numbered Chapter.Sequence, in this exact grammar:

```
[ IMG 3.2 · Style B inline, right margin · Subject: a sloth in pajamas peering over the paragraph edge · Composition: head and one arm visible, hatched shading, expressive half-open eye · Mood: unbothered · Constraints: black and white line art only, no text in image, no logos, no color ]
```

The constraints clause is mandatory on every prompt: black and white line art only, no text in image, no logos, no color, no real persons.

### Mascot rule
A recurring mascot is optional and title-dependent; Claude decides at Phase 1. When a mascot is used, the Auto-Configuration Package includes a five-line mascot bible: species, personality in one sentence, five recurring poses, how it interacts with text, and its closing appearance.

Mascot candidates: llama (chill), sloth (tired), cat (boundaries), owl (insomnia), tortoise (unhurried), penguin (formal chaos).

Themed spot-art sets may carry a book alone: dead plants, alarm clocks, tangled headphones, overflowing laundry, cold coffee cups.

Mascots must vary across the catalog. No mascot repeats within the same segment and language.

### Cover system (UHSGF override of UAPF default)
Humor Gift Book covers follow the category market standard: expressive hand-lettered or high-character typographic title on a textured neutral or bold solid field, with an optional Style A or Style B line-art element. This overrides the UAPF photorealistic-imagery default for this category only.

Still in force: no icons or badges as design crutches, no selling points on covers, background variety enforced across the catalog.

Front cover carries title and subtitle only; the pen name lives on the copyright page.

**Spine (100+ pages):** title only, reading top to bottom, in the cover display face.

**Back cover:** 3 to 5 short in-voice hook lines, one line-art element, ISBN zone clear.

---

## Content Rules

### Voice doctrine (anti-advice, locked)
The category voice is anti-advice. The book openly refuses to be a program: no five steps, no breathing exercises, no toxic positivity, no kitsch, no "just be grateful." It names the reader's reality exactly as it is, validates it with dry honesty and warmth, and then gives permission to rest.

- Humor punches at situations and systems, never at people or groups.
- Short declarative sentences. White space is part of the joke timing.
- Every chapter lands on a short, genuinely warm closing beat.
- The book may promise exactly one thing: that the reader is allowed to stop for a moment.
- Validation before consolation. The reader must feel seen before the book earns the right to be warm.

### The five humor registers (assign one per book, lock at Phase 1)
1. **Warm-dry:** Quiet observation, short sentences, wry recognition. Segments: Women, Seniors, Best Friends.
2. **Deadpan-absurd:** Logic taken to its extreme, bureaucratic language applied to domestic chaos. Segments: Overthinkers, Introverts, Remote Workers.
3. **Energetic-relatable:** Higher energy, exclamation-adjacent (never the mark itself), punchy. Segments: Teens, Young Adults, Graduates.
4. **Gentle-celebratory:** Soft humor that honours rather than roasts. Segments: Grandparents, Retirees, Milestone birthdays.
5. **Insider-professional:** Jargon weaponised against the system. Segments: Nurses, Teachers, Managers, Lawyers, all professional roles.

One register per book, declared in the Auto-Configuration Package, locked for the full manuscript. No tonal drift between chapters.

### Joke-type diversity quotas per chapter
Each chapter must contain at minimum:
- 1 observational joke (naming the reality exactly)
- 1 absurdist joke (logic taken to a surreal conclusion)
- 1 wordplay or misdirection joke
- 1 situational joke (specific scenario the reader recognises)

No single joke device may appear more than once per chapter. Variety is enforced at the per-chapter quality gate.

### Segment guardrails (all binding)

**Women:** Never mock her body, age, or choices. The joke is the day, not the woman. No wellness-guilt reversals (the book never implies she should be doing more).

**Men:** No lazy-husband cliches; competence is assumed, chaos is situational. Warm closes stay one line; never sentimental paragraphs.

**Couples:** Both partners get equal comedic weight; no punching at either role. No divorce, infidelity, or contempt humor anywhere in the segment.

**Parents (Mom and Dad sub-lines):** Kids are chaos agents, never targets; no jokes at a child's expense. No parenting-advice drift: the book validates, it never instructs.

**Seniors and Retirees:** Aging jokes stay gentle and self-owned; nothing about decline, illness, or memory loss. Retirement is a promotion, never an ending.

**Teens and Young Adults:** Internet-native rhythm without datable meme references; nothing that ages in six months. Anxiety is validated lightly, never dramatized or diagnosed.

**Professionals (by role):** Punch at the system and the shift, never at patients, students, clients, or customers. Insider jargon is explained by context, never footnoted; outsiders may smile, insiders must laugh.

### Banned humor list (absolute, no exceptions)
- Wine-mom and any alcohol-dependent humor (also a content restriction).
- Live-laugh-love mockery, hot-mess branding, "I cannot even" phrasing, Mercury retrograde jokes.
- Name-based stereotype jokes and any punching at a person or group, including mother-in-law humor.
- Dated meme formats and platform-specific slang that will age within a year.
- Repeated joke structures inside one book; each device appears at most once per chapter.
- Any humor that mocks religion, faith practice, ethnicity, or any protected characteristic.
- Dark humor that punches down (situational and observational dark humor is permitted; punching down is not).

### Content restriction rules (no exceptions, applies to every content element)
- No alcohol references anywhere: jokes, comfort props, quotes, images, image prompts, covers, or metadata.
- Comfort props are tea, coffee, and chocolate only.
- No pork or pig references.
- No gambling-positive content.
- Humor never mocks religion, faith practice, ethnicity, or any protected characteristic.
- Wellness-industry irony is permitted as satire of commercial wellness culture, never of any faith or practice community.

This rule applies to: text, quotes, attributions, lists, images, image-generation prompts, covers, A+ content, and listing metadata.

### Localisation rules (non-EN builds)
- Title language equals content language. No English titles on non-English listings.
- Humor is localized, never machine-literal. Idioms, comfort props, and daily-life references adapt to the market. Jokes are RE-CREATED for the marketplace, never literally translated.
- Fake attributions use names plausible for the marketplace language; ages and job-title comedy localize too.
- Measurements, institutions, school systems, and workplace references localize per market.
- Date format on the copyright page follows the marketplace convention.
- Japanese builds substitute Noto Serif JP and Noto Sans JP for the font pair.

### Fake attribution device
Quote pages use invented attributions in the exact form: Name Initial., age, absurd job title. Examples of the pattern: Dana K., 41, Professional Snooze Consultant; Robert M., 58, Head of the Committee for Later; Amara T., 34, Regional Manager of Overthinking; Femi A., 46, Senior Laundry Negotiator.

- Names must be plausible for the marketplace language.
- Names must never match real public figures.
- Ages range 25 to 70 and vary across the book.
- The absurd job title always relates to the chapter theme.
- Quote-page job titles never repeat across the catalog within a language.

### No real private individuals
No real private individual may be referenced, named, quoted, or illustrated anywhere in the book. Fake attributions and pen names never match real public figures. This applies to all content elements.

### The fatal flaw to avoid
The fatal flaw for this niche is **tonal drift**: chapters that begin in the correct humor register and slide into earnest self-help, toxic positivity, or unsolicited advice. The book must never start giving a program. The honest turn in Subchapter 2 is one sincere beat, not a pivot to instructional content. The closing beat is warm permission, not a call to action. The Humor Domain Master flags any drift before the chapter gate passes.

---

## QA Checklist

### Gate 1 — Phase 0 Evidence Record
- [ ] Slot ID assigned in AUD-OCC-PAIN format
- [ ] Three candidate titles with subtitles drafted; each within 200 characters combined
- [ ] Trademark check run on all three candidates; results recorded
- [ ] Top-20 competitor scan completed on target marketplace; table filed
- [ ] One reachable Humor category and one Self-Help category confirmed
- [ ] Slot scored on rubric; score stated with no zero in Demand or Differentiation if proceeding
- [ ] Seasonal window stated; manuscript-locked-by date stated
- [ ] Kill-or-proceed decision written with one paragraph of reasoning
- [ ] Evidence record complete and attached to state ledger

### Gate 2 — Phase 1 Auto-Configuration Package
- [ ] Slot ID, final title, subtitle, marketplace, language confirmed
- [ ] Audience segment assigned; humor register declared and locked (one register only)
- [ ] Body size and line spacing stated with reason (senior override applied if needed)
- [ ] Mascot decision made: named mascot with five-line bible, or themed spot-art set
- [ ] Art plan stated: Style A and Style B usage, quotas per chapter
- [ ] Trim 6 x 9 confirmed; page target within 80 to 120; chapter count 8 to 12
- [ ] Pen name sourced from fakenamegenerator.com in correct format
- [ ] Three KDP categories stated; seven draft keywords stated (each under 50 characters)
- [ ] Seasonal window and manuscript-locked-by date confirmed
- [ ] File name per naming convention; state ledger created

### Gate 3 — Phase 2 TOC Contract
- [ ] 8 to 12 chapters; every chapter title is a joke that survives being read aloud
- [ ] Every chapter subtitle is a second, smaller joke
- [ ] TOC layout: localized header, ghost numeral, chapter number + middle dot + title, subtitle-joke line beneath; no page numbers
- [ ] TOC fits one page (up to 10 chapters) or 2 balanced pages (11 to 12 chapters)
- [ ] Dedication line included (max 30 words)
- [ ] Preface plan, How to Use plan, and Introduction plan stated
- [ ] Localized structural labels confirmed for non-EN builds

### Gate 3a — Phase 3a Front Matter
- [ ] Half-title art page included
- [ ] Copyright page: edition block, copyright line, all-rights text, humor disclaimer, imprint line, ISBN placeholder; all centered
- [ ] Dedication: humorous, maximum 30 words
- [ ] Preface: exactly one page, in-voice, ends on a welcome
- [ ] How to Use: exactly one page, left-aligned numbered anti-rules, ends "that is the whole system"
- [ ] TOC: matches Phase 2 contract exactly, style-driven, no page numbers
- [ ] Section break confirmed: no folios before Introduction; Introduction opens as printed page 1 with automatic PAGE field

### Gate 3b (per chapter) — Chapter Quality Gate
Score all ten humor quality criteria; any FAIL blocks the gate until fixed:
- [ ] Register held (no tonal drift from the locked register)
- [ ] Joke-type diversity: at least one observational, one absurdist, one wordplay/misdirection, one situational
- [ ] No repeated joke device within the chapter
- [ ] No banned humor (list in Content Rules)
- [ ] Quote page present and correctly formatted (original joke, correct attribution format, within 18 words)
- [ ] Content standards: no alcohol, pork, gambling-positive content in any element
- [ ] No stereotype harmful-reinforcement (Sensitivity Reader sign-off)
- [ ] Image prompts: all correctly numbered and formatted with mandatory constraints clause; minimum quotas met; every image carries a joke
- [ ] Segment guardrail compliance (audience-specific rules)
- [ ] Closing beat: warm permission line, never cynical; the honest turn is one beat only, not instructional
- [ ] Chapter body: 600 to 900 words; all formatting via named styles only; no direct formatting

**Per-chapter report format:**
- Chapter number and title
- Word count
- Humor register: HELD / DRIFT DETECTED
- Joke types present (list)
- Banned humor check: PASS / FAIL (detail)
- Content-standards check: PASS / FAIL
- Sensitivity check: PASS / FAIL
- Image count by type (inline / spot / quote-page / full-page)
- All image prompts present with constraints clause: YES / NO
- Segment guardrail: PASS / FAIL
- Closing beat: WARM / NOT COMPLIANT
- Gate status: PROCEED / BLOCKED (reason)

### Gate 3c — Assembly Gate
- [ ] Conclusion: exactly one page, permitted callback present, warm close
- [ ] Author bio: 60 to 90 words, in-voice, under pen name
- [ ] Review request page: one final joke plus one honest, unincentivized, neutral ask
- [ ] TOC verified against final chapter list; heading-linked references refreshed
- [ ] Whole-book format pass: 6 x 9, mirrored margins, gutter confirmed at final page count, fonts embedded, folios start at Introduction as page 1
- [ ] Extent confirmed: within 80 to 120 pages

### Gate 4 — Cover, Metadata, and Release QC
- [ ] Three cover candidates delivered (A, B, C) with one-line design rationales
- [ ] Cover uses typographic or hand-lettered treatment; optional line-art element; no icons, badges, or selling points on front
- [ ] Front cover: title and subtitle only (pen name on copyright page, not cover)
- [ ] Spine (100+ pages): title only, top to bottom, in cover display face
- [ ] Back cover: 3 to 5 in-voice hook lines, one line-art element, clear ISBN zone
- [ ] No two covers in the catalog look alike; background and lettering variety confirmed
- [ ] KDP listing description: hook (anti-advice promise), 3 to 5 joke bullets, interior-experience line, gift-positioning close, specs line; within 4,000 characters
- [ ] Seven keywords: one per 50-character field, from four pools; no trademarks, competitor names, or flagged terms
- [ ] Category browse paths confirmed for target marketplace
- [ ] Price inside validated band; computed royalty stated
- [ ] A+ plan: promise banner, interior peek strip, gift-occasion module
- [ ] Release QC: interior preflight, cover wrap dimensions, metadata match, rights and AI-disclosure records, honest status flags throughout

---

## KDP Positioning

### Amazon category tree
Primary targets (confirm exact browse paths per marketplace at Phase 5; paths differ across stores):

- Humor > Humor & Entertainment > Work & Career Humor
- Humor > Humor & Entertainment > Self-Help & Motivational Humor
- Humor > Humor & Entertainment > Jokes & Riddles (for joke-forward titles)
- Self-Help > Personal Transformation (secondary; humor must dominate)
- Humor > Humor & Entertainment > Gifts (where available in the target store)

For professional-segment titles, layer in the relevant professional category as a third pick (e.g., Medical Humor for nurse titles, Education & Teaching Humor for teacher titles).

Exact browse paths are confirmed per marketplace at Phase 5.

### Category targets per segment
- Women: Humor > Self-Help & Motivational Humor + Women's Studies > Humor
- Men: Humor > Work & Career Humor + Self-Help > Humor
- Couples: Humor > Relationships & Family Humor
- Parents: Humor > Parenting Humor
- Seniors/Retirees: Humor > Aging & Retirement Humor
- Teens/Young Adults: Humor > Teen & Young Adult Humor
- Professionals: Humor > Work & Career Humor + relevant professional category

### Description leads with
The anti-advice promise, in the book's voice, 2 to 3 lines. Then: three to five bullets each carrying a joke about what's inside. Then: one line naming the interior experience (quote pages, line art, short chapters). Then: gift positioning close (who to give it to and for which occasion). Then: specs line (page count, trim, large-print note where applicable).

Total within 4,000 characters using only permitted HTML tags.

### Metadata signals (keyword pool structure)
1. **Audience gift triggers:** funny gift for nurses, gifts for women who have everything, hilarious gift for moms
2. **Pain point terms:** burnout, stress relief gifts, new mom survival, exhausted teacher
3. **Occasion terms:** birthday gift, secret santa, retirement gift, mother's day gift
4. **Competitor-proven terms** recorded in the Phase 0 evidence record

Never use trademarked terms, competitor author or series names, or any term associated with flagged publishers per the standing account-safety alert.

### Pricing
Paperback price inside the validated competitor band from Phase 0: category norm USD 7.99 to 14.99 or market equivalent. Print royalty model is 60 percent of list minus printing cost. The Phase 5 package states the computed royalty at the chosen price. Never price below the band to chase rank.

### A+ Content plan
Three modules via the UAPF cover and A+ system:
1. Promise banner in the book's voice.
2. Interior peek strip showing a quote page and one art-rich spread.
3. Gift-occasion module.

All A+ assets obey this restriction. The no-selling-points-on-cover rule does not apply to A+, but claims stay honest and unquantified.

---

## Key Rules — Do NOT Break

1. **Content restrictions, no exceptions.** No alcohol, pork, or gambling-positive content anywhere: text, quotes, attributions, lists, images, image prompts, covers, A+ content, or metadata. Comfort props are tea, coffee, and chocolate only.
2. **Anti-advice voice doctrine.** No programs, no five steps, no toxic positivity, no kitsch. Validate reality, then give permission to rest. The book never instructs the reader to do anything.
3. **One humor register per book, locked at Phase 1.** No tonal drift between chapters. The register check runs on every chapter gate.
4. **Joke-type diversity quotas.** Each chapter must contain at minimum one observational, one absurdist, one wordplay/misdirection, and one situational joke. No device repeats within a chapter.
5. **Humor punches at situations and systems, never at people or groups.** No stereotype harmful-reinforcement. Sensitivity Reader check before every chapter gate.
6. **Cultural-calibration for target marketplace.** Jokes are RE-CREATED for non-EN markets, never literally translated. Idioms, names, comfort props, and daily-life references must be authentic for the culture.
7. **No real private individuals.** No real person referenced, quoted, or illustrated. Fake attributions and pen names never match real public figures.
8. **Fake attribution format is exact and non-negotiable.** Name Initial., age, absurd chapter-related job title. No exceptions to this format.
9. **Quote-page job titles never repeat across the catalog within a language.** Log every title used.
10. **Trim 6 x 9 in, extent 80 to 120 pages hard cap.** No exceptions.
11. **Typography pair is locked.** Playfair Display for all serif display elements, Lato for body. Named styles only; no direct manual formatting ever.
12. **Interior is black and white only.** No color, no tints, no shaded panels. Cover is the only color surface.
13. **Image constraints clause is mandatory on every image prompt.** "black and white line art only, no text in image, no logos, no color, no real persons."
14. **Em dashes are banned catalogue-wide.** Use commas, parentheses, or a semicolon instead.
15. **Gate discipline is blocking.** The gate line "Type Proceed." ends every phase and every chapter. No gate is skipped or merged. No next unit begins until the operator replies Proceed.
16. **Rolling manuscript only.** One single growing DOCX per title. Separate chapter files are never delivered unless explicitly requested.
17. **Front matter order is locked.** Half-title > Copyright > Dedication > Preface > How to Use > TOC > Introduction. Folios start at the Introduction as printed page 1.
18. **No selling points on covers.** Title and subtitle only on the front. Pen name on the copyright page.
19. **Mascots must vary across the catalog.** No mascot repeats within the same segment and language.
20. **State discipline.** Never claim an external operation occurred unless it actually occurred. Use NOT RUN, PENDING, UNVERIFIED, or READY FOR IMPORT honestly.
21. **Uniqueness.** No two catalog titles share a title, a subtitle, or more than two consecutive words in a subtitle. No two covers look alike. Quote-page job titles never repeat within a language.
22. **Originality attestation.** Every book is written fresh for its slot. No text, structure, or art is derived from any existing work or competitor title. The reference class is a style source only.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
