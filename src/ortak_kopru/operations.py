"""Fixed, bounded local operations for the shared task service.

Only three named operations exist; callers cannot add argv or shell text.
A user-mode process runs in an explicit Git working-tree root and the result
is returned as a JSON-ready receipt. This module never calls a model, provider,
network service or GitHub, and never creates task state: the calling service
records the prepared operation and its completion durably.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import math
import os
from pathlib import Path
import platform
import signal
import subprocess
import sys
import threading
import time

FORMAT_VERSION = 1
MAX_OUTPUT_BYTES = 64 * 1024
MAX_TIMEOUT_SECONDS = 120
_CHUNK_BYTES = 8192
_POLL_SECONDS = 0.02
_DRAIN_SECONDS = 5.0
# Command-line config wins over repository config: no fsmonitor hook runs and
# status does not rewrite the index behind the caller's back.
_GIT_OPTIONS = ("--no-optional-locks", "-c", "core.fsmonitor=false")
OPERATIONS = {
    "repo_revision": ("git", *_GIT_OPTIONS, "rev-parse", "--verify", "HEAD"),
    "repo_status": ("git", *_GIT_OPTIONS, "status", "--porcelain=v1", "--branch"),
    "python_version": ("python", "--version"),
}
# Only what git and Python need to start. GIT_* routing, tokens and keys stay out.
_INHERITED_ENV = frozenset({
    "PATH", "PATHEXT", "SYSTEMROOT", "SYSTEMDRIVE", "WINDIR",
    "HOME", "USERPROFILE", "HOMEDRIVE", "HOMEPATH", "XDG_CONFIG_HOME",
    "TEMP", "TMP", "TMPDIR", "LANG", "LC_ALL", "LC_CTYPE",
})


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _elapsed(started):
    return max(0, round((time.monotonic() - started) * 1000))


def _operation(value):
    if not isinstance(value, str) or value not in OPERATIONS:
        raise ValueError("İşlem adı repo_revision, repo_status veya python_version olmalı.")
    return value


def _repository_root(value):
    if isinstance(value, bool) or not isinstance(value, (str, os.PathLike)):
        raise ValueError("cwd açık bir yerel dizin yolu olmalı.")
    text = os.fspath(value)
    if not isinstance(text, str) or not text or "\0" in text:
        raise ValueError("cwd açık bir yerel dizin yolu olmalı.")
    path = Path(text)
    if not path.is_absolute():
        raise ValueError("cwd mutlak yol olmalı.")
    try:
        root = path.resolve(strict=True)
        if not root.is_dir():
            raise ValueError("cwd bir dizin olmalı.")
        marker = root / ".git"
        if marker.is_dir():
            valid = (marker / "HEAD").is_file()
        elif marker.is_file():
            # Linked worktrees and submodules keep a "gitdir:" pointer file.
            with marker.open("rb") as stream:
                valid = stream.read(8) == b"gitdir: "
        else:
            valid = False
    except (OSError, RuntimeError) as exc:
        raise ValueError("cwd bulunamadı veya okunamadı.") from exc
    if not valid:
        raise ValueError("cwd bir Git çalışma ağacının kökü olmalı.")
    return root


def _timeout(value):
    if (isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or not 0 < value <= MAX_TIMEOUT_SECONDS):
        raise ValueError(f"timeout_seconds 0'dan büyük ve en fazla {MAX_TIMEOUT_SECONDS} olmalı.")
    return float(value)


def _limit(value):
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_OUTPUT_BYTES:
        raise ValueError(f"output_limit 1–{MAX_OUTPUT_BYTES} bayt arasında tam sayı olmalı.")
    return value


def _environment():
    windows = os.name == "nt"
    env = {key: value for key, value in os.environ.items()
           if (key.upper() if windows else key) in _INHERITED_ENV}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    return env


def _find(program, search_path):
    # Only absolute PATH entries count: neither the current directory nor a
    # .bat/.cmd wrapper (which Windows would hand to cmd.exe) can stand in.
    name = program + (".exe" if os.name == "nt" else "")
    for entry in search_path.split(os.pathsep):
        candidate = os.path.join(entry, name)
        if os.path.isabs(entry) and os.path.isfile(candidate) and os.access(candidate, os.X_OK):
            return candidate
    return None


def _argv(operation, env):
    program, *arguments = OPERATIONS[operation]
    if program == "python":
        executable = sys.executable
        if not executable or not os.path.isabs(executable):
            return None, "Çalışan Python yorumlayıcısının yolu bilinmiyor."
    else:
        executable = _find(program, env.get("PATH", ""))
        if executable is None:
            return None, f"{program} yürütülebilir dosyası PATH üzerinde bulunamadı."
    return [executable, *arguments], None


def _platform():
    return {"system": platform.system(), "release": platform.release(), "machine": platform.machine(),
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version()}


def _capture(stream, limit, record, overflow):
    """Read at most limit bytes; one extra byte proves the limit was exceeded."""
    buffer = record["buffer"]
    try:
        while True:
            room = limit - len(buffer)
            chunk = stream.read(min(_CHUNK_BYTES, room + 1))
            if not chunk:
                return
            if len(chunk) > room:
                buffer += chunk[:room]
                record["truncated"] = True
                overflow.set()
                return
            buffer += chunk
    except (OSError, ValueError):
        record["read_error"] = True


def _terminate(process):
    try:
        if os.name == "nt":
            process.kill()
        else:
            # The child leads its own session, so helpers it started stop too.
            os.killpg(process.pid, signal.SIGKILL)
    except OSError:
        try:
            process.kill()
        except OSError:
            pass


def _exited(process):
    """True once the child exited; POSIX keeps the zombie so its group id stays reserved."""
    if os.name != "nt" and hasattr(os, "waitid") and hasattr(os, "WNOWAIT"):
        try:
            return os.waitid(os.P_PID, process.pid, os.WEXITED | os.WNOHANG | os.WNOWAIT) is not None
        except ChildProcessError:
            return True
    return process.poll() is not None


def _drain(readers):
    """Wait a bounded time for both readers; report which pipes are still open."""
    drained_by = time.monotonic() + _DRAIN_SECONDS
    for reader in readers:
        reader.join(max(0.0, drained_by - time.monotonic()))
    return [reader.is_alive() for reader in readers]


def _stream(record):
    data = bytes(record["buffer"])
    return {"text": data.decode("utf-8", errors="backslashreplace"),
            "captured_bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "truncated": record["truncated"] or record.get("incomplete", False)}


def run_local(operation, cwd, *, timeout_seconds=10, output_limit=MAX_OUTPUT_BYTES):
    """Run one named operation and return its receipt; invalid input starts nothing."""
    name = _operation(operation)
    root = _repository_root(cwd)
    timeout = _timeout(timeout_seconds)
    limit = _limit(output_limit)
    env = _environment()
    argv, problem = _argv(name, env)
    receipt = {
        "format_version": FORMAT_VERSION, "operation": name,
        "argv": argv if argv is not None else list(OPERATIONS[name]),
        "cwd": str(root), "platform": _platform(),
        "timeout_seconds": timeout, "output_limit": limit,
        "execution_scope": "user_mode", "kernel_scope": "not_requested",
    }
    outputs = {key: {"buffer": bytearray(), "truncated": False} for key in ("stdout", "stderr")}
    started_at, started = _now(), time.monotonic()
    process = None
    if problem is None:
        try:
            process = subprocess.Popen(
                argv, cwd=root, env=env, shell=False, stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0,
                start_new_session=os.name != "nt")
        except OSError as exc:
            problem = f"Süreç başlatılamadı: {exc.strerror or type(exc).__name__}."
    if process is None:
        return {**receipt, "started_at": started_at, "finished_at": _now(),
                "duration_ms": _elapsed(started), "exit_code": None, "status": "spawn_error",
                "stdout": _stream(outputs["stdout"]), "stderr": _stream(outputs["stderr"]),
                "error": problem}

    overflow = threading.Event()
    readers = [threading.Thread(target=_capture, args=(stream, limit, outputs[key], overflow), daemon=True)
               for key, stream in (("stdout", process.stdout), ("stderr", process.stderr))]
    deadline, stopped, exit_code, notes = started + timeout, None, None, []
    try:
        for reader in readers:
            reader.start()
        while not _exited(process):
            if overflow.is_set():
                stopped = "output_limit"
            elif time.monotonic() >= deadline:
                stopped = "timeout"
            if stopped:
                _terminate(process)
                break
            overflow.wait(min(_POLL_SECONDS, max(0.0, deadline - time.monotonic())))
        lingering = _drain(readers)
        if any(lingering):
            # The process ended but a helper it started still holds a pipe open.
            if os.name == "nt":
                notes.append("Süreç çıktıktan sonra bir yardımcı süreç çıktı akışını açık tuttu; "
                             "Windows'ta süreç grubu kullanılmadığından yardımcı süreç sonlandırılamadı.")
            else:
                _terminate(process)
                notes.append("Süreç çıktıktan sonra bir yardımcı süreç çıktı akışını açık tuttu; "
                             "süreç grubu sonlandırıldı.")
                _drain(readers)
        try:
            exit_code = process.wait(timeout=_DRAIN_SECONDS)
        except subprocess.TimeoutExpired:
            notes.append("Süreç sonlandırılamadı; çıkış kodu alınamadı.")
    except BaseException:
        _terminate(process)
        raise
    for key, reader, stream, was_open in zip(("stdout", "stderr"), readers,
                                             (process.stdout, process.stderr), lingering):
        if was_open or outputs[key].get("read_error"):
            outputs[key]["incomplete"] = True
        if reader.is_alive():
            notes.append(f"{key} akışı kapanmadı; okuma bırakıldı.")
        else:
            stream.close()
    if any(record.get("read_error") for record in outputs.values()):
        notes.append("Çıktı akışı okunurken hata oluştu.")

    limited = outputs["stdout"]["truncated"] or outputs["stderr"]["truncated"]
    incomplete = any(record.get("incomplete") for record in outputs.values())
    if stopped == "timeout":
        status = "timeout"
        notes.insert(0, f"Süre sınırı ({timeout:g} sn) aşıldı; süreç sonlandırıldı.")
    elif stopped == "output_limit" or limited:
        status = "output_limit"
        notes.insert(0, f"Çıktı sınırı ({limit} bayt) aşıldı; fazlası kaydedilmedi.")
    elif exit_code == 0 and not incomplete:
        status = "completed"
    else:
        status = "failed"
    if incomplete:
        # A clean exit code never makes a partial capture a full success.
        notes.append("Çıktı eksik kaydedildi.")
    return {**receipt, "started_at": started_at, "finished_at": _now(),
            "duration_ms": _elapsed(started), "exit_code": exit_code, "status": status,
            "stdout": _stream(outputs["stdout"]), "stderr": _stream(outputs["stderr"]),
            "error": " ".join(notes) or None}
