"""AIRF 2.0 Journal Edition -- deterministic production operations for the Low-Content & Guided
Journals niche (OV-LOWC).

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_journal.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def subtitle_valid(title, subtitle, cfg=None):
    """Title+subtitle <= 200 chars; subtitle 50-150 chars. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    s = cfg["subtitle"]
    problems = []
    combined = len(title) + len(subtitle)
    if combined > s["title_plus_subtitle_max_chars"]:
        problems.append("title+subtitle %d chars exceeds %d"
                        % (combined, s["title_plus_subtitle_max_chars"]))
    if len(subtitle) < s["subtitle_min_chars"] or len(subtitle) > s["subtitle_max_chars"]:
        problems.append("subtitle %d chars outside %d-%d"
                        % (len(subtitle), s["subtitle_min_chars"], s["subtitle_max_chars"]))
    return (not problems, problems)


def interior_pages(units, pages_per_unit):
    """Repetition arithmetic: units * pages_per_unit (e.g. 110 spreads * 2 = 220)."""
    if units < 0 or pages_per_unit < 1:
        raise ValueError("units >= 0 and pages_per_unit >= 1 required")
    return units * pages_per_unit


def page_total(units, pages_per_unit, front_matter_pages, special_pages, padding_pages=0):
    """Total interior page count = front matter + repeating units + special pages + padding."""
    return (front_matter_pages + interior_pages(units, pages_per_unit)
            + special_pages + padding_pages)


def check_page_band(tier, pages, cfg=None):
    """Compare a projected page total to the tier's KDP page band. Returns a dict."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if tier not in bands or tier == "kdp_minimum_pages" or tier == "never_publish_near_minimum":
        raise ValueError("unknown tier %r (expected TIER_1/TIER_2/TIER_3)" % (tier,))
    band = bands[tier]
    kdp_min = bands["kdp_minimum_pages"]
    within = band["min"] <= pages <= band["max"]
    return {
        "ok": within,
        "tier": tier,
        "pages": pages,
        "band": [band["min"], band["max"]],
        "below_kdp_minimum": pages < kdp_min,
        "near_minimum": pages < kdp_min * 2,
    }


def line_spacing_ok(audience, spacing_in, cfg=None):
    """Physically-writable line spacing: adult 0.28-0.32 in; senior/child >= 0.5 in."""
    cfg = cfg or load_config()
    ls = cfg["line_spacing_in"]
    a = audience.lower()
    if a == "adult":
        return ls["adult_min"] <= spacing_in <= ls["adult_max"]
    if a in ("senior", "child"):
        return spacing_in >= ls["senior_child_min"]
    raise ValueError("unknown audience %r (expected adult/senior/child)" % (audience,))


def gutter_for(page_count, cfg=None):
    """Gutter inches by page count. Framework fixes 0.375 in under 150 pages; above that,
    defer to the live KDP margin table (returns None to signal a manual lookup)."""
    cfg = cfg or load_config()
    if page_count < 150:
        return cfg["margins"]["gutter_in_under_150_pages"]
    return None


def spread_alignment(pages_per_unit, front_matter_pages):
    """Verso/recto parity for a two-page spread unit. The unit's left (verso) page must land
    on a left-hand (even physical) page; physical page 1 is always a recto. Returns a dict
    with any padding needed so the first unit opens correctly. One-page units are unconstrained.
    """
    if pages_per_unit == 1:
        return {"aligned": True, "padding_pages_needed": 0, "constrained": False}
    first_interior_physical = front_matter_pages + 1
    # left/verso page == even physical position
    aligned = (first_interior_physical % 2 == 0)
    return {
        "aligned": aligned,
        "padding_pages_needed": 0 if aligned else 1,
        "constrained": True,
        "first_interior_physical_page": first_interior_physical,
    }


def selftest():
    cfg = load_config()
    checks = {}

    ok, _ = subtitle_valid(
        "Blood Pressure Log Book",
        "Undated Daily Log with 110 Guided Entry Pages, Large Print 8.5 x 11 for Seniors", cfg)
    checks["subtitle_ok"] = ok
    bad_ok, bad_probs = subtitle_valid("Tiny Title", "Too short", cfg)
    checks["subtitle_too_short_flagged"] = (not bad_ok) and len(bad_probs) >= 1

    checks["interior_pages_spread"] = interior_pages(110, 2) == 220
    # 110 two-page units + 6 front + 8 special = 234
    checks["page_total"] = page_total(110, 2, 6, 8) == 234

    band = check_page_band("TIER_3", 190, cfg)
    checks["tier3_band_ok"] = band["ok"] and not band["below_kdp_minimum"]
    checks["tier1_over_band"] = check_page_band("TIER_1", 200, cfg)["ok"] is False
    checks["below_kdp_min_flagged"] = check_page_band("TIER_1", 20, cfg)["below_kdp_minimum"] is True

    checks["adult_spacing_ok"] = line_spacing_ok("adult", 0.30, cfg) is True
    checks["adult_spacing_tight_fail"] = line_spacing_ok("adult", 0.20, cfg) is False
    checks["senior_spacing_ok"] = line_spacing_ok("senior", 0.5, cfg) is True
    checks["senior_spacing_tight_fail"] = line_spacing_ok("senior", 0.32, cfg) is False

    checks["gutter_under_150"] = gutter_for(120, cfg) == 0.375
    checks["gutter_over_150_manual"] = gutter_for(180, cfg) is None

    # 1-page unit: unconstrained
    checks["single_unit_unconstrained"] = spread_alignment(1, 6)["constrained"] is False
    # 6 front matter pages -> first interior physical page 7 (recto/odd) -> misaligned, need 1 pad
    a6 = spread_alignment(2, 6)
    checks["spread_even_front_needs_pad"] = (a6["aligned"] is False and a6["padding_pages_needed"] == 1)
    # 5 front matter pages -> first interior physical page 6 (verso/even) -> aligned
    a5 = spread_alignment(2, 5)
    checks["spread_odd_front_aligned"] = (a5["aligned"] is True and a5["padding_pages_needed"] == 0)

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
