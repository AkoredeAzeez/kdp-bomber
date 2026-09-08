#!/usr/bin/env python3
"""
ADS MATH - uapf-ads-manager
===========================
Deterministic Amazon Ads math so break-even, target bands, and budget
planning are computed, never guessed. No money is spent by this tool; it
only produces numbers and recommendations the operator confirms.

  python ads_math.py breakeven --royalty 4.23 --price 14.99
  python ads_math.py bands --royalty 4.23 --price 14.99
  python ads_math.py budget --royalty 4.23 --price 14.99 --monthly 150
"""
import argparse, sys

def breakeven(royalty, price):
    if price <= 0:
        sys.exit("price must be > 0")
    return royalty / price

def phase_bands(be):
    # target ACOS bands by launch phase, expressed as multiples of break-even
    return {
        "Launch (days 1-30)":     (be * 1.5, be * 2.0, "buy velocity/reviews/rank; deliberately unprofitable"),
        "Transition (days 30-60)":(be * 0.95, be * 1.10, "ads wash their face while organic grows"),
        "Profit (day 60+)":       (be * 0.60, be * 0.80, "ads contribute margin"),
    }

def budget_plan(be, royalty, price, monthly):
    daily = monthly / 30.0
    # 4-campaign split: auto 25, broad 25, exact 30, product 20
    split = {"Auto (discovery)": 0.25, "Broad research": 0.25,
             "Exact performance": 0.30, "Product targeting": 0.20}
    rows = [(name, round(daily * frac, 2)) for name, frac in split.items()]
    # realistic outcome framing at launch band midpoint
    launch_acos = be * 1.75
    est_ad_sales = monthly / launch_acos if launch_acos > 0 else 0
    est_units = est_ad_sales / price if price > 0 else 0
    return daily, rows, launch_acos, est_ad_sales, est_units

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for c in ("breakeven", "bands", "budget"):
        p = sub.add_parser(c)
        p.add_argument("--royalty", type=float, required=True)
        p.add_argument("--price", type=float, required=True)
        if c == "budget":
            p.add_argument("--monthly", type=float, required=True)
    a = ap.parse_args()
    be = breakeven(a.royalty, a.price)

    if a.cmd == "breakeven":
        print(f"Break-even ACOS = royalty {a.royalty:.2f} / price {a.price:.2f} = {be*100:.1f}%")
        print("At this ACOS an ad sale exactly repays its own ad cost. Below it, ads profit.")
    elif a.cmd == "bands":
        print(f"Break-even ACOS: {be*100:.1f}%  (royalty {a.royalty:.2f} / price {a.price:.2f})")
        for name, (lo, hi, why) in phase_bands(be).items():
            print(f"  {name:26} target ACOS {lo*100:.0f}%-{hi*100:.0f}%  ({why})")
    else:
        daily, rows, lacos, sales, units = budget_plan(be, a.royalty, a.price, a.monthly)
        print(f"Break-even ACOS: {be*100:.1f}%")
        print(f"Monthly budget {a.monthly:.0f} -> ~{daily:.2f}/day total. Suggested split:")
        for name, d in rows:
            print(f"  {name:22} {d:.2f}/day")
        print(f"Launch-phase realistic outcome (target ACOS ~{lacos*100:.0f}%):")
        print(f"  ~{sales:.0f} in ad-attributed sales, ~{units:.0f} units, plus organic lift and reviews.")
        print("  Launch ads are an investment in rank, not a profit line. Money actions are")
        print("  proposals: the operator confirms each daily budget before anything launches.")

if __name__ == "__main__":
    main()
