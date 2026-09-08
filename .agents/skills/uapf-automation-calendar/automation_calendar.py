#!/usr/bin/env python3
"""
AUTOMATION CALENDAR - uapf-automation-calendar
==============================================
File-backed recurring-job scheduler for the publishing feedback loop.
No daemons: Genie checks `status` at every session start and runs due
jobs between production tasks. Tier-aware: a job whose skill folder is
not installed in this pack is shown as "not in this pack" and never due.

Usage:
  python automation_calendar.py status            # what is due (run at session start)
  python automation_calendar.py done <job_id>     # stamp a job complete today
  python automation_calendar.py init              # (re)create missing default jobs
State: state/automation_schedule.json
"""
import datetime, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
STATE = os.path.join(ROOT, "state", "automation_schedule.json")
SKILLS = os.path.join(ROOT, ".agents", "skills")

DEFAULT_JOBS = [
    {"id": "weekly-review-sweep", "skill": "uapf-review-monitor", "every_days": 7,
     "what": "Sweep reviews on all published books; mine complaints; open correction tickets."},
    {"id": "weekly-sales-ingest", "skill": "uapf-royalty-reporter", "every_days": 7,
     "what": "Ingest latest KDP sales/KENP report (operator downloads or stays logged in); update per-book P&L actuals."},
    {"id": "biweekly-price-test-review", "skill": "uapf-launch-manager", "every_days": 14,
     "what": "Review running price tests against their measurement windows; conclude or extend; propose next test."},
    {"id": "weekly-ads-optimization", "skill": "uapf-ads-manager", "every_days": 7,
     "what": "For each book running ads: operator exports the search-term report; ads_analyzer.py produces the harvest/negate/bid action list against the book's break-even; safe actions applied, spend actions proposed for confirmation."},
    {"id": "monthly-seasonal-snapshot", "skill": "uapf-kdp-niche-specialist", "every_days": 30,
     "what": "Snapshot seasonal keyword positions into state/keyword_seasonal/; flag rising seasons 60-90 days out."},
    {"id": "monthly-catalog-calendar", "skill": "uapf-catalog-strategist", "every_days": 30,
     "what": "Refresh the what-to-publish-next calendar from catalog performance and niche signals."},
    {"id": "quarterly-backlist-sweep", "skill": "uapf-backlist-optimizer", "every_days": 90,
     "what": "Full backlist audit: metadata refresh, category checks, staleness flags, second-edition triggers."},
]

def load():
    if os.path.exists(STATE):
        return json.load(open(STATE, encoding="utf-8"))
    return {"jobs": []}

def save(d):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    json.dump(d, open(STATE, "w", encoding="utf-8"), indent=2)

def ensure_defaults(d):
    have = {j["id"] for j in d["jobs"]}
    added = 0
    for j in DEFAULT_JOBS:
        if j["id"] not in have:
            d["jobs"].append({**j, "last_run": None})
            added += 1
    return added

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    d = load()
    today = datetime.date.today()

    if cmd == "init":
        n = ensure_defaults(d)
        save(d)
        print(f"calendar ready: {len(d['jobs'])} jobs ({n} added)")
        return

    if cmd == "done":
        if len(sys.argv) < 3:
            sys.exit("usage: automation_calendar.py done <job_id>")
        for j in d["jobs"]:
            if j["id"] == sys.argv[2]:
                j["last_run"] = today.isoformat()
                save(d)
                print(f"{j['id']}: stamped {today.isoformat()}, next due "
                      f"{(today + datetime.timedelta(days=j['every_days'])).isoformat()}")
                return
        sys.exit(f"unknown job id: {sys.argv[2]}")

    # status
    ensure_defaults(d)
    save(d)
    due, upcoming, unavailable = [], [], []
    for j in d["jobs"]:
        installed = os.path.isdir(os.path.join(SKILLS, j["skill"]))
        if not installed:
            unavailable.append(j)
            continue
        if j["last_run"] is None:
            due.append((j, "never run"))
            continue
        last = datetime.date.fromisoformat(j["last_run"])
        overdue = (today - last).days - j["every_days"]
        if overdue >= 0:
            due.append((j, f"last run {j['last_run']}, {overdue}d overdue"))
        else:
            upcoming.append((j, (last + datetime.timedelta(days=j["every_days"])).isoformat()))
    if due:
        print(f"DUE ({len(due)}):")
        for j, note in due:
            print(f"  {j['id']:28} [{j['skill']}] {note}\n"
                  f"    -> {j['what']}")
    else:
        print("DUE (0): nothing due today.")
    for j, nxt in sorted(upcoming, key=lambda x: x[1]):
        print(f"  next {nxt}: {j['id']}")
    for j in unavailable:
        print(f"  (not in this pack: {j['id']} needs {j['skill']})")
    sys.exit(0)

if __name__ == "__main__":
    main()
