#!/usr/bin/env python3
"""
GENIE PROGRESS DASHBOARD
=========================
Shows all your books and where they stand, in plain English.
Also writes MY_BOOKS.md to the Genie folder so you always have
an up-to-date reference you can open in any text editor.

  python genie_progress.py           # full dashboard + write MY_BOOKS.md
  python genie_progress.py --brief   # short summary (used by the launcher)
"""
import argparse, json, os, re, time

HERE        = os.path.dirname(os.path.abspath(__file__))
PROJECTS    = os.path.join(HERE, "projects")
BOOKS_DIR   = os.path.join(HERE, "Books")
OUT_FILE    = os.path.join(HERE, "MY_BOOKS.md")


def _rj(path):
    try:
        return json.loads(open(path, encoding="utf-8").read())
    except Exception:
        return {}


def _title_from_folder(folder):
    name = os.path.basename(folder)
    # project.json
    for candidate in [os.path.join(folder, "project.json"),
                      os.path.join(folder, "state", "project.json")]:
        if os.path.exists(candidate):
            d = _rj(candidate)
            t = d.get("title") or d.get("book_title") or d.get("locked_title")
            if t:
                return t
    # book_lock.md
    lock = os.path.join(folder, "book_lock.md")
    if os.path.exists(lock):
        for line in open(lock, encoding="utf-8", errors="replace"):
            line = line.strip()
            if line.startswith("# "):
                t = line[2:].strip()
                t = re.sub(r'^(book\s+lock|lock|project|title)\s*[:\-—]\s*', '', t, flags=re.IGNORECASE).strip()
                return t
            if "title" in line.lower() and ":" in line:
                return line.split(":", 1)[1].strip().strip('"')
    # fallback: prettify folder name
    return name.replace("-", " ").replace("_", " ").title()


def _chapter_count(folder):
    count = 0
    skip = {".git", "state", "research", "phase0", "cover_db", "__pycache__"}
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
        for f in files:
            n = f.lower()
            if n.endswith(".docx") and ("chapter" in n or "ch0" in n or "ch1" in n):
                count += 1
    return count


def _latest_docx(folder):
    best = None
    skip = {".git", "__pycache__"}
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in skip and not d.startswith(".")]
        for f in files:
            if f.lower().endswith(".docx"):
                p  = os.path.join(root, f)
                mt = os.path.getmtime(p)
                if best is None or mt > best[0]:
                    best = (mt, p)
    return best


def _next_action(folder):
    p = os.path.join(folder, "state", "next_action.md")
    if not os.path.exists(p):
        return None
    try:
        lines = open(p, encoding="utf-8", errors="replace").read().strip().splitlines()
        for line in lines:
            line = line.strip().lstrip("#- ").strip()
            if line:
                return line[:140]
    except Exception:
        return None
    return None


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


def _status_label(complete, chapters, has_lock):
    if complete:
        return "COMPLETE"
    if chapters > 0:
        return "IN PROGRESS"
    if has_lock:
        return "STARTING"
    return "PLANNED"


def _all_projects():
    folders = []
    for base in [PROJECTS, BOOKS_DIR]:
        if os.path.isdir(base):
            for d in os.listdir(base):
                full = os.path.join(base, d)
                if os.path.isdir(full) and not d.startswith("_") and not d.startswith("."):
                    folders.append(full)
    if not folders:
        return []
    seen = set()
    unique = []
    for f in folders:
        key = os.path.normcase(os.path.abspath(f))
        if key not in seen:
            seen.add(key)
            unique.append(f)
    unique.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return unique


def _project_info(folder):
    state = os.path.join(folder, "state")
    done, chs, total, overall = _chapter_progress(folder)
    lock  = os.path.join(folder, "book_lock.md")
    best  = _latest_docx(folder)
    return {
        "title":       _title_from_folder(folder),
        "folder":      folder,
        "complete":    done,
        "chapters":    chs,
        "chapters_total": total,
        "overall":     overall,
        "has_lock":    os.path.exists(lock),
        "latest_mt":   best[0] if best else None,
        "latest_file": os.path.basename(best[1]) if best else None,
        "latest_date": time.strftime("%b %d", time.localtime(best[0])) if best else None,
        "next":        _next_action(folder),
    }


def report_brief():
    projects = _all_projects()
    if not projects:
        print("  No books yet — tell Genie your book title to start!")
        return
    print("  Your books:")
    for folder in projects[:6]:
        p  = _project_info(folder)
        st = _status_label(p["complete"], p["chapters"], p["has_lock"])
        tot = f" of {p['chapters_total']}" if p["chapters_total"] else ""
        ch = f"  ({p['chapters']}{tot} chapter(s) done)" if p["chapters"] else ""
        print(f"    [{st}] {p['title']}{ch}")
    if len(projects) > 6:
        print(f"    ... and {len(projects)-6} more  (run genie_progress.py for full list)")


def report_full():
    projects = _all_projects()
    date_str = time.strftime("%B %d, %Y")

    print()
    print(f"  {'='*54}")
    print(f"   YOUR BOOKS  |  {date_str}")
    print(f"  {'='*54}")

    if not projects:
        print()
        print("  No books started yet.")
        print("  Tell Genie your book title and where you want to sell it")
        print("  and production begins immediately.")
        print()
        return

    md = [f"# My Books\n\n*Updated: {date_str}*\n"]

    for folder in projects:
        p  = _project_info(folder)
        st = _status_label(p["complete"], p["chapters"], p["has_lock"])

        tot      = f" of {p['chapters_total']}" if p["chapters_total"] else ""
        ch_str   = f"{p['chapters']}{tot} chapter(s) written" if p['chapters'] else "not yet started"
        ov_str   = f"Detail: {p['overall'][:200]}" if p["overall"] else ""
        file_str = (f"Latest file: {p['latest_file']}  (saved {p['latest_date']})"
                    if p["latest_file"] else "")
        loc_str  = f"Folder: {p['folder']}" if p["latest_file"] else ""
        next_str = f"Next step: {p['next']}" if p["next"] else ""

        print()
        print(f"  {p['title']}")
        print(f"    Status    :  {st}")
        print(f"    Progress  :  {ch_str}")
        if file_str:
            print(f"    {file_str}")
        if loc_str:
            print(f"    {loc_str}")
        if next_str:
            print(f"    {next_str}")
        if ov_str:
            print(f"    {ov_str}")

        md.append(f"## {p['title']}")
        md.append(f"- **Status:** {st}")
        md.append(f"- **Progress:** {ch_str}")
        if file_str:
            md.append(f"- {file_str}")
        if loc_str:
            md.append(f"- {loc_str}")
        if next_str:
            md.append(f"- {next_str}")
        if ov_str:
            md.append(f"- {ov_str}")
        md.append("")

    print()
    print(f"  {'='*54}")
    print()

    try:
        open(OUT_FILE, "w", encoding="utf-8").write("\n".join(md) + "\n")
        print(f"  Dashboard saved to: MY_BOOKS.md")
        print(f"  (Open that file in any text editor to review your books.)")
    except Exception as e:
        print(f"  (Could not write MY_BOOKS.md: {e})")
    print()


def main():
    ap = argparse.ArgumentParser(description="Genie book progress dashboard")
    ap.add_argument("--brief", action="store_true",
                    help="one-liner per book (used by the launcher)")
    a = ap.parse_args()
    if a.brief:
        report_brief()
    else:
        report_full()


if __name__ == "__main__":
    main()
