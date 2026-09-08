---
name: hard-rules
description: Non-negotiable house rules for every book, cover, and A+ asset. Apply before starting any generation task in this studio; never skip.
---

# Hard rules (apply to every book, cover, and A+ asset)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

These are the quick-reference essentials. The BINDING law is the full "Global
hard rules" section in this studio's `AGENTS.md`, and, when this studio is
installed inside Genie, everything in `../AGENTS.md` as well (which wins on any
conflict). Apply all of it, always.

Never break these:
- No em dashes anywhere. Use commas, colons, or short sentences.
- No fabrication: no invented facts, statistics, sources, quotations, reviews,
  credentials, or publishing status.
- No pork or pig derivatives and no alcohol, anywhere: not in text, recipes,
  examples, quotes, or images. Enforce this silently; never announce or explain it.
- Preserve the operator's exact title. Never rewrite it.
- Place answer sections after the question section, not under each question, and
  vary the correct-option positions with no obvious pattern.
- Premium, colorful interior. Plain black-on-white is a failure. Add images
  wherever the content needs them.
- No publisher name in reader-facing content, metadata, or byline.
- No ISBN placeholder. Omit the line entirely if none is assigned.
- No image or table crosses the page margins. Caption every image beneath it as
  Figure C.N with a description, and label every table beneath it as Table C.N,
  numbered per chapter.
- Never claim a book is finished or ready to upload. Final gates, house-style
  images, cover polish, and publishing happen in Genie on Claude Code.
- **Cookbook step compression (operator directive 2026-08-14):** Every recipe step
  is ONE imperative sentence, maximum 15 words, fitting within two rendered lines.
  Tips, technique notes, and "why" explanations go in the "Note:" field only.
  Steps that overflow two lines are a layout failure — rewrite before advancing.
- **Page-count accuracy (operator directive 2026-08-18):** The finished book must
  hit the target page count, or land within 5% of it either way. Size the chapter
  plan to the target from the start so the book converges on the band; fix any miss
  by adding or trimming real CONTENT, never by padding blank pages or shrinking type
  below the niche/senior floor. Verified in Genie by
  `python ../.agents/skills/uapf-quality-gates/page_count_gate.py --project <folder>
  --docx <final.docx>`; a count outside [target-5%, target+5%] is a failure.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
