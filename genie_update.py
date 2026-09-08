#!/usr/bin/env python3
"""
GENIE CLEAN UPDATER
===================
Applies a new Genie package to an existing install WITHOUT a scratch reinstall
and WITHOUT ever touching the client's own data.

What it does, in order:
  1. Verifies the source is a real Genie package (VERSION + AGENTS.md) and that
     it is being run from an existing Genie install root.
  2. Refuses downgrades unless --allow-downgrade is passed.
  3. Removes retired files: anything listed in the INSTALLED package_manifest.txt
     that is absent from the NEW package's manifest (so renamed or deleted files
     do not linger). If the install has no manifest (older install), the update
     is additive-only and nothing is removed.
  4. Copies every file from the new package over the install.
  5. NEVER touches, in any step: Books/, projects/, cover_db/, state/, or
     .git/.
  6. Re-checks dependencies (genie_bootstrap.py --deps-only) so new requirements
     install automatically.

Usage (from the Genie install root):
  python genie_update.py <path-to-new-package.zip>     # normal update
  python genie_update.py <path-to-new-package-folder>  # folder form works too
  python genie_update.py <src> --dry-run               # show actions, change nothing
  python genie_update.py --make-manifest               # BUILD TIME ONLY: run inside
                                                       # a built package folder right
                                                       # before zipping; writes
                                                       # package_manifest.txt

This tool only applies Genie Community Edition packages to the install it
lives in. It does not export or relocate anything.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST_NAME = "package_manifest.txt"

# Paths (relative to install root, posix separators, case-insensitive match)
# that the updater must never create, overwrite, or delete. Client data and
# per-install state live here.
PRESERVE = (
    "books/",
    "projects/",
    "cover_db/",
    "state/",
    ".git/",
)

# Excluded from --make-manifest in addition to PRESERVE: build/runtime cruft
# that must never ship inside a package.
MANIFEST_EXCLUDE = ("__pycache__/", ".venv/", "thumbs.db", ".ds_store",
                    "desktop.ini")


def _norm(rel):
    return rel.replace("\\", "/").lstrip("/").lower()


def _is_preserved(rel):
    n = _norm(rel)
    for p in PRESERVE:
        if p.endswith("/"):
            if n.startswith(p) or n + "/" == p:
                return True
        elif n == p:
            return True
    return False


def _is_manifest_excluded(rel):
    n = _norm(rel)
    if _is_preserved(n):
        return True
    for p in MANIFEST_EXCLUDE:
        if p.endswith("/"):
            if ("/" + n).find("/" + p) >= 0 or n.startswith(p):
                return True
        elif n == p or n.endswith("/" + p):
            return True
    return False


def _read_version(root):
    p = os.path.join(root, "VERSION")
    try:
        return open(p, encoding="utf-8-sig").read().strip()
    except Exception:
        return None


def _version_tuple(v):
    parts = []
    for piece in (v or "0").replace("-", ".").split("."):
        num = "".join(ch for ch in piece if ch.isdigit())
        parts.append(int(num) if num else 0)
    return tuple(parts) or (0,)


def make_manifest(root):
    """Walk a built package folder and write package_manifest.txt inside it."""
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        rel_dir = "" if rel_dir == "." else rel_dir.replace("\\", "/") + "/"
        # prune preserved/excluded directories so the walk never descends
        dirnames[:] = [d for d in dirnames
                       if not _is_manifest_excluded(rel_dir + d + "/")]
        for f in filenames:
            rel = rel_dir + f
            if rel == MANIFEST_NAME or _is_manifest_excluded(rel):
                continue
            entries.append(rel)
    entries.sort()
    with open(os.path.join(root, MANIFEST_NAME), "w", encoding="utf-8") as fh:
        fh.write("\n".join(entries) + "\n")
    print(f"[manifest] wrote {MANIFEST_NAME} with {len(entries)} files")
    return entries


def _load_manifest(path):
    if not os.path.exists(path):
        return None
    lines = [ln.strip() for ln in open(path, encoding="utf-8-sig")]
    return [ln for ln in lines if ln]


def _stage_source(src, tmpdir):
    """Return a folder containing the new package's files (extracting a zip if
    needed, and stripping a single wrapping top-level folder)."""
    if os.path.isdir(src):
        root = src
    else:
        if not zipfile.is_zipfile(src):
            sys.exit(f"[error] not a folder or zip: {src}")
        with zipfile.ZipFile(src) as z:
            for m in z.namelist():
                n = m.replace("\\", "/")
                if n.startswith("/") or ".." in n.split("/"):
                    sys.exit(f"[error] unsafe path inside zip: {m}")
            z.extractall(tmpdir)
        root = tmpdir
    # unwrap a single top-level folder (Genie-5.4/AGENTS.md style)
    while True:
        items = [i for i in os.listdir(root)
                 if i not in ("__MACOSX",) and not i.startswith(".DS_")]
        if (len(items) == 1 and os.path.isdir(os.path.join(root, items[0]))
                and not os.path.exists(os.path.join(root, "AGENTS.md"))):
            root = os.path.join(root, items[0])
        else:
            break
    return root


def _iter_package_files(pkg_root):
    for dirpath, dirnames, filenames in os.walk(pkg_root):
        rel_dir = os.path.relpath(dirpath, pkg_root)
        rel_dir = "" if rel_dir == "." else rel_dir.replace("\\", "/") + "/"
        dirnames[:] = [d for d in dirnames
                       if not _is_manifest_excluded(rel_dir + d + "/")]
        for f in filenames:
            rel = rel_dir + f
            if _is_manifest_excluded(rel):
                continue
            yield rel, os.path.join(dirpath, f)


GENIE_MASTER_MARKER = "UAPF Codex operating instructions"

def _guard_root_agents(install_dir, correct_src):
    """The install root's AGENTS.md is the Genie master (Claude + Codex operating
    instructions). It must never be the shorter CodexBookStudio/AGENTS.md. If a
    bad layout ever lands the wrong file at the root, restore it from the package's
    correct copy. Idempotent and safe: a correct file is left untouched."""
    root_ag = os.path.join(install_dir, "AGENTS.md")
    try:
        cur = open(root_ag, encoding="utf-8-sig").read()
    except Exception:
        cur = ""
    if GENIE_MASTER_MARKER in cur:
        return  # already the Genie master (a wired enforcement/tier block may precede it)
    if correct_src and os.path.exists(correct_src):
        try:
            good = open(correct_src, encoding="utf-8-sig").read()
        except Exception:
            good = ""
        if GENIE_MASTER_MARKER in good:
            with open(root_ag, "w", encoding="utf-8") as f:
                f.write(good)
            print("[guard] root AGENTS.md was not the Genie master; restored it from the package.")


def apply_update(src, dry_run=False, allow_downgrade=False):
    # 1. sanity: are we inside a Genie install? (older installs predate
    # genie_bootstrap.py, so accept the .agents skill tree as proof too)
    if not (os.path.exists(os.path.join(HERE, "AGENTS.md"))
            and (os.path.exists(os.path.join(HERE, "genie_bootstrap.py"))
                 or os.path.isdir(os.path.join(HERE, ".agents")))):
        sys.exit("[error] run this from the Genie install root "
                 "(AGENTS.md plus genie_bootstrap.py or .agents/ not found)")

    with tempfile.TemporaryDirectory(prefix="genie_upd_") as tmp:
        pkg = _stage_source(src, tmp)
        if not (os.path.exists(os.path.join(pkg, "AGENTS.md"))
                and os.path.exists(os.path.join(pkg, "VERSION"))):
            sys.exit("[error] source is not a Genie package "
                     "(missing AGENTS.md/VERSION)")

        old_v, new_v = _read_version(HERE), _read_version(pkg)
        print(f"[update] installed version: {old_v or 'unknown'}   "
              f"package version: {new_v or 'unknown'}")
        if (old_v and new_v and not allow_downgrade
                and _version_tuple(new_v) < _version_tuple(old_v)):
            sys.exit("[error] package is OLDER than the installed version; "
                     "pass --allow-downgrade only if that is intended")

        # 2. removals: old manifest minus new manifest
        new_manifest = _load_manifest(os.path.join(pkg, MANIFEST_NAME))
        if new_manifest is None:
            new_manifest = [rel for rel, _ in _iter_package_files(pkg)]
            print("[update] package has no manifest; derived one from its "
                  "contents")
        old_manifest = _load_manifest(os.path.join(HERE, MANIFEST_NAME))
        removed = 0
        if old_manifest is None:
            print("[update] no installed manifest (older install): "
                  "additive update, nothing will be removed")
        else:
            new_set = {_norm(r) for r in new_manifest}
            for rel in old_manifest:
                if _norm(rel) in new_set or _is_preserved(rel):
                    continue
                target = os.path.join(HERE, rel.replace("/", os.sep))
                if os.path.isfile(target):
                    print(f"[remove] {rel}")
                    removed += 1
                    if not dry_run:
                        os.remove(target)
        # sweep now-empty directories left by removals
        if removed and not dry_run:
            for dirpath, dirnames, filenames in os.walk(HERE, topdown=False):
                rel = os.path.relpath(dirpath, HERE).replace("\\", "/") + "/"
                if rel == "./" or _is_preserved(rel):
                    continue
                if not os.listdir(dirpath):
                    os.rmdir(dirpath)

        # 3. copy everything from the package over the install
        copied = 0
        for rel, srcfile in _iter_package_files(pkg):
            if _is_preserved(rel):
                print(f"[skip-preserved] {rel}")
                continue
            dest = os.path.join(HERE, rel.replace("/", os.sep))
            copied += 1
            if not dry_run:
                os.makedirs(os.path.dirname(dest) or HERE, exist_ok=True)
                shutil.copy2(srcfile, dest)
        print(f"[update] files copied: {copied}   files removed: {removed}"
              + ("   (DRY RUN, nothing changed)" if dry_run else ""))

        # integrity guard: the root AGENTS.md must be the Genie master, never the
        # CodexBookStudio/AGENTS.md file. If any odd package layout or copy ever
        # lands the wrong file here, repair it from the package's correct copy.
        if not dry_run:
            _guard_root_agents(HERE, os.path.join(pkg, "AGENTS.md"))

        # 4. record the new manifest in the install
        if not dry_run:
            with open(os.path.join(HERE, MANIFEST_NAME), "w",
                      encoding="utf-8") as fh:
                fh.write("\n".join(new_manifest) + "\n")

    if dry_run:
        print("[done] dry run complete.")
        return

    # 5. dependencies for the new version
    print("[update] checking dependencies for the new version ...")
    subprocess.run([sys.executable, os.path.join(HERE, "genie_bootstrap.py"),
                    "--deps-only"])

    print(f"[done] Genie updated to version {_read_version(HERE)}. "
          "Books, projects, databases, and state were not touched.")


def main():
    ap = argparse.ArgumentParser(description="Genie clean updater")
    ap.add_argument("source", nargs="?",
                    help="new package: a .zip or an extracted folder")
    ap.add_argument("--make-manifest", action="store_true",
                    help="build time only: write package_manifest.txt for the "
                         "package folder this script sits in")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--allow-downgrade", action="store_true")
    a = ap.parse_args()

    if a.make_manifest:
        make_manifest(HERE)
        return
    if not a.source:
        ap.error("give the path to the new package (.zip or folder), "
                 "or --make-manifest at build time")
    apply_update(a.source, dry_run=a.dry_run,
                 allow_downgrade=a.allow_downgrade)


if __name__ == "__main__":
    main()
