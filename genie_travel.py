"""AIRF 2.0 Travel Edition -- deterministic production operations for the travel-guide niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_travel.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def competitor_stats(page_counts, cfg=None):
    """Mean and median of competitor paperback page counts. Median is weighted over
    mean per the framework. Enforces the minimum-titles benchmark rule."""
    cfg = cfg or load_config()
    cb = cfg["competitor_benchmark"]
    counts = sorted(int(p) for p in page_counts)
    n = len(counts)
    if n == 0:
        raise ValueError("no competitor page counts supplied")
    mean = sum(counts) / n
    mid = n // 2
    median = counts[mid] if n % 2 else (counts[mid - 1] + counts[mid]) / 2
    return {
        "n": n,
        "mean": round(mean, 1),
        "median": float(median),
        "meets_min_titles": n >= cb["min_titles"],
        "median_weighted_over_mean": cb["median_weighted_over_mean"],
    }


def is_studio_owner(cfg=None):
    """Studio-owner deployment iff the .genie_owner marker is present in the install root."""
    cfg = cfg or load_config()
    marker = cfg["page_budget"]["deployment_marker"]
    # install root is three levels up from this framework folder (skill/frameworks/AIRF-2.0-Travel-Edition)
    root = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
    return os.path.exists(os.path.join(root, marker))


def recommend_target_pages(competitor_median, studio_owner, cfg=None):
    """Recommend a competitive target page count near the market median, clamped to the
    deployment budget. Studio owner: never exceed the hard cap; keep the 2-page reserve
    (target 96-100). Client: near median, may raise."""
    cfg = cfg or load_config()
    b = cfg["page_budget"]
    median = int(round(competitor_median))
    if studio_owner:
        cap = b["studio_owner_hard_cap"]
        target = min(median, cap - b["studio_owner_reserve_pages"])
        target = max(target, b["studio_owner_target_min"])
        target = min(target, b["studio_owner_target_max"])
        return {"target": target, "hard_cap": cap, "reserve": b["studio_owner_reserve_pages"]}
    # client: recommend the median (operator may raise); no hard cap enforced here
    return {"target": median, "hard_cap": None, "reserve": None}


def check_page_budget(pages, studio_owner, client_budget=None, cfg=None):
    """Compare projected physical pages to the deployment budget."""
    cfg = cfg or load_config()
    b = cfg["page_budget"]
    if studio_owner:
        budget = b["studio_owner_hard_cap"]
    else:
        if client_budget is None:
            raise ValueError("client deployment requires an explicit client_budget")
        budget = int(client_budget)
    ok = pages <= budget
    out = {"ok": ok, "pages": pages, "budget": budget, "studio_owner": studio_owner}
    if not ok:
        out["over_by"] = pages - budget
    elif studio_owner:
        out["reserve_ok"] = pages <= budget - b["studio_owner_reserve_pages"]
    return out


def min_map_count(district_chapter_count, cfg=None):
    """Minimum map set = 1 overview + one per district chapter, floored at the framework
    minimum (a standard guide carries 4-5 at minimum). A single-map book is a Gate-3 fail."""
    cfg = cfg or load_config()
    floor = cfg["maps"]["min_count"]
    return max(1 + int(district_chapter_count), floor)


def check_chapter_functions(present_function_numbers, cfg=None):
    """Verify all 12 required functional blocks are present. `present_function_numbers`
    is an iterable of the function numbers (1-12) the chapter map covers."""
    cfg = cfg or load_config()
    required = cfg["chapter_functions"]["required_count"]
    present = set(int(x) for x in present_function_numbers)
    missing = sorted(set(range(1, required + 1)) - present)
    return {"ok": not missing, "required": required, "missing": missing}


def image_program_count(major_chapter_count, inline_subsection_count, map_count):
    """Total image program = 1 cover + one full-bleed opener per major chapter
    + one inline image per substantial subsection + the map set."""
    return 1 + int(major_chapter_count) + int(inline_subsection_count) + int(map_count)


def trim_spec(trim_key, cfg=None):
    """Return the canvas, safe margin, and opener resolution for a chosen trim."""
    cfg = cfg or load_config()
    opts = cfg["trim_options"]
    if trim_key not in opts:
        raise ValueError("unknown trim %r (allowed: 6x9, 8.5x11)" % (trim_key,))
    return opts[trim_key]


def selftest():
    cfg = load_config()
    checks = {}

    # competitor stats: median weighted; odd and even n
    s_odd = competitor_stats([90, 110, 100, 120, 105])
    checks["median_odd"] = s_odd["median"] == 105.0 and s_odd["mean"] == 105.0
    s_even = competitor_stats([100, 110, 120, 130])
    checks["median_even"] = s_even["median"] == 115.0
    checks["min_titles_flag"] = competitor_stats([100] * 8)["meets_min_titles"] is False
    checks["min_titles_ok"] = competitor_stats([100] * 12)["meets_min_titles"] is True

    # studio-owner target: median 130 clamps to cap-reserve=98
    r_owner = recommend_target_pages(130, True, cfg)
    checks["owner_target_clamped"] = r_owner["target"] == 98
    # studio-owner target: median 92 rises to floor 96
    checks["owner_target_floor"] = recommend_target_pages(92, True, cfg)["target"] == 96
    # client: recommend median unclamped
    checks["client_target_median"] = recommend_target_pages(140, False, cfg)["target"] == 140

    # page budget
    checks["owner_budget_ok"] = check_page_budget(98, True, cfg=cfg)["ok"] is True
    checks["owner_budget_breach"] = check_page_budget(102, True, cfg=cfg)["over_by"] == 2
    checks["owner_reserve_ok"] = check_page_budget(98, True, cfg=cfg)["reserve_ok"] is True
    checks["client_budget"] = check_page_budget(108, False, client_budget=110, cfg=cfg)["ok"] is True

    # maps: overview + one per district, floored at 4
    checks["map_floor"] = min_map_count(2, cfg) == 4
    checks["map_scaled"] = min_map_count(6, cfg) == 7

    # chapter functions
    checks["functions_ok"] = check_chapter_functions(range(1, 13), cfg)["ok"] is True
    checks["functions_missing"] = check_chapter_functions([1, 2, 3, 4, 5], cfg)["missing"] == [6, 7, 8, 9, 10, 11, 12]

    # image program: 1 + 12 openers + 24 inline + 5 maps = 42
    checks["image_program"] = image_program_count(12, 24, 5) == 42

    # trim spec lookup
    checks["trim_lookup"] = trim_spec("8.5x11", cfg)["opener_px"] == [2588, 3375]

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
