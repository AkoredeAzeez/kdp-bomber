#!/usr/bin/env python3
"""
VOICEOVER - uapf-video-studio
=============================
Generate scene-aligned narration for a video ad. Free neural voices via
edge-tts (online) by default; the operator's own recorded voice can be dropped
in later. Every line is em-dash-free and makes no income claims (the brief is
written by Genie under the global honesty rules; this just renders it).

  python vo_gen.py --scenes scenes.json --out vo/ --voice en-US-AndrewNeural
scenes.json: [{"id":1,"narration":"..."}, ...]  (lines with empty narration are skipped)
Writes vo/s<id>.mp3 for each and prints a JSON list of {id, mp3, seconds}.
"""
import argparse, asyncio, json, os, sys
from vstudio_common import clean_text, dur

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scenes", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--voice", default="en-US-AndrewNeural")
    ap.add_argument("--rate", default="-4%")
    a = ap.parse_args()
    try:
        import edge_tts
    except ImportError:
        sys.exit("edge-tts not installed. One-time: pip install edge-tts")
    scenes = json.load(open(a.scenes, encoding="utf-8"))
    os.makedirs(a.out, exist_ok=True)

    async def gen():
        meta = []
        for s in scenes:
            txt = clean_text(s.get("narration", ""))
            if not txt:
                continue
            mp3 = os.path.join(a.out, f"s{s['id']}.mp3")
            await edge_tts.Communicate(txt, a.voice, rate=a.rate).save(mp3)
            meta.append({"id": s["id"], "mp3": mp3, "seconds": round(dur(mp3), 3)})
        return meta

    meta = asyncio.run(gen())
    json.dump(meta, open(os.path.join(a.out, "vo_meta.json"), "w"), indent=1)
    print(json.dumps(meta, indent=1))

if __name__ == "__main__":
    main()
