---
name: uapf-niche-user-guide
description: Product user guides, software manuals, and device handbooks — invoked by uapf-phase0-router when the title signals documentation for a specific product, software platform, device, or application rather than a general skill or craft project book.
---

# UAPF Niche: User Guides, Manuals & Product Handbooks (OV-GUIDE)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> **Framework integration:** the machine-executable projection of this niche's framework lives in `frameworks/AIRF-2.0-User-Guide-Edition/` (config, validation, phases, and deterministic ops in `genie_user_guide.py`). This SKILL.md remains the authoritative source; that folder never overrides it. At Phase 0 stamp `framework=AIRF 2.0 User Guide Edition` into the `book_lock.md` classification line (global rule #16).

**Routed here when:** The title contains any of the following product-documentation signals — "user guide", "user manual", "manual", "handbook for [product/platform]", "mastering [named software or platform]", "complete [software/device] guide", "getting started with [named product]", "[product] for beginners", "[product] reference guide", "[product] companion", "the unofficial guide to [product]", "[software] keyboard shortcuts", "[device] setup guide", "operating manual for [device]", or any title where the primary subject is a named, version-specific product, software application, device, or platform that the reader must operate.

**NOT routed here when:**
- The title is a general skill-building book that references tools generically (route to OV-HOWTO).
- The title is a numbered project collection using craft equipment (route to OV-CRAFT).
- The product referenced is a creative medium (e.g., "How to Use a Camera" as a photography skill guide — route to OV-HOWTO; "Canon EOS R5 User Guide" — route here, OV-GUIDE).

**Version Sensitivity:** OV-GUIDE is the most version-sensitive niche in the UAPF system. Every OV-GUIDE book must name the product version it covers on the cover, in the Introduction, and in KDP metadata. Outdated version information is the single most common 1-star complaint in this niche.

---

## Expert Panel

1. **Technical Communication & Documentation Authority** (Domain Master) — 18+ years in technical writing, product documentation, and usability-driven manual development. Certified Professional Technical Communicator (CPTC). ISO/IEC 82079-1 working expertise. ANSI Z535.6 safety messaging compliance. Society for Technical Communication (STC) recognition. Governs all structural decisions, information architecture, warning hierarchy placement, terminology parity, and documentation standards compliance. Must sign off on every chapter's terminology parity check and warning placement before Gate 3 clears.

2. **Instructional Design & Skills Transfer Authority** — 20+ years instructional design and vocational curriculum development (CPTD/ATD). Ensures task-oriented architecture is maintained (chapters organized by what users do, not by what features exist), validates that procedures are executable as written, and confirms that the Getting Started / Setup chapter enables first-use success within one session.

3. **UI/UX & Product Analysis Specialist** — Expert in user interface design, user experience research, and product architecture analysis. Validates that book navigation mirrors product navigation (menu paths, screen flows, button labels), confirms that all UI element names match the product exactly, and audits that screen reference descriptions are accurate for the covered version.

4. **Safety & Compliance Reviewer** — Confirms that all DANGER / WARNING / CAUTION / NOTICE hierarchy placements comply with ANSI Z535.6, that all safety messages meet ISO/IEC 82079-1 requirements, and that product-specific regulatory notices (FCC, CE, RoHS, electrical safety standards) are accurately represented. Role is filled by the Technical Communication Authority in most cases, with external regulatory specialist consultation for medical devices, electrical appliances, or children's products.

5. **Localization & Accessibility Authority** (consulting role) — Advises on translation-readiness of writing (controlled English, short sentences, active voice, no idioms), accessibility standards (screen reader compatibility for digital editions, sufficient contrast for print), and multi-market compliance (US vs. EU regulatory language differences). Consulted at Gate 3 for any title intended for non-US or multilingual markets.

**Panel Consensus Rule:** The Technical Communication Authority and the UI/UX Specialist must jointly confirm terminology parity — that every UI element name, menu label, button name, and screen title in the book matches the product exactly as it appears in the covered version — before Gate 3 can clear.

---

## Phase 0 — Title Analysis

Execute all steps in sequence before generating any content.

### Step 0-A: Trademark Clearance (MANDATORY FIRST ACTION)

**OV-GUIDE trademark analysis is uniquely complex** because the book's title almost always references a trademarked product name. The framing must comply with nominative fair use doctrine without creating false affiliation.

**Approved framing patterns for product-name titles:**
- "The Complete Guide to [Product Name]" — acceptable as nominative reference.
- "[Product Name] for Beginners" — acceptable.
- "Mastering [Product Name]" — acceptable.
- "The Unofficial [Product Name] Handbook" — acceptable; "unofficial" signals no affiliation.
- "[Product Name] User Guide: [Version]" — acceptable.

**Prohibited framing:**
- Titles that imply official authorization or affiliation that does not exist ("The Official [Product] Guide" when not officially licensed).
- Titles using a registered mark as a possessive brand attribute without fair use justification.
- Titles combining a product name with a publisher name in a way that implies partnership.

Extract every distinctive word and brand name. Run registry clearance:
Registry coverage: USPTO (US) Class 16 + Class 9, EUIPO (EU), UKIPO (UK), CIPO (Canada), IP Australia, JPO (Japan).

**Verdicts:**
- CLEAR: Title framing is acceptable nominative fair use; proceed to Step 0-B.
- CAUTION: Reframing recommended (e.g., add "unofficial," remove "official," adjust subtitle); present 3-5 alternatives; require operator approval.
- BLOCKED: Title implies official licensing or contains a mark in a way that is not defensible as nominative use; must change. Present 3-5 alternatives. Halt until resolved.

**Output:** Trademark Clearance Report with specific framing analysis for the product name. Note: "This book must not claim or imply official authorization, partnership, or endorsement by [Company Name] unless a formal licensing agreement exists."

### Step 0-B: Product & Version Identification

**This is the most critical step in OV-GUIDE Phase 0.** The covered version must be identified and recorded before any content is written.

Extract from the title:
- **Product Name:** The specific software, device, or platform.
- **Version / Model Number:** If stated in the title (e.g., "Windows 11," "iPhone 15 Pro," "Photoshop 2025," "Excel 365").
- **Version Confirmation Requirement:** If the title does not specify a version, state in the configuration report: "Version not named in title. Operator must specify the exact version this book covers before the TOC gate. Version will appear on the cover, in the Introduction, and in KDP metadata."

**Version Discipline Rules (non-negotiable):**
1. The covered version is stated on the title page in parentheses: e.g., "(Covers [Product] Version [X.X])".
2. The Introduction's first paragraph names the covered version and states the knowledge cutoff date used for accuracy.
3. The Copyright Page includes a version declaration: "This book covers [Product] Version [X.X] / [Year] release as of [Month Year]. Features described may differ in later versions."
4. KDP metadata keywords include the version number.
5. The book description on KDP names the covered version prominently.

### Step 0-C: Product Architecture Analysis

Before writing a single word of content, map the product's architecture:

**For software/platform:**
- Primary navigation structure (menu bar, ribbon, sidebar, command palette).
- Core feature categories and their official names.
- Settings and preferences architecture.
- Account/subscription requirements for featured functions.
- Known version differences between the covered version and the immediately prior version (note as callouts where the reader may encounter differences).

**For hardware/devices:**
- Physical component nomenclature (official names from the manufacturer's own documentation).
- Control interfaces (buttons, ports, screens, dials) with official labels.
- Setup/pairing/power requirements.
- Safety certifications and regulatory notices required on the product.
- Maintenance and service access points.

**Output:** A Product Architecture Map (system layer, not published in the book) that serves as the terminology master list for the Terminology Parity Check.

### Step 0-D: Task Analysis & Chapter Scope

OV-GUIDE books are **task-oriented**: organized by what users do, not by what features exist. A feature-organized manual ("Chapter 3: The Format Menu") is a documentation anti-pattern that this framework explicitly prohibits.

From the product architecture, identify the **primary user tasks** in order of frequency and importance:

1. **First-time setup tasks** — These become the Getting Started chapter (Chapter 1 or 2).
2. **Daily / core workflow tasks** — These become the main content chapters.
3. **Configuration and customization tasks** — These become the settings/personalization chapters.
4. **Maintenance and update tasks** — These become the maintenance chapter.
5. **Troubleshooting tasks** — These become the troubleshooting chapter and/or appendix.

Record: "The primary user task set for [Product] covers [N] task categories that will map to [N] chapters."

### Step 0-E: Audience Definition

- **Declared audience:** Complete beginner (never used product before) / Intermediate (used it but not confidently) / Power user (seeking advanced features) / All-levels.
- **Prior knowledge assumed:** For software books — computer literacy assumed, specific prior software experience (e.g., "no prior [Product] experience required, basic familiarity with [OS] assumed").
- **Use context:** Personal use / Professional use / Business deployment / Educational setting.
- **Age/accessibility signal:** Standard adult (11pt, 1.15 spacing) / Senior (13pt, 1.5 spacing) / Large-print edition.

### Step 0-F: Competitor Analysis

Execute web search:
- "[Product Name] [Version] guide book" + [marketplace]
- "[Product Name] user manual book" + "Amazon"
- "[Product Name] beginner book" + [marketplace]

**Report:** Top 5 competing titles. Key finding: what version are competitors covering? If competitors are already outdated, this book's version currency is its primary differentiator.

### Step 0-G: Subtitle Generation

Generate 7 subtitle candidates. Every candidate passes the Step 0-A trademark screen. Every candidate must reference the version where space allows.

1. A Step-by-Step Guide for [Audience] — [Version]-Updated
2. The Complete [Audience] Handbook: Setup, Features & Troubleshooting for [Version]
3. From Setup to Mastery: Everything [Audience] Needs for [Product] [Version]
4. [N] Step-by-Step Tutorials for [Audience] Using [Product] [Version]
5. The Unofficial Complete Guide: [Product] [Version] Fully Explained for [Audience]
6. Setup, Workflow & Troubleshooting: The [Audience] Guide to [Product] [Version]
7. [Product] [Version] Explained: Practical Instructions, Screenshots & Real-World Workflows for [Audience]

Recommend best subtitle with strategic justification and KDP keyword capture analysis.

### Step 0-H: Auto-Configuration

Auto-select and announce all parameters.

| Parameter | Selection Logic |
|---|---|
| Content Pathway | Hybrid (web research + knowledge base) for all OV-GUIDE titles; operator may supply screenshots or official documentation as reference material |
| Page Band | 80–150 pp (compact: focused single-product beginner guide); 180–250 pp (standard: comprehensive all-features coverage); 280–350 pp (extended: expert-level with all features + workflows + troubleshooting) |
| Visual Density | Heavy Visual (80–150+ images) — software/platform books require annotated screenshots for every procedure; hardware books require labeled photographs of all physical components |
| Body Font Size | 11pt (standard); 13pt (seniors/large-print signal) |
| Line Spacing | 1.15 (standard); 1.5 (senior/large-print) |
| Screenshot Convention | Annotated screenshots with numbered callouts and reference table below each screenshot |
| Design Signature | Composed from six dimensions per UAPF Module 4.6; announced in configuration; operator logs to register |

**Configuration Gate:** Present configuration including the confirmed covered version, the task-organized chapter structure, and version disclaimer language, ending with: "Shall I proceed with the Table of Contents? Type Proceed to continue."

---

## Book Architecture

### Structural Principle: Task-Oriented Architecture

**OV-GUIDE books are organized by what users need to do, in the order they typically need to do it.** The product's menu structure is a reference framework for the author, not the organizing principle of the book. Every chapter title names a user task, not a product feature.

**Anti-pattern (prohibited):** "Chapter 4: The Insert Menu"
**Correct pattern:** "Chapter 4: Adding Images, Tables, and Charts to Your Documents"

### Chapter Formula

**Standard OV-GUIDE Chapter Structure:**

```
CHAPTER [NUMBER]: [USER TASK IN BLOCK CAPS]
[What you will be able to do after this chapter — one sentence]
[Chapter context — 75–100 words. No AI-pattern openers.]

[SUBCHAPTER 1: Before You Begin]
[Prerequisites for this task: what must already be set up or completed]
[Version Note callout if the covered version differs from the prior version for this task]

[PROCEDURE BLOCK(S)]
[See Procedure Architecture below]

[SUBCHAPTER N: Common Issues With This Task]
[2–4 common failure patterns with causes and corrections]

[CHAPTER CHECKPOINT]
[3–5 bullets: what the reader can now do]
```

### Procedure Architecture

Every task is delivered as a numbered procedure. One action per step. No compound instructions.

```
[PROCEDURE TITLE]
─────────────────────────────────────────────────────────
Covered Version: [Product] [Version X.X]
Task Time: [Estimated time for typical user]
What you need before starting:
  • [Prerequisite 1]
  • [Prerequisite 2]
  [SAFETY / CAUTION callout if applicable]
─────────────────────────────────────────────────────────

Step 1. [Action verb] [exact interface element name in bold] [precise instruction].
        [SCREENSHOT or SCREENSHOT IMAGE PROMPT — annotated with callout numbers]
        [VERSION NOTE callout if this step differs between versions]

Step 2. [Action verb] [exact interface element name in bold].
        [SCREENSHOT or prompt]

[...continue through final step]

Expected Result: [Concrete description of the correct outcome — what the reader sees on screen or
                 what the device does.]

If your result does not match: [First most-likely cause and correction.]
```

**Interface Element Naming Convention:** Every UI element referenced in a step — button name, menu item, tab label, field name, keyboard shortcut, icon name — appears in **bold** and must match the product exactly as it appears in the covered version. This is the Terminology Parity requirement.

### Screenshot and Diagram Requirements

**For software/platform books:**
- Every procedure requires at minimum one annotated screenshot showing the key interface state.
- Screenshots are annotated with numbered callouts. A numbered callout table follows each screenshot identifying each callout.
- Screenshots are framed at the minimum crop that shows the relevant UI context (not full-screen unless full-screen context is required).
- Caption format: "Figure [Chapter.N]: [What this screenshot shows — active product version state]."
- If AI cannot generate screenshots: output a [SCREENSHOT DESCRIPTION] block: `[SCREENSHOT: [Product name] [version] showing [specific UI state] with callout at [element name] in [position]. Aspect ratio: 16:9. Annotation: Callout 1 = [element], Callout 2 = [element].]`

**For hardware/device books:**
- Every physical component referenced in a procedure requires a labeled diagram or photograph.
- Exploded-view diagrams for assembly/disassembly procedures.
- Control-panel overview diagram at the start of the Setup chapter, with all controls labeled using the product's official nomenclature.
- Caption format: "Figure [Chapter.N]: [Component name and function]."

### Warning Hierarchy (ANSI Z535.6 / ISO/IEC 82079-1 Compliant)

All safety and advisory messages in OV-GUIDE books use the following hierarchy. No other warning format is permitted.

```
┌─ DANGER ───────────────────────────────────────────────────────┐
│ Indicates a hazardous situation that, if not avoided, WILL     │
│ result in death or serious injury. Use only for physical       │
│ hazards on hardware/device titles.                             │
└────────────────────────────────────────────────────────────────┘

┌─ WARNING ──────────────────────────────────────────────────────┐
│ Indicates a hazardous situation that, if not avoided, COULD    │
│ result in death or serious injury, OR serious data loss /      │
│ system damage for software contexts.                           │
└────────────────────────────────────────────────────────────────┘

┌─ CAUTION ──────────────────────────────────────────────────────┐
│ Indicates a potentially hazardous situation that, if not       │
│ avoided, may result in minor injury, data loss, or system      │
│ settings changes that are difficult to reverse.                │
└────────────────────────────────────────────────────────────────┘

┌─ NOTICE ───────────────────────────────────────────────────────┐
│ Indicates important information — not safety-related — that    │
│ the user must know to avoid minor inconvenience, errors,       │
│ subscription changes, or feature limitations.                  │
└────────────────────────────────────────────────────────────────┘

┌─ VERSION NOTE ─────────────────────────────────────────────────┐
│ Indicates a step or feature that differs from the prior        │
│ version of the product. Readers using [prior version]          │
│ should [alternative instruction].                              │
└────────────────────────────────────────────────────────────────┘
```

DANGER and WARNING boxes use red-tinted borders. CAUTION uses amber. NOTICE uses blue or primary accent. VERSION NOTE uses secondary accent.

**Placement rule:** Every warning appears at the step where the risk occurs, not only in front matter.

### Page-Band Targets

| Book Size | Chapter Count | Target Pages | Coverage Scope |
|---|---|---|---|
| Compact | 6–10 chapters | 80–150 pages | Core tasks only; ideal for single-use-case guides |
| Standard | 11–18 chapters | 180–250 pages | All primary and secondary tasks; full feature coverage |
| Extended | 19–28 chapters | 280–350 pages | All tasks + advanced workflows + troubleshooting depth |

**Standard OV-GUIDE Chapter Sequence:**
1. Getting Started (setup, account creation, first-launch walkthrough)
2. [Product] Overview (interface tour, navigation map, key terminology)
3–[N]: Core task chapters (organized by user workflow, most-used tasks first)
[N+1]: Settings & Customization
[N+2]: Maintenance & Updates
[N+3]: Troubleshooting & Problem Solving

### Front Matter (Mandatory Order)

1. **Title Page** — Title, subtitle, "(Covers [Product] Version [X.X])", author name (First Name, Middle Initial. Surname), imprint line.
2. **Copyright Page** — Copyright line + year + author; all-rights-reserved; reproduction prohibition; version disclaimer ("This book covers [Product] Version [X.X] as of [Month Year]. The author and publisher are not affiliated with [Company Name]. Features described may differ in future versions."); trademark acknowledgment ("[Product Name] is a registered trademark of [Company Name]. Use in this book is for nominative reference only."); disclaimer and liability notice; edition statement; imprint.
3. **Table of Contents** — Live Word field. Lists all chapters and major subchapters with page numbers. Figures list optional for extended titles.
4. **Preface** — Exactly one page. Who this book is for, what version it covers, and the author's approach to task-oriented documentation. Voice Persona register.
5. **How to Use This Book** — Exactly one page. Explains: how procedures are structured (numbered steps, bold UI element names, annotated screenshots/diagrams), the warning hierarchy (DANGER/WARNING/CAUTION/NOTICE/VERSION NOTE), how to find specific tasks (TOC + Index), and the Troubleshooting appendix.
6. **Introduction** — Page 1 (visible pagination starts here). Product overview and context, who this book is for (prerequisites), what version is covered and why that matters, system requirements or compatibility notes, and a "Before You Begin" checklist.

### Back Matter (Mandatory)

- **Conclusion** — 1.5 pages. Summary of capabilities the reader has built. Guidance on staying current (product update channels, official release notes sources). Community resources.
- **Appendix** — Must include: Quick Reference Card (all most-used shortcuts and commands on one page); Keyboard Shortcuts Reference (complete, version-specific); Troubleshooting Index (symptom → cause → solution → relevant chapter page); Glossary of Terms (all product-specific and technical terms defined using the product's own official language); Interface Element Naming Index (alphabetical list of all UI elements referenced in the book with their official names and chapter page references); Version History Note (brief summary of what changed between the covered version and the prior major version); Resource Directory (official product documentation URLs, support channels, community forums — not third-party alternatives).

---

## Interior Design

**Trim Size:** 8.5 × 11 inches. All margins: 0.7 inches. Gutter increase only above 500 pages.

**Font:** Times New Roman throughout all narrative and instructional text.

**Body Text:** 11pt (standard); 13pt (seniors/large-print signal). Justified.

**Line Spacing:** 1.15 (standard); 1.5 (senior/large-print).

**Chapter Headings:** 16pt, BLOCK CAPITAL LETTERS, center aligned, primary accent color.

**Subchapter Headings:** Title Case, left aligned, bold, secondary accent color.

**Procedure Title:** 13pt, Title Case, bold, left aligned, primary accent color rule below.

**Step Numbers:** Bold. Steps left aligned. One action per step.

**UI Element Names (in-text):** Bold. Must match product interface exactly. Never paraphrased.

**Keyboard Shortcuts:** Monospace font (Courier New 10pt) or bold bracketed notation: [Ctrl+S], [Cmd+Z].

**Warning Boxes:** ANSI Z535.6 hierarchy (see above). Color-coded borders per severity level. Text in bold for DANGER and WARNING.

**VERSION NOTE Boxes:** Secondary accent border, distinct from warning hierarchy. Standard design across all OV-GUIDE titles.

**NOTICE Boxes:** Primary accent left bar, light fill, 10pt text.

**Screenshot Frames:** Thin border (0.5pt) in secondary accent color. Caption directly below in 9pt italic. Callout numbers in primary accent circles.

**Figure Caption Format:** "Figure [Chapter].[N]: [Description of UI state or hardware component]."

**Annotated Callout Tables** (below screenshots): Two-column table (Callout Number | Element Name and Function). Secondary accent color header.

**Step Images / Screenshots:** Placed immediately below the step text they support. No decorative illustrations. All screenshots or hardware photographs are photorealistic and current to the covered version.

**Design Signature:** Six dimensions (palette family, callout treatment, chapter opening ornament, title page composition, callout naming set, voice persona). Announced in configuration. Logged to register. No repeat. OV-GUIDE voice personas tend toward precise, professional, and efficiency-oriented — avoid the warmly conversational personas appropriate for craft or how-to titles unless the audience signal clearly warrants it.

---

## Content Rules

### The Fatal Flaw to Avoid

**Terminology mismatch and version drift.** If the book calls a button "Save File" and the product calls it "Save As," the book is wrong and readers know it immediately. If the book describes a workflow from Version 2024 and the reader has Version 2025, every screenshot reference is wrong. These are the two root causes of the most damaging reviews in the user-guide niche. Both are completely preventable.

### Hard Constraints

1. **The covered product version must be named on the cover, in the Introduction's first paragraph, and in KDP metadata.** No version ambiguity is permitted anywhere in the book.

2. **Terminology parity is absolute.** Every UI element name, menu label, button text, tab name, field name, dialog box title, and keyboard shortcut in the book must match the product's actual interface in the covered version exactly as it appears on screen. No paraphrasing, no synonym substitution, no simplification of official labels.

3. **Task-oriented chapter organization is mandatory.** Chapters are organized by what users do, not by what features exist. The product's menu tree may inform chapter scope but must never determine chapter sequence or title.

4. **Procedures follow the one-action-per-step rule without exception.** No compound steps. Every step begins with an action verb.

5. **All UI element names in steps appear in bold.** This is the visual convention that distinguishes between the author's instruction and the product's label, and it is the primary mechanism by which readers navigate from book to screen.

6. **Warning hierarchy (DANGER/WARNING/CAUTION/NOTICE/VERSION NOTE) is the only permissible advisory message format.** No other callout styles (Tip, Note, Info without the hierarchy label) may be used for safety-related or operationally important messages. Informational tips that carry no risk use the NOTICE box.

7. **Version Notes are mandatory at any step where the procedure differs between the covered version and the prior major version.** This prevents readers who downloaded the app slightly before reading the book from following wrong steps silently.

8. **Disclaimer on Copyright Page is non-negotiable.** Must state: (a) covered version and date, (b) no affiliation with the product company, (c) features may differ in future versions, (d) trademark acknowledgment.

9. **Screenshots and diagrams must be current to the covered version.** A screenshot from a prior version that shows a different UI state is misinformation. If screenshots cannot be generated or verified, the [SCREENSHOT DESCRIPTION] block must provide exact UI state detail sufficient for a human to take the screenshot.

10. **The Troubleshooting chapter or appendix must address the top 10 most commonly reported user problems** for the covered product (researched from support forums, official FAQ, and 1- and 2-star Amazon reviews of competing titles). Generic troubleshooting is not acceptable.

11. **The Interface Element Naming Index in the appendix is mandatory.** This is the reader's cross-reference between the book's language and the product's interface. It is the primary tool for readers who search for a feature by its screen name rather than by task category.

12. **Anti-AI language strictly enforced.** Prohibited: "In today's fast-paced digital world," "It's important to note," "Let's dive into," "Here's what you need to know," "Moving forward," generic enthusiasm without specificity. Required: Technical communication register — precise, efficient, active-voice instruction. Sentence-level clarity standard: a non-technical reader must be able to follow the instruction; a technical reader must find it unambiguous.

---

## QA Checklist

### Gate 1 — Pre-Creation Foundation

- [ ] Trademark Clearance Report completed; title framing confirmed as nominative fair use; verdict CLEAR or operator-approved CAUTION
- [ ] All subtitle candidates passed trademark screen
- [ ] Covered product version explicitly identified and recorded — if not in title, operator has confirmed version before proceeding
- [ ] Version declaration drafted for Copyright Page
- [ ] Product Architecture Map completed (software: navigation structure + feature categories; hardware: component nomenclature + control interfaces)
- [ ] Primary user task set identified and mapped to chapter structure
- [ ] Task-oriented chapter titles drafted (none reference features by name; all reference user actions)
- [ ] Audience, prerequisites, and system requirements documented
- [ ] Competitor version analysis complete — competing titles' versions noted
- [ ] Auto-configuration announced (pathway, page band, visual density, font, spacing, screenshot convention, Design Signature)
- [ ] Trademark acknowledgment language drafted for Copyright Page
- [ ] Warning hierarchy format confirmed (ANSI Z535.6 / ISO/IEC 82079-1)

### Gate 2 — Real-Time Content Development (Per Chapter)

- [ ] Chapter title names a user task, not a product feature
- [ ] Every procedure has a Pre-Step block listing prerequisites and version
- [ ] Every step contains exactly one action verb and one instruction
- [ ] Every UI element name in steps is in bold and matches the product exactly (Terminology Parity spot check)
- [ ] Warning boxes use ANSI hierarchy (DANGER/WARNING/CAUTION/NOTICE/VERSION NOTE) — no non-standard advisory formats
- [ ] Warning placement: at the step where the risk occurs, not only in front matter
- [ ] Version Notes present at all steps that differ from prior major version
- [ ] Screenshots present (or SCREENSHOT DESCRIPTION blocks) for every procedure step requiring visual reference
- [ ] Screenshot callout tables present for all annotated screenshots
- [ ] Anti-AI language protocol enforced — no prohibited phrases
- [ ] Chapter ends with Chapter Checkpoint (3–5 bullets)

### Gate 3 — Post-Chapter Review (Terminology Parity + Technical Accuracy Audit)

- [ ] Technical Communication Authority has completed a terminology parity check for all UI element names in this chapter — zero mismatches confirmed
- [ ] UI/UX Specialist has confirmed that all described menu paths, button sequences, and screen flows are accurate for the covered version
- [ ] All warning placements reviewed for ANSI Z535.6 compliance
- [ ] Instructional Design Authority confirms all procedures are executable as written by a user at the declared skill level
- [ ] All screenshots/SCREENSHOT DESCRIPTIONS are current to the covered version — no prior-version UI states
- [ ] Version Notes present and accurate wherever prior-version differences exist
- [ ] Safety content accuracy: 100% — no callout is missing, no callout hierarchy level is incorrect
- [ ] Chapter word count and page estimate within page-band targets

### Gate 4 — Final Certification Before KDP Upload

- [ ] All chapters organized by user task, not by feature — task-oriented architecture confirmed throughout
- [ ] Covered version named on: Title Page, Introduction first paragraph, Copyright Page, KDP metadata
- [ ] Version disclaimer on Copyright Page: version, date, no-affiliation statement, trademark acknowledgment
- [ ] Front matter complete and in correct order: Title Page → Copyright Page → TOC → Preface → How to Use This Book → Introduction
- [ ] Preface exactly one page; How to Use This Book exactly one page; Conclusion exactly 1.5 pages
- [ ] Getting Started / Setup chapter (Chapter 1 or 2) enables complete first-use success in one session
- [ ] All seven Appendix elements present: Quick Reference Card, Keyboard Shortcuts Reference, Troubleshooting Index, Glossary, Interface Element Naming Index, Version History Note, Resource Directory
- [ ] Troubleshooting appendix covers the top 10 documented user problems for the covered product
- [ ] Visible page numbers start at Introduction (page 1); front matter unnumbered
- [ ] Design Signature applied consistently; logged in register; no repeat
- [ ] Author name consistent across Title Page, Copyright Page, and all metadata
- [ ] KDP categories confirmed correct; version number in metadata keywords
- [ ] Terminology parity confirmed across all chapters — final cross-reference of Interface Element Naming Index against all in-text references completed
- [ ] No prohibited AI-pattern language in any chapter
- [ ] Warning hierarchy compliance confirmed across all chapters (ANSI Z535.6 / ISO/IEC 82079-1)

---

## KDP Positioning

### Amazon Category Tree

**Primary and secondary categories depend on the product type:**

| Product Type | Primary Amazon Category | Secondary Category |
|---|---|---|
| General software (Windows, macOS) | Books > Computers & Technology > Operating Systems | Books > Computers & Technology > Software |
| Productivity software (Office, Google Workspace) | Books > Computers & Technology > Software > Spreadsheets | Books > Computers & Technology > Business Technology |
| Creative software (Photoshop, Illustrator, Premiere) | Books > Arts & Photography > Digital Art | Books > Computers & Technology > Graphics & Design |
| Consumer device (smartphone, tablet, smart home) | Books > Computers & Technology > Hardware & DIY | Books > Computers & Technology > Mobile Phones |
| Camera / photography equipment | Books > Arts & Photography > Photography & Video > Equipment |Books > Computers & Technology > Hardware & DIY |
| Craft equipment (Cricut, sewing machines) | Crafts, Hobbies & Home > [relevant craft sub-category] | Books > Computers & Technology > Hardware & DIY |
| Business software (CRM, accounting, ERP) | Books > Computers & Technology > Business Technology | Books > Business & Money > Skills |
| Gaming platform or software | Books > Computers & Technology > Games & Strategy Guides | [platform-specific category] |
| Medical device / professional instrument | Books > Health, Fitness & Dieting > Medical Reference | Books > Reference > Handbooks & Manuals |

### KDP Description Formula

The description **leads with the covered version and the reader's task promise.**

1. **Version Hook:** "[Product Name] [Version] — this is the guide written specifically for the [Year] release, covering every feature update since [prior version]."
2. **Audience and gap:** "If you've opened [Product] and found the interface overwhelming, or if you've been using it for months but suspect you're missing key features..."
3. **Task-organized proof:** Name 3–5 specific tasks the reader will master — using the exact task-language from the chapter titles.
4. **Differentiators:** Version-specific coverage, annotated screenshots, terminology parity with the actual product interface, troubleshooting for the top 10 user problems.
5. **Feature bullets** (5–7 bullets): Step-by-step procedures for [N] workflows, [N] annotated screenshots, ANSI-compliant warning callouts, keyboard shortcuts reference, interface element naming index, troubleshooting for [N] common problems, both metric and imperial where applicable.
6. **Close:** A specific statement of what the reader will be able to do — tied to the outcome promise from Step 0-D.

### Metadata Signals

- **Keywords (7 slots):** "[Product name] guide [version/year]", "[product name] user manual", "[product name] for beginners", "[product name] step by step", "[product name] tutorial book", "[product name] handbook", "[product name] [year] update."
- **Version in keywords is mandatory.** The version number distinguishes this book from outdated competitors and captures readers searching specifically for the current version.
- **"Unofficial" in metadata** if the title includes "unofficial" — this signals to algorithm and reader that the book is independent content, which some readers actively prefer.

---

## Key Rules — Do NOT Break

1. **The covered product version is named on the cover, in the Introduction's first paragraph, and in KDP metadata.** No version ambiguity anywhere in the book. This is the single most important differentiator in the user-guide niche.

2. **Terminology parity is absolute.** Every UI element name, menu label, button text, dialog box title, and keyboard shortcut in the book must match the product's actual interface exactly. No synonym substitution. No simplification of official labels. Not even for readability.

3. **Task-oriented chapter organization is mandatory.** Chapters are organized by what users do. "Chapter 3: The Insert Tab" is prohibited. "Chapter 3: Adding Images, Charts, and Tables" is correct.

4. **One action per step.** No compound instructions. Steps begin with an action verb.

5. **All UI element names in steps appear in bold.** Every single one. No exceptions for "obvious" or "frequently repeated" elements.

6. **Warning hierarchy (DANGER/WARNING/CAUTION/NOTICE/VERSION NOTE) is the only permissible advisory message format for safety or operationally important information.** Non-standard callout formats for safety messages are a documentation standard violation.

7. **Version Notes are mandatory at every step that differs from the prior major version.** Do not assume the reader is on the exact covered version — they may have auto-updated.

8. **The Copyright Page disclaimer is non-negotiable.** Covered version + date, no-affiliation statement, trademark acknowledgment, future-version variance notice.

9. **Screenshots must be current to the covered version.** A screenshot from a prior UI version is misinformation.

10. **The Troubleshooting chapter/appendix must cover the top 10 documented user problems** — not generic troubleshooting invented without research.

11. **The Interface Element Naming Index in the appendix is mandatory.** It is the reader's cross-reference tool and the publisher's proof of terminology parity.

12. **The anti-AI language protocol is non-negotiable.** Technical communication register throughout. Precise, active-voice, efficient instruction. No AI-pattern preambles, transitions, or enthusiasm without specificity.

## Textbook reference-bank standard applies (2026-08-14)

This niche is an educational/reference category: the HOUSE REFERENCE BANK
standard for textbooks and educational books (see uapf-niche-textbook,
"HOUSE REFERENCE BANK", derived from five catalog masters at
cover_db/_interiors/textbook/) is BINDING here on both engines and every
install: scholarly justified body, decimal-numbered sections, evidence and
key-concept panel families, shaded-header tables, labeled multi-panel
figures, professional front matter, one distinct accent system per book,
and NO TWO BOOKS with the same pattern. Niche-specific structures in this
skill (question banks, drills, exercises, entries) keep their own
architecture inside that quality bar.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
