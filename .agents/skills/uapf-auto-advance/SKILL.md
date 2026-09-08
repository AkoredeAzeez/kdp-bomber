---
name: uapf-auto-advance
description: The DEFAULT autopilot loop for all chapter and phase transitions (always on, operator directive 2026-08-18). After delivering each chapter preview in BOTH DOCX and PDF, Genie immediately continues to the next chapter or phase without waiting for PROCEED and without ever asking the operator whether to continue.
---

# UAPF Auto-Advance​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

## Purpose

AUTO-ADVANCE is the **default, always-on** behavior for every manuscript session (operator directive 2026-08-18, from a client complaint that Genie kept asking to move on). It is NOT a mode the operator switches on; it is how Genie always builds a book. Every "Type Proceed" gate at a chapter or phase boundary is self-approved. Genie NEVER asks "shall I continue?", "ready for the next chapter?", or any equivalent. After Genie delivers the chapter preview in BOTH formats, DOCX and PDF (via SendUserFile or clickable file links; operator directive 2026-08-14), it records the advance in the decision log and immediately begins the next chapter or phase. Delivering both files is mandatory and is never skipped; the preview renders with the full premium color design so the operator can spot issues while the next chapter is being drafted.

The loop runs from the first chapter to the last with no activation phrase and no pauses, and only stops if the operator says **"pause auto-advance"** or an always-on hard gate (below) is hit. Pausing to ask the operator whether to proceed is itself a production failure.

---

## Scope

AUTO-ADVANCE applies to:

| Gate type | Behavior |
|---|---|
| "Type Proceed to begin Chapter N" | Log and skip — start Chapter N immediately |
| "Type Proceed to begin [Phase]" | Log and skip — enter the phase immediately |
| "Type Proceed to generate the Table of Contents" | Log and skip |
| "Type Proceed to begin the Front Matter" | Log and skip |
| "Type Proceed to begin Chapter 1" after Front Matter | Log and skip |
| Any chapter-to-chapter "Type Proceed" gate | Log and skip |
| Correction-window close before next chapter | Do NOT block — continue drafting next chapter in parallel |

---

## What Auto-Advance Does NOT Bypass

The following gates always require explicit operator action regardless of AUTO-ADVANCE status:

- **HIGH RISK trademark finding** — pipeline stops; safer alternatives presented for operator choice
- **Catastrophic content or safety block** — halted pending review
- **KDP policy violation flagged in QC** — correction required before continuing
- **Any action that spends money** — ad spend, paid promotions, price changes (require operator confirmation with exact amount)
- **Any publishing action** — final Publish click on KDP/other platforms requires per-book per-platform operator confirmation
- **Credential or payment entry** — always operator-only, never Genie
- **Operator-explicitly-paused mode** — if operator says "pause auto-advance," stop at the very next gate and wait

---

## Execution Flow

```
Chapter N complete → Gates pass → Preview DOCX + PDF built → SendUserFile (BOTH files delivered)
  → Decision log: "AUTO-ADVANCE: Chapter N preview (DOCX + PDF) delivered — proceeding to Chapter N+1"
  → Open CORRECTION WINDOW: OPEN for Chapter N (corrections accepted asynchronously)
  → Immediately begin research and drafting for Chapter N+1
  → If correction arrives: apply to Chapter N in rolling DOCX while N+1 continues
```

---

## Decision Log Format

At every skipped gate, write exactly this line in the project decision log:

```
AUTO-ADVANCE: [Gate name] — proceeding to [next chapter / phase] without waiting. [2026-MM-DD]
```

Example:
```
AUTO-ADVANCE: Chapter 3 preview delivered — proceeding to Chapter 4 without waiting. 2026-08-04
```

---

## Activation

None required. AUTO-ADVANCE is ON by default for every manuscript session, from the first chapter, on both engines. There is nothing to invoke. The phrases **"run on autopilot"** / **"proceed automatically"** / **"don't wait between chapters"** only reaffirm the default; they are never needed to get continuous production.

---

## Session Persistence

Because it is the default, AUTO-ADVANCE is in force in every session automatically, including on resume: a new session picks up the manuscript and keeps building chapter after chapter without waiting. The only thing that changes the default is an explicit operator pause (below), which may be recorded in `state/session-flags.md` so a resumed session honors it.

## Suspension

Operator says: **"pause auto-advance"** → Genie stops at the very next chapter/phase boundary and waits.
Operator says: **"resume auto-advance"** → continuous production resumes immediately.
This is the ONLY operator-driven way to make Genie wait between chapters; absent an explicit pause, Genie always continues on its own.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
