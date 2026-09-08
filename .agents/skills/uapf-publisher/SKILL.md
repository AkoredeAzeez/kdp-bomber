---
name: uapf-publisher
description: Publishes finished books to Amazon KDP and other platforms (IngramSpark, Draft2Digital, Kobo, Google Play Books, Barnes & Noble Press, Lulu, Apple Books) via the built-in browser — fills every form from the project's metadata package, uploads interior and cover files, and stops at hard confirmation gates before any Publish click or paid action.
---

# UAPF Publisher — Platform Publishing Skill

This skill is the final hand of the Pegasus Press pipeline. Upstream skills produce the finished
manuscript (DOCX/PDF/EPUB), the cover files, and the `[BookTitle]_KDP_Metadata.docx` (description,
7 backend keywords, 3 categories). `uapf-publisher` takes those finished, QC-passed assets and
publishes the book on Amazon KDP and any additional platforms the operator selects — driving the
platform websites in the built-in browser, filling every field from the metadata package, uploading
files, and halting at hard confirmation gates before anything irreversible or paid happens.

---

## 1. Non-Negotiable Safety Gates (READ FIRST)

These gates override everything else in this skill. No deadline, batch job, or prior instruction
relaxes them.

### 1.1 Credentials, payment, and tax data — NEVER

- Genie **never** enters account passwords, payment details (bank accounts, cards), or tax
  information (SSN/EIN, tax interview answers) into any platform, ever.
- The operator must **already be logged in** to the target platform in the built-in browser.
  On arrival at each platform, Genie verifies the logged-in state (account name/avatar visible,
  dashboard reachable). If not logged in — or if a session expires mid-flow — Genie **stops
  immediately**, tells the operator which platform needs login, and waits. Genie never touches
  the login form.
- If a platform demands completion of a payment or tax setup step before publishing, Genie stops,
  reports exactly what the platform is asking for, and hands control to the operator.

### 1.2 The Publish gate — ALWAYS STOP

- Genie fills all listing forms and uploads all files, but **always stops before clicking any
  final "Publish", "Publish Your Book", "Submit for review", "Submit", "Approve proof", or
  equivalent commit button** on any platform.
- Before that button, Genie presents a **pre-publish summary** in chat:

  | Field | Value shown |
  |---|---|
  | Book | Title, subtitle, byline |
  | Platform + format | e.g. KDP Paperback / KDP Kindle eBook / IngramSpark |
  | Price(s) | List price per marketplace, currency |
  | Royalty | Plan selected and platform's royalty preview figure |
  | Territories | Worldwide or listed territories |
  | Categories | The 3 chosen categories |
  | Keywords | All 7 backend keywords |
  | Files | Interior file name + version, cover file name + version, previewer/validation result |
  | ISBN | Free platform ISBN or own ISBN (with number) |
  | AI disclosure | Answer given, per the operation's records |

- Genie then **waits for the operator's explicit confirmation in chat, for that specific book on
  that specific platform**. "Publish it" for the KDP paperback does not cover the Kindle edition,
  IngramSpark, or any other book.

### 1.3 Money and live listings

- **Price changes to already-live books** require explicit operator confirmation before saving.
- **Any action that spends money** (IngramSpark title setup fees, proof/author copy orders,
  paid services) requires explicit operator confirmation before the paying click.

### 1.4 One confirmation = one action

- An approval covers exactly one action on one book on one platform, once. It never carries
  forward to the next format, the next platform, the next book, or a retry after an error that
  changed anything. Re-present the summary and re-confirm.

---

## 2. Pre-Flight Checklist (before touching any platform)

Run this checklist and report results before opening a browser tab. Any FAIL halts the workflow.

| # | Check | Pass condition |
|---|---|---|
| 1 | Release QC | Final manuscript passed `uapf-release-qc`; QC record on file for this exact file version |
| 2 | Metadata package | `[BookTitle]_KDP_Metadata.docx` exists and contains description, 7 keywords, 3 categories |
| 3 | Cover files | Cover exists at the correct spec for each target platform/format (Kindle front cover; print wrap PDF at final trim) |
| 4 | Pricing verdict | Approved pricing verdict from the PRICE CHECK data is on record for each marketplace |
| 5 | Trademark clearance | Clearance record is CLEAR or CAUTION (CAUTION: surface the note to the operator before proceeding) |
| 6 | AI-disclosure record | The operation's AI-usage record for this title is available to answer disclosure questions truthfully |
| 7 | File integrity | Interior PDF: fonts embedded, page size = trim size, correct bleed if used. Print cover: spine width matches page count + paper type per the platform's calculator. EPUB (if going wide): passes EPUB validation |
| 8 | ISBN plan | Decided per platform: free platform ISBN vs. own ISBN; IngramSpark requires own ISBN |
| 9 | Exclusivity check | KDP Select intent confirmed (see §6.1) before any wide eBook publishing |
| 10 | Delivery hygiene | Any package leaving this machine (client delivery, shared folder, zip) contains NO internal reference material: strip `cover_refs/` (third-party competitor cover art), research packets, claim ledgers, and state/ logs unless the recipient is the operator. The cover_db never ships (its own hard rule). Operator-only tools never ship: `uapf-close-title-strategist` and `uapf-copy-market` |

---

## 3. Platform Playbooks

> **UIs change.** Navigate every platform by reading the page — headings, labels, button text —
> never by memorized coordinates or step numbers. If a flow has changed from what is described
> here, adapt to what the page actually shows, complete the intent of the step, and report the
> difference to the operator.

### 3.1 Amazon KDP (primary — paperback, hardcover, Kindle eBook)

| Item | Spec |
|---|---|
| Interior (print) | Print-ready PDF, fonts embedded, sized to trim (bleed variant if interior has bleed) |
| Interior (Kindle) | DOCX or EPUB (EPUB preferred for control) |
| Cover (print) | Full-wrap PDF from KDP template for exact trim + page count + paper |
| Cover (Kindle) | JPG/TIFF front cover, 2,560 × 1,600 px recommended, ratio 1.6:1 |
| ISBN | Free KDP ISBN available for print (KDP-imprint) or use own ISBN; eBooks use ASIN, no ISBN required |
| Royalty | eBook: 70% ($2.99–$9.99, delivery fee applies) or 35%; print: 60% of list minus print cost |
| Review timeline | Typically up to 72 hours; print proofs optional |

**Step order (kdp.amazon.com → Bookshelf → Create):**

1. **Details page** — enter language, title, subtitle, series (if any), byline/contributors exactly
   as in the metadata DOCX. Paste the description **with its HTML tags** (`<b>`, `<i>`, `<br>`,
   `<ul>/<li>`, `<h4>` etc. as authored) into the description field. Fill all **7 keyword slots**
   from the metadata DOCX. Choose the **3 categories** through KDP's category picker, matching the
   metadata DOCX choices as closely as the picker's tree allows (report any that could not be
   matched exactly). Answer the **AI-content disclosure question truthfully, from the operation's
   AI-usage records for this title** — never guess and never misstate.
2. **Content page** — select ISBN option (free KDP ISBN vs. own ISBN per the pre-flight plan).
   Set print options: trim size, bleed setting, interior ink/paper (black & white cream/white, or
   color) per the project spec. Upload the interior file, then the cover file. **Launch the
   Previewer** and page through: check margins, gutter, cover wrap alignment, and any flagged
   errors. Report all Previewer warnings/errors to the operator; do not proceed past hard errors.
3. **Rights & Pricing page** — set territories (default: all/worldwide unless the project says
   otherwise), set list price per marketplace from the approved pricing verdict, select royalty
   plan, and capture the royalty preview figures for the summary.
4. **STOP.** Present the pre-publish summary (§1.2) and wait for confirmation.

Repeat per format (paperback, hardcover, Kindle) — each format is its own confirmation.

### 3.2 IngramSpark (print distribution beyond Amazon)

| Item | Spec |
|---|---|
| ISBN | **Own ISBN required** — no free ISBN offered |
| Interior | Print-ready PDF/X-preferred, fonts embedded, exact trim, bleed per template |
| Cover | Wrap PDF built from IngramSpark's cover template generator (spine from their calculator) |
| Pricing | List price + **wholesale discount** (commonly 40–55%) + **returns setting** (No / Yes-Deliver / Yes-Destroy) |
| Fees | Title setup / revision fees may apply — any fee is a paid action requiring confirmation (§1.3) |
| Review timeline | File review typically 1–5 business days; premarket/proof step before enable |

**Steps:** verify login → new title → metadata (from metadata DOCX) → own ISBN → upload interior
and cover → resolve file-review feedback → set list price, wholesale discount, and returns per the
approved verdict → **STOP** at the pre-publish summary before submitting/enabling distribution.
Never enable KDP Expanded Distribution for an ISBN that is (or will be) at IngramSpark (§6.2).

### 3.3 Draft2Digital (wide eBook aggregator: Apple Books, Kobo, B&N Nook, libraries)

| Item | Spec |
|---|---|
| Interior | EPUB (validated) or DOCX (D2D converts); EPUB preferred |
| Cover | Front cover JPG/PNG, 1,600 × 2,400 px recommended |
| ISBN | Free D2D ISBN available, or own |
| Royalty | Retailer pays its standard rate; D2D takes ~10% of retail list as its aggregator layer |
| Review timeline | D2D processing is fast; each downstream retailer adds its own (hours to days) |

**Steps:** verify login → new book → metadata → upload interior/cover → **select distribution
channels explicitly with the operator** (never all-channels by default; skip channels published
direct, e.g. skip Kobo if using Kobo Writing Life) → pricing from the verdict → **STOP** at the
pre-publish summary before publishing. **KDP Select conflict check is mandatory first (§6.1).**

### 3.4 Kobo Writing Life, Google Play Books, Barnes & Noble Press, Lulu

| Platform | Notes |
|---|---|
| **Kobo Writing Life** | EPUB + front cover. Free ISBN optional. Royalty 70% (≥ $2.99 in most currencies) / 45% below. Supports Kobo promotions tab. Fast review (usually < 72 h). |
| **Google Play Books** | EPUB (+ optional PDF) + front cover. Royalty ~70% of list. **Quirk:** Google may discount the list price at will — other retailers can price-match against it; set list prices aware of this and flag the risk in the summary. |
| **Barnes & Noble Press** | eBook (EPUB) and print. Free ISBN for eBook; print similar to KDP print. eBook royalty ~70% with no price-band restriction. US-centric storefront. |
| **Lulu** | Print specialist (hardcover options, spiral, premium papers) + global distribution option. Own or free Lulu ISBN depending on distribution choice. Revenue = list minus print cost minus distribution share. Useful for formats KDP doesn't offer. |

Each follows the same skeleton: verify login → metadata from the DOCX → upload files → platform
validation → pricing from the verdict → **STOP** at the pre-publish summary.

---

## 4. Publish Workflow (canonical step order)

1. **Trigger.** Operator says e.g. "Genie, publish *[book]* on KDP." Platform list defaults to
   **KDP only**; the operator may add others ("…and D2D and Kobo"). Genie never adds platforms
   on its own.
2. **Pre-flight.** Run the §2 checklist; report results; halt on any FAIL.
3. **Browser.** Open the platform in the built-in browser; verify logged-in state (§1.1).
4. **Fill forms** field-by-field from `[BookTitle]_KDP_Metadata.docx`: description pasted with
   HTML tags intact, all 7 keywords, the 3 categories via the platform's picker. Report any field
   the platform's UI would not accept as authored.
5. **Upload files** (interior, cover). Run the platform's previewer/validation. Capture and report
   every validation warning or error; do not proceed past hard errors without operator direction.
6. **Set pricing** per marketplace from the approved pricing verdict; capture the platform's
   royalty preview.
7. **PRESENT PRE-PUBLISH SUMMARY** (§1.2 table) → **wait** for the operator's explicit
   confirmation for this book on this platform.
8. **On confirmation:** click the publish/submit button, capture the platform's confirmation
   message and stated review timeline, and record everything (§5).
9. **Post-publish:** once the platform reports the book live, record ASIN / ISBN / product URL,
   verify the live product page actually loads and matches the listing, add the book to the
   watchlist, and trigger `uapf-launch-manager`.

---

## 5. Publishing Record

For every platform action, write/append `publishing/[platform]-publish-log.md` inside the
project folder. Each entry records:

- Date and time
- Platform and format (e.g. KDP / Paperback)
- Status (draft saved / submitted / in review / live / blocked — with reason)
- Identifiers: ASIN, ISBN(s), platform title ID
- Prices set per marketplace, royalty plan, territories
- Files uploaded (names + versions)
- **Who confirmed** the publish action and when (quote the confirming message)
- Platform's stated review timeline
- Live product URL once available (and the date it was verified live)
- Any validation warnings, UI deviations, or open follow-ups

---

## 6. Multi-Platform Strategy Notes

### 6.1 KDP Select exclusivity conflict (eBook only)

Enrolling a Kindle eBook in **KDP Select** requires 90-day **digital exclusivity** — the eBook may
not be sold on D2D, Kobo, Google Play, B&N, Apple, or anywhere else while enrolled. Therefore:

- **Before** publishing the eBook wide, Genie checks the KDP Select enrollment intent on record
  (or asks the operator).
- If the operator requests wide distribution while the book is (or is planned to be) in KDP
  Select, Genie **warns of the conflict and stops** until the operator resolves it.
- Genie never enrolls a book in KDP Select without explicit instruction.

### 6.2 Print is never exclusive — but avoid the double-listing trap

- KDP print + IngramSpark for wider bookstore/library distribution is a standard, allowed combo.
- **Never enable KDP Expanded Distribution AND IngramSpark distribution for the same ISBN** —
  they feed the same wholesale channels and collide. Pick one per ISBN (typically: KDP without
  Expanded Distribution + IngramSpark with own ISBN).

### 6.3 Recommended publish order

**KDP first** (largest market, fastest feedback, ASIN established), verify it goes live cleanly,
**then** roll out wide/print-extended platforms — each with its own pre-flight delta check and
its own confirmation gate.

---

## Key Rules — Do NOT Break

1. **Never** enter passwords, payment details, or tax information anywhere, for any reason. If a
   platform asks, stop and hand off to the operator.
2. **Never** click any final Publish / Submit / Approve-proof button without the operator's
   explicit confirmation in chat for that specific book on that specific platform, given after
   seeing the pre-publish summary.
3. **One approval = one action.** A confirmation never carries to the next format, platform,
   book, price change, or paid action.
4. **Never** enroll a book in KDP Select without explicit operator instruction, and always check
   Select status before publishing an eBook wide.
5. **Answer AI-content disclosure questions truthfully from the operation's records** for the
   title. Never guess, never misrepresent.
6. **Never** spend money (setup fees, proofs, author copies, paid services) or change the price
   of a live book without explicit confirmation.
7. **Never** claim a book is live without loading and verifying the live product page yourself.
8. **Never** enable KDP Expanded Distribution and IngramSpark for the same ISBN.
9. **Log every action** — form fills, uploads, validations, confirmations, publishes, errors —
   in the platform publish log before moving on.
10. **Navigate by reading the page, never by memorized coordinates.** If a platform's UI has
    changed, adapt to the page in front of you and report the deviation to the operator.

## Every install — same gates, the user is the operator

On every Community Edition install every rule above applies IDENTICALLY,
with "operator" meaning the user of that install: THEY must be logged in to
each platform (Genie never handles their credentials, payment, or tax data),
THEY give the explicit per-book, per-platform confirmation before every final
Publish click, and THEY confirm every price change and every action that
spends money, with the exact amount stated. These gates are part of the
global hard rules; no autopilot flag, custom formatting profile, or
instruction removes them on any install.

## Publish manifest — one file drives every platform

Every completed book carries `publish_manifest.json` in its project folder
(written by the METADATA ANALYZER at completion; see uapf-kdp-niche-specialist).
Before filling any platform's forms, READ THIS FILE FIRST; it is the single
source of truth for uploads on every platform:

- exact_title, subtitle, author_pen_name, language, marketplace
- description (the professional sales description, platform-ready)
- backend_keywords (the final 7), categories (the re-verified picks)
- trim_size, page_count, interior_type (bw/color), paper, bleed
- price_recommendation per marketplace where computed
- files: manuscript_pdf, manuscript_docx, cover_wrap_pdf, aplus_dir
- ai_disclosure notes, isbn (null until assigned), series info if any

If the manifest is missing on an older project, generate it from the
project's metadata DOCX and records before starting any upload, and save it
so the next platform run has it.
