#!/usr/bin/env python3
"""
MUSIC BED - uapf-video-studio
=============================
A subtle, non-distracting ambient bed for the given duration, or a supplied
royalty-free track looped/trimmed to length with fades. Output is 48k stereo WAV.

  python music_bed.py --dur 47.5 --out bed.wav
  python music_bed.py --dur 47.5 --out bed.wav --track my_track.mp3 --volume 0.18
"""
import argparse, os
from vstudio_common import FFMPEG, run

def synth_bed(dur, out, volume=0.08):
    freqs = [110, 164.81, 220, 277.18]  # soft A-minor-ish pad
    ins = []
    for f in freqs:
        ins += ["-f", "lavfi", "-i", f"sine=frequency={f}:duration={dur}"]
    fc = (f"[0][1][2][3]amix=inputs=4:normalize=1,lowpass=f=850,tremolo=f=0.15:d=0.4,"
          f"afade=t=in:st=0:d=3,afade=t=out:st={max(0,dur-3):.2f}:d=3,volume={volume},"
          f"aresample=48000,pan=stereo|c0=c0|c1=c0[m]")
    run([FFMPEG, "-y", *ins, "-filter_complex", fc, "-map", "[m]", "-ac", "2", "-ar", "48000", out, "-loglevel", "error"])

def track_bed(track, dur, out, volume=0.18):
    fc = (f"[0:a]aresample=48000,volume={volume},afade=t=in:st=0:d=2,"
          f"afade=t=out:st={max(0,dur-2.5):.2f}:d=2.5[m]")
    run([FFMPEG, "-y", "-stream_loop", "-1", "-i", track, "-t", str(dur),
         "-filter_complex", fc, "-map", "[m]", "-ac", "2", "-ar", "48000", out, "-loglevel", "error"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dur", type=float, required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--track")
    ap.add_argument("--volume", type=float, default=None)
    a = ap.parse_args()
    if a.track and os.path.exists(a.track):
        track_bed(a.track, a.dur, a.out, a.volume if a.volume is not None else 0.18)
    else:
        synth_bed(a.dur, a.out, a.volume if a.volume is not None else 0.08)
    print("wrote", a.out)

if __name__ == "__main__":
    main()
