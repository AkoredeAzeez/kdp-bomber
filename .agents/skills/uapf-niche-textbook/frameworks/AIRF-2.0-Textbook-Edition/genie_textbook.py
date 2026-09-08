"""AIRF 2.0 Textbook Edition -- deterministic production operations for the Academic & Professional Textbook
niche (OV-TEXT / UTF 1.0).

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture,
domain reasoning, or citation judgement is defined here; SKILL.md remains the source of truth. These
functions only check the numeric/structural constants the SKILL.md already states (domain validity,
subtitle length, per-chapter and total page bands, objective/section/feature-box counts, visual
level buckets, opener/close word ranges, answer-key coverage, engineering image points).

CLI:  python genie_textbook.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def validate_domain(domain, cfg=None):
    """True if `domain` is one of the nine Discipline Adaptation Engine domains."""
    cfg = cfg or load_config()
    return domain in cfg["domains"]


def subtitle_length_valid(title, subtitle, cfg=None):
    """Combined title+subtitle must be under the KDP character cap (200)."""
    cfg = cfg or load_config()
    cap = cfg["subtitle"]["combined_char_max"]
    return (len(title) + len(subtitle)) < cap


def _page_band_key(domain, config_key=None, cfg=None):
    cfg = cfg or load_config()
    if config_key:
        return config_key
    return "engineering" if domain == "Engineering" else "default"


def validate_chapter_pages(pages, domain=None, config_key=None, cfg=None):
    """Validate a single chapter's page count for the active configuration.
    Engineering: pages >= 23 (no upper bound at chapter level). Others: within the band."""
    cfg = cfg or load_config()
    key = _page_band_key(domain, config_key, cfg)
    band = cfg["page_bands"][key]
    if key == "engineering":
        return pages >= band["per_chapter_min"]
    lo, hi = band["per_chapter"]
    return lo <= pages <= hi


def validate_total_pages(total, domain=None, config_key=None, cfg=None):
    """Validate the whole-book page count against the active total band."""
    cfg = cfg or load_config()
    key = _page_band_key(domain, config_key, cfg)
    lo, hi = cfg["page_bands"][key]["total"]
    return lo <= total <= hi


def validate_chapter_count(n, domain=None, config_key=None, cfg=None):
    """Validate the chapter count against the active band."""
    cfg = cfg or load_config()
    key = _page_band_key(domain, config_key, cfg)
    lo, hi = cfg["page_bands"][key]["chapters"]
    return lo <= n <= hi


def validate_objective_count(n, cfg=None):
    """Learning objectives per chapter must be 3-5."""
    cfg = cfg or load_config()
    f = cfg["chapter_formula"]
    return f["learning_objectives_min"] <= n <= f["learning_objectives_max"]


def validate_section_count(n, cfg=None):
    """Major numbered X.Y sections per chapter must be 3-5."""
    cfg = cfg or load_config()
    f = cfg["chapter_formula"]
    return f["major_sections_min"] <= n <= f["major_sections_max"]


def validate_feature_box_count(n, cfg=None):
    """Locked feature-box devices must be 3-5."""
    cfg = cfg or load_config()
    f = cfg["chapter_formula"]
    return f["feature_boxes_min"] <= n <= f["feature_boxes_max"]


def word_count_in_range(words, which="opener", cfg=None):
    """Opener/close narrative must be 500-750 words. `words` is an integer count."""
    cfg = cfg or load_config()
    lo, hi = cfg["chapter_formula"]["%s_words" % which]
    return lo <= words <= hi


def visual_level_bucket(count, cfg=None):
    """Map a planned figure count to its visual-level bucket name, or None if it falls in a gap."""
    cfg = cfg or load_config()
    v = cfg["visual_levels"]
    if count >= v["EXTENSIVE_min"]:
        return "EXTENSIVE"
    for name in ("MINIMAL", "MODERATE", "ABUNDANT"):
        lo, hi = v[name]
        if lo <= count <= hi:
            return name
    return None


def answer_key_coverage(assessment_item_count, solution_count, domain=None, cfg=None):
    """Answer-key rule. Engineering has no assessment: valid only when there are zero items and no
    key is expected. All other domains: every assessment item needs a worked solution (100%).
    Returns (ok, [problems])."""
    cfg = cfg or load_config()
    problems = []
    if domain == "Engineering":
        if assessment_item_count != 0:
            problems.append("Engineering domain carries no assessment, but %d items present"
                            % assessment_item_count)
        return (not problems, problems)
    if assessment_item_count > 0 and solution_count < assessment_item_count:
        problems.append("answer key covers %d of %d items (100%% coverage required)"
                        % (solution_count, assessment_item_count))
    return (not problems, problems)


def engineering_image_points(subchapter_count):
    """Engineering minimum image count = one realistic photographic image per subchapter."""
    if subchapter_count < 0:
        raise ValueError("subchapter_count must be >= 0")
    return subchapter_count


def selftest():
    cfg = load_config()
    checks = {}
    # domain
    checks["domain_ok"] = validate_domain("Engineering", cfg) is True
    checks["domain_bad"] = validate_domain("Cooking", cfg) is False
    # subtitle length
    checks["subtitle_ok"] = subtitle_length_valid("Fundamentals of Thermodynamics",
                                                   "A Course for Undergraduates", cfg) is True
    checks["subtitle_bad"] = subtitle_length_valid("T" * 150, "S" * 60, cfg) is False
    # chapter pages
    checks["ch_default_ok"] = validate_chapter_pages(25, domain="STEM") is True
    checks["ch_default_bad"] = validate_chapter_pages(31, domain="STEM") is False
    checks["ch_eng_ok"] = validate_chapter_pages(23, domain="Engineering") is True
    checks["ch_eng_bad"] = validate_chapter_pages(22, domain="Engineering") is False
    # total pages
    checks["total_default_ok"] = validate_total_pages(300, domain="Business") is True
    checks["total_eng_ok"] = validate_total_pages(500, domain="Engineering") is True
    checks["total_eng_bad"] = validate_total_pages(390, domain="Engineering") is False
    checks["total_compact_ok"] = validate_total_pages(250, config_key="compact_professional_reference") is True
    # chapter count
    checks["chapters_eng_ok"] = validate_chapter_count(16, domain="Engineering") is True
    checks["chapters_eng_bad"] = validate_chapter_count(13, domain="Engineering") is False
    # per-chapter structural counts
    checks["obj_ok"] = validate_objective_count(4, cfg) is True
    checks["obj_bad"] = validate_objective_count(6, cfg) is False
    checks["sec_ok"] = validate_section_count(3, cfg) is True
    checks["sec_bad"] = validate_section_count(2, cfg) is False
    checks["box_ok"] = validate_feature_box_count(5, cfg) is True
    checks["box_bad"] = validate_feature_box_count(6, cfg) is False
    # word ranges
    checks["opener_ok"] = word_count_in_range(600, "opener", cfg) is True
    checks["close_bad"] = word_count_in_range(800, "close", cfg) is False
    # visual buckets
    checks["visual_minimal"] = visual_level_bucket(7, cfg) == "MINIMAL"
    checks["visual_extensive"] = visual_level_bucket(75, cfg) == "EXTENSIVE"
    checks["visual_gap"] = visual_level_bucket(12, cfg) is None
    # answer key coverage
    ok_full, _ = answer_key_coverage(40, 40, domain="STEM", cfg=cfg)
    checks["ak_full"] = ok_full is True
    ok_short, probs_short = answer_key_coverage(40, 39, domain="STEM", cfg=cfg)
    checks["ak_short_fail"] = (ok_short is False) and len(probs_short) == 1
    ok_eng, _ = answer_key_coverage(0, 0, domain="Engineering", cfg=cfg)
    checks["ak_eng_zero"] = ok_eng is True
    ok_eng_bad, _ = answer_key_coverage(5, 0, domain="Engineering", cfg=cfg)
    checks["ak_eng_has_items_fail"] = ok_eng_bad is False
    # engineering image points
    checks["eng_images"] = engineering_image_points(48) == 48
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
