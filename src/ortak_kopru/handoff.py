"""Recorded session discovery and private, provider-independent handoff files.

A prepared package is a snapshot, never a delivery or execution receipt.
Verification establishes package integrity, not identity, authority, or current
assignment eligibility. The receiver must still use the live receive operation.
No provider, process, network, or kernel call is performed by this module.
"""
from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import stat

from .core import Conflict, CoreError, MAX_FILE_BYTES, NotFound, _json, _now, _text
from .local_files import (
    copy_verified_file, file_record, new_private_directory, private_path,
    read_regular_file, write_private_file,
)

HANDOFF_SCHEMA_VERSION = 1
MAX_MANIFEST_BYTES = 4 * 1024 * 1024
MAX_CONTEXT_BYTES = 64 * 1024 * 1024
MAX_OBJECTS = 8192
MAX_PACKAGE_BYTES = 1024 * 1024 * 1024
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_IDENTITY = re.compile(r"[0-9a-f]{32}\Z")
_MANIFEST_FIELDS = {
    "schema_version", "kind", "classification", "created_at", "task_id",
    "revision", "attempt_id", "session_id", "participant", "preparation",
    "context", "objects",
}


def _eligible(task, attempt):
    return (
        task["active_attempt_id"] == attempt["id"]
        and task["revision"] == attempt["revision"]
        and (task["status"], attempt["status"]) in {
            ("ready", "assigned"), ("running", "received"),
        }
    )


def list_sessions(store):
    """Summarize recorded session labels; never claim a live provider session."""
    sessions = {}
    with store._db() as db:
        rows = db.execute("""SELECT a.*, t.status AS task_status,
            t.revision AS task_revision, t.active_attempt_id
            FROM attempts a JOIN tasks t ON t.id=a.task_id""")
        for row in rows:
            item = sessions.setdefault(row["session_id"], {
                "session_id": row["session_id"], "participants": set(),
                "attempt_count": 0, "active_count": 0, "pending_count": 0,
                "received_count": 0, "latest_recorded_at": row["updated_at"],
                "liveness": "not_observed", "identity_verified": False,
            })
            item["participants"].add(row["participant"])
            item["attempt_count"] += 1
            item["latest_recorded_at"] = max(item["latest_recorded_at"], row["updated_at"])
            task = {"active_attempt_id": row["active_attempt_id"],
                    "revision": row["task_revision"], "status": row["task_status"]}
            if _eligible(task, row):
                item["active_count"] += 1
                item["pending_count" if row["status"] == "assigned" else "received_count"] += 1
    for item in sessions.values():
        item["participants"] = sorted(item["participants"])
    return {"sessions": sorted(sessions.values(),
                               key=lambda item: (item["latest_recorded_at"], item["session_id"]),
                               reverse=True)}


def inbox(store, session_id):
    """Return only current assigned/received work for the exact session label."""
    session = _text(session_id, "session_id", 256)
    with store._db() as db:
        rows = db.execute("""SELECT t.id AS task_id, t.revision,
            a.id AS attempt_id, a.participant, a.session_id,
            t.status AS task_status, a.status AS attempt_status, a.delivery_status,
            r.original_words AS current_words, a.created_at AS assigned_at, a.updated_at
            FROM attempts a JOIN tasks t ON t.id=a.task_id
            JOIN revisions r ON r.task_id=t.id AND r.revision=t.revision
            WHERE a.session_id=? AND t.active_attempt_id=a.id AND t.revision=a.revision
            AND ((t.status='ready' AND a.status='assigned')
                 OR (t.status='running' AND a.status='received'))
            ORDER BY a.created_at, a.id""", (session,))
        items = [dict(row) for row in rows]
    return {"session_id": session, "items": items,
            "observation": "recorded_active_assignments"}


def _record(value, *, context=False):
    if not isinstance(value, dict) or set(value) != {"path", "bytes", "sha256"}:
        raise CoreError("Devir dosyası kaydı path/bytes/sha256 alanlarını taşımalı.")
    digest, size = value["sha256"], value["bytes"]
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise CoreError("Devir dosyası SHA-256 değeri geçersiz.")
    limit = MAX_CONTEXT_BYTES if context else MAX_FILE_BYTES
    if type(size) is not int or not 0 <= size <= limit:
        raise CoreError("Devir dosyası boyutu geçersiz veya sınırı aşıyor.")
    expected_path = "context.json" if context else "objects/" + digest
    if value["path"] != expected_path:
        raise CoreError("Devir dosyası yolu sabit paket düzeniyle uyuşmuyor.")
    return dict(value)


def _objects(context):
    """Collect every source/artifact snapshot without following original paths."""
    sources, results = context.get("sources"), context.get("previous_results")
    if not isinstance(sources, list) or not isinstance(results, list):
        raise CoreError("Devir bağlamı kaynak ve önceki sonuç listelerini taşımalı.")
    references = list(sources)
    for result in results:
        if not isinstance(result, dict) or not isinstance(result.get("artifacts"), list):
            raise CoreError("Devir bağlamındaki önceki sonuç geçersiz.")
        references.extend(result["artifacts"])
    records = {}
    for reference in references:
        if not isinstance(reference, dict):
            raise CoreError("Devir kaynağı veya çıktısı geçersiz.")
        record = _record({"path": reference.get("snapshot"),
                          "bytes": reference.get("bytes"),
                          "sha256": reference.get("sha256")})
        previous = records.setdefault(record["path"], record)
        if previous != record:
            raise Conflict("Aynı devir nesnesi çelişen boyut veya karma taşıyor.")
        if len(records) > MAX_OBJECTS:
            raise CoreError("Devir paketinin nesne sayısı sınırı aşıldı.")
    return [records[path] for path in sorted(records)]


def _budget(context_record, objects, manifest_size=0):
    if len(objects) > MAX_OBJECTS:
        raise CoreError("Devir paketinin nesne sayısı sınırı aşıldı.")
    total = context_record["bytes"] + sum(record["bytes"] for record in objects) + manifest_size
    if total > MAX_PACKAGE_BYTES:
        raise CoreError("Devir paketinin toplam boyut sınırı aşıldı; hiçbir içerik atlanmadı.")


def create_handoff(store, attempt_id, session_id, destination_dir):
    """Publish a complete new private package without changing task/delivery state."""
    attempt_id = _text(attempt_id, "attempt_id", 80)
    session = _text(session_id, "session_id", 256)
    destination = private_path(destination_dir)
    if destination.is_relative_to(store.directory):
        raise CoreError("Devir paketi çalışma veritabanı dizininin dışında olmalı.")
    with store._db() as db:
        attempt = db.execute("SELECT * FROM attempts WHERE id=?", (attempt_id,)).fetchone()
        if attempt is None:
            raise NotFound("Devir için çalıştırma bulunamadı.")
        if attempt["session_id"] != session:
            raise Conflict("Devir atanmış oturuma ait olmalı.")
        task = store._task(db, attempt["task_id"])
        if not _eligible(task, attempt):
            raise Conflict("Devir için güncel, henüz sonuç üretmemiş çalıştırma gerekli.")
        attempt = dict(attempt)
    # Capture metadata consistently, then release the SQLite read transaction.
    # Immutable digest objects can be copied without delaying pause/cancel
    # commits. The package records this snapshot; a later live receive must
    # recheck eligibility even if cancellation occurred during preparation.
    context = store._context(task)
    context["handoff_attempt"] = {
        "attempt_id": attempt_id, "session_id": session,
        "participant": attempt["participant"],
    }
    context_bytes = (_json(context) + "\n").encode("utf-8")
    context_record = _record({"path": "context.json", "bytes": len(context_bytes),
                              "sha256": hashlib.sha256(context_bytes).hexdigest()}, context=True)
    objects = _objects(context)
    manifest = {
        "schema_version": HANDOFF_SCHEMA_VERSION, "kind": "deus_handoff",
        "classification": "private", "created_at": _now(),
        "task_id": task["id"], "revision": task["revision"],
        "attempt_id": attempt_id, "session_id": session, "participant": attempt["participant"],
        "preparation": {"task_status": task["status"], "attempt_status": attempt["status"],
                        "delivery_receipt": False, "live_receive_required": True},
        "context": context_record, "objects": objects,
    }
    manifest_bytes = (_json(manifest) + "\n").encode("utf-8")
    if len(manifest_bytes) > MAX_MANIFEST_BYTES:
        raise CoreError("Devir manifestosu boyut sınırını aşıyor.")
    _budget(context_record, objects, len(manifest_bytes))
    with new_private_directory(destination) as staging:
        (staging / "objects").mkdir(mode=0o700)
        for record in objects:
            copy_verified_file(store.directory / record["path"], staging / record["path"],
                               record, maximum=MAX_FILE_BYTES)
        write_private_file(staging / "context.json", context_bytes)
        write_private_file(staging / "manifest.json", manifest_bytes)
    return manifest


def _decode(data):
    def unique_pairs(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise CoreError("Devir JSON'unda yinelenen alan bulunuyor.")
            value[key] = item
        return value

    def invalid_constant(_value):
        raise CoreError("Devir JSON'unda sonlu olmayan sayı bulunuyor.")

    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=unique_pairs,
                          parse_constant=invalid_constant)
    except (UnicodeError, ValueError, RecursionError) as exc:
        if isinstance(exc, CoreError):
            raise
        raise CoreError("Devir JSON dosyası okunamadı.") from exc


def _directory(path):
    try:
        info = path.lstat()
    except OSError as exc:
        raise CoreError("Devir paketinin dizini bulunamadı.") from exc
    if not stat.S_ISDIR(info.st_mode) or (
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    ):
        raise CoreError("Devir paketi bağlantı olmayan bir dizin olmalı.")


def _manifest(value):
    if not isinstance(value, dict) or set(value) != _MANIFEST_FIELDS:
        raise CoreError("Devir manifestosunun alanları eksik veya tanımsız.")
    if type(value["schema_version"]) is not int or value["schema_version"] != HANDOFF_SCHEMA_VERSION:
        raise CoreError("Desteklenmeyen devir manifestosu sürümü.")
    if value["kind"] != "deus_handoff" or value["classification"] != "private":
        raise CoreError("Dosya özel DEUS devir manifestosu değil.")
    for name in ("task_id", "attempt_id"):
        if not isinstance(value[name], str) or not _IDENTITY.fullmatch(value[name]):
            raise CoreError("Devir işi veya çalıştırma kimliği geçersiz.")
    if type(value["revision"]) is not int or value["revision"] < 1:
        raise CoreError("Devir işinin sürümü geçersiz.")
    _text(value["session_id"], "session_id", 256)
    _text(value["participant"], "participant", 200)
    try:
        at = datetime.fromisoformat(_text(value["created_at"], "created_at", 80))
        if at.tzinfo is None:
            raise ValueError("timezone missing")
    except ValueError as exc:
        raise CoreError("Devir hazırlanma zamanı geçersiz.") from exc
    preparation = value["preparation"]
    if not isinstance(preparation, dict) or set(preparation) != {
        "task_status", "attempt_status", "delivery_receipt", "live_receive_required",
    }:
        raise CoreError("Devir hazırlık kaydı geçersiz.")
    if (preparation["task_status"], preparation["attempt_status"]) not in (
        ("ready", "assigned"), ("running", "received"),
    ) or preparation["delivery_receipt"] is not False or preparation["live_receive_required"] is not True:
        raise CoreError("Devir hazırlığı alım/çalıştırma makbuzu olarak sunulamaz.")
    _record(value["context"], context=True)
    if not isinstance(value["objects"], list) or len(value["objects"]) > MAX_OBJECTS:
        raise CoreError("Devir nesne listesi geçersiz veya sınırı aşıyor.")
    paths = set()
    for item in value["objects"]:
        record = _record(item)
        if record["path"] in paths:
            raise CoreError("Devir nesnesi manifestoda birden çok kez bulunuyor.")
        paths.add(record["path"])
    return value


def verify_handoff(package_dir):
    """Verify all package bytes/bindings, with no Store access or authority import.

    A package can remain intact after its live assignment is cancelled. This
    method does not authorize work; receive must check the current Store state.
    """
    try:
        root = Path(package_dir).expanduser().absolute()
    except (TypeError, ValueError, OSError) as exc:
        raise CoreError("Geçerli bir devir paketi dizini gerekli.") from exc
    _directory(root)
    _directory(root / "objects")
    expected_root = {"manifest.json", "context.json", "objects"}
    if {path.name for path in root.iterdir()} != expected_root:
        raise CoreError("Devir paketinde eksik veya manifestoya ait olmayan dosya var.")
    raw_manifest = read_regular_file(root / "manifest.json", maximum=MAX_MANIFEST_BYTES)
    manifest = _manifest(_decode(raw_manifest))
    _budget(manifest["context"], manifest["objects"], len(raw_manifest))
    raw_context = read_regular_file(root / "context.json", maximum=MAX_CONTEXT_BYTES)
    if (len(raw_context) != manifest["context"]["bytes"]
            or hashlib.sha256(raw_context).hexdigest() != manifest["context"]["sha256"]):
        raise Conflict("Devir bağlamının boyutu veya SHA-256 değeri uyuşmuyor.")
    context = _decode(raw_context)
    if not isinstance(context, dict) or (
        type(context.get("schema_version")) is not int
        or context.get("schema_version") != HANDOFF_SCHEMA_VERSION
        or context.get("kind") != "task_context"
        or context.get("task_id") != manifest["task_id"]
        or type(context.get("revision")) is not int
        or context["revision"] != manifest["revision"]
        or context.get("active_attempt_id") != manifest["attempt_id"]
        or context.get("status") != manifest["preparation"]["task_status"]
        or context.get("handoff_attempt") != {
            "attempt_id": manifest["attempt_id"], "session_id": manifest["session_id"],
            "participant": manifest["participant"],
        }
        or context.get("source_instructions_are_data") is not True
        or context.get("provider_context_visibility") != "application_bundle_only"
        or context.get("model_understanding_verified") is not False
    ):
        raise Conflict("Devir bağlamı iş/sürüm/çalıştırma/oturum bağıyla uyuşmuyor.")
    objects = _objects(context)
    if objects != sorted(manifest["objects"], key=lambda item: item["path"]):
        raise Conflict("Devir bağlamındaki bütün kaynak ve çıktı nesneleri pakette bulunmalı.")
    expected_names = {item["sha256"] for item in objects}
    actual_names = set()
    for path in (root / "objects").iterdir():
        if path.name not in expected_names:
            raise CoreError("Devir nesne dizininde manifestoya ait olmayan dosya var.")
        actual_names.add(path.name)
    if actual_names != expected_names:
        raise Conflict("Devir nesne dosyalarından biri eksik.")
    for record in objects:
        actual = file_record(root / record["path"], relative_path=record["path"], maximum=MAX_FILE_BYTES)
        if actual != record:
            raise Conflict("Devir kaynak veya çıktısının boyutu ya da SHA-256 değeri uyuşmuyor.")
    return manifest
