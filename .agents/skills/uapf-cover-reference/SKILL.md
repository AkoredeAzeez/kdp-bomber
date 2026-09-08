---
name: uapf-cover-reference
description: After a book is fully created, pick the three best-selling competitor covers for that title (ranked by Best Sellers Rank), bring them into Claude as reference images, read the shared winning pattern, and write a comprehensive, original cover prompt that embeds the finished book's exact title, subtitle, and author name(s). Runs right before the cover pipeline and before A+ visual design.
---

# UAPF Cover Reference​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

After the book is fully created, study the covers that are actually selling in this
title's market and turn their shared pattern into one comprehensive, original cover
prompt for this book. Reference only: never copy, trace, or closely imitate any
competitor cover. The No-Two-Books-Alike law, the content restrictions, and all rights
rules still apply. The output is an original design that fits the market's visual
conventions and is built to outsell them.

**BSR is the primary quality signal.** A cover that sells is a good cover, and Best
Sellers Rank (lower is better) is the closest public proxy for "this cover converts."
Rank candidates by BSR; use rating and review count as a quality floor and tie-breaker.

## When to run
- After the manuscript and `[BookTitle]_KDP_Metadata.docx` are finished, immediately
  before uapf-chatgpt-cover-pipeline (or any cover generation).
- Before designing A+ Content visuals in uapf-kdp-assets.

## Step 0 - check the cover database first (uapf-cover-db)

Before any live research, ask the per-niche cover bank for references:

    python .agents/skills/uapf-cover-db/cover_db.py pick --niche <niche> --count 3

- If it returns 2-3 covers: copy them into the book folder as
  `cover_refs/ref1.jpg`..., skip steps 2-6 below, and continue from step 7
  (read the pattern, write the prompt). Cite each ref's banked BSR/rating and
  captured date in `cover_reference_brief.md`. If every banked cover in the
  niche is older than about 6 months, prefer a live run instead and say so.
- If it returns NOT_ENOUGH_COVERS (or the operator asks for "fresh research"):
  run the live workflow below, then BANK each downloaded ref (step 6b) so the
  niche is stocked for next time.

## Workflow

1. **Read the finished book's exact text.** From `[BookTitle]_KDP_Metadata.docx` (or the
   locked metadata handoff), read the exact **title**, **subtitle**, and **author
   name(s)**. These go into the prompt verbatim, spelled and cased exactly.

2. **Set the marketplace, then search.** Set the "Deliver to" location first and never
   leave it on Nigeria: on the marketplace domain click the location control (id
   `nav-global-location-popover-link`), type a real postal code into the zip field (id
   `GLUXZipUpdateInput`), Apply, Done. Defaults: US 10001, UK SW1A 1AA, DE 10115, FR
   75001, IT 00184, ES 28001, NL 1011AA, JP 100-0001. Then open
   `https://www.amazon.com/s?k=KEYWORD&i=stripbooks` using the book's exact title
   keyword (or the operator's target search phrase), URL-encoded. On any CAPTCHA / "not a
   robot" wall, STOP and hand to the operator; never solve it.

3. **Collect candidates.** Run the COVER EXTRACTOR below on the results page to gather,
   for the top organic `/dp/` results, each book's title, product URL, cover image URL,
   rating, and review count. Parse `reviewsRaw` ("1,809 ratings") into an integer.

4. **Read BSR per candidate.** For the top ~8 comparable candidates (same niche and a
   real book cover, not a journal/notebook), open the product page and run the BSR READER
   to get the overall "Best Sellers Rank" in Books plus sub-category ranks. Keep the
   overall BSR as an integer (lower = better).

5. **Pick the BEST 3 by BSR.** Rank the comparables by overall BSR ascending and keep the
   top 3, subject to a quality floor: rating 4.3 or higher and a non-trivial review count
   (ignore a freak low-BSR title with almost no reviews). If BSR cannot be read for a
   candidate, fall back to review count for that one and say so. If fewer than 3 qualify,
   take what is available and note it. Record BSR, rating, and reviews for each pick.

6. **Download the 3 covers** at full size into the book folder under `cover_refs/` as
   `ref1.jpg`, `ref2.jpg`, `ref3.jpg` (PowerShell `Invoke-WebRequest`; Amazon image CDN
   URLs are public). Strip any size segment such as `_AC_UY327_` or `_SX..._` from the URL
   to request the largest image.

6b. **Bank the refs into the cover database** (one `cover_db.py add` per ref,
   with its real title/ASIN/BSR/rating/reviews) so future covers in this niche
   can skip live research. Never invent metadata; unknown fields stay empty.

7. **Upload the 3 covers to Claude and read the pattern.** Bring `ref1.jpg`–`ref3.jpg`
   into Claude's visual context (attach / read the image files) and look at them. Record,
   per cover, concrete observations, then derive the SHARED winning pattern across all
   three on these axes:
   - **Composition & focal hierarchy** — what the eye hits first; placement of the hero
     object/illustration; where the title sits (top, center, lower third); balance and
     negative space.
   - **Color** — dominant palette, background treatment, contrast level, accent usage.
   - **Typography** — serif vs sans, weight, case, title treatment (all-caps, stacked,
     scripted), relative size hierarchy of title / subtitle / author, any badge or ribbon.
   - **Imagery** — photographic, illustrated, graphic/abstract, or type-only; subject
     matter conventions for this niche.
   - **Mood & genre cues** — the instant signal that tells a buyer "this is that kind of
     book" (authoritative, cozy, playful, clinical, premium, etc.).

8. **Write the comprehensive cover prompt** to `cover_prompt.md` in the book folder. It
   must be a single, self-contained, generator-ready prompt that:
   - Directs an ORIGINAL cover that expresses the shared pattern from step 7 (fits the
     shelf) without copying any one reference.
   - States the concept, imagery, composition and focal hierarchy, color palette (HEX
     where useful), typography style, and mood, all drawn from the observed pattern.
   - Embeds the exact strings, spelled and cased exactly:
     - Title: **"[TITLE]"**
     - Subtitle: **"[SUBTITLE]"** (omit the line if there is no subtitle)
     - Author: **"[AUTHOR NAME(S)]"**
     with placement guidance for each derived from where winning covers in this market put
     them.
   - Adds the guardrails: original design (No-Two-Books-Alike, unique palette and
     treatment vs prior Pegasus titles), no competitor logos/trade dress, no excluded
     content or imagery, all text rendered sharply and spelled exactly.
   - Is written so it can drive either a full-wrap cover generation (front + spine + back)
     or a front-cover render; the cover pipeline supplies exact dimensions.

9. **Also write `cover_reference_brief.md`** capturing, for each of the 3 refs, its BSR,
   rating, review count, and 2 to 3 visual observations, plus the shared-pattern summary
   and 1 to 2 concrete ways this book stands out while still fitting in.

10. **Hand off.** `cover_refs/ref1.jpg`–`ref3.jpg`, `cover_prompt.md`, and
    `cover_reference_brief.md` are the inputs to uapf-chatgpt-cover-pipeline and to A+
    visual design in uapf-kdp-assets.

## Selection rule
Best = proven sales with a quality floor. Rank comparable competitor books by overall
Best Sellers Rank (lowest first), require rating 4.3 or higher and a real review count,
keep the top 3. These are the covers the market is actively buying; the new cover should
read as belonging on that shelf while being clearly its own original design.

## COVER EXTRACTOR (run on the search results page)
```javascript
(function(){var t=document.body.innerText||"";if(/Enter the characters|not a robot|Type the characters/i.test(t)&&t.length<3000)return JSON.stringify({blocked:true});var out=[];document.querySelectorAll('div[data-component-type="s-search-result"]').forEach(function(el){if(out.length>=18)return;var a=el.querySelector('h2 a, a.a-link-normal.s-no-outline');var url=a?a.href.split('?')[0]:null;if(!url||url.indexOf('/dp/')<0)return;var titleEl=el.querySelector('h2 a span, h2 span');var img=el.querySelector('img.s-image');var ratingEl=el.querySelector('.a-icon-alt');var rev=el.querySelector('a[href*="customerReviews"], span[aria-label*="ratings"], span[aria-label*="reviews"]');out.push({title:titleEl?titleEl.textContent.trim():null,url:url,cover:img?img.src:null,rating:ratingEl?parseFloat(ratingEl.textContent):null,reviewsRaw:rev?(rev.getAttribute('aria-label')||rev.textContent):''});});return JSON.stringify({blocked:false,items:out});})()
```

## BSR READER (run on each competitor's /dp/ product page)
```javascript
(function(){var txt=document.body.innerText||"";var o=txt.match(/Best Sellers Rank[:\s]*#([\d,]+)\s+in\s+Books/i);var ranks=[];var re=/#([\d,]+)\s+in\s+([^(#\n]+?)(?=\s*\(|#|\n|$)/g,m;while((m=re.exec(txt))){ranks.push({rank:parseInt(m[1].replace(/,/g,''),10),category:m[2].trim()});if(ranks.length>=6)break;}return JSON.stringify({overallBSR:o?parseInt(o[1].replace(/,/g,''),10):(ranks[0]?ranks[0].rank:null),ranks:ranks});})()
```

## Hard rules
- Reference only. Never reproduce, trace, or closely imitate any competitor cover. Produce an original design.
- No-Two-Books-Alike still governs: the new cover's design system must be unique.
- BSR is the primary ranking signal; rating and review count are the quality floor and tie-breaker.
- Only public search and product images, three of them, for design research. No bulk downloading.
- Real data only. If a step cannot read (BSR hidden, image missing), skip it and note it. Never invent a competitor, a BSR, or a cover.
- The generated cover carries the finished book's exact title, subtitle, and author name(s), spelled and cased exactly as in the locked metadata.
- `cover_prompt.md` honors the Pegasus cover house rules: photorealistic imagery only (no icons, badges, vector, or clip art), no selling-point callouts on the cover, no violence or blood, and no background base colour repeated within a five-cover window. These carry into whichever build path runs (uapf-chatgpt-cover-pipeline or uapf-cover-canva-build).
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
