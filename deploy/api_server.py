"""HTTP API for driving Genie from a frontend: queue a book by title,
list books and their status, download the finished files, delete when done.

Runs alongside deploy/entrypoint.sh's supervisor loop in the same
container (they share the /data volume). The supervisor owns actually
running Claude; this just manages the queue directory and a SQLite
bookkeeping table, and serves finished files.

Auth: every request needs `Authorization: Bearer <API_TOKEN>` where
API_TOKEN is a Railway variable you set yourself. If API_TOKEN isn't set,
auth is OFF and anyone with the public URL can create/delete books -- fine
for a first local test, not fine once this has a real domain.
"""
import json
import os
import re
import sqlite3
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Header, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
APP_DIR = Path(os.environ.get("APP_DIR", "/app"))
BOOKS_DIR = APP_DIR / "Books"
QUEUE_DIR = DATA_DIR / "queue"
PENDING_DIR = QUEUE_DIR / "pending"
ACTIVE_DIR = QUEUE_DIR / "active"
DONE_DIR = QUEUE_DIR / "done"
DB_PATH = DATA_DIR / "genie.db"
BLOCKED_SIGNAL = DATA_DIR / "NEEDS_OPERATOR"
CLAUDE_TOKEN_FILE = DATA_DIR / "claude_oauth_token.txt"
API_TOKEN = os.environ.get("API_TOKEN", "")

for d in (PENDING_DIR, ACTIVE_DIR, DONE_DIR):
    d.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Genie Book API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if not API_TOKEN:
    print("WARNING: API_TOKEN is not set -- every endpoint is open with no auth. "
          "Set the API_TOKEN Railway variable before exposing this publicly.")


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            brief TEXT NOT NULL,
            status TEXT NOT NULL,
            project_dir TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            completed_at TEXT,
            downloaded_at TEXT
        )
    """)
    return conn


def check_auth(authorization: Optional[str]):
    if not API_TOKEN:
        return
    expected = f"Bearer {API_TOKEN}"
    if authorization != expected:
        raise HTTPException(status_code=401, detail="missing or invalid Authorization header")


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return (slug or "book")[:40]


def guess_project_dir(title: str) -> Optional[str]:
    """Best-effort match of a completed queue item to its Books/<dir>.
    Genie names the project folder itself; we don't control it, so this is
    a heuristic (normalized-title match, else most-recently-modified
    folder), not a guarantee. Fine for the common case of one book being
    actively produced at a time."""
    if not BOOKS_DIR.exists():
        return None
    candidates = [d for d in BOOKS_DIR.iterdir() if d.is_dir()]
    if not candidates:
        return None
    norm_title = re.sub(r"[^a-z0-9]", "", title.lower())
    for d in candidates:
        norm_dir = re.sub(r"[^a-z0-9]", "", d.name.lower())
        if norm_dir and (norm_dir in norm_title or norm_title in norm_dir):
            return d.name
    candidates.sort(key=lambda d: d.stat().st_mtime, reverse=True)
    return candidates[0].name


def refresh_book(conn, row) -> sqlite3.Row:
    if row["status"] in ("complete", "deleted"):
        return row
    book_id = row["id"]
    fname = f"{book_id}.txt"
    new_status = row["status"]

    if (PENDING_DIR / fname).exists():
        new_status = "queued"
    elif (ACTIVE_DIR / fname).exists():
        new_status = "blocked" if BLOCKED_SIGNAL.exists() else "in_progress"
    elif list(DONE_DIR.glob(f"*{book_id}.txt")):
        new_status = "complete"

    if new_status != row["status"]:
        updates = {"status": new_status, "updated_at": now_iso()}
        if new_status == "complete":
            updates["completed_at"] = now_iso()
            updates["project_dir"] = guess_project_dir(row["title"])
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        conn.execute(f"UPDATE books SET {set_clause} WHERE id = ?",
                     (*updates.values(), book_id))
        conn.commit()
        row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    return row


class CreateBook(BaseModel):
    title: str
    marketplace: Optional[str] = None
    language: Optional[str] = None
    pages_per_chapter: Optional[str] = None
    max_pages: Optional[str] = None
    image_engine: Optional[str] = None
    non_negotiables: Optional[str] = None


def compose_brief(payload: CreateBook) -> str:
    lines = [
        f"Title: {payload.title}",
        f"Marketplace: {payload.marketplace or 'Amazon.com'}",
        f"Language: {payload.language or 'English (United States)'}",
    ]
    if payload.pages_per_chapter:
        lines.append(f"Target pages per chapter: {payload.pages_per_chapter}")
    if payload.max_pages:
        lines.append(f"Maximum total page count: {payload.max_pages}")
    lines.append(
        "Image engine: " + (payload.image_engine or
            "FLUX.1-schnell (Hugging Face, no API key needed) for every interior "
            "image. Do not attempt Google Flow or any browser-based image tool -- "
            "no logged-in browser is available on this server.")
    )
    if payload.non_negotiables:
        lines.append(f"Non-negotiables: {payload.non_negotiables}")
    return "\n".join(lines)


@app.get("/health")
def health():
    return {"ok": True}


class SetupToken(BaseModel):
    token: str


@app.get("/setup/status")
def setup_status():
    """Unauthenticated on purpose -- a frontend needs to know whether to show
    the 'paste your Claude token' screen before it has any token to send as
    auth. Reveals only a boolean, never the token itself."""
    have_token = bool(os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")) or CLAUDE_TOKEN_FILE.exists()
    return {"claude_token_set": have_token}


@app.post("/setup/claude-token")
def set_claude_token(payload: SetupToken, authorization: Optional[str] = Header(None)):
    """Called once by the frontend with the string the person got from
    running `claude setup-token` on their own machine (that step itself
    can't be done from a web form -- it's their subscription login). The
    supervisor loop in entrypoint.sh polls for this file and picks it up
    without needing a restart."""
    check_auth(authorization)
    token = payload.token.strip()
    if not token:
        raise HTTPException(400, "token is empty")
    CLAUDE_TOKEN_FILE.write_text(token, encoding="utf-8")
    try:
        os.chmod(CLAUDE_TOKEN_FILE, 0o600)
    except OSError:
        pass
    return {"ok": True}


@app.post("/books")
def create_book(payload: CreateBook, authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    book_id = f"{slugify(payload.title)}-{uuid.uuid4().hex[:6]}"
    brief = compose_brief(payload)
    (PENDING_DIR / f"{book_id}.txt").write_text(brief, encoding="utf-8")
    conn = db()
    conn.execute(
        "INSERT INTO books (id, title, brief, status, created_at, updated_at) "
        "VALUES (?, ?, ?, 'queued', ?, ?)",
        (book_id, payload.title, brief, now_iso(), now_iso()),
    )
    conn.commit()
    conn.close()
    return {"id": book_id, "status": "queued"}


@app.get("/books")
def list_books(authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    conn = db()
    rows = conn.execute("SELECT * FROM books ORDER BY created_at DESC").fetchall()
    rows = [refresh_book(conn, r) for r in rows]
    conn.close()
    return {
        "supervisor_blocked": BLOCKED_SIGNAL.exists(),
        "books": [dict(r) for r in rows],
    }


@app.get("/books/{book_id}")
def get_book(book_id: str, authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    conn = db()
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        raise HTTPException(404, "no such book")
    row = refresh_book(conn, row)
    conn.close()
    return dict(row)


def is_within(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def project_path_for(row) -> Path:
    if not row["project_dir"]:
        raise HTTPException(409, "no matching Books/ folder found yet for this book")
    p = (BOOKS_DIR / row["project_dir"]).resolve()
    if not is_within(p, BOOKS_DIR.resolve()):
        raise HTTPException(400, "invalid project path")
    return p


@app.get("/books/{book_id}/files")
def list_files(book_id: str, authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    conn = db()
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        raise HTTPException(404, "no such book")
    row = refresh_book(conn, row)
    conn.close()
    if not row["project_dir"]:
        return {"manifest": None, "files": []}

    project_dir = BOOKS_DIR / row["project_dir"]
    manifest = None
    manifest_path = project_dir / "publish_manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest = None

    files = []
    if manifest and manifest.get("files"):
        for label, relpath in manifest["files"].items():
            if relpath and (project_dir / relpath).exists():
                files.append({"label": label, "path": relpath})
    # Fallback / supplement: any top-level or build/ PDF, DOCX for in-progress previews
    for pattern in ("*.pdf", "*.docx", "build/*.pdf", "build/*.docx"):
        for f in project_dir.glob(pattern):
            rel = f.relative_to(project_dir).as_posix()
            if not any(existing["path"] == rel for existing in files):
                files.append({"label": rel, "path": rel})

    return {"manifest_summary": {
        "exact_title": manifest.get("exact_title") if manifest else None,
        "page_count": manifest.get("page_count") if manifest else None,
    } if manifest else None, "files": files}


@app.get("/books/{book_id}/download")
def download_file(book_id: str, path: str = Query(...),
                   authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    conn = db()
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        raise HTTPException(404, "no such book")
    project_dir = project_path_for(row)
    target = (project_dir / path).resolve()
    if not is_within(target, project_dir) or not target.is_file():
        raise HTTPException(404, "file not found")
    conn.execute("UPDATE books SET downloaded_at = ? WHERE id = ?", (now_iso(), book_id))
    conn.commit()
    conn.close()
    return FileResponse(target, filename=target.name)


@app.delete("/books/{book_id}")
def delete_book(book_id: str, force: bool = Query(False),
                 authorization: Optional[str] = Header(None)):
    check_auth(authorization)
    conn = db()
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        raise HTTPException(404, "no such book")
    row = refresh_book(conn, row)

    if row["status"] == "in_progress" and not force:
        conn.close()
        raise HTTPException(
            409,
            "book is still being produced -- pass ?force=true to delete anyway "
            "(this removes files but does not stop the running session)"
        )

    import shutil
    if row["project_dir"]:
        p = BOOKS_DIR / row["project_dir"]
        if p.exists():
            shutil.rmtree(p, ignore_errors=True)

    book_id_safe = row["id"]
    for d in (PENDING_DIR, ACTIVE_DIR):
        f = d / f"{book_id_safe}.txt"
        if f.exists():
            f.unlink()
    for f in DONE_DIR.glob(f"*{book_id_safe}.txt"):
        f.unlink()

    conn.execute("UPDATE books SET status = 'deleted', updated_at = ? WHERE id = ?",
                 (now_iso(), book_id_safe))
    conn.commit()
    conn.close()
    return {"id": book_id_safe, "status": "deleted"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
