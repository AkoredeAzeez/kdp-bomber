"""AIRF 2.0 Popular Science Edition -- deterministic production operations for the Popular Science niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture is
defined here; SKILL.md remains the source of truth for reasoning/consensus/verification. The
niche's load-bearing rules are editorial (consensus discipline, analogy-breaks law, evidence-story
integrity, mysticism sweep) and stay manual; only word/count budgets and structural-completeness
checks are computable and live here.

CLI:  python genie_popular_science.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def check_chapter_words(words, cfg=None):
    """A single explainer chapter must be 3,500-5,500 words. (SKILL.md 'Chapter specs'.)"""
    cfg = cfg or load_config()
    lo, hi = cfg["chapter"]["words_min"], cfg["chapter"]["words_max"]
    return {"ok": lo <= words <= hi, "words": words, "band": [lo, hi]}


def check_manuscript_plan(chapter_count, total_words, cfg=None):
    """Chapter count 12-18 and total 55,000-80,000 words, with the total internally feasible
    against the per-chapter band (chapter_count x [min,max] must bracket the total)."""
    cfg = cfg or load_config()
    c = cfg["chapter"]
    problems = []
    if not (c["count_min"] <= chapter_count <= c["count_max"]):
        problems.append("chapter_count %d outside %d-%d" % (
            chapter_count, c["count_min"], c["count_max"]))
    if not (c["total_words_min"] <= total_words <= c["total_words_max"]):
        problems.append("total_words %d outside %d-%d" % (
            total_words, c["total_words_min"], c["total_words_max"]))
    feasible_lo = chapter_count * c["words_min"]
    feasible_hi = chapter_count * c["words_max"]
    if not (feasible_lo <= total_words <= feasible_hi):
        problems.append("total_words %d not feasible for %d chapters at %d-%d each (%d-%d)" % (
            total_words, chapter_count, c["words_min"], c["words_max"], feasible_lo, feasible_hi))
    return {"ok": not problems, "chapter_count": chapter_count, "total_words": total_words,
            "feasible_band": [feasible_lo, feasible_hi], "problems": problems}


def check_subtitle(combined_chars, cfg=None):
    """Title+subtitle combined must be <=200 characters. (SKILL.md '0.3 Subtitle generation'.)"""
    cfg = cfg or load_config()
    limit = cfg["phase0"]["subtitle_max_combined_chars"]
    return {"ok": combined_chars <= limit, "chars": combined_chars, "limit": limit}


def check_central_question_inventory(count, cfg=None):
    """Central-question inventory must hold 10-20 genuine reader questions. (SKILL.md '0.2'.)"""
    cfg = cfg or load_config()
    lo, hi = cfg["phase0"]["central_question_inventory"]
    return {"ok": lo <= count <= hi, "count": count, "band": [lo, hi]}


def explainer_stages_complete(stages_present, cfg=None):
    """Every chapter must carry all six explainer stages, no stage skipped. Returns ok plus any
    missing/unknown stages. (SKILL.md 'Book Architecture'; Rule #2.)"""
    cfg = cfg or load_config()
    required = cfg["chapter"]["explainer_stages"]
    present = set(stages_present)
    missing = [s for s in required if s not in present]
    unknown = [s for s in present if s not in required]
    return {"ok": not missing, "missing": missing, "unknown": unknown, "required": required}


def check_visual_level(figure_count, level, cfg=None):
    """Figure count must fall within the locked visual level band (MODERATE 15-25 / ABUNDANT 30-50)."""
    cfg = cfg or load_config()
    bands = cfg["visual_level"]
    if level not in ("MODERATE", "ABUNDANT"):
        raise ValueError("level must be MODERATE or ABUNDANT, got %r" % (level,))
    lo, hi = bands[level]
    return {"ok": lo <= figure_count <= hi, "figure_count": figure_count, "level": level, "band": [lo, hi]}


def field_guide_entry_complete(fields_present, cfg=None):
    """Field-guide identification entry must carry every locked field. Returns ok plus missing
    fields. (SKILL.md 'FIELD-GUIDE VARIANT'; Rule #7 for taxonomy currency.)"""
    cfg = cfg or load_config()
    required = cfg["field_guide_variant"]["entry_fields_in_order"]
    present = set(fields_present)
    missing = [f for f in required if f not in present]
    return {"ok": not missing, "missing": missing, "required": required}


def selftest():
    cfg = load_config()
    checks = {}

    checks["chapter_words_ok"] = check_chapter_words(4500, cfg)["ok"] is True
    checks["chapter_words_short_fail"] = check_chapter_words(3000, cfg)["ok"] is False
    checks["chapter_words_long_fail"] = check_chapter_words(6000, cfg)["ok"] is False

    # 15 chapters, 67,500 words -> feasible (15*[3500,5500]=52500-82500) and in 55k-80k band.
    mp = check_manuscript_plan(15, 67500, cfg)
    checks["manuscript_plan_ok"] = mp["ok"] is True
    # 12 chapters but 90,000 words -> above total band and infeasible.
    checks["manuscript_plan_over_fail"] = check_manuscript_plan(12, 90000, cfg)["ok"] is False
    # 20 chapters -> chapter count out of range.
    checks["manuscript_plan_count_fail"] = check_manuscript_plan(20, 70000, cfg)["ok"] is False

    checks["subtitle_ok"] = check_subtitle(180, cfg)["ok"] is True
    checks["subtitle_over_fail"] = check_subtitle(220, cfg)["ok"] is False

    checks["cq_ok"] = check_central_question_inventory(15, cfg)["ok"] is True
    checks["cq_low_fail"] = check_central_question_inventory(8, cfg)["ok"] is False

    all_stages = ["hook_question", "intuition_building", "mechanism",
                  "evidence_story", "implications", "wonder_payoff"]
    checks["stages_complete"] = explainer_stages_complete(all_stages, cfg)["ok"] is True
    miss = explainer_stages_complete(all_stages[:-1], cfg)
    checks["stages_missing_flagged"] = (not miss["ok"]) and miss["missing"] == ["wonder_payoff"]

    checks["visual_moderate_ok"] = check_visual_level(20, "MODERATE", cfg)["ok"] is True
    checks["visual_abundant_low_fail"] = check_visual_level(20, "ABUNDANT", cfg)["ok"] is False

    fg_fields = cfg["field_guide_variant"]["entry_fields_in_order"]
    checks["field_guide_complete"] = field_guide_entry_complete(fg_fields, cfg)["ok"] is True
    fgm = field_guide_entry_complete(fg_fields[:-1], cfg)
    checks["field_guide_missing_flagged"] = (not fgm["ok"]) and len(fgm["missing"]) == 1

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
