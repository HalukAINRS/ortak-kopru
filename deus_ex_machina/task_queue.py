#!/usr/bin/env python3
"""Offline, user-controlled task queue; this module never launches a participant CLI."""
import argparse
import contextlib
import datetime
import json
import os
import re
import sys
import tempfile
import uuid
from pathlib import Path


TOPICS = ("Steering", "deus_ex_machina")
PARTICIPANTS = ("Hacker", "Şaman", "Şahit", "Gemini")
SCOPES = ("read_only", "manual_cli")
SCHEMA_VERSION = 1


class QueueError(ValueError):
    pass


def _now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def _clean_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise QueueError(f"{label} must be a non-empty string")
    if any(ord(char) < 32 and char not in "\t\n\r" for char in value):
        raise QueueError(f"{label} contains a control character")
    return value


def _unique_text(values, label, required=False):
    out = []
    seen = set()
    for value in values or []:
        value = _clean_text(value, label)
        if value not in seen:
            out.append(value)
            seen.add(value)
    if required and not out:
        raise QueueError(f"At least one {label} is required")
    return out


def _read_queue(path):
    path = Path(path)
    if path.is_symlink():
        raise QueueError("Queue file cannot be a symlink")
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "tasks": []}
    try:
        queue = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise QueueError(f"Cannot read task queue: {exc}") from None
    if not isinstance(queue, dict) or queue.get("schema_version") != SCHEMA_VERSION or not isinstance(queue.get("tasks"), list):
        raise QueueError("Unsupported or malformed task queue")
    return queue


@contextlib.contextmanager
def _exclusive_queue(path):
    target = Path(path)
    parent = target.parent
    parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink():
        raise QueueError("Queue file cannot be a symlink")
    lock = Path(str(target) + ".lock")
    try:
        descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise QueueError("Task queue is locked; do not run a second writer") from None
    try:
        with os.fdopen(descriptor, "w", encoding="ascii") as stream:
            stream.write("queue-write-lock\n")
        yield target
    finally:
        try:
            lock.unlink()
        except FileNotFoundError:
            pass


def _write_queue(path, queue):
    target = Path(path)
    encoded = (json.dumps(queue, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix=".tasks-", suffix=".tmp", dir=target.parent)
    try:
        if os.name != "nt":
            os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(encoded)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _find_task(queue, task_id):
    for task in queue["tasks"]:
        if task["task_id"] == task_id:
            return task
    raise QueueError(f"Unknown task id: {task_id}")


def _event(task, name, note=""):
    task["audit"].append({"event": name, "at": _now(), "note": note})
    task["updated_at"] = task["audit"][-1]["at"]


def create_task(path, original_user_words, topic, participant, acceptance_criteria, evidence_refs=(), requested_scope="read_only"):
    words = _clean_text(original_user_words, "Original user words")
    if topic not in TOPICS:
        raise QueueError(f"Unknown topic: {topic}")
    if participant not in PARTICIPANTS:
        raise QueueError(f"Unknown participant: {participant}")
    if requested_scope not in SCOPES:
        raise QueueError(f"Unknown permission scope: {requested_scope}")
    criteria = _unique_text(acceptance_criteria, "acceptance criterion", required=True)
    references = _unique_text(evidence_refs, "evidence reference")
    now = _now()
    task = {
        "schema_version": SCHEMA_VERSION,
        "task_id": str(uuid.uuid4()),
        "created_at": now,
        "updated_at": now,
        "original_user_words": words,
        "topic": topic,
        "participant": participant,
        "evidence_sources": [
            {
                "source_path": ref,
                "version": "unspecified",
                "sha256": "unknown",
                "observation_method": "reference supplied at task creation",
                "access": "not_verified",
                "evidence_status": "reference_only",
                "purpose": "task evidence reference",
                "write_permission": "none",
            }
            for ref in references
        ],
        "acceptance_criteria": criteria,
        "permission_scope": {"requested": requested_scope, "approved": None},
        "approval": {"state": "pending", "scope": None, "confirmed_at": None, "identity_verified": False},
        "status": "planned",
        "result": None,
        "artifact_refs": [],
        "verification": None,
        "audit": [{"event": "created", "at": now, "note": "User words stored as supplied; creator identity is not authenticated."}],
    }
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        queue["tasks"].append(task)
        _write_queue(target, queue)
    return task


def approve_task(path, task_id, scope, confirm_reviewed=False):
    if not confirm_reviewed:
        raise QueueError("Approval requires explicit confirmation after reviewing the task and scope")
    if scope not in SCOPES:
        raise QueueError(f"Unknown permission scope: {scope}")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] != "planned" or task["approval"]["state"] != "pending":
            raise QueueError("Only a planned task with pending approval can be approved")
        if scope == "manual_cli" and task["permission_scope"]["requested"] != "manual_cli":
            raise QueueError("Cannot expand a read_only task to manual_cli during approval")
        task["permission_scope"]["approved"] = scope
        task["approval"] = {"state": "approved", "scope": scope, "confirmed_at": _now(), "identity_verified": False}
        _event(task, "approved", f"Local operator assertion; approved scope: {scope}. Identity is not authenticated.")
        _write_queue(target, queue)
    return task


def begin_manual_task(path, task_id, confirm_manual_cli=False):
    if not confirm_manual_cli:
        raise QueueError("Beginning requires explicit confirmation; no participant process will be launched")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] != "planned" or task["approval"]["state"] != "approved":
            raise QueueError("Task is not approved and available to begin")
        if task["permission_scope"]["approved"] != "manual_cli":
            raise QueueError("Manual participant work requires a separate manual_cli approval")
        task["status"] = "running"
        task["approval"]["state"] = "consumed"
        _event(task, "manual_work_started", "One-time approval consumed; user must launch the participant manually. No subprocess was started.")
        _write_queue(target, queue)
    return task


def begin_read_only_task(path, task_id, confirm_read_only_work=False):
    if not confirm_read_only_work:
        raise QueueError("Beginning requires explicit confirmation; no participant process will be launched")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] != "planned" or task["approval"]["state"] != "approved":
            raise QueueError("Task is not approved and available to begin")
        if task["permission_scope"]["approved"] != "read_only":
            raise QueueError("Read-only work requires a separate read_only approval")
        task["status"] = "running"
        task["approval"]["state"] = "consumed"
        _event(task, "read_only_work_started", "One-time approval consumed; read-only work only. No participant process was started.")
        _write_queue(target, queue)
    return task


def record_result(path, task_id, result_text, evidence_refs=(), artifact_refs=()):
    result_text = _clean_text(result_text, "Result")
    evidence = _unique_text(evidence_refs, "evidence reference")
    artifacts = _unique_text(artifact_refs, "artifact reference")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] != "running":
            raise QueueError("A result can only be recorded for a running task")
        known = {source["source_path"] for source in task["evidence_sources"]}
        for ref in evidence:
            if ref not in known:
                task["evidence_sources"].append({
                    "source_path": ref,
                    "version": "unspecified",
                    "sha256": "unknown",
                    "observation_method": "reference supplied with participant output",
                    "access": "not_verified",
                    "evidence_status": "reference_only",
                    "purpose": "result evidence reference",
                    "write_permission": "none",
                })
        task["artifact_refs"] = list(dict.fromkeys(task["artifact_refs"] + artifacts))
        task["result"] = {
            "classification": (
                "local_operator_observation_not_user_instruction"
                if task["permission_scope"]["approved"] == "read_only"
                else "participant_output_not_user_instruction"
            ),
            "text": result_text,
            "recorded_at": _now(),
        }
        task["status"] = "unverified"
        _event(task, "result_recorded", "Participant output is not user authority; evidence references require independent review.")
        _write_queue(target, queue)
    return task


def verify_evidence(path, task_id, source_ref, version, sha256, observation_method, purpose, confirm_observed=False):
    source_ref = _clean_text(source_ref, "Evidence reference")
    version = _clean_text(version, "Evidence version")
    observation_method = _clean_text(observation_method, "Observation method")
    purpose = _clean_text(purpose, "Evidence purpose")
    if not re.fullmatch(r"[0-9a-fA-F]{64}", sha256 or ""):
        raise QueueError("Evidence hash must be a 64-character SHA-256 hex digest")
    if not confirm_observed:
        raise QueueError("Evidence verification requires an explicit local observation assertion")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] in ("completed", "blocked"):
            raise QueueError(f"Cannot verify evidence for a {task['status']} task")
        source = next((item for item in task["evidence_sources"] if item["source_path"] == source_ref), None)
        if source is None:
            raise QueueError("Evidence reference is not attached to this task")
        source.update({
            "version": version,
            "sha256": sha256.lower(),
            "observation_method": observation_method,
            "access": "observed_by_local_operator",
            "evidence_status": "verified_by_local_operator",
            "purpose": purpose,
            "write_permission": "none",
        })
        _event(task, "evidence_observed", "Local operator assertion; identity, source authenticity, and factual truth are not independently verified.")
        _write_queue(target, queue)
    return task


def complete_task(path, task_id, satisfied_criteria, confirm_acceptance=False):
    if not confirm_acceptance:
        raise QueueError("Completion requires an explicit acceptance assertion")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] != "unverified" or task["result"] is None:
            raise QueueError("Only a task with a recorded, unverified result can be completed")
        if not any(source["evidence_status"] == "verified_by_local_operator" for source in task["evidence_sources"]):
            raise QueueError("Cannot complete without a locally observed evidence source and recorded hash")
        satisfied = set(_unique_text(satisfied_criteria, "satisfied criterion"))
        required = set(task["acceptance_criteria"])
        if satisfied != required:
            raise QueueError("Completion requires an explicit assertion for every acceptance criterion")
        task["status"] = "completed"
        task["verification"] = {
            "classification": "local_operator_assertion_not_identity_verified",
            "satisfied_criteria": task["acceptance_criteria"],
            "confirmed_at": _now(),
        }
        _event(task, "completed", "Acceptance criteria asserted locally; identity and factual truth are not cryptographically verified.")
        _write_queue(target, queue)
    return task


def block_task(path, task_id, reason):
    reason = _clean_text(reason, "Block reason")
    with _exclusive_queue(path) as target:
        queue = _read_queue(target)
        task = _find_task(queue, task_id)
        if task["status"] in ("completed", "blocked"):
            raise QueueError(f"Cannot block a {task['status']} task")
        task["status"] = "blocked"
        _event(task, "blocked", reason)
        _write_queue(target, queue)
    return task


def list_tasks(path, topic=None):
    queue = _read_queue(path)
    return [task for task in queue["tasks"] if topic is None or task["topic"] == topic]


def _read_argument(text, file_path):
    if text is not None:
        return text
    return Path(file_path).read_text(encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline deus_ex_machina task queue; participant CLIs are never launched.")
    parser.add_argument("--queue", default=str(Path.home() / ".ortak-kopru" / "tasks.json"))
    commands = parser.add_subparsers(dest="command", required=True)

    create = commands.add_parser("create", help="store the exact original user words")
    words = create.add_mutually_exclusive_group(required=True)
    words.add_argument("--words")
    words.add_argument("--words-file")
    create.add_argument("--topic", required=True, choices=TOPICS)
    create.add_argument("--participant", required=True, choices=PARTICIPANTS)
    create.add_argument("--criterion", action="append", required=True)
    create.add_argument("--evidence", action="append", default=[])
    create.add_argument("--permission-scope", choices=SCOPES, default="read_only")

    approve = commands.add_parser("approve", help="record a local, scoped approval")
    approve.add_argument("task_id")
    approve.add_argument("--scope", required=True, choices=SCOPES)
    approve.add_argument("--confirm-reviewed", action="store_true")

    begin = commands.add_parser("begin", help="consume approval and reserve manual work; launches nothing")
    begin.add_argument("task_id")
    begin_confirmation = begin.add_mutually_exclusive_group(required=True)
    begin_confirmation.add_argument("--confirm-manual-cli", action="store_true")
    begin_confirmation.add_argument("--confirm-read-only", action="store_true")

    record = commands.add_parser("record", help="record an outcome without granting it user authority")
    record.add_argument("task_id")
    result = record.add_mutually_exclusive_group(required=True)
    result.add_argument("--result")
    result.add_argument("--result-file")
    record.add_argument("--evidence", action="append", default=[])
    record.add_argument("--artifact", action="append", default=[])

    verify = commands.add_parser("verify-evidence", help="record a local observation and source hash")
    verify.add_argument("task_id")
    verify.add_argument("--source-ref", required=True)
    verify.add_argument("--version", required=True)
    verify.add_argument("--sha256", required=True)
    verify.add_argument("--method", required=True)
    verify.add_argument("--purpose", required=True)
    verify.add_argument("--confirm-observed", action="store_true")

    complete = commands.add_parser("complete", help="mark complete after evidence and all acceptance checks")
    complete.add_argument("task_id")
    complete.add_argument("--satisfied", action="append", default=[])
    complete.add_argument("--confirm-acceptance", action="store_true")

    block = commands.add_parser("block", help="block a task with a reason")
    block.add_argument("task_id")
    block.add_argument("--reason", required=True)

    show = commands.add_parser("show", help="print one task as JSON")
    show.add_argument("task_id")

    listing = commands.add_parser("list", help="list local tasks, optionally by topic")
    listing.add_argument("--topic", choices=TOPICS)

    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            task = create_task(args.queue, _read_argument(args.words, args.words_file), args.topic, args.participant,
                               args.criterion, args.evidence, args.permission_scope)
            print(task["task_id"])
            return 0
        if args.command == "approve":
            approve_task(args.queue, args.task_id, args.scope, args.confirm_reviewed)
        elif args.command == "begin":
            if args.confirm_manual_cli:
                begin_manual_task(args.queue, args.task_id, confirm_manual_cli=True)
                print("Reserved for manual participant work only; no participant CLI was launched.")
            else:
                begin_read_only_task(args.queue, args.task_id, confirm_read_only_work=True)
                print("Reserved for read-only work only; no participant CLI was launched.")
            return 0
        elif args.command == "record":
            record_result(args.queue, args.task_id, _read_argument(args.result, args.result_file), args.evidence, args.artifact)
        elif args.command == "verify-evidence":
            verify_evidence(args.queue, args.task_id, args.source_ref, args.version, args.sha256,
                            args.method, args.purpose, args.confirm_observed)
        elif args.command == "complete":
            complete_task(args.queue, args.task_id, args.satisfied, args.confirm_acceptance)
        elif args.command == "block":
            block_task(args.queue, args.task_id, args.reason)
        elif args.command == "show":
            task = next((item for item in list_tasks(args.queue) if item["task_id"] == args.task_id), None)
            if task is None:
                raise QueueError(f"Unknown task id: {args.task_id}")
            print(json.dumps(task, ensure_ascii=False, indent=2))
            return 0
        elif args.command == "list":
            print(json.dumps(list_tasks(args.queue, args.topic), ensure_ascii=False, indent=2))
            return 0
        print(json.dumps(_find_task(_read_queue(args.queue), args.task_id), ensure_ascii=False, indent=2))
        return 0
    except (QueueError, OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
