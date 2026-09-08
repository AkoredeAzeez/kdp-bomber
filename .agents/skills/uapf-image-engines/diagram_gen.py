r"""GENIE DIAGRAM RENDERER: precise figures from data, never from diffusion.

AI image engines fabricate wrong symbols and garble labels on technical
figures (proven on the welding handbook). Anything with exact labels, values,
arrows, or structure is DRAWN here with matplotlib instead: deterministic,
correct, and in the book's palette.

  python diagram_gen.py --spec figure.json --out fig_1_1.png

Spec (JSON):
  {"type": "bar" | "line" | "pie" | "flow" | "steps",
   "title": "...",
   "palette": {"principal": "1F3A5F", "accent": "C8873F"},   # optional
   ... type-specific fields below ...}

  bar:   {"labels": [...], "values": [...], "ylabel": "..."}
  line:  {"x": [...], "series": [{"label": "...", "y": [...]}, ...],
          "xlabel": "...", "ylabel": "..."}
  pie:   {"labels": [...], "values": [...]}
  flow:  {"nodes": ["Start", "Do a thing", ...]}          # left-to-right boxes + arrows
  steps: {"items": ["First ...", "Second ...", ...]}      # numbered vertical steps

Output: 300 DPI PNG, LANDSCAPE by default (per the image law), white
background, grayscale-legible colors. No em dashes anywhere.
"""
import argparse, json, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def _hex(c, default):
    c = str(c or default).lstrip("#")
    return "#" + c


def render(spec, out):
    kind = spec.get("type", "bar")
    pal = spec.get("palette") or {}
    PRIN = _hex(pal.get("principal"), "1F3A5F")
    ACC = _hex(pal.get("accent"), "C8873F")
    w, h = spec.get("width", 8.0), spec.get("height", 4.5)   # landscape
    fig, ax = plt.subplots(figsize=(w, h), dpi=300)
    fig.patch.set_facecolor("white")

    title = spec.get("title", "")

    if kind == "bar":
        labels = spec["labels"]; values = spec["values"]
        bars = ax.bar(labels, values, color=PRIN, edgecolor="black", linewidth=0.6)
        for b, v in zip(bars, values):
            ax.text(b.get_x() + b.get_width() / 2, b.get_height(), str(v),
                    ha="center", va="bottom", fontsize=9)
        if spec.get("ylabel"):
            ax.set_ylabel(spec["ylabel"], fontsize=10)
        ax.spines[["top", "right"]].set_visible(False)

    elif kind == "line":
        x = spec["x"]
        styles = ["-", "--", "-.", ":"]
        colors = [PRIN, ACC, "#555555", "#999999"]
        for i, srs in enumerate(spec["series"]):
            ax.plot(x, srs["y"], styles[i % 4], color=colors[i % 4],
                    label=srs.get("label", "Series %d" % (i + 1)), linewidth=2)
        ax.legend(frameon=False, fontsize=9)
        if spec.get("xlabel"):
            ax.set_xlabel(spec["xlabel"], fontsize=10)
        if spec.get("ylabel"):
            ax.set_ylabel(spec["ylabel"], fontsize=10)
        ax.grid(True, linewidth=0.3, alpha=0.5)
        ax.spines[["top", "right"]].set_visible(False)

    elif kind == "pie":
        labels = spec["labels"]; values = spec["values"]
        greys = [PRIN, ACC, "#8a8a8a", "#bcbcbc", "#5a5a5a", "#dddddd"]
        wedges, _, autot = ax.pie(values, labels=labels, autopct="%1.0f%%",
                                  colors=[greys[i % 6] for i in range(len(values))],
                                  wedgeprops={"edgecolor": "white", "linewidth": 1.2},
                                  textprops={"fontsize": 9})
        for t in autot:
            t.set_color("white"); t.set_fontsize(9)
        ax.axis("equal")

    elif kind == "flow":
        nodes = spec["nodes"]
        ax.set_xlim(0, len(nodes)); ax.set_ylim(0, 1); ax.axis("off")
        bw = 0.78
        for i, n in enumerate(nodes):
            x0 = i + (1 - bw) / 2
            box = FancyBboxPatch((x0, 0.32), bw, 0.36,
                                 boxstyle="round,pad=0.02",
                                 facecolor="white", edgecolor=PRIN, linewidth=1.4)
            ax.add_patch(box)
            ax.text(i + 0.5, 0.5, n, ha="center", va="center", fontsize=9, wrap=True)
            if i:
                ax.add_patch(FancyArrowPatch((i - (1 - bw) / 2 + 0.01, 0.5),
                                             (x0 - 0.01, 0.5),
                                             arrowstyle="-|>", mutation_scale=16,
                                             color=ACC, linewidth=1.4))

    elif kind == "steps":
        items = spec["items"]
        n = len(items)
        ax.set_xlim(0, 1); ax.set_ylim(0, n); ax.axis("off")
        for i, txt in enumerate(items):
            y = n - 1 - i
            ax.add_patch(plt.Circle((0.06, y + 0.5), 0.16, color=ACC))
            ax.text(0.06, y + 0.5, str(i + 1), ha="center", va="center",
                    color="white", fontsize=10, fontweight="bold")
            ax.text(0.14, y + 0.5, txt, ha="left", va="center", fontsize=10, wrap=True)
            if i < n - 1:
                ax.plot([0.06, 0.06], [y + 0.34, y - 0.34 + 0.68 - 0.36],
                        color="#bbbbbb", linewidth=1.2)
        fig.set_size_inches(w, max(2.2, 0.62 * n))

    else:
        sys.exit("unknown diagram type '%s' (bar, line, pie, flow, steps)" % kind)

    if title:
        ax.set_title(title.replace("—", ", "), fontsize=12,
                     color=PRIN, fontweight="bold", pad=10)
    fig.tight_layout()
    fig.savefig(out, dpi=300, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return out


def main():
    ap = argparse.ArgumentParser(description="Render a precise book figure with matplotlib.")
    ap.add_argument("--spec", required=True, help="JSON spec file")
    ap.add_argument("--out", required=True, help="output PNG path")
    a = ap.parse_args()
    spec = json.load(open(a.spec, encoding="utf-8"))
    render(spec, a.out)
    print("rendered %s (%s)" % (a.out, spec.get("type")))


if __name__ == "__main__":
    main()
