"""One task/revision for declared session contributions and bounded observations.

No model is called or impersonated here. A session's text is a contribution;
only the fixed local runner and the pinned GitHub transport produce operation
receipts. Neither kind of receipt completes the task or verifies its acceptance
criteria. A durable claim precedes all external work and is never retried here.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time

from . import gateway
from .adapters.github import GitHubClient, GitHubError, validate_ref, validate_repository
from .core import CoreError, _json, _now, _text
from .exchange import ExchangeStore

LOCAL_OPERATIONS = frozenset({"repo_revision", "repo_status", "python_version"})
LOCAL_STATUSES = frozenset({"completed", "failed", "timeout", "output_limit", "spawn_error"})
OUTPUT_LIMIT = 65536
TIMEOUT_SECONDS = 10
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_GITHUB_CODES = frozenset({"github_error", "invalid_input", "invalid_response",
                           "redirect_refused", "unauthorized", "forbidden",
                           "not_found", "rate_limited", "http_error", "conflict",
                           "transport_error", "credentials_required"})


def _run_local(operation, cwd, *, timeout_seconds=TIMEOUT_SECONDS, output_limit=OUTPUT_LIMIT):
    # Loading the runner does not open a fresh provider/model session. Lazy
    # import also keeps read-only views independent of the local process adapter.
    from .operations import run_local
    return run_local(operation, cwd, timeout_seconds=timeout_seconds, output_limit=output_limit)


def _cwd(value):
    if isinstance(value, os.PathLike):
        value = os.fspath(value)
    value = _text(value, "cwd", 32768)
    try:
        return str(Path(value).expanduser().resolve())
    except (OSError, RuntimeError, ValueError) as exc:
        raise CoreError("CLI çalışma dizini geçersiz.") from exc


def _local_receipt(value, operation, cwd):
    """Bound the internal runner's result without replacing its captured hashes."""
    if (not isinstance(value, dict) or value.get("status") not in LOCAL_STATUSES
            or value.get("operation") != operation or value.get("cwd") != cwd):
        raise CoreError("Yerel işlem makbuzu istenen işlemle uyuşmuyor.")
    if (not isinstance(value.get("argv"), list) or len(value["argv"]) > 32
            or any(not isinstance(arg, str) or len(arg) > 32768 for arg in value["argv"])):
        raise CoreError("Yerel işlem komut makbuzu geçersiz.")
    platform_info = value.get("platform")
    if isinstance(platform_info, dict):
        fields = {"system", "release", "machine", "python_implementation", "python_version"}
        if set(platform_info) != fields:
            raise CoreError("Yerel işlem platform makbuzu beklenen beş alanı içermeli.")
        for field in fields:
            text = platform_info[field]
            if not isinstance(text, str) or len(text) > 256:
                raise CoreError("Yerel işlem platform alanları sınırlı metin olmalı.")
            text.encode("utf-8")
    else:
        # Keep the compact platform label used by local start-error receipts.
        _text(platform_info, "platform", 256)
    for field in ("started_at", "finished_at"):
        _text(value.get(field), field, 256)
    duration = value.get("duration_ms")
    if (type(duration) not in (int, float) or not math.isfinite(duration) or duration < 0
            or (value.get("exit_code") is not None and type(value["exit_code"]) is not int)
            or (value["status"] == "completed" and value.get("exit_code") != 0)):
        raise CoreError("Yerel işlem süre veya çıkış makbuzu geçersiz.")
    for field in ("stdout", "stderr"):
        stream = value.get(field)
        if (not isinstance(stream, dict) or not isinstance(stream.get("text"), str)
                or type(stream.get("captured_bytes")) is not int
                or not 0 <= stream["captured_bytes"] <= OUTPUT_LIMIT
                or not isinstance(stream.get("sha256"), str)
                or not _DIGEST.fullmatch(stream["sha256"])
                or type(stream.get("truncated")) is not bool
                # backslashreplace renders an invalid byte as four ASCII chars.
                or len(stream["text"].encode("utf-8")) > 4 * OUTPUT_LIMIT):
            raise CoreError("Yerel işlem çıktı makbuzu geçersiz veya çok büyük.")
    # A plain JSON copy also refuses non-JSON objects and non-finite fields.
    return json.loads(_json(value))


def _unavailable_local_receipt(operation, cwd, started, clock, status):
    empty = {"text": "", "captured_bytes": 0,
             "sha256": hashlib.sha256(b"").hexdigest(), "truncated": False}
    return {"operation": operation, "cwd": cwd, "argv": [], "platform": sys.platform,
            "status": status, "started_at": started, "finished_at": _now(),
            "duration_ms": round((time.monotonic() - clock) * 1000, 3), "exit_code": None,
            "stdout": dict(empty), "stderr": dict(empty),
            "error": {"code": "runner_start_failed" if status == "spawn_error" else "runner_result_unavailable",
                      "message": "Yerel işlem başlatılamadı; otomatik tekrar yapılmadı." if status == "spawn_error"
                      else "Yerel işlemin sonucu doğrulanamadı; otomatik tekrar yapılmadı."}}


class JointService:
    """Shared records; existing model sessions and task verification stay intact."""

    def __init__(self, store, *, github_client=None):
        self.store = store
        self.github_client = github_client
        # ExchangeStore deliberately refuses being inside a task data area.
        # A sibling keeps both ledgers independent, while task sources retain
        # every byte needed by the existing backup and handoff mechanisms.
        self.exchange_directory = store.directory.with_name(store.directory.name + "-joint-exchange")

    def contribute(self, task_id, author, session_id, relayed_by, stage, body,
                   expected_revision, request_key, references=None):
        return self.store.record_contribution(task_id, author, session_id, relayed_by,
                                              stage, body, expected_revision,
                                              request_key, references)

    def operate(self, task_id, operation, cwd, expected_revision, request_key, stage=64):
        if not isinstance(operation, str) or operation not in LOCAL_OPERATIONS:
            raise CoreError("İşlem repo_revision, repo_status veya python_version olmalı.")
        cwd = _cwd(cwd)
        prepared, claimed = self.store.prepare_joint_operation(
            task_id, "local_cli", stage, {"operation": operation, "cwd": cwd},
            expected_revision, request_key)
        if not claimed:
            return prepared
        started, clock = _now(), time.monotonic()
        try:
            returned = _run_local(operation, cwd, timeout_seconds=TIMEOUT_SECONDS,
                                  output_limit=OUTPUT_LIMIT)
        except (ValueError, OSError):
            # The fixed runner rejects invalid inputs / unavailable execution
            # before spawning. Preserve a bounded start-failure receipt.
            receipt = _unavailable_local_receipt(operation, cwd, started, clock, "spawn_error")
        except Exception:
            # The runner may have started a process before an unexpected error.
            # Do not call that a known failure, expose raw errors, or run again.
            receipt = _unavailable_local_receipt(operation, cwd, started, clock, "unknown")
        else:
            try:
                receipt = _local_receipt(returned, operation, cwd)
            except (CoreError, UnicodeError, TypeError, OverflowError):
                receipt = _unavailable_local_receipt(operation, cwd, started, clock, "unknown")
        return self.store.finish_joint_operation(task_id, prepared["operation_id"], receipt)

    def fetch_github(self, task_id, repository, ref, paths, expected_revision,
                     request_key, stage=32):
        repository, ref = validate_repository(repository), validate_ref(ref)
        paths = gateway._paths(paths)
        prepared, claimed = self.store.prepare_joint_operation(
            task_id, "github_fetch", stage,
            {"repository": repository, "ref": ref, "paths": paths},
            expected_revision, request_key)
        if not claimed:
            return prepared
        started, clock, captures = _now(), time.monotonic(), []
        try:
            exchange = ExchangeStore(self.exchange_directory)
            client = self.github_client if self.github_client is not None else GitHubClient.from_env()
            transfer = gateway.fetch(
                exchange, client, repository=repository, ref=ref, paths=paths,
                purpose="Selected sources for an explicitly requested shared task operation",
                request_key="joint-" + prepared["operation_id"])
            files = []
            for item in transfer["manifest"]["files"]:
                origin = dict(transfer["source_paths"][item["path"]])
                data = exchange.read_object(transfer["id"], item["sha256"])
                origin["requested_ref"] = ref
                captures.append({"data": data, "provenance": origin})
                files.append({key: item[key] for key in ("path", "bytes", "sha256")}
                             | {key: origin[key] for key in ("blob_sha", "mode")})
            receipt = {"status": "completed", "provider": "github", "repository": repository,
                       "requested_ref": ref, "commit": transfer["origin"]["commit"],
                       "tree": transfer["origin"]["tree"], "transfer_id": transfer["id"],
                       "files": files, "content_executed": False,
                       "task_completion_verified": False}
        except Exception as exc:
            # GitHubError is sanitized by the existing transport; whitelist the
            # machine-readable code anyway, never persist arbitrary error text.
            code = exc.code if isinstance(exc, GitHubError) and exc.code in _GITHUB_CODES else "fetch_failed"
            status = exc.status if isinstance(exc, GitHubError) and type(exc.status) is int else None
            receipt = {"status": "failed", "provider": "github", "repository": repository,
                       "requested_ref": ref,
                       "error": {"code": code, "http_status": status,
                                 "message": "Seçilen GitHub kaynakları alınamadı; otomatik tekrar yapılmadı."}}
            captures = []
        receipt.update(started_at=started, finished_at=_now(),
                       duration_ms=round((time.monotonic() - clock) * 1000, 3))
        return self.store.finish_joint_operation(task_id, prepared["operation_id"], receipt, captures)

    def view(self, task_id):
        return self.store.joint_view(task_id)
