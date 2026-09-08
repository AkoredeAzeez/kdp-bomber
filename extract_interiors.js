// INTERIOR CAPTURE - run on an Amazon product (dp) page.
// Collects the hi-res product gallery image URLs (best-selling activity,
// children's, and low-content books showcase interior spreads there).
// Returns JSON {asin, title, rating, imgs:[...]}; imgs[0] is usually the
// cover (interior_db.py skips it by default).
(() => {
  const out = {
    asin: (document.getElementById("ASIN") || {}).value ||
          (location.pathname.match(/\/dp\/([A-Z0-9]{10})/) || [])[1] || "",
    title: (document.getElementById("productTitle") || {}).innerText?.trim() || "",
    rating: ((document.querySelector("#acrPopover") || {}).title || "").split(" ")[0],
    imgs: []
  };
  try {
    const d = (window.ImageBlockATF && window.ImageBlockATF.data &&
               window.ImageBlockATF.data.colorImages &&
               window.ImageBlockATF.data.colorImages.initial) || [];
    d.forEach(i => out.imgs.push(i.hiRes || i.large || (i.thumb || "")));
  } catch (e) {}
  if (out.imgs.length < 2) {
    document.querySelectorAll("#altImages img, .imageThumbnail img").forEach(t => {
      const u = (t.src || "").replace(/\._[^.]*_\./, ".");
      if (u && !u.includes("sprite") && !u.includes("play-icon") &&
          !u.includes("360_icon") && !u.includes(".gif")) out.imgs.push(u);
    });
  }
  out.imgs = [...new Set(out.imgs.filter(Boolean))];
  return JSON.stringify(out);
})()
