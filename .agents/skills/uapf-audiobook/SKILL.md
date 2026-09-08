---
name: uapf-audiobook
description: Prepare a finished book for audio. Two paths: KDP Virtual Voice review so Amazon's in-KDP AI narration reads cleanly, and full audiobook generation via a connected voiceover service (real MP3s) for distribution outside Amazon. Use when the operator wants an audiobook or a Virtual Voice edition.
---

# UAPF Audiobook

Two separate roads. Confirm which one the operator wants before doing anything.

## Road 1: KDP Virtual Voice (Amazon narrates)
Amazon generates the narration inside KDP using Amazon's own AI voices. You cannot upload outside audio for Virtual Voice. Genie's job is to make sure the published ebook reads well when Amazon narrates it.
1. Run the narration QA: python genie_audiobook.py prep --manuscript book.docx --out narration --title "TITLE". Read the QA flags (figures, tables, image placeholders, URLs); these read poorly aloud.
2. Advise the operator on ebook fixes so Virtual Voice sounds right: describe or remove figure and table references that only make sense visually, spell out symbols and unusual abbreviations, and confirm a clean linear reading order. Virtual Voice skips images, so anything essential in an image must also be in the text.
3. The operator enables Virtual Voice in KDP (Bookshelf, the ebook, Virtual Voice), picks an Amazon voice, previews, and publishes. Genie never publishes; per-book operator confirmation always.

## Choose your narration engine (client choice, per audiobook)

Clients pick the narration engine at the start of each audiobook, exactly like
the per-book image engine. At intake run:

    python .agents/skills/uapf-audiobook/audio_engine_choose.py --detect

to show the engines usable on this machine, then lock the pick with
`--project <folder> --set <engine>` (stored in state/audio_engine.json; every
track uses it). Default is `kokoro` when the client does not choose.

| Engine | Local? | Free? | Commercial license | Best for |
|---|---|---|---|---|
| kokoro | yes | yes | **YES (Apache-2.0)** | Default. Natural multi-language, commercial-safe. |
| piper | yes | yes | **YES (MIT)** | Fast without a GPU; many voices/languages. |
| virtualvoice | Amazon | yes w/ KDP | **YES (Amazon's, via KDP)** | In-KDP ebook narration (Road 1). |
| clone | yes | yes | **YES (MIT model)** | Narrate in the client's OWN voice (or a voice they have permission to use); disclaimer shown. |
| paid | online | paid | **YES (per your plan)** | Premium named voices + pro cloning w/ built-in consent (ElevenLabs etc.); confirm cost first. |

COMMERCIAL-LICENSE LAW: an audiobook the client SELLS must use a
commercial-safe engine. kokoro, piper, virtualvoice, and the consent-gated
clone engine (MIT model) are all safe. The engine's output still passes
wavcheck and, where required, FLAC conversion. Edge-TTS is deliberately NOT in
the roster (its read-aloud voices are not clearly licensed for sold titles); an
adapter exists for previews/personal use only and is never offered as a
narration choice for a book the client sells.

Generation routes through the chosen engine automatically:
`genie_audiobook.py synth --engine <kokoro|piper|clone> ...` (kokoro via its
endpoint; piper/clone via audio_engines.py adapters). Virtual Voice is Road 1;
a paid service is the operator's own connection.

## Voice cloning (client's own voice) - DISCLAIMER

Clients can narrate a book in a cloned voice. Cloning carries real legal
exposure, so Genie shows a disclaimer that puts the responsibility for rights
on the client, records it, and proceeds:

1. **The disclaimer.** When clone is chosen, Genie displays:
   *"You confirm the voice being cloned is your own, or that you have the voice
   owner's written permission. Cloning a person's voice without permission may
   be illegal (right of publicity) and can violate distributor policies. You are
   solely responsible for holding the rights to any voice you clone."*
   It is printed at the run and stamped into state/voice_clone_disclaimer.json
   for the studio's paper trail. Show it verbatim with
   `voice_disclaimer.py show`.
2. **Reference sample.** Cloning needs a short (about 10 to 30 second) clean WAV
   of the voice to clone, passed to synth as `--ref-sample path\to\voice.wav`.
3. **Commercial-safe model only.** Cloning uses an MIT-licensed model
   (Chatterbox by Resemble AI), so cloned output is licensed for sold books.
   XTTS is deliberately NOT used: its model license is non-commercial and would
   taint a book the client sells. ElevenLabs (the paid engine) is the premium
   cloning option and carries its own consent verification.
4. **Same downstream gates.** Cloned audio passes wavcheck and FLAC conversion
   like any other engine, and the platform AI-narration policies in the
   distribution section still apply (ACX/Audible restrict AI narration; a
   cloned-voice audiobook is still AI narration and is never disguised as a
   human read).

       python .agents/skills/uapf-audiobook/genie_audiobook.py synth \
         --dir narration --engine clone --ref-sample my_voice.wav --project <folder>

## Road 2: External audiobook (you generate the audio)
Real MP3 narration you generate yourself. This audio is for distribution OUTSIDE Amazon Virtual Voice (a companion audio product, or platforms whose terms allow AI narration; Audible and ACX have their own policies).

### Backends (pick one)
- Kokoro Web (RECOMMENDED: free and commercial-safe). The Kokoro-82M model under Apache-2.0, self-hosted with an OpenAI-compatible API. No per-character cost, commercial use permitted, and no external dependency once it is running.
  TURNKEY setup (no Docker needed): this skill ships kokoro_setup.py. Run it once:
    python kokoro_setup.py
  It installs kokoro-onnx, downloads the Kokoro model on first run (about 350 MB, cached in a per-user folder), and starts the server on http://127.0.0.1:8880. Later runs start in seconds. Docker (kokoro-fastapi) is an alternative for a hosted server.
  Then generate every chunk at once:
    python genie_audiobook.py synth --dir narration --endpoint http://localhost:8880/v1 --voice af_bella --format wav
  List the instance's voices, pick a narrator, and confirm the voice with the operator.
- Connected credit-based service (for example vidiq or ElevenLabs): premium voices, but paid. Costs credits per 1000 characters. Use when a specific premium voice matters. The agent sends each chunk to the connected voiceover tool, polls until done, and downloads the MP3s into narration/audio/ in order (0001.mp3, 0002.mp3, and so on). CONFIRM the credit cost (from prep) and get an explicit YES before generating.
If neither backend is available, do Road 1 only and tell the operator.

### Workflow
1. Prep: python genie_audiobook.py prep --manuscript book.docx --out narration --title "TITLE". Writes chunk_XXXX.txt (4800 characters or fewer) plus manifest.json and the estimate.
2. Choose the backend and a narrator voice. For the paid backend, show the cost estimate and get an explicit YES first. For Kokoro there is no per-character cost, but still confirm the voice and that the run is wanted.
3. Generate: Kokoro via the synth command above, or the connected service chunk by chunk into narration/audio/.
4. Stitch: python genie_audiobook.py stitch --dir narration/audio --out audiobook.mp3. For clean chapter markers and metadata, re-encode with ffmpeg if it is available.
5. QA: spot-listen; check the pronunciation of names and unusual terms; regenerate any chunk that mispronounces. Deliver the MP3s to the operator.

## Cost and rights (state plainly, every time)
- Kokoro Web is free and Apache-2.0 (commercial use of the output permitted), so it has no per-character cost; prefer it for full-length books.
- The connected credit-based service costs credits or money per 1000 characters; a full book can run to thousands of credits. If that backend is used, always show the estimate and confirm first.
- AI narration is not accepted as human narration on Audible or ACX; check each platform's AI policy before distributing.
- Confirm the voice provider's license allows commercial use of the output.
- The connected voiceover service is the operator's own connection; the shipped agent does not include one.

## Hard rules
- CONFIRM before spending any credits or money on audio generation.
- Real output only: never claim an audiobook exists or was distributed unless the files exist and the operator published them.
- fully compliant narration content, same as the manuscript.
- Genie never publishes; per-book operator confirmation before any publish or distribution.
- Virtual Voice uses Amazon's voices only; never claim outside audio can be uploaded as Virtual Voice.

## WAV delivery compliance (operator directive 2026-08-15)
When WAV files are the deliverable (some distributors require WAV), every
file MUST pass `python genie_audiobook.py wavcheck --files "<glob>"` before
delivery: format code 0x0001 (WAVE_FORMAT_PCM), never 0xFFFE
(WAVE_FORMAT_EXTENSIBLE), valid fmt and data subchunks, no bytes after the
data subchunk, and full tracks only (complete chapters or the complete
book; sample clips are never delivered). The stitch path (sf.write PCM_16)
produces canonical compliant WAVs; any failing file is re-rendered through
stitch, never shipped.

## FLAC conversion (2026-08-15)
WAV deliverables convert to FLAC on request:
`python genie_audiobook.py flac --files "narration/*.wav"` (add `--replace`
to drop the WAVs after conversion). FLAC is lossless; the tool verifies
every conversion bit-exactly (decode-and-compare) and fails rather than
ship an unverified file. Use for distributors that accept or prefer FLAC;
WAV compliance (wavcheck) still governs WAV deliveries.

## Languages (2026-08-15)
The local Kokoro voice route is MULTI-LANGUAGE. The voice pack prefix picks
the language automatically (override with `--lang`): a=American English,
b=British English, e=Spanish (ef_dora, em_alex), f=French (ff_siwis),
i=Italian (if_sara, im_nicola), p=Brazilian Portuguese (pf_dora, pm_alex),
j=Japanese, z=Mandarin, h=Hindi. Pair with uapf-localization output: a
localized DE/FR/ES/IT book narrates in its own language where a voice pack
exists (German is NOT covered by Kokoro; use an external voiceover service
for German audio and say so honestly). Narration quality varies by
language; spot-check a chapter before committing to a full run. KDP
Virtual Voice languages are whatever Amazon currently offers; verify in
KDP at enable time, never assume. External voiceover services carry their
own language lists; check before estimating credits.

## Tier
Included in every Community Edition install. All audiobook capabilities in
this skill: Virtual Voice preparation, local Kokoro narration in every
supported language, external voiceover synthesis, stitching, WAV compliance
(wavcheck), and FLAC conversion.

## Distribution routes (production without distribution is half a business)

After an audiobook passes wavcheck, route it to market deliberately. The
four routes, with the decision guide; ALWAYS verify current terms,
royalty rates, and AI-narration policies LIVE before committing a title:

1. KDP VIRTUAL VOICE (inside KDP): attached to the existing eBook, no
   file upload, fastest and free; narration is Amazon's, not Genie's
   Kokoro files. Best default for backlist volume. Prepared by this
   skill's Virtual Voice section.
2. ACX (Audible/Amazon/iTunes): the biggest audiobook storefront.
   Exclusive distribution pays a higher royalty than non-exclusive, but
   locks the title in for the contract term. CRITICAL: verify ACX's
   CURRENT policy on AI/synthetic narration live before submitting
   Kokoro-narrated files; policy has been restrictive and submitting
   non-compliant narration risks the account. If policy does not allow
   it, say so honestly and route elsewhere; never disguise synthetic
   narration as human.
3. FINDAWAY VOICES / SPOTIFY and wide distributors (Kobo, libraries):
   widest reach, generally clearer acceptance paths for licensed
   synthetic narration (verify per distributor, live). This is the
   normal route for Kokoro-produced audio; the wavcheck spec in this
   skill is written to distributor requirements.
4. DIRECT (BookFunnel or the author's own site): full margin, no
   gatekeeper, needs the author-brand layer (landing page + email list)
   to matter; pairs with uapf-author-brand.

Record the chosen route, the verified policy/rate facts (with dates), and
the exclusivity decision in the book's publish_manifest.json and decision
log. Exclusivity and any paid narration service are operator-confirmed
decisions.
