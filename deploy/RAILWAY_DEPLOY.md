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
This is *not* an Anthropic API key and does not switch you to pay-per-token
billing; it authenticates the CLI against your normal plan the same way an
interactive login would. That login step can't be done from a web form --
it's a real subscription sign-in -- so whoever's Claude plan this runs
against has to run this command themselves, once.

Two ways to get the resulting string into the deployment:
- **Railway variable** (step 3): paste it as `CLAUDE_CODE_OAUTH_TOKEN`.
- **Via the API, from your frontend** (step 6): the container boots and
  serves the API even with no token set yet -- it just waits, checking
  every 30s, instead of crash-looping. `GET /setup/status` (no auth
  needed) tells your frontend whether to show a "paste your Claude token"
  screen; `POST /setup/claude-token {"token": "..."}` (needs the
  `API_TOKEN` bearer auth) submits it, and the supervisor picks it up
  within 30 seconds, no redeploy required. Useful for the 5-separate-people
  plan: each person runs `setup-token` on their own machine and pastes the
  result into their own frontend instance, instead of you collecting five
  tokens and setting five Railway variables by hand.

### 1b. Optional: Codex (ChatGPT) auth, for covers/A+ content

CLAUDE.md routes cover art and A+ Content generation through Codex when
it's available, falling back to a free image engine when it isn't -- so
this is optional, and production is never blocked waiting for it (unlike
the Claude token above).

Codex's ChatGPT-subscription login doesn't have a `setup-token`
equivalent -- there's no single exportable long-lived string. It's a small
OAuth bundle (`access_token` + `refresh_token` + `id_token`) that the
`codex` CLI refreshes on its own over time, stored at `~/.codex/auth.json`.
So instead of pasting one string, run `codex login` on your own machine
(browser sign-in with your ChatGPT account) if you haven't, then open
`~/.codex/auth.json` and send its **entire contents**:

```
curl -X POST https://<your-domain>/setup/codex-auth \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d "{\"auth_json\": $(cat ~/.codex/auth.json)}"
```

Treat this like copying a browser session, not a purpose-built export
token -- it's more sensitive than the Claude token (a stolen copy is usable
until you log that ChatGPT session out), and it stops working if you ever
log out of that session locally. Fine for your own use; think twice before
asking each of the 5 people to hand you this file versus just skipping
Codex for their deployments and letting the free image engine handle
covers too.

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

## 3. Set the required variables

Service -> Variables:

| Variable | Value |
|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | the token from step 1 |
| `API_TOKEN` | any random string you make up, e.g. `openssl rand -hex 24` |

`API_TOKEN` is the bearer token your frontend sends to the API in step 6 --
without it, anyone with the Railway public URL can create/delete books. Pick
a different one per person if you're doing the 5-separate-projects setup.

Ignore the other empty rows Railway auto-detected by scanning the repo
(`DATA_DIR`, `APP_DIR`, `BRIEF_FILE`, `CONTINUE_PROMPT`, `STARTED_MARKER`,
`EXIT_CODE` are internal to `entrypoint.sh` and aren't meant to be set from
outside; `CF_API_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`,
`POLLINATIONS_TOKEN`, `KOKORO_ENDPOINT` are optional credentials for
image/audio engines you aren't using yet).

Books are queued as files on the volume, not as a variable -- see step 3b.
(There's still a `BOOK_BRIEF` variable as a fallback for a quick first test:
if set, its contents are copied into the queue once on first boot and then
ignored from then on. Prefer the queue for anything beyond the very first
book.)

### 3b. Queue a book

Write the brief as you'd type it to Genie interactively -- title,
marketplace, language, target pages per chapter, max page count, any
non-negotiables -- **plus one line pinning the image engine**, since
there's no logged-in browser on this server:

> Use the FLUX.1-schnell image engine (Hugging Face, no API key needed) for
> every interior image on this book. Do not attempt Google Flow or any
> browser-based image tool.

(Cloudflare Workers AI is a faster free alternative if you set
`CF_API_TOKEN`/`CF_ACCOUNT_ID` in Railway's variables too -- optional.)

Save that as a local `.txt` file, then upload it into the pending queue:

```
railway link                # once, to point the CLI at this project/service
railway volume files upload ./my_first_book.txt /queue/pending/001.txt
```

The supervisor picks up queue files in sorted-filename order, one at a
time. To queue book 2 while book 1 is still running, just upload another
file (`002.txt`, or any name -- it sorts alphabetically) -- no redeploy, no
touching Variables. It'll be picked up automatically the moment the
current book signals it's done (see 3c).

### 3c. How it knows a book is done

This package doesn't ship the `scripts/project_status.py` completion gate
CLAUDE.md references, so the supervisor can't check that. Instead, every
prompt it sends Genie includes an instruction to create a marker file the
moment the book (manuscript, gates, KDP metadata) is genuinely complete --
the supervisor watches for that file, archives the finished brief into
`/data/queue/done/`, and starts the next queued one automatically. A
second marker means "blocked on something only you can do" (payment,
credentials, a Publish click, a HIGH RISK trademark result) -- the
supervisor stops nudging and just waits, checking back hourly, until you
clear it:

```
railway volume files delete /NEEDS_OPERATOR
```

This relies on Genie reliably remembering to create that file across a
long autonomous run -- it's a repeated instruction (sent on every turn,
not just the first), which helps, but it's not a hard guarantee the way a
real completion gate would be. Spot-check `Books/<project>/` occasionally
rather than trusting it blindly, especially early on.

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

## 5. Checking in

The supervisor auto-advances through the queue on its own now (3c), so you
don't have to babysit book-to-book handoffs. Still worth checking in
occasionally, since the completion signal is a best-effort convention, not
a guarantee:

- Browse the volume's `Books/<project>/` folder for delivered
  chapters/DOCX/PDF files.
- `/data/queue/done/` shows which briefs it believes it finished, and when.
- `railway ssh` into the running container and read
  `/data/logs/session_history.log`, or ask it directly with
  `claude -p --continue "Are you done? What's left?"`.

Once the whole queue is empty and nothing's pending, it's safe to stop the
Railway service to stop consuming compute -- restarting it later picks
back up (`--continue`) if a book is mid-flight, or waits for a new queued
brief if not.

## 6. The API (for your frontend)

`deploy/api_server.py` runs alongside the supervisor in the same container
and exposes a small REST API for a frontend to drive -- all you should ever
need to type by hand again is a title.

First, give the service a public URL: `railway domain` (or Settings ->
Networking -> Generate Domain in the dashboard). Every request needs
`Authorization: Bearer <API_TOKEN>` (the value you set in step 3) except
`GET /setup/status`, which is deliberately open so a frontend can check it
before it has anything to authenticate with.

| Method | Path | Body | Does |
|---|---|---|---|
| GET | `/setup/status` | - | `{"claude_token_set": bool, "codex_auth_set": bool}` -- no auth needed. Use this to decide which setup screens to show |
| POST | `/setup/claude-token` | `{"token": "..."}` | Submits the string from `claude setup-token` (run on the person's own machine, see step 1). Picked up within 30s, no redeploy |
| POST | `/setup/codex-auth` | `{"auth_json": {...}}` | Optional. Submits the full contents of `~/.codex/auth.json` (see step 1b) |
| POST | `/books` | `{"title": "..."}` (only field required; `marketplace`, `language`, `pages_per_chapter`, `max_pages`, `image_engine`, `non_negotiables` all optional) | Queues a new book, returns `{id, status}` |
| GET | `/books` | - | Lists every book with live status: `queued`, `in_progress`, `blocked`, `complete`, `deleted` |
| GET | `/books/{id}` | - | One book's detail |
| GET | `/books/{id}/files` | - | Lists downloadable files once complete (pulled from `publish_manifest.json`) |
| GET | `/books/{id}/download?path=<path from /files>` | - | Streams that file |
| DELETE | `/books/{id}` | - | Deletes the book's files. Refuses (409) while `in_progress` unless `?force=true` |

Example, once you have a title:

```
curl -X POST https://<your-domain>/books \
  -H "Authorization: Bearer <API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Next Book"}'
```

That's it for input -- everything else (marketplace, language, image engine)
falls back to sane defaults baked into `compose_brief()` in
`deploy/api_server.py`, so a bare title is enough to enqueue a full book. A
book stays around, files included, until you explicitly `DELETE` it -- so
"don't delete it yet, I'll come back to it" is just "don't call DELETE
yet"; nothing auto-expires.

Two honest limits on this, worth knowing before you build the frontend
around it:
- **Matching a finished book back to its `Books/<folder>` is a heuristic**
  (title-normalized match, falling back to "most recently modified
  folder"), because Genie names that folder itself and nothing here
  controls it. Fine when one book is in flight at a time (which is how the
  supervisor runs, per book -- see 3b); don't count on perfect accuracy if
  you ever queue wildly similar titles back to back.
- **The SQLite file (`/data/genie.db`) lives on the same volume as
  everything else** -- it's real persistent storage, but it's a single
  file with no replication. Fine for one operator's dashboard; don't treat
  it as a production database for someone else's data without backups.

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
- **"It's done" detection is a marker file Genie is instructed to create**,
  not a real completion gate. See section 3c.
- **Usage-limit detection is a best-effort text match**, not a documented
  API contract -- verify it once per section 4 rather than trusting it
  blind on the first real run.
- **The API has no auth if you skip `API_TOKEN`.** Once you generate a
  public domain (section 6), the create/list/download/delete endpoints are
  reachable by anyone who has the URL unless `API_TOKEN` is set.
- **Codex auth, if you set it up, is a copied OAuth session, not a scoped
  token.** See 1b -- know what you're sending before you POST it anywhere.
