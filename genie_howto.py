"""AIRF 2.0 How-To Edition -- deterministic production operations for the how-to niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_howto.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def classify_book_size(chapter_count, cfg=None):
    """Map a chapter count to its book size + page band + quick-win chapter.
    Ranges (inclusive) from SKILL.md 'Page-Band Targets': compact 8-12, standard
    13-20, extended 21-30. Raises for counts outside every band."""
    cfg = cfg or load_config()
    for size, spec in cfg["book_sizes"].items():
        lo, hi = spec["chapters"]
        if lo <= chapter_count <= hi:
            return {"size": size, "chapters": spec["chapters"],
                    "page_band": spec["pages"], "quick_win_chapter": spec["quick_win_chapter"]}
    raise ValueError("chapter_count %d fits no OV-HOWTO book size (8-30)" % chapter_count)


def quick_win_chapter(total_chapters, cfg=None):
    """Quick-Win chapter = the EARLIER of Chapter 3 or 20% of total chapters
    ('whichever comes first', SKILL.md Step 0-D) -> min(3, ceil(0.20 * n))."""
    cfg = cfg or load_config()
    if total_chapters < 1:
        raise ValueError("total_chapters must be >= 1")
    target = cfg["quick_win"]["target_chapter"]
    pct = cfg["quick_win"]["percent_of_chapters_alt"]
    return min(target, math.ceil(pct * total_chapters))


def zone_boundaries(total_chapters, cfg=None):
    """Three-Zone chapter boundaries (SKILL.md 'The Three-Zone Structure').
    Zone 1 = Ch 1-3 (Foundation & Quick Win). Zone 3 = final 1-2 chapters
    (~15%, clamped to 1..2). Zone 2 = everything between."""
    cfg = cfg or load_config()
    if total_chapters < 5:
        raise ValueError("OV-HOWTO books have >= 8 chapters; %d too small to zone" % total_chapters)
    zone3_count = min(2, max(1, round(cfg["zones"]["zone_3_mastery_continuation"]["share"] * total_chapters)))
    zone1_end = 3
    zone3_start = total_chapters - zone3_count + 1
    return {
        "zone_1": {"start": 1, "end": zone1_end},
        "zone_2": {"start": zone1_end + 1, "end": zone3_start - 1},
        "zone_3": {"start": zone3_start, "end": total_chapters, "count": zone3_count},
    }


def check_page_band(pages, chapter_count, cfg=None):
    """Is the projected page count within the band implied by the chapter count?"""
    cfg = cfg or load_config()
    band = classify_book_size(chapter_count, cfg)["page_band"]
    lo, hi = band
    return {"ok": lo <= pages <= hi, "pages": pages, "band": band}


def visual_density_for_domain(domain_code, cfg=None):
    """Heavy visual for physical-demonstration domains (trade, craft-skill, outdoor);
    moderate otherwise (SKILL.md Step 0-G, Visual Density)."""
    heavy = {"HOWTO-TRADE", "HOWTO-CRAFT-SKILL", "HOWTO-OUTDOOR"}
    key = "heavy" if domain_code in heavy else "moderate"
    return {"tier": key, "images": cfg["visual_density"][key]["images"] if cfg else
            load_config()["visual_density"][key]["images"]}


def appendix_complete(present_elements, cfg=None):
    """Verify all seven mandatory Appendix elements are present. Returns (ok, [missing])."""
    cfg = cfg or load_config()
    required = cfg["back_matter_appendix_elements"]
    have = set(present_elements)
    missing = [e for e in required if e not in have]
    return (not missing, missing)


def selftest():
    cfg = load_config()
    checks = {}
    # book-size classification
    checks["compact_10"] = classify_book_size(10, cfg)["size"] == "compact"
    checks["standard_16"] = classify_book_size(16, cfg)["size"] == "standard"
    checks["extended_25"] = classify_book_size(25, cfg)["size"] == "extended"
    checks["compact_band"] = classify_book_size(10, cfg)["page_band"] == [80, 150]
    # quick-win chapter: earlier of Ch3 or ceil(20% n)
    checks["qw_10_is_2"] = quick_win_chapter(10, cfg) == 2
    checks["qw_15_is_3"] = quick_win_chapter(15, cfg) == 3
    checks["qw_30_is_3"] = quick_win_chapter(30, cfg) == 3
    # zone boundaries
    z = zone_boundaries(20, cfg)
    checks["zone1_1_3"] = z["zone_1"] == {"start": 1, "end": 3}
    checks["zone3_count_2"] = z["zone_3"]["count"] == 2 and z["zone_3"]["end"] == 20
    checks["zone2_contiguous"] = z["zone_2"]["start"] == 4 and z["zone_2"]["end"] == z["zone_3"]["start"] - 1
    zc = zone_boundaries(10, cfg)
    checks["zone3_small_book"] = zc["zone_3"]["count"] in (1, 2) and zc["zone_2"]["start"] == 4
    # page band membership
    checks["page_band_ok"] = check_page_band(120, 10, cfg)["ok"] is True
    checks["page_band_breach"] = check_page_band(300, 10, cfg)["ok"] is False
    # visual density
    checks["trade_heavy"] = visual_density_for_domain("HOWTO-TRADE", cfg)["tier"] == "heavy"
    checks["digital_moderate"] = visual_density_for_domain("HOWTO-DIGITAL", cfg)["tier"] == "moderate"
    # appendix completeness
    full = cfg["back_matter_appendix_elements"]
    ok_all, missing_none = appendix_complete(full, cfg)
    checks["appendix_full_ok"] = ok_all and missing_none == []
    ok_part, missing_some = appendix_complete(full[:4], cfg)
    checks["appendix_partial_flagged"] = (not ok_part) and len(missing_some) == 3
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
