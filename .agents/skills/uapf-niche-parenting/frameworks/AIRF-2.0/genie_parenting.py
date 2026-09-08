"""AIRF 2.0 -- deterministic production operations for the parenting niche.

Machine-executable projection of the countable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture
is defined here; SKILL.md remains the source of truth for reasoning/voice/design.

Deterministic surface for this niche is intentionally small (most parenting gates are editorial
and manual). The genuinely computable checks are:
  - "When to Call the Professional" box indicator count (3-8) + urgency-level presence
  - chapter-opening image auto-rule (one per chapter at any page count -- global Rule 11)
  - sub-genre page-band membership

CLI:  python genie_parenting.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def validate_when_to_call_box(indicator_count, urgency_level, cfg=None):
    """Validate one 'When to Call the Professional' box. Returns (ok, [problems]).

    Rule (SKILL.md): 3-8 specific indicators; must specify an urgency level drawn from the
    Active Medical Authority's escalation ladder."""
    cfg = cfg or load_config()
    box = cfg["when_to_call_box"]
    problems = []
    lo, hi = box["min_indicators"], box["max_indicators"]
    if indicator_count < lo or indicator_count > hi:
        problems.append("indicator count %d outside %d-%d" % (indicator_count, lo, hi))
    allowed = [u.lower() for u in box["urgency_levels"]]
    if (urgency_level or "").strip().lower() not in allowed:
        problems.append("urgency_level %r not one of %s" % (urgency_level, box["urgency_levels"]))
    return (not problems, problems)


def images_required(page_count, chapter_count, cfg=None):
    """Chapter-opening image auto-rule (global Rule 11): one image per chapter at ANY page
    count; page count never gates image generation. page_count is accepted for signature
    stability but does not reduce the count."""
    if chapter_count < 0:
        raise ValueError("chapter_count must be >= 0")
    return chapter_count


def check_page_band(sub_genre, page_count, cfg=None):
    """Compare a projected page count to the sub-genre page band (defaults; competitor research
    may override). Returns {ok, sub_genre, pages, band}."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if sub_genre not in bands or not isinstance(bands[sub_genre], dict):
        raise ValueError("unknown sub_genre %r (allowed: %s)" % (
            sub_genre, [k for k, v in bands.items() if isinstance(v, dict)]))
    band = bands[sub_genre]
    lo, hi = band["pages_min"], band["pages_max"]
    return {"ok": lo <= page_count <= hi, "sub_genre": sub_genre,
            "pages": page_count, "band": [lo, hi]}


def selftest():
    cfg = load_config()
    checks = {}

    ok, _ = validate_when_to_call_box(5, "seek urgent care", cfg)
    checks["box_ok_midrange"] = ok
    ok3, _ = validate_when_to_call_box(3, "call your pediatrician", cfg)
    checks["box_ok_min"] = ok3
    ok8, _ = validate_when_to_call_box(8, "call emergency services", cfg)
    checks["box_ok_max"] = ok8
    bad, probs = validate_when_to_call_box(2, "seek urgent care", cfg)
    checks["box_too_few_flagged"] = (not bad) and len(probs) == 1
    bad2, probs2 = validate_when_to_call_box(9, "phone a friend", cfg)
    checks["box_too_many_and_bad_urgency"] = (not bad2) and len(probs2) == 2

    # Rule 11: one image per chapter at ANY page count (160p and 240p both full count)
    checks["images_short_book"] = images_required(160, 10, cfg) == 10
    checks["images_long_book"] = images_required(240, 12, cfg) == 12
    checks["images_not_page_gated"] = images_required(400, 8, cfg) == 8

    band_ok = check_page_band("newborn_infant_care", 220, cfg)
    checks["page_band_in_range"] = band_ok["ok"] and band_ok["band"] == [180, 260]
    band_bad = check_page_band("newborn_infant_care", 400, cfg)
    checks["page_band_out_of_range"] = band_bad["ok"] is False

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
