---
name: uapf-niche-faith
description: Faith and devotional niche overlay — invoked by uapf-phase0-router when the title contains devotional, prayer, scripture, Bible study, faith-based, spiritual growth, or religion signals to apply tradition-anchored, copyright-safe, doctrinally accurate generation rules.
---

# UAPF Niche: Faith & Devotional (OV-FAITH)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

**Routed here when:** title or stated format contains one or more of: devotional, prayer journal, scripture study, Bible study, faith-based, Christian living, spiritual growth, church, God, Jesus, Islamic, Muslim, Buddhist, spiritual practice, religious, Lent, Advent, Ramadan, Torah, Quran, dharma, sacred text, contemplative, meditations (faith context), blessings (religious context), hymn study, sermon journal, novena, rosary, lectionary, daily reading (faith context).

---

## Expert Panel

1. **Domain Master — Tradition Scholar**: Licensed theologian, seminary-trained pastor, imam, rabbi, or comparable credentialed figure within the declared tradition. Reviews doctrinal accuracy, sacred-text selection, and tradition-specific terminology. This is a review lens; actual qualified review must be separately engaged before publication.
2. **Scripture Copyright Specialist**: Expert in public-domain vs. copyright-protected translation rights, quotation limits, attribution requirements, and fair-use thresholds for sacred texts. Ensures every quoted passage has the correct translation citation and falls within permissible limits.
3. **Interfaith Sensitivity Reviewer**: Cross-tradition competency lens. Confirms the book does not mischaracterize parallel traditions, avoids appropriation without attribution, and maintains respectful framing even when writing from a single-tradition perspective.
4. **Trauma-Informed Pastoral Care Advisor**: Applies R4 framing (grief, suffering, spiritual crisis content). Ensures no victim-blaming, no prosperity-gospel guarantees, and no suggestion that illness, loss, or hardship reflects inadequate faith.
5. **Publishing Rights and Permissions Auditor**: Verifies that every translation cited is either public-domain or accompanied by documented permission and exact credit as required by the publisher. Flags any modern translation used without attribution.

---

## Phase 0 — Title Analysis

**Step 0-A: Tradition Declaration (HARD REQUIREMENT — do not skip)**

Before any other analysis proceeds, identify and lock the faith tradition. A book cannot be generated until the tradition is explicit. If the title does not make the tradition unambiguous, output this prompt to the user:

> "This project is routed to the Faith & Devotional overlay (OV-FAITH). To generate a doctrinally accurate book, I need to confirm the faith tradition before proceeding. Please specify the tradition — for example: Christian (and denomination if relevant), Catholic, Eastern Orthodox, Jewish, Islamic, Buddhist, Hindu, Bahá'í, Unitarian Universalist, or Interfaith/non-denominational. The declared tradition will govern sacred-text selection, devotional structure, and doctrinal accuracy throughout."

Once the tradition is declared:
- Record it as the **Active Tradition** and hold it for the entire project.
- Do not drift into parallel traditions mid-manuscript without the user's explicit instruction.
- If the book is explicitly **interfaith**, record all traditions represented and apply the Interfaith Protocol (see Content Rules).

**Step 0-B: Title Clearance**

Perform the standard AIRF 2.0 trademark screen with these additional faith-specific searches:
- Search for existing devotional series using the same day-count and title structure (e.g., "90-Day Devotional for Women").
- Check major Christian, Islamic, and Jewish publishers (Zondervan, Thomas Nelson, Tyndale, Baker Books, NavPress, Loyola Press, ArtScroll, Dar Al-Islam) for series using the same or similar naming.
- Flag any title that closely mirrors an established devotional franchise without distinguishing language.

**Step 0-C: Day-Count Extraction**

If the title contains a numeric day, week, or session count (e.g., "30 Days," "52 Weeks," "90-Day"), extract the exact number and lock it. Record: **DECLARED UNIT COUNT = [N]**. This number is a hard contractual commitment — the book must contain exactly N complete devotional units. There is no rounding, no approximation, and no substitution of partial units.

**Step 0-D: Format and Sub-Genre Classification**

Classify into one primary sub-genre:
- **Daily Devotional** (numbered day entries, fixed structure per day)
- **Prayer Journal** (guided prompts + writing space, minimal narrative)
- **Scripture Study Guide** (passage-by-passage commentary, discussion questions)
- **Topical Devotional** (theme-organized, not day-numbered)
- **Liturgical Companion** (tied to the church or tradition calendar, e.g., Advent, Lent, Ramadan)
- **Contemplative/Meditative** (longer reflective passages, silence practices, centering prayer)
- **Theological Reflection** (longer-form exposition, fewer structured units)

The sub-genre sets the structural unit formula and chapter architecture below.

**Step 0-E: Auto-Configuration**

After tradition declaration and format classification, auto-configure:
- **Sacred text**: Identify the canonical scripture or sacred text for the declared tradition.
- **Default translation**: Select the public-domain default (see Scripture Copyright Protocol in Content Rules).
- **Reference style**: Chicago Notes and Bibliography (standard for religion and scripture-heavy texts per AIRF 2.0).
- **Risk level**: R1 baseline. Elevate to R4 when the book covers grief, loss, suffering, spiritual crisis, spiritual abuse recovery, or bereavement.
- **Voice register**: Warm, reverent, accessible — not clinical, not preachy, not academic (unless the sub-genre is theological reflection).
- **Disclaimer**: Faith-specific disclaimer required (see Content Rules).

Output a Phase 0 Summary to the user in English, confirming the Active Tradition, unit count, sub-genre, translation, reference style, risk level, and voice register before proceeding to competitor research.

---

## Book Architecture

### Structural Unit Formula (Daily Devotional — Primary Format)

Every single devotional unit follows this four-part sequence in this order:

1. **Scripture / Sacred-Text Reference** — One primary passage, cited with book, chapter, and verse (or equivalent for non-Christian traditions). Translation cited by full name and abbreviation at first appearance in the book, thereafter by abbreviation. Length: 1–4 verses for daily devotionals; up to 12 for weekly or study formats.
2. **Reflection** — 200–350 words of substantive, reader-centered prose. Connects the passage to the reader's lived experience. No platitudes. Must introduce at least one concrete spiritual insight not restated verbatim from the passage.
3. **Prayer / Contemplation** — 50–120 words. Written as a direct address to God / the Divine / the sacred (according to the tradition's conventions). First-person singular ("I" voice) unless the tradition convention is communal ("we"). No bullet points inside prayers.
4. **Application Prompt** — 1–3 short action or reflection questions or a single concrete challenge the reader can complete that day. Left-aligned. Phrased as invitations, not commands.

**Unit length target**: 450–600 words per complete unit (excluding the scripture quotation word count).

### Alternate Unit Formulas by Sub-Genre

- **Prayer Journal**: Passage citation → Brief reflection (100–150 words) → Guided writing prompt (3–5 open questions with blank lines or space indicators) → Closing blessing sentence.
- **Scripture Study Guide**: Passage header → Context note (historical/cultural, 100–150 words) → Verse-by-verse commentary (300–500 words) → Cross-references (2–4) → Discussion or journaling questions (3–5) → Application challenge.
- **Topical Devotional**: Theme title → Anchor passage → Thematic reflection (300–400 words) → Supporting passage (secondary reference) → Prayer → Action step.
- **Liturgical Companion**: Liturgical date or season label → Lectionary passage(s) → Reflection → Liturgical tradition note (rubric, rite, or practice) → Prayer → Communal or personal application.
- **Contemplative**: Scripture or sacred phrase → Lectio Divina or equivalent reading instruction → Extended silence or centering prompt → Reflection journal prompt → Closing prayer.

### Chapter / Section Architecture

**For day-numbered books**: Group devotional units into thematic sections (parts), not traditional chapters. Suggested groupings:
- 30-unit books: 3 parts of 10 units each, or 5 parts of 6 units each.
- 52-unit books: 4 parts of 13 units each (quarterly), or 6 themed parts.
- 90-unit books: 3 parts of 30 units each (monthly), or 9 parts of 10 units each.
- 365-unit books: 12 monthly parts, or 52 weekly themed parts with daily sub-entries.

**For non-numbered formats**: Traditional chapter structure. 8–14 chapters. Each chapter opens with a theme introduction (250–400 words) before the chapter's devotional units begin.

### Page-Band Targets (6 × 9 trim, Times New Roman)

| Format | Units | Estimated Page Band |
|---|---|---|
| 30-Day Devotional | 30 | 90–130 pages |
| 52-Week Devotional | 52 | 130–180 pages |
| 90-Day Devotional | 90 | 200–280 pages |
| 365-Day Devotional | 365 | 400–520 pages |
| Scripture Study Guide (8–12 ch.) | — | 160–240 pages |
| Prayer Journal | — | 120–180 pages (with writing space) |
| Topical Devotional (10–14 ch.) | — | 150–220 pages |

Always verify against live Amazon competitor research before finalizing the page target. The above ranges are defaults only.

### Front Matter Requirements

In this order:
1. Half-title page
2. Full title page (title, subtitle, Active Tradition marker if appropriate, pseudonymous author)
3. Copyright page (standard AIRF 2.0 requirements + translation credit line + AI-image disclosure if applicable)
4. **Faith-specific disclaimer** (see Content Rules)
5. Dedication (optional)
6. Preface (~1 formatted page): how the author came to write this book; who the reader is; how to use the devotional
7. How to Use This Book (~1 formatted page): daily rhythm instructions, how to handle missed days, journaling guidance
8. **Translation Acknowledgment page**: full credit for every translation used, including rights holder, permission statement if needed, and copyright line exactly as required by the licensor
9. Automatic Table of Contents
10. Introduction (begins as page 1)

### Back Matter Requirements

- Conclusion (~1.5 pages): integrates the spiritual journey of the book; offers encouragement; avoids introducing a new doctrine or method
- **Scripture Index**: alphabetical by book of the Bible (or equivalent) with day/unit numbers
- **Topical Index**: optional for books over 200 pages
- Further Reading and Resources: 8–15 titles, tradition-appropriate, no invented publications
- **Crisis and Pastoral Support Resources**: current, jurisdiction-appropriate contacts for spiritual crisis, grief support, and domestic violence (faith-based resources where available — verify URLs and phone numbers live before finalization)
- About the Author (pseudonym only; no invented credentials or ministry history)

---

## Interior Design

**Trim size**: 6 × 9 inches, 0.7 inch margins (standard AIRF 2.0).

**Typography**:
- Body: Times New Roman, 12 pt, 1.15 line spacing (standard devotional rhythm).
- Day/Unit header: Times New Roman, 14 pt, bold, centered, all caps (e.g., DAY 1 or WEEK 1).
- Unit sub-labels (Reflection, Prayer, Application): Times New Roman, 11 pt, bold, left-aligned, small caps formatting preferred.
- Scripture quotation: Times New Roman, 12 pt, italic, block-indented 0.5 inch left and right, with full citation on the final line, right-aligned within the block.
- Section/Part opener: Times New Roman, 16 pt, bold, centered; part title on its own page with a relevant epigraph or secondary scripture reference beneath.

**Visual identity**:
- Section dividers: use a simple ruled line or decorative cross, crescent, Star of David, dharma wheel, or tradition-appropriate symbol (not clipart — use a clean, print-safe vector or typographic symbol).
- Day/Unit number: can use a large numeral (20–24 pt) as a visual anchor at the top of each unit.
- Chapter or part opener images: one image per part opener, if the book is under 180 pages (auto-generate per AIRF 2.0 mandatory image rule). Faith imagery must be spiritually appropriate for the declared tradition, non-stereotyping, and never depicting actual scriptural figures in photorealistic form (illustration style preferred for sacred figures).
- Color: interior is black-and-white print-safe. No color-dependent meaning in layout.
- Writing space: for Prayer Journal sub-genre, include 6–10 blank or lightly ruled lines per prompt. Use Word's paragraph spacing to create this, not image placeholders.

**Word style map**:
- Heading 1: Part/Section titles
- Heading 2: Day/Unit header (DAY 1 / WEEK 1)
- Heading 3: Unit sub-labels (REFLECTION, PRAYER, APPLICATION)
- Body Text: main prose
- Block Text (custom style): scripture quotations

---

## Content Rules

### Scripture Copyright Protocol (CRITICAL — READ BEFORE WRITING A SINGLE VERSE)

**Public-domain translations (use freely, no permission required):**
- King James Version (KJV) — public domain in most jurisdictions
- World English Bible (WEB) — public domain
- American Standard Version (ASV, 1901) — public domain
- Darby Bible Translation — public domain
- Young's Literal Translation (YLT) — public domain
- Webster's Bible — public domain
- For Islamic tradition: Pickthall translation of the Quran — public domain in most jurisdictions (verify by jurisdiction)
- For Jewish tradition: JPS 1917 Tanakh — public domain

**Modern translations (require explicit permission and exact attribution — DO NOT USE without confirmed rights):**
- NIV (New International Version) — Biblica; 500-verse limit per project, exact copyright line required
- ESV (English Standard Version) — Crossway; 1,000-verse limit, exact copyright line required
- NASB (New American Standard Bible) — The Lockman Foundation; strict quotation limits
- NLT (New Living Translation) — Tyndale; limits apply
- The Message — NavPress; requires permission for substantial use
- CSB, NKJV, NRSV, CEB, NRSVue — all have specific rights holders and quotation limits
- Any translation published after 1928 — assume copyright protection until confirmed otherwise

**Protocol:**
1. Default to a public-domain translation for all quoted passages.
2. If the user requests a modern translation, flag the copyright requirement explicitly before writing any passages. State: "Using [Translation] requires permission and the following attribution line: [exact credit]. Quotation limits apply. Please confirm you hold or have secured the required rights before proceeding."
3. Never silently switch from a requested modern translation to a public-domain one — inform the user and get confirmation.
4. Place the full Translation Acknowledgment page in front matter (see Book Architecture).
5. For the Quran: note that Arabic-only quotations carry no copyright concern, but English translations do. Specify which English translation is being used and verify its status.
6. For Buddhist texts (Pali Canon, Mahayana sutras): many translations are modern and copyright-protected. Default to public-domain scholarly translations where available (e.g., the Pali Text Society translations in the public domain). Verify the specific text.

### Tradition Fidelity Rules

- **Doctrinal accuracy**: all claims about the declared tradition's beliefs, practices, history, and scripture must be accurate within that tradition's mainstream understanding. Do not conflate denominational positions without flagging the distinction (e.g., Catholic vs. Protestant interpretations of specific passages differ).
- **Denominational specificity**: when the user specifies a denomination (Baptist, Lutheran, Catholic, Methodist, Reformed, Pentecostal, etc.), apply that tradition's interpretive approach. Do not write from a generic Protestant perspective for a Catholic book or vice versa.
- **Interfaith respect**: if the book addresses readers of one tradition, do not disparage, caricature, or dismiss other traditions. Even when writing from a strongly confessional position, maintain respectful framing.
- **Interfaith books**: if the book explicitly serves multiple traditions, identify exactly which traditions are represented in Phase 0 and hold all of them with equal accuracy and respect. Never blend traditions without clearly signaling the interfaith frame.
- **Sacred-figure representation**: Do not depict Jesus, Muhammad, Moses, the Buddha, or other sacred figures in photorealistic imagery. Prefer abstract or symbolic visuals. When illustrative imagery of sacred figures is tradition-appropriate (e.g., Orthodox iconography style), use established iconographic conventions and flag the style choice explicitly.

### Theological Boundaries

- **No prosperity promises**: do not guarantee financial blessing, healing, promotion, answered prayer, or material outcomes as a result of faith practice or completing the devotional. Phrasing like "God will bless you with..." or "You will receive..." that implies contractual divine obligation is prohibited.
- **No healing guarantees**: do not suggest that prayer, devotion, or faith practice will cure illness, mental health conditions, or physical disability.
- **No spiritual victim-blaming**: do not imply that suffering, illness, loss, tragedy, addiction, or hardship is the result of insufficient faith, sin unaddressed, or failure to complete spiritual practices.
- **No coercive language**: exercises and prayers are invitations, not obligations. Language such as "you must pray daily or..." or "unless you surrender completely..." is prohibited.
- **No unsupervised clinical framing**: do not instruct readers to replace therapy, psychiatric medication, or medical treatment with prayer or devotional practice.

### R4 Grief and Suffering Protocol

When the book topic includes grief, bereavement, suffering, spiritual crisis, faith deconstruction, loss of a child, terminal illness, or recovery from spiritual abuse, apply these additional rules:

- Use trauma-informed, non-pressuring language throughout.
- Make every application prompt explicitly optional: "If you feel ready..."
- Include a grief-specific disclaimer in the front matter.
- Include current crisis and pastoral support resources in back matter (verify live).
- Avoid any implication that grief has a fixed timeline or that continued sadness reflects spiritual weakness.
- One chapter or section should explicitly address the normalcy of spiritual doubt or "dark night of the soul" experiences.
- Do not use before-and-after framing ("before I found faith I suffered / now I am healed").

### The Fatal Flaw to Avoid

**Generic devotionalism**: producing reflections so universally positive and theologically vague that they could apply to any tradition, require no knowledge of the scripture cited, and offer no concrete insight. A devotional that quotes a verse and then restates the verse in different words — without connecting it to the reader's daily life, without theological depth, without emotional honesty — fails the publication standard. Every unit must deliver a genuine spiritual insight or practical transformation move.

---

## QA Checklist

### Gate 1 — Tradition and Copyright Integrity
- [ ] Active Tradition declared and documented in Phase 0 Summary
- [ ] No doctrinal statement contradicts the declared tradition's mainstream position
- [ ] Every scripture passage carries its correct citation (book, chapter, verse, translation abbreviation)
- [ ] All modern translations confirmed as either public-domain or rights-cleared with exact attribution lines
- [ ] Translation Acknowledgment page present in front matter
- [ ] Quotation limits for any licensed translation have been checked and not exceeded
- [ ] No prosperity promises in any unit
- [ ] No healing guarantees in any unit
- [ ] No spiritual victim-blaming in any unit

### Gate 2 — Day-Count and Structural Completeness
- [ ] DECLARED UNIT COUNT verified: total complete units = exactly the number stated in the title
- [ ] Every unit contains all four required components (Scripture → Reflection → Prayer → Application)
- [ ] No unit is a stub, filler, or reprint of another unit
- [ ] Part/section groupings add up to the total unit count
- [ ] Scripture Index built and verified against all units
- [ ] Word-count targets met: each Reflection is 200–350 words; each Prayer is 50–120 words
- [ ] No two units use the same reflection angle or application prompt

### Gate 3 — Theological and Safety Review
- [ ] R4 grief protocol applied if topic requires it
- [ ] No coercive language in any unit, prayer, or prompt
- [ ] Professional-referral language present where grief, spiritual crisis, or mental health is mentioned
- [ ] Crisis and pastoral support resources verified live for correct contact details and regional suitability
- [ ] No advice to replace medical or psychological professional care with spiritual practice
- [ ] Interfaith passages (if any) reviewed for accuracy and respect toward all traditions represented
- [ ] No photorealistic depictions of sacred figures in imagery

### Gate 4 — Production and KDP Readiness
- [ ] Front matter in correct order (per Book Architecture)
- [ ] Back matter complete (Conclusion, Scripture Index, Further Reading, Crisis Resources)
- [ ] Times New Roman throughout, 12 pt body, 1.15 spacing
- [ ] Scripture quotations properly block-indented and italicized with citation
- [ ] All images generated and inserted (auto-rule applies for books under 180 pages)
- [ ] Every image has caption and alt text
- [ ] Automatic TOC populated and updateable
- [ ] Page numbering begins with Introduction as page 1
- [ ] Uniqueness audit passed: this book's unit sequence, reflection angles, and prayer approaches are distinct from any previously generated devotional in this session
- [ ] Final DOCX renders cleanly with no clipped tables, broken headings, or orphaned unit labels

---

## KDP Positioning

**Primary Amazon category tree (Christian — most common routing):**
- Books > Religion & Spirituality > Christian Books & Bibles > Christian Living > Devotionals
- Books > Religion & Spirituality > Christian Books & Bibles > Bible Study & Reference > Bible Study Guides

**For Islamic titles:**
- Books > Religion & Spirituality > Islam > Quran

**For Jewish titles:**
- Books > Religion & Spirituality > Judaism > Holidays & Prayerbooks

**For Buddhist titles:**
- Books > Religion & Spirituality > Buddhism > Zen

**For Interfaith / Spiritual Practice (non-denominational):**
- Books > Religion & Spirituality > Spirituality > Personal Transformation
- Books > Self-Help > Spiritual > Personal Transformation

**Description leads with:**
- The reader problem or season of life the book addresses (not a summary of what the author wrote)
- The specific tradition and format (so readers self-select accurately)
- The day/unit count and the daily time commitment
- One concrete spiritual benefit or transformation the reader can expect (no guaranteed outcomes)

**Metadata signals:**
- Keywords must include the tradition name, day count, target reader, and season/occasion if applicable (Advent, Lent, Ramadan, etc.)
- "Devotional" or "devotions" as a keyword for Christian titles significantly improves category rank
- For gift-book positioning: note gift occasions (Christmas, Easter, baptism, confirmation, Ramadan, Bar Mitzvah, etc.) in the description
- Subtitle should contain the tradition, reader identity, and a transformation phrase

---

## Key Rules — Do NOT Break

1. **Tradition declaration is mandatory before any generation begins.** No tradition = no output. Return the tradition prompt and wait.
2. **A "90-Day Devotional" contains exactly 90 complete units.** The declared number in the title is a hard contract with the reader. Partial units, index entries, and bonus content do not count toward the total.
3. **Every devotional unit must have all four components in order**: Scripture → Reflection → Prayer → Application. Omitting or reordering any component violates the structural unit standard.
4. **Default to public-domain scripture translations.** Never quote a modern translation without flagging the copyright requirement and getting user confirmation of rights.
5. **Every modern translation quotation must carry the exact attribution line required by the rights holder**, placed in the Translation Acknowledgment page and in the copyright page.
6. **No prosperity promises, no healing guarantees, no spiritual victim-blaming.** These are absolute prohibitions with no exception for any tradition or format.
7. **Doctrinal accuracy is non-negotiable.** A reflection that misrepresents what the declared tradition believes about a scripture passage is a factual error, not a stylistic choice.
8. **No photorealistic depictions of sacred figures** (Jesus, Muhammad, the Buddha, Moses, Mary, etc.). Use symbolic, abstract, or iconographic-style imagery only.
9. **R4 grief protocol applies automatically** when the book covers bereavement, suffering, spiritual crisis, or faith deconstruction. Do not wait for the user to request it.
10. **Crisis and pastoral support resources must be verified live** for current contact information and regional suitability. Never carry over static resource lists from other projects.
11. **Interfaith respect is absolute.** No tradition covered in this book may be disparaged, caricatured, or presented as inferior — even when writing from a strongly confessional position.
12. **No invented credentials, ministry history, church affiliations, or publications for the pseudonymous author.** Name only.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
