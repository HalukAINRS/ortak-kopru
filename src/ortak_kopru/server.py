"""Loopback HTTP surface for the local task store; no provider calls."""

from __future__ import annotations

import hmac
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import secrets
from urllib.parse import unquote, urlsplit

from .core import Conflict, CoreError, NotFound, Store


MAX_BODY_BYTES = 1024 * 1024
UI_ROOT = Path(__file__).resolve().parents[2] / "ui" / "deus"


def runtime_status(backend: str, *, strict: bool = True) -> dict:
    """Kernel mode is established only by the actual driver's protocol reply."""
    if backend == "portable":
        return {
            "backend": "portable", "ready": True,
            "execution_mode": "software_portable", "kernel_verified": False,
            "task_execution": "user-mode",
            "kernel": {"ready": False, "state": "not-requested"},
        }
    if backend != "nt-kernel":
        raise ValueError("Bilinmeyen çalışma arka ucu.")
    from .adapters.windows_nt import query_status
    kernel = query_status(strict=strict)
    ready = kernel.get("ready") is True
    return {
        "backend": "nt-kernel", "ready": ready,
        "execution_mode": "nt_kernel_verified" if ready else "nt_kernel_unavailable",
        "kernel_verified": ready, "task_execution": "user-mode", "kernel": kernel,
    }


def decode_json(data: bytes):
    def unique_pairs(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise ValueError("JSON alanı birden fazla kez verilmiş.")
            obj[key] = value
        return obj

    def no_constant(_):
        raise ValueError("Sonlu olmayan JSON sayısı kabul edilmez.")

    return json.loads(data.decode("utf-8"), object_pairs_hook=unique_pairs,
                      parse_constant=no_constant)


def error_response(error: Exception):
    if isinstance(error, NotFound):
        return 404, "not_found", str(error)
    if isinstance(error, Conflict):
        return 409, "conflict", str(error)
    if isinstance(error, (CoreError, ValueError, UnicodeError)):
        return 400, "invalid_request", str(error)
    # Import lazily so portable mode needs no Windows libraries.
    if type(error).__name__ == "KernelUnavailable":
        return 503, "kernel_unavailable", "NT çekirdek uç noktası doğrulanamadı; işlem yürütülmedi."
    if isinstance(error, OSError):
        return 400, "io_error", "Yerel dosya veya veri alanına erişilemedi."
    return 500, "internal_error", "İşlem tamamlanamadı; çalışma kaydı korunuyor."


class LocalServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


class Handler(BaseHTTPRequestHandler):
    server_version = "OrtakKopru/1"

    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, _format, *args):
        # Request bodies, paths and session credentials must not enter web logs.
        pass

    def _send(self, code, payload, content_type="application/json; charset=utf-8"):
        if isinstance(payload, (dict, list)):
            data = (json.dumps(payload, ensure_ascii=False, allow_nan=False) + "\n").encode("utf-8")
        elif isinstance(payload, str):
            data = payload.encode("utf-8")
        else:
            data = payload
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.send_header("Connection", "close")
        self.end_headers()
        self.wfile.write(data)

    def _error(self, code, kind, message):
        self._send(code, {"error": {"code": kind, "message": message}})

    def _check_surface(self):
        hosts = self.headers.get_all("Host", [])
        port = self.server.server_address[1]
        allowed = {f"127.0.0.1:{port}", f"localhost:{port}"}
        if len(hosts) != 1 or hosts[0] not in allowed:
            self._error(403, "invalid_host", "Yalnız yerel köprü adresi kullanılabilir.")
            return False
        if self.headers.get("Sec-Fetch-Site", "") == "cross-site":
            self._error(403, "cross_site", "Başka bir siteden köprü isteği kabul edilmez.")
            return False
        origin = self.headers.get_all("Origin", [])
        if origin and (len(origin) != 1 or origin[0] != "http://" + hosts[0]):
            self._error(403, "invalid_origin", "İstek köprünün kendi yüzeyinden gelmeli.")
            return False
        return True

    def _check_token(self, *, mutation=False):
        values = self.headers.get_all("X-Deus-Token", [])
        if (len(values) != 1 or not values[0].isascii()
                or not hmac.compare_digest(values[0], self.server.token)):
            self._error(403, "invalid_token", "Bu yüzey oturumu için geçerli erişim gerekli.")
            return False
        if mutation and len(self.headers.get_all("Origin", [])) != 1:
            self._error(403, "missing_origin", "Yazma isteğinde yerel Origin başlığı gerekli.")
            return False
        return True

    def _path(self):
        value = urlsplit(self.path)
        if value.scheme or value.netloc or value.query or value.fragment:
            raise ValueError("Bu uç nokta sorgu veya mutlak adres kabul etmez.")
        return value.path

    def do_GET(self):
        if not self._check_surface():
            return
        try:
            path = self._path()
            if path.startswith("/api/"):
                if not self._check_token():
                    return
                if path == "/api/runtime":
                    self._send(200, runtime_status(self.server.backend, strict=False))
                    return
                if path == "/api/tasks":
                    self._send(200, {"tasks": self.server.store.list_tasks()})
                    return
                if path == "/api/sessions":
                    from .handoff import list_sessions
                    self._send(200, list_sessions(self.server.store))
                    return
                session_match = re.fullmatch(r"/api/sessions/([^/]+)/inbox", path)
                if session_match:
                    from .handoff import inbox
                    session = unquote(session_match.group(1), encoding="utf-8", errors="strict")
                    self._send(200, inbox(self.server.store, session))
                    return
                match = re.fullmatch(r"/api/tasks/([A-Za-z0-9_-]+)(?:/(context|events))?", path)
                if not match:
                    self._error(404, "not_found", "Uç nokta bulunamadı.")
                    return
                task_id, action = match.groups()
                if action == "context":
                    value = self.server.store.context_bundle(task_id)
                elif action == "events":
                    self.server.store.get_task(task_id)
                    value = {"events": self.server.store.events(task_id)}
                else:
                    value = self.server.store.get_task(task_id)
                self._send(200, value)
                return
            assets = {"/": "index.html", "/index.html": "index.html",
                      "/app.js": "app.js", "/styles.css": "styles.css"}
            if path not in assets:
                self._error(404, "not_found", "Sayfa bulunamadı.")
                return
            file = self.server.ui_root / assets[path]
            if not file.is_file():
                self._error(404, "not_found", "Arayüz dosyası bulunamadı.")
                return
            types = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
                     ".css": "text/css; charset=utf-8"}
            data = file.read_bytes()
            # Public bootstrap assets never carry credentials.  The launcher's
            # private stdout supplies a fragment URL; fragments are not sent here.
            self._send(200, data, types[file.suffix])
        except Exception as error:
            self._error(*error_response(error))

    def _body(self):
        if self.headers.get_all("Transfer-Encoding", []):
            raise ValueError("Parçalı aktarım desteklenmiyor.")
        lengths = self.headers.get_all("Content-Length", [])
        if len(lengths) != 1 or not lengths[0].isdigit():
            raise ValueError("Tek bir Content-Length alanı gerekli.")
        size = int(lengths[0])
        if size <= 0 or size > MAX_BODY_BYTES:
            raise ValueError("JSON istek gövdesi boş veya fazla büyük.")
        content_types = self.headers.get_all("Content-Type", [])
        if len(content_types) != 1 or content_types[0].split(";", 1)[0].strip().lower() != "application/json":
            raise ValueError("İstek application/json olmalı.")
        data = self.rfile.read(size)
        if len(data) != size:
            raise ValueError("Eksik istek gövdesi.")
        value = decode_json(data)
        if not isinstance(value, dict):
            raise ValueError("İstek bir JSON nesnesi olmalı.")
        return value

    def do_POST(self):
        if not self._check_surface() or not self._check_token(mutation=True):
            return
        try:
            path = self._path()
            value = self._body()
            # Recording a stop must stay possible when the kernel endpoint is lost.
            # It changes task metadata only; it does not load a driver or run code.
            metadata_stop = (re.fullmatch(r"/api/tasks/[A-Za-z0-9_-]+/control", path)
                             and value.get("action") in ("pause", "cancel"))
            runtime_status(self.server.backend, strict=not metadata_stop)
            store = self.server.store
            if path == "/api/tasks":
                result = self._invoke(store.create_task, value,
                                      {"original_words", "authority", "criteria", "request_key"}, {"sources"})
            else:
                match = re.fullmatch(r"/api/(tasks|attempts)/([A-Za-z0-9_-]+)/([a-z]+)", path)
                if not match:
                    self._error(404, "not_found", "Uç nokta bulunamadı.")
                    return
                group, identity, action = match.groups()
                routes = {
                    ("tasks", "revise"): (store.revise_task, "task_id", {"original_words", "expected_revision", "request_key"}, set()),
                    ("tasks", "control"): (store.control_task, "task_id", {"action", "expected_revision", "request_key"}, set()),
                    ("tasks", "assign"): (store.assign, "task_id", {"participant", "session_id", "expected_revision", "request_key"}, {"expected_active_attempt_id"}),
                    ("tasks", "verify"): (store.verify_task, "task_id", {"checks", "expected_revision", "request_key"}, set()),
                    ("attempts", "receive"): (store.receive, "attempt_id", {"session_id", "request_key"}, set()),
                    ("attempts", "result"): (store.submit_result, "attempt_id", {"session_id", "summary", "artifacts", "request_key"}, set()),
                }
                if (group, action) not in routes:
                    self._error(404, "not_found", "İşlem bulunamadı.")
                    return
                method, field, required, optional = routes[(group, action)]
                result = self._invoke(method, value, required, optional, **{field: identity})
            self._send(200, result)
        except Exception as error:
            self._error(*error_response(error))

    @staticmethod
    def _invoke(method, value, required, optional, **bound):
        if set(value) - required - optional or not required <= set(value):
            raise ValueError("İstek alanları eksik veya tanımsız.")
        return method(**bound, **value)


def create_server(state_dir, *, backend="nt-kernel", port=8765, ui_dir=None):
    """Create only a loopback listener; callers own serve_forever/server_close."""
    if isinstance(port, bool) or not isinstance(port, int) or not 0 <= port <= 65535:
        raise ValueError("Geçerli bir TCP portu gerekli.")
    runtime_status(backend, strict=True)
    store = Store(state_dir)
    server = LocalServer(("127.0.0.1", port), Handler)
    server.store = store
    server.backend = backend
    server.token = secrets.token_urlsafe(32)
    server.ui_root = Path(ui_dir) if ui_dir is not None else UI_ROOT
    return server
