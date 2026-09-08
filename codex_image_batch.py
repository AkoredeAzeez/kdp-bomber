#!/usr/bin/env python3
"""
IMAGE BATCH - fast whole-book image generation (operator directive 2026-08-21)
=============================================================================
Generates a book's images as a batch. Concurrency depends on the ENGINE, and
this is TESTED, not assumed:

  --engine codex        SERIALIZED (1 at a time). Codex CANNOT run multiple
                        `codex exec` sessions at once on one machine: they
                        contend for shared local-runtime singletons (the
                        node_repl pipe, computer-use backend, imagegen
                        post-processing) and abort mid-render (verified: 0/3
                        delivered concurrently). Codex speed comes from reduced
                        reasoning, not parallelism.
  --engine pollinations|flux|sdxl|qwen   TRUE PARALLEL pool. These are
                        stateless HTTP calls, so N workers really do overlap.
                        Throughput is still bounded by the provider's rate
                        limit; the pool is capped at 8, default 4.

  python codex_image_batch.py --jobs jobs.json --dest <dir> --engine flux --workers 6
  python codex_image_batch.py --jobs jobs.json --dest <dir> --engine codex   (serial)
  python codex_image_batch.py --dry-run --jobs jobs.json --engine flux --workers 6

jobs.json: [{"name": "IMG-1", "prompt": "photoreal ..."}, ...]

Every worker runs isolated (own temp / own output path) and delivers its own
file explicitly; the shared-folder "newest image" heuristic is never used
(it would let workers steal each other's output). A worker that produces no
file fails cleanly for the fallback chain; images stay compulsory for the
finished book.
"""
import argparse, concurrent.futures as cf, json, os, shutil, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))

def find_codex():
    cli = shutil.which("codex")
    if cli:
        return cli
    if os.name == "nt":
        appdata = os.environ.get("APPDATA") or os.path.expanduser(r"~\AppData\Roaming")
        for ext in (".CMD", ".cmd", ".exe", ".ps1"):
            c = os.path.join(appdata, "npm", "codex" + ext)
            if os.path.exists(c):
                return c
    return None

def _run(cmd, timeout):
    # encoding + errors are REQUIRED: codex prints smart quotes/unicode that
    # Windows' default cp1252 reader thread cannot decode, which crashes stdout
    # capture and can abort codex mid-render.
    if os.name == "nt":
        return subprocess.run(subprocess.list2cmdline(cmd), capture_output=True,
                              text=True, encoding="utf-8", errors="replace",
                              stdin=subprocess.DEVNULL, timeout=timeout, shell=True)
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, timeout=timeout)

RATE_HINTS = ("rate limit", "usage limit", "429", "quota", "resource_exhausted",
              "too many requests")

def _deliver_compress(src, dest, name, polish):
    args = [sys.executable, os.path.join(HERE, "codex_image_deliver.py"),
            "--compress-only", src] + (["--polish"] if polish else [])
    _run(args, 180)
    # deliver writes <src-stem>.jpg; move it to dest/name.jpg
    made = os.path.splitext(src)[0] + ".jpg"
    os.makedirs(dest, exist_ok=True)
    final = os.path.join(dest, name + ".jpg")
    if os.path.exists(made):
        shutil.move(made, final)
        return final
    return None

def gen_codex(job, dest, cli, timeout, retries):
    name = job["name"]
    prompt = (job["prompt"].rstrip() +
              "\nSave the generated image as a PNG file in the current working "
              "directory, then stop.")
    for attempt in range(retries + 1):
        td = tempfile.mkdtemp(prefix="genimg_")
        try:
            t0 = time.time()
            p = _run([cli, "exec", "-c", 'model_reasoning_effort="low"',
                      "--sandbox", "workspace-write",
                      "--skip-git-repo-check", "--cd", td, prompt], timeout)
            out = (p.stdout or "") + (p.stderr or "")
            pngs = [os.path.join(td, f) for f in os.listdir(td)
                    if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
            # cwd first; else rescue the newest from ~/.codex/generated_images
            # (codex often saves there on Windows). Safe because codex is
            # SERIALIZED here, so the newest generated image is this job's.
            dcmd = [sys.executable, os.path.join(HERE, "codex_image_deliver.py"),
                    "--dest", dest, "--name", name]
            if pngs:
                dcmd += ["--src", max(pngs, key=os.path.getmtime)]
            d = _run(dcmd, 180)
            dt = time.time() - t0
            if d.returncode == 0:
                return {"name": name, "ok": True, "seconds": round(dt, 1),
                        "detail": (d.stdout or "").strip().splitlines()[-1] if d.stdout else ""}
            rated = any(h in out.lower() for h in RATE_HINTS)
            if attempt < retries:
                time.sleep(20 if rated else 2); continue
            return {"name": name, "ok": False, "seconds": round(time.time() - t0, 1),
                    "detail": ("rate-limited" if rated else "no image produced") +
                              "; tail: " + out[-160:].replace("\n", " ")}
        except subprocess.TimeoutExpired:
            if attempt < retries:
                continue
            return {"name": name, "ok": False, "seconds": timeout, "detail": "timeout"}
        finally:
            shutil.rmtree(td, ignore_errors=True)

def gen_http(job, dest, engine, timeout, retries):
    """Stateless HTTP engines (pollinations / flux / sdxl / qwen): parallel-safe."""
    name = job["name"]
    polish = engine == "pollinations"
    for attempt in range(retries + 1):
        td = tempfile.mkdtemp(prefix="genimg_")
        out_png = os.path.join(td, name + ".png")
        try:
            t0 = time.time()
            if engine == "pollinations":
                cmd = [sys.executable, os.path.join(HERE, "pollinations_image_gen.py"),
                       "--prompt", job["prompt"], "--out", out_png]
            elif engine == "cloudflare":
                cmd = [sys.executable, os.path.join(HERE, "cloudflare_image_gen.py"),
                       "--prompt", job["prompt"], "--out", out_png]
            else:
                cmd = [sys.executable, os.path.join(HERE, "hf_image_gen.py"),
                       "--engine", engine, "--prompt", job["prompt"], "--out", out_png]
            p = _run(cmd, timeout)
            if os.path.exists(out_png) and os.path.getsize(out_png) > 0:
                final = _deliver_compress(out_png, dest, name, polish)
                dt = time.time() - t0
                if final:
                    return {"name": name, "ok": True, "seconds": round(dt, 1),
                            "detail": os.path.basename(final)}
                return {"name": name, "ok": False, "seconds": round(dt, 1),
                        "detail": "compress failed"}
            out = (p.stdout or "") + (p.stderr or "")
            rated = any(h in out.lower() for h in RATE_HINTS)
            if attempt < retries:
                time.sleep(20 if rated else 3); continue
            return {"name": name, "ok": False, "seconds": round(time.time() - t0, 1),
                    "detail": ("rate-limited" if rated else "no image") +
                              "; tail: " + out[-140:].replace("\n", " ")}
        except subprocess.TimeoutExpired:
            if attempt < retries:
                continue
            return {"name": name, "ok": False, "seconds": timeout, "detail": "timeout"}
        finally:
            shutil.rmtree(td, ignore_errors=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", required=True, help="JSON list of {name, prompt}")
    ap.add_argument("--dest", help="target images folder")
    ap.add_argument("--engine", default="codex",
                    choices=["codex", "pollinations", "flux", "sdxl", "qwen", "cloudflare"])
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--timeout", type=int, default=600, help="seconds per image")
    ap.add_argument("--retries", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    jobs = json.load(open(a.jobs, encoding="utf-8"))
    if not isinstance(jobs, list) or not all("name" in j and "prompt" in j for j in jobs):
        sys.exit("jobs file must be a JSON list of {name, prompt}")

    # Codex cannot run concurrent exec sessions on one machine -> force serial.
    if a.engine == "codex":
        workers = 1
        if a.workers > 1:
            print("NOTE: Codex is serialized (1 worker). Concurrent codex exec "
                  "sessions contend for shared local runtime and abort; use "
                  "--engine flux/pollinations for true parallel generation.")
    else:
        workers = max(1, min(a.workers, 8))
        if a.workers > 8:
            print(f"NOTE: workers capped at 8 (asked {a.workers}); more just trips the provider's rate limit.")

    if a.dry_run:
        print(f"DRY RUN: {len(jobs)} job(s), engine={a.engine}, {workers} worker(s).")
        for j in jobs:
            print(f"  would generate {j['name']}: {j['prompt'][:60]}...")
        return

    if not a.dest:
        sys.exit("--dest is required unless --dry-run")
    cli = None
    if a.engine == "codex":
        cli = find_codex()
        if not cli:
            sys.exit("codex CLI not found; run codex_image_repair.py --repair first.")
        # Clear any stuck orphaned codex process first: one hung codex exec jams
        # every subsequent one (shared local runtime). This is the root-cause
        # guard for the 9-minute hang.
        try:
            import importlib.util as _il
            _sp = _il.spec_from_file_location("cir", os.path.join(HERE, "codex_image_repair.py"))
            _cir = _il.module_from_spec(_sp); _sp.loader.exec_module(_cir)
            _cleared = _cir.clear_stuck_codex()
            if _cleared:
                print(f"pre-flight: cleared {len(_cleared)} stuck codex process(es) before starting.")
        except Exception as _e:
            print("pre-flight codex cleanup skipped:", str(_e)[:80])

    print(f"Batch: {len(jobs)} images, engine={a.engine}, {workers} worker(s)"
          + (", reduced reasoning" if a.engine == "codex" else "") + ".")
    t0 = time.time()
    results = []
    def run_job(j):
        if a.engine == "codex":
            return gen_codex(j, a.dest, cli, a.timeout, a.retries)
        return gen_http(j, a.dest, a.engine, a.timeout, a.retries)
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(run_job, j): j for j in jobs}
        for fut in cf.as_completed(futs):
            r = fut.result(); results.append(r)
            tag = "OK " if r["ok"] else "FAIL"
            print(f"  [{tag}] {r['name']}  {r['seconds']}s  {r['detail'][:80]}")
    wall = time.time() - t0
    ok = [r for r in results if r["ok"]]
    fail = [r for r in results if not r["ok"]]
    total_cpu = sum(r["seconds"] for r in results)
    print(f"\nDone: {len(ok)}/{len(results)} delivered in {wall:.0f}s wall-clock "
          f"(sum of per-image time {total_cpu:.0f}s; speedup ~{total_cpu/max(1,wall):.1f}x).")
    if fail:
        print("FAILED (send these to the fallback engine, never ship imageless):")
        for r in fail:
            print("  -", r["name"], ":", r["detail"][:100])
        sys.exit(2)

if __name__ == "__main__":
    main()
