---
name: uapf-niche-poetry
description: Poetry, affirmations, and spoken word niche overlay — invoked by uapf-phase0-router when the title contains poems, poetry collection, affirmations, daily affirmations, quotes collection, blessings, spoken word, or odes signals to apply originality protocols, emotional-arc sequencing, cliché audits, and cadence verification.
---

# UAPF Niche: Poetry, Affirmations & Spoken Word (OV-POET)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** title or stated format contains one or more of: poems, poetry, poetry collection, affirmations, daily affirmations, daily inspiration, morning affirmations, positive affirmations, quotes collection, blessings, spoken word, odes to, verses, verse collection, prose poetry, free verse, haiku collection, sonnets, lyric essays, meditations (literary context), mantras, personal affirmations, self-love affirmations, healing poems, grief poems, love poems, nature poems, women's poetry, empowerment poetry, inspirational quotes.

---

## Expert Panel

1. **Domain Master — Literary Poet and Craft Specialist**: Reviews every entry for craft quality — imagery, line breaks, cadence, emotional specificity, diction, and avoidance of cliché. Flags any piece that reads as AI-generated filler, recycled sentiment, or generic motivational language. This is a review lens; actual literary review must be separately engaged for high-visibility publications.
2. **Originality Auditor**: Performs a deep-scan comparison against the most common affirmation and poetry tropes, stock phrases, and recycled famous-quote paraphrases. Ensures no entry resemble known copyrighted poems or famous quotes presented as original work. Flags any piece for replacement if it fails the originality standard.
3. **Cadence and Read-Aloud Editor**: Reads a representative sample from every section aloud (simulation). Flags entries with awkward stress patterns, unintentional rhyme in free verse, missing line-break logic, or affirmations that are grammatically correct but rhythmically inert.
4. **Emotional Arc Architect**: Reviews the collection-level emotional journey. Confirms that sections are sequenced (not shuffled), that the emotional arc declared in Phase 0 is delivered, and that the collection does not peak emotionally in the wrong place or end on an unresolved note.
5. **Variety and Repetition Auditor** (Affirmation books specifically): Counts the variety of core themes, subjects, and sentence structures across all entries. For 365-entry collections, verifies that no core idea appears more than 6–8 times in substantively identical form. For smaller collections, flags any idea recycled more than 3 times without meaningful variation in approach, imagery, or framing.

---

## Phase 0 — Title Analysis

**Step 0-A: Sub-Genre Classification (determines architecture)**

Classify into one primary sub-genre:
- **Poetry Collection** (purely poetic entries; no day-numbering; organized by section/theme)
- **Daily Affirmations Book** (numbered day entries; one affirmation per day; may include reflection or prompt)
- **Quotes Collection / Wisdom Book** (curated or authored short prose aphorisms; no day-numbering required but possible)
- **Spoken Word / Performance Poetry** (composed for oral delivery; rhythm and sound are primary design parameters)
- **Prose Poetry / Lyric Essay Collection** (hybrid form; longer reflective pieces with poetic density)
- **Themed Blessing Collection** (blessings for specific occasions or relationships)
- **Odes Collection** (dedicated praise-poems for specific subjects)
- **Haiku / Formal Verse Collection** (fixed-form poetry; form rules are structural requirements)

Record as **Active Sub-Genre**. It controls the structural unit, entry format, and QA audits.

**Step 0-B: Emotional Arc Declaration (HARD REQUIREMENT)**

Before any content is generated, the collection's emotional arc must be declared and locked. An emotional arc is a purposeful progression, not a random sequence of moods. It must be stated at the section level.

Prompt if not self-evident from the title:
> "This project is routed to the Poetry & Affirmations overlay (OV-POET). To ensure a purposeful collection rather than a shuffled anthology, I need to confirm the emotional arc before generating content. Please describe the emotional journey you want readers to take from the first section to the last — for example: from grief to acceptance to renewal; from self-doubt to self-knowledge to self-trust; from isolation to connection to joy. If you do not have a specific arc in mind, I can propose three options based on the title."

Once declared, record as **Active Emotional Arc**. The arc is a structural commitment:
- The opening section must begin at the starting emotional register
- The middle sections must develop, deepen, or complicate that register
- The closing section must arrive at the stated destination
- Individual entries may deviate, but the section as a whole must serve the arc

**Step 0-C: Day-Count Extraction (for numbered collections)**

If the title contains a numeric count (e.g., "365 Daily Affirmations," "52 Weeks of Affirmations," "100 Poems"), extract and lock it. Record: **DECLARED ENTRY COUNT = [N]**. The book must contain exactly N complete, distinct entries. Partial entries, index entries, and filler do not count.

**Step 0-D: Form Declaration (for formal-verse collections)**

If the collection is in a fixed form (haiku, sonnet, villanelle, pantoum, ghazal, etc.), declare the form rules in Phase 0 and hold them throughout:
- Haiku: 5-7-5 syllable structure in English (note: some contemporary haiku traditions use looser syllable counts; clarify which convention the user prefers)
- Sonnet: 14 lines, declare rhyme scheme and meter (Shakespearean, Petrarchan, or contemporary unrhymed)
- Other fixed forms: state the rules explicitly before generating any entries

**Step 0-E: Copyright and Originality Mode Declaration**

Confirm: **ALL CONTENT GENERATED UNDER OV-POET IS ORIGINAL AND UNPUBLISHED.** No entry may:
- Paraphrase a well-known poem or quote while omitting the attribution
- Incorporate lines from copyrighted poems without explicit quotation formatting and rights confirmation
- Present as original any affirmation or aphorism that is in wide public circulation under another author's name
- Reproduce any copyrighted poem in an epigraph position without confirmed permission and attribution

Famous public-domain authors (Rumi, Shakespeare, Emily Dickinson, Walt Whitman, Langston Hughes — for works in public domain) may be quoted with attribution in epigraph positions. Modern poets (Pablo Neruda, Mary Oliver, Rupi Kaur, etc.) are copyright-protected — do not quote without permission regardless of how widely circulated their work is.

**Step 0-F: Auto-Configuration**

After sub-genre and arc declaration, auto-configure:
- **Reference style**: Chicago Notes and Bibliography (literary non-fiction default; for epigraph citations and any quoted sources)
- **Risk level**: R1 baseline. Elevate to R3 for collections explicitly centered on trauma, grief, abuse recovery, addiction, or self-harm themes (apply the R4 grief protocol's non-pressuring language rules)
- **Cliché prohibition**: activated (see Content Rules — the Cliché Audit)
- **Variety quota**: activated for collections of 30+ entries (see Content Rules)
- **Voice register**: determined by the Active Emotional Arc and target reader — lyric, confessional, celebratory, contemplative, etc.
- **Disclaimer**: minimal for literary poetry; required for collections making mental health or healing claims

Output a Phase 0 Summary confirming the Active Sub-Genre, Active Emotional Arc, entry count, form rules (if any), copyright mode, risk level, and voice register before proceeding to competitor research.

---

## Book Architecture

### Structural Unit by Sub-Genre

**Daily Affirmations (Primary Format)**

Each daily entry follows this sequence:
1. **Day number** (e.g., DAY 1 / Day 1 / 01 — consistent format throughout)
2. **Affirmation** (the core statement; 1–4 sentences; present tense; first-person singular; see Content Rules for craft requirements)
3. **Reflection** (optional for shorter collections; 50–150 words of supporting thought, context, or narrative — NOT a restatement of the affirmation in different words)
4. **Journaling or application prompt** (optional; 1–2 open questions; left-aligned; phrased as an invitation)

Minimum: Day number + Affirmation. Maximum recommended unit length: 300 words total (affirmation + reflection + prompt).

**Poetry Collection**

No fixed structural unit beyond each poem. Each poem is a complete unit. Organizational principle is sectional, not per-poem:
- 4–8 thematic sections
- Each section has a title that signals its place in the emotional arc
- Each section contains 8–20 poems (depending on total collection size)
- Section opener: title + optional epigraph (properly attributed) + no prose introduction (let the poems speak)
- Poems do not need individual epigraphs or author notes unless the collection style warrants it

**Spoken Word**

Each piece is a performance script:
- Title
- Optional performance note (e.g., "pace slows here," "pause," "voice rises") — formatted in italics or brackets
- The poem itself, with line breaks and stanza breaks as performance cues
- No day-numbering
- Organized by arc section

**Quotes / Wisdom Collection**

Each entry:
1. The aphorism (1–3 sentences)
2. Optional attribution line if derived from a historical source (clearly labeled)
3. Optional 2–3 sentence elaboration or context note

If the entire collection is original (not curated), every entry must pass the originality audit — no entry may resemble a well-known quote closely enough to invite confusion about authorship.

**Formal Verse (Haiku, Sonnet, etc.)**

Each entry is a complete poem in the declared form. Group by theme or emotional arc section. Include a brief front-matter note explaining the form chosen and any variant conventions used (especially relevant for haiku syllable-count approaches).

### Section Architecture

**Number of sections**: 4–8 sections for most collections.

**Section sequence must map to the Active Emotional Arc.** Example arcs and section maps:

*Arc: Grief → Acceptance → Renewal*
- Section 1: The Weight (grief, loss, darkness)
- Section 2: Sitting With It (acknowledgment, presence)
- Section 3: The Turning (first light, small shifts)
- Section 4: What Remains (integration, carrying forward)
- Section 5: Opening (new possibility, soft hope)

*Arc: Self-Doubt → Self-Knowledge → Self-Trust*
- Section 1: The Noise Inside (inner critic, comparison)
- Section 2: Looking Closer (self-examination, honesty)
- Section 3: What I Know (affirmation from evidence)
- Section 4: The Practice (building the habit of self-trust)
- Section 5: Enough (arrival, sufficiency)

Sections must not be interchangeable. Moving Section 3 content into Section 1 should feel emotionally wrong — that is the test of a real arc.

### Day-Count and Entry Variety Quotas

For collections of 30 or more entries, the Variety Quota applies:

| Collection Size | Maximum Repetitions of Any Single Core Idea |
|---|---|
| 30–60 entries | No more than 3 entries on substantially the same idea without meaningful variation in imagery, angle, or framing |
| 61–120 entries | No more than 5 entries on substantially the same idea |
| 121–200 entries | No more than 6 entries on substantially the same idea |
| 201–365 entries | No more than 8 entries on substantially the same idea |

**Core idea examples that are frequently over-recycled in affirmation books:**
- "You are enough"
- "You are worthy of love"
- "Trust the process"
- "You have survived everything so far"
- "Your worth is not your productivity"
- "Rest is not laziness"
- "Small steps count"

These ideas may appear in the collection — they are legitimate affirmation themes. They may NOT appear in substantially identical phrasing more than the quota allows. Each return to the theme must approach it from a different image, story, scene, angle, or emotional register.

### Page-Band Targets (6 × 9 trim, Times New Roman)

| Format | Entries / Poems | Estimated Page Band |
|---|---|---|
| 30-Day Affirmations (with reflection) | 30 | 60–100 pages |
| 90-Day Affirmations (with reflection) | 90 | 140–200 pages |
| 365-Day Affirmations | 365 | 280–400 pages |
| Poetry Collection (60–100 poems) | 60–100 | 100–180 pages |
| Spoken Word Collection | 20–50 pieces | 80–140 pages |
| Quotes / Wisdom (with elaboration) | 100–200 | 120–200 pages |
| Haiku Collection | 100–300 haiku | 60–120 pages |

Always verify against live Amazon competitor research. Above are defaults only.

### Front Matter Requirements

In this order:
1. Half-title page
2. Full title page
3. Copyright page (standard AIRF 2.0 requirements + AI-image disclosure if applicable + any epigraph permissions credits)
4. Disclaimer (if collection makes healing or mental health claims — see Content Rules)
5. Dedication (optional)
6. Preface (~1 formatted page): the emotional journey the reader is invited into; how to use the collection; a note on the arc
7. How to Use This Book (~1 formatted page): whether to read chronologically or dip in; suggestions for journaling alongside; how to sit with a poem that doesn't land immediately
8. Automatic Table of Contents (for section-organized collections)
9. Introduction (begins as page 1) — may be very short for poetry-first collections (1 page maximum before the poems begin)

### Back Matter Requirements

- Conclusion or Closing Note (~1 page): a final address to the reader; acknowledges the emotional journey taken; no new major insight introduced; closes the arc
- Acknowledgments (optional)
- About the Author: pseudonym only; no invented literary prizes, publication history, or MFA credentials
- **Index of First Lines** (for poetry collections; alphabetical; standard convention)
- Recommended Reading (5–10 titles; tradition-appropriate; real published books only — no invented titles)
- Resources (for grief, trauma, or mental health themed collections: current, verified, jurisdiction-appropriate crisis and therapy resources)

---

## Interior Design

**Trim size**: 6 × 9 inches, 0.7 inch margins (standard AIRF 2.0).

**Typography**:
- Body (poem text): Times New Roman, 12 pt, 1.5 line spacing (slightly more open than prose — breathes on the page)
- Affirmation statement (daily format): Times New Roman, 13 pt, italic, centered or left-aligned (decide once and hold throughout)
- Day number: Times New Roman, 11 pt, bold, all caps, left-aligned or centered (decide once and hold throughout)
- Section title pages: Times New Roman, 16 pt, bold, centered, with 2–3 lines of white space above and below
- Poem titles: Times New Roman, 12 pt, bold, centered or left-aligned (decide once and hold throughout; do not alternate)
- Epigraphs: Times New Roman, 11 pt, italic, centered, with attribution line in regular weight below
- Reflection text (affirmations format): Times New Roman, 12 pt, 1.15 spacing, left-aligned prose

**Visual identity**:
- Section opener images: one per section for books under 180 pages (AIRF 2.0 auto-rule). Abstract, painterly, or 2D illustration style preferred over photorealism for most poetry collections. Images should suggest emotional register, not illustrate literal content.
- Affirmation books: a small typographic ornament or rule between the affirmation and the reflection is appropriate and clean.
- Avoid decorative fonts for body text — legibility is a reading experience.
- White space is design: do not fill every page. A short poem on an otherwise white page is a design choice, not a failure to fill space.
- For spoken word: performance notes in brackets [pause] or italics — choose one convention and hold it.

**Word style map**:
- Heading 1: Section titles
- Heading 2: Poem titles (in section-organized collections) or Day headers (in numbered collections)
- Body Text: poem lines, affirmation text, reflection prose
- Caption: image captions
- Block Quote: epigraphs (attributed quotations)

---

## Content Rules

### Absolute Originality Standard

**This is the single most important content rule in OV-POET.** Every poem, affirmation, aphorism, and lyric produced under this overlay must be wholly original. The following are strictly prohibited:

1. **Paraphrasing famous quotes** without attribution and presenting the result as original writing (e.g., taking a Rumi quote, rephrasing it, and omitting the credit). This is a form of plagiarism.
2. **Recycling lines that are in wide public circulation** as affirmations (e.g., "you are enough," "she believed she could so she did," "nevertheless she persisted") — these may appear as acknowledged common phrases but may not form the core of an "original" piece without transformation.
3. **Generating poetry that closely resembles a known poet's style to the point of imitation** without transformation. Drawing stylistic influence is legitimate; producing a piece that reads as a thinly disguised Mary Oliver nature poem or a Rupi Kaur minimalist piece is not.
4. **Using copyrighted poems as epigraphs without confirmed permission**. Public-domain poets (Dickinson, Whitman, Blake, Keats, Rossetti, Hughes — for works in public domain) may be used with attribution. Post-1928 poets require permission. Do not assume any poem is public domain without verification.

The Originality Auditor runs a deep scan at Gate 3 and will return entries for replacement if they fail this standard. There is no waiver.

### Cliché Audit (The Anti-AI Poetic Law)

The following stock images and phrases are prohibited in original entries under OV-POET. They represent the fingerprint of algorithmically generated inspirational content:

**Prohibited stock imagery:**
- Shattered glass / broken pieces assembled into beauty
- Phoenix rising from ashes (without substantial transformation)
- Storm / rainbow as healing metaphor (without fresh specificity)
- Bloom where you are planted
- Rivers finding their way to the sea
- Seeds buried before flowers
- Darkness before dawn
- Unbreakable warrior / silent storm
- Moonlight as metaphor for hidden strength
- Chains breaking as self-liberation
- Wings / flight as generic freedom symbol
- Empty cups / filling your own cup

**Prohibited filler phrases:**
- "You are braver than you believe"
- "She wore her scars like armor"
- "In the end, it will all make sense"
- "The universe has a plan for you"
- "Your pain is your power"
- "Soft is not weak"
- "Wild and free"
- "Shine your light"
- "Bloom, darling"
- "You are magic"
- "Unashamedly yourself"
- "Unapologetically you"

These phrases and images may appear in the collection **only when transformed beyond recognition** — used in a surprising, inverted, or contextually specific way that generates a new meaning rather than confirming an expectation.

Every entry must introduce at least one specific, concrete image or observation that could not have been generated by a generic "inspirational poetry" template. Specificity is the test: a poem about grief that names a particular object, smell, or time of day is more original than one that names grief in the abstract.

### Present-Tense Craft Rules (Affirmations)

All affirmations must be:
- **Present tense**: "I am," "I have," "I trust," "I choose" — not "I will be" or "I am becoming" (future tense weakens the affirmation's performative function)
- **First-person singular**: "I" — not "you" unless the book explicitly uses second-person address as a design choice declared in Phase 0
- **Specific enough to be credible**: "I handle challenges with grace and resourcefulness" is more credible than "I am amazing in every way." Specificity makes the affirmation land.
- **Not grandiose to the point of unbelievability**: an affirmation the reader's inner critic immediately rejects as false does not work. Build from credible to aspirational, not from aspiration to delusion.
- **Grammatically clean**: no dangling comparatives, no vague pronoun references, no passive constructions unless intentional

### Repetition-with-Variation Discipline

For collections of 30+ entries, every return to a core theme must demonstrate visible variation in at least one of the following dimensions:
- **Imagery**: the specific objects, scenes, or sensory details used to convey the theme
- **Angle**: the emotional register (gentle vs. fierce; certain vs. questioning; quiet vs. declarative)
- **Structure**: sentence length, rhythm, internal repetition pattern, or form
- **Scale**: zoomed-in (a particular moment) vs. zoomed-out (the pattern across time)
- **Addressee**: the self as a whole vs. the self at a particular age vs. the self in a particular situation

Simply changing a few words while keeping the same image and emotional structure does not satisfy this rule.

### Cadence and Read-Aloud Standard

All entries — poems and affirmations alike — must pass the read-aloud test:
- When read aloud at a normal pace, the piece must feel intentional, not accidental
- Line breaks in poetry must fall where the voice would naturally pause, speed, or shift emphasis — not mid-phrase for visual effect with no sonic logic
- Affirmations must have natural spoken rhythm — no awkward verb-noun inversions, no syllable clusters that trip the tongue
- Free verse does not mean unrhythmed prose broken into lines arbitrarily. Each line break must do work: create emphasis, pause, syntactic ambiguity, or breath control
- The Cadence Auditor samples at least 10% of entries from each section and reads them aloud as part of the Gate 3 review

### Emotional Arc Delivery

At the collection level:
- Section 1 must begin at the starting register of the Active Emotional Arc — do not front-load resolution
- The middle sections must do the work of the arc — development, complication, deepening, or turning
- The final section must arrive at the declared endpoint of the arc — do not leave the reader stranded at the middle
- Individual poems may deviate from the section's emotional register (contrast is a valid poetic technique), but the section as a whole must serve the arc
- Epigraphs, section titles, and any prose introductions must reinforce, not contradict, the arc's direction at that point

### Mental Health and Healing Claim Rules

For collections marketed around healing, grief, trauma recovery, or mental health:
- Do not present poetry or affirmation practice as a substitute for therapy, medication, or professional mental health treatment
- Include a disclaimer in the front matter stating that the collection is for personal reflection and is not clinical treatment
- Include crisis resources in the back matter (verified live for jurisdiction and current contact details)
- Do not claim the collection will "heal" the reader — use language like "support," "accompany," "invite reflection," "offer words for what is hard to name"
- For grief collections specifically: do not imply a timeline for healing or suggest that continuing to grieve beyond a certain point reflects weakness or insufficient engagement with the book's content

### The Fatal Flaw to Avoid

**365 affirmations that are 12 ideas recycled.** A 365-entry collection that cycles through the same 12 core sentiments — "you are enough," "rest is okay," "you have survived hard things" — with only surface-level variation in phrasing is not a 365-entry collection. It is a 12-idea pamphlet inflated to book length. This is the most common and most damaging failure mode in AI-generated affirmation books. The Variety Auditor and the Originality Auditor exist to catch and prevent this failure before the book reaches Gate 4.

---

## QA Checklist

### Gate 1 — Originality and Copyright
- [ ] Active Emotional Arc declared and documented in Phase 0 Summary
- [ ] DECLARED ENTRY COUNT locked and confirmed
- [ ] All epigraphs: public-domain with attribution, or rights-cleared with documentation
- [ ] No paraphrased famous quotes presented as original writing
- [ ] No recycled widely-circulated affirmation phrases presented as original compositions
- [ ] No substantially imitative pieces resembling copyrighted poets' work without transformation

### Gate 2 — Structure and Arc Delivery
- [ ] Section structure maps to the Active Emotional Arc: opening section begins at starting register; final section arrives at declared destination
- [ ] DECLARED ENTRY COUNT verified: total distinct complete entries = exactly N
- [ ] Each section contains distinct work (Section 3 content could not be moved to Section 1 without emotional incoherence)
- [ ] No entry is a stub, placeholder, or filler
- [ ] Index of First Lines built (for poetry collections)
- [ ] Day numbers (if applicable) are sequential and complete with no gaps

### Gate 3 — Quality, Originality, and Cadence Audit
- [ ] Cliché audit passed: prohibited stock imagery and phrases not present, or present only in demonstrably transformed context
- [ ] Variety quota verified: no core theme appears more times than the quota allows in substantially identical form
- [ ] Present-tense rule verified for all affirmations
- [ ] Cadence audit: 10% sample from each section read aloud; no awkward stress patterns, no arbitrary line breaks, no rhythmically inert affirmations
- [ ] Specificity test: every section contains at least 3 entries that use concrete, particular images not interchangeable with generic inspirational content
- [ ] Mental health / healing disclaimer present if collection makes healing claims
- [ ] Crisis resources present and verified live if collection addresses grief, trauma, or mental health themes

### Gate 4 — Production and KDP Readiness
- [ ] Front matter in correct order (per Book Architecture)
- [ ] Back matter complete (Closing Note, Index of First Lines, About Author, Resources where applicable)
- [ ] Times New Roman throughout; poem body 12 pt 1.5 spacing; affirmation 13 pt italic; section titles 16 pt bold
- [ ] White space treated as intentional design (short poems not forced to fill pages)
- [ ] All images generated and inserted (auto-rule applies for books under 180 pages)
- [ ] Images use abstract or painterly style appropriate to the emotional register (not literal illustration of poem content)
- [ ] Every image has caption and alt text
- [ ] Automatic TOC populated and updateable (section-level entries for poetry collections)
- [ ] Page numbering begins with Introduction as page 1
- [ ] Uniqueness audit passed: this collection's arc, section structure, imagery, voice, and entry range are distinct from any previously generated poetry or affirmations book in this session
- [ ] Final DOCX renders cleanly with correct poem spacing, no broken stanzas across pages, no orphaned section titles

---

## KDP Positioning

**Primary Amazon category tree:**
- Books > Literature & Fiction > Poetry > [specific subcategory: Subjects & Themes / Inspirational / Women's Poetry]
- Books > Self-Help > Motivational > [for affirmations books heavily positioned as self-help]
- Books > Self-Help > Personal Transformation > [for healing-arc affirmations]
- Books > Religion & Spirituality > Spirituality > Personal Transformation (for spiritually framed blessings/affirmations)
- Books > Health, Fitness & Dieting > Mental Health > [for grief or healing poetry]

**Description leads with:**
- The emotional experience or journey the reader will have (not a structural description of what the book contains)
- The target reader's current situation or feeling state (who needs this collection right now)
- The arc or transformation offered (in benefit language, not guaranteed-outcome language)
- The format and size (so readers know what they're getting: "365 original daily affirmations" vs. "a collection of 80 poems")

**Metadata signals:**
- Day count for numbered affirmations ("365 daily affirmations," "daily affirmation book")
- Target reader identity (women, Black women, mothers, grief, anxiety, healing, etc.)
- Emotional theme (self-love, grief, healing, empowerment, body image, etc.)
- Format signals (poetry book, affirmation journal, daily reader, inspirational quotes)
- Gift occasion signals (birthday, Mother's Day, graduation, sympathy gift, Christmas gift)
- For spoken word: "spoken word poetry," "performance poetry," "slam poetry" as keywords if applicable

---

## Key Rules — Do NOT Break

1. **Emotional arc declaration is mandatory before any content is generated.** A shuffled anthology with no arc is not a publication-quality collection. The arc must be declared, documented, and delivered.
2. **A "365 Daily Affirmations" book contains exactly 365 complete, distinct affirmation entries.** The declared count is a hard contract with the reader. Partial entries and repeats do not count.
3. **Absolute originality standard is non-negotiable.** No paraphrased famous quotes presented as original. No widely-circulated affirmation phrases presented as new compositions. No substantially imitative work without transformation. The Originality Auditor's finding is final at Gate 3.
4. **The Cliché Audit is mandatory.** The prohibited stock imagery and phrase list represents the minimum standard. Entries that trigger the cliché list must be rewritten before the chapter is declared complete.
5. **Variety quotas apply to all collections of 30 or more entries.** Core ideas may not be recycled above the quota threshold. The Variety Auditor must report at Gate 3.
6. **Present tense is mandatory for all affirmations.** "I am" not "I will be." No exceptions.
7. **All affirmations must be written in the first-person singular** ("I") unless second-person address is declared as a design convention in Phase 0.
8. **The cadence audit must sample at least 10% of entries from each section**, read aloud. Rhythmically inert affirmations and arbitrary-break free verse must be returned for revision before the section is declared complete.
9. **No copyrighted poem or quote may appear as an epigraph without confirmed rights** and exact attribution. Public-domain sources are safe with attribution; post-1928 authors require verification.
10. **No crisis-adjacent collection (grief, trauma, mental health) is complete without:** (a) a front-matter disclaimer distinguishing the book from clinical treatment, and (b) current, verified crisis and professional support resources in the back matter.
11. **Images for poetry collections use abstract or painterly style**, not photorealistic or literal illustration. The image should suggest the emotional register of the section, not illustrate specific poem content.
12. **No invented publication history, literary awards, or MFA credentials for the pseudonymous author.** Name only.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
