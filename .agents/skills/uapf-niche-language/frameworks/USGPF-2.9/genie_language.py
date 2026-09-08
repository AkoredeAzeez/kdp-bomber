"""USGPF 2.9 -- deterministic production operations for the language-learning niche.

Machine-executable projection of the deterministic rules in ../../SKILL.md (authoritative).
Pure functions over config.json so results are fully deterministic. No niche
architecture is defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_language.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def _band(value, lo, hi, label):
    problems = []
    if value < lo:
        problems.append("%s %s below minimum %s" % (label, value, lo))
    if value > hi:
        problems.append("%s %s above maximum %s" % (label, value, hi))
    return (not problems, problems)


def validate_vocabulary_load(count, cfg=None):
    """20-40 new vocabulary items per unit."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(count, u["vocabulary_items_min"], u["vocabulary_items_max"], "vocabulary_items")


def validate_dialogue_turns(turns, cfg=None):
    """Dialogue is 8-16 speaker turns."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(turns, u["dialogue_turns_min"], u["dialogue_turns_max"], "dialogue_turns")


def validate_grammar_points(count, cfg=None):
    """Exactly one grammar point per unit, no exceptions."""
    cfg = cfg or load_config()
    want = cfg["unit_limits"]["grammar_points_per_unit"]
    if count == want:
        return (True, [])
    return (False, ["grammar_points %s != required %s" % (count, want)])


def validate_grammar_examples(count, cfg=None):
    """3-5 example sentences for the unit's grammar point."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(count, u["grammar_examples_min"], u["grammar_examples_max"], "grammar_examples")


def validate_drills(count, cfg=None):
    """3-5 drills per unit."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(count, u["drills_min"], u["drills_max"], "drills")


def validate_cultural_note(word_count, cfg=None):
    """Cultural note runs 100-150 words."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(word_count, u["cultural_note_words_min"], u["cultural_note_words_max"],
                 "cultural_note_words")


def validate_unit_pages(pages, cfg=None):
    """Unit length band on render is 4-8 pages."""
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return _band(pages, u["unit_page_band_min"], u["unit_page_band_max"], "unit_pages")


def unit_pages_band(num_units, cfg=None):
    """Total body page band for the units: (min_pages, max_pages) = (4N, 8N)."""
    if num_units < 0:
        raise ValueError("num_units must be >= 0")
    cfg = cfg or load_config()
    u = cfg["unit_limits"]
    return (u["unit_page_band_min"] * num_units, u["unit_page_band_max"] * num_units)


def glossary_size(per_unit_vocab_counts):
    """Glossary covers every vocabulary item introduced across all units -> sum."""
    return sum(int(x) for x in per_unit_vocab_counts)


def answer_key_item_count(per_unit_drill_counts):
    """Answer key covers every drill item in every unit -> sum."""
    return sum(int(x) for x in per_unit_drill_counts)


def validate_byline_locations(count, cfg=None):
    """Byline appears in exactly two interior locations (title page + copyright attribution)."""
    cfg = cfg or load_config()
    want = cfg["byline"]["interior_locations"]
    if count == want:
        return (True, [])
    return (False, ["byline_locations %s != required %s" % (count, want)])


def validate_subtitle(text, cfg=None):
    """Letters, numerals, and spaces only; two rendered lines or fewer.
    Line count is estimated from explicit newlines in the composed candidate."""
    cfg = cfg or load_config()
    max_lines = cfg["subtitle"]["max_rendered_lines"]
    problems = []
    for ch in text:
        if not (ch.isalnum() or ch == " " or ch == "\n"):
            problems.append("subtitle contains disallowed character %r" % ch)
            break
    lines = [ln for ln in text.split("\n") if ln.strip()]
    if len(lines) > max_lines:
        problems.append("subtitle renders %d lines (max %d)" % (len(lines), max_lines))
    return (not problems, problems)


def selftest():
    cfg = load_config()
    checks = {}
    checks["vocab_ok"] = validate_vocabulary_load(30, cfg)[0]
    checks["vocab_low_flagged"] = not validate_vocabulary_load(12, cfg)[0]
    checks["vocab_high_flagged"] = not validate_vocabulary_load(55, cfg)[0]
    checks["dialogue_ok"] = validate_dialogue_turns(12, cfg)[0]
    checks["dialogue_flagged"] = not validate_dialogue_turns(20, cfg)[0]
    checks["one_grammar_ok"] = validate_grammar_points(1, cfg)[0]
    checks["two_grammar_flagged"] = not validate_grammar_points(2, cfg)[0]
    checks["grammar_examples_ok"] = validate_grammar_examples(4, cfg)[0]
    checks["grammar_examples_flagged"] = not validate_grammar_examples(2, cfg)[0]
    checks["drills_ok"] = validate_drills(4, cfg)[0]
    checks["drills_flagged"] = not validate_drills(6, cfg)[0]
    checks["cultural_ok"] = validate_cultural_note(125, cfg)[0]
    checks["cultural_flagged"] = not validate_cultural_note(200, cfg)[0]
    checks["unit_pages_ok"] = validate_unit_pages(6, cfg)[0]
    checks["unit_pages_flagged"] = not validate_unit_pages(9, cfg)[0]
    checks["unit_band_12"] = unit_pages_band(12, cfg) == (48, 96)
    checks["glossary_sum"] = glossary_size([30, 25, 35, 20]) == 110
    checks["answer_key_sum"] = answer_key_item_count([4, 5, 3, 4]) == 16
    checks["byline_ok"] = validate_byline_locations(2, cfg)[0]
    checks["byline_flagged"] = not validate_byline_locations(3, cfg)[0]
    checks["subtitle_ok"] = validate_subtitle("Master Everyday Conversations", cfg)[0]
    checks["subtitle_char_flagged"] = not validate_subtitle("Learn Spanish -- Fast", cfg)[0]
    checks["subtitle_lines_flagged"] = not validate_subtitle("one\ntwo\nthree", cfg)[0]
    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
