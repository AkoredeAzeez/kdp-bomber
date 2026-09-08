#!/usr/bin/env python3
"""
GENIE SERIES ENGINE
===================
Keeps a multi-book series coherent: one ledger (series.json) holds the shared
brand and every book's angle and status. Generates the cross-promotion back
matter each book needs and a series overview page.

Subcommands:
  init       create a series ledger
  add        add a book to the series
  set        update a book's status/asin/blurb
  backmatter generate the "More in this series" page for one book (excludes it)
  overview   render series_overview.html
  status     print the series to the console

Examples:
  python genie_series.py init --name "Calm Mind" --author "Jane A. Doe" --audience "busy adults" --brand "short, practical mindfulness" --trim 6x9
  python genie_series.py add --title "Calm Mind at Work" --angle "workplace stress"
  python genie_series.py backmatter --for "Calm Mind at Work" --out backmatter.md
  python genie_series.py overview --out series_overview.html
"""
import argparse, json, os, datetime, html

DEFAULT = "series.json"

def load(p): return json.load(open(p, encoding="utf-8"))
def save(p, d): json.dump(d, open(p, "w", encoding="utf-8"), indent=2)
def now(): return datetime.datetime.now().strftime("%Y-%m-%d")

def cmd_init(a):
    d = {"name": a.name, "author": a.author, "audience": a.audience or "",
         "brand": a.brand or "", "naming": a.naming or "", "trim": a.trim or "6x9",
         "created": now(), "books": []}
    save(a.series, d)
    print(f"Created series '{a.name}' -> {a.series}")

def cmd_add(a):
    d = load(a.series)
    order = a.order if a.order is not None else len(d["books"]) + 1
    d["books"].append({"title": a.title, "angle": a.angle or "", "order": order,
                       "status": a.status or "planned", "asin": a.asin or "", "blurb": a.blurb or ""})
    d["books"].sort(key=lambda b: b["order"])
    save(a.series, d)
    print(f"Added '{a.title}' (order {order}) to {d['name']}")

def cmd_set(a):
    d = load(a.series)
    for b in d["books"]:
        if b["title"].lower() == a.title.lower():
            if a.status: b["status"] = a.status
            if a.asin: b["asin"] = a.asin
            if a.blurb: b["blurb"] = a.blurb
            save(a.series, d); print(f"Updated '{a.title}'"); return
    print(f"Not found: {a.title}")

def cmd_backmatter(a):
    d = load(a.series)
    others = [b for b in d["books"] if b["title"].lower() != a.for_title.lower()]
    others.sort(key=lambda b: b["order"])
    lines = [f"# More in the {d['name']} series", "",
             f"If this book helped you, the rest of the {d['name']} series goes further:", ""]
    for b in others:
        desc = b["blurb"] or b["angle"]
        lines.append(f"- **{b['title']}**" + (f": {desc}" if desc else ""))
    lines += ["", f"To find them, search \"{d['name']}\" or \"{d['author']}\" on Amazon."]
    out = a.out or "backmatter.md"
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"Wrote {out} ({len(others)} sibling titles). Insert into the book's back matter.")

def esc(s): return html.escape(str(s or ""))

def cmd_overview(a):
    d = load(a.series)
    chip = {"planned": "#4a3a06;#f2c94c", "in_production": "#1e3a8a;#93c5fd", "published": "#0c3d2e;#34d399"}
    rows = []
    for b in sorted(d["books"], key=lambda x: x["order"]):
        bg, fg = chip.get(b["status"], "#333;#ccc").split(";")
        rows.append(f"""<tr><td>{b['order']}</td><td class=t>{esc(b['title'])}</td>
<td>{esc(b['angle'])}</td>
<td><span style="background:{bg};color:{fg};padding:2px 9px;border-radius:12px;font-size:11px;font-weight:700">{esc(b['status'].replace('_',' ').upper())}</span></td>
<td class=m>{esc(b['asin'] or '-')}</td></tr>""")
    pub = sum(b["status"] == "published" for b in d["books"])
    out = a.out or "series_overview.html"
    open(out, "w", encoding="utf-8").write(f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(d['name'])} series</title>
<style>*{{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial,sans-serif}}
body{{background:#0f1420;color:#e5e7eb;padding:26px}}h1{{color:#C9A227;font-size:22px}}
.sub{{color:#6b7280;font-size:12px;margin:6px 0 18px}}
.brand{{background:#1a2130;border:1px solid #2b3446;border-radius:12px;padding:16px;margin-bottom:18px;font-size:13px;line-height:1.6}}
.brand b{{color:#C9A227}}
table{{width:100%;border-collapse:collapse;font-size:13px;background:#1a2130;border:1px solid #2b3446;border-radius:12px;overflow:hidden}}
th{{background:#0f1420;color:#C9A227;text-align:left;padding:10px;font-size:11px;text-transform:uppercase}}
td{{padding:9px 10px;border-top:1px solid #22293a}}.t{{color:#fff;font-weight:600}}.m{{font-family:Consolas,monospace;color:#9ca3af;font-size:11px}}</style>
</head><body>
<h1>{esc(d['name'])}</h1><div class="sub">Series overview. {len(d['books'])} books, {pub} published. Generated {now()}.</div>
<div class="brand"><b>Author:</b> {esc(d['author'])} &nbsp; <b>Audience:</b> {esc(d['audience'])} &nbsp; <b>Trim:</b> {esc(d['trim'])}<br>
<b>Brand:</b> {esc(d['brand'])}<br><b>Naming:</b> {esc(d['naming'])}</div>
<table><thead><tr><th>#</th><th>Title</th><th>Angle</th><th>Status</th><th>ASIN</th></tr></thead>
<tbody>{''.join(rows) or '<tr><td colspan=5 style=color:#6b7280>No books yet</td></tr>'}</tbody></table>
</body></html>""")
    print(f"Wrote {out}")

def cmd_status(a):
    d = load(a.series)
    print(f"{d['name']} by {d['author']} ({d['trim']}) - {len(d['books'])} books")
    for b in sorted(d["books"], key=lambda x: x["order"]):
        print(f"  {b['order']}. [{b['status']:>13}] {b['title']}  ({b['angle']})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", default=DEFAULT)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init"); p.add_argument("--name", required=True); p.add_argument("--author", required=True)
    p.add_argument("--audience"); p.add_argument("--brand"); p.add_argument("--naming"); p.add_argument("--trim")
    p.set_defaults(fn=cmd_init)
    p = sub.add_parser("add"); p.add_argument("--title", required=True); p.add_argument("--angle")
    p.add_argument("--order", type=int); p.add_argument("--status"); p.add_argument("--asin"); p.add_argument("--blurb")
    p.set_defaults(fn=cmd_add)
    p = sub.add_parser("set"); p.add_argument("--title", required=True); p.add_argument("--status")
    p.add_argument("--asin"); p.add_argument("--blurb"); p.set_defaults(fn=cmd_set)
    p = sub.add_parser("backmatter"); p.add_argument("--for", dest="for_title", required=True); p.add_argument("--out")
    p.set_defaults(fn=cmd_backmatter)
    p = sub.add_parser("overview"); p.add_argument("--out"); p.set_defaults(fn=cmd_overview)
    p = sub.add_parser("status"); p.set_defaults(fn=cmd_status)
    a = ap.parse_args()
    a.fn(a)

if __name__ == "__main__":
    main()
