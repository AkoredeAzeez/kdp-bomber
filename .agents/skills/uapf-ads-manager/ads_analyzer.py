#!/usr/bin/env python3
"""
ADS ANALYZER - uapf-ads-manager
===============================
Ingests an Amazon Ads search-term report (CSV exported by the operator from
advertising.amazon.com) and applies the ads skill's OWN optimization rules
mechanically, producing a ranked action list and a weekly-report draft.

Reads real numbers only; invents nothing. Every action that could spend money
(bid up, harvest into a paid campaign) is emitted as a PROPOSAL for the
operator to confirm; spend-reducing actions (negate, bid down, pause) are safe
to apply and are still logged.

Rules applied (from SKILL.md):
  HARVEST : search term with >=1 order and ACOS <= break-even -> add exact match
            to the performance campaign, negate-exact in the source campaign.
  NEGATE  : clicks > 10 and 0 orders -> negative-exact.
  WATCH   : 5-10 clicks and 0 orders -> bid down, watch one more week.
  BID UP  : has orders and ACOS below the phase target band -> +10-20%.
  BID DOWN: has orders and ACOS above the phase target band -> -10-20%.

Usage:
  python ads_analyzer.py <report.csv> --royalty 4.23 --price 14.99
         [--phase launch|transition|profit] [--project <folder>]
"""
import argparse, csv, os, sys, datetime

# tolerant column matching: Amazon renames columns across report types
COLS = {
    "term":   ["customer search term", "search term", "targeting", "keyword text", "customer search term "],
    "camp":   ["campaign name", "campaign"],
    "impr":   ["impressions"],
    "clicks": ["clicks"],
    "spend":  ["spend", "cost"],
    "orders": ["7 day total orders (#)", "orders", "14 day total orders (#)", "total orders (#)", "7 day total orders"],
    "sales":  ["7 day total sales", "sales", "14 day total sales", "total sales", "7 day total sales "],
}

def find(headers, keys):
    low = {h.lower().strip(): h for h in headers}
    for k in keys:
        if k in low:
            return low[k]
    # loose contains-match fallback
    for k in keys:
        for h_low, h in low.items():
            if k in h_low:
                return h
    return None

def num(v):
    if v is None:
        return 0.0
    s = str(v).replace(",", "").replace("$", "").replace("%", "").strip()
    try:
        return float(s) if s else 0.0
    except ValueError:
        return 0.0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--royalty", type=float, required=True)
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--phase", choices=["launch", "transition", "profit"], default="transition")
    ap.add_argument("--project", default=".")
    a = ap.parse_args()

    be = a.royalty / a.price
    # phase target ceiling (ACOS at or below this is "good" for the phase)
    ceiling = {"launch": be * 1.75, "transition": be * 1.05, "profit": be * 0.70}[a.phase]

    rows = []
    with open(a.report, encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        H = rd.fieldnames or []
        col = {k: find(H, v) for k, v in COLS.items()}
        if not col["term"] or not col["clicks"]:
            sys.exit(f"could not find search-term/clicks columns in {H}")
        for r in rd:
            term = (r.get(col["term"]) or "").strip()
            if not term:
                continue
            clicks = num(r.get(col["clicks"]))
            spend = num(r.get(col["spend"]))
            orders = num(r.get(col["orders"]))
            sales = num(r.get(col["sales"]))
            impr = num(r.get(col["impr"]))
            camp = (r.get(col["camp"]) or "").strip() if col["camp"] else ""
            acos = (spend / sales) if sales > 0 else None
            rows.append(dict(term=term, camp=camp, impr=impr, clicks=clicks,
                             spend=spend, orders=orders, sales=sales, acos=acos))

    harvest, negate, watch, bid_up, bid_down = [], [], [], [], []
    tot_spend = tot_sales = tot_orders = 0.0
    for r in rows:
        tot_spend += r["spend"]; tot_sales += r["sales"]; tot_orders += r["orders"]
        if r["orders"] >= 1 and r["acos"] is not None:
            if r["acos"] <= be:
                harvest.append(r)
            elif r["acos"] <= ceiling:
                bid_up.append(r)
            else:
                bid_down.append(r)
        elif r["clicks"] > 10 and r["orders"] == 0:
            negate.append(r)
        elif 5 <= r["clicks"] <= 10 and r["orders"] == 0:
            watch.append(r)

    blended = (tot_spend / tot_sales) if tot_sales > 0 else None
    date = datetime.date.today().isoformat() if hasattr(datetime.date, "today") else "today"

    def block(title, items, action, money):
        if not items:
            return ""
        tag = "  [PROPOSE - operator confirms spend]" if money else "  [safe - reduces/contains spend]"
        out = [f"\n{title} ({len(items)}){tag}"]
        for r in sorted(items, key=lambda x: -(x["spend"])):
            ac = f"{r['acos']*100:.0f}%" if r["acos"] is not None else "n/a"
            out.append(f"  {action}: \"{r['term']}\"  | clicks {r['clicks']:.0f} orders {r['orders']:.0f} "
                       f"spend {r['spend']:.2f} sales {r['sales']:.2f} ACOS {ac}"
                       + (f"  (from {r['camp']})" if r['camp'] else ""))
        return "\n".join(out)

    report = []
    report.append(f"ADS ANALYZER REPORT  |  {date}")
    report.append(f"Book royalty {a.royalty:.2f} / price {a.price:.2f}  ->  break-even ACOS {be*100:.1f}%  |  phase: {a.phase} (target ceiling {ceiling*100:.0f}%)")
    report.append(f"Totals in this report: spend {tot_spend:.2f} | sales {tot_sales:.2f} | orders {tot_orders:.0f} | "
                  + (f"blended ACOS {blended*100:.1f}% ({'PROFIT' if blended and blended<be else 'above break-even'})" if blended else "no attributed sales yet"))
    report.append(block("HARVEST -> add exact match to performance campaign, negate-exact in source", harvest, "harvest", True))
    report.append(block("BID UP (has orders, ACOS below phase target) -> +10-20%", bid_up, "bid up", True))
    report.append(block("BID DOWN (has orders, ACOS above phase target) -> -10-20%", bid_down, "bid down", False))
    report.append(block("NEGATE (>10 clicks, 0 orders) -> negative-exact", negate, "negate", False))
    report.append(block("WATCH (5-10 clicks, 0 orders) -> bid down, review next week", watch, "watch", False))
    report.append("\nEvery HARVEST and BID UP is a proposal: confirm the exact bids before applying.")
    report.append("NEGATE / BID DOWN / WATCH reduce or contain spend and may be applied, then logged.")
    text = "\n".join(x for x in report if x)

    out_dir = os.path.join(os.path.abspath(a.project), "advertising")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"ads-analysis-{date}.md")
    open(out_path, "w", encoding="utf-8").write(text + "\n")
    print(text)
    print(f"\n[written: {out_path}]")

if __name__ == "__main__":
    main()
