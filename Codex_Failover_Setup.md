# Codex Failover - one-time setup (so your books never stall when Claude hits a limit)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

Genie uses **Claude Code** as the primary writer and **Codex** as an automatic backup. When Claude
hits a usage/rate limit mid-book, Genie hands the work to Codex, which continues from the saved
state and hands back to Claude when it's available again. Codex can also **start** new books during
a total Claude outage (with a trademark screen you confirm before publishing).

## One-time setup on your machine

1. **Install the Codex CLI** (Windows):
   ```
   winget install --id OpenAI.Codex
   ```
2. **Sign in with your ChatGPT account:**
   ```
   codex login --device-auth
   ```
   (open the URL it prints and enter the code)
3. **Approve the Codex helper once:** in your Genie project folder run `claude`, approve the
   **codex** MCP server when prompted (or type `/mcp` -> codex -> Enable), then `/exit`.

Check it's wired:
```
python ".agents/skills/uapf-codex-failover/genie_failover.py" health --project "<your book folder>"
```

## How it behaves

- **Claude hits a limit -> Codex continues** the current book from the locked state, then hands back.
- **Total Claude outage -> Codex can start a book** (`intake`), but the **title is UNVERIFIED and
  publish is BLOCKED** until you run the trademark screen (Claude, or ChatGPT - see
  `Trademark_Screen_When_Claude_Unavailable.md`) and record it. Codex never clears a title.
- **Images:** Claude uses Google Flow; Codex uses ChatGPT Image 2.0. During a full outage Codex may
  use a free headless fallback (Z-Image) that is flagged for premium regeneration when Claude returns.

## Good to know

- Codex uses **your own ChatGPT account** - no extra API key for normal use.
- **You confirm every publish.** Codex never publishes on its own and never clears a trademark.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
