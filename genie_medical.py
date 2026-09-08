"""AIRF 2.0 Medical Edition -- deterministic production operations for the OV-MEDT medical niche.

Machine-executable projection of the computable rules in ../../SKILL.md (authoritative). Pure
functions over config.json so results are fully deterministic. No niche architecture is
defined here; SKILL.md remains the source of truth for reasoning/design.

CLI:  python genie_medical.py selftest
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(HERE, "config.json"), encoding="utf-8") as fh:
        return json.load(fh)


def subtitle_length_ok(title, subtitle, cfg=None):
    """Combined title + subtitle must remain under 200 characters (SKILL.md Step 8).
    Returns (ok, combined_len)."""
    cfg = cfg or load_config()
    limit = cfg["subtitle"]["title_plus_subtitle_char_max"]
    combined = len((title or "").strip()) + len((subtitle or "").strip())
    return (combined < limit, combined)


def validate_chapter_pages(pages, cfg=None):
    """A chapter must meet the 23-page hard floor (SKILL.md page-band). Returns (ok, floor)."""
    cfg = cfg or load_config()
    floor = cfg["page_floors"]["min_pages_per_chapter"]
    return (pages >= floor, floor)


def validate_book_pages(chapter_pages, cfg=None):
    """Validate the whole book against OV-MEDT floors: total 400-550, chapter count 10-20, and
    every chapter >= 23 pages. `chapter_pages` is a list of per-chapter page counts (chapters
    only, not front/back matter). Returns (ok, [problems], total)."""
    cfg = cfg or load_config()
    pf = cfg["page_floors"]
    problems = []
    n = len(chapter_pages)
    total = sum(chapter_pages)
    if n < pf["chapter_count_min"] or n > pf["chapter_count_max"]:
        problems.append("chapter count %d outside %d-%d" % (
            n, pf["chapter_count_min"], pf["chapter_count_max"]))
    for i, p in enumerate(chapter_pages, 1):
        if p < pf["min_pages_per_chapter"]:
            problems.append("chapter %d has %d pages (min %d)" % (
                i, p, pf["min_pages_per_chapter"]))
    if total < pf["book_total_min"] or total > pf["book_total_max"]:
        problems.append("chapter-page total %d outside %d-%d" % (
            total, pf["book_total_min"], pf["book_total_max"]))
    return (not problems, problems, total)


def body_word_estimate(pages, subchapter_images, feature_boxes, cfg=None):
    """Estimate body-prose word range for a chapter using the SKILL.md page-to-word calibration:
    a full text page carries ~650-700 words; each per-subchapter image+caption ~1/3 page; each
    feature box ~1/4 to 1/3 page. Returns {low, high, body_pages}."""
    cfg = cfg or load_config()
    c = cfg["page_to_word_calibration"]
    img_frac = c["image_plus_caption_page_fraction"]
    box_frac = c["feature_box_page_fraction_max"]
    non_body = subchapter_images * img_frac + feature_boxes * box_frac
    body_pages = max(0.0, pages - non_body)
    return {
        "body_pages": round(body_pages, 2),
        "low": int(round(body_pages * c["words_per_full_text_page_min"])),
        "high": int(round(body_pages * c["words_per_full_text_page_max"])),
    }


def meets_word_floor(budgeted_body_words, cfg=None):
    """A chapter blueprint must budget at least the body-word floor (13,000) before images,
    captions, and feature boxes (SKILL.md Gate 2). Returns (ok, floor)."""
    cfg = cfg or load_config()
    floor = cfg["page_to_word_calibration"]["chapter_body_word_floor"]
    return (budgeted_body_words >= floor, floor)


def learning_objectives_ok(count, cfg=None):
    """Learning objectives per chapter must fall within 4-6 (SKILL.md). Returns (ok, min, max)."""
    cfg = cfg or load_config()
    s = cfg["chapter_structure"]
    lo, hi = s["learning_objectives_min"], s["learning_objectives_max"]
    return (lo <= count <= hi, lo, hi)


def feature_box_selection_ok(selected_names, cfg=None):
    """Validate the feature-box selection: 3-5 types, all drawn from the Medical Feature Box
    System library. Returns (ok, [problems])."""
    cfg = cfg or load_config()
    fb = cfg["feature_boxes"]
    library = set(fb["library"])
    problems = []
    n = len(selected_names)
    if n < fb["select_min"] or n > fb["select_max"]:
        problems.append("selected %d box types (must be %d-%d)" % (
            n, fb["select_min"], fb["select_max"]))
    for name in selected_names:
        if name not in library:
            problems.append("box type %r not in Medical Feature Box System" % name)
    return (not problems, problems)


def image_slot_count(subchapters_per_chapter):
    """Image contract: exactly one photorealistic image per numbered subchapter. Given a list of
    subchapter counts (one entry per chapter), returns the total required image slots."""
    return sum(subchapters_per_chapter)


def image_labels_ok(label_count, cfg=None):
    """Verbatim label set is 8-12 maximum; more than the max means split into two images
    (SKILL.md six-part recipe, Part 4). Returns (ok, max)."""
    cfg = cfg or load_config()
    mx = cfg["visual"]["image_label_max"]
    return (1 <= label_count <= mx, mx)


def selftest():
    cfg = load_config()
    checks = {}

    ok, combined = subtitle_length_ok(
        "Clinical Cardiology for Nursing Students",
        "A Case-Based, Mechanism-Focused Textbook with Dual-Verified Accuracy", cfg)
    checks["subtitle_under_200_ok"] = ok and combined < 200
    checks["subtitle_over_200_flagged"] = not subtitle_length_ok("x" * 150, "y" * 60, cfg)[0]

    checks["chapter_23_ok"] = validate_chapter_pages(23, cfg)[0]
    checks["chapter_22_flagged"] = not validate_chapter_pages(22, cfg)[0]

    # 16 chapters * 28 pages = 448 total, within 400-550, count within 10-20
    good_book = [28] * 16
    ok_b, probs_b, total_b = validate_book_pages(good_book, cfg)
    checks["good_book_ok"] = ok_b and total_b == 448
    # too few chapters + one short chapter
    ok_bad, probs_bad, _ = validate_book_pages([28, 20], cfg)
    checks["bad_book_flagged"] = (not ok_bad) and len(probs_bad) >= 2

    est = body_word_estimate(23, 5, 6, cfg)
    # calibration should land the high end near the SKILL worked example (~13,500-14,500)
    checks["word_estimate_reasonable"] = 12000 <= est["high"] <= 15000 and est["low"] < est["high"]

    checks["word_floor_ok"] = meets_word_floor(13000, cfg)[0]
    checks["word_floor_below_flagged"] = not meets_word_floor(12500, cfg)[0]

    checks["objectives_5_ok"] = learning_objectives_ok(5, cfg)[0]
    checks["objectives_3_flagged"] = not learning_objectives_ok(3, cfg)[0]
    checks["objectives_7_flagged"] = not learning_objectives_ok(7, cfg)[0]

    ok_fb, _ = feature_box_selection_ok(
        ["Clinical Pearl", "Red Flag Alert", "Pathophysiology Spotlight", "Evidence Base"], cfg)
    checks["feature_box_ok"] = ok_fb
    bad_fb_ok, bad_fb_probs = feature_box_selection_ok(["Clinical Pearl", "Made Up Box"], cfg)
    checks["feature_box_flagged"] = (not bad_fb_ok) and len(bad_fb_probs) >= 2

    checks["image_slots"] = image_slot_count([5, 4, 6, 5]) == 20
    checks["labels_10_ok"] = image_labels_ok(10, cfg)[0]
    checks["labels_13_flagged"] = not image_labels_ok(13, cfg)[0]

    print(json.dumps({"checks": checks, "all_pass": all(checks.values())}, indent=2))
    return all(checks.values())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        raise SystemExit(0 if selftest() else 1)
    print(__doc__)
