#!/usr/bin/env python3
"""
VOICE-CLONE DISCLAIMER - uapf-audiobook
=======================================
Voice cloning puts the responsibility for rights and permission on the client,
not on Genie. Before a clone run, Genie SHOWS this disclaimer and stamps it into
the audiobook's records. It does not block the tool; it makes the client's
responsibility explicit and auditable.

  python voice_disclaimer.py show
  python voice_disclaimer.py stamp --project <folder> --ref-sample voice.wav
"""
import argparse, json, os, sys

DISCLAIMER = (
    "VOICE CLONING DISCLAIMER\n"
    "------------------------\n"
    "By using voice cloning you confirm that the voice being cloned is your own,\n"
    "or that you have the voice owner's written permission to use it. Cloning a\n"
    "person's voice without their permission may be illegal (right of publicity)\n"
    "and can violate audiobook distributor policies. You are solely responsible\n"
    "for holding the rights to any voice you clone. Genie provides the tool; the\n"
    "responsibility for consent, permission, and licensing is yours.\n"
    "Cloned narration is AI-generated and is never presented as a human read."
)

def text():
    return DISCLAIMER

def stamp(project, ref_sample):
    """Record that the disclaimer was shown for this book, for the studio's
    paper trail. Does not gate the run."""
    sd = os.path.join(os.path.abspath(project), "state")
    os.makedirs(sd, exist_ok=True)
    rec = {"voice_clone_disclaimer_shown": True,
           "ref_sample": os.path.abspath(ref_sample) if ref_sample else None,
           "disclaimer": DISCLAIMER}
    json.dump(rec, open(os.path.join(sd, "voice_clone_disclaimer.json"), "w",
                        encoding="utf-8"), indent=1)
    return rec

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("show")
    s = sub.add_parser("stamp")
    s.add_argument("--project", required=True)
    s.add_argument("--ref-sample", default=None)
    a = ap.parse_args()
    if a.cmd == "show":
        print(DISCLAIMER)
    else:
        rec = stamp(a.project, a.ref_sample)
        print("voice-clone disclaimer stamped into", a.project)

if __name__ == "__main__":
    main()
