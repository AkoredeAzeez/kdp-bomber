#!/usr/bin/env python3
"""
AUDIO ENGINE ADAPTERS - uapf-audiobook
======================================
Unified narration across engines so genie_audiobook.py synth can drive the
engine the client chose. Each adapter turns one text chunk into one WAV file.
Kokoro keeps its OpenAI-compatible-endpoint path in genie_audiobook.py; this
module adds Piper (local, MIT) and Edge-TTS (online, free). Output is always
canonical PCM WAV so wavcheck and FLAC conversion work unchanged.

  python audio_engines.py list
  python audio_engines.py say --engine piper --voice en_US-amy-medium \\
         --text "Hello." --out test.wav
"""
import argparse, os, subprocess, sys, tempfile

def piper_say(text, voice, out):
    """Piper CLI or python module. voice is a model name/path; piper resolves it."""
    exe = None
    from shutil import which
    if which("piper"):
        exe = ["piper"]
    else:
        try:
            import piper  # noqa
            exe = [sys.executable, "-m", "piper"]
        except ImportError:
            sys.exit("Piper not installed. One-time: pip install piper-tts")
    cmd = exe + ["--model", voice, "--output_file", out]
    p = subprocess.run(cmd, input=text.encode("utf-8"), capture_output=True)
    if p.returncode != 0 or not os.path.exists(out):
        sys.exit("Piper failed: " + (p.stderr.decode("utf-8", "replace")[:200]))
    return out

def edge_say(text, voice, out):
    """Edge-TTS: free Microsoft neural voices. Commercial license is UNCLEAR;
    caller must have gated this for sold titles."""
    try:
        import edge_tts
    except ImportError:
        sys.exit("Edge-TTS not installed. One-time: pip install edge-tts")
    import asyncio
    mp3 = out[:-4] + ".mp3" if out.lower().endswith(".wav") else out + ".mp3"
    async def run():
        await edge_tts.Communicate(text, voice or "en-US-AriaNeural").save(mp3)
    asyncio.run(run())
    # convert mp3 -> canonical WAV via soundfile+librosa or ffmpeg
    if out.lower().endswith(".wav"):
        try:
            import soundfile as sf, numpy as np, librosa
            data, sr = librosa.load(mp3, sr=22050, mono=True)
            sf.write(out, (data * 32767).astype("int16"), sr, subtype="PCM_16")
            os.remove(mp3)
        except Exception:
            # fallback: ffmpeg if present
            from shutil import which
            if which("ffmpeg"):
                subprocess.run(["ffmpeg", "-y", "-i", mp3, "-ar", "22050", "-ac", "1",
                                "-sample_fmt", "s16", out], capture_output=True)
                os.remove(mp3)
            else:
                sys.exit("need soundfile+librosa or ffmpeg to make WAV from Edge-TTS mp3")
    return out

def clone_say(text, voice, out, ref_sample=None):
    """Voice cloning with a commercial-safe MIT model (Chatterbox by Resemble AI).
    `ref_sample` is a short WAV of the voice being cloned. XTTS is deliberately
    NOT used: its model license is non-commercial. The caller (genie_audiobook
    synth) shows the voice-clone disclaimer and records it before this runs; the
    client is responsible for holding the rights to the voice.
    Output is canonical PCM WAV so wavcheck/FLAC work unchanged."""
    if not ref_sample or not os.path.exists(ref_sample):
        sys.exit("clone needs a reference sample WAV (--ref-sample).")
    try:
        from chatterbox.tts import ChatterboxTTS
    except Exception:
        try:
            from chatterbox_tts import ChatterboxTTS  # alt package name
        except Exception:
            sys.exit("Voice cloning model not installed. One-time: pip install chatterbox-tts")
    import torch, soundfile as sf
    model = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
    wav = model.generate(text, audio_prompt_path=ref_sample)
    arr = wav.squeeze(0).cpu().numpy() if hasattr(wav, "cpu") else wav
    sf.write(out, arr, getattr(model, "sr", 24000), subtype="PCM_16")
    if not os.path.exists(out):
        sys.exit("clone failed to write output.")
    return out

ADAPTERS = {"piper": piper_say, "edge": edge_say, "clone": clone_say}

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    s = sub.add_parser("say")
    s.add_argument("--engine", required=True, choices=list(ADAPTERS))
    s.add_argument("--voice", default="")
    s.add_argument("--text", required=True)
    s.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.cmd == "list":
        print("adapters here: piper (MIT, commercial-safe), edge (free, commercial UNCLEAR).")
        print("kokoro is driven via its endpoint in genie_audiobook.py synth;")
        print("virtualvoice and paid services are handled per the skill, not here.")
        return
    ADAPTERS[a.engine](a.text, a.voice, a.out)
    print(f"wrote {a.out} ({os.path.getsize(a.out)//1024} KB) via {a.engine}")

if __name__ == "__main__":
    main()
