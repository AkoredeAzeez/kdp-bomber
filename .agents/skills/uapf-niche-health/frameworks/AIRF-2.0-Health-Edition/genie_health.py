"""AIRF 2.0 Health Edition -- deterministic production operations for the Health, Fitness & Wellness niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture,
safety reasoning, or claims judgement is defined here; SKILL.md remains the source of truth. These
functions only check the numeric/structural constants the SKILL.md already states (competitor set
size, page-band membership, the step-by-step image-sequence panel minimum, book image count, and
audience-driven typography).

CLI:  python genie_health.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def competitor_count_valid(n, cfg=None):
    """Competitor research set must be 5-10 current relevant titles."""
    cfg = cfg or load_config()
    c = cfg["competitors"]
    return c["min_count"] <= n <= c["max_count"]


def page_band(band_name, cfg=None):
    """Return [low, high] for a named competitor-derived page band."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if band_name not in bands:
        raise ValueError("unknown page band %r (allowed: %s)" % (band_name, list(bands)))
    return bands[band_name]


def in_band(pages, band_name, cfg=None):
    """True if a page target sits inside the named band (inclusive)."""
    lo, hi = page_band(band_name, cfg)
    return lo <= pages <= hi


def min_panels(cfg=None):
    """Minimum step-by-step panels per technique image sequence (3)."""
    cfg = cfg or load_config()
    return cfg["technique_unit"]["image_sequence_min_panels"]


def validate_technique_panels(panel_count, cfg=None):
    """Validate one technique's image-sequence panel count. A single finished-pose image
    (or anything below the minimum) is a hard failure. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    mn = min_panels(cfg)
    problems = []
    if panel_count < mn:
        if panel_count <= 1:
            problems.append("single/finished-pose image only (%d); a step-by-step sequence "
                            "of at least %d panels is required" % (panel_count, mn))
        else:
            problems.append("only %d panels; minimum sequence is %d" % (panel_count, mn))
    return (not problems, problems)


def book_image_count(technique_panel_counts, chapter_count, cfg=None):
    """Total image-manifest slots = one hero per chapter opener + every technique's panels.
    `technique_panel_counts` is a list of per-technique panel counts."""
    cfg = cfg or load_config()
    heroes = chapter_count if cfg["technique_unit"].get("hero_per_chapter_opener") else 0
    return heroes + sum(technique_panel_counts)


def body_typography(audience_key, cfg=None):
    """Return the locked body typography rule for the audiences the SKILL.md fixes explicitly
    (senior/large-print -> 13-14 pt at 1.5; professional reference -> 11-12 pt at 1.15). For any
    other audience the SKILL.md leaves the choice inside the 11-14 pt band."""
    cfg = cfg or load_config()
    table = cfg["typography_by_audience"]
    if audience_key in table:
        return table[audience_key]
    opts = cfg["interior"]["body_pt_options"]
    return {"body_pt_min": min(opts), "body_pt_max": max(opts), "line_spacing": None,
            "note": "audience-chosen within the 11-14 pt band"}


def selftest():
    cfg = load_config()
    checks = {}
    # competitor set bounds
    checks["competitor_ok_5"] = competitor_count_valid(5, cfg) is True
    checks["competitor_ok_10"] = competitor_count_valid(10, cfg) is True
    checks["competitor_bad_4"] = competitor_count_valid(4, cfg) is False
    checks["competitor_bad_11"] = competitor_count_valid(11, cfg) is False
    # page bands
    checks["band_senior_lookup"] = page_band("gentle_senior_practice", cfg) == [120, 180]
    checks["band_in"] = in_band(150, "gentle_senior_practice", cfg) is True
    checks["band_out_low"] = in_band(119, "gentle_senior_practice", cfg) is False
    checks["band_out_high"] = in_band(351, "comprehensive_professional_reference", cfg) is False
    # technique panel minimum
    checks["min_panels_is_3"] = min_panels(cfg) == 3
    ok3, _ = validate_technique_panels(3, cfg)
    checks["panels_3_ok"] = ok3 is True
    ok1, probs1 = validate_technique_panels(1, cfg)
    checks["panels_1_fail"] = (ok1 is False) and len(probs1) == 1
    ok2, _ = validate_technique_panels(2, cfg)
    checks["panels_2_fail"] = ok2 is False
    # book image count: 2 chapters (heroes) + techniques [3,4,3] panels = 2 + 10 = 12
    checks["image_count"] = book_image_count([3, 4, 3], 2, cfg) == 12
    # typography by audience
    checks["senior_typo"] = body_typography("senior_large_print", cfg)["body_pt_min"] == 13
    checks["pro_typo"] = body_typography("professional_reference", cfg)["body_pt_max"] == 12
    checks["other_typo_band"] = body_typography("rehabilitation_return_to_movement", cfg)["body_pt_max"] == 14
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
