---
name: uapf-image-engines
description: Open-model image engines for the CLAUDE ENGINE ONLY (operator directive 2026-08-17): FLUX.1-schnell, Stable Diffusion XL, and Qwen-Image, hosted on Hugging Face Spaces via gradio_client (no API key, no local GPU), routed per niche. Google Flow remains the primary interior pipeline; these are the alternates for niches where their strengths are required. Invoke on "generate with flux/sdxl/qwen", or automatically per the niche routing table when Flow is unavailable or the niche calls for a specific engine.
---

# UAPF Image Engines (open models, Claude engine only)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Three open, COMMERCIALLY-LICENSED models, callable from any Claude Code
session through `hf_image_gen.py` (gradio_client; installed by the
bootstrap). No API key, no GPU on the client machine.

## The roster and the licensing law

| Engine | Model | License | Strength |
|---|---|---|---|
| `flux` | FLUX.1-schnell | Apache 2.0 | photoreal interiors: food, technique steps, scenes, crafts, travel |
| `sdxl` | Stable Diffusion XL | CreativeML Open RAIL++-M | line art, coloring pages, stylized children's illustration |
| `qwen` | Qwen-Image | Apache 2.0 | images that must contain READABLE TEXT: labeled diagrams, posters, signs |

LICENSING LAW: FLUX.1-[dev] is NON-COMMERCIAL and is NEVER used for any
book. Only the three engines above ship. If a space swap is ever needed,
verify the replacement model's license permits commercial use BEFORE
generating a single book image.

## Per-niche routing (which engine when)

- cookbook, health, travel, crafts, howto, user-guide photo steps: `flux`
- coloring books and any line-art page: `sdxl` (then lineart_qa.py MUST
  pass; gray-shaded outputs are regenerated with a harder line-art prompt)
- childrens / childrens-facts stylized illustration: `sdxl` (style locked
  by the design fingerprint; same character described identically across
  prompts for consistency)
- textbook, workbook, study-guide, exam diagrams or any image that must
  carry readable labels: `qwen`
- everything else and the DEFAULT: Google Flow remains the PRIMARY
  interior pipeline (the image engine law stands); these engines are the
  alternates where their strengths are required or Flow is unavailable.
- Codex engine: unchanged (its native tool); these engines are CLAUDE
  ENGINE ONLY.

## Usage

```
python .agents/skills/uapf-image-engines/hf_image_gen.py \
  --engine flux --prompt "<the approved image brief>" \
  --size 1024x1536 --out <project>/images/chNN_fig1.png
```

- Briefs follow the IMAGE REALISM LAW verbatim (photoreal or technically
  accurate, no text unless qwen-routed, content restrictions apply).
- Every output is checked against its caption before insertion; coloring
  pages additionally pass lineart_qa.py. FAIL = regenerate, never ship.
- Prompts are saved as production records like every other image prompt.

## Quota reality (honest)

Public Spaces run on shared GPU quota. `flux` (4-step) and `sdxl` work
anonymously; `qwen` (heavier) usually needs a FREE Hugging Face account
token: set `HF_TOKEN` in the environment and quota multiplies. If a space
is busy or quota-hit, the script says so and exits 2: report it as a
blocker, use the routed fallback (flux <-> sdxl, or Flow), and retry
later. Never claim an image was generated when it was not.

## Tiers

Interior images are core production in every install. The operator may set
HF_TOKEN per install; installs without a token still have flux and sdxl
anonymously plus Flow as primary.

## PARALLEL BATCH GENERATION (operator directive 2026-08-21, tested)

`codex_image_batch.py` generates a book's whole image batch and picks
concurrency by ENGINE, verified on real runs, not assumed:

- **Codex: SERIALIZED (1 at a time).** Concurrent `codex exec` sessions on one
  machine contend for shared local-runtime singletons (node_repl pipe,
  computer-use backend, imagegen post-processing) and abort mid-render (tested:
  0/3 delivered concurrently). The runner forces workers=1 for codex. Codex
  speed comes from reduced reasoning, not parallelism.
- **Stateless HTTP engines (flux / sdxl / qwen / pollinations / cloudflare):
  TRUE PARALLEL.** Tested: 4 FLUX images across 4 workers finished in 31s vs
  115s sequential (3.6x), all compressed under 500 KB. Pool capped at 8
  (default 4); the real ceiling is the provider's rate limit, not local CPU.
- **RAISE THE FREE CEILING BY SPREADING PROVIDERS.** Each free provider has its
  OWN separate quota, so a book's batch can round-robin across the engines a
  client has set up (HF FLUX + Cloudflare + Pollinations) to multiply the total
  free throughput and avoid hammering any one limit. Cloudflare Workers AI
  (cloudflare_image_gen.py, FLUX-1-schnell, verified 2026-08-21) gives ~10,000
  neurons/day free per account (about 100 images, no card), headless and
  commercial-safe, on the client's own free CF_ACCOUNT_ID + CF_API_TOKEN in
  .env (never shipped, never committed). Together AI was checked and is NOT a
  stable free option (credit-then-paid), so it is not added.

```
python .agents/skills/uapf-image-engines/codex_image_batch.py     --jobs jobs.json --dest <project>/images --engine flux --workers 6
```

Use the parallel FLUX/Pollinations path when a book needs its images FAST;
use single-Codex when top per-image quality matters. Every worker is isolated
(own temp / own output) and delivers explicitly; a worker that produces no file
fails to the fallback chain, so the book is never imageless. This is the batch
phase of the "full manuscript first, then images" timing law.

## CODEX IMAGE ENGINE: auto-repair and generation timing (operator directive 2026-08-19)

Clients who choose CODEX for a book's images get two guarantees, enforced
mechanically:

1. **AUTO-REPAIR at choice time.** `image_engine_choose.py --set codex` runs
   `codex_image_repair.py` automatically: Codex CLI missing -> installed on the
   spot (npm, Node via winget first if needed); not logged in -> the exact
   one-time `codex login` step is shown (the login itself is the client's
   action; Genie never touches credentials). If codex is STILL broken after
   repair, the FLUX.1-schnell fallback is armed in `state/image_engine.json`
   (`"fallback_engine": "flux"`) and THIS book's images generate with FLUX
   immediately: a book is never imageless and never stalls waiting on a broken
   engine. The client can re-pick codex next book once healthy.
   `codex_image_repair.py --repair --smoke` adds a real one-image generation
   test; run it when a client reports codex image trouble.

2. **TIMING: full manuscript first, then batch the images (operator directive
   2026-08-20).** With Codex for images, Claude writes the FULL manuscript text
   first, chapter by chapter (chapter previews ship text-only), THEN Codex
   generates ALL the book's images in one batch and they are embedded before
   the book is finished. This fits Codex's speed: no chapter waits minutes per
   image, and the batch runs at reduced reasoning (Speed Law above). Images
   stay COMPULSORY for the finished book, never optional: at release QC the
   final DOCX must carry every planned image, verified by `format_qa.py
   <final.docx> --require-images N` on the whole book (placeholders fail), and
   a book is never marked complete imageless. If Codex is unavailable at image
   time, auto-repair runs and the armed fallback (Pollinations, then FLUX)
   generates the batch instead. The standalone Codex engine may still generate
   natively inline while drafting (one agent, efficient); the whole-book image
   requirement is identical.

Both guarantees bind BOTH engines and every pack.

## GEMINI API ENGINE (operator directive 2026-08-19, client-shippable)

`gemini_image_gen.py` adds Google's free AI Studio route (gemini-2.5-flash-image,
photoreal, aspect-ratio config, commercially usable, no visible watermark via
the API) to the client choice menu as `gemini`.

- **PER-INSTALL KEY, NEVER SHARED.** Each install uses its OWN free key from
  https://aistudio.google.com/apikey placed by the CLIENT into a `.env` file at
  the Genie root (`GEMINI_API_KEY=...`). The key is never shipped in any
  package (factory excludes `.env`), never committed (`.gitignore`), never
  printed, and never entered by Genie: the client pastes it themselves; Genie
  shows the exact steps.
- **NEVER the Gemini web/chat app** for book images: it stamps a visible
  watermark. Only the API script (or the other engines).
- **Output discipline:** aspect follows the book's niche image contract
  (default 16:9 for landscape figures; recipe/full-page art keeps its
  contract aspect); every output is auto-compressed (max 1600 px longest
  side, JPEG q85, target under 500 KB) before embedding; the image realism
  law and caption check still gate every image.
- **Fallback chain (never-imageless law intact):** if gemini fails
  (quota/auth/safety-block), the script exits 2 with the exact error; the
  session reports it honestly and falls back to codex, then FLUX.1-schnell,
  so the chapter still ships with its images. Failures are never silent.

## THE CODEX IMAGE PIPELINE (operator directive 2026-08-19, from the production guide; client-shippable)

The battle-tested pipeline from `CODEX_IMAGE_PIPELINE_GUIDE.html` (ships in the
package root as client documentation), fully automated:

0. **SPEED LAW (operator directive 2026-08-20): every Codex image call runs at
   REDUCED reasoning.** Build the command as
   `codex exec -c model_reasoning_effort="low" --sandbox workspace-write ...`.
   Image generation does not need the driving model to deep-reason, and the
   default `xhigh` effort is the main reason Codex images are slow; low effort
   cuts the per-image overhead without lowering image quality (the gpt-image
   model that renders is separate from the reasoning effort). All other Codex
   work keeps its normal reasoning; only image-generation calls drop to low.
1. **SANDBOX LAW: interior image generation runs `codex exec --sandbox
   workspace-write` and NEVER danger-full-access.** The full-access two-phase
   cover flow is a separate, deliberate design and is unchanged; but no IMAGE
   GENERATION call ever uses danger-full-access, so the auto-mode classifier
   never blocks it. `codex_image_repair.py --repair` now also fixes the
   client's `~/.codex/config.toml` ADDITIVELY (sandbox_mode=workspace-write,
   approval_policy=never, network_access=true, writable_roots incl. the Genie
   folder; forward slashes; no duplicates; .bak kept; proven idempotent):
   this is the root fix for "network blocked" and "cannot save" errors.
2. **DELIVERY STEP (mandatory after EVERY codex image call):** Codex's native
   tool saves to `~/.codex/generated_images/<thread-id>/` and often reports
   "read-only workspace prevented saving" on Windows: the image EXISTS. Run
   `python .agents/skills/uapf-image-engines/codex_image_deliver.py --dest
   <project>/images --name IMG-NN [--src <path from codex's reply>]`: it
   rescues the file (newest generated if no path), renames it, verifies >0 KB,
   deletes the leftover, and compresses. No image is ever lost to the sandbox,
   and Genie never claims an image exists without the delivered file on disk.
3. **COMPRESSION LAW (all engines, before embedding):** every interior image
   is compressed to max 1600 px longest side, JPEG quality 85, target under
   500 KB (`codex_image_deliver.py --compress-only <file>`; quality steps
   down automatically until under target). Raw multi-MB PNGs never enter the
   manuscript.
4. **FALLBACK CHAIN (never silent):** chosen engine -> codex -> POLLINATIONS
   free backup (`pollinations_image_gen.py`: classic free endpoint only, never
   gen.pollinations.ai; keyless, optional free sk_ token in .env; 429 = wait
   20 s retry up to 5; every backup image is POLISHED: 1.6x Lanczos upscale +
   UnsharpMask, then compressed). Hugging Face engines remain available as
   EXPLICIT client choices but are never used as a silent automatic fallback.
   Every fallback is reported to the user with the real error; if everything
   fails, STOP and show the exact error, never claim success.
5. **Usage reality:** Codex image limits come from the client's OpenAI plan
   (rolling ~5 h window + weekly cap; dashboard: chatgpt.com/codex/settings/
   usage). Budget a few dozen images/day on Plus; a typical book takes 1-2
   days of image generation. The compulsory inline-image law still governs
   WHEN images are made (during the chapter); if the day's codex budget runs
   dry mid-book, the backup engine carries the remaining chapters and codex
   can regenerate hero images next session BEFORE release QC (upgrade, not
   defer: the chapter previews always ship with images).

## PER-TITLE ENGINE ANALYSIS: FLOW vs CLOUDFLARE (operator directive 2026-08-28)

Before generating ANY images for a book, RUN the analysis and use its answer:

    python .agents/skills/uapf-image-engines/image_engine_choose.py         --analyze --title "<exact book title>" --niche <routed-niche> --project <folder>

It scores Flow vs Cloudflare on the title's subject signals, the niche, and
live readiness, prints the reasons, and (with --project) locks the winner into
state/image_engine.json so the whole batch uses it. The heuristics:

- Photoreal instructional or lifestyle subjects (food, crafts, technique
  steps, places, people): Flow leads on realism; prefer Flow when its
  signed-in Chrome session is available.
- High-volume batches, headless runs, or when Flow's sign-in gate or the
  labs.google marketing redirect blocks the session: prefer Cloudflare.
- Diagram-adjacent or text-bearing images: neither; follow the matplotlib
  diagram rule.
Record the decision and one-line reason in the project's decision log, then
generate the whole batch on the chosen engine. The global fallback order
still applies if the chosen engine fails mid-run: never stall a book on an
engine choice, and every image still passes the realism and caption checks.

## DIAGRAM ROUTING LAW: MATPLOTLIB WHERE NEEDED (operator directive 2026-08-28)

Any figure whose value depends on EXACT labels, values, symbols, arrows, or
structure is NEVER sent to a diffusion engine: charts, graphs, process flows,
step sequences, schematics, comparison figures, anything with numbers or text
inside the image. Diffusion engines fabricate wrong symbols and garble labels
(proven on the welding handbook). Route those to matplotlib instead:

    python .agents/skills/uapf-image-engines/diagram_gen.py --spec fig.json --out fig_1_1.png

diagram_gen.py renders bar, line, pie, flow (boxes and arrows), and steps
(numbered sequence) figures from a JSON spec: 300 DPI, landscape, the book's
palette, grayscale-legible. For anything beyond those five shapes, write the
matplotlib code directly in the session; the rule is the same either way.

The split per book: photographic and artistic subjects go to the analysed
engine (Flow or Cloudflare); data-bearing and structural figures go to
matplotlib. Both kinds still pass the caption-match check before insertion,
and diagram PNGs still obey the margin and caption law.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
