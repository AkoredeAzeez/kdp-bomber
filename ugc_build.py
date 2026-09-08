#!/usr/bin/env python3
"""
UGC BUILDER - uapf-video-studio  (user images -> UGC-style ad)
==============================================================
The client hands Genie their own images (product shots, a selfie, screenshots).
This composes a vertical (9:16) UGC-style ad brief: their images are the hero
shots (Ken-Burns), optional stock B-roll cuts in between, a punchy hook, benefit
captions, casual first-person voiceover, and a CTA. Then it can build it.

  python ugc_build.py --images a.jpg b.jpg c.jpg \
      --product "My Reusable Bottle" --hook "I stopped buying plastic bottles" \
      --benefits "Keeps drinks cold 24h;Pays for itself in a week;Fits every cup holder" \
      --cta "Tap the link to grab yours" --stock "pouring water bottle;happy person drinking" \
      --voice en-US-JennyNeural --brand genie --out out_ugc/ --build

Honesty rules still apply: Genie only writes claims the client can stand behind.
No fabricated testimonials, no income promises. Real product, real words.
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PY = sys.executable

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--images", nargs="+", required=True)
    ap.add_argument("--product", required=True)
    ap.add_argument("--hook", required=True)
    ap.add_argument("--benefits", default="", help="semicolon-separated")
    ap.add_argument("--cta", default="Tap the link below")
    ap.add_argument("--stock", default="", help="semicolon-separated B-roll queries (optional)")
    ap.add_argument("--voice", default="en-US-JennyNeural")
    ap.add_argument("--brand", default="genie")
    ap.add_argument("--music", action="store_true")
    ap.add_argument("--out", default="out_ugc")
    ap.add_argument("--build", action="store_true")
    a = ap.parse_args()

    imgs = [os.path.abspath(p) for p in a.images if os.path.exists(p)]
    if not imgs:
        sys.exit("no valid --images found")
    benefits = [b.strip() for b in a.benefits.split(";") if b.strip()]
    stocks = [s.strip() for s in a.stock.split(";") if s.strip()]

    scenes = []
    sid = 1
    # 1) HOOK on the first user image
    scenes.append({"id": sid, "style": "caption", "kicker": "", "heading": a.hook,
                   "sub": "", "narration": a.hook + ".", "stock": imgs[0], "stock_kind": "image",
                   "min_seconds": 3, "motion": "zoom"}); sid += 1
    # 2) BENEFITS, alternating remaining user images and stock B-roll
    img_i = 1
    for k, b in enumerate(benefits):
        if stocks and k % 2 == 1:
            sc = {"id": sid, "style": "caption", "heading": b, "narration": b + ".",
                  "stock_query": stocks[(k // 2) % len(stocks)], "stock_kind": "video", "min_seconds": 3}
        else:
            img = imgs[img_i % len(imgs)]; img_i += 1
            sc = {"id": sid, "style": "caption", "heading": b, "narration": b + ".",
                  "stock": img, "stock_kind": "image", "min_seconds": 3, "motion": "zoom"}
        scenes.append(sc); sid += 1
    # 3) CTA on a user image (last)
    scenes.append({"id": sid, "style": "center", "kicker": a.product, "heading": a.cta,
                   "pill": a.cta, "narration": a.cta + ".", "stock": imgs[-1], "stock_kind": "image",
                   "min_seconds": 3, "motion": "zoom"})

    brief = {"project": "ugc_" + "".join(c for c in a.product.lower() if c.isalnum())[:16],
             "type": "ugc", "aspect": "9:16", "brand": a.brand, "voice": a.voice,
             "music": a.music, "scenes": scenes}
    os.makedirs(a.out, exist_ok=True)
    bpath = os.path.join(a.out, "brief.json")
    json.dump(brief, open(bpath, "w"), indent=1)
    print("UGC brief written ->", bpath, f"({len(scenes)} scenes, 9:16)")
    if a.build:
        subprocess.run([PY, os.path.join(HERE, "video_studio.py"), "--brief", bpath, "--out", a.out])

if __name__ == "__main__":
    main()
