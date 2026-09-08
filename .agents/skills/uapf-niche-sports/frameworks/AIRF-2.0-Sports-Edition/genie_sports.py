"""AIRF 2.0 Sports Edition -- deterministic production operations for the Sports & Outdoors niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture
is defined here; SKILL.md remains the source of truth for reasoning/voice/design.

Computable surface for this niche:
  - coaching session-plan block minutes (percentages must sum to 100)
  - Skill-Progression Architecture completeness (4 ordered stages, 3 drill levels, 3-5 faults)
  - OV-HEALTH R2 running weekly-mileage 10% conservative ceiling
  - segment-driven body point-size validation (S1-S6)
  - sub-niche page-band membership
  - Pre-TOC Report item count (19)

CLI:  python genie_sports.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def session_plan_minutes(total_minutes, cfg=None):
    """Resolve the coaching session-plan block percentages to concrete minutes for a given
    total session duration. Raises if the configured percentages do not sum to 100. Returns
    an ordered list of {element, pct, minutes}; minutes are rounded but re-summed to total on
    the final block so the plan always adds up to `total_minutes`."""
    cfg = cfg or load_config()
    plan = cfg["coaching_session_plan"]
    blocks = plan["blocks"]
    pct_sum = sum(b["pct"] for b in blocks)
    if pct_sum != plan["pct_total"] or pct_sum != 100:
        raise ValueError("session-plan percentages sum to %d, expected 100" % pct_sum)
    if total_minutes <= 0:
        raise ValueError("total_minutes must be > 0")
    out = []
    allocated = 0
    for i, b in enumerate(blocks):
        if i < len(blocks) - 1:
            mins = round(total_minutes * b["pct"] / 100)
            allocated += mins
        else:
            mins = total_minutes - allocated  # remainder closes to exact total
        out.append({"element": b["element"], "pct": b["pct"], "minutes": mins})
    return out


def validate_skill_progression(stages_declared, drill_levels, fault_count, cfg=None):
    """Validate a technique chapter against SR2. `stages_declared` is the ordered list of stage
    keys present; `drill_levels` the list of graded standard levels; `fault_count` the number of
    faults in the Stage-4 catalog. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    sp = cfg["skill_progression"]
    problems = []
    if list(stages_declared) != sp["stages"]:
        problems.append("stages %r != required ordered %r" % (list(stages_declared), sp["stages"]))
    if sorted(drill_levels) != sorted(sp["drill_standard_levels"]):
        problems.append("drill levels %r != required %r" % (
            list(drill_levels), sp["drill_standard_levels"]))
    if fault_count < sp["fault_catalog_min"] or fault_count > sp["fault_catalog_max"]:
        problems.append("fault catalog has %d faults (must be %d-%d)" % (
            fault_count, sp["fault_catalog_min"], sp["fault_catalog_max"]))
    return (not problems, problems)


def validate_weekly_mileage(prev_week_miles, this_week_miles, has_stated_rationale=False, cfg=None):
    """OV-HEALTH R2 running rule: weekly mileage increase should not exceed the conservative
    ceiling (default 10%) unless an explicit rationale + prerequisite fitness statement is given.
    Returns {ok, increase_pct, ceiling_pct}."""
    cfg = cfg or load_config()
    ceiling = cfg["ov_health_r2"]["running_weekly_mileage_increase_ceiling_pct"]
    if prev_week_miles <= 0:
        raise ValueError("prev_week_miles must be > 0")
    increase_pct = (this_week_miles - prev_week_miles) / prev_week_miles * 100.0
    ok = increase_pct <= ceiling + 1e-9 or has_stated_rationale
    return {"ok": ok, "increase_pct": round(increase_pct, 2), "ceiling_pct": ceiling,
            "override_by_rationale": bool(has_stated_rationale and increase_pct > ceiling)}


def validate_body_pt(segment, body_pt, cfg=None):
    """Validate a selected body point size against the dominant audience segment's allowed
    range (S1-S6). Returns (ok, [problems])."""
    cfg = cfg or load_config()
    segs = cfg["audience_segments"]
    if segment not in segs:
        raise ValueError("unknown segment %r (allowed: %s)" % (segment, list(segs)))
    lo, hi = segs[segment]["body_pt_min"], segs[segment]["body_pt_max"]
    if lo <= body_pt <= hi:
        return (True, [])
    return (False, ["body_pt %s outside %s range %d-%d" % (body_pt, segment, lo, hi)])


def check_page_band(sub_niche, page_count, cfg=None):
    """Compare a projected/recommended page count to the sub-niche baseline band. Returns
    {ok, sub_niche, pages, band}."""
    cfg = cfg or load_config()
    bands = cfg["page_bands"]
    if sub_niche not in bands or not isinstance(bands[sub_niche], list):
        raise ValueError("unknown sub_niche %r (allowed: %s)" % (
            sub_niche, [k for k, v in bands.items() if isinstance(v, list)]))
    lo, hi = bands[sub_niche]
    return {"ok": lo <= page_count <= hi, "sub_niche": sub_niche,
            "pages": page_count, "band": [lo, hi]}


def pre_toc_item_count(items_present, cfg=None):
    """Pre-TOC Report must carry all required items (19). Returns (ok, expected, got)."""
    cfg = cfg or load_config()
    expected = cfg["phase0_pre_toc_report_items"]
    return (items_present == expected, expected, items_present)


def selftest():
    cfg = load_config()
    checks = {}

    # 60-minute session -> 15/20/25/30/10% = 9/12/15/18/6 = 60
    plan = session_plan_minutes(60, cfg)
    checks["session_sums_to_total"] = sum(b["minutes"] for b in plan) == 60
    checks["session_warmup_9"] = plan[0]["minutes"] == 9
    checks["session_game_18"] = plan[3]["minutes"] == 18
    # 90-minute session still closes to exact total
    checks["session_90_sums"] = sum(b["minutes"] for b in session_plan_minutes(90, cfg)) == 90

    ok_sp, _ = validate_skill_progression(
        cfg["skill_progression"]["stages"],
        ["beginner", "intermediate", "advanced"], 4, cfg)
    checks["skill_progression_ok"] = ok_sp
    bad_sp, probs = validate_skill_progression(
        ["fundamentals", "drills_with_reps_and_standards"], ["beginner"], 2, cfg)
    checks["skill_progression_flags_all"] = (not bad_sp) and len(probs) == 3

    checks["mileage_10pct_ok"] = validate_weekly_mileage(20, 22, False, cfg)["ok"]
    checks["mileage_20pct_flagged"] = validate_weekly_mileage(20, 24, False, cfg)["ok"] is False
    over = validate_weekly_mileage(20, 24, True, cfg)
    checks["mileage_override_by_rationale"] = over["ok"] and over["override_by_rationale"]

    ok_pt, _ = validate_body_pt("S3_youth", 14, cfg)
    checks["body_pt_youth_ok"] = ok_pt
    bad_pt, _ = validate_body_pt("S2_serious_amateur", 14, cfg)
    checks["body_pt_amateur_flagged"] = bad_pt is False

    checks["page_band_survival_in"] = check_page_band("survival_bushcraft", 260, cfg)["ok"]
    checks["page_band_fishing_out"] = check_page_band("fishing", 300, cfg)["ok"] is False

    ok_toc, exp, got = pre_toc_item_count(19, cfg)
    checks["pre_toc_19_ok"] = ok_toc and exp == 19 and got == 19
    checks["pre_toc_short_flagged"] = pre_toc_item_count(17, cfg)[0] is False

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
