#!/usr/bin/env python3
"""
GENIE INTAKE WIZARD
===================
Guided Q&A that walks you through starting a new book.
No special format needed — just answer the questions.
At the end, Genie gives you a ready-to-paste book brief.

  python genie_intake.py
"""
import sys, os

MARKETPLACES = {
    "1": ("amazon.com",    "Amazon USA (most popular)"),
    "2": ("amazon.co.uk",  "Amazon UK"),
    "3": ("amazon.ca",     "Amazon Canada"),
    "4": ("amazon.com.au", "Amazon Australia"),
    "5": ("amazon.de",     "Amazon Germany"),
    "6": ("amazon.in",     "Amazon India"),
    "7": ("amazon.co.jp",  "Amazon Japan"),
}

LANGUAGES = {
    "1": "English",
    "2": "Spanish",
    "3": "French",
    "4": "German",
    "5": "Portuguese",
    "6": "Italian",
    "7": "Dutch",
    "8": "Arabic",
}


def ask(label, hint=None, required=False):
    suffix = f"  (example: {hint})" if hint else ""
    if not required:
        suffix += "  [press Enter to skip]" if not hint else "  [or press Enter to skip]"
    try:
        val = input(f"\n  {label}{suffix}\n  > ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\n  Intake cancelled. Come back when you are ready!\n")
        sys.exit(0)
    return val or None


def ask_menu(label, options, default_key="1"):
    print(f"\n  {label}\n")
    for k, v in options.items():
        desc = v if isinstance(v, str) else v[1]
        marker = "  <-- default" if k == default_key else ""
        print(f"    {k}.  {desc}{marker}")
    try:
        val = input(f"\n  Type a number (or press Enter for {default_key}): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n\n  Intake cancelled. Come back when you are ready!\n")
        sys.exit(0)
    return val if val in options else default_key


def divider(step, total, label):
    print()
    print(f"  {'='*52}")
    print(f"   Step {step} of {total} — {label}")
    print(f"  {'='*52}")


def main():
    print()
    print("  ====================================================")
    print("   GENIE  --  New Book Wizard")
    print("  ====================================================")
    print()
    print("  Answer a few quick questions and Genie will prepare")
    print("  everything you need to start writing your book.")
    print("  (Press Ctrl+C at any time to cancel.)")

    # Step 1 — Title / topic
    divider(1, 6, "Your Book")
    title = None
    while not title:
        title = ask("What is your book title or main topic?",
                    hint="The Complete Guide to Home Canning", required=True)
        if not title:
            print("  A title or topic is required — please enter something.")

    # Step 2 — Marketplace
    divider(2, 6, "Where Will You Sell It?")
    mkt_key  = ask_menu("Choose your primary marketplace:", MARKETPLACES, default_key="1")
    mkt_url, mkt_name = MARKETPLACES[mkt_key]

    # Step 3 — Language
    divider(3, 6, "Book Language")
    lang_key = ask_menu("What language should the book be written in?", LANGUAGES, default_key="1")
    language = LANGUAGES[lang_key]

    # Step 4 — Length
    divider(4, 6, "Book Length")
    print("  Not sure? Leave both blank and Genie will plan the right length")
    print("  based on the niche and what sells best in your market.")

    pages_raw    = ask("Total page count?",       hint="150")
    pages_ch_raw = ask("Pages per chapter?",      hint="12")

    try:    total_pages = int(pages_raw)
    except: total_pages = None
    try:    pages_per_chapter = int(pages_ch_raw)
    except: pages_per_chapter = None

    # Step 5 — Audience
    divider(5, 6, "Who Is This Book For?")
    audience = ask("Describe your reader:", hint="busy parents, complete beginners, seniors over 60")

    # Step 6 — Special notes
    divider(6, 6, "Anything Else?")
    print("  Topics to cover, things to avoid, tone, style, competing books,")
    print("  or any other detail that would help Genie write a better book.")
    notes = ask("Special requirements or notes:")

    # Build the brief
    brief_parts = [f'Write a book: "{title}"']
    brief_parts.append(f"Marketplace: {mkt_url}  ({mkt_name})")
    brief_parts.append(f"Language: {language}")
    if total_pages:
        brief_parts.append(f"Target page count: {total_pages} pages")
    if pages_per_chapter:
        brief_parts.append(f"Pages per chapter: {pages_per_chapter}")
    if audience:
        brief_parts.append(f"Target audience: {audience}")
    if notes:
        brief_parts.append(f"Special requirements: {notes}")

    # Show the brief
    print()
    print()
    print("  ====================================================")
    print("   YOUR BOOK BRIEF")
    print("   Copy everything between the lines and paste it")
    print("   into Genie's chat window to start your book.")
    print("  ====================================================")
    print()
    for line in brief_parts:
        print(f"  {line}")
    print()
    print("  ====================================================")
    print()
    print("  That is it! Paste the lines above into Genie's chat")
    print("  and your book production starts automatically.")
    print()

    # Optionally save to file
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "my_book_brief.txt")
    try:
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(brief_parts) + "\n")
        print(f"  Brief also saved to: my_book_brief.txt")
        print(f"  (You can open that file to copy from it anytime.)")
        print()
    except Exception:
        pass


if __name__ == "__main__":
    main()
