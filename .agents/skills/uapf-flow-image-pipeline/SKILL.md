---
name: uapf-flow-image-pipeline
description: Use after UAPF generates image_manifest.md to automate the full image pipeline for a book: submits each prompt to Google Flow via the user's real Chrome browser (Chrome MCP), reads each generated image straight from the page, downloads it from its signed CDN URL, and inserts them into the manuscript DOCX at the correct [IMG-XX] placeholder. Run once per book project after the manuscript is complete and image prompts are ready.
---

# UAPF Google Flow Image Pipeline (Chrome MCP Edition)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Automate AI image generation for a UAPF book project using the **Chrome extension MCP** (`mcp__claude-in-chrome__*` tools). This runs in the user's REAL Chrome browser where they are already logged into Google — no separate login required, no browser pane needed.

> METHOD UPDATE 2026-08-06: Flow changed how it serves images. The old
> `aisandbox` + `batchGenerateImages` + `fifeUrl` interceptor no longer fires
> and is REMOVED. Generated images now appear directly in the page DOM as
> `<img src=".../trpc/media.getMediaUrlRedirect?name={mediaId}">`. You capture
> them from the DOM and resolve them to the signed CDN URL. This method was
> proven end to end on 2026-08-06.
>
> ENGINE UPDATE 2026-08-22: Switched from built-in Claude browser to Chrome
> MCP. Root cause of the old approach: the built-in browser has no Google
> session, so labs.google redirects to the Google sign-in page and blocks image
> generation. Chrome MCP uses the user's real Chrome session (already logged
> in) and eliminates the login problem entirely.
>
> SIGN-IN GATE HARDENED 2026-08-23 (verified live): the ONLY reliable way past
> the block is the user's own logged-in Chrome, driven by the Chrome extension
> MCP. There is no automation trick that gets an unauthenticated or built-in
> browser into Flow (Google gates the tool behind a real Google login and blocks
> automated sign-in), and Genie never signs in for the user. Detect the blocked
> state precisely: navigating to `labs.google/fx/tools/flow` REDIRECTS to bare
> `labs.google` (the marketing page) when there is no session; it STAYS on
> `/fx/tools/flow` with the app UI when logged in. On the redirect, stop and ask
> the user to sign into Chrome, then retry. For headless/cloud/client runs where
> the user's Chrome is not available, use a keyless engine instead (Cloudflare
> Workers AI, FLUX via HF, or Codex gpt-image) via uapf-image-engines; Flow is an
> opt-in path for a signed-in operator, not a headless one.

## Preconditions

- `image_manifest.md` is present in the book folder with `## IMG-XX` sections containing `**Save as:**` and `**Flow prompt:**` fields
- `cowork_image_task.md` is present in the book folder with slot dimensions and source/output DOCX filenames (falls back to sensible defaults if absent)
- The source `.docx` contains `[IMG-XX]` placeholder paragraphs
- **Chrome is open** and the Claude Chrome extension is connected (`mcp__claude-in-chrome__*` tools are available). If `tabs_context_mcp` errors or the `mcp__claude-in-chrome__*` tools are missing, STOP: ask the user to open Chrome and make sure the Claude extension is active. Do NOT fall back to the built-in browser pane for Flow: it has no Google session and is always blocked (redirected to the marketing page).
- **The user is logged into Google in Chrome (SIGN-IN GATE, verify before every run).** Google gates the Flow tool behind a Google login and blocks any browser without the user's real session; there is no way around this and Genie never signs in on the user's behalf. Verify with a hard, scriptable check, not just the avatar:
  1. `tabs_create_mcp` a new tab and `navigate` it to `https://labs.google/fx/tools/flow`.
  2. Read the landed URL (`tabs_context_mcp`, or `javascript_tool` -> `location.href`).
  3. **Logged in / ready:** the URL stays on `labs.google/fx/tools/flow` (or `/fx/tools/flow/project/...`) and the page shows the app UI ("+ New project", or an open project canvas). Proceed.
  4. **Blocked / not logged in:** the URL redirects to bare `https://labs.google` (the marketing landing page with "Create with Google Flow", "Pricing", "Models"). This is the block. STOP and tell the user: "Open Chrome, sign into your Google account, and make sure the Claude extension is connected, then say continue." Do not attempt to sign in, and do not switch engines automatically unless the operator asked for a fallback.

---

## Architecture — what actually happens inside Flow (proven 2026-08-06)

| Fact | Detail |
|------|--------|
| Prompt box | A **Slate.js** rich-text editor: `div[contenteditable="true"]`. `mcp__claude-in-chrome__computer type` correctly updates its state. |
| Submit | The `→` button, a normal `<button>` whose text is `arrow_forward Create` (there is NO `button[type=submit]`). It requires a REAL gesture: a JavaScript `.click()` does NOT submit. Click it by coordinate (see 3c). **NEVER press Enter** — Slate inserts a newline. Submission is confirmed when the prompt box clears to the placeholder "What do you want to create?". |
| Model | Default is **"Nano Banana 2", 16:9, x2** (2 images per prompt). x2 is fine — pick the better variant, or download both. |
| Image location | Generated images **DO appear in the DOM** as `<img src="https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name={mediaId}">`. (The old "images are not in the DOM" rule is obsolete.) |
| Signed URL | `media.getMediaUrlRedirect?name={id}` 302-redirects to `https://flow-content.google/image/{id}?Expires={ts}&KeyName=labs-flow-prod-cdn-key&Signature={sig}` — a pre-signed CDN URL, valid ~6 hours, needs no auth. |
| How to get the signed URL | You cannot `fetch()` it in-page (CORS) and canvas is tainted. Instead navigate a scratch Chrome tab to the `getMediaUrlRedirect` URL and read `location.href` — the tab lands on the signed URL. |
| Download | `Invoke-WebRequest` in PowerShell downloads the signed URL directly. No auth headers. |

---

## Step-by-step Workflow

### 1 — Parse the manifest

Read `image_manifest.md` from the book folder. Extract all `IMG-XX` slots:

```python
import re
from pathlib import Path

def parse_manifest(folder):
    text = Path(folder, "image_manifest.md").read_text(encoding="utf-8")
    slots = {}
    for m in re.finditer(r'## (IMG-\d+)(.*?)(?=## IMG-|\Z)', text, re.DOTALL):
        slot_id, block = m.group(1), m.group(2)
        save_as = re.search(r'\*\*Save as:\*\*\s*`([^`]+)`', block)
        prompt  = re.search(r'\*\*Flow prompt:\*\*\s*(.+?)(?=\n-\s*\*\*|\Z)', block, re.DOTALL)
        if save_as and prompt:
            slots[slot_id] = {"file": save_as.group(1).strip(),
                              "prompt": prompt.group(1).strip()}
    return slots
```

Skip any slot whose image file already exists and is > 5 KB.

### 2 — Open Google Flow in Chrome

1. Call `tabs_context_mcp` to list open tabs and find any existing `labs.google/fx` tab. If found, record its `tabId` and use it. If not, call `tabs_create_mcp` to open a new tab, then `navigate` it to `https://labs.google/fx`.
2. After the project loads, the page title becomes "Google Flow" and a prompt input appears at the bottom ("What do you want to create?"). Verify the contenteditable is present:

```javascript
// action: "javascript_exec", tabId: <flow_tab_id>
!!document.querySelector('div[contenteditable="true"]')
```

3. Click **"+ New project"** (or an existing project tile to resume). Keep the whole book's images in ONE project for style coherence — use the identical character/style prefix on every prompt.

### 3 — For each image slot (in order)

#### 3a — Record the images already on the page (so you can detect the new ones)

```javascript
// action: "javascript_exec", tabId: <flow_tab_id>
(function(){
  window._before = new Set([...document.querySelectorAll('img')]
    .map(i=>i.src).filter(s=>/getMediaUrlRedirect/.test(s)));
  return window._before.size;
})()
```

#### 3b — Type the prompt into the Slate box

1. `read_page` (filter: interactive, tabId: flow_tab_id) → get the prompt `textbox` ref (the contenteditable near the bottom).
2. `computer left_click` that ref to focus it (pass tabId).
3. `computer type` the full prompt text (pass tabId).
4. Verify: `document.querySelector('div[contenteditable="true"]').innerText.length` is roughly the prompt length.

Do NOT use `execCommand` or innerHTML — Slate will not see it and the submit does nothing.

#### 3c — Click the Create (→) button by coordinate

A JS `.click()` will NOT submit. First take a `computer screenshot` of the Flow tab to get the actual pixel dimensions. Then compute the button center:

```javascript
// action: "javascript_exec", tabId: <flow_tab_id>
(function(){
  const b=[...document.querySelectorAll('button')]
    .find(x=>/arrow_forward/i.test(x.innerText)&&/Create/i.test(x.innerText));
  if(!b) return JSON.stringify({error:"button not found"});
  const r=b.getBoundingClientRect();
  // Returns CSS-pixel center; scale by screenshot_width/window.innerWidth for coordinate clicks
  return JSON.stringify({
    cssX: Math.round(r.x+r.width/2),
    cssY: Math.round(r.y+r.height/2),
    winW: window.innerWidth,
    winH: window.innerHeight
  });
})()
```

Then convert to screenshot coordinates:
- `screenX = Math.round(cssX * screenshotWidth / winW)`
- `screenY = Math.round(cssY * screenshotHeight / winH)`

Take a fresh `computer screenshot` (tabId: flow_tab_id), then `computer left_click` at `{screenX, screenY}`. Confirm the prompt box cleared to the placeholder "What do you want to create?".

#### 3d — Wait for generation, then read the new image id(s)

Wait ~10s, then poll (up to ~40s total) for images that were not there before:

```javascript
// action: "javascript_exec", tabId: <flow_tab_id>
(function(){
  const now=[...document.querySelectorAll('img')].map(i=>i.src)
    .filter(s=>/getMediaUrlRedirect/.test(s));
  const fresh=now.filter(s=>!window._before.has(s));
  const ids=fresh.map(s=>(s.match(/name=([0-9a-f-]+)/)||[])[1]).filter(Boolean);
  return JSON.stringify({newCount:fresh.length, ids});
})()
```

With x2 you get 2 ids. Pick `ids[0]` (or download both and choose the better one). If `newCount` stays 0 after ~40s, retry the slot (up to 3 times).

#### 3e — Resolve the signed URL in a scratch Chrome tab

Create a new Chrome tab with `tabs_create_mcp`, then `navigate` it (tabId: scratch_tab) to:
`https://labs.google/fx/api/trpc/media.getMediaUrlRedirect?name={id}`

It 302-redirects; read the landed URL:

```javascript
// action: "javascript_exec", tabId: <scratch_tab_id>
location.href   // -> https://flow-content.google/image/{id}?Expires=...&Signature=...
```

Close the scratch tab with `tabs_close_mcp` after reading. Keep the Flow project tab open at all times.

#### 3f — Download via PowerShell, saving as the manifest filename

```powershell
Invoke-WebRequest -Uri "<signed flow-content.google URL>" `
  -OutFile "C:\path\to\book_folder\images\IMG-01.png" -TimeoutSec 30
```

Verify the file is > 100 KB. The signed URL needs no auth. The bytes may be PNG or JPEG regardless of extension; python-docx reads magic bytes, so the extension is harmless.

---

### 4 — DOCX insertion

After all slots are downloaded, insert them into the manuscript:

```powershell
$py = "python"
$insert = @'
import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(os.environ["LOCALAPPDATA"]) / "FlowPipeline"))
from flow_book_images import parse_manifest, parse_cowork, insert_images
folder = Path(sys.argv[1])
slots  = parse_manifest(folder)
dims, source_name, output_name = parse_cowork(folder, slots)
print(f"Inserting into {source_name} -> {output_name}")
sys.exit(0 if insert_images(folder, slots, dims, source_name, output_name) else 1)
'@
$insert | & $py - "<book_folder>"
```

This replaces each `[IMG-XX]` placeholder in the source DOCX with its image at the size from `cowork_image_task.md`, and saves `*_FINAL.docx`.

### 5 — Final report

Report slots succeeded / failed / skipped, the output DOCX path + size, and any slots to retry.

---

## Error reference

| Symptom | Fix |
|---------|-----|
| `labs.google/fx/tools/flow` redirects to bare `labs.google` (marketing page: "Create with Google Flow", "Pricing") | THE BLOCK: no Google session in this browser. Flow only opens in the user's own logged-in Chrome. Ask them to open Chrome, sign into Google, and confirm the Claude extension is connected, then retry. Never sign in for them; never use the built-in browser pane (always blocked). |
| Prompt box does not clear after clicking → | The click missed (or was a JS click). Recompute the button center (3c), take a fresh screenshot, click by coordinate again. |
| No new `getMediaUrlRedirect` img after 40s | Generation slow or failed. Re-poll, then retry the slot. Confirm the prompt actually submitted (box cleared). |
| `location.href` still shows the redirect URL | Give the scratch tab a second to land, re-read `location.href`. It must land on `flow-content.google`. |
| `Invoke-WebRequest` fails / tiny file | The signed URL expired (>6h) — regenerate the image and re-resolve. |
| DOCX placeholder not found | The manifest `## IMG-XX` must match `[IMG-XX]` in the DOCX exactly. |
| `tabs_create_mcp` not available | Chrome extension MCP not connected. Ask user to open Chrome and ensure the Claude extension is active. |

---

## Key rules (do NOT break these)

1. **NEVER press Enter to submit** — Slate adds a newline. Click the `→` Create button.
2. **A JS `.click()` does NOT submit** — click Create by coordinate (real gesture), after a fresh screenshot.
3. **Images ARE in the DOM now** — read `<img src=...getMediaUrlRedirect?name=ID>`; do NOT use a fetch interceptor (it no longer fires).
4. **Get the signed URL by navigating a scratch Chrome tab** to the `getMediaUrlRedirect` URL and reading `location.href`; never `fetch()` it in-page (CORS) and never draw the img to canvas (tainted).
5. **Download via PowerShell** from the `flow-content.google` signed URL; no auth headers.
6. **Always pass the correct `tabId`** to every Chrome MCP call — Flow tab for generation/reading, scratch tab for URL resolution. Never mix them.
7. **Close scratch tabs** after reading the signed URL to keep Chrome clean.

---

## Runtime

- Chrome MCP tools: `mcp__claude-in-chrome__computer`, `mcp__claude-in-chrome__javascript_tool`, `mcp__claude-in-chrome__read_page`, `mcp__claude-in-chrome__navigate`, `mcp__claude-in-chrome__tabs_create_mcp`, `mcp__claude-in-chrome__tabs_context_mcp`, `mcp__claude-in-chrome__tabs_close_mcp`
- PowerShell: `Invoke-WebRequest` for image download, Python invocation for DOCX insertion
- Python 3.10+ with `python-docx`: the `python` on PATH (the first-run bootstrap installs all dependencies)
- Helper functions for DOCX insertion: `insert_images`, `parse_manifest`, `parse_cowork` from `%LOCALAPPDATA%\FlowPipeline\flow_book_images.py`
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
