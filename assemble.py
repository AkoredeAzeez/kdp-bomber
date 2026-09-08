#!/usr/bin/env python3
"""
ASSEMBLE - uapf-video-studio
============================
Composite every scene (stock video/image + brand overlay), build the narration
track and music bed, and render the master plus WhatsApp-sized exports.

  python assemble.py --built scenes_built.json --vo vo/ --aspect 16:9 \
      --brand genie --out ad.mp4 --music --whatsapp --parts

scenes_built.json: [{"id":1,"duration":8.7,"kind":"video|image","stock":"a/s1.mp4",
                     "overlay":"o/s1.png","ss":2,"motion":"zoom|none"}, ...]
"""
import argparse, json, os, subprocess
from vstudio_common import FFMPEG, run, dur

SIZES = {"16:9": (1920, 1080), "9:16": (1080, 1920), "1:1": (1080, 1080)}

def scene_clip(s, size, out):
    W, H = size; d = s["duration"]
    ov = s.get("overlay")
    if s["kind"] == "video":
        bg = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"fps=30,unsharp=3:3:0.5,eq=brightness=-0.02,setsar=1[bg]")
        ins = ["-stream_loop", "-1", "-ss", str(s.get("ss", 0)), "-i", s["stock"]]
    else:  # image: Ken-Burns
        frames = int(round(d*30)); z = 0.06
        bg = (f"[0:v]scale={int(W*2)}:{int(H*2)}:force_original_aspect_ratio=increase,crop={int(W*2)}:{int(H*2)},"
              f"zoompan=z='min(1.001+on/{frames}*{z},{round(1+z,4)})':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
              f"s={W}x{H}:fps=30,trim=duration={d},setsar=1[bg]")
        ins = ["-framerate", "30", "-loop", "1", "-t", str(d), "-i", s["stock"]]
    if ov:
        fc = bg + ";[1:v]null[o];[bg][o]overlay=0:0,format=yuv420p[v]"
        ins += ["-framerate", "30", "-loop", "1", "-t", str(d), "-i", ov]
    else:
        fc = bg + ";[bg]format=yuv420p[v]"
    run([FFMPEG, "-y", *ins, "-filter_complex", fc, "-map", "[v]", "-t", str(d),
         "-r", "30", "-c:v", "libx264", "-preset", "medium", "-crf", "20", out, "-loglevel", "error"])

def build_audio(scenes, vo_dir, tmp, total, music, track):
    # narration padded per-scene so speech aligns to scene starts
    parts = []
    for s in scenes:
        mp3 = os.path.join(vo_dir, f"s{s['id']}.mp3")
        w = os.path.join(tmp, f"n{s['id']}.wav")
        if os.path.exists(mp3):
            run([FFMPEG, "-y", "-i", mp3, "-af", "aresample=48000,apad", "-t", str(s["duration"]),
                 "-ac", "2", "-ar", "48000", w, "-loglevel", "error"])
        else:
            run([FFMPEG, "-y", "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo", "-t", str(s["duration"]),
                 w, "-loglevel", "error"])
        parts.append(w)
    lst = os.path.join(tmp, "nlist.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    narration = os.path.join(tmp, "narration.wav")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", narration, "-loglevel", "error"])
    if not music:
        return narration
    bed = os.path.join(tmp, "bed.wav")
    import music_bed
    if track and os.path.exists(track):
        music_bed.track_bed(track, total, bed)
    else:
        music_bed.synth_bed(total, bed)
    mix = os.path.join(tmp, "mix.wav")
    run([FFMPEG, "-y", "-i", narration, "-i", bed, "-filter_complex",
         "[0:a]volume=1.05[v];[1:a]volume=1.0[b];[v][b]amix=inputs=2:duration=first:dropout_transition=0[a]",
         "-map", "[a]", "-ac", "2", "-ar", "48000", mix, "-loglevel", "error"])
    return mix

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--built", required=True)
    ap.add_argument("--vo", default="")
    ap.add_argument("--aspect", default="16:9", choices=list(SIZES))
    ap.add_argument("--brand", default="genie")
    ap.add_argument("--out", required=True)
    ap.add_argument("--music", action="store_true")
    ap.add_argument("--track", default="")
    ap.add_argument("--whatsapp", action="store_true", help="also write a <9MB copy next to out")
    ap.add_argument("--parts", action="store_true", help="also cut scene-group parts")
    a = ap.parse_args()
    size = SIZES[a.aspect]
    scenes = json.load(open(a.built, encoding="utf-8"))
    tmp = os.path.join(os.path.dirname(os.path.abspath(a.out)), "_vstudio_tmp")
    os.makedirs(tmp, exist_ok=True)
    clips = []
    for s in scenes:
        c = os.path.join(tmp, f"c{s['id']}.mp4")
        scene_clip(s, size, c); clips.append(c)
        print("scene", s["id"], "ok")
    vlist = os.path.join(tmp, "vlist.txt")
    open(vlist, "w").write("".join(f"file '{c}'\n" for c in clips))
    silent = os.path.join(tmp, "silent.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", vlist, "-c", "copy", silent, "-loglevel", "error"])
    total = dur(silent)
    audio = build_audio(scenes, a.vo, tmp, total, a.music, a.track) if a.vo else None
    if audio:
        run([FFMPEG, "-y", "-i", silent, "-i", audio, "-map", "0:v:0", "-map", "1:a:0",
             "-c:v", "libx264", "-preset", "slow", "-crf", "20", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", a.out, "-loglevel", "error"])
    else:
        run([FFMPEG, "-y", "-i", silent, "-c:v", "libx264", "-preset", "slow", "-crf", "20",
             "-pix_fmt", "yuv420p", "-movflags", "+faststart", a.out, "-loglevel", "error"])
    print("MASTER", a.out, round(dur(a.out), 1), "s")

    if a.whatsapp:
        base = os.path.splitext(a.out)[0]
        nine = base + "_9MB.mp4"
        vd = dur(a.out); vw = 1280 if size[0] >= size[1] else 720; vh = 720 if size[0] >= size[1] else 1280
        vbit = max(300, int((8.6*8192)/max(1, vd) - 96))
        log = os.path.join(tmp, "2pass")
        run([FFMPEG, "-y", "-i", a.out, "-vf", f"scale={vw}:{vh}:flags=lanczos", "-c:v", "libx264",
             "-b:v", f"{vbit}k", "-pass", "1", "-passlogfile", log, "-an", "-preset", "medium", "-f", "mp4",
             os.devnull, "-loglevel", "error"])
        run([FFMPEG, "-y", "-i", a.out, "-vf", f"scale={vw}:{vh}:flags=lanczos", "-c:v", "libx264",
             "-b:v", f"{vbit}k", "-pass", "2", "-passlogfile", log, "-preset", "medium", "-c:a", "aac",
             "-b:a", "96k", "-movflags", "+faststart", nine, "-loglevel", "error"])
        print("WHATSAPP", nine, round(os.path.getsize(nine)/1048576, 2), "MB")
    print("DONE")

if __name__ == "__main__":
    main()
