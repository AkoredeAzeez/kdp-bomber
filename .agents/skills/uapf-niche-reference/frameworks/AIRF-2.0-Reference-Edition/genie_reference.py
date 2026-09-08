"""AIRF 2.0 Reference Edition -- deterministic production operations for the Adult Reference & Trivia niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture is
defined here; SKILL.md remains the source of truth for reasoning/design/verification.

CLI:  python genie_reference.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def check_count_claim(claimed_count, per_page, pages):
    """Count-claim achievability / reconciliation. Given the per-page entry (or question)
    density and the page target, can the claimed count fit? Returns capacity, minimum pages
    needed, and ok. (SKILL.md 'Count Claim Exactness'; Rule #3.)"""
    if claimed_count < 0 or per_page <= 0 or pages < 0:
        raise ValueError("claimed_count>=0, per_page>0, pages>=0 required")
    capacity = math.floor(per_page * pages)
    min_pages = math.ceil(claimed_count / per_page) if claimed_count else 0
    return {"claimed": claimed_count, "capacity": capacity, "pages": pages,
            "per_page": per_page, "min_pages_needed": min_pages,
            "ok": claimed_count <= capacity}


def reconcile_final_count(actual_count, claimed_count):
    """Gate 4 reconciliation: verified count must equal or exceed the title claim."""
    return {"actual": actual_count, "claimed": claimed_count,
            "ok": actual_count >= claimed_count, "short_by": max(0, claimed_count - actual_count)}


def check_page_count(pages, subtype, cfg=None):
    """Page count must be even, >= KDP minimum, and within the sub-type range."""
    cfg = cfg or load_config()
    pr = cfg["page_rules"]
    lo, hi = pr["page_count_range"][subtype]
    problems = []
    if pages % 2 != 0:
        problems.append("page count %d is not even" % pages)
    if pages < pr["kdp_min_pages"]:
        problems.append("page count %d below KDP minimum %d" % (pages, pr["kdp_min_pages"]))
    if pages < lo or pages > hi:
        problems.append("page count %d outside %s range %d-%d" % (pages, subtype, lo, hi))
    return {"ok": not problems, "pages": pages, "range": [lo, hi], "problems": problems}


def validate_round_architecture(total_rounds, questions_per_round, target_questions=None, cfg=None):
    """REF-TRIVIA round math: fixed questions-per-round must be one of the allowed options;
    total rounds within book range; total questions = rounds x qpr, optionally inside a target
    question band. (SKILL.md 'Round Architecture'.)"""
    cfg = cfg or load_config()
    tr = cfg["trivia_rounds"]
    allowed = set(tr["questions_per_round_options"].values())
    lo, hi = tr["total_rounds_per_book"]
    problems = []
    if questions_per_round not in allowed:
        problems.append("questions_per_round %d not in allowed %s" % (
            questions_per_round, sorted(allowed)))
    if total_rounds < lo or total_rounds > hi:
        problems.append("total_rounds %d outside %d-%d" % (total_rounds, lo, hi))
    total_questions = total_rounds * questions_per_round
    if target_questions is not None:
        tlo, thi = target_questions
        if total_questions < tlo or total_questions > thi:
            problems.append("total_questions %d outside target band %d-%d" % (
                total_questions, tlo, thi))
    return {"ok": not problems, "total_questions": total_questions,
            "total_rounds": total_rounds, "questions_per_round": questions_per_round,
            "problems": problems}


def difficulty_bucket(question_number, cfg=None):
    """Map a question number in a standard round to its difficulty tier via the configured
    ladder (accessible / moderate / specialist)."""
    cfg = cfg or load_config()
    ladder = cfg["trivia_rounds"]["difficulty_ladder"]
    for tier, (lo, hi) in ladder.items():
        if lo <= question_number <= hi:
            return tier
    raise ValueError("question_number %d not covered by ladder %s" % (question_number, ladder))


def check_entry_length_consistency(word_counts, target, tolerance_pct, cfg=None):
    """REF-LIST (20%) / REF-REF (30%): every entry within tolerance_pct of the target word
    count. Returns ok plus the list of offending (index, words) outliers. (SKILL.md
    'Entry Length Consistency Rule'; Rule #9.)"""
    if target <= 0:
        raise ValueError("target must be > 0")
    band = target * tolerance_pct / 100.0
    lo, hi = target - band, target + band
    outliers = [(i, w) for i, w in enumerate(word_counts) if w < lo or w > hi]
    return {"ok": not outliers, "target": target, "tolerance_pct": tolerance_pct,
            "band": [lo, hi], "outliers": outliers}


def selftest():
    cfg = load_config()
    checks = {}

    # Count claim: 500 entries at 3/page over 200 pages -> capacity 600, achievable, needs 167 pp.
    cc = check_count_claim(500, 3, 200)
    checks["count_claim_achievable"] = cc["ok"] and cc["capacity"] == 600 and cc["min_pages_needed"] == 167
    # 1000 claim at 2/page over 160 pages -> capacity 320, NOT achievable.
    checks["count_claim_unachievable"] = check_count_claim(1000, 2, 160)["ok"] is False
    # Final reconciliation.
    checks["reconcile_ok"] = reconcile_final_count(1005, 1000)["ok"] is True
    checks["reconcile_short"] = reconcile_final_count(980, 1000)["short_by"] == 20

    # Page count: 150 even and in REF-FACT [100,300]; 151 odd fails; 90 below REF-TRIVIA [100,200].
    checks["page_ok"] = check_page_count(150, "REF-FACT", cfg)["ok"] is True
    checks["page_odd_fail"] = check_page_count(151, "REF-FACT", cfg)["ok"] is False
    checks["page_below_range_fail"] = check_page_count(90, "REF-TRIVIA", cfg)["ok"] is False

    # Round architecture: 50 rounds x 10 = 500 questions, ok in 250-500 band.
    ra = validate_round_architecture(50, 10, [250, 500], cfg)
    checks["rounds_ok"] = ra["ok"] and ra["total_questions"] == 500
    # 5 rounds below the 10-50 range fails.
    checks["rounds_too_few_fail"] = validate_round_architecture(5, 10, None, cfg)["ok"] is False
    # qpr of 7 is not an allowed fixed count.
    checks["rounds_bad_qpr_fail"] = validate_round_architecture(30, 7, None, cfg)["ok"] is False

    # Difficulty ladder buckets.
    checks["ladder_accessible"] = difficulty_bucket(2, cfg) == "accessible"
    checks["ladder_moderate"] = difficulty_bucket(5, cfg) == "moderate"
    checks["ladder_specialist"] = difficulty_bucket(9, cfg) == "specialist"

    # Entry-length consistency: within 20% ok; a 150 vs 100 target (50% over) flagged.
    checks["entry_len_ok"] = check_entry_length_consistency([100, 110, 90, 118, 82], 100, 20, cfg)["ok"]
    bad = check_entry_length_consistency([100, 150], 100, 20, cfg)
    checks["entry_len_outlier_flagged"] = (not bad["ok"]) and bad["outliers"] == [(1, 150)]

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
