"""AIRF 2.0 -- deterministic production operations for the poetry/affirmations niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

The niche is mostly craft-judgement (originality, cadence, cliche), which stays manual. But a
handful of gate values ARE deterministic and are computed here: the size-banded variety quota,
the 10% cadence sample size, declared-entry-count verification, day-number sequencing, and the
section / poems-per-section structure bands.

CLI:  python genie_poetry.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def variety_quota(collection_size, cfg=None):
    """Max repetitions of any single core idea in substantially identical form, by size band.
    Below the activation threshold (30 entries) the quota does not apply -> returns None."""
    cfg = cfg or load_config()
    vq = cfg["variety_quota"]
    if collection_size < vq["applies_at_min_entries"]:
        return None
    for band in vq["bands"]:
        if band["min"] <= collection_size <= band["max"]:
            return band["max_reps"]
    raise ValueError("collection_size %d outside supported bands (max %d)" % (
        collection_size, vq["bands"][-1]["max"]))


def cadence_sample_size(section_entries, cfg=None):
    """At least 10% of each section's entries, read aloud (rounded up, minimum 1)."""
    if section_entries < 0:
        raise ValueError("section_entries must be >= 0")
    cfg = cfg or load_config()
    ca = cfg["cadence_audit"]
    if section_entries == 0:
        return 0
    return max(ca["min_sample"], math.ceil(section_entries * ca["sample_fraction"]))


def verify_entry_count(actual_distinct_entries, declared_count):
    """Declared entry count is a hard contract: total distinct complete entries must equal N."""
    ok = actual_distinct_entries == declared_count
    return {"ok": ok, "actual": actual_distinct_entries, "declared": declared_count,
            "delta": actual_distinct_entries - declared_count}


def verify_day_sequence(day_numbers):
    """Day numbers must be sequential 1..N and complete with no gaps or duplicates."""
    nums = list(day_numbers)
    n = len(nums)
    expected = list(range(1, n + 1))
    problems = []
    if sorted(nums) != expected:
        missing = sorted(set(expected) - set(nums))
        dupes = sorted({x for x in nums if nums.count(x) > 1})
        if missing:
            problems.append("missing day numbers: %s" % missing)
        if dupes:
            problems.append("duplicate day numbers: %s" % dupes)
        extra = sorted(set(nums) - set(expected))
        if extra:
            problems.append("out-of-range day numbers: %s" % extra)
    return (not problems, problems)


def validate_section_count(count, cfg=None):
    """Collections carry 4-8 sections."""
    cfg = cfg or load_config()
    s = cfg["structure"]
    problems = []
    if count < s["sections_min"]:
        problems.append("sections %d below minimum %d" % (count, s["sections_min"]))
    if count > s["sections_max"]:
        problems.append("sections %d above maximum %d" % (count, s["sections_max"]))
    return (not problems, problems)


def validate_poems_per_section(count, cfg=None):
    """Each section carries 8-20 poems."""
    cfg = cfg or load_config()
    s = cfg["structure"]
    problems = []
    if count < s["poems_per_section_min"]:
        problems.append("poems %d below minimum %d" % (count, s["poems_per_section_min"]))
    if count > s["poems_per_section_max"]:
        problems.append("poems %d above maximum %d" % (count, s["poems_per_section_max"]))
    return (not problems, problems)


def validate_haiku_syllables(line_syllables, cfg=None):
    """Haiku lines must match the declared 5-7-5 structure (English default convention)."""
    cfg = cfg or load_config()
    want = cfg["haiku_syllables"]
    return (list(line_syllables) == list(want), {"got": list(line_syllables), "want": want})


def selftest():
    cfg = load_config()
    checks = {}
    # variety quota bands
    checks["quota_below_threshold_none"] = variety_quota(20, cfg) is None
    checks["quota_30_60"] = variety_quota(45, cfg) == 3
    checks["quota_61_120"] = variety_quota(90, cfg) == 5
    checks["quota_121_200"] = variety_quota(150, cfg) == 6
    checks["quota_201_365"] = variety_quota(365, cfg) == 8
    checks["quota_boundary_60"] = variety_quota(60, cfg) == 3
    checks["quota_boundary_61"] = variety_quota(61, cfg) == 5
    # cadence sample = ceil(0.10*n), min 1
    checks["cadence_20"] = cadence_sample_size(20, cfg) == 2
    checks["cadence_11"] = cadence_sample_size(11, cfg) == 2
    checks["cadence_5_min1"] = cadence_sample_size(5, cfg) == 1
    checks["cadence_0"] = cadence_sample_size(0, cfg) == 0
    # entry count contract
    checks["entry_count_ok"] = verify_entry_count(365, 365)["ok"] is True
    checks["entry_count_short"] = verify_entry_count(360, 365)["delta"] == -5
    # day sequence
    checks["day_seq_ok"] = verify_day_sequence([1, 2, 3, 4, 5])[0] is True
    checks["day_seq_gap"] = not verify_day_sequence([1, 2, 4, 5])[0]
    checks["day_seq_dupe"] = not verify_day_sequence([1, 2, 2, 3])[0]
    # structure bands
    checks["section_ok"] = validate_section_count(5, cfg)[0]
    checks["section_flagged"] = not validate_section_count(9, cfg)[0]
    checks["poems_ok"] = validate_poems_per_section(12, cfg)[0]
    checks["poems_flagged"] = not validate_poems_per_section(25, cfg)[0]
    # haiku
    checks["haiku_ok"] = validate_haiku_syllables([5, 7, 5], cfg)[0]
    checks["haiku_flagged"] = not validate_haiku_syllables([5, 7, 6], cfg)[0]
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
