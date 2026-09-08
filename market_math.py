#!/usr/bin/env python3
"""
MARKET MATH ENGINE - uapf-kdp-niche-specialist
==============================================
Deterministic computations behind the intelligence modes. Pure stdlib.

  bsr-sales      BSR -> estimated sales/day + monthly units/revenue
  print-cost     KDP paperback printing cost for a trim/ink/page count
  margin         royalty + margin per sale at a list price
  niche-score    composite A-F niche grade from collected metrics
  kw-difficulty  keyword difficulty 0-100 from top-10 observations

All sales figures are ESTIMATES derived from public BSR curve observations;
label them as estimates in every report. Print-cost tables reflect KDP's
published US rates (last synced 2026-08; verify live at PRICE CHECK when a
final pricing decision is being made).

Examples:
  python market_math.py bsr-sales --bsr 12000 --marketplace US --price 14.99
  python market_math.py print-cost --pages 120 --ink color --trim large
  python market_math.py margin --price 24.99 --pages 100 --ink color --trim large
  python market_math.py niche-score --demand-bsr 18000 --top10-avg-reviews 220 \
      --indie-share 0.7 --new-entrants-90d 6 --median-price 16.99 --pages 120 --ink color
  python market_math.py kw-difficulty --title-density 6 --top10-avg-bsr 45000 \
      --top10-avg-reviews 350 --exact-title-matches 2
"""
import argparse, bisect, json, math, sys

# BSR -> sales/day anchor points (US Books, log-log interpolated between).
# Widely observed public curve; an estimate, not Amazon data.
BSR_CURVE = [
    (1, 3500), (5, 2000), (10, 1500), (50, 600), (100, 400), (500, 180),
    (1000, 115), (2500, 70), (5000, 45), (10000, 26), (20000, 15),
    (50000, 6.5), (100000, 2.8), (200000, 1.2), (500000, 0.35),
    (1000000, 0.1), (2000000, 0.03), (5000000, 0.005),
]
# Marketplace size scaling vs US (rough public approximations).
MARKET_SCALE = {"US": 1.0, "UK": 0.35, "DE": 0.30, "FR": 0.15, "IT": 0.12,
                "ES": 0.12, "CA": 0.15, "AU": 0.10, "JP": 0.20}

# KDP US paperback printing (per-unit): fixed + per-page, by ink type.
# large trim = above 6.12 x 9 (e.g. 8.5x11). Synced 2026-08; verify live.
PRINT_RATES = {
    ("bw", "regular"):      {"fixed": 1.00, "page": 0.012},
    ("bw", "large"):        {"fixed": 1.00, "page": 0.017},
    ("color-std", "regular"): {"fixed": 1.00, "page": 0.0255},
    ("color-std", "large"):   {"fixed": 1.00, "page": 0.0402},
    ("color", "regular"):   {"fixed": 1.00, "page": 0.0650},
    ("color", "large"):     {"fixed": 1.00, "page": 0.0894},
}
ROYALTY_RATE = 0.60  # KDP paperback list-price royalty


def bsr_to_daily(bsr, marketplace="US"):
    bsr = max(1, int(bsr))
    xs = [p[0] for p in BSR_CURVE]
    i = bisect.bisect_left(xs, bsr)
    if i == 0:
        daily = BSR_CURVE[0][1]
    elif i >= len(xs):
        daily = BSR_CURVE[-1][1]
    else:
        (x0, y0), (x1, y1) = BSR_CURVE[i - 1], BSR_CURVE[i]
        t = (math.log(bsr) - math.log(x0)) / (math.log(x1) - math.log(x0))
        daily = math.exp(math.log(y0) + t * (math.log(y1) - math.log(y0)))
    return daily * MARKET_SCALE.get(marketplace.upper(), 1.0)


def print_cost(pages, ink="bw", trim="regular"):
    r = PRINT_RATES[(ink, trim)]
    return r["fixed"] + r["page"] * max(24, int(pages))


def margin(price, pages, ink="bw", trim="regular"):
    cost = print_cost(pages, ink, trim)
    royalty = ROYALTY_RATE * price - cost
    return cost, royalty, (royalty / price if price else 0)


def niche_score(a):
    """0-100 composite -> letter. Higher = better opportunity."""
    s_demand = max(0, min(100, 100 * (1 - math.log(max(a.demand_bsr, 100)) / math.log(2000000))))
    if a.top10_avg_reviews <= 50: s_moat = 90
    elif a.top10_avg_reviews <= 150: s_moat = 75
    elif a.top10_avg_reviews <= 400: s_moat = 55
    elif a.top10_avg_reviews <= 1000: s_moat = 35
    else: s_moat = 15
    s_indie = a.indie_share * 100
    _, roy, pct = margin(a.median_price, a.pages, a.ink,
                         "large" if a.pages and a.ink != "bw" else "regular")
    s_margin = max(0, min(100, pct * 250))
    sat = max(0, min(100, 100 - a.new_entrants_90d * 7))
    score = (0.30 * s_demand + 0.25 * s_moat + 0.15 * s_indie +
             0.20 * s_margin + 0.10 * sat)
    grade = ("A" if score >= 75 else "B" if score >= 62 else
             "C" if score >= 48 else "D" if score >= 35 else "F")
    return {"score": round(score, 1), "grade": grade,
            "components": {"demand": round(s_demand, 1), "moat": round(s_moat, 1),
                            "indie_share": round(s_indie, 1), "margin": round(s_margin, 1),
                            "saturation": round(sat, 1)},
            "royalty_at_median": round(roy, 2)}


def kw_difficulty(a):
    """0-100; higher = harder to rank for."""
    d_title = min(100, a.title_density * 12)            # exact keyword in top-10 titles
    d_rank = max(0, min(100, 100 * (1 - math.log(max(a.top10_avg_bsr, 100)) / math.log(2000000))))
    d_rev = min(100, a.top10_avg_reviews / 12)
    d_exact = min(100, a.exact_title_matches * 25)
    score = 0.30 * d_title + 0.30 * d_rank + 0.25 * d_rev + 0.15 * d_exact
    band = ("VERY HARD" if score >= 75 else "HARD" if score >= 55 else
            "MODERATE" if score >= 35 else "EASY")
    return {"difficulty": round(score, 1), "band": band}


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("bsr-sales")
    p.add_argument("--bsr", type=int, required=True)
    p.add_argument("--marketplace", default="US")
    p.add_argument("--price", type=float, default=None)
    p = sub.add_parser("print-cost")
    p.add_argument("--pages", type=int, required=True)
    p.add_argument("--ink", choices=["bw", "color-std", "color"], default="bw")
    p.add_argument("--trim", choices=["regular", "large"], default="regular")
    p = sub.add_parser("margin")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--pages", type=int, required=True)
    p.add_argument("--ink", choices=["bw", "color-std", "color"], default="bw")
    p.add_argument("--trim", choices=["regular", "large"], default="regular")
    p = sub.add_parser("niche-score")
    p.add_argument("--demand-bsr", dest="demand_bsr", type=int, required=True,
                   help="median BSR of the top 10")
    p.add_argument("--top10-avg-reviews", dest="top10_avg_reviews", type=float, required=True)
    p.add_argument("--indie-share", dest="indie_share", type=float, required=True,
                   help="0-1 fraction of top 10 that is indie/KDP")
    p.add_argument("--new-entrants-90d", dest="new_entrants_90d", type=int, required=True)
    p.add_argument("--median-price", dest="median_price", type=float, required=True)
    p.add_argument("--pages", type=int, required=True)
    p.add_argument("--ink", choices=["bw", "color-std", "color"], default="bw")
    p = sub.add_parser("kw-difficulty")
    p.add_argument("--title-density", dest="title_density", type=int, required=True,
                   help="top-10 titles containing the keyword")
    p.add_argument("--top10-avg-bsr", dest="top10_avg_bsr", type=int, required=True)
    p.add_argument("--top10-avg-reviews", dest="top10_avg_reviews", type=float, required=True)
    p.add_argument("--exact-title-matches", dest="exact_title_matches", type=int, default=0)
    a = ap.parse_args()

    if a.cmd == "bsr-sales":
        d = bsr_to_daily(a.bsr, a.marketplace)
        out = {"estimate": True, "bsr": a.bsr, "marketplace": a.marketplace.upper(),
               "sales_per_day": round(d, 2), "sales_per_month": round(d * 30, 1)}
        if a.price:
            out["gross_revenue_month"] = round(d * 30 * a.price, 2)
        print(json.dumps(out))
    elif a.cmd == "print-cost":
        print(json.dumps({"print_cost": round(print_cost(a.pages, a.ink, a.trim), 2),
                          "note": "US rates, synced 2026-08; verify live before final pricing"}))
    elif a.cmd == "margin":
        cost, roy, pct = margin(a.price, a.pages, a.ink, a.trim)
        print(json.dumps({"list_price": a.price, "print_cost": round(cost, 2),
                          "royalty_per_sale": round(roy, 2),
                          "margin_pct_of_price": round(pct * 100, 1),
                          "verdict": "OK" if roy >= 2.0 else "THIN" if roy > 0 else "LOSS"}))
    elif a.cmd == "niche-score":
        print(json.dumps(niche_score(a)))
    elif a.cmd == "kw-difficulty":
        print(json.dumps(kw_difficulty(a)))


if __name__ == "__main__":
    main()
