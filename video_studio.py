#!/usr/bin/env python3
"""
VIDEO STUDIO - orchestrator (uapf-video-studio, MAX pack)
=========================================================
Turn a brief into a finished video ad: plan scene durations from the voiceover,
fetch stock video/images, render brand overlays, and assemble the master plus a
WhatsApp-sized copy. Genie writes the brief from the client's request under the
global honesty rules (no income claims, no fabrication, em-dash-free copy).

  python video_studio.py --brief brief.json --out out/           # full build
  python video_studio.py --brief brief.json --out out/ --no-fetch # stock already placed
  python video_studio.py --brief brief.json --plan-only           # durations + stock plan

brief.json (abridged):
{ "project":"acme","type":"ad","aspect":"16:9","brand":"genie",
  "voice":"en-US-AndrewNeural","music":true,
  "scenes":[ {"id":1,"style":"caption","kicker":"..","heading":"..","sub":"..",
              "narration":"..","stock_query":"typing laptop","stock_kind":"video",
              "ss":2,"min_seconds":3,"stock":null}, ... ] }
For UGC set a scene's "stock" to a user image path and "stock_kind":"image".
"""
import argparse, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
ORIENT = {"16:9": "landscape", "9:16": "portrait", "1:1": "square"}

def sh(args):
    p = subprocess.run([PY, os.path.join(HERE, args[0])] + args[1:], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.stdout: print(p.stdout.rstrip())
    return p

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brief", required=True)
    ap.add_argument("--out", default="out")
    ap.add_argument("--no-fetch", action="store_true")
    ap.add_argument("--plan-only", action="store_true")
    a = ap.parse_args()
    brief = json.load(open(a.brief, encoding="utf-8"))
    aspect = brief.get("aspect", "16:9"); brand = brief.get("brand", "genie")
    scenes = brief["scenes"]
    os.makedirs(a.out, exist_ok=True)
    vo_dir = os.path.join(a.out, "vo"); stock_dir = os.path.join(a.out, "stock")
    ov_dir = os.path.join(a.out, "overlays")

    # 1) scene specs for overlay + narration
    scenes_json = os.path.join(a.out, "scenes.json")
    json.dump(scenes, open(scenes_json, "w"), indent=1)

    # 2) voiceover (optional)
    vo_meta = {}
    if brief.get("voice"):
        sh(["vo_gen.py", "--scenes", scenes_json, "--out", vo_dir, "--voice", brief["voice"]])
        mp = os.path.join(vo_dir, "vo_meta.json")
        if os.path.exists(mp):
            vo_meta = {m["id"]: m["seconds"] for m in json.load(open(mp))}

    # 3) durations
    n = len(scenes)
    for i, s in enumerate(scenes):
        base = vo_meta.get(s["id"], 0)
        d = max(base + 0.35, s.get("min_seconds", 3)) if base else s.get("seconds", s.get("min_seconds", 4))
        if i == n - 1:
            d += 1.2  # let the end card breathe
        s["_duration"] = round(d, 2)
    total = round(sum(s["_duration"] for s in scenes), 2)
    print(f"planned {n} scenes, total {total}s")

    # 4) stock plan / fetch
    need = [s for s in scenes if not s.get("stock")]
    queries = [{"id": s["id"], "query": s.get("stock_query", ""), "kind": s.get("stock_kind", "video"),
                "orientation": ORIENT[aspect]} for s in need if s.get("stock_query")]
    qfile = os.path.join(a.out, "stock_queries.json"); json.dump(queries, open(qfile, "w"), indent=1)
    if a.plan_only:
        json.dump(scenes, open(scenes_json, "w"), indent=1)
        print("PLAN ONLY. Stock queries at", qfile)
        return
    if need and not a.no_fetch:
        p = sh(["stock_fetch.py", "--batch", qfile, "--out", stock_dir, "--orientation", ORIENT[aspect]])
        man = os.path.join(stock_dir, "stock_manifest.json")
        if os.path.exists(man):
            got = {m["id"]: m.get("file") for m in json.load(open(man)) if m.get("ok")}
            for s in scenes:
                if not s.get("stock") and s["id"] in got:
                    s["stock"] = got[s["id"]]
        missing = [s["id"] for s in scenes if not s.get("stock")]
        if missing:
            print("\nNO API KEY or misses for scenes", missing,
                  "\nGenie: harvest these via the browser (Pexels only, skip iStock), save each as",
                  f"{stock_dir}/s<id>.mp4|.jpg, then re-run with --no-fetch.")
            # emit harvest plan for Genie
            sh(["stock_fetch.py", "--batch", qfile, "--harvest-plan"])
            # try to pick up any files Genie may already have placed by convention
    # convention pickup: stock/s<id>.mp4 or .jpg
    for s in scenes:
        if not s.get("stock"):
            for ext in (".mp4", ".jpg", ".jpeg", ".png", ".mov"):
                cand = os.path.join(stock_dir, f"s{s['id']}{ext}")
                if os.path.exists(cand):
                    s["stock"] = cand; break
    unresolved = [s["id"] for s in scenes if not s.get("stock")]
    if unresolved:
        json.dump(scenes, open(scenes_json, "w"), indent=1)
        sys.exit(f"stock missing for scenes {unresolved}; place files in {stock_dir} and re-run --no-fetch")

    # 5) overlays
    sh(["overlay_gen.py", "--scenes", scenes_json, "--brand", brand, "--aspect", aspect, "--out", ov_dir])

    # 6) built scene list + assemble
    built = [{"id": s["id"], "duration": s["_duration"],
              "kind": "image" if s.get("stock_kind") == "image" or str(s.get("stock", "")).lower().endswith((".jpg", ".jpeg", ".png")) else "video",
              "stock": s["stock"], "overlay": os.path.join(ov_dir, f"s{s['id']}.png"),
              "ss": s.get("ss", 0), "motion": s.get("motion", "zoom")} for s in scenes]
    bfile = os.path.join(a.out, "scenes_built.json"); json.dump(built, open(bfile, "w"), indent=1)
    master = os.path.join(a.out, f"{brief.get('project','ad')}_{aspect.replace(':','x')}.mp4")
    args = ["assemble.py", "--built", bfile, "--aspect", aspect, "--brand", brand, "--out", master, "--whatsapp"]
    if brief.get("voice"):
        args += ["--vo", vo_dir]
    if brief.get("music"):
        args += ["--music"]
        if brief.get("track"):
            args += ["--track", brief["track"]]
    sh(args)
    print("\nVIDEO STUDIO COMPLETE ->", master)

if __name__ == "__main__":
    main()
