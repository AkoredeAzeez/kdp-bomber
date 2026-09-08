#!/usr/bin/env python3
"""
GENIE LOCALIZATION LEDGER
=========================
Plans and tracks translated editions of one finished book across Amazon
marketplaces. It does NOT translate: Genie translates, and only AFTER the
operator confirms the plan. This tool scaffolds the plan, tracks status, and
renders an overview.

Subcommands:
  plan      create a localization plan for target marketplaces
  set       update a locale's status / asin
  overview  render localization_overview.html
  markets   print the supported marketplace registry

Examples:
  python genie_localize.py plan --title "Chair Yoga for Seniors" --targets DE,FR,ES,IT --out loc.json
  python genie_localize.py --plan loc.json set --locale DE --status translated
  python genie_localize.py --plan loc.json overview --out loc.html
"""
import argparse, json, datetime, html

# locale -> language, marketplace, currency, measurement units, date format
MARKETS = {
    "US": ("English (US)", "amazon.com", "USD", "imperial", "MM/DD/YYYY"),
    "UK": ("English (UK)", "amazon.co.uk", "GBP", "metric", "DD/MM/YYYY"),
    "DE": ("German", "amazon.de", "EUR", "metric", "DD.MM.YYYY"),
    "FR": ("French", "amazon.fr", "EUR", "metric", "DD/MM/YYYY"),
    "ES": ("Spanish", "amazon.es", "EUR", "metric", "DD/MM/YYYY"),
    "IT": ("Italian", "amazon.it", "EUR", "metric", "DD/MM/YYYY"),
    "NL": ("Dutch", "amazon.nl", "EUR", "metric", "DD-MM-YYYY"),
    "JP": ("Japanese", "amazon.co.jp", "JPY", "metric", "YYYY/MM/DD"),
    "MX": ("Spanish (Mexico)", "amazon.com.mx", "MXN", "metric", "DD/MM/YYYY"),
    "BR": ("Portuguese (Brazil)", "amazon.com.br", "BRL", "metric", "DD/MM/YYYY"),
}

def now(): return datetime.datetime.now().strftime("%Y-%m-%d")
def load(p): return json.load(open(p, encoding="utf-8"))
def save(p, d): json.dump(d, open(p, "w", encoding="utf-8"), indent=2)
def esc(s): return html.escape(str(s or ""))

def cmd_plan(a):
    targets = []
    for loc in [x.strip().upper() for x in a.targets.split(",") if x.strip()]:
        if loc not in MARKETS:
            print(f"  skip unknown locale: {loc}"); continue
        lang, mkt, cur, units, datef = MARKETS[loc]
        targets.append({"locale": loc, "language": lang, "marketplace": mkt, "currency": cur,
                        "units": units, "date_format": datef, "status": "planned", "asin": ""})
    d = {"title": a.title, "source_lang": a.source_lang or "English (US)", "created": now(), "targets": targets}
    save(a.plan, d)
    print(f"Planned {len(targets)} target market(s) for '{a.title}': " + ", ".join(t["locale"] for t in targets))
    print("NEXT: present this plan to the operator and get explicit confirmation BEFORE translating anything.")

def cmd_set(a):
    d = load(a.plan)
    for t in d["targets"]:
        if t["locale"] == a.locale.upper():
            if a.status: t["status"] = a.status
            if a.asin: t["asin"] = a.asin
            save(a.plan, d); print(f"Updated {a.locale.upper()}"); return
    print(f"Locale not in plan: {a.locale}")

def cmd_overview(a):
    d = load(a.plan)
    chip = {"planned": "#4a3a06;#f2c94c", "translated": "#1e3a8a;#93c5fd",
            "metadata": "#3a1e4a;#c9a0f2", "published": "#0c3d2e;#34d399"}
    rows = []
    for t in d["targets"]:
        bg, fg = chip.get(t["status"], "#333;#ccc").split(";")
        rows.append(f"""<tr><td class=b>{esc(t['locale'])}</td><td>{esc(t['language'])}</td>
<td class=m>{esc(t['marketplace'])}</td><td>{esc(t['currency'])} / {esc(t['units'])}</td>
<td><span style="background:{bg};color:{fg};padding:2px 9px;border-radius:12px;font-size:11px;font-weight:700">{esc(t['status'].upper())}</span></td>
<td class=m>{esc(t['asin'] or '-')}</td></tr>""")
    pub = sum(t["status"] == "published" for t in d["targets"])
    out = a.out or "localization_overview.html"
    open(out, "w", encoding="utf-8").write(f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Localization: {esc(d['title'])}</title>
<style>*{{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial,sans-serif}}
body{{background:#0f1420;color:#e5e7eb;padding:26px}}h1{{color:#C9A227;font-size:20px}}
.sub{{color:#6b7280;font-size:12px;margin:6px 0 18px}}
table{{width:100%;border-collapse:collapse;font-size:13px;background:#1a2130;border:1px solid #2b3446;border-radius:12px;overflow:hidden}}
th{{background:#0f1420;color:#C9A227;text-align:left;padding:10px;font-size:11px;text-transform:uppercase}}
td{{padding:9px 10px;border-top:1px solid #22293a}}.b{{color:#fff;font-weight:700}}.m{{font-family:Consolas,monospace;color:#9ca3af;font-size:11px}}</style>
</head><body>
<h1>{esc(d['title'])}</h1><div class="sub">Localization plan. Source: {esc(d['source_lang'])}. {len(d['targets'])} markets, {pub} published. Generated {now()}.</div>
<table><thead><tr><th>Locale</th><th>Language</th><th>Marketplace</th><th>Currency / units</th><th>Status</th><th>ASIN</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan=6 style=color:#6b7280>No targets</td></tr>'}</tbody></table>
</body></html>""")
    print(f"Wrote {out}")

def cmd_markets(a):
    print("Supported marketplaces:")
    for loc, (lang, mkt, cur, units, datef) in MARKETS.items():
        print(f"  {loc}: {lang:20} {mkt:16} {cur}  {units}  {datef}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", default="localization_plan.json")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan"); p.add_argument("--title", required=True); p.add_argument("--source-lang", dest="source_lang")
    p.add_argument("--targets", required=True); p.add_argument("--out"); p.set_defaults(fn=lambda a: cmd_plan(a))
    p = sub.add_parser("set"); p.add_argument("--locale", required=True); p.add_argument("--status"); p.add_argument("--asin")
    p.set_defaults(fn=cmd_set)
    p = sub.add_parser("overview"); p.add_argument("--out"); p.set_defaults(fn=cmd_overview)
    p = sub.add_parser("markets"); p.set_defaults(fn=cmd_markets)
    a = ap.parse_args()
    if getattr(a, "out", None) is None and a.cmd == "plan":
        a.out = a.plan
    if a.cmd == "plan":
        a.plan = a.out or a.plan
    a.fn(a)

if __name__ == "__main__":
    main()
