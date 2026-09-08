#!/usr/bin/env bash
# Supervisor loop for running Genie unattended on Railway.
#
# Starts (or resumes) one long-lived Claude Code conversation and keeps
# nudging it forward turn by turn. If a turn fails because the Claude
# subscription's usage limit was hit, it backs off and retries instead of
# giving up. There is no external "is the book done yet" signal shipped in
# this Community package (scripts/project_status.py referenced in CLAUDE.md
# does not exist here), so this loop runs until you stop the Railway
# service yourself -- check Books/<project>/ on the volume periodically.
set -uo pipefail

DATA_DIR="/data"
APP_DIR="/app"
LOG_DIR="$DATA_DIR/logs"
mkdir -p "$LOG_DIR" "$DATA_DIR/home"

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

# --- Book brief (first boot only) -----------------------------------------
BRIEF_FILE="$DATA_DIR/book_brief.txt"
if [ ! -f "$BRIEF_FILE" ]; then
  if [ -z "${BOOK_BRIEF:-}" ]; then
    log "FATAL: no book brief on the volume and no BOOK_BRIEF variable set."
    log "Set the BOOK_BRIEF Railway variable (title, marketplace, language,"
    log "pages/chapter, max page count, image-engine choice, any non-negotiables)"
    log "before the first boot, then redeploy."
    exit 1
  fi
  printf '%s' "$BOOK_BRIEF" > "$BRIEF_FILE"
  log "Saved book brief to $BRIEF_FILE"
fi

STARTED_MARKER="$DATA_DIR/.genie_started"
RETRY_SECONDS="${RETRY_SECONDS:-1800}"   # backoff when a limit/error is hit
IDLE_SECONDS="${IDLE_SECONDS:-15}"       # pause between clean turns
CONTINUE_PROMPT="Resume production automatically. Keep following auto-advance and the chapter-by-chapter build law without waiting for confirmation, until the book is fully drafted, formatted, gated, and its KDP metadata package is delivered. If you are genuinely blocked on something only the operator can do (payment, credentials, a final Publish click, a HIGH RISK trademark result), record it clearly in the decision log and state exactly what you did instead, then stop."

while true; do
  if [ -f "$STARTED_MARKER" ]; then
    log "Resuming existing Genie session (claude --continue)..."
    OUTPUT=$(claude -p --continue "$CONTINUE_PROMPT" \
      --permission-mode bypassPermissions \
      --output-format json \
      2> "$LOG_DIR/stderr.last.log")
    EXIT_CODE=$?
  else
    log "Starting new Genie session from the book brief..."
    OUTPUT=$(claude -p "$(cat "$BRIEF_FILE")" \
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
