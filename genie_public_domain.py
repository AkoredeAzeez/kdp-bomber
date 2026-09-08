"""AIRF 2.0 Public Domain Edition -- deterministic screening operations for the public-domain niche.

Machine-executable projection of the deterministic term rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic.

IMPORTANT: these functions are a SCREENING AID only, not legal advice and not a substitute for
the 7-Point Legal Verification Checklist. The Publishing-Rights Analyst's verified sources and
absolute stop authority (SKILL.md) remain authoritative; a "PD" screen here still requires the
full evidence-based checklist to PASS.

CLI:  python genie_public_domain.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def us_pd_cutoff_year(production_year, cfg=None):
    """US rolling cutoff: works first published before this year are PD in the US.
    = production_year - us_rolling_offset_years (96 -> 1930 in production year 2026)."""
    cfg = cfg or load_config()
    return production_year - cfg["legal_term_rules"]["us_rolling_offset_years"]


def us_public_domain_status(publication_year, production_year, cfg=None):
    """Screen the US publication-date point (checklist point 2).
    Returns one of:
      'PD'                         -> published before the rolling cutoff
      'REQUIRES_RENEWAL_ANALYSIS'  -> within us_renewal_analysis_range (fails if inconclusive)
      'IN_COPYRIGHT_LIKELY'        -> after the renewal range
    """
    cfg = cfg or load_config()
    cutoff = us_pd_cutoff_year(production_year, cfg)
    lo, hi = cfg["legal_term_rules"]["us_renewal_analysis_range"]
    if publication_year < cutoff:
        return "PD"
    if lo <= publication_year <= hi:
        return "REQUIRES_RENEWAL_ANALYSIS"
    return "IN_COPYRIGHT_LIKELY"


def life_plus_70_pd(author_death_year, production_year, cfg=None):
    """Screen the EU/DE and UK points (checklist points 3 and 4): PD only if the author died
    MORE THAN 70 full calendar years before the production year."""
    cfg = cfg or load_config()
    n = cfg["legal_term_rules"]["life_plus_70_years"]
    return (production_year - author_death_year) > n


def meets_differentiation_floor(original_illustrations, apparatus_pages, total_pages, cfg=None):
    """Screen the KDP value-add differentiation floor (Gate 4).
    Passes if 10+ original illustrations OR apparatus ratio >= 0.15. Returns (ok, ratio)."""
    cfg = cfg or load_config()
    floor = cfg["value_add_floor"]
    ratio = (apparatus_pages / total_pages) if total_pages else 0.0
    ok = (original_illustrations >= floor["original_illustrations_min"]
          or ratio >= floor["intro_plus_apparatus_ratio_min"])
    return (ok, round(ratio, 4))


def selftest():
    cfg = load_config()
    checks = {}
    # US rolling cutoff: 2026 -> 1930
    checks["us_cutoff_2026"] = us_pd_cutoff_year(2026, cfg) == 1930
    checks["us_pd_1925"] = us_public_domain_status(1925, 2026, cfg) == "PD"
    checks["us_renewal_1950"] = us_public_domain_status(1950, 2026, cfg) == "REQUIRES_RENEWAL_ANALYSIS"
    checks["us_incopyright_1990"] = us_public_domain_status(1990, 2026, cfg) == "IN_COPYRIGHT_LIKELY"
    checks["us_boundary_1930"] = us_public_domain_status(1930, 2026, cfg) == "REQUIRES_RENEWAL_ANALYSIS"
    # life+70: died 1950, production 2026 -> 76 > 70 -> PD
    checks["life70_pd"] = life_plus_70_pd(1950, 2026, cfg) is True
    # died 1960 -> 66 not > 70 -> not PD
    checks["life70_not_pd"] = life_plus_70_pd(1960, 2026, cfg) is False
    # exactly 70 years -> not > 70 -> not PD
    checks["life70_boundary"] = life_plus_70_pd(1956, 2026, cfg) is False
    # differentiation floor
    ok_ill, _ = meets_differentiation_floor(12, 5, 300, cfg)
    checks["floor_by_illustrations"] = ok_ill is True
    ok_ratio, ratio = meets_differentiation_floor(0, 60, 300, cfg)
    checks["floor_by_ratio"] = ok_ratio is True and ratio == 0.2
    bad, _ = meets_differentiation_floor(3, 10, 300, cfg)
    checks["floor_fails_thin"] = bad is False
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
