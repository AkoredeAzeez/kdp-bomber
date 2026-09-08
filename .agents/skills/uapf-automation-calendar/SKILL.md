---
name: uapf-automation-calendar
description: The publishing feedback loop on a clock. File-backed recurring jobs (weekly review sweep, weekly sales ingest, biweekly price-test review, monthly seasonal keyword snapshot, monthly catalog calendar, quarterly backlist audit) checked at every session start and run between production tasks. Also owns the PRICE ELASTICITY TEST protocol. Invoke on "Genie, what's due", "Genie, run the weekly sweep", or automatically at session start.
---

# UAPF Automation Calendar (the always-on publishing loop)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

World-class publishing is a LOOP, not a line: publish, measure, adjust,
republish. This skill puts the measuring and adjusting on a clock without
any background daemon: state lives in `state/automation_schedule.json`,
and Genie simply checks it every session.

## Session-start law (binding, operator directive 2026-08-16)

At every session start, run:

```
python .agents/skills/uapf-automation-calendar/automation_calendar.py status
```

- Report DUE jobs in the standup/first status line.
- Run due jobs BETWEEN production tasks, exactly like cover-bank seeding:
  a due sweep never blocks an active book build, and an active book build
  never cancels a due sweep; it queues.
- After completing a job's work through its owning skill, stamp it:
  `python ... automation_calendar.py done <job_id>`.
- Jobs whose owning skill is not installed in this pack are shown as
  "not in this pack" and are never due (tier-aware by design).

## The jobs

| Job | Cadence | Owning skill | What happens |
|---|---|---|---|
| weekly-review-sweep | 7d | uapf-review-monitor | Review sweep, complaint mining, correction tickets |
| weekly-sales-ingest | 7d | uapf-royalty-reporter | Ingest the latest KDP report; update per-book P&L actuals |
| biweekly-price-test-review | 14d | uapf-launch-manager | Conclude/extend running price tests; propose the next |
| monthly-seasonal-snapshot | 30d | uapf-kdp-niche-specialist | Snapshot seasonal keywords; flag seasons 60-90 days out |
| monthly-catalog-calendar | 30d | uapf-catalog-strategist | Refresh the what-to-publish-next calendar |
| quarterly-backlist-sweep | 90d | uapf-backlist-optimizer | Full backlist metadata/category/staleness audit |

Sales ingest is honest about its dependency: KDP reports require the
operator's logged-in browser or a downloaded report file. If neither is
available this session, the job stays due and the standup says exactly
that; actuals are NEVER estimated (global no-fabrication rule).

## Price elasticity test protocol (PRICE TEST)

Prices are a lever most self-publishers never test. The protocol:

1. PROPOSE: pick one book, one variable (list price only), one step
   (for example 14.99 -> 12.99), a 14-day window, and the success metric
   (royalty per day, not units alone). Genie states the exact current
   price, test price, and projected margin per unit at both prices.
2. CONFIRM: any price change is a money action: the operator confirms
   the exact change before it is made (hard gate, all installs).
3. MEASURE: record daily orders/KENP from real report data across the
   window in `state/price_tests/<book>.json`. No mid-window changes.
4. DECIDE: at window end, keep whichever price earned more royalty per
   day; the revert (if losing) is also operator-confirmed. Record the
   conclusion in the book's decision log and the launch plan.
5. One live test per book at a time; never test during a launch week or
   a major promo (contaminated data).

## Engines and tiers

Binds BOTH engines, Claude and Codex alike. The Community Edition ships every
job's owning skill, so the full loop is active. The calendar itself never
spends money and never publishes; it routes work to skills that hold their
own hard gates.
(Starter has no research or publishing layer to schedule). On PRO, only
the seasonal snapshot job is active (the rest show "not in this pack");
the full loop runs on MAX. The calendar itself never spends money and
never publishes; it routes work to skills that hold their own hard gates.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
