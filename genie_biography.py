"""AIRF 2.0 Biography Edition -- deterministic production operations for the Biography, Memoir & True Crime
niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture,
reasoning, dignity judgment, or content rule is defined here; SKILL.md remains the source of truth.

Scope of what is genuinely deterministic in this niche:
  - quotation volume bucketing LOW/MEDIUM/HIGH  (SKILL.md 0.5 / Auto-Config)
  - BIO-COL profile-count == title-count  (Rule 6; Gate 4)
  - BIO-COL four-unit completeness Hook/Life/Contribution/Legacy  (Rule 6; Rule 10)
  - BIO-COL length consistency: +/-10% of cohort and no profile > 2x the shortest  (Architecture BIO-C)
  - BIO-COL per-unit word budgets  (Architecture BIO-C unit_words)
  - bibliography source floor: 20 under 250 pages, proportional above  (Rule 14)

CLI:  python genie_biography.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def classify_quotation_volume(count):
    """LOW (<5), MEDIUM (5-20 inclusive), HIGH (>20) per SKILL.md."""
    n = int(count)
    if n < 5:
        return "LOW"
    if n <= 20:
        return "MEDIUM"
    return "HIGH"


def profile_count_match(title_count, profile_count):
    """BIO-COL: the profile count must equal the count claimed in the title."""
    return int(title_count) == int(profile_count)


def profile_units_complete(profile, cfg=None):
    """A BIO-COL profile must carry all four units. `profile` is a dict; a unit counts as present
    when its key exists and its value is truthy. Returns (ok, [missing_units])."""
    cfg = cfg or load_config()
    units = cfg["architectures"]["BIO-C"]["profile_units"]
    missing = [u for u in units if not profile.get(u)]
    return (not missing, missing)


def profile_length_consistency(profile_word_counts, cfg=None):
    """BIO-COL length rules: every profile within +/-10% of the cohort mean AND no profile longer
    than 2x the shortest. `profile_word_counts` is a list of ints. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    bc = cfg["architectures"]["BIO-C"]
    pct = bc["profile_length_consistency_pct"] / 100.0
    mult = bc["max_profile_multiple_of_shortest"]
    data = [int(w) for w in profile_word_counts]
    problems = []
    if not data:
        return (False, ["no profiles supplied"])
    mean = sum(data) / len(data)
    lo, hi = mean * (1 - pct), mean * (1 + pct)
    for i, w in enumerate(data):
        if w < lo or w > hi:
            problems.append("profile %d (%d words) outside +/-%d%% of cohort mean %.0f"
                            % (i, w, bc["profile_length_consistency_pct"], mean))
    shortest = min(data)
    if max(data) > mult * shortest:
        problems.append("longest profile %d exceeds %dx the shortest %d"
                        % (max(data), mult, shortest))
    return (not problems, problems)


def validate_profile_section_words(sections, cfg=None):
    """BIO-COL: check each unit's word count against its configured range. `sections` is
    {unit: word_count}. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    ranges = cfg["architectures"]["BIO-C"]["unit_words"]
    problems = []
    for unit, (lo, hi) in ranges.items():
        if unit not in sections:
            problems.append("missing unit %s" % unit)
            continue
        w = int(sections[unit])
        if w < lo or w > hi:
            problems.append("%s %d words outside [%d, %d]" % (unit, w, lo, hi))
    return (not problems, problems)


def bibliography_minimum(pages, cfg=None):
    """Minimum bibliography sources: 20 for books under 250 pages; proportionally more above,
    scaled linearly on the 250-page basis (ceil(20 * pages / 250))."""
    cfg = cfg or load_config()
    b = cfg["bibliography"]
    floor = b["min_sources_under_250_pages"]
    basis = b["scaling_basis_pages"]
    p = int(pages)
    if p < basis:
        return floor
    return math.ceil(floor * p / basis)


def selftest():
    cfg = load_config()
    checks = {}
    checks["qv_low"] = classify_quotation_volume(4) == "LOW"
    checks["qv_medium_low_edge"] = classify_quotation_volume(5) == "MEDIUM"
    checks["qv_medium_high_edge"] = classify_quotation_volume(20) == "MEDIUM"
    checks["qv_high"] = classify_quotation_volume(21) == "HIGH"

    checks["count_match"] = profile_count_match(50, 50) is True
    checks["count_mismatch"] = profile_count_match(50, 49) is False

    ok_units, missing = profile_units_complete(
        {"hook": "x", "life": "x", "contribution": "x", "legacy": "x"}, cfg)
    checks["units_complete"] = ok_units and not missing
    bad_units, bad_missing = profile_units_complete({"hook": "x", "life": "x", "contribution": "x"}, cfg)
    checks["units_missing_flagged"] = (not bad_units) and "legacy" in bad_missing

    ok_len, _ = profile_length_consistency([500, 510, 490, 505], cfg)
    checks["length_consistent_ok"] = ok_len
    bad_len, bad_probs = profile_length_consistency([200, 600], cfg)
    checks["length_inconsistent_flagged"] = (not bad_len) and len(bad_probs) >= 1

    ok_sec, _ = validate_profile_section_words(
        {"hook": 200, "life": 450, "contribution": 600, "legacy": 300}, cfg)
    checks["sections_ok"] = ok_sec
    bad_sec, bad_sec_probs = validate_profile_section_words(
        {"hook": 100, "life": 450, "contribution": 900, "legacy": 300}, cfg)
    checks["sections_flagged"] = (not bad_sec) and len(bad_sec_probs) >= 2

    checks["biblio_under_250"] = bibliography_minimum(200, cfg) == 20
    checks["biblio_at_250"] = bibliography_minimum(250, cfg) == 20
    checks["biblio_500"] = bibliography_minimum(500, cfg) == 40
    checks["biblio_300"] = bibliography_minimum(300, cfg) == 24

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
