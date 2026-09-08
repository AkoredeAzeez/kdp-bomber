---
name: generate-aplus
description: Generate Amazon A+ content modules and assemble 970x600 masters. Use when the user asks for A+ content, listing modules, or Amazon marketing images.
---

# generate-aplus​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Generate Amazon A+ content modules and assemble 970x600 masters. First apply
the `hard-rules` skill (`.agents/skills/hard-rules/SKILL.md`).

## Require before starting (ask if any is missing)
- The book title, category, and its main selling points (or the manuscript).
- How many A+ modules to produce (a typical set is 3 to 5).
- Style direction and palette (keep it consistent with the cover).

## Plan the modules
For each module, write:
- A short headline (benefit-led, no fabrication, no publisher name).
- One or two lines of body copy drawn from the actual book.
- An image brief for the module art.

## Generate the art
- Generate each module image with your NATIVE built-in image tool (never an
  API key). Use landscape
  1536x1024 for banner-style modules and 1024x1024 for tiles, then the assembler
  fits them to the 970x600 frame.
- Keep imagery family-safe, with no pork or alcohol anywhere. Do not put
  unreadable small text inside the generated art; real text is added by the
  assembler.

## Assemble
- Run `scripts/aplus_assemble.py` to compose each module into a 970x600 master
  (art plus headline plus body), exported as PNG at the exact Amazon dimension.

## Finish
- Deliver the set of 970x600 masters plus a short caption sheet mapping each
  module to its headline and source. Do not claim listing status; A+ upload
  happens in Genie.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
