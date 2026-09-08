---
name: uapf-background-blocker-manager
description: Classify, queue, retry, and resolve UAPF blockers without stopping unrelated work. Use whenever a task cannot immediately pass.
---

1. Read `framework/BACKGROUND_BLOCKER_HANDLING.md`.
2. Classify the blocker as A, B, or C.
3. For Class A, repair and retest immediately.
4. For Class B, add a structured item to `state/blocker-queue.json`, quarantine
   only the affected task, and continue all independent work.
5. Retry Class B items after each major phase and before final QA.
6. For Class C, continue any remaining independent work before stopping.
7. Never hide, falsify, or mark an unresolved blocker as passed.
8. Include unresolved items in the release-readiness report.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
