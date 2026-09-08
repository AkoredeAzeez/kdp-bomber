"""AIRF 2.0 Business and Money Edition -- deterministic production operations for the Business & Money niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture,
reasoning, or content rule is defined here; SKILL.md remains the source of truth.

Scope of what is genuinely deterministic in this niche:
  - competitor page-target statistics (mean / median / min / max / central range), median-preferred
    when outliers exist  (SKILL.md 0.7 Competitor Research and Page Target)
  - compulsory image rule (auto-insert all necessary visuals at ANY page count -- global Rule 11)
    (SKILL.md Interior Design)
  - page-band membership check  (SKILL.md Book Architecture "Page bands")

CLI:  python genie_business.py selftest
"""
import json
import math
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def comparable_stats(page_counts):
    """Mean, median, min, max, and central range for a set of comparable print page counts.
    `central_range` is the interquartile band [Q1, Q3] (the middle cluster the framework asks the
    agent to weigh). Returns a dict. Requires at least one value."""
    data = [int(p) for p in page_counts]
    if not data:
        raise ValueError("need at least one comparable page count")
    out = {
        "n": len(data),
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "min": min(data),
        "max": max(data),
    }
    if len(data) >= 2:
        q1, _med, q3 = statistics.quantiles(data, n=4, method="inclusive")
        out["central_range"] = [q1, q3]
    else:
        out["central_range"] = [data[0], data[0]]
    return out


def recommend_page_target(page_counts, outliers_present=False):
    """Recommend the page target from comparables. The framework prefers the MEDIAN when outliers
    exist, otherwise the mean is a reasonable center. Returns both plus the recommendation."""
    s = comparable_stats(page_counts)
    recommended = s["median"] if outliers_present else s["mean"]
    return {
        "mean": s["mean"],
        "median": s["median"],
        "min": s["min"],
        "max": s["max"],
        "central_range": s["central_range"],
        "outliers_present": bool(outliers_present),
        "recommended": recommended,
        "basis": "median (outliers present)" if outliers_present else "mean (no outliers)",
    }


def image_rule(projected_pages, cfg=None):
    """Compulsory image rule (global Rule 11): all necessary visuals are auto-inserted at ANY
    page count; page count never gates generation. Quantity follows content need, not pages."""
    cfg = cfg or load_config()
    pages = int(projected_pages)
    return {
        "projected_pages": pages,
        "auto_insert_all": True,
        "quantity_by_content_need_not_page_count": True,
        "page_gated": False,
    }


def page_band(band_name, target=None, cfg=None):
    """Return a page band [low, high] by name; if `target` given, also report membership."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if band_name not in bands:
        raise ValueError("unknown band %r (allowed: %s)" % (band_name, list(bands)))
    low, high = bands[band_name]
    out = {"band": band_name, "low": low, "high": high}
    if target is not None:
        out["in_band"] = low <= int(target) <= high
    return out


def selftest():
    cfg = load_config()
    checks = {}
    counts = [140, 150, 160, 180, 200, 220, 250, 300]  # mean 200, median 190
    s = comparable_stats(counts)
    checks["mean_200"] = s["mean"] == 200
    checks["median_190"] = s["median"] == 190
    checks["min_max"] = s["min"] == 140 and s["max"] == 300
    checks["central_range_brackets_median"] = s["central_range"][0] <= s["median"] <= s["central_range"][1]

    rec_out = recommend_page_target(counts, outliers_present=True)
    checks["target_median_on_outliers"] = rec_out["recommended"] == 190
    rec_in = recommend_page_target(counts, outliers_present=False)
    checks["target_mean_no_outliers"] = rec_in["recommended"] == 200

    # Rule 11: images auto-insert at ANY page count -- never page-gated
    checks["image_auto_at_120"] = image_rule(120, cfg)["auto_insert_all"] is True
    checks["image_auto_at_300"] = image_rule(300, cfg)["auto_insert_all"] is True
    checks["image_not_page_gated"] = image_rule(300, cfg)["page_gated"] is False

    checks["band_hit"] = page_band("standard_business_career", 190, cfg)["in_band"] is True
    checks["band_miss"] = page_band("beginner_personal_finance", 130, cfg)["in_band"] is False

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
