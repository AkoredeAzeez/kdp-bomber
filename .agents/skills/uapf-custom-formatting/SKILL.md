---
name: uapf-custom-formatting
description: Client-facing per-niche formatting customization, two modes. INTERVIEW mode records the client's preferred style by Q&A. MIRROR mode (operator directive 2026-08-19) lets the client upload a book of their choice (DOCX best, PDF supported) and Genie extracts its complete formatting fingerprint mechanically (style_mirror.py) and applies that SYSTEM to every future book in the niche, while No-Two-Books-Alike and the premium interior law still bind every individual book. Invoke on "Genie, customize formatting for [niche]", "Genie, mirror this book's formatting for [niche]", "format my [niche] books like this book", "Genie, show my formatting style", "Genie, reset formatting for [niche]".
---

# UAPF Custom Formatting (per-niche client styles)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

## Purpose

Lets the studio's user define the formatting style THEY want for each niche,
either by describing it (INTERVIEW) or by handing Genie a book to copy the
formatting system from (MIRROR). Once a niche profile is saved, every future
book routed to that niche is formatted to the profile automatically, by BOTH
engines (Claude and Codex), until the profile is changed or reset.

## Commands

| Command | Action |
|---|---|
| "Genie, customize formatting for [niche]" | Interview, then save the niche profile |
| "Genie, mirror this book's formatting for [niche]" (+ a DOCX/PDF) | MIRROR mode: extract the book's formatting fingerprint and save it as the niche profile |
| "format my [niche] books like this book" | Same as mirror |
| "Genie, show my formatting style for [niche]" | Display the saved profile |
| "Genie, show all my formatting styles" | List every saved profile |
| "Genie, reset formatting for [niche]" | Delete the profile; house defaults return |

The niche is one of the 29 standard keys (cookbook, textbook, selfhelp, ...).
If the user names a niche loosely ("my recipe books"), map it to the key and
confirm.

## MIRROR MODE (upload a book, Genie mirrors its formatting)

When the client provides a book file, run the mechanical extractor:

```
python .agents/skills/uapf-custom-formatting/style_mirror.py \
    --file <their-book.docx|pdf> --niche <key>
```

It reads the book and captures the complete formatting SYSTEM:

- trim size and all four margins
- body font family, size, line spacing, alignment
- the full heading scale: H1/H2/H3 sizes, case convention, alignment, weight
- chapter-opener pattern (hero image vs styled text opening)
- the unit anatomy and label vocabulary (Ingredients/Directions, Yarn/Hook/
  Round N, Materials/Steps, whatever the book actually uses)
- table style class (shaded headers, row tints vs plain) and callout usage
- image density and totals
- front and back matter sequence and TOC depth

Then: present the extracted summary to the client in plain language, confirm
it reads like the book they handed over, and save. DOCX gives the full
fingerprint; PDF extraction is approximate (say so) and the client should be
offered the chance to answer the two or three questions the PDF could not
reveal. A mirrored profile can be fine-tuned afterward by interview at any
time ("keep everything but make the headings centered").

### THE MIRROR LAW (non-negotiable)

**What IS mirrored:** structure and rhythm. Trim, margins, type scale, spacing,
heading case and alignment, unit anatomy, opener pattern, table/callout style
classes, density, matter order. This is the SYSTEM of the book.

**What is NEVER mirrored:** the exact color palette (the extractor records a
palette DIRECTION at most; concrete colors are generated fresh per book), any
artwork, motifs, decorative elements, cover identity, layout files, or text.
Mirroring a third-party book's structure is learning from architecture;
copying its colors, art, or identity would violate No-Two-Books-Alike and is
never done, whoever the book belongs to.

**No-Two-Books-Alike still governs every book.** Two books produced under the
same mirrored profile share the skeleton but must never look the same: each
book generates its own unique concrete palette, motif set, and arrangement
fingerprint INSIDE the mirrored system, and the standard fingerprint
uniqueness check (thumbnail-confusion test included) still gates every book.

**The premium floor still binds.** If the uploaded book is plain
black-on-white, Genie mirrors its structure and executes it WITH the premium
color system (styled openers, colored typography, tinted panels, styled
tables, header bars) in each book's unique palette. Tell the client plainly:
"I mirrored the layout; the color styling stays premium, that part is house
law." A mirror can never disable the premium interior, type floors,
containment, senior sizing, or any global hard rule.

## The interview

Ask only about what the user wants to control; anything not specified stays on
the house default. Cover, in plain language:

1. Body font and size (within the legal floors below).
2. Heading treatment: font, weight, capitalization taste.
3. Color direction: the palette family they want (e.g. "warm earth tones",
   "clean blues", "bold high-contrast"). The exact palette still varies book
   to book under No-Two-Books-Alike; the profile sets the DIRECTION.
4. Chapter opener style: hero image, styled callout, motif line, minimal.
5. Callout panel taste: soft tints vs strong borders; rounded vs square.
6. Table style preference.
7. Line spacing and alignment preference.
8. Anything to always include or avoid (visual elements only).

Confirm the summary back to the user before saving.

## Storage

One JSON file per niche at `state/custom_formatting/<niche>.json`:

```json
{
  "niche": "cookbook",
  "body_font": "Georgia",
  "body_size_pt": 12,
  "heading_font": "same-as-body",
  "heading_style_notes": "bold, generous spacing above",
  "palette_direction": "warm earth tones",
  "chapter_opener": "hero image with colored rule",
  "callout_style": "soft tinted panels, rounded",
  "table_style": "shaded header, light row tints",
  "line_spacing": "1.15",
  "alignment": "justified",
  "always_include": [],
  "always_avoid": [],
  "notes": "",
  "saved": "2026-08-14"
}
```

A MIRRORED profile uses the same file with `"mode": "mirrored"`,
`"mirrored_from": <filename>`, and a full `"mirror"` block holding the
extracted fingerprint (trim, margins, heading scale, unit labels, table and
callout classes, densities, matter order). The design fingerprint consumes
the mirror block the same way it consumes interview answers.

`state/` is never touched by the updater, so profiles survive every version
update. Profiles are per-install and are never shipped in packages.

## Application

- At Phase 0 / book intake, after the niche is routed, check
  `state/custom_formatting/<niche>.json`. If present, load it, record
  "custom formatting profile applied" in the decision log and `book_lock.md`
  notes, and pass its choices into the design fingerprint.
- The profile shapes the book's design system; No-Two-Books-Alike still
  applies WITHIN the profile (each book gets a unique concrete palette,
  motifs, and arrangement inside the client's chosen direction).
- Both engines honor the same file: Codex runs (CodexBookStudio and
  failover) read `../state/custom_formatting/` relative to the studio, or
  `state/custom_formatting/` at the package root.

## Precedence (non-negotiable)

A custom profile customizes AESTHETICS ONLY. It sits ABOVE the house
defaults in uapf-formatting-standard but BELOW every binding law. It can
NEVER override:

- The premium color bar: a profile may choose the style of the premium
  interior, never disable it. "Plain black-on-white" is not a valid profile.
- Containment and render QA: margins, no cutoff text, verified on the
  rendered page.
- Type floors: senior-audience 13 to 14 pt body; 8.5 x 11 chapter titles in
  BLOCK LETTERS at 28 pt or larger with subchapter headings 14 to 18 pt.
- Pagination and final TOC law; chapter-by-chapter build and dual-format
  preview delivery; trim-size defaults unless the operator sets a trim in
  the book brief.
- Global hard rules (content restrictions, no em dashes, Title Preservation,
  No-Two-Books-Alike, margin/caption law, and the rest).

If a requested preference conflicts with a law, explain the limit briefly,
offer the nearest compliant option, and save only what is allowed.

## Honesty

Never claim a profile was applied to a book that was produced before the
profile existed. When showing a profile, show what is actually in the file.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
