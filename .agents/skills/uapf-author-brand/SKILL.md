---
name: uapf-author-brand
description: Build compounding author-brand assets around pen names. Amazon Author Central setup per pen name, a simple landing page + email list for flagship pen names, and a TOS-compliant ARC/early-reader program for launches. Invoke on "Genie, set up the author brand for [pen name]", "author page for [pen name]", "launch team", or "ARC program", and automatically as a launch-plan step for flagship titles.
---

# UAPF Author Brand (pen names that compound)

A byline is a label; a brand is an asset. This skill turns the strongest
pen names into brands with three components, each honest to the pen-name
truthfulness rules (no fabricated credentials or biography, ever).

## 1. Amazon Author Central (per pen name, per marketplace)

Genie prepares; the operator clicks (Author Central requires the KDP
account login: operator-only by the credentials hard gate).

Genie prepares a ready-to-paste kit per pen name:
- BIO: 3 sentences, truthful by construction: describes the CATALOG's
  focus and philosophy, never invented personal history, degrees, or
  experience ("[Pen Name] writes practical renal-diet cookbooks focused
  on...", not "[Pen Name] is a dietitian with 20 years...").
- The book list to claim on the profile.
- Optional author photo policy: NO AI-generated human portrait may be
  passed off as a real person. Use a text monogram/logotype image in the
  pen name's palette instead (generate via the standard cover engine).
The kit is saved to `state/author_brand/<pen-name>/author_central_kit.md`
and the operator walks it in under authorcentral.amazon.com. Track setup
status per marketplace in the pen-name registry.

## 2. Landing page + email list (flagship pen names only)

For a pen name with 3+ published titles or an operator "flagship" flag:
- Genie generates a single-file static landing page (self-contained
  HTML, book covers, storefront links, and an email signup form) into
  `state/author_brand/<pen-name>/site/`. Palette follows the pen name's
  registered fingerprint.
- The email form posts to whichever list service the operator has (the
  operator supplies the form action/embed; Genie never creates accounts
  or handles credentials). Until then the page ships with the signup
  section present but marked inactive.
- Hosting and domain purchase are money actions: operator decides and
  pays; Genie prepares files and step-by-step deploy notes only.
- The reader magnet (a short PDF sampler or bonus chapter built from the
  catalog's own content) is generated on request to make the signup
  worth it.

## 3. ARC / early-reader program (TOS-compliant, non-negotiable rules)

Early reviews legally and safely, per Amazon's review policies:
- Free advance copies (PDF/EPUB via the operator's chosen delivery) MAY
  be offered to readers.
- NEVER in exchange for a review, NEVER for a POSITIVE review, NEVER
  with payment, gifts, rebates, or review swaps. The ask is exactly:
  "if you enjoy it, an honest review helps"; reviewing is optional and
  its content is the reader's.
- Amazon-required disclosure practices are followed as currently
  published; verify the current policy live at each launch.
- Genie maintains the reader roster in
  `state/author_brand/<pen-name>/arc_roster.json` (name/contact/notes,
  operator-supplied), drafts the invitation and launch emails for the
  operator to send, and tracks who received which title. Genie never
  sends outreach itself without explicit operator confirmation per send,
  and never fabricates roster members or claims reviews that do not
  exist.

## Launch integration

uapf-launch-manager calls this skill in launch week: ARC copies go out
(operator-confirmed) before or at publish, the Author Central kit is
verified current, and the landing page gains the new title. Results
(signups, ARC sends) are reported as actuals in checkpoint reports.

## Engines and tiers

Binds BOTH engines. Included in every Community Edition install as part of
the publishing operations layer.
