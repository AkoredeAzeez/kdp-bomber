# Codex Book Studio (bundled with Genie)​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​

A companion agent that runs on OpenAI Codex and generates book content, covers,
and A+ assets using the same house standards as Genie. It is part of the free
Community Edition: nothing to activate.

## Requirements
- OpenAI Codex, either flavor:
  - **Codex in VS Code (recommended)** - install VS Code, then the
    "Codex - OpenAI's coding agent" extension (`openai.chatgpt`), then sign in
    with your ChatGPT account inside the extension
  - **Codex CLI** - `npm i -g @openai/codex` (or `winget install OpenAI.Codex`
    on Windows), then `codex login`
- Python 3.8+ and: `pip install python-docx reportlab pillow "openai>=1.60"`
- An `OPENAI_API_KEY` in your environment (for cover and A+ artwork)

## Use it
Open this folder (`Genie\CodexBookStudio` in your home folder) in Codex -
in VS Code: File > Open Folder, then open the Codex panel and type `$`:

- `$generate-book`  - draft a manuscript to house rules and build a DOCX
- `$generate-cover` - generate cover art and assemble the KDP wrap PDF
- `$generate-aplus` - generate A+ modules as 970x600 masters

In the Codex CLI: run `codex` inside this folder and use the same `$` mentions.

## Notes
- Artwork here comes from OpenAI image models and spends your OpenAI credits.
  For research-gated, house-style production, finish books in Genie.
- There is no license check. This is the free Community Edition.
​‍‍​‌‍‌‌‍‍‌‌‍‌‌‌‍‍‍‍‍‌‍‍‍‌‍‌‌‌‌‍‌‌‍‌​
