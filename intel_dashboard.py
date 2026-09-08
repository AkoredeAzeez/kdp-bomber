#!/usr/bin/env python3
"""
INTERACTIVE INTELLIGENCE DASHBOARD - uapf-kdp-niche-specialist
==============================================================
Renders a keyword-research JSON twin as a self-contained HTML dashboard.
STATIC-FIRST: every chart is pre-rendered as SVG in Python with native
<title> hover tooltips, so the page displays fully in script-blocked
viewers (the Claude Code side panel included). In a normal browser a small
JS layer adds rich cursor tooltips and live sorting on top.

Usage:
  python intel_dashboard.py keyword_sheet.json [-o intel_dashboard.html]

Input schema: see the skill's Interactive dashboard law. All sales and
revenue figures are estimates and are labeled as such on the page.
"""
import argparse, html, json, math, os

L = {"surface": "#fcfcfb", "page": "#f9f9f7", "ink": "#0b0b0b", "ink2": "#52514e",
     "muted": "#898781", "grid": "#e1e0d9", "axis": "#c3c2b7", "s1": "#2a78d6",
     "s2": "#eb6834", "s3": "#1baf7a", "s4": "#eda100",
     "seq": ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]}

def fmt(n):
    if n is None: return "–"
    if n >= 1000: return f"{n/1000:.0f}k" if n >= 10000 else f"{n/1000:.1f}k"
    return f"{n:.1f}".rstrip("0").rstrip(".")

def money(n): return "–" if n is None else "$" + fmt(n)
def esc(s): return html.escape(str(s), quote=True)

def opportunity(k):
    return max(0.0, (k.get("est_sales_day") or 0.05)) * (100 - (k.get("difficulty") or 50))


def insights_html(kws, mkts):
    """Plain-language 'what this means' bullets computed from the data."""
    out = []
    scored = sorted(kws, key=opportunity, reverse=True)
    gold = [k for k in scored if (k.get("difficulty") or 99) < 35 and (k.get("est_sales_day") or 0) > 1]
    if gold:
        names = ", ".join(f'&ldquo;{esc(k["keyword"])}&rdquo;' for k in gold[:3])
        out.append(f"<b>Your best openings:</b> {names} sit in the GOLDMINE zone: "
                   "real demand, weak keyword competition. Put these in the subtitle and backend keywords.")
    beat = [k for k in kws if (k.get("top10_avg_bsr") or 9e9) < 10000]
    for k in beat[:1]:
        out.append(f"<b>Demand is proven:</b> the top book for &ldquo;{esc(k['keyword'])}&rdquo; ranks "
                   f"around BSR {fmt(k.get('top10_avg_bsr'))}, selling every day.")
    hard = [k for k in scored if (k.get("difficulty") or 0) >= 55]
    if hard:
        out.append(f"<b>Approach with care:</b> &ldquo;{esc(hard[0]['keyword'])}&rdquo; is dominated by "
                   "entrenched sellers. Rank under it via categories, do not fight it head-on in the title.")
    zero_td = [k for k in gold if (k.get("title_density") or 0) == 0]
    if zero_td:
        out.append(f"<b>Nobody is using</b> &ldquo;{esc(zero_td[0]['keyword'])}&rdquo; in their titles yet: "
                   "an uncontested phrase with live demand.")
    for mk in mkts:
        if mk.get("note") and mk.get("opportunity", 0) >= 65:
            out.append(f"<b>Amazon {mk['code']}:</b> {esc(mk['note'])}.")
    if not out:
        out.append("No standout openings in this set: consider widening the seed keywords.")
    return "<ul>" + "".join(f"<li>{b}</li>" for b in out) + "</ul>"

def tiles(kws, mkts):
    tot = sum(k.get("est_rev_month") or 0 for k in kws)
    easy = sum(1 for k in kws if (k.get("difficulty") or 99) < 35)
    t = [(str(len(kws)), "keywords scored"), (money(tot), "est. combined revenue/mo"),
         (str(easy), "EASY-band keywords"), (str(len(mkts)), "marketplaces scanned")]
    return "".join(f'<div class="tile"><div class="v">{v}</div><div class="l">{l}</div></div>'
                   for v, l in t)

def bubble_svg(kws):
    W, H = 880, 380; Pl, Pr, Pt, Pb = 56, 16, 26, 38
    ys = [k.get("est_sales_day") or 0.05 for k in kws]
    y_max = max(ys + [1]) * 1.15
    r_max = max([k.get("est_rev_month") or 1 for k in kws] + [1])
    X = lambda d: Pl + (d / 100) * (W - Pl - Pr)
    Y = lambda v: H - Pb - (v / y_max) * (H - Pt - Pb)
    g = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    for i in range(5):
        yv = y_max * i / 4; y = Y(yv)
        g.append(f'<line x1="{Pl}" y1="{y:.1f}" x2="{W-Pr}" y2="{y:.1f}" stroke="{L["grid"]}"/>' \
                 f'<text x="{Pl-8}" y="{y+4:.1f}" text-anchor="end" fill="{L["muted"]}">{fmt(yv)}</text>')
    for d in (0, 25, 50, 75, 100):
        g.append(f'<text x="{X(d):.1f}" y="{H-Pb+16}" text-anchor="middle" fill="{L["muted"]}">{d}</text>')
    g.append(f'<line x1="{Pl}" y1="{H-Pb}" x2="{W-Pr}" y2="{H-Pb}" stroke="{L["axis"]}"/>')
    g.append(f'<line x1="{X(50):.1f}" y1="{Pt}" x2="{X(50):.1f}" y2="{H-Pb}" stroke="{L["grid"]}" stroke-dasharray="3 4"/>')
    g.append(f'<text x="{X(25):.1f}" y="{Pt-8}" text-anchor="middle" fill="{L["muted"]}">GOLDMINE: easy + demand</text>')
    g.append(f'<text x="{X(75):.1f}" y="{Pt-8}" text-anchor="middle" fill="{L["muted"]}">CONTESTED</text>')
    top = sorted(kws, key=opportunity, reverse=True)[:5]
    top_set = {k["keyword"] for k in top}
    for k in kws:
        r = max(5, 4 + 14 * math.sqrt((k.get("est_rev_month") or 1) / r_max))
        cx, cy = X(k.get("difficulty") or 50), Y(k.get("est_sales_day") or 0.05)
        tip = (f'{k["keyword"]}\ndifficulty {k.get("difficulty")} ({k.get("band","")})'
               f'\nest. {fmt(k.get("est_sales_day"))} sales/day · {money(k.get("est_rev_month"))}/mo'
               f'\ntop-10 avg BSR {fmt(k.get("top10_avg_bsr"))} · title density {k.get("title_density","–")}')
        g.append(f'<circle class="bub" data-band="{k.get("band","")}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{L["s1"]}" '
                 f'fill-opacity="0.78" stroke="{L["surface"]}" stroke-width="2">'
                 f'<title>{esc(tip)}</title></circle>')
        if k["keyword"] in top_set:
            lab = k["keyword"] if len(k["keyword"]) <= 26 else k["keyword"][:24] + "…"
            g.append(f'<text x="{cx:.1f}" y="{cy-r-4:.1f}" text-anchor="middle" fill="{L["ink2"]}">{esc(lab)}</text>')
    g.append("</svg>")
    return "".join(g)

def bars_svg(kws, key="opportunity"):
    rows = sorted(kws, key=lambda k: (k.get(key) if key != "opportunity" else opportunity(k)) or 0,
                  reverse=True)[:15]
    W, rh, Pl, Pr, Pt = 880, 24, 250, 120, 6
    Hh = Pt + len(rows) * rh + 8
    m = max([(k.get(key) if key != "opportunity" else opportunity(k)) or 0 for k in rows] + [1e-9])
    g = [f'<svg viewBox="0 0 {W} {Hh}" width="{W}" height="{Hh}">']
    for i, k in enumerate(rows):
        v = (k.get(key) if key != "opportunity" else opportunity(k)) or 0
        y = Pt + i * rh; w = max(3, v / m * (W - Pl - Pr))
        name = k["keyword"] if len(k["keyword"]) <= 34 else k["keyword"][:32] + "…"
        val = money(v) if key == "est_rev_month" else fmt(v)
        tip = f'{k["keyword"]}\nopportunity {fmt(opportunity(k))} · difficulty {k.get("difficulty")}\nest. {money(k.get("est_rev_month"))}/mo'
        g.append(f'<text x="{Pl-10}" y="{y+15}" text-anchor="end" fill="{L["ink"]}">{esc(name)}</text>')
        g.append(f'<rect class="barr" data-band="{k.get("band","")}" x="{Pl}" y="{y+4}" width="{w:.1f}" height="{rh-8}" rx="4" fill="{L["s1"]}">'
                 f'<title>{esc(tip)}</title></rect>')
        g.append(f'<text x="{Pl+w+8:.1f}" y="{y+15}" fill="{L["ink2"]}">{val}</text>')
    g.append("</svg>")
    return "".join(g)

def seasonal_svg(seasonal):
    S = [s for s in (seasonal or []) if len(s.get("snapshots", [])) > 1][:4]
    if not S: return None
    W, H, Pl, Pr, Pt, Pb = 880, 260, 64, 110, 14, 30
    months = sorted({p["date"] for s in S for p in s["snapshots"]})
    vals = [p["top10_avg_bsr"] for s in S for p in s["snapshots"]]
    v_max, v_min = max(vals) * 1.1, max(0, min(vals) * 0.9)
    X = lambda i: Pl + i / max(1, len(months) - 1) * (W - Pl - Pr)
    Y = lambda v: H - Pb - (v - v_min) / (v_max - v_min) * (H - Pt - Pb)
    cols = [L["s1"], L["s2"], L["s3"], L["s4"]]
    g = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    for i in range(4):
        vv = v_min + (v_max - v_min) * i / 3; y = Y(vv)
        g.append(f'<line x1="{Pl}" y1="{y:.1f}" x2="{W-Pr}" y2="{y:.1f}" stroke="{L["grid"]}"/>' \
                 f'<text x="{Pl-8}" y="{y+4:.1f}" text-anchor="end" fill="{L["muted"]}">{fmt(vv)}</text>')
    for i, mo in enumerate(months):
        if len(months) <= 14 or i % 2 == 0:
            g.append(f'<text x="{X(i):.1f}" y="{H-Pb+16}" text-anchor="middle" fill="{L["muted"]}">{mo[2:]}</text>')
    legend = []
    for si, s in enumerate(S):
        pts, tips = [], []
        for i, mo in enumerate(months):
            p = next((q for q in s["snapshots"] if q["date"] == mo), None)
            if p:
                pts.append(f'{X(i):.1f},{Y(p["top10_avg_bsr"]):.1f}')
                tips.append(f'{mo}: BSR {fmt(p["top10_avg_bsr"])}')
        g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{cols[si]}" stroke-width="2">'
                 f'<title>{esc(s["keyword"] + chr(10) + chr(10).join(tips))}</title></polyline>')
        for i, mo in enumerate(months):
            p = next((q for q in s["snapshots"] if q["date"] == mo), None)
            if p:
                g.append(f'<circle cx="{X(i):.1f}" cy="{Y(p["top10_avg_bsr"]):.1f}" r="4" fill="{cols[si]}">'
                         f'<title>{esc(s["keyword"] + " " + mo + ": BSR " + fmt(p["top10_avg_bsr"]))}</title></circle>')
        last = s["snapshots"][-1]
        g.append(f'<text x="{W-Pr+6}" y="{Y(last["top10_avg_bsr"])+4:.1f}" fill="{cols[si]}">{esc(s["keyword"][:15])}</text>')
        legend.append(f'<span><span class="dot" style="background:{cols[si]}"></span>{esc(s["keyword"])}</span>')
    g.append("</svg>")
    return "".join(g), "".join(legend)

def map_svg(mkts):
    if not mkts: return None
    tile, gap = 92, 8
    LAY = {"CA": (0, 0), "US": (0, 1), "UK": (2, 0), "DE": (3, 0), "FR": (2, 1),
           "IT": (3, 1), "ES": (2.5, 2), "JP": (5, 0), "AU": (5, 1)}
    m = max([x.get("est_rev_month") or 0 for x in mkts] + [1e-9])
    g = ['<svg viewBox="0 0 880 240" width="880" height="240">']
    for mk in mkts:
        px, py = LAY.get(mk["code"], (6, 2))
        x, y = 20 + px * (tile + gap), 16 + py * (tile * 0.62 + gap)
        f = (mk.get("est_rev_month") or 0) / m
        step = L["seq"][min(6, int(f * 6.99))]
        ink1, ink2 = ("#0b0b0b", "rgba(11,11,11,.72)") if f < 0.45 else ("#ffffff", "rgba(255,255,255,.85)")
        tip = f'Amazon {mk["code"]}\nest. {money(mk.get("est_rev_month"))}/mo'
        if mk.get("opportunity") is not None: tip += f'\nopportunity {mk["opportunity"]}/100'
        if mk.get("note"): tip += f'\n{mk["note"]}'
        g.append(f'<g><rect x="{x:.0f}" y="{y:.0f}" width="{tile}" height="{tile*0.62:.0f}" rx="8" '
                 f'fill="{step}" stroke="rgba(11,11,11,.10)"/>'
                 f'<text x="{x+tile/2:.0f}" y="{y+24:.0f}" text-anchor="middle" font-weight="600" fill="{ink1}">{mk["code"]}</text>'
                 f'<text x="{x+tile/2:.0f}" y="{y+42:.0f}" text-anchor="middle" fill="{ink2}">{money(mk.get("est_rev_month"))}</text>'
                 f'<title>{esc(tip)}</title></g>')
    lx, ly = 20, 200
    g.append(f'<text x="{lx}" y="{ly-6}" fill="{L["muted"]}">est. revenue/mo: low</text>')
    for i, s in enumerate(L["seq"]):
        g.append(f'<rect x="{lx+120+i*26}" y="{ly-16}" width="24" height="12" rx="2" fill="{s}"/>')
    g.append(f'<text x="{lx+120+7*26+6}" y="{ly-6}" fill="{L["muted"]}">high</text></svg>')
    return "".join(g)

def table_html(kws):
    cols = [("keyword", "Keyword"), ("difficulty", "Difficulty"), ("band", "Band"),
            ("est_sales_day", "Est. sales/day"), ("est_rev_month", "Est. rev/mo"),
            ("top10_avg_bsr", "Top-10 avg BSR"), ("title_density", "Title density")]
    head = "<tr>" + "".join(f"<th>{h}</th>" for _, h in cols) + "</tr>"
    body = []
    for k in sorted(kws, key=lambda x: x.get("est_rev_month") or 0, reverse=True):
        tds = []
        for c, _ in cols:
            v = k.get(c)
            if c == "est_rev_month": v = money(v)
            elif isinstance(v, (int, float)): v = fmt(v)
            tds.append(f"<td>{esc(v if v is not None else chr(0x2013))}</td>")
        body.append(f'<tr data-band="{k.get("band","")}">' + "".join(tds) + "</tr>")
    return head, "".join(body)

def build(data):
    kws = data.get("keywords", [])
    mkts = data.get("marketplaces", [])
    title = f"Keyword Intelligence: {data.get('niche', 'niche')}"
    sub = (f"{data.get('marketplace', 'US')} marketplace · generated {data.get('generated', '')} "
           f"· {len(kws)} keywords · all sales and revenue figures are ESTIMATES")
    seas = seasonal_svg(data.get("seasonal"))
    mapv = map_svg(mkts)
    thead, tbody = table_html(kws)
    note = esc(data.get("data_notes", ""))
    parts = [f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title>
<style>
*{{box-sizing:border-box;margin:0}}
body{{background:{L['page']};color:{L['ink']};font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;padding:20px}}
h1{{font-size:19px;margin-bottom:2px}} .sub{{color:{L['ink2']};font-size:12px;margin-bottom:6px}}
.dnote{{color:{L['muted']};font-size:11px;margin-bottom:14px;max-width:880px}}
.card{{background:{L['surface']};border:1px solid rgba(11,11,11,.10);border-radius:10px;padding:16px;margin-bottom:14px;overflow-x:auto}}
.card h2{{font-size:13px;font-weight:600;margin-bottom:2px}}
.card .note{{color:{L['muted']};font-size:11px;margin-bottom:10px}}
.tiles{{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:14px}}
.tile{{background:{L['surface']};border:1px solid rgba(11,11,11,.10);border-radius:10px;padding:12px 16px;min-width:130px}}
.tile .v{{font-size:22px;font-weight:650}} .tile .l{{color:{L['ink2']};font-size:11px}}
table{{border-collapse:collapse;width:100%;font-size:12px}}
th{{color:{L['ink2']};font-weight:600;text-align:left;border-bottom:1px solid {L['axis']};padding:6px 8px}}
td{{border-bottom:1px solid {L['grid']};padding:5px 8px;font-variant-numeric:tabular-nums}}
svg text{{font:11px system-ui,-apple-system,"Segoe UI",sans-serif}}
.leg{{display:flex;gap:14px;align-items:center;font-size:11px;color:{L['ink2']};margin-top:6px;flex-wrap:wrap}}
.leg span{{display:inline-flex;align-items:center;gap:5px}}
.dot{{width:9px;height:9px;border-radius:50%;display:inline-block}}
.bub{{cursor:pointer}}
.insights ul{{margin-left:18px}} .insights li{{margin-bottom:7px;max-width:820px}}
.chips{{display:flex;gap:6px;align-items:center;margin:0 0 12px}}
.chiplbl{{color:{L['muted']};font-size:11px}}
.chip{{background:none;border:1px solid {L['axis']};border-radius:14px;color:{L['ink2']};padding:3px 12px;font-size:11px;cursor:pointer}}
.chip.on{{border-color:{L['s1']};color:{L['ink']};font-weight:600}}
.dim{{opacity:.14}}
#tip{{position:fixed;pointer-events:none;background:{L['surface']};border:1px solid {L['axis']};border-radius:8px;padding:8px 11px;font-size:12px;box-shadow:0 4px 16px rgba(0,0,0,.18);display:none;z-index:9;max-width:280px;white-space:pre-line}}
</style></head><body>
<h1>{esc(title)}</h1><div class="sub">{sub}</div>""",
    f'<div class="dnote">{note}</div>' if note else "",
    f'<div class="tiles">{tiles(kws, mkts)}</div>',
    f'<div class="card"><h2>What this means</h2><div class="insights">{insights_html(kws, mkts)}</div></div>',
    f'<div class="chips" id="bandChips" hidden><span class="chiplbl">Filter:</span>'
    f'<button class="chip on" data-band="">All</button>'
    f'<button class="chip" data-band="EASY">Easy</button>'
    f'<button class="chip" data-band="MODERATE">Moderate</button>'
    f'<button class="chip" data-band="HARD">Hard</button>'
    f'<button class="chip" data-band="VERY HARD">Very hard</button></div>',
    f'<div class="card"><h2>Keyword opportunity map</h2>'
    f'<div class="note">x: difficulty (easier to harder) · y: estimated demand (sales/day) '
    f'· bubble size: est. revenue/month · hover a bubble for detail</div>{bubble_svg(kws)}</div>',
    f'<div class="card"><h2>Top keywords</h2>'
    f'<div class="note">bar length by the chosen measure · hover a bar</div>'
    f'<div class="chips" id="sortChips" hidden>'
    f'<button class="chip on" data-v="v-opportunity">Opportunity</button>'
    f'<button class="chip" data-v="v-difficulty">Difficulty</button>'
    f'<button class="chip" data-v="v-revenue">Est. revenue</button></div>'
    f'<div id="v-opportunity">{bars_svg(kws)}</div>'
    f'<div id="v-difficulty" hidden>{bars_svg(kws, "difficulty")}</div>'
    f'<div id="v-revenue" hidden>{bars_svg(kws, "est_rev_month")}</div></div>']
    if seas:
        parts.append(f'<div class="card"><h2>Seasonality — tracked keywords</h2>'
                     f'<div class="note">monthly top-10 average BSR (lower = more demand) · hover points</div>'
                     f'{seas[0]}<div class="leg">{seas[1]}</div></div>')
    if mapv:
        parts.append(f'<div class="card"><h2>Marketplace map</h2>'
                     f'<div class="note">tile shade: estimated monthly revenue per Amazon marketplace '
                     f'(sequential scale) · hover a tile</div>{mapv}</div>')
    parts.append(f'<div class="card"><h2>Data table</h2><table><thead>{thead}</thead>'
                 f'<tbody>{tbody}</tbody></table></div>')
    parts.append(ENHANCE_JS)
    parts.append("</body></html>")
    return "".join(parts)


ENHANCE_JS = """
<div id="tip"></div>
<script>
(function(){
 // reveal interactive controls (hidden for script-blocked viewers)
 document.querySelectorAll('.chips[hidden]').forEach(c => c.hidden = false);
 var tip = document.getElementById('tip');
 // rich cursor tooltip: lift native <title> text into data-tip
 document.querySelectorAll('svg title').forEach(function(t){
   var p = t.parentNode; p.setAttribute('data-tip', t.textContent); p.removeChild(t);
 });
 document.querySelectorAll('[data-tip]').forEach(function(el){
   el.addEventListener('mousemove', function(e){
     tip.textContent = el.getAttribute('data-tip');
     tip.style.display = 'block';
     tip.style.left = Math.min(e.clientX + 14, innerWidth - 300) + 'px';
     tip.style.top  = (e.clientY + 12) + 'px';
   });
   el.addEventListener('mouseleave', function(){ tip.style.display = 'none'; });
 });
 // bar view switcher
 document.querySelectorAll('#sortChips .chip').forEach(function(b){
   b.addEventListener('click', function(){
     document.querySelectorAll('#sortChips .chip').forEach(function(x){ x.classList.remove('on'); });
     b.classList.add('on');
     ['v-opportunity','v-difficulty','v-revenue'].forEach(function(id){
       document.getElementById(id).hidden = (id !== b.dataset.v);
     });
   });
 });
 // band filter: dim non-matching bubbles, bars, table rows
 document.querySelectorAll('#bandChips .chip').forEach(function(b){
   b.addEventListener('click', function(){
     document.querySelectorAll('#bandChips .chip').forEach(function(x){ x.classList.remove('on'); });
     b.classList.add('on');
     var band = b.dataset.band;
     document.querySelectorAll('[data-band]').forEach(function(el){
       el.classList.toggle('dim', !!band && el.getAttribute('data-band') !== band);
     });
   });
 });
 // click a bubble to pin its detail in the tooltip for 4s
 document.querySelectorAll('.bub').forEach(function(el){
   el.addEventListener('click', function(e){
     tip.textContent = el.getAttribute('data-tip');
     tip.style.display = 'block';
     setTimeout(function(){ tip.style.display = 'none'; }, 4000);
   });
 });
 // table sorting
 document.querySelectorAll('table th').forEach(function(th, ci){
   th.style.cursor = 'pointer'; var dir = -1;
   th.addEventListener('click', function(){
     var tb = th.closest('table').querySelector('tbody');
     var rows = Array.from(tb.rows);
     rows.sort(function(a, b){
       var av = a.cells[ci].textContent.replace(/[$,k]/g,''), bv = b.cells[ci].textContent.replace(/[$,k]/g,'');
       var an = parseFloat(av), bn = parseFloat(bv);
       if (!isNaN(an) && !isNaN(bn)) return dir * (an - bn);
       return dir * av.localeCompare(bv);
     });
     dir *= -1;
     rows.forEach(function(r){ tb.appendChild(r); });
   });
 });
})();
</script>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--out", default=None)
    ap.add_argument("--open", action="store_true", help="open in the system default browser (Chrome)")
    a = ap.parse_args()
    data = json.load(open(a.input, encoding="utf-8"))
    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.input)), "intel_dashboard.html")
    open(out, "w", encoding="utf-8").write(build(data))
    print(f"dashboard written: {out} ({os.path.getsize(out)//1024} KB, static-first + interactive layer)")
    if a.open:
        import webbrowser
        webbrowser.open("file:///" + os.path.abspath(out).replace(os.sep, "/"))
        print("opened in system browser")

if __name__ == "__main__":
    main()
