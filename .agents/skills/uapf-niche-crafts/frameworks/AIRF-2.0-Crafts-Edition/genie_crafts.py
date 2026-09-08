"""AIRF 2.0 Crafts Edition -- deterministic sizing operations for the crafts niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative):
the page-band <-> project-count table and its section/page ranges. Pure functions over
config.json so the production agent classify and validate IDENTICALLY. Crafts has no exact page
formula (project complexity varies; two-per-page is conditional), so this file does band
CLASSIFICATION and VALIDATION only -- it never invents an exact page count.

CLI:  python genie_crafts.py selftest
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def page_band(project_count, cfg=None):
    """Return the band name whose project range contains project_count, or None."""
    cfg = cfg or load_config()
    for name, b in cfg["page_bands"].items():
        if b["project_min"] <= project_count <= b["project_max"]:
            return name
    return None


def band_spec(name, cfg=None):
    cfg = cfg or load_config()
    return cfg["page_bands"].get(name)


def min_hero_images(project_count):
    """Every project unit carries at least one hero image -> >= project_count heroes."""
    if project_count < 0:
        raise ValueError("project_count must be >= 0")
    return project_count


def validate_sizing(project_count, page_count=None, section_count=None, cfg=None):
    """Validate a crafts book's sizing against the band table. Returns (ok, band, problems).
    Only checks what the framework actually fixes: project_count must fall in a band; if a
    page_count/section_count is supplied it must sit within that band's declared range."""
    cfg = cfg or load_config()
    problems = []
    band = page_band(project_count, cfg)
    if band is None:
        lo = min(b["project_min"] for b in cfg["page_bands"].values())
        hi = max(b["project_max"] for b in cfg["page_bands"].values())
        problems.append("project_count %d outside all bands (%d-%d)" % (project_count, lo, hi))
        return (False, None, problems)
    b = cfg["page_bands"][band]
    if page_count is not None and not (b["page_min"] <= page_count <= b["page_max"]):
        problems.append("page_count %d outside %s band range %d-%d" % (
            page_count, band, b["page_min"], b["page_max"]))
    if section_count is not None and not (b["sections_min"] <= section_count <= b["sections_max"]):
        problems.append("section_count %d outside %s band range %d-%d" % (
            section_count, band, b["sections_min"], b["sections_max"]))
    return (not problems, band, problems)


def selftest():
    cfg = load_config()
    checks = {}
    checks["band_compact"] = page_band(30, cfg) == "compact"
    checks["band_standard"] = page_band(50, cfg) == "standard"
    checks["band_extended"] = page_band(100, cfg) == "extended"
    checks["band_none_low"] = page_band(10, cfg) is None
    checks["band_none_high"] = page_band(200, cfg) is None
    checks["hero_min"] = min_hero_images(50) == 50
    ok, band, _ = validate_sizing(50, page_count=220, section_count=6, cfg=cfg)
    checks["valid_standard_ok"] = ok and band == "standard"
    bad_ok, _, bad = validate_sizing(120, page_count=150, cfg=cfg)  # 120 is extended, 150 too few
    checks["bad_pagecount_flagged"] = (not bad_ok) and len(bad) >= 1
    out_ok, _, out = validate_sizing(200, cfg=cfg)
    checks["out_of_band_flagged"] = (not out_ok) and len(out) >= 1
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
