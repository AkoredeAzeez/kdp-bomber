"""UCGF 1.0 -- deterministic production operations for the cookbook niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_cookbook.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def appendix_pages(plan_days, cfg=None):
    """Appendix page count by meal-plan duration (30 -> 12, 60 -> 20)."""
    cfg = cfg or load_config()
    table = cfg["page_governor"]["appendix_pages"]
    key = str(int(plan_days))
    if key not in table:
        raise ValueError("unsupported plan_days %r (allowed: %s)" % (plan_days, list(table)))
    return table[key]


def recipe_pages(recipe_count):
    """Two recipes per page, no split -> ceil(R/2)."""
    if recipe_count < 0:
        raise ValueError("recipe_count must be >= 0")
    return math.ceil(recipe_count / 2)


def page_estimate(recipe_count, category_count, plan_days=30, cfg=None):
    """Governor formula: Pages = 6 + 6 + C + ceil(R/2) + 2 + A."""
    cfg = cfg or load_config()
    g = cfg["page_governor"]
    return (g["front_matter_pages"] + g["intro_plus_education_pages"]
            + category_count + recipe_pages(recipe_count)
            + g["conclusion_pages"] + appendix_pages(plan_days, cfg))


def image_slot_count(category_count, recipe_count):
    """Image contract count = 1 hero + one divider per category + one per recipe."""
    return 1 + category_count + recipe_count


def per_serving_round(calories, macros_g, cfg=None):
    """Round a Per Serving line per framework: calories to nearest 5, macros to nearest 1 g."""
    cfg = cfg or load_config()
    cal_step = cfg["nutrition"]["calorie_round_to"]
    cals = int(round(calories / cal_step) * cal_step)
    macros = {k: int(round(v)) for k, v in dict(macros_g).items()}
    return {"calories": cals, "macros_g": macros}


def validate_categories(category_counts, cfg=None):
    """Validate the category set against UCGF rules. `category_counts` is
    {CATEGORY_NAME: recipe_count}. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    c = cfg["categories"]
    problems = []
    n = len(category_counts)
    if n < c["min_count"] or n > c["max_count"]:
        problems.append("category count %d outside %d-%d" % (n, c["min_count"], c["max_count"]))
    for name, cnt in category_counts.items():
        if cnt < c["recipes_per_category_min"] or cnt > c["recipes_per_category_max"]:
            problems.append("category %s has %d recipes (must be %d-%d)" % (
                name, cnt, c["recipes_per_category_min"], c["recipes_per_category_max"]))
    joined = " ".join(category_counts.keys()).lower()
    meals = {"breakfast": ["breakfast", "smoothie", "morning"],
             "lunch": ["lunch", "salad", "soup", "sandwich", "bowl"],
             "dinner": ["dinner", "main", "poultry", "seafood", "beef", "entree"],
             "snack": ["snack", "dessert", "side", "bite"]}
    for meal, hints in meals.items():
        if not any(h in joined for h in hints):
            problems.append("category set may not cover %s" % meal)
    return (not problems, problems)


def check_page_budget(pages, budget, cfg=None):
    """Compare projected pages to the deployment budget; on breach return the
    fixed compression order the framework mandates."""
    cfg = cfg or load_config()
    if pages <= budget:
        return {"ok": True, "pages": pages, "budget": budget, "compression_order": []}
    return {"ok": False, "pages": pages, "budget": budget,
            "over_by": pages - budget,
            "compression_order": cfg["page_budget"]["compression_order_on_breach"]}


def selftest():
    cfg = load_config()
    checks = {}
    # governor: 90 recipes, 10 categories, 30-day -> 6+6+10+45+2+12 = 81
    checks["page_estimate_90_10_30"] = page_estimate(90, 10, 30, cfg) == 81
    # 60-day appendix is 20 -> 6+6+10+45+2+20 = 89
    checks["page_estimate_90_10_60"] = page_estimate(90, 10, 60, cfg) == 89
    checks["recipe_pages_odd"] = recipe_pages(91) == 46
    checks["image_slots"] = image_slot_count(10, 90) == 101
    checks["per_serving_round"] = per_serving_round(312, {"protein": 20.4, "fat": 9.6}) == {
        "calories": 310, "macros_g": {"protein": 20, "fat": 10}}
    ok_cats, _ = validate_categories({
        "BREAKFAST": 9, "SMOOTHIES": 8, "SALADS": 10, "SOUPS": 8, "POULTRY": 9,
        "SEAFOOD": 8, "MAINS": 12, "SIDES": 7, "SNACKS": 8, "DESSERTS": 11})
    checks["valid_category_set_ok"] = ok_cats
    bad_ok, bad_probs = validate_categories({"BREAKFAST": 3, "MAINS": 20})
    checks["bad_category_set_flagged"] = (not bad_ok) and len(bad_probs) >= 2
    checks["budget_breach_order"] = check_page_budget(120, 100, cfg)["compression_order"][0] == "appendix_density"
    checks["budget_ok"] = check_page_budget(81, 100, cfg)["ok"] is True
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
