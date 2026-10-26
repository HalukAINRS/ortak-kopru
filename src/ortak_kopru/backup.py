"""Consistent, verified private backups of the task database and its objects.

The SQLite backup API captures committed database state, including the request
ledger and complete task history. Only objects referenced by that snapshot are
included. Runtime credentials and unrelated files are deliberately not copied.
Manifests establish byte integrity, not authorship or independent truth.
"""
from __future__ import annotations

from contextlib import closing
from datetime import datetime, timezone
from functools import wraps
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import time

from .core import MAX_FILE_BYTES, MAX_REFERENCES, SCHEMA_VERSION, TASK_STATES, _authority, _criteria, _text
from .local_files import (
    LocalFileError,
    copy_verified_file,
    file_record,
    new_private_directory,
    private_path,
    read_regular_file,
    write_private_file,
)

FORMAT_VERSION = 1
MAX_MANIFEST_BYTES = 16 * 1024 * 1024
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_TABLE_COLUMNS = {
    "metadata": ("key", "value"),
    "tasks": ("id", "original_words", "authority", "criteria", "revision", "status", "active_attempt_id", "current_result_id", "created_at", "updated_at"),
    "revisions": ("task_id", "revision", "original_words", "created_at"),
    "sources": ("task_id", "source_id", "position", "data"),
    "attempts": ("id", "task_id", "revision", "participant", "session_id", "status", "delivery_status", "created_at", "updated_at"),
    "results": ("id", "task_id", "attempt_id", "revision", "summary", "artifacts", "created_at"),
    "checks": ("task_id", "result_id", "criterion_id", "passed", "evidence", "verifier", "at"),
    "events": ("seq", "id", "task_id", "revision", "kind", "at", "data"),
    "requests": ("request_key", "operation", "payload_sha256", "response"),
    "sqlite_sequence": ("name", "seq"),
}


class BackupError(LocalFileError):
    """A backup is incomplete, corrupt, unsupported or cannot be published."""


def _operation(function):
    @wraps(function)
    def checked(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except BackupError:
            raise
        except (LocalFileError, sqlite3.Error, OSError, ValueError, TypeError) as exc:
            raise BackupError(f"Yedekleme işlemi tamamlanamadı: {exc}") from exc
    return checked


def _directory(path):
    directory = private_path(path)
    if not directory.is_dir():
        raise BackupError("Kaynak, var olan özel bir dizin olmalı.")
    return directory


def _regular_path(path):
    path = private_path(path)
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode):
        raise BackupError("Veritabanı bağlantı olmayan düzenli bir dosya olmalı.")
    return path


def _destination(source, destination):
    target = private_path(destination)
    if target.is_relative_to(source):
        raise BackupError("Hedef dizin kaynak dizinin içinde olamaz.")
    return target


def _unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise BackupError("JSON içinde yinelenen alan adı var.")
        value[key] = item
    return value


def _invalid_constant(value):
    raise BackupError(f"JSON sayısı geçersiz: {value}")


def _load_json(data):
    return json.loads(data, object_pairs_hook=_unique_object, parse_constant=_invalid_constant)


def _reference_record(reference):
    if not isinstance(reference, dict):
        raise BackupError("Veritabanındaki dosya başvurusu geçersiz.")
    digest, size = reference.get("sha256"), reference.get("bytes")
    if not isinstance(digest, str) or not _DIGEST.fullmatch(digest):
        raise BackupError("Dosya başvurusunun SHA-256 değeri geçersiz.")
    if type(size) is not int or not 0 <= size <= MAX_FILE_BYTES:
        raise BackupError("Dosya başvurusunun boyutu geçersiz.")
    relative = f"objects/{digest}"
    if reference.get("snapshot") != relative:
        raise BackupError("Dosya başvurusu beklenen hash nesnesini göstermiyor.")
    if reference.get("kind") != "local_file" or reference.get("instruction_authority") is not False:
        raise BackupError("Kaynak türü veya talimat yetkisi kaydı geçersiz.")
    if not isinstance(reference.get("id"), str) or not _DIGEST.fullmatch(reference["id"]):
        raise BackupError("Kaynak kimliği geçersiz.")
    _text(reference.get("path"), "source.path", 32768)
    return {"path": relative, "bytes": size, "sha256": digest}


def _validate_application_records(db):
    """Validate links the v1 SQL schema cannot express as foreign keys.

    This verifies readability and the core's current-state invariants, not the
    truth of user declarations. Historical results/checks remain valid even
    after a later correction or an interrupted attempt.
    """
    db.row_factory = sqlite3.Row
    try:
        for task in db.execute("SELECT * FROM tasks"):
            _text(task["id"], "task.id", 80)
            _text(task["original_words"], "task.original_words")
            revision = task["revision"]
            if type(revision) is not int or revision < 1 or task["status"] not in TASK_STATES:
                raise BackupError("Görevin sürümü veya durumu geçersiz.")
            authority, criteria = _load_json(task["authority"]), _load_json(task["criteria"])
            if authority != _authority(authority) or criteria != _criteria(criteria):
                raise BackupError("Görevin yetki veya kabul ölçütü kaydı geçersiz.")
            criterion_ids = {item["id"] for item in criteria}
            revisions = list(db.execute("SELECT * FROM revisions WHERE task_id=? ORDER BY revision", (task["id"],)))
            if len(revisions) != revision or any(row["revision"] != index for index, row in enumerate(revisions, 1)):
                raise BackupError("Görevin revizyon zinciri eksik veya güncel sürümüyle uyuşmuyor.")
            if revisions[0]["original_words"] != task["original_words"]:
                raise BackupError("Görevin özgün sözleri ilk revizyonla uyuşmuyor.")
            for row in revisions:
                _text(row["original_words"], "revision.original_words")

            attempts = {row["id"]: row for row in db.execute("SELECT * FROM attempts WHERE task_id=?", (task["id"],))}
            results = {row["id"]: row for row in db.execute("SELECT * FROM results WHERE task_id=?", (task["id"],))}
            for attempt in attempts.values():
                _text(attempt["participant"], "attempt.participant", 200)
                _text(attempt["session_id"], "attempt.session_id", 256)
                if type(attempt["revision"]) is not int or not 1 <= attempt["revision"] <= revision:
                    raise BackupError("Çalıştırma var olmayan bir görev revizyonuna bağlı.")
                if attempt["status"] not in ("assigned", "received", "result_submitted", "superseded", "interrupted") or attempt["delivery_status"] not in ("pending", "received"):
                    raise BackupError("Çalıştırma veya teslim durumu geçersiz.")
                if attempt["status"] in ("assigned", "received", "result_submitted") and task["active_attempt_id"] != attempt["id"]:
                    raise BackupError("Etkin olmayan çalıştırma etkin durumda görünüyor.")
            result_attempts = set()
            for result in results.values():
                attempt = attempts.get(result["attempt_id"])
                if attempt is None or result["revision"] != attempt["revision"] or result["attempt_id"] in result_attempts:
                    raise BackupError("Sonuç başka görevin çalıştırmasına veya yanlış sürüme bağlı.")
                if attempt["delivery_status"] != "received" or attempt["status"] in ("assigned", "received"):
                    raise BackupError("Sonucun çalıştırma teslim kaydı geçersiz.")
                _text(result["summary"], "result.summary")
                result_attempts.add(result["attempt_id"])
            active = attempts.get(task["active_attempt_id"])
            current = results.get(task["current_result_id"])
            if task["active_attempt_id"] is not None and (active is None or active["revision"] != revision):
                raise BackupError("Etkin çalıştırma göreve veya güncel sürüme ait değil.")
            if task["current_result_id"] is not None and (current is None or current["revision"] != revision or current["attempt_id"] != task["active_attempt_id"]):
                raise BackupError("Güncel sonuç göreve, sürüme veya etkin çalıştırmaya ait değil.")
            result_states = ("awaiting_verification", "blocked", "completed")
            expected_status = {"ready": "assigned", "running": "received", **{state: "result_submitted" for state in result_states}}
            if active is not None and active["status"] != expected_status.get(task["status"]):
                raise BackupError("Görev durumu etkin çalıştırmayla uyuşmuyor.")
            if task["status"] in ("running", *result_states) and active is None:
                raise BackupError("Görevin gerekli etkin çalıştırması eksik.")
            if (task["status"] in result_states) != (current is not None):
                raise BackupError("Görev durumu güncel sonuç kaydıyla uyuşmuyor.")
            if active is not None and active["delivery_status"] != ("pending" if active["status"] == "assigned" else "received"):
                raise BackupError("Etkin çalıştırmanın teslim kaydı geçersiz.")

            current_checks = {}
            for check in db.execute("SELECT * FROM checks WHERE task_id=?", (task["id"],)):
                if check["result_id"] not in results or check["criterion_id"] not in criterion_ids or type(check["passed"]) is not int or check["passed"] not in (0, 1):
                    raise BackupError("Denetim başka göreve, bilinmeyen ölçüte veya geçersiz sonuca bağlı.")
                _text(check["evidence"], "check.evidence")
                _text(check["verifier"], "check.verifier")
                if check["result_id"] == task["current_result_id"]:
                    current_checks[check["criterion_id"]] = bool(check["passed"])
            if current is not None:
                expected_state = "blocked" if any(not value for value in current_checks.values()) else "completed" if criterion_ids.issubset(current_checks) else "awaiting_verification"
                if task["status"] != expected_state:
                    raise BackupError("Görev durumu güncel sonucun kabul denetimleriyle uyuşmuyor.")
            for source in db.execute("SELECT source_id,data FROM sources WHERE task_id=?", (task["id"],)):
                data = _load_json(source["data"])
                if not isinstance(data, dict) or data.get("id") != source["source_id"]:
                    raise BackupError("Kaynak kimliği kayıtla uyuşmuyor.")
            for event in db.execute("SELECT revision,data FROM events WHERE task_id=?", (task["id"],)):
                if type(event["revision"]) is not int or not 1 <= event["revision"] <= revision or not isinstance(_load_json(event["data"]), dict):
                    raise BackupError("Olay revizyonu veya JSON verisi geçersiz.")
        for request in db.execute("SELECT response FROM requests"):
            if not isinstance(_load_json(request["response"]), dict):
                raise BackupError("Kayıtlı istek yanıtı geçerli bir JSON nesnesi değil.")
    finally:
        db.row_factory = None


def _inspect_database(path):
    """Check a closed standalone snapshot, never the changing live database."""
    records = {}
    uri = path.as_uri() + "?mode=ro&immutable=1"
    with closing(sqlite3.connect(uri, uri=True, timeout=30)) as db:
        db.execute("PRAGMA query_only=ON")
        db.execute("PRAGMA trusted_schema=OFF")
        db.execute("PRAGMA foreign_keys=ON")
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if tables != set(_TABLE_COLUMNS):
            raise BackupError("Veritabanı şeması eksik veya desteklenmiyor.")
        if db.execute("SELECT 1 FROM sqlite_master WHERE type IN ('view','trigger') LIMIT 1").fetchone():
            raise BackupError("Veritabanında desteklenmeyen görünüm veya tetikleyici var.")
        version = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
        if version != (str(SCHEMA_VERSION),):
            raise BackupError("Veritabanı şema sürümü desteklenmiyor.")
        for table, columns in _TABLE_COLUMNS.items():
            # Names here are fixed program constants, not imported SQL input.
            actual = tuple(row[1] for row in db.execute(f'PRAGMA table_info("{table}")'))
            if actual != columns:
                raise BackupError("Veritabanı tablo alanları eksik veya desteklenmiyor.")
        if db.execute("PRAGMA integrity_check").fetchall() != [("ok",)]:
            raise BackupError("SQLite bütünlük denetimi başarısız.")
        if db.execute("PRAGMA foreign_key_check").fetchone() is not None:
            raise BackupError("Veritabanında karşılığı olmayan bir kayıt başvurusu var.")
        _validate_application_records(db)

        def include(reference):
            record = _reference_record(reference)
            previous = records.get(record["path"])
            if previous is not None and previous != record:
                raise BackupError("Aynı nesne için çelişen dosya metadata'sı var.")
            records[record["path"]] = record

        for row in db.execute("SELECT data FROM sources"):
            include(_load_json(row[0]))
        for row in db.execute("SELECT artifacts FROM results"):
            artifacts = _load_json(row[0])
            if not isinstance(artifacts, list) or len(artifacts) > MAX_REFERENCES:
                raise BackupError("Sonucun dosya listesi geçersiz.")
            for artifact in artifacts:
                include(artifact)
        counts = {name: db.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
                  for name in ("tasks", "events", "results")}
    objects = [records[key] for key in sorted(records)]
    counts["objects"] = len(objects)
    return objects, counts


def _snapshot_database(source, destination):
    # Create privately before SQLite opens it. sqlite3's connection context
    # manager does not close handles, so closing() is explicit on every path.
    write_private_file(destination, b"")
    started = time.monotonic()

    def progress(status, remaining, total):
        if time.monotonic() - started > 30:
            raise BackupError("Tutarlı veritabanı görüntüsü 30 saniyede alınamadı; yeniden deneyin.")

    with closing(sqlite3.connect(source.as_uri() + "?mode=ro", uri=True, timeout=30)) as original:
        original.execute("PRAGMA query_only=ON")
        original.execute("PRAGMA trusted_schema=OFF")
        with closing(sqlite3.connect(destination, timeout=30)) as snapshot:
            original.backup(snapshot, pages=128, progress=progress, sleep=0.05)
            # A backup must stand alone; no live WAL or shared-memory files are
            # necessary to recover it, even when the source uses WAL mode.
            snapshot.execute("PRAGMA journal_mode=DELETE")
            snapshot.commit()
    with destination.open("rb+") as stream:
        os.fsync(stream.fileno())


def _record(value, expected_path, maximum=None):
    if not isinstance(value, dict) or set(value) != {"path", "bytes", "sha256"}:
        raise BackupError("Manifest dosya kaydı geçersiz.")
    if value["path"] != expected_path:
        raise BackupError("Manifest beklenmeyen bir dosya yolu içeriyor.")
    if type(value["bytes"]) is not int or value["bytes"] < 0 or (maximum is not None and value["bytes"] > maximum):
        raise BackupError("Manifest dosya boyutu geçersiz.")
    if not isinstance(value["sha256"], str) or not _DIGEST.fullmatch(value["sha256"]):
        raise BackupError("Manifest SHA-256 değeri geçersiz.")


def _manifest(data):
    manifest = _load_json(data)
    fields = {"format", "format_version", "schema_version", "classification", "integrity", "created_at", "database", "objects", "counts"}
    if not isinstance(manifest, dict) or set(manifest) != fields:
        raise BackupError("Yedek manifestinin alanları geçersiz.")
    if manifest["format"] != "ortak-kopru-backup" or type(manifest["format_version"]) is not int or manifest["format_version"] != FORMAT_VERSION:
        raise BackupError("Yedek biçimi desteklenmiyor.")
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != SCHEMA_VERSION:
        raise BackupError("Yedek şema sürümü desteklenmiyor.")
    if manifest["classification"] != "private" or manifest["integrity"] != "sha256_not_authentication":
        raise BackupError("Yedeğin gizlilik veya bütünlük tanımı geçersiz.")
    if not isinstance(manifest["created_at"], str) or datetime.fromisoformat(manifest["created_at"]).utcoffset() is None:
        raise BackupError("Yedek tarihi saat dilimi içermeli.")
    _record(manifest["database"], "deus.sqlite3")
    if not isinstance(manifest["objects"], list):
        raise BackupError("Manifest nesne listesi geçersiz.")
    seen = set()
    for record in manifest["objects"]:
        digest = record.get("sha256") if isinstance(record, dict) else None
        _record(record, f"objects/{digest}", MAX_FILE_BYTES)
        if record["path"] in seen:
            raise BackupError("Manifest aynı nesneyi birden fazla kez içeriyor.")
        seen.add(record["path"])
    if manifest["objects"] != sorted(manifest["objects"], key=lambda item: item["path"]):
        raise BackupError("Manifest nesneleri kanonik sırada değil.")
    counts = manifest["counts"]
    if not isinstance(counts, dict) or set(counts) != {"tasks", "events", "results", "objects"} or any(type(value) is not int or value < 0 for value in counts.values()):
        raise BackupError("Manifest kayıt sayıları geçersiz.")
    if counts["objects"] != len(manifest["objects"]):
        raise BackupError("Manifest nesne sayısı listeyle uyuşmuyor.")
    return manifest


def _verify_directory(directory):
    if {path.name for path in directory.iterdir()} != {"deus.sqlite3", "objects", "manifest.json", "manifest.sha256"}:
        raise BackupError("Yedek dizini eksik veya beklenmeyen dosya içeriyor.")
    _directory(directory / "objects")
    manifest_bytes = read_regular_file(directory / "manifest.json", maximum=MAX_MANIFEST_BYTES)
    checksum = read_regular_file(directory / "manifest.sha256", maximum=65)
    if checksum != (hashlib.sha256(manifest_bytes).hexdigest() + "\n").encode("ascii"):
        raise BackupError("Manifestin SHA-256 denetimi başarısız.")
    manifest = _manifest(manifest_bytes)
    if file_record(directory / "deus.sqlite3", relative_path="deus.sqlite3") != manifest["database"]:
        raise BackupError("Veritabanının SHA-256 veya boyut denetimi başarısız.")
    objects, counts = _inspect_database(directory / "deus.sqlite3")
    if objects != manifest["objects"] or counts != manifest["counts"]:
        raise BackupError("Manifest veritabanının gerçek başvuruları veya kayıt sayılarıyla uyuşmuyor.")
    expected_names = {record["sha256"] for record in objects}
    if {path.name for path in (directory / "objects").iterdir()} != expected_names:
        raise BackupError("Yedek nesne dizini eksik veya fazladan dosya içeriyor.")
    for record in objects:
        if file_record(directory / record["path"], relative_path=record["path"], maximum=MAX_FILE_BYTES) != record:
            raise BackupError("Yedek nesnesinin SHA-256 veya boyut denetimi başarısız.")
    return manifest


@_operation
def create_backup(state_dir, destination_dir):
    """Publish a verified directory backup to a new private Git-external path."""
    source = _directory(state_dir)
    database = _regular_path(source / "deus.sqlite3")
    _directory(source / "objects")
    target = _destination(source, destination_dir)
    with new_private_directory(target) as staging:
        snapshot = staging / "deus.sqlite3"
        _snapshot_database(database, snapshot)
        objects, counts = _inspect_database(snapshot)
        (staging / "objects").mkdir(mode=0o700)
        for record in objects:
            copy_verified_file(source / record["path"], staging / record["path"], record, maximum=MAX_FILE_BYTES)
        manifest = {
            "format": "ortak-kopru-backup", "format_version": FORMAT_VERSION,
            "schema_version": SCHEMA_VERSION, "classification": "private",
            "integrity": "sha256_not_authentication",
            "created_at": datetime.now(timezone.utc).isoformat(timespec="microseconds"),
            "database": file_record(snapshot, relative_path="deus.sqlite3"),
            "objects": objects, "counts": counts,
        }
        data = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False) + "\n").encode("utf-8")
        if len(data) > MAX_MANIFEST_BYTES:
            raise BackupError("Yedek manifesti 16 MiB sınırını aşıyor.")
        write_private_file(staging / "manifest.json", data)
        write_private_file(staging / "manifest.sha256", (hashlib.sha256(data).hexdigest() + "\n").encode("ascii"))
        _verify_directory(staging)
    return manifest


@_operation
def verify_backup(backup_dir):
    """Read-only verification of manifest, SQLite structure and every object."""
    return _verify_directory(_directory(backup_dir))


@_operation
def restore_backup(backup_dir, destination_dir):
    """Restore verified state to a new directory, never over existing data.

    The resulting directory contains only deus.sqlite3 and objects/. Backup
    manifests are not left beside the subsequently mutable live database.
    """
    source = _directory(backup_dir)
    target = _destination(source, destination_dir)
    manifest = _verify_directory(source)
    with new_private_directory(target) as staging:
        copy_verified_file(source / "deus.sqlite3", staging / "deus.sqlite3", manifest["database"])
        (staging / "objects").mkdir(mode=0o700)
        for record in manifest["objects"]:
            copy_verified_file(source / record["path"], staging / record["path"], record, maximum=MAX_FILE_BYTES)
        objects, counts = _inspect_database(staging / "deus.sqlite3")
        if objects != manifest["objects"] or counts != manifest["counts"]:
            raise BackupError("Geri yüklenen kayıtlar yedek manifestiyle uyuşmuyor.")
    return manifest
