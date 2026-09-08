# Running Genie unattended on Railway

What this gets you: push a book brief once, close your laptop, come back
later to a finished (or in-progress, or blocked-on-you) book. What it costs:
a Railway compute bill for however long the container runs, and a few real
gaps versus running Genie locally in Claude Code (see "What's different"
below) that are worth reading before you trust it with something you care
about.

## 1. Get a long-lived auth token from your subscription (no API key)

On your own machine, in a terminal:

```
claude setup-token
```

This logs in with your existing Claude subscription and prints a token.
Copy it -- you'll paste it into Railway as `CLAUDE_CODE_OAUTH_TOKEN` in step 3.
This is *not* an Anthropic API key and does not switch you to pay-per-token
billing; it authenticates the CLI against your normal plan the same way an
interactive login would.

## 2. Create the Railway project

1. Push this folder to a GitHub repo (Railway deploys from a repo or via its
   CLI). This folder isn't a git repo yet:
   ```
   git init
   git add .
   git commit -m "Genie: add Railway deployment"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```
2. In Railway: **New Project -> Deploy from GitHub repo**, pick this repo.
   It will find `Dockerfile` and `railway.json` automatically.
3. **Attach a volume**: Railway dashboard -> your service -> Settings ->
   Volumes -> add one, mount path `/data`. This is what makes `Books/`,
   `state/`, `cover_db/`, and the Claude session (so `--continue` survives a
   restart) persist. Without this, every redeploy starts from zero.

## 3. Set variables

Service -> Variables:

| Variable | Value |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | the token from step 1 |
| `BOOK_BRIEF` | the full book brief, see below |

`BOOK_BRIEF` is only read once, on first boot, and saved to the volume
(`/data/book_brief.txt`). To start a different book later, either edit that
file directly (via `railway ssh` / the volume) or wipe the volume and set a
new `BOOK_BRIEF`.

Write the brief the same way you would type it to Genie interactively --
include the things CLAUDE.md's autopilot section needs (title, marketplace,
language, target pages per chapter, max page count, any non-negotiables) --
**plus one line pinning the image engine**, since there's no logged-in
browser on this server:

> Use the FLUX.1-schnell image engine (Hugging Face, no API key needed) for
> every interior image on this book. Do not attempt Google Flow or any
> browser-based image tool.

(Cloudflare Workers AI is a faster free alternative if you set
`CF_API_TOKEN`/`CF_ACCOUNT_ID` in Railway's variables too -- optional.)

## 4. Deploy, then watch the first run closely

Railway will build the image and start the container, which runs
`deploy/entrypoint.sh`. Watch the deploy logs for the first hour or so --
don't just walk away on the very first run. Specifically check:

- The book brief was picked up and Genie actually started (you'll see the
  normal session-start standup output in the logs).
- It reaches a real chapter, not stuck retrying `winget`-style install
  attempts (it shouldn't -- Node/Claude Code/LibreOffice are baked into the
  image already -- but confirm once).
- If/when you hit your usage limit, check `/data/logs/stderr.last.log` (via
  `railway ssh` or the volume browser) for the **actual** message text. The
  entrypoint script guesses at the wording ("usage limit", "rate limit",
  "resets at", "try again"); if what you see doesn't match, tighten the
  `grep -qiE` pattern in `deploy/entrypoint.sh` and redeploy.

Once you've confirmed one limit-hit-and-resume cycle actually works, it's
reasonable to leave it running unattended.

## 5. Checking in / stopping it

There's no "book is done" signal the supervisor can detect on its own --
CLAUDE.md references a `scripts/project_status.py` completion gate that
isn't actually shipped in this Community package, so the loop just keeps
nudging Genie forward turn after turn indefinitely. To check progress,
either:

- Browse the volume's `Books/<project>/` folder for delivered
  chapters/DOCX/PDF files, or
- `railway ssh` into the running container and read
  `/data/logs/session_history.log`, or ask it directly with
  `claude -p --continue "Are you done? What's left?"`.

When the book is actually finished (or stuck on an operator-only gate --
payment, credentials, a Publish click, a HIGH RISK trademark result), stop
the Railway service so it stops consuming compute. Restarting it later
resumes the same conversation via `--continue`.

## What's different from running Genie locally

- **No logged-in browser.** Google Flow images and anything that opens
  Chrome won't work. Pin a headless image engine in the brief (step 3).
  Live web research (trademark checks, competitor lookups) uses Claude
  Code's built-in web tools, not a browser, so those still work.
- **No human approves tool calls.** The container runs with
  `--permission-mode bypassPermissions` because there's nobody present to
  click "allow" -- otherwise the very first Bash call would hang forever.
  That means every Bash/Write/Edit call executes without a checkpoint. The
  content-level hard gates in CLAUDE.md (money actions, credentials, the
  final Publish click) still hold because Genie has no payment/credential
  info to act on and is instructed to record and stop, not because
  anything in this deployment enforces them mechanically. Keep this
  Railway project isolated -- no other secrets, no production
  infrastructure -- since a container with all permissions bypassed is a
  real blast-radius decision, not a formality.
- **No automatic "it's done" detection.** See section 5.
- **Usage-limit detection is a best-effort text match**, not a documented
  API contract -- verify it once per section 4 rather than trusting it
  blind on the first real run.
