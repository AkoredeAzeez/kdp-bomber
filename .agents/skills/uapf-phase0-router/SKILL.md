---
name: uapf-phase0-router
description: Analyze a title, route it to the correct UAPF overlay and risk regime, generate five compliant subtitles, create the byline and auto-configuration package, and auto-proceed after validation.
---

1. Read Master Phase 0, router, risk, language, trim, formatting, and relevant
   overlay sections.
2. IMMEDIATELY after the title is received and the marketplace is detected or
   inferred, invoke **uapf-trademark-checker**. This gate runs BEFORE subtitle
   generation, routing confirmation, or any content work. Only CLEAR or an
   explained CAUTION may continue; HIGH RISK stops the pipeline and presents
   safer alternative titles; UNVERIFIED is queued as a blocker and reported
   honestly.
3. After trademark clearance passes, invoke **uapf-kdp-niche-specialist** in
   TITLE INTELLIGENCE mode. It builds the competitive frame (top-10 competitor
   table, gap analysis, page/price bands, category picks, keyword list) and
   writes `phase0/kdp-market-intelligence.md`. The exact-title competitor list
   from the trademark checker seeds its competitor table.
4. Inventory supplied sources and extract locked details verbatim.
5. Analyze subject, audience, format, marketplace, language, risk, and competitor
   signals — citing the market-intelligence report instead of re-researching.
6. Select the primary overlay, modifiers, risk regime, and inheritance chain.
7. Generate exactly five subtitle candidates and run the required compliance
   battery. Select the strongest passing option. Re-run uapf-trademark-checker
   on any subtitle that introduces a new distinctive term.
8. Generate the byline under the Master’s format and collision rules. Never invent
   credentials or a biography.
9. Resolve audience, language, marketplace, length, trim, research pathway,
   visuals, assessments, supplements, format profile, and expert-role panel.
10. Run eponym, byline, and catalog-collision checks with the data actually
    available. Mark unavailable registries rather than claiming a pass. (Title
    trademark clearance was already completed in step 2 — cite its report.)
11. Write all Phase 0 records and auto-proceed after the package passes. Every
    project's `book_lock.md` ROUTING BLOCK MUST carry, verbatim, one canonical
    machine-readable classification line so continuity and failover tools can read
    the locked decision deterministically (no guessing):
    `- Classification (locked, machine-readable): overlay=<OV-CODE>; selected_skill=uapf-niche-<x>; framework=<NAME VERSION>; classification_locked=true; framework_locked=true`
    Fill it from the overlay and niche skill chosen in the ROUTING DECISION BLOCK
    (see the invocation table in step 12) and the active framework name/version.
    Never change it after Phase 0 except on an explicit operator reclassification order.
12. After announcing the ROUTING DECISION BLOCK, immediately invoke the matching
    niche skill using the table below. Do not wait for the user to type PROCEED —
    auto-invoke the niche skill as part of Phase 0 completion.

    NICHE SKILL INVOCATION TABLE:
    OV-COOK   → invoke uapf-niche-cookbook
    OV-TEXT   → invoke uapf-niche-textbook
    OV-MEDT   → invoke uapf-niche-medical
    OV-WORK   → invoke uapf-niche-workbook
    OV-STUDY  → invoke uapf-niche-study-guide
    OV-EXSIM  → invoke uapf-niche-exam-simulator
    OV-CHILD  → invoke uapf-niche-childrens
    OV-CFACT  → invoke uapf-niche-childrens-facts
    OV-ACT    → invoke uapf-niche-activity
    OV-CRAFT  → invoke uapf-niche-crafts
    OV-HEALTH → invoke uapf-niche-health
    OV-SELF   → invoke uapf-niche-selfhelp
    OV-HOWTO  → invoke uapf-niche-howto
    OV-HUMOR  → invoke uapf-niche-humor
    OV-HIST   → invoke uapf-niche-history
    OV-FIC    → invoke uapf-niche-fiction (UFFV 1.1 parent; it detects the
                sub-genre and loads one of the 12 overlay skills:
                romance/thriller/mystery/fantasy/scifi/horror/literary/
                historical/ya/action/womens/faith)
    OV-PD     → invoke uapf-niche-public-domain
    OV-TRAVEL → invoke uapf-niche-travel
    OV-GUIDE  → invoke uapf-niche-user-guide
    OV-LOWC   → invoke uapf-niche-journal
    OV-FAITH  → invoke uapf-niche-faith
    OV-BIZ    → invoke uapf-niche-business
    OV-BIO    → invoke uapf-niche-biography
    OV-PARENT → invoke uapf-niche-parenting
    OV-SPORT  → invoke uapf-niche-sports
    OV-LANG   → invoke uapf-niche-language
    OV-POET   → invoke uapf-niche-poetry
    OV-REF    → invoke uapf-niche-reference
    OV-POPSCI → invoke uapf-niche-popular-science

    For hybrid stacks (e.g., OV-WORK + OV-MEDT), invoke the FORMAT overlay's
    niche skill first, then state the SUBJECT overlay's panel and risk regime.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
