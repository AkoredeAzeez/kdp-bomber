---
name: uapf-localization
description: Turn one finished book into translated editions for other Amazon marketplaces (German, French, Spanish, Italian, Japanese, and more). ALWAYS confirms the plan with the operator before translating anything. Adapts text, metadata, keywords, measurements, and currency per market. Use when the operator wants to sell a finished book in more marketplaces.
---

# UAPF Localization

Take a finished book and produce quality editions for other Amazon marketplaces. Translation is done by Genie, but only AFTER the operator confirms the plan. Never start translating on assumption.

## When to run
- A book is finished (manuscript, metadata, and cover) and the operator wants it in more marketplaces.

## STEP 1 (REQUIRED): plan, then CONFIRM before translating
1. Build the plan:
   python genie_localize.py plan --title "TITLE" --targets DE,FR,ES,IT --out localization_plan.json
2. Present the plan to the operator in plain language:
   - the source book and language,
   - the target marketplaces and languages,
   - what will be produced per market (translated manuscript, localized metadata and keywords, cover text in the target language),
   - the honest quality caveat below,
   - whether to translate the TITLE for each market or keep the original. Do not decide this alone; the Title Preservation Law means the operator owns the title.
3. STOP and get the operator's explicit YES before translating anything. If the operator named only some languages, still confirm the full list and the title decision first. No translation begins without confirmation.

## Honest quality caveat (state it every time)
AI translation is strong but not automatically publication-grade, especially for idioms, humor, safety-critical wording, and languages the model handles less well. Recommend a native-speaker proofread before publishing, and say so plainly. Never claim a translation is professionally certified.

## STEP 2: translate (only after confirmation)
For each confirmed market:
1. Translate the full manuscript faithfully: preserve meaning, structure, headings, tables, questions and answers, figure and table captions, and all promised elements. Translate captions and any in-image text notes; regenerate an image only if it has baked-in source-language text.
2. Adapt, do not just translate: measurements (imperial to metric per the market), currency, date format, examples, and idioms, so the book reads native.
3. Keep every global hard rule in the target language: absolute content restrictions, no fabrication, no publisher name in reader-facing content, no ISBN placeholder, no em dashes (use the language's normal punctuation), and the margin and caption rules.
4. Cover: the front-cover title, subtitle, and back-cover copy must be in the target language. Run the cover pipeline again for that edition (uapf-cover-reference on that marketplace, then uapf-chatgpt-cover-pipeline) so the cover text and market fit match the local shelf.

## STEP 3: localized metadata (per market)
Do NOT translate keywords word for word. Research what buyers in that marketplace actually type, then build the description, the seven keyword fields, and the categories for that market via uapf-kdp-assets. Price is set in the local currency by the operator.
When researching a market on Amazon, use that market's own domain (amazon.de, amazon.fr, and so on) and set the "Deliver to" location to a real postal code in that country, never Nigeria, so autocomplete, results, and prices reflect that market. Defaults: DE 10115, FR 75001, ES 28001, IT 00184, NL 1011AA, JP 100-0001, UK SW1A 1AA, US 10001.

## STEP 4: track and publish
- Record progress: python genie_localize.py --plan localization_plan.json set --locale DE --status translated (then metadata, then published with the ASIN).
- Overview any time: python genie_localize.py --plan localization_plan.json overview --out localization_overview.html
- Each translated edition is its own KDP listing in that marketplace. Per-book, per-marketplace operator confirmation before any publish click, always.

## Supported marketplaces
Run python genie_localize.py markets to list them (US, UK, DE, FR, ES, IT, NL, JP, MX, BR). Each carries its language, currency, measurement system, and date format.

## Hard rules
- CONFIRM BEFORE TRANSLATING. No translation work starts until the operator approves the plan and the title decision.
- Real data only: never fabricate a translated review, a rank, or a claim, and never invent an ASIN.
- Faithful translation: never add, drop, or "improve" content beyond what localization requires; preserve the author's meaning.
- Every edition passes its own QA and all global hard rules in the target language.
- Per-book, per-marketplace operator confirmation before publishing.
