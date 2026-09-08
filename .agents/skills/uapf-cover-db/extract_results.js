// Amazon search-results extractor for cover_db stocking runs.
// Run via the browser javascript tool on an amazon.com /s?k=... results page.
// Returns pipe-format lines (asin|rating|img_code|title) ready for
// stock_niche.py. Quality floor: rating >= 4.3; deduped by ASIN.
(() => {
  const out = []; const seen = new Set();
  document.querySelectorAll('div[data-asin][data-component-type="s-search-result"]').forEach(d => {
    const asin = d.getAttribute('data-asin');
    if (!asin || seen.has(asin)) return;
    const img = d.querySelector('img.s-image');
    const titleEl = d.querySelector('h2 span');
    const ratingEl = d.querySelector('[aria-label*="out of 5 stars"]');
    let rating = null;
    if (ratingEl) { const m = ratingEl.getAttribute('aria-label').match(/([\d.]+) out of 5/); if (m) rating = parseFloat(m[1]); }
    if (!img || rating === null || rating < 4.3) return;
    const m2 = img.src.match(/\/images\/I\/([^.]+)\./);
    if (!m2) return;
    seen.add(asin);
    out.push([asin, rating, m2[1], (titleEl ? titleEl.textContent.trim() : '').replace(/\|/g, ' ').slice(0, 70)].join('|'));
  });
  return out.join('\n');
})()
