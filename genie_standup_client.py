#!/usr/bin/env python3
"""
GENIE CLIENT STATUS SUMMARY
============================
Plain-English status update for your current book.
No jargon. Just what you need to know right now.

  python genie_standup_client.py
  python genie_standup_client.py --all    # show all books, not just the most recent
"""
import argparse, json, os, re, time

HERE     = os.path.dirname(os.path.abspath(__file__))
PROJECTS = os.path.join(HERE, "projects")
BOOKS    = os.path.join(HERE, "Books")


def _rj(path):
    try:
        return json.loads(open(path, encoding="utf-8").read())
    except Exception:
        return {}


def _all_project_folders():
    folders = []
    for base in [PROJECTS, BOOKS]:
        if os.path.isdir(base):
            for d in os.listdir(base):
                full = os.path.join(base, d)
                if os.path.isdir(full) and not d.startswith("_") and not d.startswith("."):
                    folders.append(full)
    seen, unique = set(), []
    for f in folders:
        k = os.path.normcase(os.path.abspath(f))
        if k not in seen:
            seen.add(k)
            unique.append(f)
    unique.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return unique


def _title(folder):
    name = os.path.basename(folder)
    for c in [os.path.join(folder, "project.json"),
              os.path.join(folder, "state", "project.json")]:
        if os.path.exists(c):
            d = _rj(c)
            t = d.get("title") or d.get("book_title") or d.get("locked_title")
            if t:
                return t
    lock = os.path.join(folder, "book_lock.md")
    if os.path.exists(lock):
        for line in open(lock, encoding="utf-8", errors="replace"):
            line = line.strip()
            if line.startswith("# "):
                t = line[2:].strip()
                t = re.sub(r'^(book\s+lock|lock|project|title)\s*[:\-—]\s*', '', t, flags=re.IGNORECASE).strip()
                return t
    return name.replace("-", " ").replace("_", " ").title()


def _ready_files(folder):
    files = []
    skip  = {".git", "__pycache__", "state", "research"}
    for root, dirs, flist in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
        for f in flist:
            if f.lower().endswith((".docx", ".pdf")):
                p  = os.path.join(root, f)
                mt = os.path.getmtime(p)
                files.append((mt, p))
    files.sort(reverse=True)
    return [(p, time.strftime("%b %d", time.localtime(mt))) for mt, p in files]


def _next_action(folder):
    p = os.path.join(folder, "state", "next_action.md")
    if not os.path.exists(p):
        return None
    try:
        for line in open(p, encoding="utf-8", errors="replace"):
            line = line.strip().lstrip("#- ").strip()
            if line:
                return line[:160]
    except Exception:
        pass
    return None


def _chapter_count(folder):
    count = 0
    skip  = {".git", "state", "research", "phase0", "__pycache__"}
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
        for f in files:
            n = f.lower()
            if n.endswith(".docx") and ("chapter" in n or "ch0" in n or "ch1" in n):
                count += 1
    return count


def _chapter_progress(folder):
    """Chapters written / total, read from the production record first.
    Order: state/completion.json (chapters_complete / chapters_total),
    then project.json chapters_total, then chapter source files in
    manuscript/ (NN-*.md or chNN.md, 01..89), then chapter DOCX files."""
    state = os.path.join(folder, "state")
    comp  = _rj(os.path.join(state, "completion.json")) if os.path.isdir(state) else {}
    proj  = _rj(os.path.join(folder, "project.json"))
    total = comp.get("chapters_total") or proj.get("chapters_total")
    done  = comp.get("chapters_complete")
    if done is None:
        ms = os.path.join(folder, "manuscript")
        nums = set()
        if os.path.isdir(ms):
            non_chapter = ("introduction", "front_matter", "front-matter",
                           "preface", "conclusion", "glossary", "appendix")
            for f in os.listdir(ms):
                fl = f.lower()
                if any(w in fl for w in non_chapter):
                    continue
                m = re.match(r"^(?:chapter[-_]|ch)?(\d{2})[-_.]", fl)
                if m and fl.endswith((".md", ".docx")) and 1 <= int(m.group(1)) <= 89:
                    nums.add(int(m.group(1)))
        done = len(nums) if nums else _chapter_count(folder)
    # NOTE: reaching chapters_total only means the learning chapters are drafted,
    # not that the whole manuscript is done (practice questions, answers, and
    # back matter can still be outstanding). Completion must be asserted
    # explicitly via completion.json, never inferred from chapter count alone.
    complete = bool(comp.get("manuscript_complete") or comp.get("complete")
                    or comp.get("manuscript_text_complete"))
    try:
        total = int(total) if total else None
        done  = int(done or 0)
    except (TypeError, ValueError):
        total, done = None, 0
    return complete, done, total, (comp.get("overall_status") or "").strip()


def _print_book(folder, index=None):
    state  = os.path.join(folder, "state")
    done, chs, total, overall = _chapter_progress(folder)
    title  = _title(folder)
    files  = _ready_files(folder)
    nxt    = _next_action(folder)

    label = f"  Book {index}: " if index else "  Current book: "
    print(f"{label}{title}")

    of_total = f" of {total}" if total else ""
    if done:
        print(f"    Status   :  COMPLETE — your manuscript is finished ({chs}{of_total} chapters)")
    elif chs > 0:
        print(f"    Status   :  IN PROGRESS — {chs}{of_total} chapter(s) written so far")
    else:
        print("    Status   :  JUST STARTED — writing is about to begin")
    if overall:
        print(f"    Detail   :  {overall[:200]}")

    if files:
        latest_path, latest_date = files[0]
        print(f"    Latest   :  {os.path.basename(latest_path)}  (saved {latest_date})")
        print(f"    Location :  {os.path.dirname(latest_path)}")
    else:
        print("    Files    :  none ready yet — come back after the first chapter")

    if nxt:
        print(f"    Next step:  {nxt}")

    if len(files) > 1:
        print(f"    All files ({len(files)} total):")
        for fp, fd in files[:5]:
            print(f"       - {os.path.basename(fp)}  ({fd})")
        if len(files) > 5:
            print(f"       ... and {len(files)-5} more in your project folder")


def main():
    ap = argparse.ArgumentParser(description="Genie client status summary")
    ap.add_argument("--all", action="store_true", help="show all books, not just the most recent")
    a = ap.parse_args()

    print()
    print("  ====================================================")
    print("   GENIE  --  Your Book Status")
    print(f"   {time.strftime('%A, %B %d, %Y')}")
    print("  ====================================================")

    folders = _all_project_folders()

    if not folders:
        print()
        print("  No books in progress yet.")
        print()
        print("  To start your first book, open Genie and say:")
        print('  "Write a book about [your topic]"')
        print()
        print("  Or run the intake wizard for a step-by-step guide:")
        print("  python genie_intake.py")
        print()
        return

    print()
    if a.all:
        for i, folder in enumerate(folders, 1):
            _print_book(folder, index=i)
            print()
    else:
        _print_book(folders[0])
        if len(folders) > 1:
            print()
            print(f"  You have {len(folders)-1} other book(s). Run with --all to see them all,")
            print("  or run: python genie_progress.py")

    print()
    print("  To continue: open Genie and say 'resume' or 'continue the book'")
    print("  For a full production report: say 'Genie, standup'")
    print()


if __name__ == "__main__":
    main()
