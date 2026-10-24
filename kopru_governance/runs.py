"""Local-only append-only run events with per-run hash chaining."""

import json
import os
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .core import GovernanceError, canonical_json, pretty_json, sha256, _json_no_duplicates


MAX_LEDGER_BYTES = 1024 * 1024
MAX_EVENTS = 32
TRANSITIONS = {
    None: {"ready", "failed"},
    "ready": {"waiting_approval", "attempted", "skipped", "failed"},
    "waiting_approval": {"skipped"},
    "attempted": {"attempted", "succeeded", "failed", "recovery_required"},
    "succeeded": set(),
    "failed": set(),
    "skipped": set(),
    "recovery_required": set(),
}


def _private_dir(path):
    if path.is_symlink():
        raise GovernanceError("run storage directory may not be a symlink")
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise GovernanceError("run storage directory may not be a symlink")
    try:
        path.chmod(0o700)
    except OSError:
        pass


def _exclusive_write(path, data):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    fd = os.open(path, flags, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        try:
            os.unlink(path)
        except OSError:
            pass
        raise


def write_private_artifact(root, output, data):
    """Create a 0600 artifact under non-symlinked ignored runs/ storage."""
    root = Path(root).resolve(strict=True)
    runs_root = root / "runs"
    if runs_root.is_symlink():
        raise GovernanceError("runs/ may not be a symlink")
    runs_root.mkdir(mode=0o700, exist_ok=True)
    if runs_root.is_symlink():
        raise GovernanceError("runs/ may not be a symlink")
    runs_root.chmod(0o700)
    output = Path(output)
    if not output.is_absolute():
        output = root / output
    output = Path(os.path.abspath(output))
    try:
        relative = output.relative_to(runs_root)
    except ValueError as exc:
        raise GovernanceError("private artifacts must be stored under ignored runs/") from exc
    if not relative.parts or any(part in ("", ".", "..") for part in relative.parts):
        raise GovernanceError("unsafe private artifact path")
    current = runs_root
    for part in relative.parts[:-1]:
        current = current / part
        if current.is_symlink():
            raise GovernanceError("private artifact directories may not be symlinks")
        current.mkdir(mode=0o700, exist_ok=True)
        if current.is_symlink():
            raise GovernanceError("private artifact directories may not be symlinks")
        current.chmod(0o700)
    if output.is_symlink():
        raise GovernanceError("private artifact may not be a symlink")
    _exclusive_write(output, data)
    return output


def _load_events(path):
    path = Path(path)
    raw = path.read_bytes()
    if len(raw) > MAX_LEDGER_BYTES:
        raise GovernanceError("run ledger exceeds size limit")
    if not raw.endswith(b"\n"):
        raise GovernanceError("run ledger has an incomplete final event")
    try:
        lines = raw.decode("utf-8", "strict").splitlines()
        events = [json.loads(line, object_pairs_hook=_json_no_duplicates) for line in lines]
    except (UnicodeDecodeError, json.JSONDecodeError, GovernanceError) as exc:
        raise GovernanceError("run ledger is not valid UTF-8 JSONL") from exc
    if not events or len(events) > MAX_EVENTS:
        raise GovernanceError("run ledger has an invalid event count")
    previous = ""
    status = None
    for sequence, event in enumerate(events):
        if not isinstance(event, dict) or set(event) != {
            "sequence", "at", "status", "metadata", "previous_hash", "event_hash"
        }:
            raise GovernanceError("run event has an invalid shape")
        if (type(event["sequence"]) is not int or not isinstance(event["status"], str)
                or not isinstance(event["metadata"], dict)
                or not isinstance(event["previous_hash"], str)
                or not isinstance(event["event_hash"], str)
                or not re.fullmatch(r"[a-f0-9]{64}", event["event_hash"])):
            raise GovernanceError("run event fields have invalid types")
        try:
            event_time = datetime.fromisoformat(event["at"].replace("Z", "+00:00"))
        except (AttributeError, ValueError) as exc:
            raise GovernanceError("run event timestamp is invalid") from exc
        if event_time.tzinfo is None:
            raise GovernanceError("run event timestamp must be timezone-aware")
        if event["sequence"] != sequence or event["previous_hash"] != previous:
            raise GovernanceError("run event sequence or previous hash is invalid")
        if event["status"] not in TRANSITIONS.get(status, set()):
            raise GovernanceError("run status transition is invalid")
        unhashed = {key: value for key, value in event.items() if key != "event_hash"}
        if sha256(canonical_json(unhashed)) != event["event_hash"]:
            raise GovernanceError("run event hash mismatch")
        previous = event["event_hash"]
        status = event["status"]
    return events


def create_run(runs_dir, bundle):
    """Reserve a unique ledger and private context snapshot before any provider call."""
    runs_dir = Path(runs_dir)
    private_root = runs_dir / "private"
    _private_dir(runs_dir)
    _private_dir(private_root)
    run_id = uuid.uuid4().hex
    ledger = runs_dir / f"{run_id}.jsonl"
    private_bundle = private_root / f"{run_id}-context.json"
    # Exclusive creation means simultaneous runs never replace one another.
    fd = os.open(ledger, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    os.close(fd)
    try:
        raw = pretty_json(bundle)
        _exclusive_write(private_bundle, raw)
        append_event(ledger, "ready", {
            "policy_sha256": bundle["manifest"]["policy_sha256"],
            "context_hash": bundle["manifest"]["context_hash"],
            "manifest_sha256": bundle["manifest"]["manifest_sha256"],
            "messages_sha256": bundle["manifest"]["messages_sha256"],
            "source_hashes": {
                source["path"]: source["sha256"] for source in bundle["manifest"]["sources"]
            },
            "request": bundle["manifest"]["request"],
            "visibility": bundle["manifest"]["visibility"],
            "private_bundle_sha256": sha256(raw),
            "provider_requested": bundle["manifest"]["request"].get("provider", "unknown"),
            "model_requested": bundle["manifest"]["request"].get("model", "unknown"),
        })
    except BaseException:
        try:
            if ledger.stat().st_size == 0:
                ledger.unlink()
        except OSError:
            pass
        raise
    return run_id, ledger, private_root


def append_event(ledger, status, metadata=None):
    ledger = Path(ledger)
    try:
        events = _load_events(ledger) if ledger.stat().st_size else []
    except FileNotFoundError:
        events = []
    old_status = events[-1]["status"] if events else None
    if status not in TRANSITIONS.get(old_status, set()):
        raise GovernanceError(f"invalid run status transition: {old_status} -> {status}")
    if len(events) >= MAX_EVENTS:
        raise GovernanceError("run ledger event limit reached")
    metadata = metadata or {}
    if not isinstance(metadata, dict):
        raise GovernanceError("run event metadata must be an object")
    at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    event = {
        "sequence": len(events),
        "at": at,
        "status": status,
        "metadata": metadata,
        "previous_hash": events[-1]["event_hash"] if events else "",
    }
    event["event_hash"] = sha256(canonical_json(event))
    line = canonical_json(event) + b"\n"
    if ledger.stat().st_size + len(line) > MAX_LEDGER_BYTES:
        raise GovernanceError("run ledger exceeds size limit")
    fd = os.open(ledger, os.O_WRONLY | os.O_APPEND)
    try:
        written = os.write(fd, line)
        if written != len(line):
            raise OSError("short run ledger write")
        os.fsync(fd)
    finally:
        os.close(fd)
    return event["event_hash"]


def write_private_output(private_root, run_id, output):
    if not isinstance(output, str):
        raise GovernanceError("provider output must be text")
    data = output.encode("utf-8")
    path = Path(private_root) / f"{run_id}-output.txt"
    _exclusive_write(path, data)
    return path, sha256(data)


def verify_run(ledger):
    events = _load_events(ledger)
    return {
        "valid": True,
        "events": len(events),
        "run_id": Path(ledger).stem,
        "status": events[-1]["status"],
        "head_hash": events[-1]["event_hash"],
    }


def public_metadata(ledger):
    """Whitelist only hashes, lifecycle and model selection; never export prompts/errors/output."""
    events = _load_events(ledger)
    first = events[0]["metadata"]
    last = events[-1]
    requested = first.get("request", {})
    last_metadata = last["metadata"]
    result = {
        "schema_version": 1,
        "run_id": Path(ledger).stem,
        "status": last["status"],
        "context_hash": first.get("context_hash", "unknown"),
        "policy_sha256": first.get("policy_sha256", "unknown"),
        "manifest_sha256": first.get("manifest_sha256", "unknown"),
        "messages_sha256": first.get("messages_sha256", "unknown"),
        "source_hashes": first.get("source_hashes", {}),
        "provider_requested": first.get("provider_requested", "unknown"),
        "model_requested": first.get("model_requested", "unknown"),
        "reasoning_requested": requested.get("reasoning_requested", "unknown"),
        "provider_observed": last_metadata.get("provider_observed", "unknown"),
        "model_observed": last_metadata.get("model_observed", "unknown"),
        "reasoning_applied": last_metadata.get("reasoning_applied", "unknown"),
        "output_sha256": last_metadata.get("output_sha256", "unknown"),
        "events": [
            {"sequence": event["sequence"], "at": event["at"], "status": event["status"],
             "event_hash": event["event_hash"]}
            for event in events
        ],
        "notice": "Redacted metadata only; provider/base prompts and full effective context are not recorded.",
    }
    return result
