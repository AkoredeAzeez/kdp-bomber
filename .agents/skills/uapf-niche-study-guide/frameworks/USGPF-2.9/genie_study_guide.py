"""USGPF 2.9 -- deterministic production operations for the study-guide / exam-prep niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_study_guide.py selftest
"""
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def questions_per_set(total, set_count):
    """Split the operator-supplied total into balanced per-set counts (max-min <= 1),
    preserving continuous numbering 1..total across the whole division."""
    if total < 0 or set_count <= 0:
        raise ValueError("total must be >= 0 and set_count > 0")
    base, rem = divmod(total, set_count)
    sizes = [base + (1 if i < rem else 0) for i in range(set_count)]
    assert sum(sizes) == total
    return sizes


def answer_key_quota(n_items, option_count=None, cfg=None):
    """Balanced answer-key quota for a set: each key letter within one of even
    (SKILL.md randomization engine: 'balanced quotas per set within one of even')."""
    cfg = cfg or load_config()
    option_count = option_count or cfg["assessment"]["default_option_count"]
    if n_items < 0 or option_count <= 0:
        raise ValueError("n_items >= 0 and option_count > 0 required")
    base, rem = divmod(n_items, option_count)
    quotas = {chr(65 + i): base + (1 if i < rem else 0) for i in range(option_count)}
    assert sum(quotas.values()) == n_items
    return quotas


def quota_balanced(quotas, cfg=None):
    """True if the key distribution is within the configured tolerance (default 1)."""
    cfg = cfg or load_config()
    tol = cfg["assessment"]["quota_balance_tolerance"]
    if not quotas:
        return True
    return (max(quotas.values()) - min(quotas.values())) <= tol


def resolve_run_cap(option_count, has_two_option_type=False, cfg=None):
    """Effective max consecutive-run cap. Default 1; any two-option in-sequence type
    (or a two-option profile) auto-raises to at least 2, shipped default 3 (Two Option Law)."""
    cfg = cfg or load_config()
    a = cfg["assessment"]
    if option_count == 2 or has_two_option_type:
        return max(a["two_option_run_cap_min"], a["two_option_run_cap_default"])
    return a["run_cap_default"]


def max_run(seq):
    """Longest run of an identical key letter in a sequence."""
    best = run = 0
    prev = None
    for x in seq:
        run = run + 1 if x == prev else 1
        prev = x
        best = max(best, run)
    return best


def has_doubled_4perm(seq):
    """True if a 4-letter permutation (four distinct letters) repeats immediately, e.g. ABCD ABCD."""
    s = list(seq)
    for i in range(len(s) - 7):
        block = s[i:i + 4]
        if len(set(block)) == 4 and s[i + 4:i + 8] == block:
            return True
    return False


def has_tripled_2alt(seq):
    """True if a two-letter alternation repeats for three cycles, e.g. ABABAB."""
    s = list(seq)
    for i in range(len(s) - 5):
        a, b = s[i], s[i + 1]
        if a != b and s[i:i + 6] == [a, b, a, b, a, b]:
            return True
    return False


def pattern_guard_check(seq, option_count=None, has_two_option_type=False, cfg=None):
    """Full pattern-guard verdict for a randomized key sequence. Returns (ok, problems)."""
    cfg = cfg or load_config()
    problems = []
    cap = resolve_run_cap(option_count or cfg["assessment"]["default_option_count"],
                          has_two_option_type, cfg)
    mr = max_run(seq)
    if mr > cap:
        problems.append("max run %d exceeds cap %d" % (mr, cap))
    if cfg["assessment"]["pattern_guards"]["no_doubled_4perm"] and has_doubled_4perm(seq):
        problems.append("doubled 4-letter permutation present")
    if cfg["assessment"]["pattern_guards"]["no_tripled_2alt"] and has_tripled_2alt(seq):
        problems.append("tripled 2-letter alternation present")
    return (not problems, problems)


def answer_count_match(question_numbers, answer_numbers):
    """Continuous-numbering integrity: question count equals answer count, both are the
    contiguous range 1..N with no gaps or duplicates, and they align one to one."""
    q = list(question_numbers)
    a = list(answer_numbers)
    problems = []
    if len(q) != len(a):
        problems.append("question count %d != answer count %d" % (len(q), len(a)))
    expected = list(range(1, len(q) + 1))
    if sorted(q) != expected:
        problems.append("question numbering not contiguous 1..N")
    if sorted(a) != expected:
        problems.append("answer numbering not contiguous 1..N")
    if q != a:
        problems.append("answer numbers do not align to question numbers")
    return (not problems, problems)


def explanation_within_cap(text, cfg=None):
    """True if an explanation is within the word cap (default 50 words)."""
    cfg = cfg or load_config()
    cap = cfg["assessment"]["explanation_max_words"]
    return len(text.split()) <= cap


def chapter_page_ok(pages, cfg=None):
    """Single-chapter page band (6 to 10 rendered pages)."""
    cfg = cfg or load_config()
    b = cfg["page_bands"]
    return b["chapter_min_pages"] <= pages <= b["chapter_max_pages"]


def chapters_total_ok(page_list, cfg=None):
    """Learning-chapters total against the band and the absolute 60-page ceiling.
    Returns {ok, total, ceiling, in_band, over_ceiling}."""
    cfg = cfg or load_config()
    b = cfg["page_bands"]
    total = sum(page_list)
    over = total > b["chapters_absolute_ceiling"]
    in_band = b["chapters_total_min"] <= total <= b["chapters_total_max"]
    return {"ok": in_band and not over, "total": total,
            "ceiling": b["chapters_absolute_ceiling"], "in_band": in_band,
            "over_ceiling": over}


def section_band_ok(pages, cfg=None):
    """Preface/Introduction/Conclusion band (1.40 to 1.55 rendered pages)."""
    cfg = cfg or load_config()
    lo, hi = cfg["page_bands"]["section_band_pages"]
    return lo <= pages <= hi


def chapter_floors_ok(table_count, figure_count, cfg=None):
    """Per-chapter minimums: >=2 captioned data tables and >=2 content figures."""
    cfg = cfg or load_config()
    return (table_count >= cfg["data_tables"]["min_per_chapter"]
            and figure_count >= cfg["figures"]["min_content_per_chapter"])


def validate_subtitle(subtitle, total, cfg=None):
    """Subtitle Composition Law: states the exact total with 'Practice Questions',
    letters/numerals/spaces only. Returns (ok, problems)."""
    cfg = cfg or load_config()
    phrase = cfg["subtitle"]["must_contain_phrase"]
    problems = []
    if not re.fullmatch(r"[A-Za-z0-9 ]+", subtitle or ""):
        problems.append("subtitle contains characters other than letters/numerals/spaces")
    if phrase.lower() not in (subtitle or "").lower():
        problems.append("subtitle missing phrase '%s'" % phrase)
    if not re.search(r"(?<!\d)%d(?!\d)" % int(total), subtitle or ""):
        problems.append("subtitle does not state the exact total %d" % int(total))
    return (not problems, problems)


def selftest():
    cfg = load_config()
    checks = {}

    # assessment split: 600 across 8 sets -> 75 each, sums to 600
    sizes = questions_per_set(600, 8)
    checks["split_balanced"] = sizes == [75] * 8 and sum(sizes) == 600
    odd = questions_per_set(601, 8)
    checks["split_remainder"] = max(odd) - min(odd) == 1 and sum(odd) == 601

    # key quota: 75 items, 4 options -> 19,19,19,18 ; balanced within 1
    q = answer_key_quota(75, 4, cfg)
    checks["quota_values"] = sorted(q.values()) == [18, 19, 19, 19]
    checks["quota_balanced"] = quota_balanced(q, cfg)
    checks["quota_unbalanced_flagged"] = not quota_balanced({"A": 40, "B": 10}, cfg)

    # run caps
    checks["run_cap_default"] = resolve_run_cap(4, False, cfg) == 1
    checks["run_cap_two_option"] = resolve_run_cap(2, False, cfg) == 3
    checks["run_cap_two_option_flag"] = resolve_run_cap(4, True, cfg) == 3

    # pattern guards
    checks["max_run"] = max_run(list("AABBBC")) == 3
    checks["doubled_4perm_detected"] = has_doubled_4perm(list("ABCDABCD"))
    checks["doubled_4perm_clean"] = not has_doubled_4perm(list("ABCDBADC"))
    checks["tripled_2alt_detected"] = has_tripled_2alt(list("ABABAB"))
    checks["tripled_2alt_clean"] = not has_tripled_2alt(list("ABABCB"))
    ok_seq, _ = pattern_guard_check(list("ABCDBCADACBD"), 4, False, cfg)
    checks["pattern_guard_clean_ok"] = ok_seq
    bad_seq, probs = pattern_guard_check(list("AAAABBBB"), 4, False, cfg)
    checks["pattern_guard_flags_run"] = (not bad_seq) and any("run" in p for p in probs)

    # numbering integrity
    ok_n, _ = answer_count_match(range(1, 11), range(1, 11))
    checks["numbering_ok"] = ok_n
    bad_n, _ = answer_count_match(range(1, 11), range(1, 10))
    checks["numbering_mismatch_flagged"] = not bad_n

    # explanation cap
    checks["expl_ok"] = explanation_within_cap("word " * 50, cfg)
    checks["expl_over"] = not explanation_within_cap("word " * 51, cfg)

    # page bands
    checks["chapter_page_ok"] = chapter_page_ok(8, cfg) and not chapter_page_ok(11, cfg)
    tot = chapters_total_ok([8] * 7, cfg)  # 56 -> in band
    checks["chapters_total_in_band"] = tot["ok"] and tot["total"] == 56
    over = chapters_total_ok([9] * 7, cfg)  # 63 -> over ceiling
    checks["chapters_total_ceiling"] = (not over["ok"]) and over["over_ceiling"]
    checks["section_band"] = section_band_ok(1.5, cfg) and not section_band_ok(1.6, cfg)

    # chapter floors
    checks["floors_ok"] = chapter_floors_ok(2, 2, cfg)
    checks["floors_short"] = not chapter_floors_ok(1, 2, cfg)

    # subtitle
    ok_s, _ = validate_subtitle("NCLEX RN Review 600 Practice Questions", 600, cfg)
    checks["subtitle_ok"] = ok_s
    bad_s, sp = validate_subtitle("NCLEX-RN Review: 600 Q&A", 600, cfg)
    checks["subtitle_flags_punct_and_phrase"] = (not bad_s) and len(sp) >= 2
    wrong_count, _ = validate_subtitle("Review 500 Practice Questions", 600, cfg)
    checks["subtitle_wrong_count"] = not wrong_count

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
