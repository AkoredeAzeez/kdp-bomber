#!/usr/bin/env bash
# Supervisor loop for running Genie unattended on Railway, across multiple
# books, driven by a queue on the volume and (optionally) the HTTP API in
# deploy/api_server.py.
#
# Books are read from a queue directory on the volume:
#   /data/queue/pending/<id>.txt   drop/POST a new brief here to enqueue it
#   /data/queue/active/<id>.txt    the brief currently being worked (one at a time)
#   /data/queue/done/<ts>_<id>.txt finished briefs, archived
#
# Add a book to the queue without a frontend:
#   railway volume files upload ./my_brief.txt /queue/pending/<any-id>.txt
# Or via the API: POST /books {"title": "..."} -- see deploy/api_server.py.
#
# Completion is detected via marker files Genie is instructed to create
# (this package doesn't ship the scripts/project_status.py completion gate
# CLAUDE.md references, so we can't check that):
#   $DATA_DIR/BOOK_COMPLETE    -> archive this book, start the next queued one
#   $DATA_DIR/NEEDS_OPERATOR   -> stop nudging, wait for you to intervene
# If a turn fails because the Claude subscription's usage limit was hit, it
# backs off and retries instead of giving up.
set -uo pipefail

DATA_DIR="/data"
APP_DIR="/app"
LOG_DIR="$DATA_DIR/logs"
QUEUE_DIR="$DATA_DIR/queue"
PENDING_DIR="$QUEUE_DIR/pending"
ACTIVE_DIR="$QUEUE_DIR/active"
DONE_DIR="$QUEUE_DIR/done"
STARTED_MARKER="$DATA_DIR/.genie_started"
COMPLETE_SIGNAL="$DATA_DIR/BOOK_COMPLETE"
BLOCKED_SIGNAL="$DATA_DIR/NEEDS_OPERATOR"

mkdir -p "$LOG_DIR" "$DATA_DIR/home" "$PENDING_DIR" "$ACTIVE_DIR" "$DONE_DIR"

log() { echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $*"; }

if [ -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]; then
  log "FATAL: CLAUDE_CODE_OAUTH_TOKEN is not set."
  log "On your own machine: run 'claude setup-token', log in with your Claude subscription,"
  log "then paste the printed token into this Railway service's variables."
  exit 1
fi
export CLAUDE_CODE_OAUTH_TOKEN

# --- Persist Genie's output/state across restarts and redeploys ----------
# Railway volumes mount at one path (/data here). Move each of these dirs
# onto the volume once, then symlink /app/<dir> -> /data/<dir> so every
# Genie script keeps reading/writing its normal relative paths.
for dir in Books state cover_db catalog; do
  mkdir -p "$DATA_DIR/$dir"
  if [ -e "$APP_DIR/$dir" ] && [ ! -L "$APP_DIR/$dir" ]; then
    cp -rn "$APP_DIR/$dir/." "$DATA_DIR/$dir/" 2>/dev/null || true
    rm -rf "$APP_DIR/$dir"
  fi
  ln -sfn "$DATA_DIR/$dir" "$APP_DIR/$dir"
done

cd "$APP_DIR"

# --- Start the HTTP API alongside the supervisor (shares this volume) ----
DATA_DIR="$DATA_DIR" APP_DIR="$APP_DIR" python3 "$APP_DIR/deploy/api_server.py" \
  >> "$LOG_DIR/api_server.log" 2>&1 &
API_PID=$!
log "API server started (pid $API_PID), logging to $LOG_DIR/api_server.log"

# One-time migration: if BOOK_BRIEF is still set (the old single-book setup),
# seed it as the first queue entry instead of using it directly.
if [ -n "${BOOK_BRIEF:-}" ] && [ ! -f "$DATA_DIR/.env_brief_seeded" ]; then
  printf '%s' "$BOOK_BRIEF" > "$PENDING_DIR/env-seed-$(date -u +%s).txt"
  touch "$DATA_DIR/.env_brief_seeded"
  log "Seeded the BOOK_BRIEF variable into the queue. You can remove that variable now; the queue drives production from here on."
fi

RETRY_SECONDS="${RETRY_SECONDS:-1800}"           # backoff on a limit/error
IDLE_SECONDS="${IDLE_SECONDS:-15}"               # pause between clean turns
IDLE_QUEUE_SECONDS="${IDLE_QUEUE_SECONDS:-600}"  # pause when the queue is empty
BLOCKED_POLL_SECONDS="${BLOCKED_POLL_SECONDS:-3600}"  # pause while blocked on you

COMPLETION_INSTRUCTION="Operational note for this unattended deployment: when this book's manuscript, formatting gates, and KDP metadata package are fully complete and delivered, run a Bash command to create an empty file at exactly this path: touch $COMPLETE_SIGNAL -- that signals the supervisor to archive this book and start the next queued one. If you are genuinely blocked on something only the operator can do (payment, credentials, a final Publish click, a HIGH RISK trademark result) and there is no further independent progress to make right now, run: touch $BLOCKED_SIGNAL -- that pauses the supervisor until the operator clears it. Do not create either file unless one of those conditions is actually true."
CONTINUE_PROMPT="Resume production automatically. Keep following auto-advance and the chapter-by-chapter build law without waiting for confirmation. $COMPLETION_INSTRUCTION"

while true; do
  # --- Blocked on the operator: stop nudging, just wait ------------------
  if [ -f "$BLOCKED_SIGNAL" ]; then
    log "Blocked on an operator-only action -- see the decision/blocker log in Books/<project>/."
    log "Delete $BLOCKED_SIGNAL (e.g. 'railway volume files delete /NEEDS_OPERATOR') once handled, to resume."
    sleep "$BLOCKED_POLL_SECONDS"
    continue
  fi

  # --- Previous book finished: archive it and clear state ----------------
  if [ -f "$COMPLETE_SIGNAL" ]; then
    log "Book complete."
    for f in "$ACTIVE_DIR"/*.txt; do
      [ -e "$f" ] || continue
      mv "$f" "$DONE_DIR/$(date -u +%Y%m%dT%H%M%SZ)_$(basename "$f")"
    done
    rm -f "$COMPLETE_SIGNAL" "$STARTED_MARKER"
  fi

  # --- Nothing in progress: pull the next queued brief --------------------
  if [ ! -f "$STARTED_MARKER" ]; then
    NEXT=$(ls -1 "$PENDING_DIR" 2>/dev/null | sort | head -n1 || true)
    if [ -z "$NEXT" ]; then
      log "Queue empty. POST /books or drop a brief into $PENDING_DIR to start the next book. Checking again in ${IDLE_QUEUE_SECONDS}s."
      sleep "$IDLE_QUEUE_SECONDS"
      continue
    fi
    mv "$PENDING_DIR/$NEXT" "$ACTIVE_DIR/$NEXT"
    log "Starting next queued book: $NEXT"
  fi

  ACTIVE_FILE=$(ls -1 "$ACTIVE_DIR"/*.txt 2>/dev/null | head -n1 || true)

  if [ -f "$STARTED_MARKER" ]; then
    log "Resuming existing Genie session (claude --continue)..."
    OUTPUT=$(claude -p --continue "$CONTINUE_PROMPT" \
      --permission-mode bypassPermissions \
      --output-format json \
      2> "$LOG_DIR/stderr.last.log")
    EXIT_CODE=$?
  else
    log "Starting new Genie session from $ACTIVE_FILE..."
    OUTPUT=$(claude -p "$(cat "$ACTIVE_FILE")

$COMPLETION_INSTRUCTION" \
      --permission-mode bypassPermissions \
      --output-format json \
      2> "$LOG_DIR/stderr.last.log")
    EXIT_CODE=$?
    touch "$STARTED_MARKER"
  fi

  {
    echo "=== $(date -u) exit=$EXIT_CODE ==="
    echo "$OUTPUT"
  } >> "$LOG_DIR/session_history.log"

  COMBINED="$OUTPUT
$(cat "$LOG_DIR/stderr.last.log" 2>/dev/null)"

  # Best-effort detection -- the exact wording hasn't been verified against
  # a real limit hit. First time this fires, check stderr.last.log and
  # tighten this pattern if it didn't match what you actually see.
  if echo "$COMBINED" | grep -qiE "usage limit|rate limit|quota|resets? (at|in)|try again (later|in)"; then
    log "Looks like a usage limit was hit. Sleeping ${RETRY_SECONDS}s, then retrying."
    log "(See $LOG_DIR/stderr.last.log for the exact message.)"
    sleep "$RETRY_SECONDS"
    continue
  fi

  if [ "$EXIT_CODE" -ne 0 ]; then
    log "claude exited with code $EXIT_CODE (not a recognized limit message)."
    log "Sleeping ${RETRY_SECONDS}s and retrying. Inspect $LOG_DIR/stderr.last.log."
    sleep "$RETRY_SECONDS"
    continue
  fi

  log "Turn finished cleanly. Continuing in ${IDLE_SECONDS}s (stop the Railway service to halt)."
  sleep "$IDLE_SECONDS"
done
