"""
Delete a chapter's standalone DOCX preview after it has been merged into the
rolling manuscript.  The PDF preview is always kept (it is the review copy).
Safe to call multiple times -- idempotent.

Usage:
    python cleanup_chapter_docx.py <book_folder> <chapter_num>
    python cleanup_chapter_docx.py <book_folder> <path/to/chapter.docx>

Examples:
    python cleanup_chapter_docx.py "Books/My_Book" 3
    python cleanup_chapter_docx.py "Books/My_Book" "previews/chapter-03-preview.docx"
"""

import sys
from pathlib import Path


def cleanup_chapter_docx(book_folder, chapter_num=None, docx_path=None):
    folder = Path(book_folder)

    if docx_path:
        target = Path(docx_path) if Path(docx_path).is_absolute() else folder / docx_path
    elif chapter_num is not None:
        n = str(chapter_num).zfill(2)
        previews = folder / "previews"
        # Try all known naming patterns in order of likelihood
        candidates = [
            previews / f"chapter-{n}-preview.docx",
            previews / f"chapter_{n}.docx",
            previews / f"ch{n}.docx",
            folder / f"chapter-{n}-preview.docx",
            folder / f"chapter_{n}.docx",
        ]
        target = next((p for p in candidates if p.exists()), None)
        if target is None:
            print(f"[cleanup] Chapter {n} DOCX not found in {folder} -- already deleted or never created.")
            return True  # idempotent
    else:
        print("[cleanup] Error: supply chapter_num or docx_path.")
        return False

    if not target.exists():
        print(f"[cleanup] Already gone: {target.name}")
        return True

    size_kb = target.stat().st_size / 1024
    target.unlink()
    print(f"[cleanup] Deleted {target.name} ({size_kb:.0f} KB freed)")
    return True


def cleanup_all_rolled(book_folder, keep_latest=True):
    """
    Delete ALL chapter-NN-preview.docx files in <book_folder>/previews/.
    If keep_latest=True, the highest-numbered chapter DOCX is spared
    (it may still be the current working chapter).
    Returns (deleted_count, freed_bytes).
    """
    folder = Path(book_folder) / "previews"
    if not folder.exists():
        return 0, 0

    import re
    chapter_docx = sorted(
        folder.glob("chapter-*-preview.docx"),
        key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)) if re.search(r"(\d+)", p.stem) else 0
    )

    if keep_latest and len(chapter_docx) > 1:
        chapter_docx = chapter_docx[:-1]  # spare the last one

    deleted, freed = 0, 0
    for p in chapter_docx:
        freed += p.stat().st_size
        p.unlink()
        print(f"[cleanup] Deleted {p.name}")
        deleted += 1

    print(f"[cleanup] Removed {deleted} chapter DOCX(s), freed {freed / 1024:.0f} KB")
    return deleted, freed


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    book = sys.argv[1]

    if len(sys.argv) == 2:
        # No chapter arg -- clean all rolled chapters, spare the latest
        d, f = cleanup_all_rolled(book, keep_latest=True)
        sys.exit(0)

    arg2 = sys.argv[2]
    if arg2.endswith(".docx"):
        ok = cleanup_chapter_docx(book, docx_path=arg2)
    else:
        ok = cleanup_chapter_docx(book, chapter_num=arg2)

    sys.exit(0 if ok else 1)
