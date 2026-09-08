#!/usr/bin/env python3
"""
GENIE AUDIOBOOK PREP
====================
Two jobs:
  prep    Turn a finished manuscript into a narration-clean script, split into
          chapters and TTS-sized chunks (<= 4800 chars), with a narration-QA
          report and a cost estimate. Feeds either KDP Virtual Voice review or
          an external voiceover service.
  stitch  Concatenate the generated chapter MP3s into one audiobook file.

This tool does NOT call any voiceover API. For external audio, Genie sends each
chunk to a connected voiceover service (per the uapf-audiobook skill), downloads
the MP3s here, then runs `stitch`.

Examples:
  python genie_audiobook.py prep --manuscript book.docx --out narration --title "My Book"
  python genie_audiobook.py stitch --dir narration/audio --out audiobook.mp3
"""
import argparse, json, os, re, zipfile, html, glob

CREDITS_PER_1000 = 14   # matches the connected voiceover service pricing


def _audio_ext(data, fallback="wav"):
    """Detect the real audio container from magic bytes, so files are never
    mislabeled (the Kokoro server returns WAV regardless of requested format)."""
    if data[:4] == b"RIFF": return "wav"
    if data[:3] == b"ID3" or (len(data) > 1 and data[0] == 0xFF and (data[1] & 0xE0) == 0xE0): return "mp3"
    if data[:4] == b"OggS": return "ogg"
    if data[:4] == b"fLaC": return "flac"
    return fallback


def _ffmpeg():
    import shutil
    return shutil.which("ffmpeg")


def _encode_mp3(wav_in, mp3_out):
    import subprocess
    subprocess.run([_ffmpeg(), "-y", "-i", wav_in, "-codec:a", "libmp3lame",
                    "-qscale:a", "2", mp3_out], check=True, capture_output=True)

def read_text(path):
    if path.lower().endswith(".docx"):
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf-8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        xml = re.sub(r"<[^>]+>", "", xml)
        return html.unescape(xml)
    return open(path, encoding="utf-8-sig").read()

ABBREV = [(r"\be\.g\.", "for example"), (r"\bi\.e\.", "that is"),
          (r"\betc\.", "and so on"), (r"\bvs\.", "versus"), (r"\bapprox\.", "approximately")]

def clean_line(ln):
    s = ln.strip()
    if re.fullmatch(r"\[IMG-\d+\]", s): return ""          # image placeholder
    if re.fullmatch(r"\d{1,4}", s): return ""              # bare page number
    for pat, rep in ABBREV:
        s = re.sub(pat, rep, s)
    return s

def split_chapters(text):
    lines = text.split("\n")
    chapters, cur, title = [], [], "Front matter"
    head = re.compile(r"^(#{1,2}\s+.+|chapter\s+\d+.*|introduction|conclusion|appendix.*)$", re.I)
    for ln in lines:
        s = ln.strip()
        if s and len(s) <= 60 and head.match(s):
            if cur: chapters.append((title, "\n".join(cur)))
            title = re.sub(r"^#+\s*", "", s); cur = []
        else:
            cur.append(ln)
    if cur: chapters.append((title, "\n".join(cur)))
    return chapters or [("Book", text)]

def chunk(text, limit=4800):
    parts = re.split(r"(?<=[.!?])\s+", text)
    chunks, buf = [], ""
    for p in parts:
        if not p.strip(): continue
        if len(buf) + len(p) + 1 > limit:
            if buf: chunks.append(buf.strip())
            buf = p
        else:
            buf = (buf + " " + p).strip()
    if buf.strip(): chunks.append(buf.strip())
    return chunks

def cmd_prep(a):
    raw = read_text(a.manuscript)
    # QA flags before cleaning
    flags = {"figures": len(re.findall(r"\bFigure\s+\d", raw)),
             "tables": len(re.findall(r"\bTable\s+\d", raw)),
             "image_placeholders": len(re.findall(r"\[IMG-\d+\]", raw)),
             "urls": len(re.findall(r"https?://", raw))}
    cleaned = "\n".join(filter(None, (clean_line(l) for l in raw.split("\n"))))
    chapters = split_chapters(cleaned)
    os.makedirs(a.out, exist_ok=True)
    manifest, total_chars, idx = [], 0, 0
    for ci, (title, body) in enumerate(chapters, 1):
        chs = chunk(body)
        files = []
        for c in chs:
            idx += 1; total_chars += len(c)
            fn = f"chunk_{idx:04d}.txt"
            open(os.path.join(a.out, fn), "w", encoding="utf-8").write(c)
            files.append(fn)
        manifest.append({"chapter": ci, "title": title.strip()[:80], "chunks": files})
    json.dump({"title": a.title or os.path.basename(a.manuscript), "chapters": manifest,
               "total_chars": total_chars}, open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8"), indent=2)
    credits = -(-total_chars // 1000) * CREDITS_PER_1000
    mins = total_chars / 1000 * 1.1   # ~ rough narration minutes
    print(f"Prepared {len(chapters)} chapters, {idx} TTS chunks, {total_chars:,} chars.")
    print(f"External-audio cost estimate: ~{credits:,} credits; ~{mins:.0f} min of audio.")
    print(f"Narration QA flags (read poorly aloud): {flags}")
    print(f"Wrote {a.out}/manifest.json and {idx} chunk files.")

def cmd_synth(a):
    """Synthesize every chunk with the chosen engine. Default kokoro (via an
    OpenAI-compatible endpoint; Apache-2.0, free, no per-character cost).
    --engine piper or edge routes to the local/online adapters instead."""
    man = json.load(open(os.path.join(a.dir, "manifest.json"), encoding="utf-8"))
    order = [fn for ch in man["chapters"] for fn in ch["chunks"]]
    audio_dir = os.path.join(a.dir, "audio"); os.makedirs(audio_dir, exist_ok=True)

    engine = getattr(a, "engine", None) or "kokoro"
    if engine in ("piper", "edge", "clone"):
        import importlib.util, os as _os
        here = _os.path.dirname(_os.path.abspath(__file__))

        ref_sample = None
        if engine == "clone":
            # DISCLAIMER (not a gate): the client is responsible for holding the
            # rights to the voice they clone. Genie shows the disclaimer and
            # stamps it into the book's records, then proceeds. Binds both engines.
            ref_sample = getattr(a, "ref_sample", None)
            if not ref_sample or not _os.path.exists(ref_sample):
                sys.exit("Voice cloning needs a reference voice sample: "
                         "--ref-sample path\\to\\voice.wav")
            project = getattr(a, "project", None) or _os.path.dirname(_os.path.abspath(a.dir))
            vspec = importlib.util.spec_from_file_location(
                "voice_disclaimer", _os.path.join(here, "voice_disclaimer.py"))
            vd = importlib.util.module_from_spec(vspec); vspec.loader.exec_module(vd)
            print(vd.text())
            vd.stamp(project, ref_sample)

        spec = importlib.util.spec_from_file_location(
            "audio_engines", _os.path.join(here, "audio_engines.py"))
        ae = importlib.util.module_from_spec(spec); spec.loader.exec_module(ae)
        say = ae.ADAPTERS[engine]
        done = 0
        for i, fn in enumerate(order, 1):
            text = open(os.path.join(a.dir, fn), encoding="utf-8").read()
            out = os.path.join(audio_dir, f"{i:04d}.wav")
            if engine == "clone":
                say(text, a.voice, out, ref_sample=ref_sample)
            else:
                say(text, a.voice, out)
            done += 1
            print(f"  chunk {i}/{len(order)} -> {out} ({os.path.getsize(out)//1024} KB) [{engine}]")
        if engine == "edge":
            note = "commercial license UNCLEAR (Edge-TTS): do not sell without a Microsoft license"
        elif engine == "clone":
            note = "commercial-safe (MIT model); consented voice only"
        else:
            note = "commercial-safe (MIT)"
        print(f"Synthesized {done}/{len(order)} chunks via {engine}. {note}. Next: stitch, then wavcheck.")
        return

    import urllib.request
    url = a.endpoint.rstrip("/") + "/audio/speech"
    done = 0
    for i, fn in enumerate(order, 1):
        text = open(os.path.join(a.dir, fn), encoding="utf-8").read()
        body = json.dumps({"model": a.model, "input": text, "voice": a.voice,
                           "response_format": a.format,
                           **({"lang": a.lang} if getattr(a, "lang", None) else {})}).encode()
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
        try:
            data = urllib.request.urlopen(req, timeout=180).read()
        except Exception as e:
            print(f"  chunk {i}: FAILED ({e}). Is a Kokoro endpoint running at {a.endpoint}?")
            return
        ext = _audio_ext(data, a.format)   # trust the bytes, not the request
        out = os.path.join(audio_dir, f"{i:04d}.{ext}")
        open(out, "wb").write(data); done += 1
        print(f"  chunk {i}/{len(order)} -> {out} ({len(data)//1024} KB)")
    print(f"Synthesized {done}/{len(order)} chunks into {audio_dir}. No credits used. Next: stitch.")

def cmd_stitch(a):
    wavs = sorted(glob.glob(os.path.join(a.dir, "*.wav")))
    mp3s = sorted(glob.glob(os.path.join(a.dir, "*.mp3")))
    if not wavs and not mp3s:
        print("No .wav or .mp3 chunks found in", a.dir); return

    # WAV path (local Kokoro backend): concatenate PCM under a SINGLE header.
    # Raw byte-concatenation of WAV files is invalid (a header lands mid-stream).
    if wavs:
        import soundfile as sf
        import numpy as np
        sr0, parts, skipped = None, [], 0
        for f in wavs:
            data, sr = sf.read(f, dtype="int16")
            if sr0 is None:
                sr0 = sr
            elif sr != sr0:
                print(f"  WARNING: {os.path.basename(f)} is {sr} Hz (expected {sr0}); skipped")
                skipped += 1
                continue
            parts.append(data)
        if not parts:
            print("No usable WAV chunks."); return
        combined = np.concatenate(parts)
        wav_out = os.path.splitext(a.out)[0] + ".wav"
        sf.write(wav_out, combined, sr0, subtype="PCM_16")
        dur = len(combined) / sr0
        print(f"Stitched {len(parts)} WAV chunks -> {wav_out} "
              f"({os.path.getsize(wav_out)//1024} KB, {dur/60:.1f} min)"
              + (f", {skipped} skipped" if skipped else "") + ".")
        # Optional MP3 if requested and ffmpeg is available.
        if a.out.lower().endswith(".mp3"):
            if _ffmpeg():
                _encode_mp3(wav_out, a.out)
                print(f"Encoded MP3 -> {a.out} ({os.path.getsize(a.out)//1024} KB).")
            else:
                print("ffmpeg not found; kept WAV. Install ffmpeg to also get an MP3.")
        return

    # MP3 path (external voiceover service): frame concatenation plays fine.
    out_path = os.path.splitext(a.out)[0] + ".mp3"
    with open(out_path, "wb") as out:
        for f in mp3s:
            out.write(open(f, "rb").read())
    print(f"Stitched {len(mp3s)} MP3s -> {out_path} ({os.path.getsize(out_path)//1024} KB). "
          "For clean chapter markers/metadata, re-encode with ffmpeg if available.")


def cmd_wavcheck(a):
    """Validate WAV deliverables against distributor requirements:
    PCM 0x0001 (never 0xFFFE extensible), valid fmt+data subchunks,
    nothing after the data subchunk, and a full-track duration."""
    import struct
    failures = []
    for path in sorted(glob.glob(a.files)):
        raw = open(path, "rb").read()
        probs = []
        if raw[:4] != b"RIFF" or raw[8:12] != b"WAVE":
            probs.append("not a RIFF/WAVE file")
        else:
            pos, fmt_code, data_end, has_fmt, has_data, sr, ch, bits = 12, None, None, False, False, 0, 0, 0
            while pos + 8 <= len(raw):
                cid = raw[pos:pos+4]; size = struct.unpack("<I", raw[pos+4:pos+8])[0]
                if cid == b"fmt ":
                    has_fmt = True
                    fmt_code = struct.unpack("<H", raw[pos+8:pos+10])[0]
                    ch = struct.unpack("<H", raw[pos+10:pos+12])[0]
                    sr = struct.unpack("<I", raw[pos+12:pos+16])[0]
                    bits = struct.unpack("<H", raw[pos+22:pos+24])[0]
                if cid == b"data":
                    has_data = True; data_end = pos + 8 + size; data_size = size
                pos += 8 + size + (size % 2)
            if fmt_code == 0xFFFE: probs.append("WAVE_FORMAT_EXTENSIBLE (0xFFFE) not accepted")
            elif fmt_code != 1: probs.append(f"format code 0x{fmt_code:04X}, need 0x0001 PCM")
            if not has_fmt: probs.append("missing fmt subchunk")
            if not has_data: probs.append("missing data subchunk")
            if has_data and len(raw) - data_end > 0:
                probs.append(f"{len(raw)-data_end} bytes after data subchunk")
            if has_data and has_fmt and sr and ch and bits:
                dur = data_size / (sr * ch * (bits // 8))
                if dur < float(a.min_minutes) * 60:
                    probs.append(f"only {dur/60:.1f} min: full tracks only, no sample clips")
        tag = "PASS" if not probs else "FAIL"
        print(f"[{tag}] {os.path.basename(path)}" + ("" if not probs else "  - " + "; ".join(probs)))
        if probs: failures.append(path)
    if failures:
        print(f"{len(failures)} file(s) non-compliant. Fix: re-render through stitch "
              "(sf.write PCM_16 mono/stereo produces canonical 0x0001 fmt+data only).")
        raise SystemExit(1)
    print("All WAV deliverables compliant (PCM 0x0001, clean fmt+data, full tracks).")


def cmd_flac(a):
    """Convert WAV deliverables to FLAC (Free Lossless Audio Codec),
    bit-exact: samples are compared after encoding and any mismatch fails
    the conversion. Keeps the WAV unless --replace is given."""
    import numpy as np, soundfile as sf
    files = sorted(glob.glob(a.files))
    if not files:
        print("no files match", a.files); return
    for path in files:
        data, sr = sf.read(path, dtype="int16")
        out = os.path.splitext(path)[0] + ".flac"
        sf.write(out, data, sr, format="FLAC", subtype="PCM_16")
        back, sr2 = sf.read(out, dtype="int16")
        ok = sr == sr2 and data.shape == back.shape and bool((data == back).all())
        print(f"[{'OK' if ok else 'FAIL'}] {os.path.basename(out)} "
              f"({os.path.getsize(out)//1024} KB, lossless verified: {ok})")
        if not ok:
            os.remove(out); raise SystemExit(f"lossless verification failed for {path}")
        if a.replace:
            os.remove(path)

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prep"); p.add_argument("--manuscript", required=True)
    p.add_argument("--out", default="narration"); p.add_argument("--title"); p.set_defaults(fn=cmd_prep)
    p = sub.add_parser("synth"); p.add_argument("--dir", required=True)
    p.add_argument("--engine", default="kokoro", choices=["kokoro", "piper", "edge", "clone"],
                   help="narration engine (client choice; kokoro default). 'clone' shows the voice disclaimer.")
    p.add_argument("--project", default=None, help="project folder (for the clone disclaimer record)")
    p.add_argument("--ref-sample", dest="ref_sample", default=None,
                   help="reference voice WAV to clone (required for --engine clone)")
    p.add_argument("--endpoint", default="http://localhost:8880/v1", help="OpenAI-compatible TTS base URL (Kokoro only)")
    p.add_argument("--voice", default="af_bella"); p.add_argument("--model", default="kokoro")
    p.add_argument("--format", default="wav")
    p.add_argument("--lang", default=None, help="override language (defaults to the voice pack's language)")
    p.set_defaults(fn=cmd_synth)
    p = sub.add_parser("stitch"); p.add_argument("--dir", required=True)
    p.add_argument("--out", default="audiobook.wav"); p.set_defaults(fn=cmd_stitch)
    p = sub.add_parser("wavcheck", help="validate WAV deliverables for distributors")
    p.add_argument("--files", required=True, help="glob, e.g. narration/*.wav")
    p.add_argument("--min-minutes", default="1", help="full-track floor in minutes")
    p.set_defaults(fn=cmd_wavcheck)
    p = sub.add_parser("flac", help="convert WAV deliverables to FLAC, lossless-verified")
    p.add_argument("--files", required=True, help="glob, e.g. narration/*.wav")
    p.add_argument("--replace", action="store_true", help="delete the WAV after verified conversion")
    p.set_defaults(fn=cmd_flac)
    a = ap.parse_args(); a.fn(a)

if __name__ == "__main__":
    main()
