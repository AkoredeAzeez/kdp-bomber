# What Can Genie Do?​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Genie is your AI book production assistant. Tell Genie what you need in plain English — no commands required.

---

## Starting a New Book

Just describe what you want:

- "Write a book about healthy eating for seniors"
- "I want a cookbook for busy parents, 200 pages"
- "Make a children's activity book about space"
- "Create a 30-day fitness workbook for beginners"
- "Write a self-help book called [your title] for Amazon UK"

Genie handles the structure, the writing, the formatting, and the images — all automatically.

**Not sure how to phrase it?** Run the intake wizard for a step-by-step guide:
`python genie_intake.py`

---

## Checking Your Progress

- **"Genie, standup"** — full status report
- **"What chapter are we on?"** — quick progress check
- **"Show me what has been written so far"** — summary of completed chapters
- **"How many pages do we have?"** — current page count

Or run the dashboard anytime:
`python genie_standup_client.py`

---

## Continuing a Book

- **"Resume"** or **"Continue the book"** — picks up from where it stopped
- **"Resume [book title]"** — resume a specific book if you have more than one
- **"Pause auto-advance"** — stop between chapters so you can review each one
- **"Resume auto-advance"** — go back to writing chapters automatically

---

## Reviewing and Correcting

- **"Change chapter 3 to focus more on [topic]"** — revise a chapter
- **"Make the tone more conversational"** — style adjustment
- **"The intro is too short, expand it"** — length correction
- **"Fix the formatting in chapter 5"** — formatting correction

---

## Images

- **"Use [free/Codex/HiDream/FLUX] for images"** — choose your image engine
- **"Generate the images for this book"** — add images to a text draft
- **"No images for this book"** — text-only production
- **"Regenerate the image for chapter 2"** — redo a specific image

---

## Covers

- **"Make a cover for [book title]"** — design a full KDP-ready cover
- **"Show me 3 cover concepts"** — see options before committing
- **"Hardcover edition of [book title]"** — create a hardcover variant
- **"Large print edition of [book title]"** — larger text, new cover

---

## Publishing on Amazon

- **"Prepare the KDP metadata for [book title]"** — title, description, keywords, categories
- **"What categories should I pick?"** — niche-specific KDP category advice
- **"Publish [book title] to Amazon"** — guided KDP upload (you confirm the final click)

---

## Audio

- **"Make an audiobook of [book title]"** — narration, WAV compliance, distribution
- **"Narrate [book title] in Spanish"** — multilingual narration

*(Audiobook features require the MAX plan.)*

---

## Other Formats

- **"Make an EPUB of [book title]"** — ebook for Kobo, Barnes & Noble, Draft2Digital
- **"PDF version for wide distribution"** — print-ready PDF for IngramSpark

---

## Business

- **"How are my books selling?"** — royalty and sales summary from your real KDP data
- **"What should I publish next?"** — niche and market analysis
- **"Run ads for [book title]"** — Amazon Ads setup and weekly optimization

---

## Handy Commands

| What you say | What happens |
|---|---|
| "Genie, standup" | Full production + sales status report |
| "Genie, help" | Shows this guide |
| "What can you do?" | Same as above |
| "Resume" | Continues the current book |
| "Pause" | Stops between chapters for your review |
| "How long until this book is done?" | Estimated completion time |

---

## Useful Scripts (run from the Genie folder)

| Script | What it does |
|---|---|
| `python genie_intake.py` | Step-by-step new book wizard |
| `python genie_progress.py` | Full book dashboard + saves MY_BOOKS.md |
| `python genie_standup_client.py` | Your current book status in plain English |

---

## Important Notes

- Genie **never** spends money, publishes, or sends messages without your explicit confirmation.
- Every final "Publish" click on Amazon is always confirmed by you — Genie never clicks it for you.
- Your books are saved in the `Books/` and `projects/` folders in the Genie directory.

---

*Questions? Just ask Genie anything in plain English — it will figure out what you need.*
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
