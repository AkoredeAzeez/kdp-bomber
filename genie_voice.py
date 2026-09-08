r"""GENIE VOICE INPUT: speak, and Genie types what you said.

Genie itself has no microphone. This is a small local listener that turns your
speech into typed text in your Genie window, so you can talk to Genie instead
of typing. Everything runs on this machine: the audio never leaves it, there is
no API key, and there is no per-word cost.

    python genie_voice.py                 listen, wake word "Genie", locked window
    python genie_voice.py --print         transcribe only, never type
    python genie_voice.py --no-wake       act on everything you say
    python genie_voice.py --no-lock       type into whatever window is focused
    python genie_voice.py --file demo.wav transcribe one 16 kHz mono wav and exit
    python genie_voice.py --model base    faster, slightly less accurate
    python genie_voice.py --list-devices  show microphones

HOW IT WORKS
  Say "Genie" to wake it, then your instruction: "Genie, write chapter two."
  After it wakes it stays listening for a short while, so you can keep talking
  without repeating the wake word. Say "go to sleep" to stop it early.

  End with a send phrase ("go ahead", "send it", "proceed") and it presses
  Enter, so a spoken instruction runs hands free. Say "scratch that" to discard
  what you just dictated.

  It locks onto one window at startup and types ONLY there. If that window is
  not focused when your words are ready, it restores it first; if it cannot,
  it skips typing rather than putting your words somewhere else.

STOP IT with Ctrl+C.
"""
import argparse, queue, re, sys, time

SAMPLE_RATE = 16000
BLOCK = 1600                    # 100 ms blocks
SILENCE_HANG = 0.6              # seconds of quiet that ends a phrase
MIN_SPEECH = 0.35               # ignore blips shorter than this
CALIBRATE_SECONDS = 1.0         # sample the room to set the noise floor
AWAKE_WINDOW = 30.0             # keep listening this long after a wake word

# Genie's own vocabulary, so the model stops writing "doc x" and "cook book".
VOCAB = ("Genie, KDP, DOCX, PDF, EPUB, Amazon, manuscript, chapter, subtitle, "
         "blurb, trim size, 6 by 9, 8.5 by 11, cookbook, workbook, journal, "
         "study guide, low content, coloring book, puzzle book, front matter, "
         "back matter, table of contents, pen name, paperback, hardcover.")

SEND_PHRASES = ("go ahead", "send it", "send that", "proceed", "run it", "do it now")
CANCEL_PHRASES = ("scratch that", "cancel that", "forget that", "ignore that")
SLEEP_PHRASES = ("go to sleep", "never mind", "stand down", "stop listening")

# Whisper hears the wake word many ways. Accept the near misses too.
WAKE_ALIASES = ("genie", "jeannie", "jeanie", "ginny", "ginnie", "genee",
                "jinnie", "gini", "jeany", "jeannine")


# ---------------------------------------------------------------- window lock
class WindowLock:
    """Type only into one chosen window. Fails safe: never types elsewhere."""

    def __init__(self, enabled=True):
        self.enabled = enabled
        self.hwnd = None
        self.title = ""
        self.u32 = None
        if enabled and sys.platform == "win32":
            import ctypes
            self.u32 = ctypes.windll.user32

    def _title_of(self, hwnd):
        import ctypes
        n = self.u32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(n + 1)
        self.u32.GetWindowTextW(hwnd, buf, n + 1)
        return buf.value

    def capture(self, delay):
        """Lock onto whichever window is focused after `delay` seconds."""
        if not self.enabled:
            return
        if self.u32 is None:
            print("[voice] window lock needs Windows; continuing without it.")
            self.enabled = False
            return
        if delay:
            print("[voice] click the Genie window you want to type into ...")
            for s in range(delay, 0, -1):
                print("        locking on in %d ..." % s, end="\r", flush=True)
                time.sleep(1)
            print(" " * 40, end="\r")
        self.hwnd = self.u32.GetForegroundWindow()
        self.title = self._title_of(self.hwnd)
        print('[voice] locked onto: "%s"' % (self.title or "untitled window"))

    def focus(self):
        """Make the locked window frontmost. True only if it really is."""
        if not self.enabled or not self.hwnd:
            return True
        if not self.u32.IsWindow(self.hwnd):
            print("[voice] the locked window is gone; not typing.")
            return False
        if self.u32.GetForegroundWindow() == self.hwnd:
            return True
        self.u32.ShowWindow(self.hwnd, 9)          # SW_RESTORE
        self.u32.SetForegroundWindow(self.hwnd)
        for _ in range(10):                        # give Windows a moment
            time.sleep(0.05)
            if self.u32.GetForegroundWindow() == self.hwnd:
                return True
        print('[voice] could not bring "%s" to the front; skipped typing.' % self.title)
        return False


# ------------------------------------------------------------------- speech
def load_model(size, quiet=False, threads=0):
    import os
    from faster_whisper import WhisperModel
    if not quiet:
        print("[voice] loading %s model (first run downloads it) ..." % size, flush=True)
    # int8 on CPU: fast enough for dictation and leaves the GPU alone for the
    # image pipeline. Use every core; the default of 4 leaves half the machine
    # idle while you wait for your own words.
    threads = threads or (os.cpu_count() or 4)
    return WhisperModel(size, device="cpu", compute_type="int8", cpu_threads=threads)


def warm(model):
    """First transcription is always slowest; spend it before the user speaks."""
    import numpy as np
    transcribe(model, np.zeros(SAMPLE_RATE, dtype=np.float32))


def transcribe(model, audio):
    segments, _ = model.transcribe(
        audio, language="en", vad_filter=True, beam_size=1,
        initial_prompt=VOCAB, condition_on_previous_text=False,
        without_timestamps=True)
    return " ".join(s.text.strip() for s in segments).strip()


def strip_trailing(text, phrases):
    """If the text ends with one of these phrases, remove it and report a hit."""
    low = text.lower().rstrip(" .!?,")
    for p in phrases:
        if low.endswith(p):
            return text[:len(low) - len(p)].rstrip(" .!?,-"), True
    return text, False


def strip_wake(text):
    """Remove a leading wake word. Returns (text, was_woken)."""
    m = re.match(r"^\s*(?:hey\s+|ok\s+|okay\s+)?([a-z]+)\b[\s,.!:-]*",
                 text, re.IGNORECASE)
    if m and m.group(1).lower() in WAKE_ALIASES:
        return text[m.end():].strip(), True
    return text, False


# Whisper hears these wrong no matter which model you pick, and a fast model
# gets them wrong more often. Repairing them here is instant and certain, which
# beats paying three extra seconds a phrase for a bigger model to guess right.
FIXUPS = (
    (r"\bdoc\s*[- ]?\s*x\b", "DOCX"),
    (r"\bdocks\b", "DOCX"),
    (r"\bdoc\s*ex\b", "DOCX"),
    (r"\be\s*pub\b", "EPUB"),
    (r"\bpee?\s*dee?\s*eff\b", "PDF"),
    (r"\bkay\s*dee\s*pee\b", "KDP"),
    (r"\bk\.?\s*d\.?\s*p\.?\b", "KDP"),
    (r"\bcook\s+book\b", "cookbook"),
    (r"\bwork\s+book\b", "workbook"),
    (r"\bsub\s+title\b", "subtitle"),
    (r"\bpen\s+name\b", "pen name"),
    (r"\bfront\s+matter\b", "front matter"),
    # spoken trim sizes -> the way they are written on a KDP listing
    (r"\beight(?:\s+and\s+a\s+half|\s+point\s+five)?\s+by\s+eleven\b", "8.5 x 11"),
    # Whisper often mixes numerals and words: "8 and a half by 11".
    (r"\b8\s+and\s+a\s+half\s+by\s+11\b", "8.5 x 11"),
    (r"\beight\s+and\s+a\s+half\s+by\s+11\b", "8.5 x 11"),
    (r"\b8\s+point\s+5\s+by\s+11\b", "8.5 x 11"),
    (r"\b8\.5\s+by\s+11\b", "8.5 x 11"),
    (r"\bsix\s+by\s+nine\b", "6 x 9"),
    (r"\b6\s+by\s+9\b", "6 x 9"),
    (r"\bfive\s+by\s+eight\b", "5 x 8"),
    (r"\bseven\s+by\s+ten\b", "7 x 10"),
)


def fixup(text):
    """Repair the terms Whisper reliably mangles in Genie's vocabulary."""
    for pattern, repl in FIXUPS:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text


def clean(text):
    text = re.sub(r"\s+", " ", text).strip()
    # Whisper likes to emit bare filler on silence.
    if text.lower().strip(" .!?") in ("you", "thank you", "thanks", "bye", ""):
        return ""
    return fixup(text)


def type_out(text, send, lock):
    if not lock.focus():
        return False
    import pyautogui
    pyautogui.write(text, interval=0.008)
    if send:
        pyautogui.press("enter")
    return True


# -------------------------------------------------------------------- modes
def run_file(model, path, do_type, lock):
    import numpy as np, wave
    with wave.open(path, "rb") as w:
        if w.getframerate() != SAMPLE_RATE or w.getnchannels() != 1:
            print("[voice] expected 16 kHz mono wav; got %d Hz / %d ch"
                  % (w.getframerate(), w.getnchannels()))
        raw = w.readframes(w.getnframes())
    audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    text = clean(transcribe(model, audio))
    print("[heard] %s" % (text or "(nothing)"))
    if do_type and text:
        type_out(text, False, lock)
    return text


def run_mic(model, device, do_type, lock, need_wake):
    import numpy as np, sounddevice as sd

    q = queue.Queue()

    def cb(indata, frames, t, status):
        q.put(indata[:, 0].copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, blocksize=BLOCK, device=device,
                        channels=1, dtype="float32", callback=cb):
        print("[voice] calibrating, stay quiet for a second ...", flush=True)
        floor = []
        for _ in range(int(CALIBRATE_SECONDS * SAMPLE_RATE / BLOCK)):
            floor.append(float(np.sqrt(np.mean(q.get() ** 2))))
        base = sorted(floor)[len(floor) // 2]
        thresh = max(base * 3.5, 0.008)
        print("[voice] noise floor %.4f, speaking threshold %.4f" % (base, thresh))
        if need_wake:
            print('[voice] ready. Say "Genie" then your instruction. Ctrl+C to stop.\n',
                  flush=True)
        else:
            print("[voice] ready (no wake word). Speak. Ctrl+C to stop.\n", flush=True)

        buf, speaking, quiet_for, awake_until = [], False, 0.0, 0.0
        while True:
            block = q.get()
            level = float(np.sqrt(np.mean(block ** 2)))
            if level >= thresh:
                if not speaking:
                    speaking, buf = True, []
                quiet_for = 0.0
                buf.append(block)
                continue
            if not speaking:
                continue

            buf.append(block)
            quiet_for += BLOCK / SAMPLE_RATE
            if quiet_for < SILENCE_HANG:
                continue

            audio = np.concatenate(buf)
            speaking, buf, quiet_for = False, [], 0.0
            if len(audio) / SAMPLE_RATE < MIN_SPEECH:
                continue
            text = clean(transcribe(model, audio))
            if not text:
                continue

            awake = time.time() < awake_until
            if need_wake:
                text, woken = strip_wake(text)
                if not (woken or awake):
                    print("[ignored] %s" % text[:60])
                    continue
                if not text:                       # just the wake word
                    awake_until = time.time() + AWAKE_WINDOW
                    print("[voice] listening ...")
                    continue

            stripped, sleeping = strip_trailing(text, SLEEP_PHRASES)
            if sleeping and not stripped:
                awake_until = 0.0
                print("[voice] going to sleep; say the wake word again.")
                continue

            text, cancelled = strip_trailing(text, CANCEL_PHRASES)
            if cancelled:
                print("[voice] discarded")
                awake_until = time.time() + AWAKE_WINDOW
                continue

            text, send = strip_trailing(text, SEND_PHRASES)
            if not text:
                continue
            print("[heard] %s%s" % (text, "  -> SEND" if send else ""))
            if do_type:
                type_out(text + ("" if send else " "), send, lock)
            awake_until = 0.0 if send else time.time() + AWAKE_WINDOW


def main():
    ap = argparse.ArgumentParser(description="Speak to Genie; it types what you say.")
    ap.add_argument("--model", default="base.en",
                    help="base.en (default, ~1.4s a phrase), small.en or small "
                         "for slower but sharper, or any faster-whisper model")
    ap.add_argument("--threads", type=int, default=0,
                    help="CPU threads (default: all cores)")
    ap.add_argument("--device", type=int, help="input device index")
    ap.add_argument("--print", dest="print_only", action="store_true",
                    help="print transcripts instead of typing them")
    ap.add_argument("--file", help="transcribe one 16 kHz mono wav and exit")
    ap.add_argument("--no-wake", dest="wake", action="store_false",
                    help="act on everything, no wake word")
    ap.add_argument("--no-lock", dest="lock", action="store_false",
                    help="type into whatever window is focused")
    ap.add_argument("--lock-delay", type=int, default=5,
                    help="seconds to pick the window to lock onto (default 5)")
    ap.add_argument("--list-devices", action="store_true")
    a = ap.parse_args()

    if a.list_devices:
        import sounddevice as sd
        for i, d in enumerate(sd.query_devices()):
            if d["max_input_channels"]:
                print("  [%d] %s" % (i, d["name"]))
        return

    do_type = not a.print_only
    lock = WindowLock(enabled=a.lock and do_type)
    model = load_model(a.model, threads=a.threads)
    if a.file:
        run_file(model, a.file, do_type, lock)
        return
    warm(model)
    lock.capture(a.lock_delay if lock.enabled else 0)
    try:
        run_mic(model, a.device, do_type, lock, a.wake)
    except KeyboardInterrupt:
        print("\n[voice] stopped.")


if __name__ == "__main__":
    main()
