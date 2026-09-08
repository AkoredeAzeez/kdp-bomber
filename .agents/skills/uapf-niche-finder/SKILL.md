---
name: uapf-niche-finder
description: KDP niche and keyword opportunity research. Reads the top real Amazon competitors for a keyword (BSR, reviews, rating, price, age, publisher) on demand and renders a report with a 0-100 Opportunity score and a Go / Caution / Avoid verdict. Use before locking a title or when the operator asks whether a niche is worth publishing into.
---

# UAPF Niche Finder​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Turn a keyword into a market report from REAL Amazon data, read on demand. Never invent numbers. If the data for a book cannot be read, skip it and say so.

## When to run
- The operator asks whether a niche or keyword is worth publishing into, or asks to compare niches.
- Before locking a title, to confirm real demand and beatable competition.

## Data rules (hard)
- Real data only. Sales and royalty figures are heuristic ESTIMATES from BSR and price; always label them as estimates, never as exact Amazon figures.
- On-demand, small-scale reads only: the top ~15 results for the one keyword being evaluated. Never build or run a bulk crawler.
- If Amazon shows a CAPTCHA or a "not a robot" wall, STOP. Never attempt to solve it. Tell the operator and let them continue in their own browser.
- Set the delivery location to the target marketplace (see the next section) so prices are in that market's currency, not the browser default. Never leave the location on Nigeria. BSR is marketplace-wide and valid regardless.

## Set the marketplace location (do this FIRST, never leave it on Nigeria)
Before reading any Amazon data, set the delivery location to the marketplace you are researching, so prices, availability, and results reflect that market and not the browser's default region.
1. Use the marketplace's own domain: US amazon.com, UK amazon.co.uk, DE amazon.de, FR amazon.fr, IT amazon.it, ES amazon.es, NL amazon.nl, JP amazon.co.jp, CA amazon.ca, AU amazon.com.au.
2. Click the "Deliver to" control near the top left (element id nav-global-location-popover-link, or the glow-ingress-block area). In the popup, type a real postal code for that country into the zip field (id GLUXZipUpdateInput), click Apply, then Done.
3. Default postal codes: US 10001, UK SW1A 1AA, DE 10115, FR 75001, IT 00184, ES 28001, NL 1011AA, JP 100-0001, CA M5V 3L9, AU 2000.
4. Verify it took: the "Deliver to" now shows that country and prices are in that market's currency, not NGN. If prices still show NGN or the location still reads Nigeria, the change did not apply; retry before trusting any price.
Do this once per marketplace at the start of the session, before extraction.

## Workflow
1. Get the keyword from the operator.
2. Open the Amazon books search: https://www.amazon.com/s?k=KEYWORD&i=stripbooks (URL-encode the keyword).
2b. Set the marketplace location (see the section above) before extracting. Do not read prices until the "Deliver to" shows that market and prices are in its currency, not NGN.
3. Extract the top results with the SEARCH EXTRACTOR below. Keep only organic results whose URL contains /dp/ (skip sponsored /sspa/ rows) and dedupe by ASIN. Aim for the top 12 to 15.
4. For each kept result, open its product page and read BSR, publication date, price, and the indie flag with the PRODUCT EXTRACTOR below. If it returns null on the first load, wait 2 to 3 seconds and read once more before giving up. Skip any book that still will not read, and record how many were skipped.
5. Compute age_days from the publication date (today minus the publication date).
6. Write the collected books to books.json as a list of objects with these fields: title, bsr, reviews, rating, price, age_days, publisher ("Independent" or "Traditional").
7. Render the report:
   python genie_niche_finder.py --keyword "KEYWORD" --data books.json --out niche_report.html
8. Present to the operator: the Opportunity score, the verdict (Go / Caution / Avoid), the median sales and median reviews, and one line on where the openings are (for example "top locked by 1800-plus review leaders, but recent indie titles rank on a few hundred reviews lower down"). Give the path to niche_report.html, and note how many books were skipped and the marketplace region.

## Interpreting the score
- Opportunity = 50 percent demand (median estimated sales) plus 50 percent competition-ease (fewer median reviews and more indie winners).
- GO (65 and up): real demand, beatable competition. CAUTION (45 to 64): mixed, look for a sub-angle. AVOID (below 45): entrenched or thin.
- Calibrate est_monthly_sales in genie_niche_finder.py to the category over time; the default curve is a rough public heuristic, not an exact figure.

## SEARCH EXTRACTOR (run in the search results page)
```javascript
(function(){var t=document.body.innerText||"";if(/Enter the characters|not a robot|Type the characters/i.test(t)&&t.length<3000)return JSON.stringify({blocked:true});var out=[];document.querySelectorAll('div[data-component-type="s-search-result"]').forEach(function(el){if(out.length>=18)return;var a=el.querySelector('h2 a, a.a-link-normal.s-no-outline');var titleEl=el.querySelector('h2 a span, h2 span');var ratingEl=el.querySelector('.a-icon-alt');var rev=el.querySelector('a[href*="customerReviews"], span[aria-label*="ratings"], span[aria-label*="reviews"]');out.push({title:titleEl?titleEl.textContent.trim():null,url:a?a.href.split('?')[0]:null,rating:ratingEl?parseFloat(ratingEl.textContent):null,reviewsRaw:rev?(rev.getAttribute('aria-label')||rev.textContent):''});});return JSON.stringify({blocked:false,items:out});})()
```
Parse reviewsRaw such as "1,809 ratings" into an integer.

## PRODUCT EXTRACTOR (run in each product page)
```javascript
(function(){var t=document.body.innerText||"";if(/Enter the characters|not a robot|Type the characters/i.test(t)&&t.length<3000)return JSON.stringify({blocked:true});var mB=t.match(/#([\d,]+)\s+in\s+Books/i);var mD=t.match(/Publication date\s*:?\s*([A-Za-z]+ \d{1,2}, \d{4})/)||t.match(/\(([A-Za-z]+ \d{1,2}, \d{4})\)/);var pe=document.querySelector('.a-price .a-offscreen');return JSON.stringify({bsr:mB?parseInt(mB[1].replace(/,/g,'')):null,date:mD?mD[1]:null,price:pe?pe.textContent.trim():null,indie:/Independently published/i.test(t)});})()
```
Use price only if it is in USD. If it carries another currency symbol or code, treat the price as unknown.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
