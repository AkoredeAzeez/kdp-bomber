"""AIRF 2.0 History Edition -- deterministic production operations for the History & Politics niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No historical
judgment, sourcing, or interpretation is defined here; SKILL.md remains the source of truth.

CLI:  python genie_history.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def quotation_volume_class(n, cfg=None):
    """Classify direct-quotation volume: LOW (<5), MEDIUM (5-20), HIGH (>20).

    HIGH activates the Quotation Authentication Specialist for every chapter.
    """
    cfg = cfg or load_config()
    q = cfg["quotation_volume"]
    if n < q["low_max_exclusive"]:
        level = "LOW"
    elif n <= q["medium_max"]:
        level = "MEDIUM"
    else:
        level = "HIGH"
    return {"level": level,
            "per_chapter_authentication": level == "HIGH" and q["high_activates_per_chapter_authentication"]}


def bibliography_min(pages, cfg=None):
    """Minimum bibliography source count for a given page length.

    SKILL.md: at least 15 sources for any book under 200 pages; proportionally more for longer
    works. Projected as a floor of 15 below the pivot, and the 15-per-200-pages base rate applied
    proportionally at or above it.
    """
    cfg = cfg or load_config()
    b = cfg["bibliography"]
    floor = b["min_sources_under_200_pages"]
    pivot = b["page_pivot"]
    base_n, base_pages = b["base_rate_per_pages"]
    if pages < pivot:
        return floor
    return max(floor, math.ceil(base_n * pages / base_pages))


def glossary_required(term_count, cfg=None):
    """Glossary is mandatory when the book introduces 10+ specialized terms."""
    cfg = cfg or load_config()
    return term_count >= cfg["glossary"]["mandatory_when_terms_at_least"]


def _arch_key(architecture):
    a = architecture.strip().upper()
    if a in ("A", "A_CHRONOLOGICAL_NARRATIVE"):
        return "A_chronological_narrative"
    if a in ("B", "B_THEMATIC_ANALYSIS"):
        return "B_thematic_analysis"
    if a in ("C", "C_BIOGRAPHICAL_NARRATIVE"):
        return "C_biographical_narrative"
    raise ValueError("unknown architecture %r" % architecture)


def chapter_count_ok(architecture, n, cfg=None):
    """Validate chapter count against the locked architecture's bounds.

    Architecture A -> 8-16, Architecture C -> 10-18. Architecture B has no fixed chapter
    count in SKILL.md, so it is reported ok with a note rather than bounded.
    """
    cfg = cfg or load_config()
    key = _arch_key(architecture)
    arch = cfg["architectures"][key]
    if "chapters_min" not in arch:
        return {"ok": True, "n": n, "note": "Architecture B has no fixed chapter count in SKILL.md"}
    lo, hi = arch["chapters_min"], arch["chapters_max"]
    return {"ok": lo <= n <= hi, "n": n, "min": lo, "max": hi}


def page_band_lookup(audience_band, cfg=None):
    """Return the page and word-count band for a named audience band."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if audience_band not in bands:
        raise ValueError("unknown page band %r (allowed: %s)" % (audience_band, list(bands)))
    return bands[audience_band]


def word_count_in_band(words, audience_band, cfg=None):
    """Check a manuscript word count against a named page band's word range."""
    band = page_band_lookup(audience_band, cfg)
    return {"ok": band["words_min"] <= words <= band["words_max"],
            "words": words, "min": band["words_min"], "max": band["words_max"]}


def chapter_words_in_architecture(architecture, words, academic=False, cfg=None):
    """Check a chapter word count against the architecture's target range.

    Architecture A: general 3500-6000 (academic up to 8000). B: 4000-7000. C: uses the
    general narrative expectation and is reported without a hard cap (SKILL gives no C range).
    """
    cfg = cfg or load_config()
    key = _arch_key(architecture)
    arch = cfg["architectures"][key]
    if key == "A_chronological_narrative":
        lo = arch["chapter_words_general_min"]
        hi = arch["chapter_words_academic_max"] if academic else arch["chapter_words_general_max"]
        return {"ok": lo <= words <= hi, "words": words, "min": lo, "max": hi}
    if key == "B_thematic_analysis":
        lo, hi = arch["chapter_words_min"], arch["chapter_words_max"]
        return {"ok": lo <= words <= hi, "words": words, "min": lo, "max": hi}
    return {"ok": True, "words": words, "note": "Architecture C carries no fixed chapter word range in SKILL.md"}


def keyword_ok(keywords, cfg=None):
    """Exactly 7 backend keyword strings, each under the 50-character slot limit."""
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


def selftest():
    cfg = load_config()
    checks = {}

    checks["quote_low"] = quotation_volume_class(4, cfg)["level"] == "LOW"
    checks["quote_medium"] = quotation_volume_class(5, cfg)["level"] == "MEDIUM"
    checks["quote_medium_top"] = quotation_volume_class(20, cfg)["level"] == "MEDIUM"
    checks["quote_high"] = quotation_volume_class(21, cfg)["level"] == "HIGH"
    checks["quote_high_activates"] = quotation_volume_class(30, cfg)["per_chapter_authentication"] is True

    checks["biblio_floor"] = bibliography_min(180, cfg) == 15
    checks["biblio_pivot"] = bibliography_min(200, cfg) == 15
    checks["biblio_proportional"] = bibliography_min(400, cfg) == 30
    checks["biblio_mid"] = bibliography_min(300, cfg) == 23

    checks["glossary_yes"] = glossary_required(10, cfg) is True
    checks["glossary_no"] = glossary_required(9, cfg) is False

    checks["chapters_A_ok"] = chapter_count_ok("A", 12, cfg)["ok"] is True
    checks["chapters_A_bad"] = chapter_count_ok("A", 7, cfg)["ok"] is False
    checks["chapters_C_ok"] = chapter_count_ok("C", 14, cfg)["ok"] is True
    checks["chapters_B_note"] = "note" in chapter_count_ok("B", 5, cfg)

    checks["band_lookup"] = page_band_lookup("general_narrative", cfg)["pages_max"] == 280
    checks["word_band_ok"] = word_count_in_band(70000, "general_narrative", cfg)["ok"] is True
    checks["word_band_bad"] = word_count_in_band(200000, "general_narrative", cfg)["ok"] is False

    checks["ch_words_A_general"] = chapter_words_in_architecture("A", 5000, False, cfg)["ok"] is True
    checks["ch_words_A_academic"] = chapter_words_in_architecture("A", 7500, True, cfg)["ok"] is True
    checks["ch_words_A_over_general"] = chapter_words_in_architecture("A", 7500, False, cfg)["ok"] is False
    checks["ch_words_B_ok"] = chapter_words_in_architecture("B", 6000, cfg=cfg)["ok"] is True

    checks["keywords_ok"] = keyword_ok(["roman empire fall causes", "world war 2 pacific",
                                        "cold war diplomacy", "medieval europe history",
                                        "ancient rome politics", "history books for beginners",
                                        "why did rome fall"], cfg)["ok"] is True
    checks["keywords_bad_count"] = keyword_ok(["a", "b"], cfg)["ok"] is False
    checks["keywords_too_long"] = keyword_ok(["x" * 55] + ["ok"] * 6, cfg)["ok"] is False

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
