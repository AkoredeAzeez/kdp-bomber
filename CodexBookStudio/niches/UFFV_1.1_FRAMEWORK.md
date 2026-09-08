# UFFV 1.1 MASTER FRAMEWORK (governing)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

> Authoritative UFFV 1.1 source, embedded verbatim. The parent
> SKILL.md operationalizes this; on any conflict this document governs,
> above it the operator's live instructions govern.

PEGASUS PRESS
UNIVERSAL FICTION FRAMEWORK
UFFV 1.1
Master Framework Document (governing)
Twelve Sub-Genre Overlays, Four Format Modifiers, Thirty Critical Rules
Status: AUTHORITATIVE upon operator approval. Companion document: uffv-prompt (executable pipeline).
August 2026
TABLE OF CONTENTS
## SECTION 0: IDENTITY, SCOPE AND GOVERNANCE
0.1 Identity
This document is the Universal Fiction Framework, Version 1.1 (UFFV 1.1). It is the single governing standard for every work of narrative fiction produced under Pegasus Press and all of its imprints. It joins the framework registry alongside UCGF v2.7 (cookbooks), UTGF v3.0 (travel), UWGF v1.7 (workbooks), USGPF v2.9 (study guides), UTF 1.0 (textbooks), CBF 2.0 (children), AIRF 2.0 and 2.1 (nonfiction categories), and is executed through the pegasus-orchestrator with delegation to the uapf specialist skills.
0.2 Scope
UFFV 1.1 governs all prose fiction intended for readers aged thirteen and above: novels, novellas, short story collections, and serialized series in every fiction genre. Fiction for children aged zero to twelve remains under CBF 2.0 and is out of scope here. Narrative nonfiction, true crime scripts, and all nonfiction categories remain under their existing frameworks.
0.3 The Two-Document Convention
UFFV ships as two verbatim documents in the orchestrator registry: fiction-framework (this Master Framework, which governs) and fiction-prompt (the executable pipeline). Wherever the two conflict, this Master Framework wins. Wherever this framework conflicts with the operator's live instructions or the global rules file, the precedence order in 0.4 wins.
0.4 Precedence (strict)
1. The operator's live instructions in the current conversation.
2. Operator standing corrections in references/global-rules.md (gate wording, pen name format, image manifest workflow, em dash ban, Book Register).
3. This document, fiction-framework (UFFV 1.1 Master Framework).
4. fiction-prompt (the executable pipeline).
5. Specialist skill defaults (uapf-manuscript-builder, uapf-chapter-format-auditor, uapf-formatting-engine, uapf-cover-aplus-system, uapf-research-compliance, uapf-release-qc).
0.5 Reader Promise Doctrine
Every fiction genre is a promise made to a reader before page one. Romance promises an emotionally satisfying committed ending. Mystery promises a fair puzzle honestly solved. Thriller promises escalating danger and release. Fantasy promises a consistent second world. This framework exists to guarantee that every Pegasus Press title keeps its genre promise completely, cleanly, and on budget. Breaking the reader promise is a release-blocking defect at QA.
0.6 Design Lineage
UFFV 1.1 is built on the six universal narrative elements (character, conflict, narrative mode, plot, setting, theme), the documented structure canon (three-act structure, Freytag, the seventeen-stage monomyth condensed to a working twelve, Kishotenketsu, dual timeline), industry word count bands per genre, and the per-genre reader contracts recorded in the Fiction Research Master Document of August 2026. All of it is operationalized here as gates, ledgers, governors, and laws in the established Pegasus Press style.
0.7 Change Log from 1.0
Series runtime added: Book 2 and later load the Series Bible and prior-book ledger snapshots at Phase 0; QA Pass 13 audits cross-book continuity (14.5, 12).
Resume Protocol added: every gate updates run_state.md; paused runs resume from artifacts, never from conversation memory (19.3).
AI disclosure made explicit law: the KDP AI-content declaration is compiled at Phase 10, verified and archived at Phase 11 (Rule 29, 17.7).
Prose tools localized: non-English titles generate language-equivalent filter and blacklist sets at Phase 1 (8.10).
Modifier stack budget resolution defined, including the romantasy case (3.1).
The Dual Timeline Grid specified in full (Appendix F).
Collection QA defined: per-story promise checks plus Pass 14 Collection Unity for FMT-SHORT (12).
Prologue and Epilogue Law added; the bonus HEA epilogue is the OV-ROM house default (5.8, Appendix B).
Tension map instituted: a 1 to 5 score logged per chapter powers QA Pass 8 with data (11.4, 12).
Cover base color memory instituted: register column or covers_ledger.md feeds the five-cover window (Rule 7, 16).
Beat-drift projection added to the governor with a climax pacing exemption (3.3, 11.5).
Metadata polish: blurbs ship as A and B variants; a review request page joins standard back matter (17.2, 13.5).
## SECTION 1: THE THIRTY CRITICAL RULES (GLOBAL LAWS)
The following rules are absolute. They apply to every overlay, every format, every imprint, and every marketplace. A violation of any Critical Rule is a release-blocking defect. Rules 2 to 10 restate catalogue-wide Pegasus Press law; Rule 1 and Rules 11 to 30 are fiction-specific.
Rule 1. Content Rating Law. Every title declares a content rating at Phase 0, UFFV-Clean or UFFV-Mainstream, recorded in the Story Spec. The declared rating binds every chapter, the metadata pack, and QA Pass 10 per Section 9. Where no rating is stated, Mainstream is the default.
Rule 2. Em Dash Ban. No em dashes and no en dashes appear anywhere in any deliverable: manuscript, front matter, back matter, metadata, blurb, image prompts, or cover text. Substitutes: comma, colon, parentheses, period, or a rebuilt sentence. Numeric ranges use the hyphen (55,000-80,000) or the word to.
Rule 3. Pen Name Law. Author names are sourced from fakenamegenerator.com in First Name, Initial(s). Surname format, screened against real living authors before lock, and recorded in the Story Spec.
Rule 4. Gate Line Law. Every production phase closes with exactly the line Type Proceed. No phase advances without it.
Rule 5. Rolling DOCX Law. The manuscript is built as one rolling DOCX that grows chapter by chapter. Separate editable chapter files are never exposed unless the operator explicitly requests them. Chapter previews ship as versioned read-only PDFs.
Rule 6. Image Manifest Law. Every image slot ships as an [IMG-XX] placeholder in the DOCX plus a matching row in image_manifest.md, with cowork_watcher.md at the configuration gate, cowork_generate_chNN.md at each chapter gate that contains slots, and cowork_image_task.md at final delivery. Prompts are content-derived, self-contained, always in English, and genre-matched. Fiction image policy is defined in Section 15.
Rule 7. Book Register Law. At final delivery, a record is appended to Pegasus_Press_Book_Register.xlsx with Date of Generation, Book Title, Author Name, Category, Framework (UFFV 1.1 plus overlay code), Imprint, and the Cover Base Color where the register carries that column (Section 16). If the register is not uploaded, the record row is output with a reminder to upload.
Rule 8. Language Law. The title's language determines the manuscript language. Chat output stays in English. All internal artifacts (bibles, ledgers, manifests) stay in English regardless of manuscript language.
Rule 9. State Discipline Law. No external operation is ever claimed unless it actually occurred. Honest states: NOT RUN, PENDING, UNVERIFIED, READY FOR IMPORT. Trademark and real-person screens require live web research or are reported NOT RUN.
Rule 10. Catalogue Uniqueness Law. No two Pegasus Press fiction titles may share the same premise, the same protagonist name and occupation pairing, or the same title within any marketplace. The uniqueness check runs at Phase 0 against the Book Register.
Rule 11. Reader Promise Law. The matched overlay's mandatory elements and ending law are contractual. Romance ends committed and hopeful. Mystery is solved fairly. Thriller resolves the threat. The promise is verified at QA Pass 1 and again at Release QC.
Rule 12. Structure Lock Law. One structure from the Structure Library is selected at Phase 1 and locked. The Beat Sheet is built on it at Phase 4 and every chapter is drafted against it. Structure may only change through the Correction Protocol, which invalidates all downstream gates.
Rule 13. POV and Tense Lock Law. Point of view type, viewpoint character list, and tense are locked at Phase 1. Head-hopping (shifting viewpoint inside a scene) is banned. A viewpoint change requires a scene break or chapter break.
Rule 14. Word Budget Governor. Total word count, chapter count, and per-chapter band are locked at Phase 1 from the overlay table with a tolerance of plus or minus ten percent. Drift beyond tolerance halts the chapter loop for rebalancing.
Rule 15. Continuity Ledger Law. A Continuity Ledger is created at Phase 2 and updated after every chapter: character knowledge states, physical anchors, injuries, objects, locations, world rules invoked, and open promises. Every chapter is drafted against the current ledger, never against memory.
Rule 16. Timeline Integrity Law. A Timeline Ledger records each chapter's calendar position, time span, and elapsed time. Seasons, travel durations, healing times, and day-night cycles must remain plausible. Verified at QA Pass 4.
Rule 17. Chekhov Law. Every significant planted element (object, skill, secret, foreshadow) is logged in the Chekhov Registry with its planting chapter and must either fire by the climax or be removed. Unfired plants and unplanted payoffs are both defects.
Rule 18. Fair Play Law. In the Mystery overlay, every clue the detective uses is shown to the reader when the detective encounters it. The culprit appears within the first thirty percent. No solutions by coincidence, unknown science, or information withheld from the reader.
Rule 19. Escalation Law. In Thriller, Horror, and Action overlays, every act raises stakes above the last. The midpoint reversal makes retreat impossible. A tension audit at QA confirms no sagging middle.
Rule 20. Character Bible Law. No drafting begins before the Character Bible gate passes: protagonist sheet, antagonist sheet, supporting cast register within the casting cap, naming law compliance, and three logged voice markers per major character.
Rule 21. Antagonist Motive Law. The antagonist believes they are right. Pure evil without comprehensible motive is banned outside clearly mythic Fantasy framing, and even there the opposing force must have logic.
Rule 22. Anti-Duplication Variation Engine. No repeated scene shapes within five chapters, no distinctive word repeated within one hundred fifty words, no simile or metaphor reused in the book, no two consecutive chapters opening in the same mode. The echo scan runs at every chapter gate and again whole-book.
Rule 23. Hook Law. Every chapter opens with a hook (action, question, imbalance, or voice) and closes with forward pressure appropriate to the overlay's pacing profile. Thriller chapter endings are mandatory hooks; Literary endings may resolve on image or insight.
Rule 24. Dialogue Law. The eight dialogue laws in Section 8.2 govern all speech: said as default, no adverb stacking, subtext in conflict scenes, no exposition dialogue, rhythm-based dialect, ellipsis for trailing speech, rating-consistent language, and logged voice markers.
Rule 25. Show Priority Law. Dramatize what matters; summarize transitions. Emotion is rendered through action, sensation, and speech before it is named. Filter words (saw, felt, heard, realized, noticed, seemed) are minimized per Section 8.3.
Rule 26. Research Gate Law. Historical fiction and any real-world technical, medical, legal, or geographic content pass through uapf-research-compliance before drafting the affected chapters. Claims about real history follow the source ledger discipline; anachronisms are QA defects.
Rule 27. No Real Persons Law. No living real person appears as a character. Historical public figures older than seventy years deceased may appear in Historical fiction within the dignity limits of Section 8.7 and the research gate. Character names are screened against famous living persons.
Rule 28. Series Integrity Law. Series titles maintain a Series Bible. Every series book resolves its own central conflict while advancing the series thread. Hard cliffhangers that withhold the book's own promised ending are banned; soft forward hooks are permitted per overlay.
Rule 29. Clean Metadata Law. Blurbs spoil nothing past the forty percent mark, contain no other author's name and no trademarked property, keep the em dash ban, and follow the Blurb Formula. Keywords pass the trademark screen. The KDP AI-content declaration is completed truthfully per Section 17.7.
Rule 30. Correction Scope Law. Corrections follow the Correction Protocol exactly as scoped, never advance a gate on their own, and mark every dependent gate RETEST REQUIRED.
## SECTION 2: DETECTION AND ROUTING
2.1 Fiction Detection Triggers
The orchestrator routes a title to UFFV 1.1 when any of the following is true: the operator names UFFV or an overlay code; the title or brief describes an invented story, characters, or plot; the request uses the words novel, novella, fiction, story, saga, or a genre name from the overlay registry in a storytelling sense; or the concept is a narrative that is not fact-bound. Explicit operator instruction always wins.
2.2 Boundary Rules
CBF 2.0 boundary: intended readers twelve and under, or picture-led narrative, routes to CBF 2.0. UFFV takes thirteen and above.
Nonfiction boundary: true stories told as fact (memoir style, true crime, history) route to their nonfiction frameworks. A fictionalized story inspired by real events stays in UFFV under the Historical overlay with the research gate.
Humor gift boundary: novelty gift books route to UHSGF when embedded; narrative comic fiction stays in UFFV with the comedic register noted in the Story Spec.
2.3 Overlay Selection
Exactly one primary overlay is selected per title. Where two overlays genuinely blend (romantic suspense, historical mystery, science fantasy), the primary overlay is the one whose ending law governs the climax, and the secondary overlay is recorded as a modifier whose applicable laws also run at QA. If detection finds two comparable primaries, ask the operator ONE question offering exactly those two, then proceed.
2.4 Age Band Routing
Default band is Adult. The YA overlay activates when the protagonist is fourteen to eighteen and the concerns are coming of age. YA stacks its additional gates from Section 8.9 on top of whichever genre furnishes the plot engine (a YA fantasy runs OV-YA primary with OV-FAN modifier).
2.5 Format Detection
Formats: FMT-NOVEL (default), FMT-NOVELLA, FMT-SHORT (a themed collection), FMT-SERIAL (a planned series). Format modifies budgets and pipeline artifacts per Section 3.3 and Section 13 and never changes the overlay's content laws.
## SECTION 3: OVERLAY REGISTRY (SUMMARY)
Twelve overlays cover the commercial fiction catalogue. Each overlay's full specification follows in Section 4 blocks OV-1 to OV-12. This summary table is the routing reference.

[TABLE]
Code | Overlay | Reader promise | Default structure | Word band (novel)
OV-ROM | Romance | Committed, hopeful ending for the central couple | UFFV-ROMBEAT on 3-Act | 55,000-80,000
OV-THR | Thriller and Suspense | Escalating danger, threat resolved | UFFV-3ACT fast profile | 70,000-90,000
OV-MYS | Mystery and Crime | A fair puzzle honestly solved | UFFV-MYSBEAT on 3-Act | 65,000-85,000
OV-FAN | Fantasy | A consistent second world, quest fulfilled | UFFV-HJ twelve stage | 90,000-120,000
OV-SFI | Science Fiction | A rigorous What If explored to consequence | UFFV-3ACT or UFFV-HJ | 80,000-110,000
OV-HOR | Horror and Supernatural Suspense | Dread built and released, threat resolved | UFFV-3ACT escalation profile | 65,000-85,000
OV-LIT | Literary and Book Club | Depth of character, language, and theme | UFFV-3ACT loose or UFFV-KTK | 70,000-100,000
OV-HIS | Historical Fiction | A vivid, accurate past honestly rendered | UFFV-3ACT or UFFV-DUAL | 85,000-115,000
OV-YA | Young Adult | Coming of age, hopeful and true | Genre engine plus YA gates | 55,000-75,000
OV-ACT | Action and Adventure | Momentum, capability, victory earned | UFFV-HJ or 3-Act fast | 65,000-85,000
OV-WFC | Women's Fiction and Family Drama | Emotional truth, relationships transformed | UFFV-3ACT or UFFV-DUAL | 70,000-90,000
OV-FTH | Faith and Inspirational | Faith lived with dignity through story | UFFV-3ACT | 60,000-80,000
[/TABLE]

3.1 Modifier Stacking
A title carries one primary overlay and at most one modifier overlay. Both content law sets apply; the primary's ending law and pacing profile govern. Examples: romantic suspense is OV-ROM primary with OV-THR modifier; historical mystery is OV-MYS primary with OV-HIS modifier (research gate active); science fantasy is OV-FAN primary with OV-SFI modifier.
Stack budget resolution. When the two overlays carry different word bands, the stack resolves to the longer band unless the operator sets otherwise; the primary's chapter-length band applies within the resolved total, and the Chapter Budget Governor recomputes chapter count from that pair. A world-bearing modifier (FAN, SFI, HIS) pulls its Phase 3 gate into the pipeline even as a modifier. Worked case, romantasy: OV-ROM primary with OV-FAN modifier resolves to 90,000-120,000 words, ROMBEAT beats mapped onto the longer grid, World Bible mandatory, ROM chapter lengths inside the FAN total.
3.2 Word Bands by Format

[TABLE]
Format | Words | Chapters | Notes
FMT-NOVEL | Per overlay table | Per overlay table | Default format
FMT-NOVELLA | 20,000-40,000 | 10-16 | Single plot line, subplot cap of one
FMT-SHORT | 40,000-60,000 total | 8-14 stories | Each story 2,500-7,000 words, one unifying theme; QA runs per story plus Pass 14
FMT-SERIAL | Per book: overlay table | Per book: overlay table | Series Bible mandatory, Section 13
[/TABLE]

3.3 Chapter Budget Governor
Chapter count equals target words divided by the overlay's midpoint chapter length, rounded to the overlay's chapter band. Per-chapter tolerance is plus or minus twenty percent of the band midpoint; whole-book tolerance is plus or minus ten percent of target words. The governor is checked at every chapter gate; two consecutive out-of-band chapters halt the loop for rebalancing before drafting continues.
Beat-drift projection. At every fifth chapter gate the governor also projects the landing position of the next Master Grid beat against its Appendix A window: drift beyond five percentage points is AMBER, beyond eight is HALT for rebalancing. Climax exemption. Within the climax sequence (beat 14), per-chapter minimum bands are waived so chapters may run short for pace; the whole-book tolerance still governs.
## SECTION 4: OVERLAY SPECIFICATIONS (FULL)
Each overlay specification is complete and self-contained. Fields: Definition, Mandatory Elements, Forbidden Elements, Ending Law, Structure, Budgets, POV and Tense Defaults, Pacing Profile, Approved Trope Menu, Content Notes, Image Policy, Cover Direction, Metadata Notes.
OV-1 / OV-ROM: ROMANCE
Definition. A story whose central plot is the growth of romantic love between two leads, in which both the main conflict and the climax arise from the relationship itself, ending in an emotionally satisfying committed resolution (the genre's core contract).
Mandatory Elements. Two leads with independent wants and wounds; a meet (or re-meet) by the ten percent mark; a believable barrier that is neither a trivial misunderstanding sustained past its natural life nor solvable by one honest conversation in chapter two; escalating emotional intimacy through conversation, shared trial, and sacrifice; a black moment near seventy-five to eighty percent; a truth-telling or grand gesture; a committed, hopeful ending (HEA or a firmly grounded HFN).
Forbidden Elements. Love triangles resolved by humiliation; infidelity by a lead inside the central relationship; a lead redeemed from cruelty by love alone; endings in ambiguity or separation; content beyond the title's declared rating.
Ending Law. Committed and hopeful, on the page, with the emotional payoff dramatized in scene (not summarized).
Structure. UFFV-ROMBEAT (Appendix B) laid over the three-act grid. Dual-POV alternation between the two leads is the house default. A bonus HEA epilogue (1,000-2,500 words, set after the commitment) is the house default; omit only by operator order.
Budgets. Novel 55,000-80,000 words; 24-32 chapters; 2,000-3,000 words per chapter. Novella 20,000-40,000.
POV and Tense. Third limited, alternating between the two leads by chapter; past tense. First person single is permitted for category-style titles; declare at Phase 1.
Pacing Profile. Moderate with timed emotional beats. Every chapter contains at least one relationship movement (closer, farther, or complicated). Chapter endings favor emotional pressure over physical danger.
Approved Trope Menu. Second chance, forced proximity, enemies to allies to love, best friend's sibling, fake relationship, marriage of convenience moving to real love, small town return, guardianship of a child, rival family businesses, workplace rivals, love rediscovered in later life.
Content Notes. Heat level is declared at Phase 1 within the title's content rating: Clean titles are closed-door throughout; Mainstream titles select a heat ceiling and hold it consistently. The HEA contract is rating-independent.
Image Policy. Interior images: none. Chapter ornaments optional per Section 15.
Cover Direction. Photorealistic couple at warm middle distance, or a single symbolic object (letters, a ring box, a garden gate). Warm palette. All UDCF hard rules apply.
Metadata Notes. BISAC FIC027050 Contemporary or FIC027110 Historical variants; add FIC042040 Clean and Wholesome as secondary where the title is rated Clean. Keyword slots emphasize the active trope and the declared heat lane.
OV-2 / OV-THR: THRILLER AND SUSPENSE
Definition. A story defined by the moods it produces: suspense, anticipation, and anxiety, in which a protagonist faces imminent, escalating harm from a capable opposing force and must defeat it. Often villain-driven: the antagonist's plan structures the plot.
Mandatory Elements. A threat with a clock; a capable antagonist whose plan is active before page one; escalating attempts and failures; a midpoint reversal that makes retreat impossible; at least two legitimate plot twists; a climax where the protagonist's earned capabilities defeat the threat; the threat fully resolved.
Forbidden Elements. Rescue by coincidence; a villain defeated by their own unforced stupidity; a final twist that invalidates the reader's entire experience.
Ending Law. Threat resolved, cost acknowledged, order restored. A soft forward hook is permitted for series.
Structure. UFFV-3ACT fast profile: shortest chapters in the catalogue, mandatory chapter-end hooks, twist placement at approximately thirty-five, sixty-five, and eighty-five percent.
Budgets. Novel 70,000-90,000 words; 35-50 chapters; 1,500-2,500 words per chapter.
POV and Tense. Third limited, up to three viewpoints (protagonist, one ally or investigator, and optionally limited antagonist interludes that conceal identity where the plot requires). Past tense default; present tense permitted by declaration.
Pacing Profile. Fast throughout. Scene-sequel ratio tilted to scene. No chapter without new pressure. Reflection is rationed to sequels of one page or less.
Approved Trope Menu. Ticking clock, wrong person accused, protected witness, conspiracy uncovered by an ordinary professional, cat and mouse, the mole, the vanished spouse or sibling, the inheritance with strings, the whistleblower.
Content Notes. Violence intensity follows the declared rating per Section 9.4: consequence over choreography either way, with on-page intensity at genre standard for Mainstream and restrained for Clean.
Image Policy. None.
Cover Direction. High-contrast atmospheric scene, isolated figure, cool palette, strong single light source. No blood, no weapons pointed at the viewer, per UDCF.
Metadata Notes. BISAC FIC031000 Suspense or FIC030000 Thrillers plus the specific lane (FIC031010 Espionage, FIC031080 Psychological, FIC031070 Legal). Keywords carry the lane and the clock.
OV-3 / OV-MYS: MYSTERY AND CRIME
Definition. A crime (usually a killing or a disappearance) is presented, investigated, and solved by logical deduction from clues the reader also sees. Lanes range from cozy (puzzle first, community rich, violence off page by genre convention) to procedural and hardboiled (grit and realism on page).
Mandatory Elements. The crime established by the ten percent mark (or before chapter one); an engaged investigator by twelve percent; a closed suspect pool of four to seven, each with motive, means, and opportunity; a minimum of three genuine clues and two to four red herrings, all logged in the Clue Grid (Appendix C); a false solution near seventy to seventy-five percent; the true reveal at eighty-five to ninety-two percent; a full explanation scene; a justice outcome.
Forbidden Elements. Everything the Fair Play Law bans: hidden clues, unknown poisons, solutions by accident, culprits introduced after thirty percent, supernatural solutions in a realist mystery, and the investigator concealing reasoning from the reader.
Ending Law. Solved fairly, culprit identified with the reader's own evidence, justice served.
Structure. UFFV-MYSBEAT (Appendix C) laid over the three-act grid.
Budgets. Novel 65,000-85,000 words; 26-34 chapters; 2,200-3,000 words per chapter.
POV and Tense. Single viewpoint with the investigator (first person or third limited); past tense. The reader never enters the culprit's head.
Pacing Profile. Steady with puzzle rhythm: interview, clue, reflection, complication. A second crime or sharp escalation is placed near fifty-five to sixty percent if momentum requires it.
Approved Trope Menu. Amateur sleuth with a day trade (bookshop, bakery, tailoring house, antiques stall), the retired detective drawn back, the locked room, the will reading, the festival crime, the small community where everyone holds one secret, the investigator's counterpart in the police, the cold case reopened.
Content Notes. The lane sets the floor: cozy keeps violence off page and language mild by genre convention regardless of rating; procedural and hardboiled lanes under a Mainstream rating may render the crime scene at genre-standard intensity. Victims are rendered with dignity per Section 9.6 in every lane.
Image Policy. None. An optional single map of the village or house is permitted for manor and village mysteries, per Section 15.
Cover Direction. Setting-forward scene with a single clue-object motif (a lantern, a key, an envelope). Warm-dark palette for cozy lanes. No blood.
Metadata Notes. BISAC FIC022000 Mystery and Detective plus lane (FIC022070 Cozy general and its craft or culinary variants where relevant, FIC022020 Women Sleuths, FIC022060 Historical with OV-HIS modifier, FIC022010 Police Procedural).
OV-4 / OV-FAN: FANTASY
Definition. A story with imaginative elements that need not obey real-world nature, set wholly or partly in a constructed second world, where a magic or wonder system operates by consistent internal rules.
Mandatory Elements. A World Bible passed at Phase 3; a magic or wonder system defined by the source, cost, and limit triad; a quest or need that only this protagonist can answer; a mentor or aid figure; thresholds, trials, and an ordeal; the boon brought home; a map slot if geography carries plot weight.
Forbidden Elements. Rule-breaking magic that solves the climax without established cost; invented cultures that are thin copies of real ones used disrespectfully; prophecy that removes protagonist agency.
Ending Law. Quest resolved, cost paid, world changed, protagonist transformed. Series may leave the wider war open while closing this book's quest.
Structure. UFFV-HJ, the twelve-stage working monomyth: Ordinary World, Call, Refusal, Mentor and Aid, First Threshold, Trials and Allies, Approach, Ordeal, Reward, The Road Back, Climax and Transformation, Return with the Boon.
Budgets. Novel 90,000-120,000 words; 28-38 chapters; 2,800-4,000 words per chapter. Debut ceiling 120,000 hard.
POV and Tense. Third limited, up to four viewpoints (five permitted only above 100,000 words); past tense.
Pacing Profile. Measured openings earn their length through wonder and pressure together: every worldbuilding paragraph must carry either character or plot freight. Set-piece rhythm: a major wonder or trial every three to four chapters.
Approved Trope Menu. The reluctant heir, the found family of companions, the sealed evil stirring, the academy of a craft, the artifact with a price, the border kingdom holding the line, the map with a blank region, the tournament, the oath and its cost, the dark lord with comprehensible logic.
Content Notes. Grimdark lanes require a Mainstream rating and declare their intensity at Phase 1; classic and cozy fantasy lanes sit naturally at Clean. The system triad and Rule 21 hold in every lane.
Image Policy. One illustrated map slot [IMG-01] standard; optional chapter-opening glyph set; nothing else by default. Section 15 governs.
Cover Direction. Photorealistic composite: epic landscape, or a figure with the artifact, painterly light within photorealism. No icon badges, no floating symbols.
Metadata Notes. BISAC FIC009020 Epic, FIC009100 Action and Adventure fantasy, FIC009120 Dragons and Mythical Creatures as fits. Glossary triggers per Section 13 when invented terms exceed fifteen.
OV-5 / OV-SFI: SCIENCE FICTION
Definition. A story built on one disciplined What If drawn from technology, science, or social systems, extrapolated to human consequence with internal plausibility.
Mandatory Elements. The What If stated in one sentence in the Story Spec; a world that has fully absorbed the premise (second-order consequences shown, not just the gadget); a protagonist whose personal stake embodies the theme; a cost of the technology or change dramatized; a climax where the premise, not luck, decides the outcome.
Forbidden Elements. Technology that changes capability mid-book without setup; info-dump chapters; societies with one job and one opinion; the premise abandoned for a generic chase in act three.
Ending Law. The What If answered through consequence. Bittersweet is permitted; nihilism is not.
Structure. UFFV-3ACT default; UFFV-HJ for voyage and first-contact shapes; UFFV-DUAL for generation and timeline stories.
Budgets. Novel 80,000-110,000 words; 26-36 chapters; 2,600-3,800 words per chapter.
POV and Tense. Third limited up to four viewpoints; past tense. A ship, station, or settlement ensemble may add one viewpoint above 95,000 words.
Pacing Profile. Front-load the premise inside a human problem within two chapters. Exposition budget: no more than one paragraph of explanation per scene, dramatized wherever possible.
Approved Trope Menu. First contact, the generation ship decision, the settlement that must choose, the inventor confronting the use of the invention, the archive that remembers, the long signal, the terraforming dilemma, the apprentice engineer, the last librarian of a failing station.
Content Notes. Dystopian and military lanes declare their intensity at Phase 1 under the rating; the exposition budget applies in every lane.
Image Policy. Optional single schematic or star map slot; otherwise none.
Cover Direction. Photorealistic vista: hull, horizon, station, or planetary scene, one human-scale element for stakes. Cool palettes rotated per the five-cover window rule.
Metadata Notes. BISAC FIC028010 Adventure, FIC028070 Space Exploration, FIC028100 Colonization and so forth by lane; keywords carry the What If in plain words.
OV-6 / OV-HOR: HORROR AND SUPERNATURAL SUSPENSE
Definition. A story engineered to produce dread and fear and then release them, through a threat natural or supernatural. The house default lane is dread-forward atmospheric horror; harder lanes are available under a Mainstream rating.
Mandatory Elements. A wrongness introduced by chapter two; an escalation ladder of manifestations, each larger than the last; a protagonist flaw the threat exploits; a rules-discovery thread (what it is, what it wants, what limits it); a confrontation the protagonist can only win by change or sacrifice.
Forbidden Elements. A threat that changes its own rules at the climax; scares that never cost anything; an ending where the threat simply wins without meaning or cost.
Ending Law. Dread released: the threat defeated, banished, or truthfully contained, at a visible cost. A final unsettling image is permitted.
Structure. UFFV-3ACT escalation profile with manifestation beats at ten, twenty-five, forty, fifty-five, seventy, and eighty-five percent.
Budgets. Novel 65,000-85,000 words; 26-34 chapters; 2,000-3,000 words per chapter.
POV and Tense. Single or dual third limited; past tense. Never the threat's viewpoint.
Pacing Profile. Alternating dread and reprieve; quiet chapters exist to be broken. In the atmospheric lane, what is heard and almost seen outweighs what is shown; harder lanes may show more under their declared intensity.
Approved Trope Menu. The inherited house with a sealed room, the lighthouse posting, the archive that should have stayed closed, the village that does not speak of the orchard, the night shift, the whisper that knows names, the guardian who forgot the rules, the entity bound by a bargain.
Content Notes. The lane and intensity are declared at Phase 1: atmospheric horror sits naturally at Clean; body horror, splatter-adjacent, and psychological-extreme lanes require Mainstream and hold their declared ceiling consistently. Cruelty to children on page is banned in every lane as house standard.
Image Policy. None.
Cover Direction. Atmosphere only: fog, doorway, treeline, a single lit window. No creatures rendered, no blood, per UDCF.
Metadata Notes. BISAC FIC015000 Horror general or FIC024000 Occult and Supernatural by lane, with keyword signaling matched to the declared intensity (atmospheric, gothic, extreme).
OV-7 / OV-LIT: LITERARY AND BOOK CLUB FICTION
Definition. Character-driven fiction whose payoff is depth: interior life, layered language, and theme, engineered for discussion. Plot exists and matters, but transformation is the promise.
Mandatory Elements. A protagonist with a rich interior life and a lie they believe; a central question the book keeps complicating; at least two mirrored characters who answer the question differently; recurring motif work (Leitwortstil logged in the Story Spec); a climax of recognition; an ending that lands the theme in image or act.
Forbidden Elements. Plotlessness (a book with no causal spine), misery without meaning, stylistic obscurity that hides rather than reveals, and endings of pure despair.
Ending Law. Earned recognition. Bittersweet and open textures are permitted; the theme must resolve even where the plot stays soft.
Structure. UFFV-3ACT loose profile or UFFV-KTK (introduction, development, turn, consequence) for quieter shapes; UFFV-DUAL for memory braids.
Budgets. Novel 70,000-100,000 words; 18-28 chapters; 3,000-5,000 words per chapter.
POV and Tense. First person or close third; past or present by declaration. One viewpoint default, three maximum.
Pacing Profile. Permission to linger, never to stall: every scene still turns on desire, resistance, and change, however quiet.
Approved Trope Menu. The return to the family house, the inheritance of an unfinished task, the friendship across a divide, the craft that carries a life (calligraphy, boatbuilding, orchard keeping), the letter found late, the parent understood too late, the town changed by one arrival.
Content Notes. The rating shapes register, not depth: difficult material is available in either rating, rendered by implication at Clean and directly at Mainstream where the story requires it.
Image Policy. None.
Cover Direction. Minimal symbolic photograph: one object, one light. Typography carries weight within UDCF rules.
Metadata Notes. BISAC FIC019000 Literary; book club guide of eight to twelve questions is a standard back matter option, flagged at Phase 7.
OV-8 / OV-HIS: HISTORICAL FICTION
Definition. An invented story set at least fifty years in the past, faithful to the period's manners, material culture, and constraints, written from research.
Mandatory Elements. The research gate passed before drafting (era brief, source ledger, anachronism watchlist); a setting rendered through period-true daily life; a plot that could only happen then and there; an Author's Note separating fact from invention; a timeline ledger reconciled to real dates where real events appear.
Forbidden Elements. Anachronistic speech, objects, and attitudes presented as period; living persons; deceased public figures within seventy years used as characters; real atrocities used as set dressing.
Ending Law. True to period and premise; hope is drawn honestly from the era's real possibilities.
Structure. UFFV-3ACT default; UFFV-DUAL for past and present braids (the present line then follows OV-WFC or OV-MYS law as detected).
Budgets. Novel 85,000-115,000 words; 26-36 chapters; 2,800-4,000 words per chapter.
POV and Tense. Third limited, up to three viewpoints; past tense strongly defaulted.
Pacing Profile. Immersion up front, then the era's constraints as pressure. Research is invisible: no paragraph exists to display a fact.
Approved Trope Menu. The scribe or clerk who sees too much, the trade caravan season, the physician in the plague year, the mapmaker at the frontier, the widow holding the workshop, the scholar and the manuscript, the siege winter, the emigration voyage.
Content Notes. Period accuracy governs content: the era's realities are rendered at the declared rating's intensity, and the Author's Note owns the line between fact and invention.
Image Policy. One era map slot standard; optional single period plate; per Section 15.
Cover Direction. Era-true photorealistic figure or scene; costume research feeds the prompt; palette rotation per the five-cover window.
Metadata Notes. BISAC FIC014000 general plus period lanes; the Author's Note is mandatory back matter and is itself QA-checked for accuracy.
OV-9 / OV-YA: YOUNG ADULT
Definition. Fiction whose protagonist is fourteen to eighteen and whose spine is coming of age: identity, belonging, first responsibility, and hope. OV-YA is a primary that borrows its plot engine from a modifier overlay.
Mandatory Elements. A teen protagonist with real agency (adults may help, never solve); a stake that is enormous at that age and treated as such; a found or repaired belonging; growth measurable between first and final chapter; hope in the ending.
Forbidden Elements. Everything in Section 9.7: explicit content in any rating, gratuitous harm on page, despairing endings, adult savior resolutions.
Ending Law. Hopeful and earned; the protagonist ends more capable and more connected than they began.
Structure. The modifier overlay's structure with YA proportion: faster openings, shorter chapters.
Budgets. Novel 55,000-75,000 words; 24-32 chapters; 1,800-2,800 words per chapter.
POV and Tense. First person or close third, single viewpoint default; past or present by declaration.
Pacing Profile. Immediate: inciting incident by eight percent, voice-forward chapters, momentum protected.
Approved Trope Menu. The new school year that changes everything, the competition team, the family trade inherited early, the sibling responsibility, the mentor teacher, the secret talent, the community project that becomes a cause, the friendship tested and remade, the first love that teaches.
Content Notes. YA runs on the age-appropriate gates of Section 9.7 regardless of the declared rating: romance emotionally led and age-appropriate, violence survivable-tense, language mild.
Image Policy. None (map permitted if modifier is OV-FAN).
Cover Direction. Character-forward, bright contrast, contemporary energy within photorealism.
Metadata Notes. YAF BISAC tree by modifier lane; age range twelve to eighteen declared in KDP; keywords carry teen fiction signals for the lane.
OV-10 / OV-ACT: ACTION AND ADVENTURE
Definition. A story of momentum and capability: a protagonist crosses hostile ground toward a concrete objective through set-piece obstacles, and earns victory through skill, grit, and team.
Mandatory Elements. A concrete objective statable in one line; a journey or operation spine; four to six set pieces, each teaching or costing something used later; a capable opposing force; a team with distinct competencies; victory earned by established skill.
Forbidden Elements. Invincibility, consequence-free destruction, rescue by coincidence.
Ending Law. Objective achieved (or transformed into the truer objective), cost paid, team honored.
Structure. UFFV-HJ or UFFV-3ACT fast; set pieces placed at roughly fifteen, thirty, fifty, sixty-five, eighty, and ninety-two percent.
Budgets. Novel 65,000-85,000 words; 30-42 chapters; 1,800-2,600 words per chapter.
POV and Tense. Third limited, one to three viewpoints; past tense.
Pacing Profile. Fastest sentence rhythm in the catalogue during set pieces (Section 8.5); connective chapters short and purposeful.
Approved Trope Menu. The salvage expedition, the mountain rescue, the heist to recover what was stolen, the desert crossing, the storm season convoy, the wildlife ranger unit, the search for the lost expedition.
Content Notes. Set-piece violence follows the declared rating; in every rating the set pieces are consequence-real and skill-earned.
Image Policy. Optional single route map.
Cover Direction. Motion and scale: figure against terrain, weather as antagonist. No weapon-forward compositions.
Metadata Notes. BISAC FIC002000; keywords carry the terrain and the objective.
OV-11 / OV-WFC: WOMEN'S FICTION AND FAMILY DRAMA
Definition. Emotional-truth fiction centered on a woman's or a family's relational transformation: marriages, sisters, mothers and daughters, inheritance of duty, and the remaking of a life.
Mandatory Elements. A protagonist at a life hinge; a relational web of at least four consequential bonds; a secret, debt, or duty surfacing by twenty percent; escalating relational reckonings; a choice at the climax that redefines the protagonist's place; transformed relationships shown in a coda.
Forbidden Elements. Cruelty without account; transformation delivered by romance alone.
Ending Law. Emotionally true and restorative; relationships end honestly repaired, honestly released, or honestly redefined.
Structure. UFFV-3ACT relational profile or UFFV-DUAL for generational braids.
Budgets. Novel 70,000-90,000 words; 24-32 chapters; 2,400-3,400 words per chapter.
POV and Tense. First or close third; one to three viewpoints (sisters and generations braid well); past tense default.
Pacing Profile. Scene-sequel balanced; each act closes on a relational reversal.
Approved Trope Menu. The family business at a crossroads, the return for a parent's care, the recipe book of a grandmother, the house that must be sold or saved, the sister who came back, the letter unsent for twenty years, the season of weddings, the marriage at a truth point.
Content Notes. Difficult relational material (divorce, betrayal, estrangement) is fully available; the declared rating sets how directly it is rendered.
Image Policy. None.
Cover Direction. Warm domestic scene or symbolic heirloom object; light-filled palettes rotated per window rule.
Metadata Notes. BISAC FIC044000 Women plus FIC045000 Family Life; book club questions standard back matter option.
OV-12 / OV-FTH: FAITH AND INSPIRATIONAL FICTION
Definition. Fiction in which lived faith is load-bearing in character and plot: the story could not happen to a faithless cast unchanged. Commercial lanes include inspirational fiction, Christian fiction, Muslim-life fiction, and interfaith family stories.
Mandatory Elements. Faith practiced naturally on the page (worship, community, ethics in trade and family) without sermon interludes; a trial that tests conviction; counsel and community as real forces; growth in trust, patience, gratitude, or courage; hope in the ending.
Forbidden Elements. Preachiness (narrative halted to lecture), caricature of any faith, tidy miracles replacing earned resolution, despair endings.
Ending Law. Hope earned through faith lived; the trial resolved and the character deepened.
Structure. UFFV-3ACT; the interior arc (doubt to trust, fear to courage) is plotted on the beat grid alongside the exterior plot.
Budgets. Novel 60,000-80,000 words; 22-30 chapters; 2,200-3,200 words per chapter.
POV and Tense. First or close third, one or two viewpoints; past tense.
Pacing Profile. Warm and steady; reflective sequels carry the interior arc and are capped at one third of any chapter.
Approved Trope Menu. The new minister's or imam's first season in a divided community, the family bakery and the hard ethical question, the convert or returner finding family, the savings tested by a neighbor's need, the school under threat and the parents who save it, the reconciliation of estranged siblings before a season of pilgrimage or holiday.
Content Notes. Faith fiction lanes conventionally publish at Clean; the market expects it and the metadata signals it. The dignity standards of Section 9.6 extend to every faith depicted.
Image Policy. None.
Cover Direction. Light-filled architecture, lanterns, gardens, seasonal motifs rendered photographically; no icon badges.
Metadata Notes. BISAC FIC041000 Religious general (FIC042000 Christian lanes where applicable) with lane-matched keyword strategy; comparable-free keyword slots per the trademark screen.
## SECTION 5: STORY ARCHITECTURE ENGINE
5.1 The Story Spec (Phase 1 Artifact)
The Story Spec is a one-page locked contract produced before any bible or chapter. Fields:
Working title, marketplace, manuscript language, imprint, pen name (locked per Rule 3).
Primary overlay, modifier overlay (if any), format, age band.
Content rating (UFFV-Clean or UFFV-Mainstream) and, where Mainstream, the heat and intensity declarations the overlay requires.
Premise in one sentence: protagonist, want, obstacle, stakes.
Dramatic question in one sentence (the question the climax answers).
Theme as a thematic statement (what the book says about its subject), plus one motif for Leitwortstil tracking.
Setting: time, place, social frame.
Structure selection from the library (5.2) with rationale in one line.
POV type, viewpoint character list, tense (locked per Rule 13).
Word target, chapter count, chapter band (locked per Rule 14).
Series flag and, if series, the position and thread note.
Comparable positioning in plain words (no author names, no trademarks).
5.2 The Structure Library

[TABLE]
Code | Structure | Use
UFFV-3ACT | Three acts on the fifteen-beat Master Grid (Appendix A): setup and inciting incident, confrontation with midpoint reversal, resolution through climax | Default for THR, MYS, HOR, LIT, HIS, WFC, FTH, SFI
UFFV-HJ | The working monomyth in twelve stages, departure to return, condensed from the seventeen-stage canon | FAN and ACT defaults; SFI voyages
UFFV-ROMBEAT | The romance beat sheet (Appendix B) fused to the three-act grid | OV-ROM mandatory
UFFV-MYSBEAT | The mystery clue structure (Appendix C) fused to the three-act grid | OV-MYS mandatory
UFFV-KTK | Kishotenketsu: introduction, development, turn, consequence; tension without required combat | OV-LIT quiet shapes; short stories
UFFV-DUAL | Dual timeline: two braided lines, alternating by chapter, converging at a shared revelation at eighty-five to ninety percent | HIS past-present braids; WFC generational; SFI (full grid: Appendix F)
[/TABLE]

5.3 The Fifteen-Beat Master Grid
Every structure maps onto the Master Grid in Appendix A, which places fifteen beats by percentage of total words. The Beat Sheet (Phase 4) assigns every beat to a numbered chapter before drafting. The grid is a placement law, not a formula for content: what happens is the story's own; where it lands is governed.
5.4 Scene and Sequel Units
Scene: goal, conflict, outcome (usually a setback or a costly win). Sequel: reaction, dilemma, decision that launches the next scene. Every chapter is composed of one to three such units. Overlay pacing profiles set the ratio: THR and ACT run scene-heavy; LIT and FTH give sequels fuller weight; ROM alternates emotional scenes with reflective sequels on the beat sheet.
5.5 Subplot Governor
Maximum three subplots in a novel (one in a novella). Each subplot receives its own three-beat mini-arc (launch, complication, resolution) placed on the Beat Sheet, must braid into the main plot at a stated beat, and must either serve the theme or pressure the protagonist. Orphan subplots are removed at QA Pass 1.
5.6 Opening and Closing Laws
Page one establishes viewpoint character, want or imbalance, and setting within the first three hundred words; the inciting incident lands inside the overlay's window (Appendix A).
The climax is the longest continuous sequence in the book, on the page and in scene; climaxes by summary are defects.
The resolution shows the changed normal in at least one dramatized scene and lands the final image against the opening image.
5.7 Timeline Ledger
Fields per chapter: story day or date, span covered, elapsed since chapter one, season and weather notes, and any fixed real dates (HIS). The ledger is the sole authority for time; drafting from memory of time is banned.
5.8 Prologue and Epilogue Law
A prologue is permitted only when it earns its place: it must be a dramatized scene (never an information dump), run under 2,000 words, and plant a Chekhov Registry element that fires by the midpoint. Its viewpoint may differ from the body's locked list by declaration at Phase 1. An epilogue is optional in most overlays and the house default in OV-ROM (the bonus HEA epilogue, 1,000-2,500 words, set weeks or months later, dramatizing the committed life in one scene). Series epilogues may carry the soft forward hook of Rule 28. Both are placed on the Beat Sheet at Phase 4 and counted inside the word budget.
## SECTION 6: CHARACTER SYSTEM
6.1 The Character Bible (Phase 2 Artifact)
The Character Bible is created after the Story Spec and before the World Bible. It contains the Protagonist Sheet, Antagonist Sheet, Supporting Cast Register, Relationship Map, and Voice Marker Log. Drafting before the bible gate is banned (Rule 20).
6.2 Protagonist Sheet (fourteen fields)
Name (naming law compliant), age, role and trade.
Want (external, concrete, statable in one line).
Need (internal, the true lack the story answers).
Wound (the past event that installed the lie).
The lie believed (the false rule the character lives by at page one).
Strengths (three) and flaws (three), each capable of driving a scene.
Physical anchors: exactly three, logged for continuity (the three-anchor limit is a continuity and echo-scan device).
Voice markers: three logged speech signatures (rhythm, vocabulary register, verbal habit).
Arc type: positive, flat, or negative, declared at Phase 1 (a negative-arc protagonist is a deliberate choice recorded in the Story Spec).
Arc milestones mapped to acts: the lie at act one, the lie tested at midpoint, the lie broken at the dark night, the truth acted on at climax.
Relationships: bonds to every major character in one line each.
Skills and knowledge state at page one (feeds the Continuity Ledger).
Values note: what the character will not trade (drives choices under pressure).
The one-sentence essence line used to keep the character consistent at every gate.
6.3 Antagonist Sheet
Same fields, plus: the plan (what the antagonist is doing before page one and at each act), why they are right in their own eyes (Rule 21), the mirror principle (which protagonist flaw or theme the antagonist embodies at full strength), and the pressure schedule (which chapters they squeeze). Antagonists may be persons, institutions, nature, or the unseen; institutions and nature still receive a face character who carries the pressure on page.
6.4 Supporting Cast Register and Casting Caps
Every named character is registered at creation with role, one-line essence, distinguishing anchor, and first-appearance chapter. Caps (Appendix D) bind by word band; exceeding a cap requires merging characters, not waiving the cap.
6.5 Character Naming Law
No two major characters share a first initial; across the full named cast, no more than two share any initial.
Names fit the setting and culture and are pronounceable on first read; invented-world names carry at most one apostrophe-free unfamiliar cluster.
Every major name is screened against famous living persons and existing famous fictional characters (live web or NOT RUN).
Nicknames are registered as aliases; a character is introduced under one name and keeps it unless a reveal is plotted on the Beat Sheet.
6.6 Voice Differentiation Law
Each major character's three voice markers are enforced at chapter gates: read any dialogue line with the tag removed and the register should identify the speaker among the majors. Shared idiolect across characters is an echo-scan defect.
6.7 Arc Tracking Ledger
A per-chapter line records each viewpoint character's position on their arc (lie held, lie doubted, truth glimpsed, truth resisted, truth acted). QA Pass 2 verifies each arc moves through its milestones and that no chapter moves an arc backward without a plotted reason.
## SECTION 7: WORLD, SETTING AND CONTINUITY
7.1 Setting Sheet (all overlays)
Time, place, and social frame rendered as usable craft: five sensory signatures of the primary setting (sound, smell, light, texture, weather), the economic life of the place (what people do all day), the social rules that create pressure, and the map of recurring locations with travel times between them.
7.2 World Bible (OV-FAN and OV-SFI mandatory; OV-HIS as Era Brief)
Physics or wonder frame: what differs from the real world, in one page.
The system triad: source (where the power or technology comes from), cost (what it takes from the user or the world), limit (what it cannot do). All three are locked before drafting and may not loosen mid-book.
Cosmology and geography sufficient to the plot, built bottom-up from the locations the story actually visits, expanded top-down only where travel or politics demand.
Cultures: for each on-page culture, livelihood, values, authority, celebration, and one internal disagreement (one-opinion cultures are banned).
History: only the past that presses on the present of the story, as a dated line list.
Invented-term registry: every coined word with meaning, part of speech, and first use; the glossary trigger fires at fifteen terms (Section 13).
7.3 Era Brief (OV-HIS)
Produced with uapf-research-compliance before drafting: period frame, material culture list (dress, food, tools, money, transport, communication), speech register guidance, law and authority structure, the anachronism watchlist (top twenty period-breaking errors for that era), and the source ledger. Real events touching the plot get fixed dates into the Timeline Ledger.
7.4 Continuity Ledger
The single consistency authority, updated at every chapter gate: character knowledge states (who knows what, as of which chapter), physical anchors and injuries with healing clocks, possessions and their locations, location facts established, world rules invoked, promises opened (and the Chekhov Registry cross-reference), and names-dates-numbers stated on the page. Every chapter is drafted against the current ledger; QA Pass 3 audits the whole book against it.
7.5 The Chekhov Registry
Every planted element is logged at planting: item, chapter, intended payoff window. At the climax gate the registry must show every plant fired or removed and every payoff planted. Mystery clues live in the Clue Grid, which is the registry's OV-MYS extension.
## SECTION 8: PROSE ENGINE
8.1 POV Discipline
Viewpoint is locked per Rule 13. Within a scene the camera stays behind one character's eyes: no other character's thoughts, no information the viewpoint character cannot perceive, no narrator asides in limited modes. Viewpoint changes occur only at scene or chapter breaks and are signposted by the first sentence naming the new viewpoint character.
8.2 The Eight Dialogue Laws
D1: Said is the default tag; expressive verbs (whispered, called) are rationed; tags are dropped where beats identify the speaker.
D2: No adverb stacking on tags; the emotion lives in the line and the beat.
D3: Conflict scenes carry subtext: characters pursue goals through speech, they do not announce feelings on request.
D4: No maid-and-butler exposition (two characters telling each other what both know for the reader's benefit).
D5: Dialect is rendered by rhythm, word choice, and syntax, never phonetic spelling.
D6: Trailing speech uses ellipsis; interrupted speech is cut with a period and an action beat (the em dash convention is banned by Rule 2 and this substitute is the house standard).
D7: Language follows the title declared content rating (Section 9.5); where the rating permits strong language, it is rationed and character-true, and pressure is still voiced first through crafted speech.
D8: Every major character speaks through their three logged voice markers.
8.3 Show Priority and Filter Words
Dramatize turning points, decisions, and emotions; summarize travel and routine. The filter list (saw, heard, felt, noticed, realized, watched, seemed, wondered, thought, knew) is minimized: the target is fewer than three filter constructions per thousand words outside deliberate interiority in OV-LIT.
8.4 Sensory Anchor Rule
Every scene opening grounds the reader in place with at least two senses inside the first paragraph, chosen from the setting sheet's sensory signatures so that recurring locations stay recognizably themselves.
8.5 Sentence Rhythm Rule
Action sequences average under twelve words per sentence with paragraph lengths of one to three sentences; reflective passages may run to twenty-word averages with fuller paragraphs; every page varies sentence length. Three consecutive sentences of near-equal length trip the echo scan outside deliberate incantation effects.
8.6 The Anti-Duplication Variation Engine (Fiction Edition)
Word echo: no distinctive word repeated within one hundred fifty words (names, said, and function words exempt).
Image echo: no simile or metaphor reused in the book; the image log grows at every chapter gate.
Scene-shape echo: no repeated shape (same location, same pair, same conflict type, same outcome) within five chapters.
Opener rotation: chapter openings rotate across the four modes (Action, Dialogue, Setting, Interior); no two consecutive chapters share a mode and no mode exceeds forty percent of the book.
Beat phrasing: recurring physical beats (nodding, sighing, turning) are budgeted; the beat frequency report prints at every fifth chapter gate.
8.7 Cliche and Stock Phrase Blacklist
The blacklist ships in the prompt document and includes, at minimum: a breath she did not know she was holding, heart pounding like a drum, time stood still, piercing eyes of any color, raven hair, steely gaze, deafening silence, cold sweat, blood ran cold, every fiber of her being. Blacklist hits are chapter-gate defects; fresh images are drawn from the setting's own sensory signatures.
8.8 Interior Monologue Standard
Direct thought is rendered in italics sparingly; free indirect style is the default interior register in third limited. Interiority never repeats what the scene just dramatized.
8.9 Paragraphing and White Space
Paragraphs turn with the camera: new speaker, new paragraph; new focus, new paragraph. Action climaxes earn short paragraphs and white space; dense pages in act three are a pacing defect.
8.10 Language Localization of Prose Tools
The filter watchlist, the cliche blacklist, the echo scans, and the opener rotation operate in the manuscript language. For any non-English title, Phase 1 produces language-equivalent tool sets (minimum twenty-five blacklist entries and ten filter constructions native to that language, not translations of the English lists) and appends them to the Story Spec; every chapter gate and QA Pass 9 then runs on the localized sets.
## SECTION 9: CONTENT STANDARDS AND RATINGS
The framework does not impose a single content standard. Instead, every title declares a rating at Phase 0 (Rule 1) and the declared rating is enforced with the same rigor as any other lock: at every chapter gate and at QA Pass 10. The rating is a market-positioning instrument; the dignity standards of 9.6 and the YA gates of 9.7 apply regardless of rating.
9.1 The Rating Declaration
Two ratings exist: UFFV-Clean and UFFV-Mainstream. The rating is declared at Phase 0, recorded in the Story Spec, and drives category placement, keyword signaling, and QA. Where the operator states no preference, Mainstream is the default. A rating may only change through the Correction Protocol, which re-audits every drafted chapter.
9.2 UFFV-Clean (market lane)
Chosen when targeting clean, sweet, wholesome, cozy, faith, and family-shelf markets. Under Clean: romance is closed-door throughout; there is no profanity; lethal violence occurs off page or at fade with consequence carried on page; no explicit content of any kind. Clean unlocks Clean and Wholesome category placement and clean keyword signaling in the metadata pack.
9.3 UFFV-Mainstream
General trade conventions per overlay and lane. Intimate content is written to the heat ceiling declared at Phase 1 and held consistently; the catalogue does not publish content requiring adult classification under platform policy. Strong language is permitted, rationed, and character-true (9.5). Violence and dread run at genre-standard intensity for the declared lane (9.4).
9.4 Violence Scaling
Clean: consequence-forward; lethal violence off page or at fade; injuries carry real healing clocks in the Continuity Ledger. Mainstream: on-page intensity at the genre standard of the declared lane, rendered for stakes rather than spectacle, with the same healing-clock discipline. Lane conventions still bind inside either rating: the cozy mystery keeps its crime off page by genre contract regardless of rating.
9.5 Language Scaling
Clean: no profanity; pressure is voiced through crafted, character-true speech. Mainstream: profanity is permitted with a frequency ceiling logged in the Story Spec, deployed for character and impact rather than texture, and never in YA. In either rating, dialect and register work per dialogue law D5 carries more voice than expletives.
9.6 Dignity Standards (rating-independent)
No caricature of any real faith, culture, or people; belief systems on the page are rendered through characters, not verdicts.
Victims of crime and violence are rendered with dignity per the lane's convention; real-events inspiration passes the Phase 0.5 defamation and dignity review.
Revered figures of real religions are not used as characters.
9.7 YA Gates (rating-independent)
No explicit content in any YA title, whatever the declared rating.
Romance is age-appropriate and emotionally led; violence is survivable-tense, not terrorizing; language stays mild.
Themes bend toward agency, repair, and hope; adults may mentor and support but never resolve the protagonist's central problem.
## SECTION 10: PRODUCTION PIPELINE (PHASES AND GATES)
Twelve phases. Every phase closes with exactly the line Type Proceed (Rule 4). The gate register tracks every gate; any upstream change marks each dependent gate RETEST REQUIRED (Rule 30).

[TABLE]
Phase | Name | Output and gate condition
0 | Intake and Detection | Title, language, marketplace, imprint received; overlay plus modifier and format detected and stated in one line; content rating declared (Clean or Mainstream, with Mainstream the unstated default); catalogue uniqueness check run against the Book Register; pen name generated and locked. FMT-SERIAL Book 2 and later: the Series Bible and the prior book's closing ledger snapshots load here per 14.5.
0.5 | Screens | Trademark screen on title and keywords, real-person screen on planned character names and premise (live web research or reported NOT RUN). Defamation and dignity review for any real-events inspiration.
1 | Story Spec | The full Story Spec of 5.1 delivered and locked: premise, dramatic question, theme and motif, structure, POV and tense, budgets, rating with heat and intensity declarations where Mainstream, series flag.
2 | Character Bible | Protagonist and antagonist sheets, supporting register within the casting cap, relationship map, naming law check, voice marker log. Continuity Ledger and Chekhov Registry initialized.
3 | World Gate (conditional) | World Bible (FAN, SFI), Era Brief with research ledger (HIS), or Setting Sheet only (all others). System triad locked. Invented-term registry opened.
4 | Beat Sheet and Chapter Blueprint | All fifteen Master Grid beats (plus overlay beat sheet) assigned to numbered chapters; per-chapter briefs of two to four lines each (viewpoint, location, goal, turn); subplot mini-arcs placed; image slots planned; Timeline Ledger skeleton dated.
5 | Chapter Loop | Chapter-by-chapter drafting per Section 11, rolling DOCX growing, ledgers updating, preview PDFs and cowork briefs at each gate.
6 | Whole-Book QA | The QA passes of Section 12 run and logged (twelve core, plus Pass 13 for series and Pass 14 for collections); defects corrected under the Correction Protocol; passes re-run to green.
7 | Front and Back Matter | Per the overlay's matter table in Section 13: title pages, copyright, dedication, epigraph optional, map plate where planned, Author's Note (HIS mandatory), glossary trigger check, acknowledgements, About the Author (pen name legend consistent), Also By, series preview chapter where applicable, book club questions where flagged.
8 | Formatting | Interior typography per Section 13 executed through uapf-formatting-engine; whole-book format audit; print PDF and EPUB masters prepared.
9 | Cover | UDCF pipeline through uapf-cover-aplus-system with the overlay's cover direction; all catalogue cover laws verified (photorealistic only, no icons or badges or selling points, no violence or blood, background base color rules within the five-cover window, read from the Cover Base Color Ledger per Section 16).
10 | Metadata and KDP Pack | Blurb per the formula, seven keywords, BISAC primary and secondary, age range where YA, series metadata, pricing bands, the KDP AI-content declaration compiled per Section 17.7, KDP Upload Sheet fields per the upstream automation framework.
11 | Release QC and Register | uapf-release-qc independent whole-book validation; reader promise re-verified; archives and checksums; Book Register record appended (or output with reminder).
[/TABLE]

10.1 Delegation Map
Research and screens: uapf-research-compliance. Chapter assembly and rolling DOCX: uapf-manuscript-builder. Per-chapter gate and preview PDF: uapf-chapter-format-auditor. Book-wide formatting and masters: uapf-formatting-engine. Covers and A+ assets: uapf-cover-aplus-system. Final validation: uapf-release-qc. The framework's own ceilings, ledgers, and laws override specialist defaults wherever they conflict.
## SECTION 11: THE CHAPTER LOOP (PHASE 5 IN DETAIL)
11.1 Inputs to Every Chapter
The chapter brief from the blueprint; the current Continuity, Timeline, and Arc ledgers; the Chekhov Registry; the beat this chapter must land; the word band; the opener mode assigned by rotation.
11.2 Draft Rules
Open on the assigned mode with the hook; ground with the sensory anchor rule; hold single viewpoint; land the brief's turn; close with the overlay's forward pressure.
Every scene passes the unit test: goal, conflict, outcome; every sequel: reaction, dilemma, decision.
The chapter advances at least one of plot, arc, or relationship, and never only worldbuilding.
11.3 The Fifteen-Point Chapter Self-Edit
1. Beat landed as briefed. 2. Word band held. 3. Single viewpoint held, tense clean. 4. Hook opens, pressure closes. 5. Sensory anchor present. 6. Dialogue laws D1 to D8 pass. 7. Filter-word count within target. 8. Echo scan clean (word, image, scene shape, opener mode). 9. Blacklist clean. 10. Continuity checked against ledger, ledger updated. 11. Timeline entered. 12. Arc position entered. 13. Chekhov plants and payoffs logged. 14. Declared content rating held. 15. Em dash scan returns zero.
11.4 Gate Deliverables
The chapter merged into the rolling DOCX; the versioned read-only chapter preview PDF from uapf-chapter-format-auditor; ledger snapshots; cowork_generate_chNN.md when the chapter contains image slots; the governor report (running total against budget); the chapter tension score (1 to 5) logged to tension_map.md. The gate closes with Type Proceed.
11.5 Halt Conditions
Two consecutive out-of-band chapters, a governor drift beyond ten percent projected, a continuity conflict the ledger cannot resolve, or any Critical Rule violation halts the loop for correction before the next chapter is drafted. The fifth-gate beat-drift projection of 3.3 applies (AMBER at five points, HALT at eight), and the climax exemption waives per-chapter minimums inside beat 14.
## SECTION 12: WHOLE-BOOK QA (TWELVE CORE PASSES PLUS TWO CONDITIONAL)

[TABLE]
Pass | Audit | Green condition
1 | Structure and Promise | Every Master Grid beat present within window; overlay mandatory elements all present; forbidden elements absent; the ending law satisfied on the page; subplots braided and resolved.
2 | Arcs | Every viewpoint arc moves through its milestones; the protagonist's lie is installed, tested, broken, and answered; no unplotted regressions.
3 | Continuity | Whole book audited against the final Continuity Ledger: knowledge states, anchors, injuries, possessions, world rules, names and numbers all consistent.
4 | Timeline | Ledger reconciled: seasons, travel, healing, day-night, and (HIS) real dates all plausible and consistent.
5 | Chekhov | Registry closed: all plants fired or removed, all payoffs planted; (MYS) the Clue Grid balances.
6 | Fair Play (MYS only) | Every clue reader-visible at detective contact; culprit inside thirty percent; solution reproducible from on-page evidence.
7 | Ending Law by Overlay | ROM committed and hopeful in scene; THR threat resolved; HOR threat resolved or truthfully contained at cost; FTH hope earned; YA hopeful and agent; each per its specification.
8 | Escalation (THR, HOR, ACT) | The logged tension map (1 to 5 per chapter from the gates) rises act over act; the midpoint bars retreat; no five-chapter window sags below its act baseline.
9 | Prose | Whole-book echo scan, opener rotation report, filter and blacklist sweep, sentence-rhythm sampling, dialogue law sampling, all within targets.
10 | Content Rating | Full Section 9 sweep: the declared rating held across intimacy, language, and violence; heat and intensity ceilings consistent end to end; dignity standards met; YA gates where active.
11 | Mechanics | Em dash and en dash scan returns zero everywhere including front and back matter; punctuation, numerals, and capitalization per house style; language of manuscript consistent.
12 | Budget | Total words within ten percent of target; chapter bands within tolerance; page estimate updated for Phase 8.
13 | Series (FMT-SERIAL only) | Standing cast knowledge states, timeline, and invented terms consistent with the Series Bible and every prior book; the series thread advanced, not resolved (unless the final book); no contradiction with any published book.
14 | Collection Unity (FMT-SHORT only) | Every story satisfies its own promise and mini ending law (Passes 1, 2, and 7 run per story); the unifying theme present in each; no premise duplicated between stories; the order builds, with the strongest stories opening and closing.
[/TABLE]

Each pass logs findings as a defect list with chapter references. Defects route through the Correction Protocol; a corrected book re-runs the affected passes to green before Phase 7; Passes 13 and 14 run only where their format flag is set.
## SECTION 13: TYPOGRAPHY, INTERIOR AND MATTER SPEC
13.1 Trim and Page Geometry

[TABLE]
Overlay group | Trim | Notes
ROM, THR, MYS, HOR, YA, ACT, WFC, FTH | 5 x 8 in | House fiction default
FAN, SFI, HIS, and LIT above 90,000 words | 6 x 9 in | Long-form comfort
Novellas, all overlays | 5 x 8 in | Uniform
[/TABLE]

Margins: top 0.75 in, bottom 0.75 in, outside 0.5 in. Inside gutter by KDP page count table: 24-150 pages 0.375 in; 151-300 pages 0.5 in; 301-500 pages 0.625 in; 501-700 pages 0.75 in; 701-828 pages 0.875 in.
13.2 Body Typography
Body face Palatino Linotype 11 pt (alternate EB Garamond 11.5 pt where licensing requires), line spacing 1.15 on 5 x 8 and 1.2 on 6 x 9, justified, first-line indent 0.3 in, no space between paragraphs. First paragraph after any chapter opening or scene break is flush left. Scene break marker: a centered line of three spaced asterisks. Hyphenation on; widow and orphan control on; no more than two consecutive end-line hyphens.
13.3 Chapter Openers and Heads
Chapters begin on a new page, text starting one third down. Chapter label in small caps 14 pt (Chapter One style for LIT, HIS, FTH; Chapter 1 numerals for THR, ACT, SFI; overlay default otherwise numerals). Chapter titles optional by overlay: ON for FAN, HIS, LIT, WFC; OFF for THR, MYS default. Drop caps (three-line) optional for LIT, HIS, FAN; OFF elsewhere. Running heads: verso author name, recto book title, small caps 9 pt, suppressed on opener pages. Page numbers bottom center.
13.4 Front Matter Order
Half title; title page (title, subtitle if any, pen name, imprint); copyright page (imprint line, year, rights line, this-is-a-work-of-fiction line, ISBN placeholder); dedication (optional); epigraph (optional); map plate where planned; Table of Contents only where chapter titles are ON. Fiction default for ROM, THR, MYS is no TOC.
13.5 Back Matter Order
Author's Note (HIS mandatory: fact versus invention); glossary when the invented-term registry exceeds fifteen entries (FAN, SFI); acknowledgements (optional); review request page (one short paragraph inviting an honest review); About the Author (pen name legend, consistent across the imprint); Also By (series and imprint backlist); series preview: chapter one of the next book where the series flag is set; book club questions (eight to twelve) where flagged for LIT and WFC.
13.6 Page Estimation
Words per page: 5 x 8 approximately 290; 6 x 9 approximately 350. Estimated pages equal words divided by the factor, plus matter pages, rounded up to an even number. The estimate updates at every fifth chapter gate and feeds spine width at Phase 9 through the established preflight framework.
## SECTION 14: SERIES ARCHITECTURE
14.1 The Series Flag
Set at Phase 0. FMT-SERIAL activates the Series Bible before Book One's Story Spec and re-loads it at every subsequent book's Phase 0.
14.2 The Series Bible
Series premise and the series-long thread (the question only the final book answers).
The book map: one line per planned book (its own conflict, its thread advance), three to seven books.
The standing cast with per-book knowledge states; the standing world rules; the standing timeline.
Naming, place, and term registries shared across books (the ledgers begin from the bible, not from zero).
The escalation plan: how stakes rise book over book without breaking the code.
14.3 Per-Book Laws
Every series book resolves its own central conflict on the page and advances the series thread (Rule 28). Hard cliffhangers that withhold the book's own promised ending are banned; a soft forward hook (a new question opened after the resolution) is the permitted series pull, strongest in THR and FAN. Book One must stand fully alone. Recaps in later books are woven, never front-loaded summaries.
14.4 Series Packaging
Numbering appears in subtitle position (A Something Series Book N pattern), covers share a family system under the UDCF background window rules, Also By updates every earlier book at each release, and the preview chapter law feeds each book's back matter.
14.5 Series Runtime
At Phase 0 of Book N (N of two or more): load the Series Bible and Book N minus one's closing snapshots of the continuity, timeline, and arc ledgers, the invented-term registry, and the cover base colors. The new book's ledgers initialize from that carried state, never from zero; the book map row for Book N seeds the premise; the escalation plan is checked against the new Story Spec; and QA Pass 13 audits the finished book against the whole series state.
## SECTION 15: IMAGE SYSTEM (FICTION EDITION)
15.1 Default
Fiction interiors are text-only. This is the operator's standing economy: images only where they genuinely serve comprehension or genre convention.
15.2 Permitted Slots by Overlay

[TABLE]
Overlay | Standard slots | Optional slots
FAN | [IMG-01] world or region map (illustrated) | Chapter-opening glyph set (one repeated ornament)
SFI | None | [IMG-01] star map or station schematic
HIS | [IMG-01] era map (illustrated) | One period plate
MYS | None | Village or house map for manor and village mysteries
ACT | None | Route map
All others | None | Chapter ornament only by operator order
[/TABLE]

15.3 Mechanics
All slots follow Rule 6: [IMG-XX] placeholders in the rolling DOCX, matching rows in image_manifest.md, cowork_watcher.md at the configuration gate, cowork_generate_chNN.md at any chapter gate carrying slots, cowork_image_task.md at final delivery for fill-and-insert. Prompts are content-derived from the drafted text, self-contained, always in English, and genre-matched. Interior maps are originally illustrated (the travel-guide precedent); the photorealism mandate applies to covers, not interior maps. The Google Flow desktop pipeline consumes the briefs; files return as IMG-XX.png for the automated insertion pass.
## SECTION 16: COVER DIRECTION (UDCF HANDSHAKE)
Covers run through uapf-cover-aplus-system under UDCF. Restated hard laws: photorealistic only; no icons, badges, vector or clip art; no selling points on covers; no violence or blood; no two consecutive imprint covers share a background base color and no base color repeats within any five-cover window. The overlay Cover Direction lines in Section 4 feed archetype selection; typography is deterministic per UDCF; the manuscript-upload workflow (extract title, subtitle, author; skim for themes; Stage 1 variables; archetype; composition; generation prompt) runs automatically at Phase 9. The Cover Base Color Ledger supplies the window state: Phase 9 reads the last four base colors from the Book Register's Cover Base Color column, or from covers_ledger.md when the register is not uploaded, and Phase 11 writes the new base color back.
## SECTION 17: METADATA AND MARKETING PACK
17.1 Title and Subtitle Law
Fiction titles stand alone; subtitles are optional and, when used, carry series position or a single evocative phrase. No keyword-stuffed subtitles in fiction. Title uniqueness is checked at Phase 0 (Rule 10).
17.2 The Blurb Formula (120 to 170 words)
Line 1: the hook, a question or bold statement in the book's voice.
Block 1: protagonist, world, and want in two to three sentences.
Block 2: the disruption and the stakes.
Block 3: the impossible choice, teased without spoiling anything past the forty percent mark.
Final line: the promise or the question, plus the series line where applicable.
The blurb obeys the em dash ban, names no other author, references no trademarked property, and is written in the overlay's register (a THR blurb is clipped; a WFC blurb is warm). It ships as two variants, A and B, built on different hook angles; the operator selects at Phase 10, mirroring the cover candidate convention.
17.3 The Seven Keyword Slots
1: subgenre phrase. 2: active trope phrase. 3: mood and pace phrase. 4: setting phrase. 5: audience phrase (clean or mainstream signals per the declared rating). 6: comparable positioning in generic words (no names, no trademarks). 7: format or series phrase. All seven pass the trademark screen; the TM-Safe Reframe Layer applies.
17.4 BISAC Map

[TABLE]
Overlay | Primary | Common secondary
ROM | FIC027050 Romance Contemporary (or FIC027110 Historical) | FIC042040 Clean and Wholesome where rated Clean
THR | FIC030000 Thrillers General | FIC031010 Espionage / FIC031080 Psychological by lane
MYS | FIC022000 Mystery and Detective General | FIC022070 Cozy / FIC022020 Women Sleuths
FAN | FIC009020 Fantasy Epic | FIC009100 Fantasy Action and Adventure
SFI | FIC028000 Science Fiction General | FIC028070 Space Exploration by lane
HOR | FIC015000 Horror | FIC024000 Occult and Supernatural (used with clean signaling)
LIT | FIC019000 Literary | FIC045000 Family Life
HIS | FIC014000 Historical General | Period lane code
YA | YAF lane by modifier | YAF lane secondaries; Clean and Wholesome equivalents where rated Clean
ACT | FIC002000 Action and Adventure | Terrain lane
WFC | FIC044000 Women | FIC045000 Family Life
FTH | FIC041000 Religious | FIC019000 Literary where fitting
[/TABLE]

17.5 Pricing Bands
Ebook: 2.99 to 5.99 USD-equivalent by length and lane, with Book One of a series permitted at the low band. Paperback: KDP printing cost plus imprint margin by page count, harmonized across the fifteen marketplaces at Phase 10. Final prices are operator-approved on the KDP Upload Sheet; the framework supplies the recommendation.
17.6 A+ Content
Fiction A+ masters (970 x 600) follow the cover system's guidance: mood banner, series banner where applicable, and the lane promise stated plainly. Produced by uapf-cover-aplus-system.
17.7 AI Disclosure
The KDP AI-content declaration is completed truthfully for every title. The disclosure record (text, images, and cover, each marked AI-generated, AI-assisted, or none) is compiled at Phase 10, carried on the KDP Upload Sheet, verified by uapf-release-qc at Phase 11, and archived with the release package.
## SECTION 18: CORRECTION PROTOCOL
A correction is scoped exactly: the artifact, the chapters, the lines, the ledgers touched.
Corrections never advance a gate on their own (Rule 30); the corrected artifact re-enters its own gate.
Any upstream change marks every dependent gate RETEST REQUIRED in the gate register; the retest list prints with the correction.
Ledger corrections cascade: a continuity fix re-audits every later chapter that touched the corrected fact.
Structure-level corrections (a beat moved, a POV added) re-run Phase 4 and invalidate all later chapter gates; this is stated plainly to the operator before executing.
Whole-book QA re-runs only the affected passes, then Pass 12, before Phase 7 resumes.
## SECTION 19: DELIVERABLES REGISTER AND OUTPUT FORMAT
19.1 Deliverables by Phase
Phase 1: story_spec.md. Phase 2: character_bible.md, continuity_ledger.md (initialized), chekhov_registry.md. Phase 3: world_bible.md or era_brief.md with source ledger, invented_terms.md. Phase 4: beat_sheet.md, chapter_blueprint.md, timeline_ledger.md, image_manifest.md (initialized), cowork_watcher.md. Phase 5, per chapter: rolling DOCX updated, chapter preview PDF (versioned, read-only), ledger snapshots, cowork_generate_chNN.md where slots exist. Phase 6: qa_report.md with the twelve passes. Phase 7 and 8: matter complete, print PDF and EPUB masters. Phase 9: cover candidates A, B, C and the selected wrap. Phase 10: metadata_pack.md and the KDP Upload Sheet row. Phase 11: release_qc.md, archive with checksums, Book Register record. In addition: run_state.md is created at Phase 0 and updated at every gate; Phase 5 grows tension_map.md; Phase 9 maintains the base color state (register column or covers_ledger.md); FMT-SERIAL maintains series_bible.md across books.
19.2 Standing Output Format at Every Significant Transition
Current state; detected overlay, modifier, and format with the one-line rationale; active goal; locked inputs; skills invoked; gates passed, pending, invalidated; next permitted action; current artifact paths; current chapter preview link and correction status; governor report line.
19.3 Resume Protocol
A paused run resumes only from artifacts: load run_state.md (phase, gate register states, governor line, artifact list, next permitted action, open corrections), every ledger, and the latest rolling DOCX; print the Standing Output block; continue at the recorded next action. Resuming from conversation memory is banned; the ledger-not-memory principle of Rule 15 extends to the run itself.
## APPENDIX A: THE FIFTEEN-BEAT MASTER GRID

[TABLE]
Beat | Name | Placement | Function
1 | Opening Image and Ordinary World | 0-2 percent | Establish viewpoint, want or imbalance, setting; the image the final image will answer
2 | Setup | 2-8 percent | Stakes of normal life; the lie believed shown in action
3 | Inciting Incident | 8-12 percent | The disruption that makes the dramatic question askable
4 | Debate | 12-18 percent | Resistance, cost-counting; refusal beats live here
5 | First Plot Point | 20-25 percent | Commitment; the door closes on the old normal
6 | New World | 25-35 percent | Adjustment, allies, rules of the new situation
7 | First Pinch | About 35 percent | The opposing force applies direct pressure
8 | Midpoint Reversal | 48-52 percent | Revelation or defeat that changes the goal or the understanding; retreat barred
9 | Raised Stakes | 52-60 percent | Consequences of the midpoint compound
10 | Second Pinch | About 62 percent | The opposing force strikes harder; cost lands close
11 | Complication Cascade | 62-72 percent | Plans fail forward; subplot braids tighten
12 | Dark Night | About 75 percent | The all-is-lost; the lie breaks
13 | Second Plot Point | 78-82 percent | The truth found; the final plan formed
14 | Climax Sequence | 85-95 percent | The longest continuous sequence; the dramatic question answered in scene
15 | Resolution and Final Image | 95-100 percent | The changed normal dramatized; final image answers the opening
[/TABLE]

## APPENDIX B: THE ROMANCE BEAT SHEET (UFFV-ROMBEAT)

[TABLE]
Beat | Placement | Law
Meet or re-meet | By 10 percent | Both leads on page together; the dynamic and the barrier visible
Attraction and barrier | By 15 percent | Why them, and why not yet, both established honestly
First close moment | About 25 percent | A moment of genuine connection through conversation or service
Deepening | 25-45 percent | Escalating emotional intimacy; supporting cast pressure entering
Midpoint shift | About 50 percent | Hope becomes real to both; the stakes of losing it become real too
Doubt seeds | 55-70 percent | The barrier's true weight; honest obstacles, not sustained misunderstanding
Black moment | 75-80 percent | The break; each lead confronts their lie
Truth and gesture | 85-90 percent | Truth spoken; the gesture that proves change
Commitment | 95-100 percent | The committed, hopeful ending in scene; the payoff dramatized
Bonus epilogue | After the final beat | House default: weeks or months later, the committed life dramatized in one scene, 1,000-2,500 words
[/TABLE]

## APPENDIX C: THE MYSTERY CLUE GRID (UFFV-MYSBEAT)

[TABLE]
Element | Placement | Law
Crime established | By 10 percent | Per lane convention (cozy: off page); victim rendered with dignity
Investigator engaged | By 12 percent | Personal stake or duty stated
Suspect pool | 15-30 percent | Four to seven suspects, each with motive, means, opportunity logged
Genuine clues | Distributed | Minimum three; each logged with chapter shown and chapter interpreted
Red herrings | Distributed | Two to four; each with an innocent explanation that surfaces by the reveal
Mid reveal | About 50 percent | A discovery that reorders the suspect pool
Escalation | 55-60 percent | Second crime or sharp raise if momentum requires
False solution | 70-75 percent | Plausible, clue-consistent, wrong
True reveal | 85-92 percent | Reproducible from on-page evidence alone
Explanation and justice | To 100 percent | The full chain shown; the community restored
[/TABLE]

## APPENDIX D: CASTING CAP TABLE

[TABLE]
Word band | Viewpoints | Major cast | Named total | Suspects (MYS)
Under 60,000 | 1-2 | 4-6 | 18 | 4-6
60,000-90,000 | Up to 3 | 5-8 | 25 | 4-7
90,000-120,000 | Up to 4 (5 above 100,000 in FAN, SFI, HIS) | 6-10 | 35 | n/a
[/TABLE]

## APPENDIX E: WORD BAND QUICK TABLE

[TABLE]
Overlay | Novel words | Chapters | Chapter band
ROM | 55,000-80,000 | 24-32 | 2,000-3,000
THR | 70,000-90,000 | 35-50 | 1,500-2,500
MYS | 65,000-85,000 | 26-34 | 2,200-3,000
FAN | 90,000-120,000 | 28-38 | 2,800-4,000
SFI | 80,000-110,000 | 26-36 | 2,600-3,800
HOR | 65,000-85,000 | 26-34 | 2,000-3,000
LIT | 70,000-100,000 | 18-28 | 3,000-5,000
HIS | 85,000-115,000 | 26-36 | 2,800-4,000
YA | 55,000-75,000 | 24-32 | 1,800-2,800
ACT | 65,000-85,000 | 30-42 | 1,800-2,600
WFC | 70,000-90,000 | 24-32 | 2,400-3,400
FTH | 60,000-80,000 | 22-30 | 2,200-3,200
[/TABLE]

## APPENDIX F: THE DUAL TIMELINE GRID (UFFV-DUAL)

[TABLE]
Element | Placement | Law
Line A opens | Chapter 1 | The present (or frame) line owns the book's opening image and dramatic question
Line B opens | By chapter 3 | The second line opens on its own hook; its era or position named in the first sentence
Alternation | Throughout | Default 2:1 A to B by chapter; 1:1 for equal-weight braids declared at Phase 1; no line silent for more than three consecutive chapters
Braid points | 25, 50, 75 percent | An object, echo, or revelation crosses between the lines and raises pressure in both
Line B inciting | B's second appearance | Line B's own disruption lands by its second chapter on page
Aligned midpoint | 48-52 percent | A Line B revelation reframes Line A's understanding; both goals shift
Line B climax | 80-85 percent | Line B resolves first; its truth becomes the key Line A lacks
Convergence | 85-90 percent | The lines meet: Line B's truth unlocks Line A's climax
Joint resolution | 95-100 percent | Both lines close; the final image answers both opening images
[/TABLE]

## APPENDIX G: GLOSSARY OF FRAMEWORK TERMS
Beat: a required story event placed by percentage on the Master Grid.
Black moment: the romance overlay's darkest relational point before truth and gesture.
Braid point: a scheduled crossing of pressure between dual timeline lines (Appendix F).
Casting cap: the maximum named cast by word band (Appendix D).
Chekhov Registry: the ledger of planted elements and their payoffs.
Clue Grid: the mystery overlay's ledger of clues, herrings, and suspects.
Continuity Ledger: the single authority for facts established on the page.
Content rating: the per-title Clean or Mainstream declaration of Section 9, locked at Phase 0.
Echo scan: the anti-duplication sweep across words, images, scene shapes, and opener modes.
Governor: an automatic budget check (words, chapters) that can halt the loop.
Ledger: any append-only tracking artifact updated at chapter gates.
Overlay: a genre specification block in Section 4; one primary, at most one modifier.
Reader promise: the contract of the genre, enforced as the ending law.
Run state: run_state.md, the artifact a paused run resumes from (19.3).
Scene and sequel: the two prose units of Section 5.4.
Soft hook: a new question opened after a book's own resolution; the lawful series pull.
System triad: source, cost, and limit; the consistency lock on any magic or technology.
Tension map: the per-chapter 1 to 5 score that powers QA Pass 8 (11.4).
Voice markers: three logged speech signatures per major character.
End of UFFV 1.1 Master Framework. Companion executable: fiction-prompt. This document is authoritative upon operator approval and supersedes any earlier fiction guidance in memory or prior conversations.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
