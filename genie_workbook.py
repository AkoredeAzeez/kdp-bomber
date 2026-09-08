"""AIRF 2.0 Workbook Edition -- deterministic production operations for the OV-WORK workbook niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture is
defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_workbook.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def validate_chapter_pages(pages, cfg=None):
    """Every chapter is EXACTLY 10 pages, not 9, not 11 (SKILL.md Rule 1). Returns (ok, required)."""
    cfg = cfg or load_config()
    req = cfg["practice_unit"]["pages_per_chapter_exact"]
    return (pages == req, req)


def difficulty_bands_ok(band_labels, cfg=None):
    """Exactly three difficulty bands, in order Foundation -> Development -> Mastery, must be
    present and labelled (SKILL.md Rule 2). Returns (ok, [problems])."""
    cfg = cfg or load_config()
    pu = cfg["practice_unit"]
    expected = [b.lower() for b in pu["band_labels"]]
    got = [b.strip().lower() for b in band_labels]
    problems = []
    if len(got) != pu["difficulty_bands_required"]:
        problems.append("found %d bands (must be %d)" % (len(got), pu["difficulty_bands_required"]))
    if got != expected:
        problems.append("band order %r != required %r" % (band_labels, pu["band_labels"]))
    return (not problems, problems)


def worksheet_share_ok(share_pct, cfg=None):
    """Worksheet share of a chapter must fall within 70-80% (SKILL.md Rule 7). Returns
    (ok, min, max)."""
    cfg = cfg or load_config()
    pu = cfg["practice_unit"]
    lo, hi = pu["worksheet_share_min_pct"], pu["worksheet_share_max_pct"]
    return (lo <= share_pct <= hi, lo, hi)


def exercise_types_ok(selected_types, cfg=None):
    """At least three exercise types per unit, all drawn from the six-type library (SKILL.md
    Rule 7). Returns (ok, [problems])."""
    cfg = cfg or load_config()
    pu = cfg["practice_unit"]
    library = set(pu["exercise_type_library"])
    problems = []
    distinct = set(selected_types)
    if len(distinct) < pu["exercise_types_per_unit_min"]:
        problems.append("only %d distinct exercise types (need >=%d)" % (
            len(distinct), pu["exercise_types_per_unit_min"]))
    for t in distinct:
        if t not in library:
            problems.append("exercise type %r not in the six-type library" % t)
    return (not problems, problems)


def unit_component_pages_ok(component_pages, cfg=None):
    """Validate a practice unit's component page allocation: each component within its configured
    min/max range and the total equal to the fixed 10-page unit. `component_pages` is
    {component_name: pages}. Returns (ok, [problems], total)."""
    cfg = cfg or load_config()
    pu = cfg["practice_unit"]
    ranges = {c["name"]: (c["pages_min"], c["pages_max"]) for c in pu["components"]}
    problems = []
    for name, pages in component_pages.items():
        if name not in ranges:
            problems.append("unknown component %r" % name)
            continue
        lo, hi = ranges[name]
        if pages < lo or pages > hi:
            problems.append("%s = %s pages (must be %s-%s)" % (name, pages, lo, hi))
    total = round(sum(component_pages.values()), 4)
    if total != pu["pages_per_chapter_exact"]:
        problems.append("component total %s != %d" % (total, pu["pages_per_chapter_exact"]))
    return (not problems, problems, total)


def project_pages(chapter_count, appendix_pages, cfg=None):
    """Project total book pages: front matter + Introduction + chapters*10 + Conclusion +
    appendices (incl. the worked-solutions answer key) (SKILL.md Phase 0 step 6). Returns total."""
    cfg = cfg or load_config()
    pb = cfg["page_budget"]
    return round(
        pb["front_matter_pages"] + pb["introduction_pages"]
        + chapter_count * pb["chapter_pages_each"] + pb["conclusion_pages"]
        + appendix_pages, 4)


def page_budget_ok(total_pages, cfg=None):
    """Total must not exceed the 150-page hard cap (SKILL.md Rule 6). Returns (ok, cap)."""
    cfg = cfg or load_config()
    cap = cfg["page_budget"]["book_hard_cap_pages"]
    return (total_pages <= cap, cap)


def max_chapters(appendix_pages, cfg=None):
    """Maximum chapter count that still fits under the 150-page cap for a given appendix weight.
    total = front + intro + C*10 + conclusion + appendix <= cap."""
    cfg = cfg or load_config()
    pb = cfg["page_budget"]
    fixed = pb["front_matter_pages"] + pb["introduction_pages"] + pb["conclusion_pages"] + appendix_pages
    room = cfg["page_budget"]["book_hard_cap_pages"] - fixed
    return max(0, int(math.floor(room / pb["chapter_pages_each"])))


def subtitle_ok(title, subtitle, cfg=None):
    """Title + subtitle combined <=200 chars, and the subtitle itself 50-150 chars (SKILL.md
    Phase 0 step 4). Returns (ok, [problems], combined_len, subtitle_len)."""
    cfg = cfg or load_config()
    s = cfg["subtitle"]
    combined = len((title or "").strip()) + len((subtitle or "").strip())
    sub_len = len((subtitle or "").strip())
    problems = []
    if combined > s["title_plus_subtitle_char_max"]:
        problems.append("title+subtitle %d chars > %d" % (combined, s["title_plus_subtitle_char_max"]))
    if sub_len < s["subtitle_char_min"] or sub_len > s["subtitle_char_max"]:
        problems.append("subtitle %d chars (must be %d-%d)" % (
            sub_len, s["subtitle_char_min"], s["subtitle_char_max"]))
    return (not problems, problems, combined, sub_len)


def copyright_components_ok(component_words, cfg=None):
    """Validate the copyright/disclaimer page components against their word ranges (SKILL.md
    front matter, ~400 words total across five components). `component_words` is
    {component_name: word_count}. Returns (ok, [problems], total)."""
    cfg = cfg or load_config()
    ranges = {c["name"]: (c["words_min"], c["words_max"]) for c in cfg["front_matter"]["copyright_components"]}
    problems = []
    for name, (lo, hi) in ranges.items():
        if name not in component_words:
            problems.append("missing component %r" % name)
            continue
        w = component_words[name]
        if w < lo or w > hi:
            problems.append("%s = %d words (must be %d-%d)" % (name, w, lo, hi))
    total = sum(component_words.values())
    return (not problems, problems, total)


def selftest():
    cfg = load_config()
    checks = {}

    checks["chapter_10_ok"] = validate_chapter_pages(10, cfg)[0]
    checks["chapter_11_flagged"] = not validate_chapter_pages(11, cfg)[0]

    checks["bands_ok"] = difficulty_bands_ok(["Foundation", "Development", "Mastery"], cfg)[0]
    bad_bands_ok, bad_bands_probs = difficulty_bands_ok(["Foundation", "Mastery"], cfg)
    checks["bands_flagged"] = (not bad_bands_ok) and len(bad_bands_probs) >= 1

    checks["share_75_ok"] = worksheet_share_ok(75, cfg)[0]
    checks["share_60_flagged"] = not worksheet_share_ok(60, cfg)[0]
    checks["share_85_flagged"] = not worksheet_share_ok(85, cfg)[0]

    checks["types_ok"] = exercise_types_ok(["fill_in", "short_answer", "applied_scenario_case"], cfg)[0]
    checks["types_too_few_flagged"] = not exercise_types_ok(["fill_in", "short_answer"], cfg)[0]
    checks["types_unknown_flagged"] = not exercise_types_ok(
        ["fill_in", "short_answer", "essay"], cfg)[0]

    comp = {
        "concept_briefing": 1.0, "band_1_foundation": 2.75, "band_2_development": 3.0,
        "band_3_mastery": 2.75, "unit_checkpoint": 0.5}
    ok_comp, probs_comp, total_comp = unit_component_pages_ok(comp, cfg)
    checks["unit_components_ok"] = ok_comp and total_comp == 10
    bad_comp = dict(comp)
    bad_comp["unit_checkpoint"] = 1.5  # out of range and breaks the 10-page total
    checks["unit_components_flagged"] = not unit_component_pages_ok(bad_comp, cfg)[0]

    # 12 chapters + 20-page appendix = 6 + 2 + 120 + 1.5 + 20 = 149.5, under cap
    total = project_pages(12, 20, cfg)
    checks["project_149_5"] = total == 149.5
    checks["budget_ok"] = page_budget_ok(total, cfg)[0]
    # 14 chapters + 20 appendix = 159.5, over cap
    checks["budget_breach_flagged"] = not page_budget_ok(project_pages(14, 20, cfg), cfg)[0]

    # max chapters for a 20-page appendix: (150 - 6 - 2 - 1.5 - 20)/10 = 12.05 -> 12
    checks["max_chapters_20app"] = max_chapters(20, cfg) == 12
    checks["max_chapters_minimal_app"] = max_chapters(0, cfg) == 14

    ok_sub, _, combined, sub_len = subtitle_ok(
        "Anatomy Practice Workbook",
        "300 Labelled Exercises Across Three Difficulty Bands with Complete Worked Answer Key", cfg)
    checks["subtitle_ok"] = ok_sub and combined <= 200 and 50 <= sub_len <= 150
    checks["subtitle_short_flagged"] = not subtitle_ok("Title", "Too short", cfg)[0]

    cw = {
        "copyright_notice": 60, "general_disclaimer_liability": 175,
        "educational_use_statement": 85, "professional_advice_notice": 60, "publication_info": 35}
    ok_cw, _, total_cw = copyright_components_ok(cw, cfg)
    checks["copyright_ok"] = ok_cw and 350 <= total_cw <= 450
    checks["copyright_flagged"] = not copyright_components_ok(
        {"copyright_notice": 10, "general_disclaimer_liability": 175,
         "educational_use_statement": 85, "professional_advice_notice": 60,
         "publication_info": 35}, cfg)[0]

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
