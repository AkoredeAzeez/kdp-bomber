"""AIRF 2.0 Humor Edition -- deterministic production operations for the Humor & Comedy niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture, voice, or design judgment is defined here; SKILL.md remains the source of truth.

CLI:  python genie_humor.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def combined_title_len_ok(title, subtitle, cfg=None):
    """Combined title + subtitle must stay within the KDP metadata char limit (200)."""
    cfg = cfg or load_config()
    limit = cfg["title"]["combined_title_subtitle_max_chars"]
    # Combined length as the concatenated metadata field (title + separator + subtitle).
    combined = len(title) + len(subtitle)
    return {"ok": combined <= limit, "chars": combined, "limit": limit}


def score_slot(demand, differentiation, seasonal_fit, price_band_health,
               category_access, cfg=None):
    """Score a Phase 0 slot on the five-criteria rubric and return the mandated decision.

    Returns dict with total, decision in {proceed, proceed_with_justification, kill},
    and any range/zero problems. Decision logic (SKILL.md Phase 0.5):
      - 7+ and no zero in demand or differentiation -> proceed
      - 5 to 6                                       -> proceed_with_justification
      - 4 or below                                   -> kill
    A zero in demand or differentiation forbids a plain 'proceed'.
    """
    cfg = cfg or load_config()
    r = cfg["scoring_rubric"]
    crit = r["criteria"]
    scores = {
        "demand": demand, "differentiation": differentiation,
        "seasonal_fit": seasonal_fit, "price_band_health": price_band_health,
        "category_access": category_access,
    }
    problems = []
    for name, val in scores.items():
        lo, hi = crit[name]["min"], crit[name]["max"]
        if val < lo or val > hi:
            problems.append("%s=%s outside %d-%d" % (name, val, lo, hi))
    total = sum(scores.values())
    zero_in_gate = any(scores[k] == 0 for k in r["no_zero_allowed_in"])

    if total >= r["proceed_threshold"] and not zero_in_gate:
        decision = "proceed"
    elif total <= r["kill_at_or_below"]:
        decision = "kill"
    elif total >= r["proceed_with_justification_min"]:
        # 5-6, or 7+ but with a zero in a gated criterion -> requires documented justification
        decision = "proceed_with_justification"
    else:
        decision = "kill"
    return {"total": total, "max": r["max_points"], "decision": decision,
            "zero_in_gated_criterion": zero_in_gate, "problems": problems}


def keyword_ok(keywords, cfg=None):
    """Exactly 7 keywords, each under the 50-character field limit."""
    cfg = cfg or load_config()
    m = cfg["kdp_metadata"]
    required = m["keywords_required"]
    limit = m["keyword_max_chars"]
    problems = []
    if len(keywords) != required:
        problems.append("expected %d keywords, got %d" % (required, len(keywords)))
    for kw in keywords:
        if len(kw) >= limit:
            problems.append("keyword %r is %d chars (must be < %d)" % (kw, len(kw), limit))
    return {"ok": not problems, "problems": problems}


def chapter_count_ok(n, cfg=None):
    """Chapter count within 8-12."""
    cfg = cfg or load_config()
    s = cfg["structure"]
    return {"ok": s["chapters_min"] <= n <= s["chapters_max"],
            "n": n, "min": s["chapters_min"], "max": s["chapters_max"]}


def page_band_ok(pages, cfg=None):
    """Extent within the 80-120 page band (120 is a hard cap)."""
    cfg = cfg or load_config()
    b = cfg["page_band"]
    return {"ok": b["target_min"] <= pages <= b["target_max"],
            "pages": pages, "min": b["target_min"], "max": b["target_max"],
            "hard_cap": b["hard_cap"]}


def chapter_body_words_ok(words, cfg=None):
    """Chapter body within 600-900 words."""
    cfg = cfg or load_config()
    s = cfg["structure"]
    return {"ok": s["chapter_body_words_min"] <= words <= s["chapter_body_words_max"],
            "words": words, "min": s["chapter_body_words_min"], "max": s["chapter_body_words_max"]}


def author_bio_words_ok(words, cfg=None):
    """Author bio within 60-90 words."""
    cfg = cfg or load_config()
    b = cfg["back_matter"]
    return {"ok": b["author_bio_words_min"] <= words <= b["author_bio_words_max"],
            "words": words, "min": b["author_bio_words_min"], "max": b["author_bio_words_max"]}


def value_element_budget(per_chapter_counts, cfg=None):
    """Value elements: at most one per chapter, at most four per book total."""
    cfg = cfg or load_config()
    s = cfg["structure"]
    per_max = s["value_element_max_per_chapter"]
    book_max = s["value_element_max_per_book"]
    problems = []
    for i, c in enumerate(per_chapter_counts, start=1):
        if c > per_max:
            problems.append("chapter %d has %d value elements (max %d)" % (i, c, per_max))
    total = sum(per_chapter_counts)
    if total > book_max:
        problems.append("book has %d value elements (max %d)" % (total, book_max))
    return {"ok": not problems, "total": total, "book_max": book_max, "problems": problems}


def image_quota_ok(inline, spot, quote_page, cfg=None):
    """Per-chapter minimum image quotas: >=2 inline, >=2 spot, >=1 quote-page illustration."""
    cfg = cfg or load_config()
    q = cfg["image_quotas_per_chapter"]
    problems = []
    if inline < q["inline_min"]:
        problems.append("inline %d < %d" % (inline, q["inline_min"]))
    if spot < q["spot_min"]:
        problems.append("spot %d < %d" % (spot, q["spot_min"]))
    if quote_page < q["quote_page_illustration_min"]:
        problems.append("quote_page %d < %d" % (quote_page, q["quote_page_illustration_min"]))
    return {"ok": not problems, "problems": problems}


def selftest():
    cfg = load_config()
    checks = {}

    checks["title_len_ok"] = combined_title_len_ok("Too Tired To Adult", "the honest survival guide for exhausted nurses", cfg)["ok"] is True
    checks["title_len_breach"] = combined_title_len_ok("X" * 120, "Y" * 120, cfg)["ok"] is False

    # rubric: 8 total, no zero in gated -> proceed
    checks["rubric_proceed"] = score_slot(3, 3, 1, 0, 1, cfg)["decision"] == "proceed"
    # 6 total -> proceed_with_justification
    checks["rubric_justify"] = score_slot(2, 2, 1, 0, 1, cfg)["decision"] == "proceed_with_justification"
    # 3 total -> kill
    checks["rubric_kill"] = score_slot(1, 0, 0, 1, 1, cfg)["decision"] == "kill"
    # 8 total but zero in differentiation -> cannot plainly proceed
    checks["rubric_zero_gate"] = score_slot(3, 0, 1, 1, 2, cfg)["decision"] == "proceed_with_justification"
    # out-of-range flagged
    checks["rubric_range_flag"] = len(score_slot(5, 3, 1, 1, 2, cfg)["problems"]) == 1

    checks["keywords_ok"] = keyword_ok(["burnout gift", "funny nurse gift", "secret santa nurse",
                                        "exhausted teacher", "stress relief book", "gag gift women",
                                        "retirement humor"], cfg)["ok"] is True
    checks["keywords_bad_count"] = keyword_ok(["a", "b"], cfg)["ok"] is False
    checks["keywords_too_long"] = keyword_ok(["x" * 55] + ["ok"] * 6, cfg)["ok"] is False

    checks["chapters_ok"] = chapter_count_ok(10, cfg)["ok"] is True
    checks["chapters_bad"] = chapter_count_ok(13, cfg)["ok"] is False
    checks["page_band_ok"] = page_band_ok(96, cfg)["ok"] is True
    checks["page_band_over"] = page_band_ok(121, cfg)["ok"] is False
    checks["chapter_words_ok"] = chapter_body_words_ok(750, cfg)["ok"] is True
    checks["chapter_words_bad"] = chapter_body_words_ok(950, cfg)["ok"] is False
    checks["author_bio_ok"] = author_bio_words_ok(75, cfg)["ok"] is True

    checks["value_budget_ok"] = value_element_budget([1, 0, 1, 0, 1, 0, 1, 0], cfg)["ok"] is True
    checks["value_budget_book_breach"] = value_element_budget([1, 1, 1, 1, 1], cfg)["ok"] is False
    checks["value_budget_chapter_breach"] = value_element_budget([2, 0], cfg)["ok"] is False

    checks["image_quota_ok"] = image_quota_ok(2, 2, 1, cfg)["ok"] is True
    checks["image_quota_bad"] = image_quota_ok(1, 2, 1, cfg)["ok"] is False

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
