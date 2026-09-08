---
name: uapf-codex-failover
description: Codex is Genie's SECONDARY / FAILOVER production agent behind Claude Code (the primary). Use to consult Codex for review/validation via MCP while Claude is available, and to hand production off to Codex automatically when Claude hits a usage or rate limit, then hand back to Claude when it returns. Extends Genie's existing project state; does not replace it.
---

# UAPF Codex Failover​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

```
GENIE  (the overall system, unchanged)
├── Claude Code — PRIMARY  production agent
└── Codex       — FAILOVER production agent
```

Genie stays the system. Claude Code is preferred and primary. Codex is the backup that
keeps production moving when Claude cannot. Codex is never the main orchestrator, and there
is never a second Genie. Both agents use the **same** framework and the **same** authoritative
project state; there is no Claude-only or Codex-only version of any framework.

Controller: `genie_failover.py` (this skill folder). Config: `failover_config.json`.

## Two Codex pathways

### Path 1 — Claude → Codex (MCP): consult while Claude is available
While Claude Code is running, it can consult Codex directly for second opinions, independent
review, validation, debugging, framework analysis, hard reasoning, and QA. Codex runs as a
project-scoped MCP server, configured in `<genie>/.mcp.json`:
```json
{ "mcpServers": { "codex": { "command": "codex", "args": ["mcp-server"] } } }
```
This is equivalent to `claude mcp add --scope project codex -- codex mcp-server`. No
credentials are stored here; Codex handles its own auth. To enable and verify (once the
Codex CLI is installed):
```
codex --version
codex mcp-server            # confirms Codex can serve MCP
claude mcp list             # codex should be listed
claude mcp get codex        # shows the project-scoped server
```
Then Claude can call Codex through the `codex` MCP tools for a review/second opinion.

### Path 2 — Genie → Codex (direct exec): emergency failover
MCP is not enough for failover: once Claude hits its usage limit it may be unable to call
anything. So **Genie**, not Claude, launches Codex directly and non-interactively:
```
codex exec --sandbox workspace-write --skip-git-repo-check --cd "<project_dir>" --json  < prompt-on-stdin
```
A restricted `workspace-write` sandbox is used (not unrestricted access); `--skip-git-repo-check`
is required because Genie project dirs are not their own git repos; the prompt is fed on stdin;
and `--json` (JSONL events) is parsed for the agent's final structured result. Verified live:
Codex writes the unit and returns the `{"status":"completed",...}` result the controller validates. Claude does NOT need to initiate this. The controller builds the
continuation prompt entirely from disk state, so Codex needs no chat history.

## Shared authoritative state (extends the existing model)
Genie already uses `project.json` + `state/` + `chapters/`. This skill adds ONE file,
`state/agent_state.json`, holding the fields needed to resume from disk alone. It reuses
existing values (framework/niche from `project.json`, next action mirrored to
`state/next_action.md` for `generate_handoff.py`) and does not duplicate them:

- project_id, framework, framework_version, locked_decisions
- current_phase, current_chapter, current_section
- last_completed_item, next_unfinished_item, completed_items
- files_modified, validation_status
- active_production_agent, agent_available, handoff_reason
- last_valid_checkpoint

The authoritative state always wins over either agent's memory.

## Niche classification lock (existing router → Codex)
The niche is chosen ONLY by the existing `uapf-phase0-router` and persisted by the existing
niche skills (`book_lock.md` ROUTING/BOOK LOCK, or `project.json`). The controller does not
classify, re-route, or duplicate niche metadata. It only READS the existing record and carries
the locked decision to Codex:
- `parse_book_lock` reads the project's `book_lock.md`; `router_overlay_map` reads the overlay→
  skill table live from `uapf-phase0-router/SKILL.md` (single source of truth). `resolve_niche`
  maps the already-chosen overlay (e.g. `OV-COOK`) to its skill (`uapf-niche-cookbook`) — a
  lookup of a made decision, never a new classifier.
- `_apply_classification` folds that into the shared state as `overlay`, `primary_niche`,
  `selected_skill`, `niche_skill_path`, `title`, `framework`/`framework_version`, and sets
  `classification_locked` / `framework_locked` (reusing existing field names; adding only the
  minimal lock fields). It never overwrites a value already set explicitly.
- The handoff prompt tells Codex the classification is LOCKED — do NOT run Phase 0, re-detect,
  re-route, or pick a different niche/framework; only the operator may order reclassification —
  and points Codex to READ the SAME shared files Claude uses: the selected `uapf-niche-*/SKILL.md`,
  `book_lock.md`, `uapf-global-rules/SKILL.md`, and `state/agent_state.json`. One source of truth
  feeds both agents. **Verified live:** Codex under `--cd <project>` + `workspace-write` can read
  a niche SKILL.md by absolute path outside the project dir, so no compiled/duplicate framework is
  needed. (`stage_failover_packet` staging a verbatim in-project copy remains available as a
  fallback for locked-down sandboxes; not used by default.)
- **Preflight guard:** a real failover REFUSES to run Codex if no niche skill can be resolved
  from the existing records (returns `CLASSIFICATION_UNRESOLVED` + a blocker, audits
  `FAILOVER_BLOCKED`), so Codex is never handed a book without its locked framework. Legacy/
  hand-authored records that carry a profile code (e.g. `CB-PIC`) instead of an `OV-` code are
  resolved via a small profile→overlay alias grounded in the children's skill's own taxonomy.
  The permanent fix — the router/niche skills emitting an explicit `OV-`/`selected_skill` line
  into `book_lock.md` — is deferred until niche-content edits are authorized.

## Handoff rule (Claude → Codex)
When Claude hits a usage or rate limit, Genie runs:
```
python genie_failover.py failover --project "<project_dir>" --error "<claude error text>"
```
which: preserves valid on-disk work, checkpoints, marks Claude unavailable and records why,
assigns Codex, hands Codex the project dir + shared framework + locked decisions + the exact
next unfinished unit, tells Codex not to regenerate completed work, runs Codex, validates the
structured result, updates shared state, and keeps checkpointing. Codex must treat the files
and `state/agent_state.json` as authoritative and must never guess where Claude stopped from
prose or chat.

## Hand-back rule (Codex → Claude)
When Claude is available again it must resume from **state**, not from its old chat position.
Example: Claude did 1–82, hit its limit, Codex did 83–117. On return Genie tells Claude
"last verified: 117, next: 118" and Claude starts at 118, never at 83. Codex first finishes
its current atomic unit, saves, validates, and checkpoints, then:
```
python genie_failover.py handback --project "<project_dir>"
```

## Agent locking
Only one agent holds WRITE ownership of a production unit at a time (`state/locks/<unit>.lock`).
`advance` refuses to write a unit locked by the other agent. Read-only review by the other
agent is allowed. Claude and Codex can never both write the same chapter/unit.

## Failure classification and policy
`classify_error` maps Claude errors to: USAGE_LIMIT, RATE_LIMIT, AUTH_ERROR, NETWORK_ERROR,
TOOL_ERROR, VALIDATION_ERROR, UNKNOWN_ERROR. Not every error triggers Codex. Automatic
takeover fires only for the classes in `failover_config.json`:
```json
{ "primary_agent": "claude", "failover_agent": "codex",
  "return_to_primary": true, "auto_failover_on": ["USAGE_LIMIT", "RATE_LIMIT"],
  "executables": { "claude": "auto", "codex": "auto" } }
```
`executables` controls how each CLI is located: `"auto"` detects it (PATH, then the WinGet
package dir) so the controller works even when the caller's shell lacks it on PATH; set an
explicit absolute path instead to pin a specific binary.
`return_to_primary: true` means control returns to Claude when it is back — but Codex is
never interrupted mid-unit; it finishes the current unit, saves, validates, checkpoints, then
hands back.

## Structured Codex result
Codex returns, and Genie validates before advancing state:
```json
{ "status": "completed", "agent": "codex", "project_id": "...", "task": "...",
  "completed_units": [], "last_completed_unit": "...", "next_task": "...",
  "files_modified": [], "validation_notes": [], "blockers": [] }
```

## Audit log
`state/audit_log.jsonl` records CLAUDE_TASK_STARTED/COMPLETED, CLAUDE_USAGE_LIMIT,
FAILOVER_STARTED, CODEX_TASK_STARTED/COMPLETED/FAILED, CLAUDE_AVAILABLE, HAND_BACK_TO_CLAUDE.
No authentication secrets are ever logged.

## Health check
```
python genie_failover.py health --project "<project_dir>"
```
Reports whether the Claude CLI, Codex CLI, and `codex mcp-server` are available, whether Claude
sees the Codex MCP, whether direct `codex exec` is available, whether shared state and the
current framework load, that the controller is ready, and that primary=claude, backup=codex.
No secrets are shown.

## Self-test
```
python genie_failover.py selftest
```
Runs the controlled 10-unit handoff (Claude 1–5 → simulated usage limit → Codex 6–8 →
Claude restored → Claude 9–10) and asserts: units 1–10 present, 0 missing, 0 duplicates,
correct order, Claude→Codex and Codex→Claude continuity, and locked config unchanged.

## Confidentiality (both engines, every sandbox)
Global rule #13 (confidentiality of construction) binds Codex exactly as it
binds Claude, in every session and sandbox mode INCLUDING danger-full-access.
The Community Edition has no licensing, activation, or kill switch; a Codex
session never simulates or demands one. The full-access sandbox exists to run
Genie's own finishers and QA gates on Genie-generated artifacts.

## Formatting standard (both engines)
Every Codex-produced manuscript, interior, cover, wrap, and A+ asset follows
**uapf-formatting-standard** (the consolidated master formatting standard,
operator directive 2026-08-13) exactly as a Claude-produced one does: same
universal rules, PREMIUM/PROFESSIONAL/HIGH-GRADE bar, per-niche interior
specs, production sequences, and the final preflight checklist. Precedence:
locked framework, approved TOC, exact counts, and explicit project
instructions override its general defaults.

**Render-QA duty under Codex (self-contained via the two-phase security
split, operator directive 2026-08-13).** The premium bar is verified on the
RENDERED page (`uapf-quality-gates/render_qa.py` + page-by-page PDF
inspection). Production runs use the designer skill's two-phase split:
generation in `--sandbox workspace-write` (the phase that reads third-party
reference content stays mechanically fenced; the native image tool works
there), then finishing + render QA in `--sandbox danger-full-access` on
GENIE-GENERATED ARTIFACTS ONLY (the workspace-write sandbox blocks Python
on this machine, verified 2026-08-13, so the gates run in the full-access
phase). Full access is never combined with third-party or external inputs
in one session. If a session is sandbox-restricted and the gate cannot run
(try `py` and the absolute interpreter path first), mark the unit
`render_qa_pending` in the state file and report it, never marking the book
or chapter COMPLETE; the pending gate runs on handback or by the operator.
A missing gate is a blocker, never a silent pass.

## Interior images (agent-specific)
Interior photos follow the producing agent: **Claude Code uses Google Flow; Codex uses ChatGPT
Image 2.0 (gpt-image-2)** — its native OpenAI-ecosystem image tool. Covers, A+, and labeled maps
stay ChatGPT Image 2.0 for both. Codex writes each interior image as a numbered slot + prompt in
`image_manifest.md`.

**Codex premium image tool (covers, A+, interiors):**
Codex carries **gpt-image-2 (ChatGPT Image 2.0) as a NATIVE tool** in its ChatGPT account
session — no browser, no API key, no separate billing. The permanent family-safe content
guard applies to every prompt. (`CodexBookStudio/scripts/openai_image.py` remains the
scripted alternate for sessions where the native tool is unavailable; it needs
`OPENAI_API_KEY`.) **Covers are IMMEDIATE (operator directive 2026-08-13):** the moment a Codex-produced manuscript passes release QC and its metadata DOCX
exists, Codex runs the full cover + A+ pipeline itself via the "Codex execution path" in
uapf-cover-aplus-designer (cover_db refs -> comprehensive block-letter photoreal prompt ->
openai_image.py -> local cover_wrap.py --finish -> QA gate). Cover work is never deferred to
wait for a browser. Only browser-dependent steps (live Amazon research, cover_db seeding, the
ChatGPT web project) still wait for the operator or Claude.

### Free headless fallback during a Claude limit (Option A)
Only when BOTH premium paths are unavailable (native gpt-image-2 tool absent from the session
AND no `OPENAI_API_KEY` for openai_image.py) may Codex generate PLACEHOLDER-grade images
headlessly and free via `genie_image_fallback.py`:
```
python genie_image_fallback.py --project "<dir>" --slot IMG-Rnn --out units/IMG-Rnn.png --prompt "<image prompt>"
python genie_image_fallback.py --project "<dir>" --list-regen     # pending premium regens
```
It calls the free Z-Image Turbo Gradio space (`pip install gradio_client`; no browser, no API key,
no cost) and logs every image to `state/image_regen_queue.jsonl` with `needs_premium_regen:true`.
These are NEVER final: when a browser driver returns, the queued slots MUST be regenerated at
premium quality (ChatGPT Image 2.0 for Codex chapters, Google Flow for Claude chapters), then the
DOCX re-assembled. See [[feedback-flow-only-images]]. This is the only sanctioned non-Flow/
non-ChatGPT generator, and only under this limit-time-fallback-with-mandatory-regen rule.

## Codex intake + trademark gate (TOTAL Claude outage)
Normally Codex never runs Phase 0. The ONE exception is a total Claude outage where the operator
still needs to START new books. Then Codex may do a PROVISIONAL intake -- but it never clears a
title, and nothing ships until the trademark is verified off-Claude.
```
python genie_failover.py intake --project "<dir>" --title "<book title>"      # Codex classifies -> provisional book_lock (trademark UNVERIFIED)
python genie_failover.py trademark-prompt --title "<book title>"              # paste into ChatGPT (browsing) to run the screen
python genie_failover.py set-trademark --project "<dir>" --status CLEARED --by "operator (ChatGPT)" --note "GREEN ..."
python genie_failover.py ratify --project "<dir>" --by operator               # accept/confirm the provisional niche
python genie_failover.py publish-ready --project "<dir>"                      # gate: publish BLOCKED until trademark CLEARED
```
- `intake`: Codex reads the router table + niche skills, classifies the title into overlay/skill/
  framework, and writes a PROVISIONAL `book_lock.md` (`classification_provisional=true`,
  `title_status=UNVERIFIED`, `trademark_status=UNVERIFIED`). Codex MUST NOT do trademark/market web
  research -- it cannot clear a title.
- Codex then writes the manuscript normally (content carries no trademark risk).
- **Trademark is a HARD PUBLISH GATE.** `publish-ready` refuses publish unless `trademark_status=CLEARED`.
  The screen is run off-Claude -- by the operator manually (Amazon + USPTO TESS + Google) or via the
  `trademark-prompt` fed to ChatGPT (browsing) -- and recorded with `set-trademark`. Genie's verdict
  is a preliminary risk screen, not legal clearance; the operator is responsible and Publish is always
  operator-confirmed. A provisional niche is a warning (affects format, not legality); confirm with
  `ratify`. See [[codex-failover]].

## Hard rules
- Do not make Codex the orchestrator; Genie is the system and Claude is primary.
- Both agents share ONE framework and ONE authoritative state.
- Never store or log credentials.
- Never let both agents write the same unit; the lock is authoritative.
- The Codex CLI must be installed and signed in by the operator for the live paths; the
  controller degrades gracefully (reports `unavailable`) when it is not.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
