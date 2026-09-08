---
name: uapf-quality-gates
description: Run UAPF factual, audience, structural, voice, proofreading, consistency, originality, policy, formatting, source-presentation, and blocker-management reviews.
---

1. Declare the review scope and source version.
2. Treat every draft as unverified until checked.
3. Separate findings by category and severity.
4. Verify facts and numbers against internal source and claim ledgers.
5. Verify that raw `SRC-####` identifiers do not appear in reader-facing files.
6. Verify that references appear in back matter without internal IDs.
7. Verify the Introduction occupies approximately 2–3 rendered pages.
7b. Verify the GLOBAL premium interior mandate (AGENTS.md "Manuscript
    formatting — premium interior") is satisfied in every chapter: styled
    openers, colored typographic system, tinted callout panels, styled
    tables, shaded unit header bars, grayscale legibility. A plain
    black-on-white manuscript is a Class A formatting finding in every niche.
7c. Verify no image or table crosses the page margins, and that every image has a
    "Figure C.N: description" caption directly beneath it and every table a
    "Table C.N" label directly beneath it, numbered per chapter and reset each
    chapter. A margin overflow, or a missing, misplaced, or misnumbered figure or
    table caption, is a Class A formatting finding.
7d. Run the active niche's machine-executable framework checks. Resolve the niche's
    `frameworks/<FRAMEWORK_ID>/` folder (the `framework=` token in `book_lock.md`). Load
    `validation.json` and enforce every gate: run each `type: "python"` check via the niche's
    `genie_<X>.py` deterministic operations (page-governor/page-band, category/section counts,
    image-slot and image counts, per-serving or answer-key math, budget) and treat any failing
    computation as a Class A finding; verify each `type: "manual"` gate by inspection. Confirm
    the produced book matches the `config.json` constants (trim, body type, counts, ranges).
    The niche SKILL.md remains authoritative if it and the projection ever disagree.
7e. Render-containment QA (EVERY niche, mandatory before PASS). Export the produced DOCX to
    PDF and inspect every rendered page — never assume layout from the source:
    ```
    python render_qa.py --docx "<book.docx>" [--expect-pages N] [--bleed-pages 2,5]
    # if this environment cannot drive Word from Python, export the PDF via Word first, then:
    python render_qa.py --pdf "<book.pdf>" [--expect-pages N]
    ```
    It FAILS the book if any non-bleed page has text or an image crossing the margins, or the
    book spills past its expected page structure (a unit that overflowed its column/page). Any
    violation is a Class A finding. Full-bleed pages (dividers/covers) are declared with
    --bleed-pages or auto-detected. This is how "no recipe beyond its column, no text beyond the
    margin" is verified on the page for cookbooks and the equivalent containment rule for every
    other niche — enforced, not eyeballed.
7f. Page-count accuracy gate (EVERY niche, mandatory before a book is marked complete; global
    hard rule 21). The final rendered page count must be within 5% of the target, either way:
    ```
    python page_count_gate.py --project "<book_folder>" --docx "<final.docx>"
    # or with a pre-exported PDF / a known count:
    python page_count_gate.py --target N --pdf "<final.pdf>"
    python page_count_gate.py --target N --actual <pages>
    ```
    It resolves the target from project.json (requested_page_count, else a target_pages_min/max
    band, else provisional_page_ceiling, else projected_physical_pages; --target overrides) and
    FAILS as a Class A finding if the count is outside [target-5%, target+5%]. The report gives the
    exact page delta to reach the band and to hit the target. Repair by CONTENT only: expand real
    material for an under-count, tighten/re-plan for an over-count — never pad blank pages or shrink
    type below the niche/senior floor (rules 17 and 18 still bind). Re-render and re-run until PASS.
8. Repair Class A findings automatically.
9. Queue Class B findings and continue independent work.
10. Do not mark PASS while a terminal blocker or unresolved high-severity finding
    makes the manuscript unreliable.
11. Update review, state, decision, and blocker records.

## TEXT HYGIENE (rendering cleanliness, visible QC step)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

`text_hygiene.py` removes genuinely stray invisible/control characters that
break DOCX/EPUB rendering or trip KDP ingestion (zero-width space U+200B, word
joiner, mid-text BOM, soft hyphen, C0/C1 control chars), reports exactly what
it removed, and keeps a `.prehygiene.bak`. Legitimate marks are preserved:
non-breaking space, real hyphens, and ZWJ/ZWNJ (which matter in Arabic, Indic,
and emoji) are FLAGGED, never blind-stripped; U+FFFD is flagged as encoding
data loss for human review.

```
python .agents/skills/uapf-quality-gates/text_hygiene.py <final.docx> --fix
```

Run it at release QC on the final rolling DOCX (and on chapter previews if a
source paste looked dirty). This is FILE CLEANLINESS ONLY: it does NOT target,
detect, or defeat any AI provenance or watermark system, and never alters
authorship or the truthful ai_disclosure value in the publish manifest. It is
a visible, logged step, never an "underground" one. Ships every pack, both
engines.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
