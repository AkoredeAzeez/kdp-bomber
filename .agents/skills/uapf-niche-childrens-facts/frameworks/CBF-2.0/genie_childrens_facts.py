"""CBF 2.0 -- deterministic production operations for the children's
nonfiction fact-book niche (OV-CFACT, specialization of OV-CHILD).

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_childrens_facts.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def fact_count_reconcile(produced_numbered_facts, title_claim, cfg=None):
    """Count-claim promise: the manuscript must contain AT LEAST the title's claimed number of
    individually numbered, verified facts. `title_claim` may be an int or None (no claim)."""
    if title_claim is None:
        return {"ok": True, "produced": produced_numbered_facts, "claim": None,
                "shortfall": 0}
    shortfall = max(0, title_claim - produced_numbered_facts)
    return {"ok": produced_numbered_facts >= title_claim,
            "produced": produced_numbered_facts, "claim": title_claim,
            "shortfall": shortfall}


def facts_per_spread_valid(fact_count, kd=None, cfg=None):
    """A themed spread never exceeds the hard cap of 8 facts. If a knowledge-depth level is given,
    also require the count to sit inside that KD's target range."""
    cfg = cfg or load_config()
    cap = cfg["facts_per_spread_hard_cap"]
    problems = []
    if fact_count > cap:
        problems.append("spread has %d facts (hard cap %d)" % (fact_count, cap))
    if kd is not None:
        lo, hi = cfg["knowledge_depth"][kd]["facts_per_spread"]
        if fact_count < lo or fact_count > hi:
            problems.append("%s spread has %d facts (target %d-%d)" % (kd, fact_count, lo, hi))
    return (not problems, problems)


def dual_source_ok(source_count, cfg=None):
    """Every fact needs at least two independent authoritative sources before Gate 2."""
    cfg = cfg or load_config()
    return source_count >= cfg["fact_verification"]["sources_required_per_fact"]


def sidebar_law(sidebar_spreads, total_spreads, cfg=None):
    """Sidebars may appear on no more than 40% of spreads."""
    cfg = cfg or load_config()
    if total_spreads <= 0:
        raise ValueError("total_spreads must be > 0")
    limit = cfg["layout_laws"]["sidebar_max_spread_fraction"]
    frac = sidebar_spreads / total_spreads
    return {"ok": frac <= limit + 1e-9, "fraction": round(frac, 4), "limit": limit,
            "max_allowed_spreads": math.floor(total_spreads * limit)}


def page_count_valid(pages, cfg=None):
    """KDP: page count must be even and >= the KDP minimum (24)."""
    cfg = cfg or load_config()
    r = cfg["page_count_targets"]
    problems = []
    if pages % 2 != 0:
        problems.append("page count %d is not even" % pages)
    if pages < r["kdp_min_pages"]:
        problems.append("page count %d below KDP minimum %d" % (pages, r["kdp_min_pages"]))
    return (not problems, problems)


def color_class(pages, cfg=None):
    """Ink economics: standard color activates at 72 pages; below that KDP prints premium color.
    OV-CFACT is always full color, so this only picks the cost class, never monochrome."""
    cfg = cfg or load_config()
    threshold = cfg["page_count_targets"]["standard_color_starts_page"]
    return "standard" if pages >= threshold else "premium"


def bleed_page_size(trim_w_in, trim_h_in, cfg=None):
    """Bleed page size = trim + 0.125 in width, + 0.25 in height.
    8.5 x 11 -> 8.625 x 11.25 ; 8.5 x 8.5 -> 8.625 x 8.75."""
    cfg = cfg or load_config()
    g = cfg["trim_geometry"]
    return (round(trim_w_in + g["bleed_add_width_in"], 4),
            round(trim_h_in + g["bleed_add_height_in"], 4))


def type_floor_ok(profile_key, element, point_size, cfg=None):
    """Validate a point size against the OV-CFACT type-floor table.
    element in {body, callout_wow, gloss, caption}. For body the floor is the range minimum."""
    cfg = cfg or load_config()
    table = cfg["type_floors_pt"]
    if profile_key not in table:
        raise ValueError("unknown profile %r (allowed: %s)" % (profile_key, list(table)))
    spec = table[profile_key][element]
    floor_min = spec[0] if isinstance(spec, list) else spec
    return point_size >= floor_min


def selftest():
    cfg = load_config()
    checks = {}
    # count-claim reconciliation
    checks["count_meets_claim"] = fact_count_reconcile(105, 100, cfg)["ok"] is True
    r = fact_count_reconcile(88, 100, cfg)
    checks["count_shortfall"] = (r["ok"] is False) and r["shortfall"] == 12
    checks["count_no_claim"] = fact_count_reconcile(60, None, cfg)["ok"] is True
    # facts per spread
    ok8, _ = facts_per_spread_valid(8, "KD-3", cfg)
    checks["facts_8_kd3_ok"] = ok8
    bad9, probs9 = facts_per_spread_valid(9, "KD-3", cfg)
    checks["facts_9_over_cap"] = (not bad9) and any("cap" in p for p in probs9)
    kd1bad, _ = facts_per_spread_valid(5, "KD-1", cfg)
    checks["facts_5_kd1_out_of_range"] = not kd1bad
    # dual source
    checks["two_sources_ok"] = dual_source_ok(2, cfg) is True
    checks["one_source_fail"] = dual_source_ok(1, cfg) is False
    # sidebar law: 40% of 10 spreads -> 4 allowed
    sb = sidebar_law(4, 10, cfg)
    checks["sidebar_4_of_10_ok"] = sb["ok"] and sb["max_allowed_spreads"] == 4
    checks["sidebar_5_of_10_fail"] = sidebar_law(5, 10, cfg)["ok"] is False
    # page parity + minimum
    ok_even, _ = page_count_valid(48, cfg)
    checks["page_valid_48"] = ok_even
    bad_odd, bad_probs = page_count_valid(23, cfg)
    checks["page_invalid_23"] = (not bad_odd) and len(bad_probs) == 2
    # color economics
    checks["color_premium_48"] = color_class(48, cfg) == "premium"
    checks["color_standard_80"] = color_class(80, cfg) == "standard"
    # bleed geometry (both trims)
    checks["bleed_letter"] = bleed_page_size(8.5, 11.0, cfg) == (8.625, 11.25)
    checks["bleed_square"] = bleed_page_size(8.5, 8.5, cfg) == (8.625, 8.75)
    # type floors
    checks["wow_floor_ab3"] = type_floor_ok("AB-3_KD-3", "callout_wow", 14, cfg) is True
    checks["wow_below_floor"] = type_floor_ok("AB-3_KD-3", "callout_wow", 13, cfg) is False
    checks["body_floor_ab1"] = type_floor_ok("AB-1_KD-1", "body", 18, cfg) is True
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
