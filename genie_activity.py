"""AIRF 2.0 Activity Edition -- deterministic production operations for the activity/puzzle/coloring niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_activity.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def default_page_map_total(cfg=None):
    """Sum the puzzle-dominant 100-page map components; must equal the stated total."""
    cfg = cfg or load_config()
    m = cfg["page_map_puzzle_dominant"]
    computed = (m["front_matter_pages"] + m["activity_area_pages"]
                + m["solutions_pages"] + m["progress_tracker_pages"] + m["notes_pages"])
    return {"computed": computed, "declared_total": m["total"], "ok": computed == m["total"]}


def validate_interior_page_count(pages, documented_reason=False, cfg=None):
    """Exactly 100 by default; even 96-104 only with a documented reason; else FAIL."""
    cfg = cfg or load_config()
    itr = cfg["interior"]
    if pages == itr["default_pages"]:
        return {"ok": True, "pages": pages, "mode": "exact_default"}
    lo, hi = itr["even_exception_min"], itr["even_exception_max"]
    if lo <= pages <= hi and pages % 2 == 0 and documented_reason:
        return {"ok": True, "pages": pages, "mode": "documented_even_exception"}
    reasons = []
    if pages != itr["default_pages"]:
        reasons.append("not the 100-page default")
    if not (lo <= pages <= hi):
        reasons.append("outside %d-%d even band" % (lo, hi))
    if pages % 2 != 0:
        reasons.append("odd page count")
    if (lo <= pages <= hi) and pages % 2 == 0 and not documented_reason:
        reasons.append("even exception requires documented reason")
    return {"ok": False, "pages": pages, "problems": reasons}


def activity_pages_for(promised_items, items_per_page):
    """Pages of activity area needed for a promised item count at a given density."""
    if promised_items < 0 or items_per_page <= 0:
        raise ValueError("promised_items>=0 and items_per_page>0 required")
    return math.ceil(promised_items / items_per_page)


def reconcile_count_ledger(front_matter, activity_pages, solution_pages,
                           blank_backs, closing_pages, approved_total):
    """SKILL.md count ledger: front matter + activity pages + solution entries pages
    + blank backs + closing pages must equal the exact approved page total."""
    total = front_matter + activity_pages + solution_pages + blank_backs + closing_pages
    return {"total": total, "approved_total": approved_total,
            "ok": total == approved_total,
            "delta": total - approved_total}


def validate_sample_map(activity_count, total_pages=None, cfg=None):
    """10-page sample must be 10 pages and carry >= the minimum substantive activities."""
    cfg = cfg or load_config()
    s = cfg["sample_map"]
    total_pages = s["total_pages"] if total_pages is None else total_pages
    problems = []
    if total_pages != s["total_pages"]:
        problems.append("sample must be %d pages, got %d" % (s["total_pages"], total_pages))
    if activity_count < s["min_substantive_activities"]:
        problems.append("sample needs >=%d activities, got %d"
                        % (s["min_substantive_activities"], activity_count))
    return {"ok": not problems, "problems": problems}


def coloring_single_sided_pages(design_count, cfg=None):
    """Single-sided coloring budget: front matter + design*2 (each design + blank reverse)
    + closing pages. Also flags whether design_count is inside the SKILL.md range and whether
    the resulting total is a valid even interior count."""
    cfg = cfg or load_config()
    v = cfg["page_map_coloring_variant"]
    total = v["front_matter_pages"] + design_count * 2 + v["closing_pages"]
    in_range = v["design_count_min"] <= design_count <= v["design_count_max"]
    return {"total": total, "design_count": design_count,
            "design_in_range": in_range,
            "even": total % 2 == 0}


def diversity_quota_ok(mechanic_pages, cfg=None):
    """No single supporting mechanic may exceed the max fraction of activity pages.
    `mechanic_pages` is {mechanic: page_count}. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    cap = cfg["diversity_quotas"]["single_supporting_mechanic_max_fraction"]
    total = sum(mechanic_pages.values())
    problems = []
    if total <= 0:
        return {"ok": False, "problems": ["no activity pages"], "cap": cap}
    for mech, pages in mechanic_pages.items():
        frac = pages / total
        if frac > cap:
            problems.append("%s is %.0f%% of activity pages (cap %.0f%%)"
                            % (mech, frac * 100, cap * 100))
    return {"ok": not problems, "problems": problems, "cap": cap}


def word_list_overlap(list_a, list_b, cfg=None):
    """Overlap fraction between two word-search word lists = |shared| / min(|a|,|b|).
    Flags a duplicate when it exceeds the SKILL.md threshold (>50%)."""
    cfg = cfg or load_config()
    thr = cfg["duplicate_scan"]["word_search_overlap_duplicate_threshold"]
    a = {w.strip().lower() for w in list_a if w.strip()}
    b = {w.strip().lower() for w in list_b if w.strip()}
    if not a or not b:
        return {"overlap": 0.0, "duplicate": False, "threshold": thr}
    shared = len(a & b)
    overlap = shared / min(len(a), len(b))
    return {"overlap": overlap, "duplicate": overlap > thr, "threshold": thr}


def difficulty_arc_monotone(ratings):
    """A section's difficulty ratings must be non-decreasing (progressive, monotone within
    sections). `ratings` is an ordered list of numeric difficulty values."""
    ok = all(ratings[i] <= ratings[i + 1] for i in range(len(ratings) - 1))
    return {"ok": ok, "ratings": list(ratings)}


def selftest():
    cfg = load_config()
    checks = {}
    # default 100-page map sums to 100
    checks["page_map_total_100"] = default_page_map_total(cfg)["ok"]
    # page-count validation
    checks["exact_100_ok"] = validate_interior_page_count(100, cfg=cfg)["ok"]
    checks["even_102_with_reason_ok"] = validate_interior_page_count(102, True, cfg)["ok"]
    checks["even_102_no_reason_fail"] = not validate_interior_page_count(102, False, cfg)["ok"]
    checks["odd_101_fail"] = not validate_interior_page_count(101, True, cfg)["ok"]
    checks["page_90_out_of_band_fail"] = not validate_interior_page_count(90, True, cfg)["ok"]
    # activity pages density math
    checks["activity_pages_200_at_4"] = activity_pages_for(200, 4) == 50
    checks["activity_pages_odd_ceil"] = activity_pages_for(201, 4) == 51
    # count ledger reconciles against the default map (4 + 80 + 14 + 0 + 2 = 100)
    led = reconcile_count_ledger(4, 80, 14, 0, 2, 100)
    checks["count_ledger_reconciles"] = led["ok"] and led["delta"] == 0
    checks["count_ledger_mismatch_flagged"] = not reconcile_count_ledger(4, 80, 10, 0, 2, 100)["ok"]
    # sample map
    checks["sample_map_ok"] = validate_sample_map(4, 10, cfg)["ok"]
    checks["sample_map_too_few_fail"] = not validate_sample_map(3, 10, cfg)["ok"]
    # coloring single-sided budget: 45 -> 96, 48 -> 102, both even, both in range
    c45 = coloring_single_sided_pages(45, cfg)
    c48 = coloring_single_sided_pages(48, cfg)
    checks["coloring_45_is_96_even"] = c45["total"] == 96 and c45["even"] and c45["design_in_range"]
    checks["coloring_48_is_102_even"] = c48["total"] == 102 and c48["even"] and c48["design_in_range"]
    # diversity quota
    ok_div = diversity_quota_ok({"maze": 20, "wordsearch": 20, "sudoku": 20, "trivia": 20})
    checks["diversity_ok"] = ok_div["ok"]
    bad_div = diversity_quota_ok({"maze": 60, "wordsearch": 20, "sudoku": 20})
    checks["diversity_over_cap_flagged"] = not bad_div["ok"]
    # word overlap duplicate detection
    dup = word_list_overlap(["cat", "dog", "fish", "bird"], ["cat", "dog", "fish", "owl"])
    checks["word_overlap_duplicate"] = dup["duplicate"] is True
    fresh = word_list_overlap(["cat", "dog", "fish", "bird"], ["lion", "tiger", "bear", "wolf"])
    checks["word_overlap_distinct_ok"] = fresh["duplicate"] is False
    # difficulty arc monotonicity
    checks["difficulty_monotone_ok"] = difficulty_arc_monotone([1, 1, 2, 3, 3, 4])["ok"]
    checks["difficulty_nonmonotone_fail"] = not difficulty_arc_monotone([1, 3, 2])["ok"]
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
