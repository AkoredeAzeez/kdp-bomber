---
name: uapf-daily-standup
description: Genie's morning report to the Pegasus Press operator — production status, publishing gates, market signals, ads summary, and today's plan in one tight, scannable page with every number sourced and dated.
---

# UAPF Daily Standup​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

One page, every morning: what's moving, what the numbers say, what's waiting on the operator, and what Genie will do today. The standup is a **report**, not a work session — it reads existing state and presents it honestly.

## When to Run

| Trigger | Behavior |
|---|---|
| Operator says "Genie, standup" (or similar) | Produce the report immediately |
| Scheduled morning run | Produce the report and present it as the day's opener |
| Operator asks "what's blocked?" / "what needs me?" | Produce at minimum the NEEDS-DECISION section |

## Data Gathering

Collect from existing records only. Each item notes its source file and the date of the data.

### 0. Environment

The Community Edition has no license or integrity check; nothing runs here.
If `state/environment.json` reports a MISSING tool (Codex CLI, DOCX-to-PDF
converter), list it once under ENVIRONMENT, never as a headline.

### 1. Production Status

For every active project (from project state files / orchestrator records):

- Current framework and phase (research, TOC, drafting, formatting, QC, cover, publish prep)
- Chapters done / total; gates passed (chapter-format audits, release QC)
- Open blockers from the blocker queues, with age

### 2. Publishing Status

- Books sitting at a **confirmation gate** (upload, re-upload, live-listing change) waiting on the operator
- Books submitted and currently **in platform review** at KDP, with days elapsed
- Recently gone live (since last standup)

### 3. Market Signals

- BSR moves from the most recent WATCHLIST snapshots (uapf-kdp-niche-specialist)
- New reviews and any new correction tickets (uapf-review-monitor)
- **Only if fresh data exists.** If snapshots are stale, label them stale with their date. The standup **may refresh watchlists itself** when data is stale and time permits — but never delays the report significantly to do so; report stale-and-labeled rather than late.

### 4. Ads Summary

- Only if the ads log (uapf-ads-manager) has entries since the last standup: spend, clicks/orders if recorded, and any campaign state changes. Otherwise the section says "nothing new."

### 5. Today's Plan

- Next concrete action per active project
- Decisions currently waiting on the operator (these also headline the report)
- Scheduled sweeps due today (review sweep, backlist sweep, royalty pull)

## Report Format

Lead with whatever is **blocked on the operator** — that is the most valuable line in the report. Then:

```
GENIE STANDUP — [date]

NEEDS-DECISION
1. [decision] — waiting since [date] — [what unblocks]
(if none: "Nothing waiting on you.")

STATUS
- [Project A]: [phase], ch [x/y], gates [..], blockers [..]
- [Book B]: in KDP review, day 2 (submitted 2026-08-01)

NUMBERS
- [Book C] BSR 41,230 -> 33,871 (watchlist 2026-08-02)
- [Book D] new review 5* (reviews file, 2026-08-01)
(each number: source file + date; stale data marked STALE [date])

TODAY
- [Project A]: draft ch 5, run chapter audit
- Refresh watchlist for [niche] (stale since 2026-07-20)
```

### Formatting rules

| Rule | Detail |
|---|---|
| Length | Under one page unless the operator asks for detail |
| Order | NEEDS-DECISION first, always |
| Scannability | Short lines, one item per line, no prose paragraphs |
| Empty sections | Say "nothing new" — never pad, never invent |
| Numbers | Every figure carries source file + data date |
| Staleness | Data older than its expected refresh cadence is labeled STALE with its date |

## Honest-Data Rule

The standup's only value is that it can be trusted:

1. Every number cites the file it came from and the date of that data.
2. Stale data is presented, but labeled stale — not silently passed off as current.
3. Nothing is ever invented to make a section look complete. An empty section is reported as empty.
4. If a source file is missing or unreadable, the report says so in that section rather than guessing.
5. Estimates, when unavoidable, are explicitly marked as estimates with their basis.

## Workflow

1. Read project state, blocker queues, publishing gate records, latest watchlist snapshots, review files, and ads log — noting each file's date.
2. Optionally refresh stale watchlists if the operator isn't waiting and time permits; otherwise mark STALE.
3. Assemble the report in the format above, decisions first.
4. Deliver it. If the operator responds to a NEEDS-DECISION item, route the decision to the owning skill (uapf-publisher for upload gates, uapf-backlist-optimizer for listing changes, etc.).
5. Do not start executing today's plan inside the standup unless the operator says go.

## Key Rules — Do NOT Break

1. **Never fabricate a metric.** No number appears without a real source file and date behind it.
2. **Decisions-needed come first**, every time — the operator's blockers headline the report.
3. **Stale data is labeled stale**; empty sections say "nothing new." Padding a report is lying with formatting.
4. **Keep it under a page** unless the operator explicitly asks for the long version.
5. **The standup reports; it does not act** — except an optional watchlist refresh when data is stale and time permits. All other work waits for the operator's go.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
