#!/usr/bin/env python3
"""
AUDIO ENGINE CHOICE - uapf-audiobook
====================================
Detects which narration engines are usable on THIS computer and records the
client's per-audiobook choice. The choice locks into the book and every track
in that audiobook uses it. Mirrors the per-book image-engine chooser.

HONEST COMMERCIAL-LICENSE FLAGS: an audiobook you SELL needs an engine whose
output is licensed for commercial use. Kokoro (Apache-2.0), Piper (MIT), and
KDP Virtual Voice (Amazon's own) are commercial-safe. Edge-TTS uses Microsoft
Edge's read-aloud voices whose commercial licensing is NOT clearly granted:
offered for demos/personal use and flagged, never the silent default for a
paid title. A paid connected service (e.g. ElevenLabs) is commercial per the
client's own plan.

  python audio_engine_choose.py --detect
  python audio_engine_choose.py --project <folder> --set <engine>
  python audio_engine_choose.py --project <folder> --get
"""
import argparse, json, os, shutil, subprocess, sys

ENGINES = {
    "kokoro": {"label": "Kokoro (local, free, Apache-2.0)",
               "note": "Default. Natural multi-language voices, commercial-safe, runs on your computer, no per-word cost.",
               "commercial": "YES (Apache-2.0)", "needs": "local"},
    "piper":  {"label": "Piper (local, free, MIT)",
               "note": "Fast even without a graphics card, many voices and languages, commercial-safe.",
               "commercial": "YES (MIT)", "needs": "piper"},
    "virtualvoice": {"label": "KDP Virtual Voice (Amazon narrates in KDP)",
               "note": "Amazon's own AI voices, free with a KDP ebook, published inside KDP. No local files; you cannot upload outside audio as Virtual Voice.",
               "commercial": "YES (Amazon's, via KDP)", "needs": "none"},
    "clone":  {"label": "Voice cloning (your own voice, commercial-safe model)",
               "note": "Clone a voice from a short sample and narrate in it. A disclaimer is shown: you confirm the voice is your own or one you have permission to use; you are responsible for the rights. Uses an MIT-licensed model (Chatterbox); commercial-safe. XTTS is NOT used (non-commercial).",
               "commercial": "YES (MIT model)", "needs": "clone"},
    "paid":   {"label": "Connected premium service (e.g. ElevenLabs)",
               "note": "Premium named voices and pro voice cloning with built-in consent checks; paid per character; your own account. Confirm cost first.",
               "commercial": "YES (per your plan)", "needs": "paid"},
}

def _pip_has(mod):
    try:
        __import__(mod); return True
    except Exception:
        return False

def available():
    have = {}
    have["kokoro"] = _pip_has("kokoro_onnx") or _pip_has("kokoro") or bool(os.environ.get("KOKORO_ENDPOINT"))
    have["piper"]  = bool(shutil.which("piper")) or _pip_has("piper")
    have["clone"]  = _pip_has("chatterbox") or _pip_has("chatterbox_tts")
    have["virtualvoice"] = True   # always offerable (Amazon-side, no local install)
    have["paid"]   = True         # always offerable (operator's own connection)
    ready = {}
    for k, v in ENGINES.items():
        state = "ready" if have.get(k) else ("setup once" if k in ("kokoro","piper","clone") else "ready")
        ready[k] = state
    return ready

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--detect", action="store_true")
    ap.add_argument("--project")
    ap.add_argument("--set")
    ap.add_argument("--get", action="store_true")
    a = ap.parse_args()

    if a.set and a.project:
        if a.set not in ENGINES:
            sys.exit("unknown engine: " + a.set + " (choose from: " + ", ".join(ENGINES) + ")")
        sd = os.path.join(os.path.abspath(a.project), "state")
        os.makedirs(sd, exist_ok=True)
        json.dump({"audio_engine": a.set, "label": ENGINES[a.set]["label"],
                   "commercial": ENGINES[a.set]["commercial"]},
                  open(os.path.join(sd, "audio_engine.json"), "w", encoding="utf-8"), indent=1)
        print(f"audiobook engine locked for this book: {a.set} ({ENGINES[a.set]['label']})")
        print(f"commercial use: {ENGINES[a.set]['commercial']}")
        return

    if a.get and a.project:
        p = os.path.join(os.path.abspath(a.project), "state", "audio_engine.json")
        if os.path.exists(p):
            print(json.load(open(p, encoding="utf-8")).get("audio_engine", "not set"))
        else:
            print("not set (defaults to kokoro)")
        return

    # detect / menu
    ready = available()
    print("Choose the narration engine for this audiobook. Available on this computer:\n")
    for k, v in ENGINES.items():
        print(f"  {k:12} {v['label']:42} [{ready[k]}]")
        print(f"               {v['note']}")
        print(f"               commercial: {v['commercial']}")
    print("\nDefault if you do not choose: kokoro (free, commercial-safe, works anywhere).")
    print("Voice cloning ('clone') shows a disclaimer: you confirm the voice is your")
    print("own, or one you have permission to use. You are responsible for the rights.")

if __name__ == "__main__":
    main()
