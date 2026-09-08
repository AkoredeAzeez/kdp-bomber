#!/usr/bin/env python3
"""
GENIE NICHE FINDER  (KDP-Scout-style)
=====================================
Turns a keyword's top Amazon competitors into a one-screen market report:
a ranked table (BSR, estimated sales/royalty, reviews, rating, price, age,
publisher type) and a single 0-100 Opportunity Score with a Go / Caution /
Avoid verdict.

DATA: this renderer is fed a list of competitor books for one keyword. Collect
those rows from the REAL Amazon search results (top ~15-20) - see collect stub
below. Sales and royalty figures are HEURISTIC ESTIMATES from BSR and price,
clearly labeled as estimates, never presented as exact Amazon figures.

Run the demo:  python genie_niche_finder.py        (renders sample report)
"""
import html, json, os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Estimators (transparent heuristics; calibrate to your category) ───────────
# BSR -> approx monthly sales. Rough public-style curve, NOT an exact figure.
def est_monthly_sales(bsr):
    if not bsr or bsr <= 0:
        return 0
    return max(1, round(18930 / (bsr ** 0.7)))

# Approx KDP paperback royalty per copy (US): 60% of list minus ~printing cost.
def est_royalty_per_copy(price, print_cost=2.6):
    return max(0.0, round(price * 0.6 - print_cost, 2))

# ── Opportunity score (0-100), documented weighting ──────────────────────────
def median(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return 0
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2

def score_niche(books):
    sales = [est_monthly_sales(b.get("bsr")) for b in books]
    reviews = [b.get("reviews", 0) for b in books]
    ages = [b.get("age_days", 0) for b in books]
    indie = [1 for b in books if str(b.get("publisher", "")).lower().startswith(("indep", "indie"))]
    med_sales = median(sales)
    med_reviews = median(reviews)
    med_age = median(ages)
    pct_indie = round(100 * len(indie) / max(1, len(books)))

    # Demand: more median sales -> higher (cap influence)
    demand = min(100, (med_sales / 60) * 100)          # 60+ sales/mo median ~= full demand
    # Competition ease: fewer reviews and more indie presence -> easier
    review_ease = max(0, 100 - (med_reviews / 8))       # 800+ median reviews ~= saturated
    indie_ease = pct_indie                               # more indies winning = more accessible
    competition_ease = 0.6 * review_ease + 0.4 * indie_ease
    # Blend: half demand, half ease
    score = round(0.5 * demand + 0.5 * competition_ease)
    score = max(0, min(100, score))

    if score >= 65:
        verdict, vclass = "GO", "go"
    elif score >= 45:
        verdict, vclass = "CAUTION", "caution"
    else:
        verdict, vclass = "AVOID", "avoid"
    prices = [p for p in ((b.get("price") or 0) for b in books) if p]
    return {
        "score": score, "verdict": verdict, "vclass": vclass,
        "med_sales": round(med_sales), "med_reviews": round(med_reviews),
        "med_age_months": round(med_age / 30, 1), "pct_indie": pct_indie,
        "avg_price": round(sum(prices) / len(prices), 2) if prices else None,
    }

def esc(s):
    return html.escape(str(s))

def color_for(kind, value):
    # green/amber/red thresholds mirroring the KDP-Scout traffic-light feel
    t = {"bsr": (20000, 100000), "reviews": (150, 800), "age": (365, 1095)}[kind]
    good, bad = t
    if kind in ("bsr", "reviews", "age"):
        return "g" if value <= good else ("a" if value <= bad else "r")
    return "a"

CSS = """
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial,sans-serif}
body{background:#0b0f1a;color:#e8eaf0;padding:26px}
.top{display:flex;gap:22px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
h1{font-size:20px;color:#fff}.kw{color:#C9A227}
.sample{background:#4a3a06;color:#f2c94c;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px}
.sub{color:#6b7280;font-size:12px;margin-bottom:20px}
.row{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:20px}
.gauge{background:#121826;border:1px solid #232c40;border-radius:16px;padding:22px 26px;text-align:center;min-width:210px}
.gauge .num{font-size:54px;font-weight:800;line-height:1}
.gauge .v{display:inline-block;margin-top:10px;padding:4px 14px;border-radius:20px;font-weight:800;font-size:13px}
.go{background:#0c3d2e;color:#34d399}.caution{background:#4a3a06;color:#f2c94c}.avoid{background:#4a1010;color:#f87171}
.num.go{color:#34d399}.num.caution{color:#f2c94c}.num.avoid{color:#f87171}
.cards{display:flex;gap:12px;flex-wrap:wrap;flex:1}
.stat{background:#121826;border:1px solid #232c40;border-radius:12px;padding:14px 16px;min-width:120px;flex:1}
.stat b{display:block;font-size:22px;color:#fff}.stat span{font-size:11px;color:#9ca3af;text-transform:uppercase;letter-spacing:.5px}
table{width:100%;border-collapse:collapse;font-size:12.5px;background:#121826;border:1px solid #232c40;border-radius:12px;overflow:hidden}
th{background:#0f1420;color:#C9A227;text-align:left;padding:10px 12px;font-size:10.5px;text-transform:uppercase;letter-spacing:.6px}
td{padding:9px 12px;border-top:1px solid #1c2333}
td.t{color:#fff;max-width:280px}
.pill{padding:2px 8px;border-radius:12px;font-weight:700;font-size:11px}
.g{background:#0c3d2e;color:#34d399}.a{background:#4a3a06;color:#f2c94c}.r{background:#4a1010;color:#f87171}
.indie{color:#93c5fd}.trad{color:#9ca3af}
.note{color:#4b5563;font-size:11px;margin-top:14px;line-height:1.5}
"""

def render(keyword, books, sample=True):
    sc = score_niche(books)
    rows = []
    ranked = sorted(books, key=lambda b: b.get("bsr", 1e9))
    for b in ranked:
        s = est_monthly_sales(b.get("bsr"))
        price = b.get("price") or 0
        if price:
            price_cell = f"${price:.2f}"
            roy_cell = f"${round(s * est_royalty_per_copy(price)):,}/mo"
        else:
            price_cell = roy_cell = "&mdash;"
        pub = str(b.get("publisher", ""))
        indie = pub.lower().startswith(("indep", "indie"))
        rows.append(f"""<tr>
<td class="t">{esc(b.get('title','?'))}</td>
<td><span class="pill {color_for('bsr', b.get('bsr',0))}">#{b.get('bsr','?'):,}</span></td>
<td>{s:,}/mo</td>
<td>{roy_cell}</td>
<td><span class="pill {color_for('reviews', b.get('reviews',0))}">{b.get('reviews',0):,}</span></td>
<td>{b.get('rating','?')}&#9733;</td>
<td>{price_cell}</td>
<td><span class="pill {color_for('age', b.get('age_days',0))}">{round(b.get('age_days',0)/30)} mo</span></td>
<td class="{'indie' if indie else 'trad'}">{'Indie' if indie else 'Trad'}</td>
</tr>""")
    badge = '<span class="sample">SAMPLE DATA - illustrative only</span>' if sample else ''
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Niche Report: {esc(keyword)}</title>
<style>{CSS}</style></head><body>
<div class="top"><h1>Niche report: <span class="kw">{esc(keyword)}</span></h1>{badge}</div>
<div class="sub">Top {len(books)} competitors. Sales and royalties are heuristic estimates from BSR and price, not exact Amazon figures. Generated {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}.</div>
<div class="row">
<div class="gauge"><div class="num {sc['vclass']}">{sc['score']}</div><div style="color:#6b7280;font-size:11px;margin-top:4px">OPPORTUNITY / 100</div><div class="v {sc['vclass']}">{sc['verdict']}</div></div>
<div class="cards">
<div class="stat"><b>{sc['med_sales']:,}</b><span>Median sales / mo</span></div>
<div class="stat"><b>{sc['med_reviews']:,}</b><span>Median reviews</span></div>
<div class="stat"><b>{sc['pct_indie']}%</b><span>Indie-published</span></div>
<div class="stat"><b>{sc['med_age_months']}</b><span>Median age (mo)</span></div>
<div class="stat"><b>{('$%.2f' % sc['avg_price']) if sc['avg_price'] else '&mdash;'}</b><span>Avg price</span></div>
</div></div>
<table><thead><tr><th>Competing title</th><th>BSR</th><th>Est. sales</th><th>Est. royalty</th><th>Reviews</th><th>Rating</th><th>Price</th><th>Age</th><th>Publisher</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table>
<div class="note">Scoring (transparent): Opportunity = 50% demand (median estimated sales) + 50% competition-ease (fewer median reviews and more indie winners = easier). Green/amber/red mark easier/harder cells. Estimates should be calibrated to your category. Connect a live data source (see genie_niche_finder.py) to replace the sample rows with real Amazon figures.</div>
</body></html>"""

# ── Data collection stub (wire to on-demand browser reads of Amazon search) ──
def collect_from_amazon(keyword):
    """TODO: open Amazon search for `keyword` in the browser, read the top ~15
    results' title, BSR (from each product page), price, reviews, rating, and
    publication date, and return a list of dicts like SAMPLE below. Real data
    only; label estimates as estimates."""
    raise NotImplementedError("Wire this to on-demand browser reads.")

# Illustrative sample so you can see the outlook before we connect live data.
SAMPLE = [
    {"title": "Chair Yoga for Seniors: Gentle Routines", "bsr": 4200, "reviews": 1820, "rating": 4.6, "price": 12.99, "age_days": 900, "publisher": "Independent"},
    {"title": "Chair Yoga for Weight Loss After 60", "bsr": 9100, "reviews": 640, "rating": 4.5, "price": 11.99, "age_days": 400, "publisher": "Independent"},
    {"title": "Sit and Be Fit: Senior Chair Workouts", "bsr": 15800, "reviews": 220, "rating": 4.4, "price": 13.49, "age_days": 210, "publisher": "Independent"},
    {"title": "The Big Book of Chair Exercises", "bsr": 24000, "reviews": 95, "rating": 4.3, "price": 14.99, "age_days": 150, "publisher": "Independent"},
    {"title": "Gentle Yoga for Beginners Over 60", "bsr": 33000, "reviews": 410, "rating": 4.5, "price": 10.99, "age_days": 1200, "publisher": "Traditional"},
    {"title": "10-Minute Chair Yoga Daily", "bsr": 47000, "reviews": 60, "rating": 4.2, "price": 9.99, "age_days": 95, "publisher": "Independent"},
    {"title": "Balance and Flexibility for Seniors", "bsr": 62000, "reviews": 180, "rating": 4.4, "price": 12.99, "age_days": 520, "publisher": "Independent"},
    {"title": "Chair Yoga Illustrated", "bsr": 88000, "reviews": 40, "rating": 4.1, "price": 15.99, "age_days": 70, "publisher": "Independent"},
]

def main():
    import argparse
    ap = argparse.ArgumentParser(description="Render a KDP-Scout-style niche report.")
    ap.add_argument("--keyword", help="the niche keyword searched")
    ap.add_argument("--data", help="JSON file: list of competitor books (title,bsr,reviews,rating,price,age_days,publisher)")
    ap.add_argument("--out", default=os.path.join(ROOT, "niche_report.html"))
    a = ap.parse_args()
    if a.keyword and a.data:
        books = json.load(open(a.data, encoding="utf-8"))
        if not books:
            print("No books in data file; nothing to score."); return
        open(a.out, "w", encoding="utf-8").write(render(a.keyword, books, sample=False))
        sc = score_niche(books)
        print(f"Rendered {a.out}  ->  {sc['score']}/100 ({sc['verdict']})  from {len(books)} real competitors")
    else:
        open(a.out, "w", encoding="utf-8").write(render("chair yoga for seniors", SAMPLE, sample=True))
        sc = score_niche(SAMPLE)
        print(f"Rendered SAMPLE {a.out}  ->  {sc['score']}/100 ({sc['verdict']}). "
              "Pass --keyword and --data <books.json> for a live report.")

if __name__ == "__main__":
    main()
