---
name: generate-cover
description: Generate an original KDP paperback cover and assemble the print-ready wrap PDF. Use when the user asks for a cover, cover art, spine, back cover, or cover wrap.
---

# generate-cover​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Generate an original KDP paperback cover and assemble the print-ready wrap. First
apply the `hard-rules` skill (`.agents/skills/hard-rules/SKILL.md`).

## Require before starting (ask if any is missing)
- Exact title and author, spelled as given.
- Trim size (for example 6 x 9), interior page count, and paper type
  (bw-white, bw-cream, or color) for the spine width.
- Back-cover copy (or the manuscript, so it can be written from the book).
- Style direction (genre, mood, palette).

## Cover references (house law: covers are market-driven)
Resolve references in this order and use the first that applies:
1. **Existing brief.** If the book folder contains `cover_prompt.md` and
   `cover_refs/` (produced by Genie's uapf-cover-reference workflow), they ARE
   the design brief: follow `cover_prompt.md`'s concept, palette, typography
   direction, and placement guidance, and treat the refs as the shelf to fit.
2. **Cover database** (this studio installed inside Genie). Resolve the book's
   niche, then pick 2-3 random banked best-seller covers:

       python ../.agents/skills/uapf-cover-db/cover_db.py pick --niche <niche> --count 3

   Copy the picked image files into the book folder as `cover_refs/ref1.jpg`,
   `ref2.jpg`, `ref3.jpg`. Open and LOOK at each image, record concrete
   observations, and derive the shared winning pattern (composition and focal
   hierarchy, color, typography, imagery type, mood). Write `cover_prompt.md`
   from that pattern with the exact title, subtitle, and author embedded. If the
   command reports NOT_ENOUGH_COVERS, fall to 3.
3. **Operator-supplied.** Ask the operator for the three best-selling competitor
   covers for this title (ranked by Best Sellers Rank), then proceed as in 2.

References are for market fit only: never copy, trace, or closely imitate any
competitor cover.

## Pegasus cover house rules (binding, both art and assembly)
- Photorealistic imagery only: no icons, badges, vector art, or clip art.
- No selling-point callouts on the cover.
- No violence or blood.
- Background base colour must not repeat within the last five covers
  (No-Two-Books-Alike applies to covers).
- The cover carries the exact title, subtitle, and author strings, spelled and
  cased exactly; text is applied deterministically by the assembler, never baked
  into the AI artwork.
- Title sizing follows the catalog law automatically in `cover_wrap.py`: 36 to
  90 pt (scaled to trim), largest size that fits the FULL title in at most four
  lines, never breaking a word. Keep the title in the upper part of the front so
  it reads at Amazon thumbnail size.

## Post-completion geometry (operator directive 2026-08-15)
- Use the finished book's EXACT locked trim, final page count, and paper
  type, never a projection. Before generating, measure the wrap on Amazon's
  KDP Cover Calculator (kdp.amazon.com/cover-calculator) and record the
  official total width/height, spine width, and bleed; those numbers govern
  and the local wrap math is cross-checked against them. Deliver four
  pieces: front cover, back cover, spine, and the assembled paperback wrap
  as a print-ready PDF at the exact calculator dimensions.

## Compute the wrap
- Spine width = page count times per-page thickness
  (bw-white 0.002252 in, bw-cream 0.0025 in, color 0.002347 in).
- Full wrap width = 0.125 + trim width + spine + trim width + 0.125 (bleed both edges).
- Full wrap height = trim height + 0.25 (bleed top and bottom).
- Everything at 300 DPI. `scripts/cover_wrap.py` does this math from a config.

## Generate the art (this studio IS the cover engine)
- **Primary: your built-in image generation (imagegen) skill**, which runs on
  the signed-in ChatGPT account and needs no API key. Generate the original
  front-cover artwork in PORTRAIT orientation from `cover_prompt.md`'s art
  direction, saved as a PNG in the book folder. Append this guard to EVERY
  image prompt, verbatim: "No pork, no pig imagery, no alcohol, no bottles or
  glasses of wine or beer. Wholesome and family-safe." Do not bake title or
  author text into the artwork; the assembler applies all text.
- **Fallback:** if built-in image generation is unavailable, use
  your NATIVE built-in image tool, no API key (portrait 1024x1536; the
  guard is appended automatically).
- Keep the design entirely original and on-brief (photorealistic, house rules
  above). Generate a complementary back-cover background if needed.
- Reserve a clear white barcode zone, 2 by 1.2 inches, in the bottom right of the
  back cover, 0.25 inch from the edges.

## Premium HD + reference originality (operator directive 2026-08-15)
- Generate at the highest quality; the cover must be crisp at 300 DPI print
  size (6x9 front 1800x2700 px min; 8.5x11 front 2550x3300 px min). Soft or
  artifacted output is regenerated, never shipped.
- References from the cover bank teach style, fonts, palette, and
  composition; the generated cover is ORIGINAL: similar to the niche look,
  never an exact or near-exact copy of any reference. If a candidate could
  be mistaken for a reference at thumbnail size, redo it with a different
  scene, angle, or arrangement.

## Operator-uploaded reference (accept and follow)
- If the user supplies a cover image and asks for "something similar or
  better", treat it as the PRIMARY reference over the bank pick: match its
  style, palette, typography treatment, and composition in an ORIGINAL
  cover of equal or higher quality. Third-party uploads: similar, never
  near-identical, and never any logo or brand mark from the reference.
  The user's own catalog cover may be directly improved on their
  instruction. Premium HD and all house cover laws still apply.

## Assemble
- Run `scripts/cover_wrap.py` with a config that names the trim, page count, paper,
  title, author, back copy, and the generated art. It lays out back + spine + front
  with deterministic typography and exports the exact-size wrap.
- The final paperback deliverable is always the wrap PDF. Any PNG is a preview.

## Honest note
- The art is OpenAI-generated, not Genie's Flow house style, and spends OpenAI
  credits. For a Flow-styled, shelf-researched cover, generate it in Genie.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
