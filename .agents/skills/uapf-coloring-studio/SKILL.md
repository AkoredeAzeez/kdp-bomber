---
name: uapf-coloring-studio
description: The coloring-book BUILDER for OV-ACT books. Line-art direction (bold-and-easy vs detailed styles), per-page art briefs for the engines' image generators, the mechanical line-art QA gate (lineart_qa.py), single-sided assembly, and test-color pages. Invoked whenever a coloring book's pages must actually be produced ("Genie, build the coloring pages for [Title]", "bold and easy coloring book", "50 designs").
---

# UAPF Coloring Studio (line-art builder)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

uapf-niche-activity (OV-ACT) governs coloring-book ARCHITECTURE
(45-48 designs, single-sided with budgeted blank reverses, page maps).
This studio produces the actual pages and refuses bad ones mechanically.

## Style system (locked per book at design-fingerprint time)

- BOLD AND EASY (the current best-seller style, per the interior bank):
  thick 8-14 px-equivalent outlines at print size, large open regions,
  minimal detail density, generous white space. Default for adults
  seeking relaxation, seniors, and kids.
- DETAILED/INTRICATE: fine-line dense compositions (mandalas, botanical,
  scenes) for the enthusiast market. Never mix the two styles in one
  book; the style is part of the design fingerprint and the subtitle
  promise ("Bold and Easy" on the cover means EVERY page qualifies).
- THEME PLAN: one coherent theme per book, one subject per page, no
  repeats; the theme list is written first and locked like a TOC
  (count promise = design count).

## Producing pages (image engine law applies)

- CLAUDE ENGINE: pages generate through Google Flow
  (uapf-flow-image-pipeline) from per-page briefs this studio writes.
- CODEX ENGINE: pages generate inline with Codex's native image tool.
- Every brief demands: pure black line art on pure white, no shading,
  no gray fills, no text, subject fully inside a stated safe margin,
  portrait at the locked trim. Briefs are saved as production records
  (never deleted after generation).
- ORIGINALITY: references from `interior_db.py pick --niche coloring`
  teach line weight and composition density only; never trace or
  reproduce a referenced design (No-Two-Books-Alike applies per page
  and across the catalog).

## The mechanical gate (every page, no exceptions)

```
python .agents/skills/uapf-coloring-studio/lineart_qa.py "pages/*.png" --trim 8.5x11
```

PASS requires: 300 DPI at trim, under 10% gray midtones (muddy print
killer), ink coverage 1.5%-45% (empty page / uncolorable blob bounds),
and white margin bands unless the page is declared full-bleed. A FAIL
page is REGENERATED from an adjusted brief, never retouched into
compliance or shipped. Results go in the book's QA log.

## Assembly

- Single-sided layout: every design on a right-hand page, blank reverse
  budgeted (OV-ACT law), so felt-tip bleed never ruins the next design.
- Front matter: title page, copyright (no publisher name, no ISBN
  placeholder), a short "how to use" page, and a TEST-COLOR page with
  swatch shapes ("try your markers here first").
- B&W interior on white paper; bleed only if the style is full-bleed
  scenes. Render-containment QA (rule 17) runs on the assembled PDF.
- Back matter: a one-page catalog teaser for the pen name's other books
  (truthful listings only).

## Tiers and engines

Included in every Community Edition install. Binds BOTH engines, Claude and
Codex alike. References come from uapf-interior-db (`pick --niche coloring`).
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
