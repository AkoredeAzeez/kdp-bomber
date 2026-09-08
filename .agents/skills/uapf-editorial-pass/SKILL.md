---
name: uapf-editorial-pass
description: Editorial line-edit gate that runs after every chapter passes its structural gates and before the chapter preview is delivered. Hunts AI "tells" (stock phrases, robotic rhythm, uniform paragraphs), scores readability against the locked audience, and checks the new chapter against the whole catalog for self-plagiarism. Also runs as a whole-book pass at release QC. Invoke on "Genie, editorial pass on [chapter/Title]" or automatically per the chapter gate law.
---

# UAPF Editorial Pass (line edit, AI-tell hunt, catalog originality)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

A world-class publisher puts an editor between the writer and the press.
This skill is that editor. It runs in EVERY niche, on BOTH engines
(Claude and Codex), and ships in EVERY pack.

## When it runs (binding, operator directive 2026-08-16)

1. AFTER a chapter passes its niche/structural gates and BEFORE the
   DOCX+PDF chapter preview is delivered: run both checks below on the
   chapter source. FAIL blocks advancement; the chapter is revised and
   re-run until it passes.
2. At RELEASE QC: run the whole-book readability audit plus the full
   catalog similarity sweep. A release is not PASS with an editorial FAIL.

## Check 1: readability + AI-tell audit

```
python .agents/skills/uapf-editorial-pass/readability.py <chapter file> --audience <band>
```

Audience band comes from the locked audience decision: `children`,
`general`, `senior`, `health` (patient-facing medical or condition
cookbooks, where necessary terminology inflates difficulty scores), or
`professional` (exam prep, clinical, engineering).
The script scores Flesch Reading Ease and FK grade against the band and
hunts the mechanical fingerprints of machine prose:

- stock phrases ("delve into", "in today's fast-paced world", "a testament
  to", "unlock", "elevate", "tapestry", and the rest of its list);
- robotic sentence rhythm (sentence-length variation below 0.40);
- repeated sentence starters (over ~22% of sentences opening with the
  same word);
- near-uniform paragraph lengths;
- exactly duplicated sentences inside the chapter.

Exit 0 PASS / 1 WARN / 2 FAIL. WARN is advisory: fix what is cheap to fix
now, note the rest in the review record. FAIL means REWRITE the flagged
passages (vary rhythm, cut the stock phrasing, split or merge paragraphs)
and re-run. Never "fix" a readability FAIL by padding or dumbing down
content that the niche requires; restructure sentences instead.

## Check 2: catalog self-plagiarism

```
python .agents/skills/uapf-editorial-pass/catalog_similarity.py --file <new chapter>
```

Compares the new chapter against every other BOOK in `Books/` and
`projects/` using 8-word shingle overlap. Same-book files are never
compared. Thresholds: 20% overlap = WARN, 35% = FAIL. On FAIL, rewrite
the overlapping passages so no two books in the catalog share prose;
shared FACTS are fine, shared SENTENCES are not. This protects the
account: KDP treats heavily duplicated content across a catalog as a
policy risk.

At release QC run the full sweep (no `--file`) to catch anything that
slipped through per-chapter checks.

## Honest limits

- These are mechanical screens, not a human editor. A PASS raises the
  floor; it does not certify literary quality. The niche skill's voice
  and content rules still govern what good looks like.
- Recipe steps, exam items, and worksheet instructions are legitimately
  formulaic; expect and accept higher structural uniformity there. Apply
  the rhythm checks to PROSE sections (intros, chapter narrative, tips),
  not to numbered step blocks.
- Never label any book "AI-detection proof" or similar; that claim is
  both unverifiable and unnecessary.

## Records

Write each chapter's editorial result (verdict + key metrics) to the
chapter's review record, and the release-QC sweep result to the project's
QA log. WARN items that were consciously accepted are recorded with a
one-line reason.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
