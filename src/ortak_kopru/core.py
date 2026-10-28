"""Persistent task state separate from the historical HTML correspondence.

Only the standard library is used. The owner of the private state directory is
trusted to declare a current user instruction and to submit verification
receipts. These declarations are not independent identity or truth proofs.
The core never runs source text, models, tools, network calls or old bridge jobs.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile
import uuid

SCHEMA_VERSION = 1
MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_CONTEXT_TEXT_BYTES = 2 * 1024 * 1024
MAX_REFERENCES = 64
JOINT_STAGES = (16, 32, 64, 128)
MAX_JOINT_RECEIPT_BYTES = 1024 * 1024
TASK_STATES = ("ready", "running", "paused", "awaiting_verification", "blocked", "completed", "cancelled")


class CoreError(ValueError):
    """Invalid request or unsupported state."""


class Conflict(CoreError):
    """The supplied request conflicts with a recorded request or current state."""


class NotFound(CoreError):
    """The referenced object does not exist."""


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _json(value):
    try:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError) as exc:
        raise CoreError("İstek JSON olarak kaydedilebilir olmalı.") from exc


def _text(value, name, maximum=200000):
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise CoreError(f"{name}: boş olmayan, en fazla {maximum} karakterlik metin gerekli.")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise CoreError(f"{name}: geçerli Unicode metni gerekli.") from exc
    return value  # Preserve the original words, including whitespace.


def _revision(value):
    if type(value) is not int or value < 1:
        raise CoreError("expected_revision pozitif tam sayı olmalı.")
    return value


def _joint_stage(value):
    if type(value) is not int or value not in JOINT_STAGES:
        raise CoreError("stage yalnız 16, 32, 64 veya 128 olmalı.")
    return value


def _authority(value):
    if not isinstance(value, dict):
        raise CoreError("authority bir nesne olmalı.")
    if value.get("kind", "direct_user") != "direct_user":
        raise CoreError("Tarihsel alıntı veya katman çıktısı görev yetkisi olamaz.")
    result = {key: _text(value.get(key), f"authority.{key}") for key in ("actor", "source", "scope")}
    result.update(kind="direct_user", verification="local_owner_declaration")
    return result


def _criteria(values):
    if not isinstance(values, list) or not 1 <= len(values) <= 100:
        raise CoreError("criteria, 1–100 kabul ölçütü içeren liste olmalı.")
    result, seen = [], set()
    for index, value in enumerate(values, 1):
        if isinstance(value, str):
            value = {"id": f"criterion-{index}", "description": value}
        if not isinstance(value, dict):
            raise CoreError("Kabul ölçütü metin veya id/description nesnesi olmalı.")
        identity = _text(value.get("id"), "criterion.id", 80)
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:-]*", identity) or identity in seen:
            raise CoreError("Kabul ölçütü kimlikleri geçerli ve benzersiz olmalı.")
        seen.add(identity)
        result.append({"id": identity, "description": _text(value.get("description"), "criterion.description")})
    return result


def _references(values):
    if values is None:
        return []
    if not isinstance(values, list) or len(values) > MAX_REFERENCES:
        raise CoreError(f"En fazla {MAX_REFERENCES} yerel dosya başvurusu verilebilir.")
    result = []
    for value in values:
        if isinstance(value, (str, os.PathLike)):
            value = {"path": os.fspath(value)}
        if not isinstance(value, dict):
            raise CoreError("Dosya başvurusu path alanı taşımalı.")
        path = str(Path(_text(value.get("path"), "path", 32768)).expanduser().resolve())
        role = value.get("role", "evidence")
        if role not in ("evidence", "reference"):
            raise CoreError("Kaynak rolü evidence veya reference olmalı; kaynaklar talimat değildir.")
        note = value.get("note", "")
        if not isinstance(note, str) or len(note) > 200000:
            raise CoreError("Kaynak notu geçersiz.")
        if note:
            _text(note, "note")
        result.append({"path": path, "role": role, "note": note})
    return result


class Store:
    """One local SQLite owner; remote clients use the broker, not a shared DB file."""

    def __init__(self, state_dir):
        self.directory = Path(state_dir).expanduser().resolve()
        for parent in (self.directory, *self.directory.parents):
            marker = parent / ".git"
            if marker.is_file() or (marker / "HEAD").is_file():
                raise CoreError("Özel çalışma dizini bir Git çalışma ağacının içinde olamaz.")
        self.directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.objects = self.directory / "objects"
        self.objects.mkdir(exist_ok=True, mode=0o700)
        self.path = self.directory / "deus.sqlite3"
        with self._db(write=True) as db:
            # Reject foreign/future state before issuing any schema mutation.
            existing = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            if existing:
                if "metadata" not in existing:
                    raise CoreError("Bu dosya DEUS çalışma veritabanı değil.")
                version = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
                if version is None or version[0] != str(SCHEMA_VERSION):
                    raise CoreError("Desteklenmeyen çalışma veritabanı sürümü.")
            schema = """
                CREATE TABLE IF NOT EXISTS metadata(key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS tasks(
                    id TEXT PRIMARY KEY, original_words TEXT NOT NULL,
                    authority TEXT NOT NULL, criteria TEXT NOT NULL,
                    revision INTEGER NOT NULL, status TEXT NOT NULL,
                    active_attempt_id TEXT, current_result_id TEXT,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS revisions(
                    task_id TEXT NOT NULL REFERENCES tasks(id), revision INTEGER NOT NULL,
                    original_words TEXT NOT NULL, created_at TEXT NOT NULL,
                    PRIMARY KEY(task_id,revision));
                CREATE TABLE IF NOT EXISTS sources(
                    task_id TEXT NOT NULL REFERENCES tasks(id), source_id TEXT NOT NULL,
                    position INTEGER NOT NULL, data TEXT NOT NULL,
                    PRIMARY KEY(task_id,source_id));
                CREATE TABLE IF NOT EXISTS attempts(
                    id TEXT PRIMARY KEY, task_id TEXT NOT NULL REFERENCES tasks(id),
                    revision INTEGER NOT NULL, participant TEXT NOT NULL, session_id TEXT NOT NULL,
                    status TEXT NOT NULL, delivery_status TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS results(
                    id TEXT PRIMARY KEY, task_id TEXT NOT NULL REFERENCES tasks(id),
                    attempt_id TEXT NOT NULL REFERENCES attempts(id), revision INTEGER NOT NULL,
                    summary TEXT NOT NULL, artifacts TEXT NOT NULL, created_at TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS checks(
                    task_id TEXT NOT NULL REFERENCES tasks(id), result_id TEXT NOT NULL REFERENCES results(id),
                    criterion_id TEXT NOT NULL, passed INTEGER NOT NULL, evidence TEXT NOT NULL,
                    verifier TEXT NOT NULL, at TEXT NOT NULL,
                    PRIMARY KEY(task_id,result_id,criterion_id));
                CREATE TABLE IF NOT EXISTS events(
                    seq INTEGER PRIMARY KEY AUTOINCREMENT, id TEXT NOT NULL UNIQUE,
                    task_id TEXT NOT NULL REFERENCES tasks(id), revision INTEGER NOT NULL,
                    kind TEXT NOT NULL, at TEXT NOT NULL, data TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS requests(
                    request_key TEXT PRIMARY KEY, operation TEXT NOT NULL,
                    payload_sha256 TEXT NOT NULL, response TEXT NOT NULL);
            """
            # execute each DDL statement inside the existing transaction:
            # executescript would commit early and expose a half-created schema.
            for statement in schema.split(";"):
                if statement.strip():
                    db.execute(statement)
            current = db.execute("SELECT value FROM metadata WHERE key='schema_version'").fetchone()
            if current is not None and current[0] != str(SCHEMA_VERSION):
                raise CoreError("Desteklenmeyen çalışma veritabanı sürümü.")
            db.execute("INSERT OR IGNORE INTO metadata VALUES('schema_version',?)", (str(SCHEMA_VERSION),))
        if os.name != "nt":
            self.path.chmod(0o600)

    @contextmanager
    def _db(self, write=False):
        db = sqlite3.connect(self.path, timeout=30)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        db.execute("PRAGMA busy_timeout=30000")
        try:
            db.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            with db:
                yield db
        finally:
            db.close()

    def _write(self, operation, request_key, payload, action, replay_action=None):
        key = _text(request_key, "request_key", 256)
        digest = hashlib.sha256(_json(payload).encode("utf-8")).hexdigest()
        with self._db(write=True) as db:
            previous = db.execute("SELECT * FROM requests WHERE request_key=?", (key,)).fetchone()
            if previous:
                if previous["operation"] != operation or previous["payload_sha256"] != digest:
                    raise Conflict("Aynı istek anahtarı farklı işlem veya içerikle kullanılmış.")
                # Work delivery cannot replay obsolete eligibility or context.
                # Historical mutation receipts remain stable for other operations.
                if replay_action is not None:
                    return replay_action(db)
                return json.loads(previous["response"])
            result = action(db)
            db.execute("INSERT INTO requests VALUES(?,?,?,?)", (key, operation, digest, _json(result)))
            return result

    def _row(self, db, task_id, expected_revision=None):
        task_id = _text(task_id, "task_id", 80)
        row = db.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        if row is None:
            raise NotFound("İş bulunamadı.")
        if expected_revision is not None and row["revision"] != expected_revision:
            raise Conflict("İş sürümü değişti; güncel işi oku.")
        return row

    def _event(self, db, task_id, revision, kind, data):
        identity, at = uuid.uuid4().hex, _now()
        db.execute("INSERT INTO events(id,task_id,revision,kind,at,data) VALUES(?,?,?,?,?,?)",
                   (identity, task_id, revision, kind, at, _json(data)))
        return {"id": identity, "at": at, "revision": revision, "data": data}

    def _invalidate(self, db, task, reason):
        if task["active_attempt_id"]:
            db.execute("UPDATE attempts SET status=?,updated_at=? WHERE id=?",
                       (reason, _now(), task["active_attempt_id"]))
        db.execute("UPDATE tasks SET active_attempt_id=NULL,current_result_id=NULL WHERE id=?", (task["id"],))

    def _snapshot(self, reference):
        path = Path(reference["path"])
        try:
            if not path.is_file():
                raise CoreError("Kaynak veya çıktı düzenli bir dosya olmalı.")
            with path.open("rb") as stream:
                data = stream.read(MAX_FILE_BYTES + 1)
        except OSError as exc:
            raise CoreError(f"Dosya okunamadı: {path.name}") from exc
        if len(data) > MAX_FILE_BYTES:
            raise CoreError(f"Dosya sınırı {MAX_FILE_BYTES} bayt; kaynağı açık parçalarla ver.")
        return self._snapshot_bytes(reference, data)

    def _snapshot_bytes(self, reference, data):
        """Capture already obtained bytes; callers hold the short DB write lock."""
        if not isinstance(data, bytes) or len(data) > MAX_FILE_BYTES:
            raise CoreError("Kaynak baytları dosya boyut sınırı içinde olmalı.")
        digest = hashlib.sha256(data).hexdigest()
        target = self.objects / digest
        # All snapshot writers hold this Store's BEGIN IMMEDIATE transaction.
        # Publish only complete, flushed bytes. A failed write must not poison the
        # permanent digest path and prevent a later retry of the same request.
        temporary = None
        try:
            if target.exists():
                if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                    raise Conflict("Özel kaynak görüntüsünün bütünlüğü bozuk.")
            else:
                fd, name = tempfile.mkstemp(prefix=".snapshot-", dir=self.objects)
                temporary = Path(name)
                with os.fdopen(fd, "wb") as stream:
                    stream.write(data)
                    stream.flush()
                    os.fsync(stream.fileno())
                # A completed committed object is never overwritten. The DB write
                # lock serializes cooperating Store instances across processes.
                if target.exists():
                    if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                        raise Conflict("Özel kaynak görüntüsünün bütünlüğü bozuk.")
                else:
                    os.replace(temporary, target)
        except OSError as exc:
            raise CoreError("Özel kaynak görüntüsü kalıcı olarak yazılamadı.") from exc
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        source_id = hashlib.sha256(_json({**reference, "sha256": digest}).encode("utf-8")).hexdigest()
        return {**reference, "id": source_id, "kind": "local_file", "bytes": len(data),
                "sha256": digest, "snapshot": f"objects/{digest}", "observed_at": _now(),
                "observation": "file_bytes_captured", "instruction_authority": False}

    def _task(self, db, task_id):
        task = dict(self._row(db, task_id))
        task["schema_version"] = SCHEMA_VERSION
        task["authority"] = json.loads(task["authority"])
        task["criteria"] = json.loads(task["criteria"])
        task["revisions"] = [dict(r) for r in db.execute("SELECT revision,original_words,created_at FROM revisions WHERE task_id=? ORDER BY revision", (task_id,))]
        task["current_words"] = task["revisions"][-1]["original_words"]
        task["sources"] = [json.loads(r[0]) for r in db.execute("SELECT data FROM sources WHERE task_id=? ORDER BY position", (task_id,))]
        task["attempts"] = [dict(r) for r in db.execute("SELECT * FROM attempts WHERE task_id=? ORDER BY created_at,id", (task_id,))]
        task["results"] = []
        for row in db.execute("SELECT * FROM results WHERE task_id=? ORDER BY created_at,id", (task_id,)):
            result = dict(row)
            result["artifacts"] = json.loads(result["artifacts"])
            task["results"].append(result)
        task["verification"] = []
        if task["current_result_id"]:
            for row in db.execute("SELECT * FROM checks WHERE task_id=? AND result_id=? ORDER BY criterion_id", (task_id, task["current_result_id"])):
                check = dict(row)
                check["passed"] = bool(check["passed"])
                check["verification"] = "submitted_receipt"
                task["verification"].append(check)
        task["identity_verified"] = False
        return task

    def get_task(self, task_id):
        with self._db() as db:
            return self._task(db, task_id)

    def list_tasks(self):
        with self._db() as db:
            return [self._task(db, row[0]) for row in db.execute("SELECT id FROM tasks ORDER BY created_at DESC,id")]

    def _joint_eligible(self, db, task_id, expected_revision):
        task = self._row(db, task_id, expected_revision)
        if task["status"] in ("paused", "cancelled", "completed"):
            raise Conflict("Duraklatılmış veya kapanmış işe yeni ortak kayıt eklenemez.")
        return task

    def _joint_source(self, db, task_id, revision, record_id, category, data,
                      provenance, *, role="evidence"):
        # The stored object is a real local file. Its remote origin, when any,
        # remains metadata; it is never confused with a local repository HEAD.
        digest = hashlib.sha256(data).hexdigest()
        note = _json({"category": category, "task_id": task_id,
                      "revision": revision, "record_id": record_id,
                      "provenance": provenance})
        source = self._snapshot_bytes({"path": str(self.objects / digest),
                                       "role": role, "note": note}, data)
        source.update(task_id=task_id, revision=revision, record_id=record_id,
                      category=category, provenance=provenance)
        position = db.execute("SELECT COALESCE(MAX(position),-1)+1 FROM sources WHERE task_id=?",
                              (task_id,)).fetchone()[0]
        db.execute("INSERT INTO sources VALUES(?,?,?,?)",
                   (task_id, source["id"], position, _json(source)))
        return source

    def record_contribution(self, task_id, author, session_id, relayed_by, stage,
                            body, expected_revision, request_key, references=None):
        """Append a session's declared contribution without assigning an attempt."""
        revision = _revision(expected_revision)
        if references is None:
            references = []
        if not isinstance(references, list) or len(references) > MAX_REFERENCES:
            raise CoreError("Katkı en fazla 64 metin başvurusu içerebilir.")
        data = {"author": _text(author, "author", 200),
                "session_id": _text(session_id, "session_id", 256),
                "relayed_by": _text(relayed_by, "relayed_by", 200),
                "stage": _joint_stage(stage), "body": _text(body, "body"),
                "references": [_text(value, "reference", 4096) for value in references],
                "identity_verified": False, "instruction_authority": False,
                "execution_evidence": False}
        payload = {"task_id": _text(task_id, "task_id", 80),
                   "expected_revision": revision, **data}

        def action(db):
            self._joint_eligible(db, task_id, revision)
            event = self._event(db, task_id, revision, "contribution_recorded", data)
            document = {"kind": "session_contribution", "task_id": task_id,
                        **data, **{key: event[key] for key in ("id", "at", "revision")}}
            self._joint_source(db, task_id, revision, event["id"], "contribution",
                               (_json(document) + "\n").encode("utf-8"),
                               {"author": data["author"], "session_id": data["session_id"],
                                "relayed_by": data["relayed_by"]}, role="reference")
            return {"id": event["id"]}

        saved = self._write("joint_contribution", request_key, payload, action)
        return next(item for item in self.joint_view(task_id)["contributions"]
                    if item["id"] == saved["id"])

    def prepare_joint_operation(self, task_id, kind, stage, parameters,
                                expected_revision, request_key):
        """Claim once before external work; a replay never grants a second claim."""
        revision = _revision(expected_revision)
        if kind not in ("local_cli", "github_fetch") or not isinstance(parameters, dict):
            raise CoreError("Ortak işlem türü veya parametreleri geçersiz.")
        if kind == "local_cli":
            if (set(parameters) != {"operation", "cwd"} or parameters["operation"] not in
                    ("repo_revision", "repo_status", "python_version")):
                raise CoreError("Ortak yerel işlem sabit işlem listesinden seçilmeli.")
            _text(parameters["cwd"], "cwd", 32768)
        else:
            if (set(parameters) != {"repository", "ref", "paths"}
                    or not isinstance(parameters["paths"], list)
                    or not 1 <= len(parameters["paths"]) <= MAX_REFERENCES):
                raise CoreError("GitHub işlemi depo, ref ve 1–64 seçilmiş yol içermeli.")
            _text(parameters["repository"], "repository", 140)
            _text(parameters["ref"], "ref", 256)
            for path in parameters["paths"]:
                _text(path, "path", 1024)
        if len(_json(parameters).encode("utf-8")) > 256 * 1024:
            raise CoreError("Ortak işlem parametreleri boyut sınırını aşıyor.")
        payload = {"task_id": _text(task_id, "task_id", 80), "kind": kind,
                   "stage": _joint_stage(stage), "parameters": parameters,
                   "expected_revision": revision}
        claimed = False

        def action(db):
            nonlocal claimed
            self._joint_eligible(db, task_id, revision)
            event = self._event(db, task_id, revision, "operation_prepared", {
                "kind": kind, "stage": stage, "parameters": parameters,
                "identity_verified": False, "instruction_authority": False,
                "task_completion_verified": False})
            claimed = True
            return {"operation_id": event["id"]}

        saved = self._write("joint_operation", request_key, payload, action)
        return self._get_joint_operation(task_id, saved["operation_id"]), claimed

    def finish_joint_operation(self, task_id, operation_id, receipt, captures=None):
        """Persist actual return bytes at the claimed revision, even after a correction.

        This internal completion does not reauthorize work or change task/attempt
        state. No network or subprocess is allowed while this transaction is open.
        """
        if (not isinstance(receipt, dict) or receipt.get("status") not in
                ("completed", "failed", "timeout", "output_limit", "spawn_error", "unknown")):
            raise CoreError("Ortak işlem makbuzunun durumu geçersiz.")
        encoded = _json(receipt).encode("utf-8")
        if len(encoded) > MAX_JOINT_RECEIPT_BYTES:
            raise CoreError("Ortak işlem makbuzu boyut sınırını aşıyor.")
        captures = [] if captures is None else captures
        if not isinstance(captures, list) or len(captures) > MAX_REFERENCES:
            raise CoreError("İşlem en fazla 64 kaynak görüntüsü içerebilir.")
        for capture in captures:
            if (not isinstance(capture, dict) or set(capture) != {"data", "provenance"}
                    or not isinstance(capture["data"], bytes)
                    or len(capture["data"]) > MAX_FILE_BYTES
                    or not isinstance(capture["provenance"], dict)
                    or len(_json(capture["provenance"]).encode("utf-8")) > 16384):
                raise CoreError("İşlem kaynak görüntüsü geçersiz veya çok büyük.")
        if sum(len(capture["data"]) for capture in captures) > 64 * 1024 * 1024:
            raise CoreError("İşlem kaynaklarının toplam boyutu 64 MiB sınırını aşıyor.")
        with self._db(write=True) as db:
            self._row(db, task_id)
            prepared = db.execute("SELECT * FROM events WHERE id=? AND task_id=? AND kind='operation_prepared'",
                                  (_text(operation_id, "operation_id", 80), task_id)).fetchone()
            if prepared is None:
                raise NotFound("İşlem başlamadan önce hazırlanmış olmalı.")
            finished = self._joint_finished(db, task_id).get(operation_id)
            if finished is not None:
                if finished["receipt"] != receipt:
                    raise Conflict("İşlemin makbuzu daha önce farklı içerikle kaydedilmiş.")
            else:
                revision, parameters = prepared["revision"], json.loads(prepared["data"])
                document = {"task_id": task_id, "revision": revision,
                            "operation_id": operation_id, **parameters, "receipt": receipt}
                sources = [self._joint_source(
                    db, task_id, revision, operation_id, "operation_receipt",
                    (_json(document) + "\n").encode("utf-8"), {"kind": parameters["kind"]})]
                for capture in captures:
                    sources.append(self._joint_source(db, task_id, revision, operation_id,
                                                      "operation_source", capture["data"],
                                                      capture["provenance"]))
                self._event(db, task_id, revision, "operation_finished", {
                    "operation_id": operation_id, "receipt": receipt,
                    "source_ids": [source["id"] for source in sources],
                    "task_completion_verified": False})
        return self._get_joint_operation(task_id, operation_id)

    @staticmethod
    def _joint_finished(db, task_id):
        return {data["operation_id"]: data for row in db.execute(
            "SELECT data FROM events WHERE task_id=? AND kind='operation_finished' ORDER BY seq",
            (task_id,)) for data in [json.loads(row[0])]}

    def joint_view(self, task_id):
        with self._db() as db:
            revision = self._row(db, task_id)["revision"]
            finished, contributions, operations = self._joint_finished(db, task_id), [], []
            for row in db.execute("SELECT * FROM events WHERE task_id=? AND kind IN ('contribution_recorded','operation_prepared') ORDER BY seq", (task_id,)):
                data = json.loads(row["data"])
                common = {"revision": row["revision"], "at": row["at"],
                          "historical": row["revision"] != revision}
                if row["kind"] == "contribution_recorded":
                    contributions.append({**data, **common, "id": row["id"]})
                else:
                    completion = finished.get(row["id"], {})
                    receipt = completion.get("receipt")
                    operations.append({**data, **common, "operation_id": row["id"],
                                       "status": receipt["status"] if receipt is not None else "unknown",
                                       "receipt": receipt, "source_ids": completion.get("source_ids", [])})
            return {"task_id": task_id, "revision": revision,
                    "contributions": contributions, "operations": operations,
                    "identity_verified": False, "instruction_authority": False}

    def _get_joint_operation(self, task_id, operation_id):
        return next(item for item in self.joint_view(task_id)["operations"]
                    if item["operation_id"] == operation_id)

    def create_task(self, original_words, authority, criteria, request_key, sources=None):
        words, permission, required, refs = _text(original_words, "original_words"), _authority(authority), _criteria(criteria), _references(sources)
        payload = {"original_words": words, "authority": permission, "criteria": required, "sources": refs}
        def action(db):
            task_id, at = uuid.uuid4().hex, _now()
            db.execute("INSERT INTO tasks VALUES(?,?,?,?,1,'ready',NULL,NULL,?,?)", (task_id, words, _json(permission), _json(required), at, at))
            db.execute("INSERT INTO revisions VALUES(?,1,?,?)", (task_id, words, at))
            source_ids = []
            for position, ref in enumerate(refs):
                snapshot = self._snapshot(ref)
                if snapshot["id"] in source_ids:
                    raise CoreError("Aynı kaynak iki kez verilmiş.")
                source_ids.append(snapshot["id"])
                db.execute("INSERT INTO sources VALUES(?,?,?,?)", (task_id, snapshot["id"], position, _json(snapshot)))
            self._event(db, task_id, 1, "task_created", {"authority": permission, "source_ids": source_ids, "criteria": required})
            return self._task(db, task_id)
        return self._write("create_task", request_key, payload, action)

    def revise_task(self, task_id, original_words, expected_revision, request_key):
        words, revision = _text(original_words, "original_words"), _revision(expected_revision)
        def action(db):
            task = self._row(db, task_id, revision)
            if task["status"] in ("completed", "cancelled"):
                raise Conflict("Kapanmış işe sessizce devam edilmez; yeni açık iş oluştur.")
            self._invalidate(db, task, "superseded")
            next_revision, at = revision + 1, _now()
            state = "paused" if task["status"] == "paused" else "ready"
            db.execute("INSERT INTO revisions VALUES(?,?,?,?)", (task_id, next_revision, words, at))
            db.execute("UPDATE tasks SET revision=?,status=?,updated_at=? WHERE id=?", (next_revision, state, at, task_id))
            self._event(db, task_id, next_revision, "user_correction", {"previous_revision": revision, "original_words": words, "authority_scope_changed": False})
            return self._task(db, task_id)
        return self._write("revise_task", request_key, {"task_id": task_id, "original_words": words, "expected_revision": revision}, action)

    def control_task(self, task_id, action, expected_revision, request_key):
        revision = _revision(expected_revision)
        if action not in ("pause", "resume", "cancel"):
            raise CoreError("İş kontrolü pause, resume veya cancel olmalı.")
        def change(db):
            task = self._row(db, task_id, revision)
            if task["status"] in ("completed", "cancelled"):
                raise Conflict("Tamamlanmış veya durdurulmuş iş yeniden başlatılamaz.")
            if action == "resume":
                if task["status"] != "paused":
                    raise Conflict("Yalnız duraklatılmış iş sürdürülebilir.")
                state = "ready"
            elif action == "pause":
                if task["status"] == "paused":
                    raise Conflict("İş zaten duraklatılmış.")
                state = "paused"
            else:
                state = "cancelled"
            self._invalidate(db, task, "interrupted")
            db.execute("UPDATE tasks SET status=?,updated_at=? WHERE id=?", (state, _now(), task_id))
            self._event(db, task_id, revision, "task_" + action, {"previous_status": task["status"], "external_actions_undone": False})
            return self._task(db, task_id)
        return self._write("control_task", request_key, {"task_id": task_id, "action": action, "expected_revision": revision}, change)

    def assign(self, task_id, participant, session_id, expected_revision, request_key, expected_active_attempt_id=None):
        participant, session, revision = _text(participant, "participant", 200), _text(session_id, "session_id", 256), _revision(expected_revision)
        expected_attempt = None if expected_active_attempt_id is None else _text(expected_active_attempt_id, "expected_active_attempt_id", 80)
        def action(db):
            task = self._row(db, task_id, revision)
            if task["status"] in ("paused", "cancelled", "completed"):
                raise Conflict("Bu durumda yeni çalıştırma atanamaz.")
            if task["active_attempt_id"] != expected_attempt:
                raise Conflict("Etkin çalıştırma değişti; devretmek için güncel active_attempt_id gerekli.")
            self._invalidate(db, task, "superseded")
            attempt, at = uuid.uuid4().hex, _now()
            db.execute("INSERT INTO attempts VALUES(?,?,?,?,?,'assigned','pending',?,?)", (attempt, task_id, revision, participant, session, at, at))
            db.execute("UPDATE tasks SET active_attempt_id=?,status='ready',updated_at=? WHERE id=?", (attempt, at, task_id))
            self._event(db, task_id, revision, "attempt_assigned", {"attempt_id": attempt, "participant": participant, "session_id": session, "previous_attempt_id": expected_attempt, "identity_verified": False})
            return self._task(db, task_id)
        return self._write("assign", request_key, {"task_id": task_id, "participant": participant, "session_id": session, "expected_revision": revision, "expected_active_attempt_id": expected_attempt}, action)

    def _active_attempt(self, db, attempt_id, session_id):
        attempt_id = _text(attempt_id, "attempt_id", 80)
        attempt = db.execute("SELECT * FROM attempts WHERE id=?", (attempt_id,)).fetchone()
        if attempt is None:
            raise NotFound("Çalıştırma bulunamadı.")
        if attempt["session_id"] != session_id:
            raise Conflict("Sonuç veya alım atanmış oturuma ait olmalı.")
        task = self._row(db, attempt["task_id"])
        if task["active_attempt_id"] != attempt_id or task["revision"] != attempt["revision"]:
            raise Conflict("Çalıştırma geçersizleşmiş; güncel atamayı oku.")
        if task["status"] in ("paused", "cancelled", "completed"):
            raise Conflict("İş bu durumda çalıştırılamaz.")
        return task, attempt

    def receive(self, attempt_id, session_id, request_key):
        session = _text(session_id, "session_id", 256)
        def action(db):
            task, attempt = self._active_attempt(db, attempt_id, session)
            if attempt["status"] not in ("assigned", "received"):
                raise Conflict("Bu çalıştırma daha önce sonuç üretti.")
            if attempt["status"] == "assigned":
                at = _now()
                db.execute("UPDATE attempts SET status='received',delivery_status='received',updated_at=? WHERE id=?", (at, attempt_id))
                db.execute("UPDATE tasks SET status='running',updated_at=? WHERE id=?", (at, task["id"]))
                self._event(db, task["id"], task["revision"], "attempt_received", {"attempt_id": attempt_id, "session_id": session, "observation": "local_receiver_declaration", "model_understanding_verified": False})
            current = self._task(db, task["id"])
            return {"task": current, "context": self._context(current)}
        return self._write("receive", request_key, {"attempt_id": attempt_id, "session_id": session}, action, replay_action=action)

    def submit_result(self, attempt_id, session_id, summary, artifacts, request_key):
        session, summary, refs = _text(session_id, "session_id", 256), _text(summary, "summary"), _references(artifacts)
        def action(db):
            task, attempt = self._active_attempt(db, attempt_id, session)
            if attempt["status"] != "received" or task["status"] != "running":
                raise Conflict("Sonuç öncesinde güncel çalıştırma alınmış olmalı.")
            captured = [self._snapshot(ref) for ref in refs]
            result, at = uuid.uuid4().hex, _now()
            db.execute("INSERT INTO results VALUES(?,?,?,?,?,?,?)", (result, task["id"], attempt_id, task["revision"], summary, _json(captured), at))
            db.execute("UPDATE attempts SET status='result_submitted',updated_at=? WHERE id=?", (at, attempt_id))
            db.execute("UPDATE tasks SET status='awaiting_verification',current_result_id=?,updated_at=? WHERE id=?", (result, at, task["id"]))
            self._event(db, task["id"], task["revision"], "result_submitted", {"attempt_id": attempt_id, "result_id": result, "artifact_ids": [r["id"] for r in captured], "completion_verified": False})
            return self._task(db, task["id"])
        return self._write("submit_result", request_key, {"attempt_id": attempt_id, "session_id": session, "summary": summary, "artifacts": refs}, action)

    def verify_task(self, task_id, checks, expected_revision, request_key):
        revision = _revision(expected_revision)
        if not isinstance(checks, list) or not 1 <= len(checks) <= 100:
            raise CoreError("checks boş olmayan denetim listesi olmalı.")
        normalized, seen = [], set()
        for item in checks:
            if not isinstance(item, dict) or type(item.get("passed")) is not bool:
                raise CoreError("Denetim passed boolean alanı taşımalı.")
            check = {name: _text(item.get(name), f"check.{name}") for name in ("criterion_id", "result_id", "evidence", "verifier")}
            if check["criterion_id"] in seen:
                raise CoreError("Aynı ölçüt bir denetimde iki kez verilmiş.")
            seen.add(check["criterion_id"])
            check["passed"] = item["passed"]
            normalized.append(check)
        def action(db):
            task = self._row(db, task_id, revision)
            if task["status"] not in ("awaiting_verification", "blocked") or not task["current_result_id"]:
                raise Conflict("Denetlenecek güncel sonuç bulunmuyor.")
            required = {c["id"] for c in json.loads(task["criteria"])}
            if not seen.issubset(required):
                raise CoreError("Denetim bilinmeyen kabul ölçütüne bağlı.")
            for check in normalized:
                if check["result_id"] != task["current_result_id"]:
                    raise Conflict("Denetim başka veya eski bir sonuca bağlı.")
                db.execute("""INSERT INTO checks VALUES(?,?,?,?,?,?,?)
                    ON CONFLICT(task_id,result_id,criterion_id) DO UPDATE SET
                    passed=excluded.passed,evidence=excluded.evidence,verifier=excluded.verifier,at=excluded.at""",
                    (task_id, check["result_id"], check["criterion_id"], int(check["passed"]), check["evidence"], check["verifier"], _now()))
            recorded = {r[0]: bool(r[1]) for r in db.execute("SELECT criterion_id,passed FROM checks WHERE task_id=? AND result_id=?", (task_id, task["current_result_id"]))}
            if any(not value for value in recorded.values()):
                state = "blocked"
            elif required.issubset(recorded) and all(recorded.values()):
                state = "completed"
            else:
                state = "awaiting_verification"
            db.execute("UPDATE tasks SET status=?,updated_at=? WHERE id=?", (state, _now(), task_id))
            self._event(db, task_id, revision, "verification_recorded", {"result_id": task["current_result_id"], "checks": normalized, "status": state, "verification": "submitted_receipts"})
            if state == "completed":
                self._event(db, task_id, revision, "task_completed", {"result_id": task["current_result_id"], "criteria": sorted(required)})
            return self._task(db, task_id)
        return self._write("verify_task", request_key, {"task_id": task_id, "checks": normalized, "expected_revision": revision}, action)

    def events(self, task_id=None):
        with self._db() as db:
            if task_id is not None:
                self._row(db, task_id)
                rows = db.execute("SELECT * FROM events WHERE task_id=? ORDER BY seq", (task_id,))
            else:
                rows = db.execute("SELECT * FROM events ORDER BY seq")
            result = []
            for row in rows:
                event = dict(row)
                event["schema_version"] = SCHEMA_VERSION
                event["data"] = json.loads(event["data"])
                result.append(event)
            return result

    def _context(self, task):
        sources, used = [], 0
        for source in task["sources"]:
            item = dict(source)
            try:
                with (self.directory / source["snapshot"]).open("rb") as stream:
                    data = stream.read(MAX_FILE_BYTES + 1)
            except OSError as exc:
                raise Conflict("Bağlam kaynağının sabit görüntüsü okunamadı.") from exc
            if len(data) > MAX_FILE_BYTES or hashlib.sha256(data).hexdigest() != source["sha256"]:
                raise Conflict("Bağlam kaynağının sabit görüntüsü bozulmuş.")
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                item.update(text=None, representation="binary_metadata", text_omitted_reason="utf8_text_not_available")
            else:
                if used + len(data) <= MAX_CONTEXT_TEXT_BYTES:
                    item.update(text=text, representation="full_utf8_text")
                    used += len(data)
                else:
                    item.update(text=None, representation="snapshot_reference", text_omitted_reason="context_budget")
            sources.append(item)
        return {"schema_version": SCHEMA_VERSION, "kind": "task_context", "task_id": task["id"],
                "revision": task["revision"], "original_words": task["original_words"],
                "current_words": task["current_words"], "corrections": task["revisions"][1:],
                "authority": task["authority"], "criteria": task["criteria"], "status": task["status"],
                "active_attempt_id": task["active_attempt_id"], "sources": sources,
                "previous_results": task["results"], "source_instructions_are_data": True,
                "provider_context_visibility": "application_bundle_only",
                "model_understanding_verified": False,
                "text_budget_bytes": MAX_CONTEXT_TEXT_BYTES, "included_text_bytes": used}

    def context_bundle(self, task_id):
        return self._context(self.get_task(task_id))

    def export_data(self):
        """Private JSON-ready export, never automatically published or added to Git."""
        with self._db() as db:
            tasks = [self._task(db, row[0]) for row in db.execute("SELECT id FROM tasks ORDER BY created_at,id")]
            events = []
            for row in db.execute("SELECT * FROM events ORDER BY seq"):
                event = dict(row)
                event["data"] = json.loads(event["data"])
                events.append(event)
        return {"schema_version": SCHEMA_VERSION, "classification": "private", "exported_at": _now(), "tasks": tasks, "events": events}
