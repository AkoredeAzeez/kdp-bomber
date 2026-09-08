# UFFV 1.1 FICTION-PROMPT (executable pipeline)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> Authoritative UFFV 1.1 source, embedded verbatim. The parent
> SKILL.md operationalizes this; on any conflict this document governs,
> above it the operator's live instructions govern.

PEGASUS PRESS
UFFV 1.1 FICTION-PROMPT
EXECUTABLE PIPELINE DOCUMENT
Companion to fiction-framework (UFFV 1.1 Master Framework, governing)
Runtime scripts, gate templates, artifact formats, and reference cards for every phase
August 2026
CONTENTS
## RUN 0: RUNTIME BINDING
Load order. Load fiction-framework (the UFFV 1.1 Master Framework) before executing anything in this document. This document is the executor; the framework governs. On any conflict, the framework wins, and above the framework, the operator's live instructions win (framework Section 0.4).
Voice. Every block below is written to the assistant as runtime instruction. Run the blocks in order; never skip a gate; close every phase with exactly the line Type Proceed and stop for the operator.
Honest states. Report external operations only as they actually ran: PASS, FAIL, NOT RUN, PENDING, UNVERIFIED, READY FOR IMPORT (framework Rule 9).
Standing sweeps. At every gate, before printing the gate block: run the em dash and en dash scan (must return zero), the declared-rating spot check, and the governor line. These three never wait for QA.
## RUN 1: PHASE 0, INTAKE AND DETECTION
Step 1. Receive the title or brief. Extract: working title, manuscript language, target marketplace(s), imprint. Missing values: language defaults to the title's language, marketplace to Amazon.com, imprint to the operator's named default.
Step 2. Detect the primary overlay from the framework Section 2 triggers and the Section 3 registry. Detect at most one modifier. Detect format (FMT-NOVEL default). If two primaries genuinely tie, ask the operator ONE question offering exactly those two; otherwise never ask.
Step 3. Record the content rating: UFFV-Clean only if the operator or brief says so; otherwise UFFV-Mainstream by default (framework Rule 1). Where Mainstream and the overlay requires it, note that heat and intensity declarations are due at Phase 1.
Step 4. Run the catalogue uniqueness check against Pegasus_Press_Book_Register.xlsx: title collision, premise collision, protagonist name and occupation pairing. If the register is not uploaded, report NOT RUN and continue.
Step 5. Generate the pen name from fakenamegenerator.com in First Name, Initial(s). Surname format; screen it against real living authors (live web, else NOT RUN); lock it.
Step 6. FMT-SERIAL, Book 2 and later: load the Series Bible and the prior book's closing ledger snapshots (continuity, timeline, arc outcomes, invented terms, cover base colors); initialize this book's ledgers from that state per framework 14.5.
Step 7. Create run_state.md and print the Phase 0 gate block and stop.
UFFV 1.1 RUN | PHASE 0: INTAKE AND DETECTION
Title: {working title}
Language: {lang} | Marketplace: {mkt} | Imprint: {imprint}
Overlay: {OV-XXX} | Modifier: {OV-YYY or none} | Format: {FMT-XXXX}
Rationale: {one line}
Content rating: {UFFV-Clean | UFFV-Mainstream (default)}
Uniqueness: {PASS | CONFLICT: register row | NOT RUN: register not uploaded}
Pen name: {First M. Surname} | Author screen: {PASS | NOT RUN}
Series: {standalone | Book N: bible loaded, ledgers carried}
run_state.md: created
Gate register: Phase 0 COMPLETE.
Type Proceed
## RUN 2: PHASE 0.5, SCREENS
Step 1. Trademark screen: working title and any planned series name against live trademark and marketplace search. Apply the TM-Safe Reframe Layer to any hit: strip the mark, keep any credential or place nominatively where lawful, rebuild.
Step 2. Real-person screen: premise and any pre-named characters against famous living persons. Historical figures pass only under framework Rule 27 conditions.
Step 3. If the premise is inspired by real events, run the defamation and dignity review: identifiability of living persons, portrayal risk, and the fictionalization distance required.
Step 4. Print the gate block and stop.
PHASE 0.5: SCREENS
Trademark (title/series): {PASS | REFRAME APPLIED: detail | NOT RUN}
Real-person screen: {PASS | FLAG: name, action | NOT RUN}
Real-events review: {N/A | PASS | CONDITIONS: list}
Type Proceed
## RUN 3: PHASE 1, STORY SPEC
Step 1. Draft every field of the Story Spec (framework 5.1) in one page. Select the structure from the Structure Library with a one-line rationale. Lock POV, tense, and budgets from the overlay tables.
Step 2. Where the rating is Mainstream, capture the declarations the overlay requires: ROM heat ceiling; THR, HOR, ACT intensity lane; language frequency ceiling if profanity will appear.
Step 3. Non-English manuscript: generate the localized prose tool sets (framework 8.10: minimum twenty-five native blacklist entries, ten native filter constructions) and append them to the spec.
Step 4. Write the spec to story_spec.md, print it in full in chat, and stop.
story_spec.md
Title: {..}   Series: {none | Name, Book N}
Imprint: {..}   Pen name: {..}   Language: {..}   Marketplace: {..}
Overlay: {OV-XXX} + {modifier/none}   Format: {FMT-..}   Age band: {Adult|YA}
Rating: {UFFV-Clean | UFFV-Mainstream}   Declarations: {heat/intensity/language or n/a}
Premise: {protagonist} wants {want} but {obstacle}, and if they fail {stakes}.
Dramatic question: Will {..}?
Theme statement: {what the book says}   Motif (Leitwortstil): {..}
Setting: {time} | {place} | {social frame}
Structure: {UFFV-....} because {one line}
POV: {type; viewpoint list}   Tense: {past|present}
Budget: {total} words | {N} chapters | band {a}-{b} | tolerance 10 percent
Comparable positioning (generic, no names): {one line}
Localized prose tools: {n/a | appended: {n} blacklist, {n} filter}
Type Proceed
## RUN 4: PHASE 2, CHARACTER BIBLE
Step 1. Build the Protagonist Sheet (fourteen fields), the Antagonist Sheet (plus plan, why-right, mirror, pressure schedule), and the Supporting Cast Register within the Appendix D casting cap. Enforce the naming law; log three voice markers per major character.
Step 2. Initialize continuity_ledger.md, chekhov_registry.md, and the Arc Tracking Ledger from the sheets.
Step 3. Print the bible summary block, write character_bible.md, and stop.
character_bible.md (sheet format, one block per character)
[PROTAGONIST] Name: {..}  Age: {..}  Trade: {..}
Want: {..}   Need: {..}   Wound: {..}   Lie: {..}
Strengths: {1;2;3}   Flaws: {1;2;3}
Anchors (3): {..}   Voice markers (3): {..}
Arc: {positive|flat|negative} | Milestones: A1 {..} MID {..} DN {..} CLI {..}
Relationships: {name: one line} ...
Knowledge at page one: {..}   Values note: {..}   Essence: {one sentence}
[ANTAGONIST] ...same fields... Plan: {pre-page-one; act 1; act 2; act 3}
Why right: {..}   Mirror: {..}   Pressure schedule: {ch list}
[REGISTER] {Name | role | essence | anchor | first ch}  (cap: {n}/{cap})
Ledgers initialized: continuity, chekhov, arc.
Type Proceed
## RUN 5: PHASE 3, WORLD GATE (CONDITIONAL)
Step 1. Route by overlay: OV-FAN and OV-SFI build the World Bible; OV-HIS builds the Era Brief through uapf-research-compliance; every other overlay builds the Setting Sheet only.
Step 2. Lock the system triad (source, cost, limit) for any magic or technology before proceeding; open invented_terms.md and log every coined word from this point forward.
Step 3. Write world_bible.md or era_brief.md (with source ledger) or setting_sheet.md, print the summary block, and stop.
world_bible.md (FAN/SFI)
Frame: {what differs from the real world, one page max}
Triad: SOURCE {..} | COST {..} | LIMIT {..}  [LOCKED]
Geography: {locations the plot visits, travel times}
Cultures: {name: livelihood, values, authority, celebration, one internal disagreement}
History line: {date: event pressing on the present} ...
invented_terms.md: {term | meaning | part of speech | first ch}
era_brief.md (HIS)  Period: {..}  Sources: {ledger refs}
Material culture: dress, food, tools, money, transport, communication
Speech register: {..}   Law and authority: {..}
Anachronism watchlist (20): {..}   Fixed real dates: {..}
Type Proceed
## RUN 6: PHASE 4, BEAT SHEET AND CHAPTER BLUEPRINT
Step 1. Lay the fifteen Master Grid beats (framework Appendix A) onto numbered chapters using the locked structure; add the overlay beat sheet where one exists (ROMBEAT, MYSBEAT). Verify every beat lands inside its percentage window at the chapter's projected word position.
Step 2. Write one brief per chapter: viewpoint, location, story day, goal, turn, beat(s) carried, opener mode by rotation (A action, D dialogue, S setting, I interior), word target, image slots if any.
Step 3. Place any prologue (earned scene, under 2,000 words, Chekhov plant) and any epilogue (OV-ROM: bonus HEA epilogue is the default) on the Beat Sheet per framework 5.8; UFFV-DUAL builds both lines on the Appendix F grid. Then place subplot mini-arcs (launch, complication, resolution) on named chapters; date the Timeline Ledger skeleton; initialize image_manifest.md and emit cowork_watcher.md if any slot is planned.
Step 4. Print the beat map and the first five chapter briefs as a sample, write beat_sheet.md and chapter_blueprint.md, and stop.
beat_sheet.md
{Beat # | name | target % | assigned ch | one-line content}
chapter_blueprint.md
Ch {NN} | POV {..} | {location} | Day {..} | Goal {..} | Turn {..}
        | Beats {..} | Opener {A|D|S|I} | Words {target} | Slots {none|IMG-XX}
timeline_ledger.md (skeleton): Ch | story day/date | span | elapsed | season
Subplots: {S1 launch ch, complication ch, resolution ch} ...
Type Proceed
## RUN 7: PHASE 5, THE CHAPTER LOOP
Run this block once per chapter, in order, without skipping. The loop is the production heart; its discipline is the book's quality.
Step 1. Read the chapter brief and the CURRENT ledgers (continuity, timeline, arc) and the Chekhov Registry. Never draft from memory of previous chapters.
Step 2. Draft the chapter: open on the assigned mode with a hook; ground with two senses in the first paragraph from the setting's sensory signatures; hold one viewpoint; compose one to three scene or sequel units; land the brief's turn; close with the overlay's forward pressure.
Step 3. Run the fifteen-point self-edit (framework 11.3) and print it as a PASS/FLAG line per point. Fix every FLAG before proceeding; re-run the flagged points.
Step 4. Update the ledgers: continuity entries created or changed; timeline row; arc position per viewpoint; Chekhov plants and payoffs; invented terms; the image manifest for any slot placed.
Step 5. Merge the chapter into the rolling DOCX via uapf-manuscript-builder; obtain the versioned read-only chapter preview PDF from uapf-chapter-format-auditor.
Step 6. Log the chapter tension score (1 to 5) to tension_map.md. Emit cowork_generate_chNN.md if the chapter carries slots. Compute the governor line (every fifth gate: add the next-beat landing projection; inside beat 14 the per-chapter minimum is waived). Update run_state.md. Print the gate block and stop.
PHASE 5 GATE | CHAPTER {NN}/{N}: {chapter label}
Self-edit: 1 PASS 2 PASS 3 PASS 4 PASS 5 PASS 6 PASS 7 PASS 8 PASS
           9 PASS 10 PASS 11 PASS 12 PASS 13 PASS 14 PASS 15 PASS
Ledgers updated: continuity {+n} | timeline row | arc {..} | chekhov {+p/+f}
Preview: {filename_vX.pdf} (read-only)
Cowork: {none | cowork_generate_ch{NN}.md emitted}
Tension: {n}/5 -> tension_map.md
Governor: ch words {x} (band {a}-{b}) | total {t}/{T} ({pct} percent)
          projection {P} ({+/-d} percent) | beat proj (5th gates): {beat n at pct}
          status {GREEN|AMBER|HALT}
Em dash scan: ZERO | Rating check: {CLEAN HELD | MAINSTREAM WITHIN DECLARATIONS}
Type Proceed
Halt handling. On HALT (two consecutive out-of-band chapters or projected drift beyond ten percent): stop drafting, print the rebalancing options (merge chapters, split chapters, retarget bands), and wait for the operator's choice before the next chapter.
## RUN 8: PHASE 6, WHOLE-BOOK QA
Step 1. Run the passes of framework Section 12 in order: twelve core, Pass 13 for FMT-SERIAL, Pass 14 for FMT-SHORT. For each pass, print one line: pass number, name, GREEN or the defect count.
Step 2. Log every defect in qa_report.md in the standard row format and route fixes through the Correction Protocol (RUN 14). After fixes, re-run the affected passes and then Pass 12.
Step 3. Print the QA summary block and stop only when every applicable pass is GREEN.
qa_report.md defect row:
QA-{pass}-{nn} | Ch {x} | {finding in one line} | {fix applied} | {re-run: GREEN}
PHASE 6 GATE | WHOLE-BOOK QA
P1 Structure GREEN  P2 Arcs GREEN  P3 Continuity GREEN  P4 Timeline GREEN
P5 Chekhov GREEN   P6 FairPlay {GREEN|N/A}  P7 Ending GREEN  P8 Escalation {GREEN|N/A}
P9 Prose GREEN     P10 Rating GREEN  P11 Mechanics GREEN  P12 Budget GREEN
P13 Series {GREEN|N/A}  P14 Collection {GREEN|N/A}
Defects found {n} | corrected {n} | open 0
Type Proceed
## RUN 9: PHASES 7 AND 8, MATTER AND FORMATTING
Step 1. Assemble front and back matter per framework 13.4 and 13.5 for the overlay: check the TOC rule (only where chapter titles are ON), the Author's Note mandate (HIS), the glossary trigger (invented terms above fifteen), Also By, the series preview chapter, and book club questions where flagged.
Step 2. Execute interior typography per framework Section 13 through uapf-formatting-engine; run the whole-book format audit; produce the print PDF and EPUB masters; update the page estimate and feed spine width forward.
Step 3. Print the gate block (matter checklist plus master file names and page count) and stop.
PHASE 7-8 GATE | MATTER AND FORMATTING
Front: half title, title, copyright, {dedication}, {epigraph}, {map}, {TOC on/off}
Back: {authors note}, {glossary n terms}, {acks}, about the author, also by,
      {series preview}, {book club questions}
Interior: trim {5x8|6x9} | body {font size} | gutter {in} | pages {est}
Masters: {title}_print.pdf | {title}.epub
Type Proceed
## RUN 10: PHASE 9, COVER (UDCF HANDOFF)
Step 1. Compose the handoff block for uapf-cover-aplus-system: title, subtitle or series line, pen name, overlay cover direction (framework Section 4), five theme bullets skimmed from the finished manuscript, and the palette window state (the last four base colors used on the imprint).
Step 2. Run the UDCF pipeline to three candidates (A, B, C); verify every catalogue cover law before presenting; assemble the wrap for the selected candidate with the Phase 8 spine width.
PHASE 9 HANDOFF
Title: {..} | Series line: {..} | Pen name: {..}
Overlay direction: {one line from Section 4}
Themes: {1} {2} {3} {4} {5}
Palette window (last 4, from register Base Color column or covers_ledger.md):
  {c1, c2, c3, c4} -> excluded for base
Laws verified: photorealistic | no icons/badges | no selling points |
               no violence/blood | window rule
Candidates: A {..} B {..} C {..}  ->  operator selects
Type Proceed
## RUN 11: PHASE 10, METADATA AND KDP PACK
Step 1. Build the blurb by the formula (framework 17.2) as two variants, A and B, on different hook angles; each 120 to 170 words, in the overlay's register, em dash free, nothing spoiled past forty percent. The operator selects one.
Step 2. Fill the seven keyword slots (17.3) and pass every slot through the trademark screen. Select BISAC primary and secondary from the 17.4 map, adding Clean and Wholesome placements only where the title is rated Clean. Compile the AI-content declaration (17.7: text, images, cover, each marked). Recommend the price bands.
Step 3. Write metadata_pack.md and the KDP Upload Sheet row; print both; stop.
metadata_pack.md
Blurb A ({wc} words): {full text}
Blurb B ({wc} words): {full text}
Selected: {A|B (operator)}
Keywords: 1 {subgenre} 2 {trope} 3 {mood/pace} 4 {setting}
          5 {audience per rating} 6 {comparable, generic} 7 {format/series}
TM screen: {PASS | reframed: slot n}
BISAC: {primary code + label} | {secondary code + label}
Age range: {n/a | 12-18 (YA)}
AI declaration: text {AI-generated|AI-assisted} | images {..} | cover {..}
Pricing: ebook {x.99} band | paperback {cost + margin} by {pages} pages
KDP Upload Sheet row: {title | subtitle | series | author | 7 keywords |
  categories | language | trim | pages | prices per marketplace |
  AI declaration}
Type Proceed
## RUN 12: PHASE 11, RELEASE QC AND BOOK REGISTER
Step 1. Hand the full package to uapf-release-qc for independent validation: reader promise re-verified against the overlay ending law, regression checks, print and EPUB preflight, archives with checksums.
Step 2. Emit cowork_image_task.md if any image slots remain unfilled. Append the Book Register record (including the Cover Base Color where the column exists, else write covers_ledger.md); if the register is not uploaded, print the row and the upload reminder.
PHASE 11 GATE | RELEASE QC
Release QC: {GREEN | defects -> RUN 14}
Archive: {title}_v1.zip | checksums logged | AI disclosure record archived
Register row: {YYYY-MM-DD} | {Title} | {Pen Name} | Fiction: {overlay name}
              | UFFV 1.1 ({OV-code}) | {Imprint} | Base color: {..}
{Register appended | REGISTER NOT UPLOADED: append on next upload}
RUN COMPLETE.
Type Proceed
## RUN 13: STANDING OUTPUT FORMAT
Print this block at every significant transition (phase completion, correction acceptance, resumption of a paused run):
STATE | {title} | {OV-code}+{mod} | {FMT} | rating {Clean|Mainstream}
Goal: {current phase objective}
Locks: structure {..} | POV/tense {..} | budget {T} words / {N} ch
Skills: {invoked this phase}
Gates: passed {list} | pending {list} | RETEST {list or none}
Next action: {one line}
Artifacts: {current file list}
Preview: {latest chapter preview file} | Corrections: {open n}
Governor: {line}
## RUN 14: CORRECTION PROTOCOL RUNTIME
Step 1. Receive the correction; restate its exact scope (artifact, chapters, lines, ledgers) in one line and list every dependent gate that becomes RETEST REQUIRED before touching anything.
Step 2. Apply the correction to the rolling DOCX and every touched ledger; cascade continuity fixes to every later chapter that used the corrected fact.
Step 3. Re-run the affected chapter self-edits or QA passes to green; produce fresh preview PDFs for corrected chapters; print the correction block; the run resumes only at the operator's Type Proceed.
CORRECTION | scope: {..}
RETEST REQUIRED: {gates}
Applied: {chapters/ledgers touched}
Cascade: {later chapters re-audited}
Re-run: {self-edit points | QA passes} -> GREEN
Previews: {files}
Type Proceed
## RUN 15: RESUME RUNTIME
Step 1. On any resumption of a paused run: load run_state.md, every ledger, the gate register, the tension map, and the latest rolling DOCX. Never resume from conversation memory (framework 19.3).
Step 2. Print the Standing Output block (RUN 13) from the loaded state and continue at the recorded next permitted action.
run_state.md
Phase: {n} | Next action: {one line}
Gates: {phase: PASSED|PENDING|RETEST} ...
Governor: {last line} | Tension map: through ch {n}
Artifacts: {file list} | Rolling DOCX: {filename} | Previews: {latest}
Open corrections: {none | list}
Updated: {gate stamp}
## RUN 16: REFERENCE CARDS
16.1 Overlay Quick Cards

[TABLE]
Code | Structure | Novel band | Chapters | Ending law keyword
OV-ROM | ROMBEAT on 3-Act | 55,000-80,000 | 24-32 | Committed and hopeful
OV-THR | 3ACT fast | 70,000-90,000 | 35-50 | Threat resolved
OV-MYS | MYSBEAT on 3-Act | 65,000-85,000 | 26-34 | Solved fairly
OV-FAN | HJ twelve stage | 90,000-120,000 | 28-38 | Quest resolved, cost paid
OV-SFI | 3ACT or HJ | 80,000-110,000 | 26-36 | What If answered
OV-HOR | 3ACT escalation | 65,000-85,000 | 26-34 | Dread released at cost
OV-LIT | 3ACT loose or KTK | 70,000-100,000 | 18-28 | Earned recognition
OV-HIS | 3ACT or DUAL | 85,000-115,000 | 26-36 | True to period
OV-YA | Modifier engine | 55,000-75,000 | 24-32 | Hopeful and earned
OV-ACT | HJ or 3ACT fast | 65,000-85,000 | 30-42 | Objective earned
OV-WFC | 3ACT or DUAL | 70,000-90,000 | 24-32 | Emotionally true
OV-FTH | 3ACT | 60,000-80,000 | 22-30 | Hope earned
[/TABLE]

16.2 Opener Rotation Codes
A: Action in motion. D: Dialogue mid-exchange. S: Setting through the senses. I: Interior thought or voice. No two consecutive chapters share a code; no code exceeds forty percent of the book.
16.3 Filter Word Watchlist
saw, heard, felt, noticed, realized, watched, seemed, wondered, thought, knew, could see, began to, started to. Target: fewer than three filter constructions per thousand words outside deliberate OV-LIT interiority.
16.4 The Cliche and Stock Phrase Blacklist
A chapter-gate defect on any hit. Replace from the setting's own sensory signatures.
a breath she did not know she was holding | heart pounded like a drum
heart hammered in his chest | time stood still | time slowed to a crawl
piercing {color} eyes | eyes like pools | steely gaze | raven hair
cascading locks | deafening silence | blood ran cold | cold sweat
every fiber of her being | heart skipped a beat | released a breath
butterflies in her stomach | chills ran down her spine | a single tear
heart in her throat | white as a sheet | jaw dropped | eyes widened in shock
the air was thick with tension | cut the tension with a knife
her world came crashing down | against all odds | in the nick of time
a wave of relief washed over | heaved a sigh of relief | needless to say
little did she know | shattered into a million pieces | darkness consumed
sleep claimed her | her mind raced | thoughts swirled | weight of the world
crystal clear | dead of night | bolt upright | blinked in confusion
swallowed hard | knuckles turned white | storm of emotions
rollercoaster of emotions | let out a breath he had been holding
16.5 Casting Caps
Under 60,000 words: 1-2 viewpoints, 4-6 major, 18 named. 60,000-90,000: up to 3 viewpoints, 5-8 major, 25 named. 90,000-120,000: up to 4 viewpoints (5 above 100,000 in FAN, SFI, HIS), 6-10 major, 35 named.
## RUN 17: COWORK FILE TEMPLATES (FICTION EDITION)
17.1 cowork_watcher.md (paste once at the configuration gate)
WATCHER | {Book Title} | UFFV 1.1
Watch folder: {book folder path}
Expect files named exactly: IMG-01.png, IMG-02.png, ...
Style: originally illustrated map style (fiction interior standard);
       full slot list and per-slot prompts arrive per chapter gate.
On file arrival: confirm name matches manifest, hold for insertion pass.
17.2 cowork_generate_chNN.md (per chapter gate carrying slots)
GENERATE | Chapter {NN} | slots: {IMG-XX, ...}
[IMG-XX] {slot title}
Prompt (paste into Flow, English, self-contained):
{content-derived prompt drawn from the drafted chapter: subject, style,
 composition, labels if a map, palette, aspect}
Save as: IMG-XX.png into the watch folder.
17.3 cowork_image_task.md (final delivery)
INSERTION PASS | {Book Title}
For each row in image_manifest.md:
  find [IMG-XX] placeholder in the rolling DOCX,
  insert IMG-XX.png at slot width (maps: full text width),
  remove the placeholder line, caption per manifest.
Report: slots filled {n}/{N}; missing files listed by name.
End of fiction-prompt. Governed by fiction-framework (UFFV 1.1). Embed both verbatim in pegasus-orchestrator.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
