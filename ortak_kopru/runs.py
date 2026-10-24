import datetime
import json
import os
import re
import tempfile
import uuid
from pathlib import Path

from .context import ContextError, canonical_bytes, sha256


SECRET_PATTERNS = (
    re.compile(r"\b(?:sk-[A-Za-z0-9_-]{12,}|sk-ant-[A-Za-z0-9_-]{8,})"),
    re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{30,}"),
)


def contains_secret(value):
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def _write_exclusive(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".pending-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        # Windows rename refuses an existing destination; POSIX hard links provide no-replace publication.
        if os.name == "nt":
            os.rename(temporary, path)
        else:
            os.link(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


class RunStore:
    """Append-only per-run event files; local raw payloads live outside public metadata."""

    def __init__(self, root):
        self.root = Path(root)
        self.private = self.root / "private"

    def start(self, compiled, metadata):
        if self.root.is_symlink() or self.private.is_symlink():
            raise ContextError("Run storage directories cannot be symlinks")
        try:
            self.root.mkdir(parents=True, exist_ok=True)
            self.private.mkdir(parents=True, exist_ok=True)
            self.private.resolve(strict=True).relative_to(self.root.resolve(strict=True))
        except (OSError, ValueError):
            raise ContextError("Run storage must be writable and remain in the configured directory") from None
        run_id = str(uuid.uuid4())
        run_private = self.private / run_id
        try:
            run_private.mkdir(mode=0o700)
        except OSError as exc:
            raise ContextError(f"Cannot reserve a unique private run directory: {exc}") from None
        event = {
            "run_id": run_id,
            "sequence": 0,
            "previous_hash": None,
            "status": "ready",
            "context_sha256": compiled["context_sha256"],
            "message_sha256": compiled["message_sha256"],
            "sources": compiled["sources"],
            "metadata": metadata,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        if contains_secret(event):
            raise ContextError("Public run metadata failed the local secret-pattern scan")
        event["event_sha256"] = sha256(canonical_bytes(event))
        public_path = self.root / f"{run_id}.0000.json"
        private_path = run_private / "context.json"
        try:
            _write_exclusive(private_path, canonical_bytes(compiled))
            _write_exclusive(public_path, canonical_bytes(event))
        except OSError as exc:
            raise ContextError(f"Cannot create required pre-call run record: {exc}") from None
        return RunHandle(self.root, self.private, run_id, event["event_sha256"])


class RunHandle:
    def __init__(self, root, private, run_id, previous_hash):
        self.root = Path(root)
        self.private = Path(private)
        self.run_id = run_id
        self.previous_hash = previous_hash
        self.sequence = 0

    def append(self, status, metadata=None, raw=None):
        if status not in {"attempted", "succeeded", "failed", "skipped", "recovery_required"}:
            raise ContextError(f"Invalid run status: {status}")
        if raw is not None:
            raw_path = self.private / self.run_id / f"raw-{self.sequence + 1:04d}.json"
            _write_exclusive(raw_path, canonical_bytes(raw))
        event = {
            "run_id": self.run_id,
            "sequence": self.sequence + 1,
            "previous_hash": self.previous_hash,
            "status": status,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "metadata": metadata or {},
        }
        if contains_secret(event):
            raise ContextError("Public event failed the local secret-pattern scan; raw data was not published")
        event["event_sha256"] = sha256(canonical_bytes(event))
        path = self.root / f"{self.run_id}.{self.sequence + 1:04d}.json"
        try:
            _write_exclusive(path, canonical_bytes(event))
        except OSError as exc:
            raise ContextError(f"Run event could not be recorded: {exc}") from None
        self.sequence += 1
        self.previous_hash = event["event_sha256"]
        return event


def verify_runs(root):
    root = Path(root)
    grouped = {}
    errors = []
    for path in sorted(root.glob("*.????.json")):
        try:
            event = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(event, dict):
                errors.append(f"{path.name}: event must be a JSON object")
                continue
            if contains_secret(event):
                errors.append(f"{path.name}: secret-like public metadata")
                continue
            if not isinstance(event.get("run_id"), str) or type(event.get("sequence")) is not int:
                errors.append(f"{path.name}: invalid event identity or sequence")
                continue
            digest = event.pop("event_sha256", None)
            if digest != sha256(canonical_bytes(event)):
                errors.append(f"{path.name}: event hash mismatch")
                continue
            event["event_sha256"] = digest
            grouped.setdefault(event["run_id"], []).append((event["sequence"], event))
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError) as exc:
            errors.append(f"{path.name}: invalid event ({exc})")
    for run_id, entries in grouped.items():
        entries.sort()
        previous = None
        previous_status = None
        for expected, (sequence, event) in enumerate(entries):
            if sequence != expected or event.get("previous_hash") != previous:
                errors.append(f"{run_id}: broken or forked chain at sequence {sequence}")
                break
            status = event.get("status")
            allowed = {
                None: {"ready"},
                "ready": {"attempted", "skipped"},
                "attempted": {"succeeded", "failed", "recovery_required"},
            }
            if status not in allowed.get(previous_status, set()):
                errors.append(f"{run_id}: invalid status transition at sequence {sequence}")
                break
            if (sequence == 0 and status != "ready") or sequence > 2:
                errors.append(f"{run_id}: invalid event sequence {sequence}")
                break
            previous = event.get("event_sha256")
            previous_status = status
    return errors
