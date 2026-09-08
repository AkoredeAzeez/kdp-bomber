---
name: uapf-autonomous-full-pipeline
description: Run a complete UAPF book project from title through research, manuscript, rolling DOCX, QA, images, back-matter references, and KDP handoff assets on autopilot without waiting at routine approval gates.
---

1. Read the root instructions, autopilot requirements, background blocker rules,
   autonomous override, execution contract, and relevant Master sections.
2. Require and record the minimum operator inputs: title/topic, marketplace,
   language, target pages per chapter, and maximum total page count.
3. Create the project with `python scripts/new_book.py --title "<title>"`.
4. Persist the operator brief and supplied-file inventory.
5. Execute Phases 0–VII in order.
6. Auto-approve routine gates only after checks pass.
6b. BUILD CHAPTER BY CHAPTER, NEVER ALL AT ONCE (binding operator rule
    2026-08-14): produce exactly one chapter at a time. After each chapter
    passes its gates and before the next chapter begins, deliver the
    completed chapter preview as BOTH a DOCX and a PDF download, rendered
    with the full premium color design so the operator can check it for
    issues, then automatically move to the next chapter. AUTO-ADVANCE IS THE
    DEFAULT (operator directive 2026-08-18): deliver both files and continue
    to the next chapter IMMEDIATELY, without waiting and without EVER asking
    the operator whether to proceed. Genie never emits a "Type Proceed" /
    "Continue?" / "ready for the next chapter?" gate; it just keeps building
    to the end. It never skips the dual delivery. Drafting multiple chapters
    in one pass, delivering chapters in a batch, or pausing to ask whether to
    continue is a production failure. Only an explicit "pause auto-advance"
    or an always-on hard gate (trademark/policy/money/Publish/credentials)
    stops the loop.
7. Repair Class A blockers automatically.
8. Queue Class B blockers and continue all independent work.
9. Stop only for a Class C blocker after no meaningful work remains.
10. Produce an Introduction of approximately 2–3 rendered pages.
11. Keep all `SRC-####` identifiers out of reader-facing content.
12. Build references in back matter without internal IDs.
13. Keep one rolling DOCX and versioned source files.
14. Preserve image prompt files after image generation.
15. After all chapters are merged and reviewed, if the project contains image slots
    ([IMG-XX] placeholders), generate `image_manifest.md` and `cowork_image_task.md`
    in the project folder using the format documented in the uapf-flow-image-pipeline
    skill. Then run the Google Flow image pipeline:
    ```
    python "$env:LOCALAPPDATA\FlowPipeline\flow_book_images.py" "<project_folder>"
    ```
    Prerequisite: Chrome must be open at labs.google/fx/tools/flow with the operator
    logged in. If Chrome is not reachable, treat as a Class B blocker — continue
    back matter and KDP assets — then report the pipeline command to the operator
    at the end so they can run it manually.
16. Verify the final DOCX has zero remaining [IMG-XX] placeholders before marking
    the project complete.
17. Persist exact progress before any run ends.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
