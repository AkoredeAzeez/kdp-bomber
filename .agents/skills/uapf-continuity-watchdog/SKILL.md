---
name: uapf-continuity-watchdog
description: Maintain durable UAPF progress across long-running Codex turns and resumed sessions. Use at checkpoints, before a session ends, and when continuing an incomplete project.
---

1. Read `GOAL.md` and `framework/CONTINUITY_AND_RECOVERY.md`.
2. Read project state, task log, decisions, blocker queue, and completion criteria.
3. Continue from the first incomplete valid action; do not repeat passed work.
4. After every chapter and phase, persist outputs and update all state records.
5. Keep each completion criterion false until direct evidence supports it.
6. Run project validation and DOCX assembly after material manuscript changes.
7. Before completion, run `scripts/finalize_project.py` and then
   `scripts/project_status.py --json`.
8. If the session must end early, record the exact next command or action.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
