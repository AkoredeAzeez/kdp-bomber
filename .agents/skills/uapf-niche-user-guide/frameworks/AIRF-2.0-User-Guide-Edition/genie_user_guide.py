"""AIRF 2.0 User Guide Edition -- deterministic production operations for the user-guide niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_user_guide.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def classify_size_band(chapter_count, cfg=None):
    """Classify a book into compact/standard/extended by chapter count.
    Returns the band name, or None if the chapter count falls in no band."""
    cfg = cfg or load_config()
    for name, band in cfg["page_bands"].items():
        if band["chapters_min"] <= chapter_count <= band["chapters_max"]:
            return name
    return None


def validate_size_band(size, chapter_count, page_estimate, cfg=None):
    """Confirm a declared size band is internally consistent: chapter_count and
    page_estimate both fall inside the declared band's ranges. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    problems = []
    if size not in bands:
        return (False, ["unknown size band %r (allowed: %s)" % (size, list(bands))])
    b = bands[size]
    if not (b["chapters_min"] <= chapter_count <= b["chapters_max"]):
        problems.append("chapter_count %d outside %s band %d-%d" % (
            chapter_count, size, b["chapters_min"], b["chapters_max"]))
    if not (b["pages_min"] <= page_estimate <= b["pages_max"]):
        problems.append("page_estimate %d outside %s band %d-%d" % (
            page_estimate, size, b["pages_min"], b["pages_max"]))
    return (not problems, problems)


def validate_warning_level(label, cfg=None):
    """True iff `label` is one of the only permissible advisory formats (ANSI hierarchy)."""
    cfg = cfg or load_config()
    return label in cfg["warning_hierarchy"]["levels"]


def check_front_matter_order(order, cfg=None):
    """Confirm the front matter appears in the mandatory order. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    required = cfg["front_matter_order"]
    if list(order) == required:
        return (True, [])
    return (False, ["front matter order %r != required %r" % (list(order), required)])


def check_appendix_elements(present, cfg=None):
    """Verify all seven required Appendix elements are present. Returns (ok, [missing])."""
    cfg = cfg or load_config()
    required = cfg["back_matter"]["appendix_required_elements"]
    present_set = set(present)
    missing = [e for e in required if e not in present_set]
    return (not missing, missing)


def check_troubleshooting_count(problem_count, cfg=None):
    """Troubleshooting must cover at least the top-N documented user problems."""
    cfg = cfg or load_config()
    required = cfg["back_matter"]["troubleshooting_top_problems"]
    return {"ok": problem_count >= required, "required": required, "have": problem_count}


def body_settings(audience_signal, cfg=None):
    """Return body point size and line spacing for a senior/large-print signal vs standard."""
    cfg = cfg or load_config()
    a = cfg["audience"]
    if audience_signal in ("senior", "seniors", "large-print", "large_print"):
        return dict(a["senior_large_print"])
    return dict(a["standard"])


def selftest():
    cfg = load_config()
    checks = {}

    # band classification by chapter count
    checks["classify_compact"] = classify_size_band(8, cfg) == "compact"
    checks["classify_standard"] = classify_size_band(14, cfg) == "standard"
    checks["classify_extended"] = classify_size_band(24, cfg) == "extended"
    checks["classify_none"] = classify_size_band(40, cfg) is None

    # band validation consistency
    ok_std, _ = validate_size_band("standard", 14, 220, cfg)
    checks["band_ok"] = ok_std
    bad_ok, bad_probs = validate_size_band("compact", 14, 220, cfg)
    checks["band_bad_flags_both"] = (not bad_ok) and len(bad_probs) == 2

    # warning levels
    checks["warn_valid"] = validate_warning_level("VERSION NOTE", cfg) is True
    checks["warn_invalid"] = validate_warning_level("Tip", cfg) is False

    # front matter order
    good_order = ["Title Page", "Copyright Page", "Table of Contents", "Preface",
                  "How to Use This Book", "Introduction"]
    checks["front_order_ok"] = check_front_matter_order(good_order, cfg)[0] is True
    bad_order = ["Title Page", "Preface", "Copyright Page", "Table of Contents",
                 "How to Use This Book", "Introduction"]
    checks["front_order_bad"] = check_front_matter_order(bad_order, cfg)[0] is False

    # appendix seven elements
    full = list(cfg["back_matter"]["appendix_required_elements"])
    checks["appendix_full_ok"] = check_appendix_elements(full, cfg)[0] is True
    ok_missing, missing = check_appendix_elements(full[:-2], cfg)
    checks["appendix_missing_two"] = (not ok_missing) and len(missing) == 2

    # troubleshooting count
    checks["trouble_ok"] = check_troubleshooting_count(10, cfg)["ok"] is True
    checks["trouble_short"] = check_troubleshooting_count(6, cfg)["ok"] is False

    # body settings
    checks["body_standard"] = body_settings("all-levels", cfg) == {"body_pt": 11, "line_spacing": 1.15}
    checks["body_senior"] = body_settings("senior", cfg) == {"body_pt": 13, "line_spacing": 1.5}

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
