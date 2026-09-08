#!/usr/bin/env python3
"""
GENIE KOKORO SETUP (turnkey, free local audiobook voice)
========================================================
One command. It installs kokoro-onnx if missing, downloads the Kokoro-82M model
on first run (Apache-2.0, free, commercial-safe), and starts an OpenAI-compatible
TTS server that genie_audiobook.py `synth` talks to. No Docker, no credits.

  python kokoro_setup.py

Then, in another terminal:
  python genie_audiobook.py synth --dir narration --endpoint http://localhost:8880/v1 --voice af_bella --format wav

Options: --host 127.0.0.1  --port 8880  --models <dir>
First run downloads ~350 MB once (cached); later runs start in seconds.
Windows / macOS / Linux. Faster on a GPU host, but works on CPU.
"""
import argparse, os, sys, subprocess, platform, urllib.request

ONNX_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx"
VOICES_URL = "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin"

def cache_dir(custom):
    if custom:
        os.makedirs(custom, exist_ok=True); return custom
    base = os.environ.get("LOCALAPPDATA", os.path.expanduser("~")) if platform.system() == "Windows" \
        else os.path.join(os.path.expanduser("~"), ".cache")
    d = os.path.join(base, "GenieKokoro"); os.makedirs(d, exist_ok=True); return d

def ensure_deps():
    try:
        import kokoro_onnx, soundfile  # noqa: F401
        return
    except ImportError:
        print("Installing kokoro-onnx and soundfile (one time)...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "kokoro-onnx", "soundfile"])
        except Exception as e:
            print(f"Could not auto-install ({e}). Run:  pip install kokoro-onnx soundfile"); sys.exit(1)
        print("Dependencies installed.")

def download(url, dest, label):
    if os.path.exists(dest) and os.path.getsize(dest) > 5_000_000:
        print(f"  {label}: already present ({os.path.getsize(dest)//1_000_000} MB)"); return
    print(f"  {label}: downloading (first run only)...")
    def hook(b, bs, total):
        if total > 0:
            sys.stdout.write(f"\r    {min(100, b * bs * 100 // total)}%"); sys.stdout.flush()
    urllib.request.urlretrieve(url, dest, hook); print("\r    done       ")

def ensure_model(models):
    onnx = os.path.join(models, "kokoro-v1.0.onnx")
    voices = os.path.join(models, "voices-v1.0.bin")
    print(f"Model cache: {models}")
    download(ONNX_URL, onnx, "model")
    download(VOICES_URL, voices, "voices")
    return onnx, voices

def serve(onnx, voices, host, port):
    import io, json
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import soundfile as sf
    from kokoro_onnx import Kokoro
    print("Loading Kokoro model...")
    K = Kokoro(onnx, voices)

    class H(BaseHTTPRequestHandler):
        def do_POST(self):
            if not self.path.rstrip("/").endswith("/audio/speech"):
                self.send_response(404); self.end_headers(); return
            n = int(self.headers.get("Content-Length", 0))
            req = json.loads(self.rfile.read(n) or b"{}")
            try:
                voice = req.get("voice", "af_bella")
                # language follows the voice pack prefix unless overridden:
                # a=en-us b=en-gb j=ja z=cmn e=es f=fr-fr h=hi i=it p=pt-br
                LANG = {"a": "en-us", "b": "en-gb", "j": "ja", "z": "cmn",
                        "e": "es", "f": "fr-fr", "h": "hi", "i": "it", "p": "pt-br"}
                lang = req.get("lang") or LANG.get(voice[:1], "en-us")
                s, sr = K.create(req.get("input", ""), voice=voice,
                                 speed=1.0, lang=lang)
                buf = io.BytesIO(); sf.write(buf, s, sr, format="WAV"); data = buf.getvalue()
                self.send_response(200); self.send_header("Content-Type", "audio/wav")
                self.send_header("Content-Length", str(len(data))); self.end_headers(); self.wfile.write(data)
            except Exception as e:
                m = json.dumps({"error": str(e)}).encode()
                self.send_response(500); self.send_header("Content-Length", str(len(m)))
                self.end_headers(); self.wfile.write(m)

        def log_message(self, *a):
            pass

    print(f"Kokoro ready. OpenAI-compatible server on http://{host}:{port}  (POST /v1/audio/speech)")
    print(f"Now run:  python genie_audiobook.py synth --dir narration --endpoint http://{host}:{port}/v1 --voice af_bella --format wav")
    HTTPServer((host, port), H).serve_forever()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8880)
    ap.add_argument("--models")
    a = ap.parse_args()
    ensure_deps()
    onnx, voices = ensure_model(cache_dir(a.models))
    serve(onnx, voices, a.host, a.port)

if __name__ == "__main__":
    main()
