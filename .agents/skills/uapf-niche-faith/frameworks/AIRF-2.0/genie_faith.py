"""AIRF 2.0 -- deterministic production operations for the Faith & Devotional niche
(OV-FAITH).

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

Note: the niche is prose-heavy and most gates are manual (doctrinal/theological/live-verification),
but a few rules are genuinely computable count/limit/budget math: the declared-unit-count
contract, part-partition sums, reflection/prayer word bands, modern-translation verse limits, and
the part-opener image count. Those live here.

CLI:  python genie_faith.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def validate_unit_count(declared, actual):
    """Hard contract: a book whose title declares N units must contain exactly N complete units."""
    return {"ok": declared == actual, "declared": declared, "actual": actual}


def parts_partition_ok(parts, declared_unit_count):
    """Part/section groupings must add up to the total declared unit count. `parts` is a list of
    per-part unit counts. Returns (ok, sum)."""
    total = sum(parts)
    return (total == declared_unit_count, total)


def suggested_partitions(unit_count, cfg=None):
    """Return the framework's suggested [parts, units_per_part] groupings for a known unit count
    (null units_per_part means 'themed', size not fixed). Empty list if none suggested."""
    cfg = cfg or load_config()
    table = cfg["chapter_architecture"]["part_groupings"]
    return table.get(str(int(unit_count)), [])


def word_band_check(component, word_count, cfg=None):
    """Word-count band per component: reflection 200-350, prayer 50-120, unit 450-600."""
    cfg = cfg or load_config()
    u = cfg["unit_daily_devotional"]
    bands = {
        "reflection": (u["reflection_words_min"], u["reflection_words_max"]),
        "prayer": (u["prayer_words_min"], u["prayer_words_max"]),
        "unit": (u["unit_words_min"], u["unit_words_max"]),
    }
    key = component.lower()
    if key not in bands:
        raise ValueError("unknown component %r (expected reflection/prayer/unit)" % (component,))
    lo, hi = bands[key]
    return {"ok": lo <= word_count <= hi, "component": key, "band": [lo, hi], "count": word_count}


def translation_verse_limit_ok(translation, verse_count, cfg=None):
    """Check a quoted verse count against modern-translation limits. Public-domain translations are
    unlimited; modern translations with a stated limit are compared; modern translations without a
    numeric limit here require a manual permission check (ok=None)."""
    cfg = cfg or load_config()
    sc = cfg["scripture_copyright"]
    t = translation.upper()
    pd = [x.split()[0].upper() for x in sc["public_domain"]]
    if t in pd:
        return {"ok": True, "translation": translation, "limit": None, "public_domain": True}
    limits = {k.upper(): v for k, v in sc["modern_verse_limits"].items()}
    if t in limits:
        lim = limits[t]
        return {"ok": verse_count <= lim, "translation": translation, "limit": lim,
                "public_domain": False}
    # modern, permission-gated, no numeric limit encoded -> manual clearance required
    return {"ok": None, "translation": translation, "limit": None, "public_domain": False,
            "requires_manual_clearance": True}


def page_band(book_format, cfg=None):
    """Return the [min, max] page band for a format key (unit count as string, or a named format)."""
    cfg = cfg or load_config()
    bands = cfg["page_bands_6x9_tnr"]
    key = str(book_format)
    if key not in bands or key == "verify_against_live_competitor_research":
        raise ValueError("unknown format %r" % (book_format,))
    return bands[key]


def part_opener_image_count(page_count, part_count, cfg=None):
    """One image per part opener, at ANY page count (global Rule 11 -- page count never gates
    image generation). page_count is accepted for signature stability but does not reduce count."""
    if part_count < 0:
        raise ValueError("part_count must be >= 0")
    return part_count


def selftest():
    cfg = load_config()
    checks = {}

    checks["unit_count_ok"] = validate_unit_count(90, 90)["ok"] is True
    checks["unit_count_short_fail"] = validate_unit_count(90, 88)["ok"] is False

    ok90, total90 = parts_partition_ok([30, 30, 30], 90)
    checks["parts_sum_ok"] = ok90 and total90 == 90
    bad_ok, _ = parts_partition_ok([10, 10, 5], 30)
    checks["parts_sum_fail"] = bad_ok is False
    checks["suggested_90"] = suggested_partitions(90, cfg) == [[3, 30], [9, 10]]
    checks["suggested_unknown_empty"] = suggested_partitions(45, cfg) == []

    checks["reflection_ok"] = word_band_check("reflection", 300, cfg)["ok"] is True
    checks["reflection_short_fail"] = word_band_check("reflection", 150, cfg)["ok"] is False
    checks["prayer_ok"] = word_band_check("prayer", 90, cfg)["ok"] is True
    checks["prayer_long_fail"] = word_band_check("prayer", 200, cfg)["ok"] is False
    checks["unit_ok"] = word_band_check("unit", 520, cfg)["ok"] is True

    checks["kjv_unlimited"] = translation_verse_limit_ok("KJV", 5000, cfg)["ok"] is True
    checks["niv_under_limit"] = translation_verse_limit_ok("NIV", 400, cfg)["ok"] is True
    checks["niv_over_limit"] = translation_verse_limit_ok("NIV", 600, cfg)["ok"] is False
    checks["esv_limit"] = translation_verse_limit_ok("ESV", 1000, cfg)["limit"] == 1000
    checks["nasb_manual"] = translation_verse_limit_ok("NASB", 100, cfg)["ok"] is None

    checks["page_band_90"] = page_band("90", cfg) == [200, 280]
    checks["page_band_named"] = page_band("Prayer Journal", cfg) == [120, 180]

    # Rule 11: one image per part opener at ANY page count (130p and 220p both full count)
    checks["images_short_book"] = part_opener_image_count(130, 3, cfg) == 3
    checks["images_long_book"] = part_opener_image_count(220, 5, cfg) == 5

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
