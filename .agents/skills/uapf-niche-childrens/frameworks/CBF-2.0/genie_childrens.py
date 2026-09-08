"""CBF 2.0 -- deterministic production operations for the children's-book niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_childrens.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def bleed_page_size(trim_w_in, trim_h_in, cfg=None):
    """Bleed page size = trim + 0.125 in width, + 0.25 in height (SKILL.md Interior Design).
    8.5 x 8.5 trim -> 8.625 x 8.75 bleed page."""
    cfg = cfg or load_config()
    g = cfg["trim_geometry"]
    return (round(trim_w_in + g["bleed_add_width_in"], 4),
            round(trim_h_in + g["bleed_add_height_in"], 4))


def page_count_valid(pages, cfg=None):
    """KDP paperback: page count must be even and >= the KDP minimum (24)."""
    cfg = cfg or load_config()
    r = cfg["print_release"]
    problems = []
    if pages % 2 != 0:
        problems.append("page count %d is not even" % pages)
    if pages < r["kdp_min_pages"]:
        problems.append("page count %d below KDP minimum %d" % (pages, r["kdp_min_pages"]))
    return (not problems, problems)


def color_class(pages, cfg=None):
    """Ink economics: standard color activates at 72 pages; below that KDP prints premium color."""
    cfg = cfg or load_config()
    threshold = cfg["color"]["standard_color_starts_page"]
    return "standard" if pages >= threshold else "premium"


def band_type_floor(band, cfg=None):
    """Return the [min_pt, max_pt] type floor for an age band (AB-0..AB-3)."""
    cfg = cfg or load_config()
    bands = cfg["age_bands"]
    if band not in bands:
        raise ValueError("unknown band %r (allowed: %s)" % (band, list(bands)))
    return bands[band]["type_floor_pt"]


def type_floor_ok(band, point_size, cfg=None):
    """A page's body point size is valid only if it is at or above the band's floor minimum."""
    floor_min = band_type_floor(band, cfg)[0]
    return point_size >= floor_min


def guest_insert_max_pages(total_pages, cfg=None):
    """Guest inserts (activity spread in a picture book, etc.) never exceed one-third of pages."""
    cfg = cfg or load_config()
    frac = cfg["guest_insert_max_fraction"]
    return math.floor(total_pages * frac)


def selftest():
    cfg = load_config()
    checks = {}
    # bleed geometry: 8.5x8.5 -> 8.625x8.75 (the worked example in SKILL.md)
    checks["bleed_square"] = bleed_page_size(8.5, 8.5, cfg) == (8.625, 8.75)
    # page parity + minimum
    ok_even, _ = page_count_valid(32, cfg)
    checks["page_valid_32"] = ok_even
    odd_ok, odd_probs = page_count_valid(23, cfg)
    checks["page_invalid_23"] = (not odd_ok) and len(odd_probs) == 2  # odd AND below 24
    # color economics
    checks["color_premium_under_72"] = color_class(48, cfg) == "premium"
    checks["color_standard_at_72"] = color_class(72, cfg) == "standard"
    # type floors
    checks["floor_ab0"] = band_type_floor("AB-0", cfg) == [24, 36]
    checks["floor_ab3"] = band_type_floor("AB-3", cfg) == [11, 14]
    checks["type_floor_ok_true"] = type_floor_ok("AB-1", 18, cfg) is True
    checks["type_floor_ok_false"] = type_floor_ok("AB-1", 16, cfg) is False
    # guest insert cap (one-third)
    checks["guest_cap_32"] = guest_insert_max_pages(32, cfg) == 10
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
