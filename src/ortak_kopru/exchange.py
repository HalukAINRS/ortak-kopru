"""Selected file transfers, independent of tasks, sessions and the NT runtime.

Package manifests describe only selected bytes and portable destination paths.
Purpose, original paths, provenance and transport receipts remain in this
private ledger. Nothing here sends, executes or applies the selected content.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import stat
import unicodedata
import uuid

from .core import CoreError
from .local_files import (
    copy_verified_file, new_private_directory, private_path,
    read_regular_file, write_private_file,
)

SCHEMA_VERSION = 1
MAX_FILES = 64
MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
MAX_METADATA_BYTES = 1024 * 1024
STATES = frozenset({"prepared", "received", "planned", "sending", "unknown",
                    "published", "conflict", "failed"})
_ID = re.compile(r"x_[0-9a-f]{32}\Z")
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_DEVICE = re.compile(r"(?:CON|PRN|AUX|NUL|CLOCK\$|CONIN\$|CONOUT\$|COM[1-9¹²³]|LPT[1-9¹²³])(?:\..*)?\Z", re.I)
_COLUMNS = {
    "metadata": ("key", "value"),
    "transfers": ("id", "request_key", "fingerprint", "record"),
    "events": ("seq", "transfer_id", "kind", "at", "data"),
}


class ExchangeError(CoreError):
    """Invalid transfer, unsupported ledger or damaged immutable package."""


class ExchangeConflict(ExchangeError):
    """A repeated intent, concurrent operation or state no longer matches."""


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _text(value, name, maximum=4096):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ExchangeError(f"{name}: boş olmayan, en fazla {maximum} karakterlik metin gerekli.")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ExchangeError(f"{name}: geçerli Unicode metni gerekli.") from exc
    return value


def _json(value):
    try:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False)
        encoded = text.encode("utf-8")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise ExchangeError("Aktarım bilgisi geçerli JSON olmalı.") from exc
    if len(encoded) > MAX_METADATA_BYTES:
        raise ExchangeError("Aktarım bilgisi boyut sınırını aşıyor.")
    return text


def _decode(value):
    def pairs(items):
        result = {}
        for key, item in items:
            if key in result:
                raise ExchangeError("Aktarım JSON'unda yinelenen alan var.")
            result[key] = item
        return result

    def constant(_):
        raise ExchangeError("Aktarım JSON'unda sonlu olmayan sayı var.")

    try:
        return json.loads(value, object_pairs_hook=pairs, parse_constant=constant)
    except (UnicodeError, ValueError, TypeError) as exc:
        if isinstance(exc, ExchangeError):
            raise
        raise ExchangeError("Aktarım JSON'u okunamadı.") from exc


def _object(value, name):
    if not isinstance(value, dict):
        raise ExchangeError(f"{name} bir JSON nesnesi olmalı.")
    return _decode(_json(value))


def validate_path(value):
    """Return a portable NFC relative file path; never interpret local paths."""
    value = unicodedata.normalize("NFC", _text(value, "path", 1024))
    if any(ord(char) < 32 or ord(char) == 127 or char in '\\:<>"|?*' for char in value):
        raise ExchangeError("Aktarım dosyası yolu taşınabilir göreli yol olmalı.")
    for part in value.split("/"):
        if (not part or part in {".", ".."} or part.casefold() == ".git"
                or part != part.rstrip(" .") or len(part.encode("utf-8")) > 255
                or _DEVICE.fullmatch(part)):
            raise ExchangeError("Aktarım dosyası yolu geçersiz veya ayrılmış bir ad içeriyor.")
    return value


def _paths(values):
    if not isinstance(values, list) or not 1 <= len(values) <= MAX_FILES:
        raise ExchangeError(f"Aktarım 1–{MAX_FILES} dosya içermeli.")
    files, components = set(), {}
    paths = []
    for value in values:
        path = validate_path(value)
        folded = path.casefold()
        if folded in files:
            raise ExchangeError("Aktarımda çakışan dosya yolları var.")
        parts = path.split("/")
        for end in range(1, len(parts) + 1):
            prefix = "/".join(parts[:end])
            key = prefix.casefold()
            if key in components and components[key] != prefix:
                raise ExchangeError("Aktarımda büyük/küçük harfle çakışan dizin veya dosya var.")
            components[key] = prefix
        files.add(folded)
        paths.append(path)
    for path in files:
        parts = path.split("/")
        if any("/".join(parts[:end]) in files for end in range(1, len(parts))):
            raise ExchangeError("Bir aktarım yolu hem dosya hem dizin olamaz.")
    return paths


def _identifier(value):
    if not isinstance(value, str) or not _ID.fullmatch(value):
        raise ExchangeError("Aktarım kimliği geçersiz.")
    return value


def _regular(path):
    info = path.lstat()
    if (not stat.S_ISREG(info.st_mode)
            or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
        raise ExchangeError("Aktarım alanındaki dosya bir bağlantı veya düzenli olmayan dosya.")


def _manifest(value):
    if (not isinstance(value, dict) or set(value) != {"schema_version", "kind", "files"}
            or type(value["schema_version"]) is not int or value["schema_version"] != SCHEMA_VERSION
            or value["kind"] != "ortak_kopru_exchange"):
        raise ExchangeError("Aktarım manifestosu desteklenmiyor.")
    files = value["files"]
    if not isinstance(files, list) or any(not isinstance(item, dict) for item in files):
        raise ExchangeError("Aktarım dosya listesi geçersiz.")
    paths = _paths([item.get("path") for item in files])
    objects, total = {}, 0
    for path, item in zip(paths, files):
        if (set(item) != {"path", "bytes", "sha256", "object"} or item["path"] != path
                or type(item["bytes"]) is not int or not 0 <= item["bytes"] <= MAX_FILE_BYTES
                or not isinstance(item["sha256"], str) or not _DIGEST.fullmatch(item["sha256"])
                or item["object"] != "objects/" + item["sha256"]):
            raise ExchangeError("Aktarım dosya kaydı geçersiz.")
        if objects.setdefault(item["sha256"], item["bytes"]) != item["bytes"]:
            raise ExchangeError("Aynı içerik karmasının dosya boyutları uyuşmuyor.")
        total += item["bytes"]
    if total > MAX_TOTAL_BYTES:
        raise ExchangeError("Aktarımın toplam dosya boyutu sınırı aşıldı.")
    return value


class ExchangeStore:
    """Private durable transfers with immutable packages and short DB writes."""

    def __init__(self, directory, *, create=True):
        self.directory = private_path(directory)
        if any((parent / "deus.sqlite3").exists()
               for parent in (self.directory, *self.directory.parents)):
            raise ExchangeError("Aktarım alanı mevcut görev veri alanından ayrı olmalı.")
        self.path = self.directory / "exchange.sqlite3"
        self.packages = self.directory / "packages"
        self.locks = self.directory / "locks"
        if not create and not self.path.exists():
            raise ExchangeError("Aktarım alanı bulunamadı; boş alan oluşturulmadı.")
        if create:
            self.directory.mkdir(mode=0o700, parents=True, exist_ok=True)
            for path in (self.packages, self.locks):
                private_path(path).mkdir(mode=0o700, exist_ok=True)
            try:
                descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            except FileExistsError:
                pass
            else:
                os.close(descriptor)
            # Do not unlink a database after an initialization exception:
            # commit may have succeeded before the exception was delivered,
            # and another initializer may already have opened this file.
            with self._db(write=True) as db:
                tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
                if not tables:
                    # create=True may initialize an empty database left by
                    # an interrupted initializer. BEGIN IMMEDIATE also
                    # serializes concurrent first-use constructors.
                    db.execute("CREATE TABLE metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL)")
                    db.execute("CREATE TABLE transfers(id TEXT PRIMARY KEY, request_key TEXT NOT NULL UNIQUE, fingerprint TEXT NOT NULL, record TEXT NOT NULL)")
                    db.execute("CREATE TABLE events(seq INTEGER PRIMARY KEY, transfer_id TEXT NOT NULL REFERENCES transfers(id), kind TEXT NOT NULL, at TEXT NOT NULL, data TEXT NOT NULL)")
                    db.execute("INSERT INTO metadata VALUES('schema_version', ?)", (str(SCHEMA_VERSION),))
                    db.execute("INSERT INTO metadata VALUES('kind', 'ortak_kopru_exchange')")
                self._check_schema(db)
        else:
            with self._db() as db:
                self._check_schema(db)
        for path in (self.packages, self.locks):
            if not private_path(path).is_dir():
                raise ExchangeError("Aktarım alanının gerekli dizini eksik.")

    @contextmanager
    def _db(self, *, write=False):
        db = None
        try:
            private_path(self.path)
            _regular(self.path)
            db = sqlite3.connect(self.path.as_uri() + "?mode=rw", uri=True, timeout=10)
            db.execute("PRAGMA foreign_keys=ON")
            db.execute("PRAGMA trusted_schema=OFF")
            db.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            yield db
            db.commit()
        except sqlite3.Error as exc:
            if db is not None:
                db.rollback()
            raise ExchangeError("Aktarım veritabanı işlemi tamamlanamadı.") from exc
        except BaseException:
            if db is not None:
                db.rollback()
            raise
        finally:
            if db is not None:
                db.close()

    @staticmethod
    def _check_schema(db):
        tables = {row[0] for row in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if tables != set(_COLUMNS):
            raise ExchangeError("Desteklenmeyen aktarım veritabanı şeması.")
        if db.execute("SELECT 1 FROM sqlite_master WHERE type IN ('view','trigger') LIMIT 1").fetchone():
            raise ExchangeError("Aktarım veritabanında desteklenmeyen görünüm veya tetikleyici var.")
        for table, columns in _COLUMNS.items():
            if tuple(row[1] for row in db.execute(f'PRAGMA table_info("{table}")')) != columns:
                raise ExchangeError("Desteklenmeyen aktarım veritabanı alanları.")
        if dict(db.execute("SELECT key, value FROM metadata")) != {
                "schema_version": str(SCHEMA_VERSION), "kind": "ortak_kopru_exchange"}:
            raise ExchangeError("Desteklenmeyen aktarım veritabanı sürümü.")

    def _get(self, db, transfer_id):
        row = db.execute("SELECT record FROM transfers WHERE id=?", (_identifier(transfer_id),)).fetchone()
        if row is None:
            raise ExchangeError("Aktarım bulunamadı.")
        record = _decode(row[0])
        if (not isinstance(record, dict) or record.get("id") != transfer_id
                or not isinstance(record.get("state"), str) or record["state"] not in STATES
                or not isinstance(record.get("direction"), str)
                or record["direction"] not in {"inbound", "outbound"}):
            raise ExchangeError("Aktarım kaydı geçersiz.")
        _manifest(record.get("manifest"))
        return record

    @staticmethod
    def _event(db, record, kind, data):
        db.execute("INSERT INTO events(transfer_id,kind,at,data) VALUES(?,?,?,?)",
                   (record["id"], kind, _now(), _json(data)))

    def _create(self, files, *, direction, endpoint, purpose, request_key, sources):
        purpose = _text(purpose, "purpose")
        request_key = _text(request_key, "request_key", 256)
        endpoint = _object(endpoint, "target" if direction == "outbound" else "origin")
        paths = _paths([item["path"] for item in files])
        entries, objects, total = [], {}, 0
        for path, item in zip(paths, files):
            data = item["data"]
            if not isinstance(data, bytes) or len(data) > MAX_FILE_BYTES:
                raise ExchangeError("Aktarım dosyası bytes olmalı ve boyut sınırını aşmamalı.")
            total += len(data)
            if total > MAX_TOTAL_BYTES:
                raise ExchangeError("Aktarımın toplam dosya boyutu sınırı aşıldı.")
            digest = hashlib.sha256(data).hexdigest()
            entries.append({"path": path, "bytes": len(data), "sha256": digest,
                            "object": "objects/" + digest})
            objects[digest] = data
        entries.sort(key=lambda item: item["path"])
        manifest = _manifest({"schema_version": SCHEMA_VERSION,
                              "kind": "ortak_kopru_exchange", "files": entries})
        sources = _object(sources, "sources")
        fingerprint = hashlib.sha256(_json({"direction": direction, "endpoint": endpoint,
                                           "purpose": purpose, "manifest": manifest,
                                           "sources": sources}).encode("utf-8")).hexdigest()
        transfer_id = "x_" + uuid.uuid4().hex
        package = self.packages / transfer_id
        published = False
        try:
            with self._db(write=True) as db:
                previous = db.execute("SELECT id,fingerprint FROM transfers WHERE request_key=?", (request_key,)).fetchone()
                if previous:
                    if previous[1] != fingerprint:
                        raise ExchangeConflict("İstek anahtarı başka aktarım içeriği veya kapsamıyla kullanılmış.")
                    return self.verify(previous[0])
                # Only local bounded writes run inside this transaction. All
                # network operations use operation(), never an open DB write.
                with new_private_directory(package) as staging:
                    (staging / "objects").mkdir(mode=0o700)
                    for digest, data in objects.items():
                        write_private_file(staging / "objects" / digest, data)
                    write_private_file(staging / "manifest.json", (_json(manifest) + "\n").encode("utf-8"))
                published = True
                now = _now()
                record = {"id": transfer_id, "direction": direction,
                          "state": "prepared" if direction == "outbound" else "received",
                          "purpose": purpose, "request_key": request_key,
                          "created_at": now, "updated_at": now,
                          "target": endpoint if direction == "outbound" else None,
                          "origin": endpoint if direction == "inbound" else None,
                          "manifest": manifest, "source_paths": sources,
                          "plan": None, "checkpoint": None, "receipt": None, "error": None}
                db.execute("INSERT INTO transfers VALUES(?,?,?,?)",
                           (transfer_id, request_key, fingerprint, _json(record)))
                self._event(db, record, record["state"], {"files": len(entries)})
            return record
        except BaseException:
            if published:
                # An interrupt can arrive after commit but before returning
                # its result. Remove bytes only when the ledger positively
                # confirms no durable record refers to them. An unreadable
                # outcome leaves a private orphan rather than broken history.
                try:
                    with self._db() as db:
                        committed = db.execute("SELECT 1 FROM transfers WHERE id=?", (transfer_id,)).fetchone() is not None
                except Exception:
                    committed = True
                if not committed:
                    shutil.rmtree(package)
            raise

    def prepare_outbound(self, selections, target, purpose, request_key):
        if not isinstance(selections, list) or any(not isinstance(item, dict) or set(item) != {"source", "path"} for item in selections):
            raise ExchangeError("Seçim listesi source/path nesneleri içermeli.")
        paths = _paths([item["path"] for item in selections])
        files, sources, total = [], {}, 0
        for path, item in zip(paths, selections):
            if not isinstance(item["source"], (str, os.PathLike)):
                raise ExchangeError("Seçilen kaynak geçerli bir dosya yolu olmalı.")
            source = Path(_text(os.fspath(item["source"]), "source", 32768)).expanduser().absolute()
            # Unlike private_path(), selected project files may be in Git.
            # Check every existing component before resolving the source.
            for candidate in (source, *source.parents):
                info = candidate.lstat()
                if (stat.S_ISLNK(info.st_mode)
                        or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
                    raise ExchangeError("Seçilen dosya yolu bağlantı içeremez.")
            data = read_regular_file(source, maximum=MAX_FILE_BYTES)
            total += len(data)
            if total > MAX_TOTAL_BYTES:
                raise ExchangeError("Aktarımın toplam dosya boyutu sınırı aşıldı.")
            files.append({"path": path, "data": data})
            sources[path] = str(source.resolve())
        return self._create(files, direction="outbound", endpoint=target,
                            purpose=purpose, request_key=request_key, sources=sources)

    def record_inbound(self, files, origin, purpose, request_key):
        if not isinstance(files, list) or any(not isinstance(item, dict) or set(item) != {"path", "data", "source"} for item in files):
            raise ExchangeError("Gelen dosyalar path/data/source alanlarını taşımalı.")
        paths = _paths([item["path"] for item in files])
        sources = {path: _object(item["source"], "source") for path, item in zip(paths, files)}
        return self._create(files, direction="inbound", endpoint=origin,
                            purpose=purpose, request_key=request_key, sources=sources)

    def get(self, transfer_id):
        with self._db() as db:
            return self._get(db, transfer_id)

    def list_transfers(self):
        with self._db() as db:
            identities = [row[0] for row in db.execute("SELECT id FROM transfers ORDER BY rowid")]
            return [self._get(db, identity) for identity in identities]

    def events(self, transfer_id):
        with self._db() as db:
            self._get(db, transfer_id)
            return [{"seq": row[0], "kind": row[1], "at": row[2], "data": _decode(row[3])}
                    for row in db.execute("SELECT seq,kind,at,data FROM events WHERE transfer_id=? ORDER BY seq", (transfer_id,))]

    def update(self, transfer_id, *, expected_states, state, **changes):
        if (not isinstance(expected_states, (list, tuple, set, frozenset)) or not expected_states
                or any(value not in STATES for value in expected_states) or state not in STATES):
            raise ExchangeError("Aktarımın beklenen veya yeni durumu geçersiz.")
        if set(changes) - {"plan", "checkpoint", "receipt", "error"}:
            raise ExchangeError("Aktarımın sabit alanları değiştirilemez.")
        normalized = {key: None if value is None else _object(value, key) for key, value in changes.items()}
        with self._db(write=True) as db:
            record = self._get(db, transfer_id)
            if record["state"] not in expected_states:
                raise ExchangeConflict("Aktarımın durumu değişti; güncel kayıt yeniden okunmalı.")
            previous = record["state"]
            record.update(normalized, state=state, updated_at=_now())
            db.execute("UPDATE transfers SET record=? WHERE id=?", (_json(record), transfer_id))
            self._event(db, record, "updated", {"from": previous, "to": state, "fields": sorted(changes)})
            return record

    def read_object(self, transfer_id, sha256):
        record = self.get(transfer_id)
        item = next((item for item in record["manifest"]["files"] if item["sha256"] == sha256), None)
        if item is None:
            raise ExchangeError("İstenen nesne bu aktarımda bulunmuyor.")
        path = private_path(self.packages / transfer_id / item["object"])
        data = read_regular_file(path, maximum=MAX_FILE_BYTES)
        if len(data) != item["bytes"] or hashlib.sha256(data).hexdigest() != sha256:
            raise ExchangeError("Aktarım nesnesinin boyut veya SHA-256 denetimi başarısız.")
        return data

    def verify(self, transfer_id):
        record = self.get(transfer_id)
        package = private_path(self.packages / transfer_id)
        if not package.is_dir() or {path.name for path in package.iterdir()} != {"manifest.json", "objects"}:
            raise ExchangeError("Aktarım paketinin dosya kümesi eksik veya fazla.")
        manifest = _manifest(_decode(read_regular_file(package / "manifest.json", maximum=MAX_METADATA_BYTES)))
        if manifest != record["manifest"]:
            raise ExchangeError("Paket manifestosu özel aktarım kaydıyla uyuşmuyor.")
        objects = private_path(package / "objects")
        expected = {item["sha256"] for item in manifest["files"]}
        if not objects.is_dir() or {path.name for path in objects.iterdir()} != expected:
            raise ExchangeError("Aktarım nesne listesi eksik veya fazla.")
        for digest in expected:
            self.read_object(transfer_id, digest)
        return record

    def materialize(self, transfer_id, destination):
        record = self.verify(transfer_id)
        target = private_path(destination)
        if target.is_relative_to(self.directory):
            raise ExchangeError("Dosya çıkarma hedefi aktarım veri alanının dışında olmalı.")
        with new_private_directory(target) as staging:
            for item in record["manifest"]["files"]:
                output = staging / item["path"]
                current = staging
                for component in item["path"].split("/")[:-1]:
                    current /= component
                    current.mkdir(mode=0o700, exist_ok=True)
                copy_verified_file(self.packages / transfer_id / item["object"], output,
                                   item, maximum=MAX_FILE_BYTES)
        with self._db(write=True) as db:
            self._event(db, record, "materialized", {"output_path": str(target)})
        return {"id": transfer_id, "output_path": str(target),
                "files": [{key: item[key] for key in ("path", "bytes", "sha256")}
                          for item in record["manifest"]["files"]]}

    @contextmanager
    def operation(self, transfer_id):
        """Exclusive nonblocking OS lock, released even if the process crashes."""
        self.get(transfer_id)
        lock = private_path(self.locks / (_identifier(transfer_id) + ".lock"))
        descriptor, locked = None, False
        try:
            flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
            descriptor = os.open(lock, flags, 0o600)
            _regular(lock)
            if not os.path.samestat(lock.stat(), os.fstat(descriptor)):
                raise ExchangeError("Aktarım kilit dosyası açılırken değişti.")
            if os.fstat(descriptor).st_size == 0:
                os.write(descriptor, b"\0")
                os.fsync(descriptor)
            try:
                if os.name == "nt":
                    import msvcrt
                    os.lseek(descriptor, 0, os.SEEK_SET)
                    msvcrt.locking(descriptor, msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                raise ExchangeConflict("Bu aktarım için başka bir işlem sürüyor.") from exc
            locked = True
            yield
        finally:
            if descriptor is not None:
                try:
                    if locked:
                        if os.name == "nt":
                            import msvcrt
                            os.lseek(descriptor, 0, os.SEEK_SET)
                            msvcrt.locking(descriptor, msvcrt.LK_UNLCK, 1)
                        else:
                            import fcntl
                            fcntl.flock(descriptor, fcntl.LOCK_UN)
                finally:
                    os.close(descriptor)
