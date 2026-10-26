"""Bounded GitHub REST transport for explicit, selected file exchanges.

Only api.github.com is contacted. Reads pin Git objects; writes can create
objects, a new branch and a pull request, never update an existing branch.
HTTP redirects and automatic retries are deliberately disabled. The caller
owns durable checkpoints and reconciliation after an uncertain write.
"""
from __future__ import annotations

import base64
import binascii
import hashlib
from http.client import HTTPException
import json
import math
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener

from ..core import CoreError

API_ROOT = "https://api.github.com"
API_VERSION = "2022-11-28"
MAX_FILES = 64
MAX_FILE_BYTES = 8 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
_SHA = re.compile(r"[0-9a-fA-F]{40}\Z")
_OWNER = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}\Z")
_REPOSITORY = re.compile(r"[A-Za-z0-9_.-]{1,100}\Z")


class GitHubError(CoreError):
    """A sanitized failure; ambiguous means a write may have taken effect."""

    def __init__(self, message, *, status=None, code="github_error", ambiguous=False):
        super().__init__(message)
        self.status = status
        self.code = code
        self.ambiguous = bool(ambiguous)


class GitHubConflict(GitHubError):
    """An existing remote state or validation condition prevents the write."""


def _invalid(message="GitHub girdisi geçersiz."):
    return GitHubError(message, code="invalid_input")


def _protocol(*, ambiguous=False):
    return GitHubError("GitHub yanıtı beklenen nesne veya işlemle uyuşmuyor.",
                       code="invalid_response", ambiguous=ambiguous)


def _sha(value, *, ambiguous=False):
    if not isinstance(value, str) or not _SHA.fullmatch(value):
        raise _protocol(ambiguous=ambiguous)
    return value.lower()


def _input_sha(value):
    if not isinstance(value, str) or not _SHA.fullmatch(value):
        raise _invalid("Tam Git commit veya nesne kimliği gerekli.")
    return value.lower()


def validate_repository(value):
    """Accept an owner/repository name, never a URL or credential-bearing text."""
    if not isinstance(value, str) or value.count("/") != 1:
        raise _invalid("GitHub deposu sahip/depo biçiminde olmalı.")
    owner, name = value.split("/")
    if not _OWNER.fullmatch(owner) or not _REPOSITORY.fullmatch(name) or name in {".", ".."}:
        raise _invalid("GitHub deposu sahip/depo biçiminde olmalı.")
    return value


def validate_ref(value):
    """Accept a literal branch/tag/ref or complete commit, not revision syntax."""
    if (not isinstance(value, str) or not value or len(value) > 256
            or value == "@" or value.startswith(("/", "-")) or value.endswith(("/", "."))
            or ".." in value or "@{" in value
            or any(ord(c) < 33 or ord(c) == 127 or c in "~^:?*[\\" for c in value)
            or any(not part or part.startswith(".") or part.endswith(".lock") for part in value.split("/"))):
        raise _invalid("GitHub ref adı geçersiz.")
    try:
        value.encode("utf-8")
    except UnicodeError:
        raise _invalid("GitHub ref adı geçerli UTF-8 olmalı.") from None
    return value


def validate_branch(value):
    value = validate_ref(value)
    if value == "HEAD" or value.startswith("refs/"):
        raise _invalid("Dal adı kısa biçimde verilmeli; HEAD veya refs/ öneki kullanılamaz.")
    return value


def _paths(values):
    if not isinstance(values, (list, tuple)) or not 1 <= len(values) <= MAX_FILES:
        raise _invalid("GitHub seçimi 1 ile 64 dosya içermeli.")
    result = []
    for value in values:
        if (not isinstance(value, str) or not value or len(value) > 4096
                or "\\" in value or any(ord(c) < 32 or ord(c) == 127 for c in value)
                or any(part in {"", ".", ".."} or part.casefold() == ".git"
                       for part in value.split("/"))):
            raise _invalid("Dosya yolu depoya göreli, açık ve geçerli olmalı.")
        result.append(value)
    if len(set(result)) != len(result):
        raise _invalid("Aynı dosya birden çok kez seçilemez.")
    selected = set(result)
    for path in result:
        parts = path.split("/")
        if any("/".join(parts[:n]) in selected for n in range(1, len(parts))):
            raise _invalid("Seçimde dosya ve alt yol çakışması var.")
    return result


def git_blob_sha(data):
    if not isinstance(data, bytes):
        raise _invalid("Git blob içeriği bytes olmalı.")
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data,
                        usedforsecurity=False).hexdigest()


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def _json_decode(data):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    def constant(_value):
        raise ValueError("non-finite JSON value")

    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)


class GitHubClient:
    def __init__(self, token=None, *, opener=None, timeout=20):
        if token is not None:
            if (not isinstance(token, str) or not token or not token.isascii()
                    or any(c.isspace() or ord(c) < 32 or ord(c) == 127 for c in token)):
                raise _invalid("GitHub erişim bilgisi biçimi geçersiz.")
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or not 0 < timeout <= 120:
            raise _invalid("HTTP zaman aşımı 0 ile 120 saniye arasında olmalı.")
        self._token = token
        self._opener = opener if opener is not None else build_opener(_NoRedirect())
        self.timeout = timeout

    @classmethod
    def from_env(cls):
        for key in ("ORTAK_KOPRU_GITHUB_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"):
            value = os.environ.get(key, "").strip()
            if value:
                return cls(value)
        return cls()

    @property
    def authenticated(self):
        return self._token is not None

    def _http_error(self, status, *, write):
        if 300 <= status < 400:
            return GitHubError("GitHub yönlendirmesi izlenmedi; hedef açıkça yeniden seçilmeli.",
                               status=status, code="redirect_refused", ambiguous=write)
        if status in (409, 422):
            return GitHubConflict("GitHub hedef durumu veya doğrulama koşulu işlemle çakıştı.",
                                  status=status, code="conflict")
        messages = {
            401: ("unauthorized", "GitHub kimlik doğrulaması başarısız."),
            403: ("forbidden", "GitHub erişimi veya istek kotası bu işlemi engelledi."),
            404: ("not_found", "GitHub nesnesi bulunamadı veya bu oturuma görünmüyor."),
            429: ("rate_limited", "GitHub istek sınırı aşıldı; işlem otomatik tekrarlanmadı."),
        }
        code, message = messages.get(status, ("http_error", "GitHub HTTP isteği tamamlanamadı."))
        return GitHubError(message, status=status, code=code,
                           ambiguous=write and (200 <= status < 300 or status >= 500 or status == 408))

    def _request(self, method, path, body=None, *, expected=200):
        # Every public method constructs its own path; reject arbitrary hosts,
        # header delimiters or caller-provided credential URLs even internally.
        if (method not in {"GET", "POST"} or not path.startswith("/repos/")
                or any(ord(c) < 32 or ord(c) == 127 for c in path)):
            raise _invalid()
        write = method == "POST"
        if write and not self._token:
            raise GitHubError("GitHub yazımı için yerel erişim bilgisi gerekli.", code="credentials_required")
        payload = None
        if body is not None:
            try:
                payload = json.dumps(body, ensure_ascii=False, allow_nan=False, separators=(",", ":")).encode("utf-8")
            except (ValueError, TypeError, UnicodeError):
                raise _invalid() from None
            if len(payload) > MAX_RESPONSE_BYTES:
                raise _invalid("GitHub istek içeriği boyut sınırını aşıyor.")
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": API_VERSION,
                   "User-Agent": "ortak-kopru-exchange/1", "Accept-Encoding": "identity"}
        if self._token:
            headers["Authorization"] = "Bearer " + self._token
        if payload is not None:
            headers["Content-Type"] = "application/json; charset=utf-8"
        request = Request(API_ROOT + path, data=payload, headers=headers, method=method)
        try:
            open_request = self._opener.open if hasattr(self._opener, "open") else self._opener
            with open_request(request, timeout=self.timeout) as response:
                status = response.status
                if response.geturl() != request.full_url:
                    raise GitHubError("GitHub yanıtı istenen adresten gelmedi.", code="redirect_refused", ambiguous=write)
                if status != expected:
                    raise self._http_error(status, write=write)
                length = response.headers.get("Content-Length")
                if length is not None:
                    try:
                        length = int(length)
                    except (TypeError, ValueError):
                        raise _protocol(ambiguous=write) from None
                    if not 0 <= length <= MAX_RESPONSE_BYTES:
                        raise _protocol(ambiguous=write)
                data = response.read(MAX_RESPONSE_BYTES + 1)
                if len(data) > MAX_RESPONSE_BYTES:
                    raise _protocol(ambiguous=write)
        except HTTPError as exc:
            status = exc.code
            exc.close()
            raise self._http_error(status, write=write) from None
        except (URLError, OSError, TimeoutError, HTTPException):
            raise GitHubError("GitHub bağlantısı tamamlanamadı; uzak sonuç sorgulanmalıdır." if write
                               else "GitHub kaynağına bağlantı kurulamadı.",
                               code="transport_error", ambiguous=write) from None
        try:
            return _json_decode(data)
        except (ValueError, UnicodeError, RecursionError):
            raise _protocol(ambiguous=write) from None

    @staticmethod
    def _root(repository):
        return "/repos/" + validate_repository(repository)

    def resolve_ref(self, repository, ref):
        ref = validate_ref(ref)
        value = self._request("GET", self._root(repository) + "/commits/" + quote(ref, safe=""))
        if not isinstance(value, dict) or not isinstance(value.get("commit"), dict):
            raise _protocol()
        tree = value["commit"].get("tree")
        if not isinstance(tree, dict):
            raise _protocol()
        commit_sha = _sha(value.get("sha"))
        if _SHA.fullmatch(ref) and commit_sha != ref.lower():
            raise _protocol()
        return {"commit": commit_sha, "tree": _sha(tree.get("sha"))}

    @staticmethod
    def _commit(value, *, expected_sha=None, write=False):
        if (not isinstance(value, dict) or not isinstance(value.get("tree"), dict)
                or not isinstance(value.get("parents"), list) or len(value["parents"]) > 128
                or not isinstance(value.get("message"), str) or len(value["message"]) > 1024 * 1024):
            raise _protocol(ambiguous=write)
        sha = _sha(value.get("sha"), ambiguous=write)
        parents = []
        for parent in value["parents"]:
            if not isinstance(parent, dict):
                raise _protocol(ambiguous=write)
            parents.append(_sha(parent.get("sha"), ambiguous=write))
        if expected_sha is not None and sha != expected_sha:
            raise _protocol(ambiguous=write)
        return {"sha": sha, "tree": _sha(value["tree"].get("sha"), ambiguous=write),
                "parents": parents, "message": value["message"]}

    def get_commit(self, repository, sha):
        sha = _input_sha(sha)
        return self._commit(self._request("GET", self._root(repository) + "/git/commits/" + sha), expected_sha=sha)

    def _tree(self, repository, sha, cache):
        if sha in cache:
            return cache[sha]
        value = self._request("GET", self._root(repository) + "/git/trees/" + sha)
        if (not isinstance(value, dict) or _sha(value.get("sha")) != sha
                or value.get("truncated") is not False or not isinstance(value.get("tree"), list)):
            raise _protocol()
        entries = {}
        for entry in value["tree"]:
            if not isinstance(entry, dict):
                raise _protocol()
            path = entry.get("path")
            if not isinstance(path, str) or not path or "/" in path or path in entries:
                raise _protocol()
            if entry.get("type") not in {"blob", "tree", "commit"} or not isinstance(entry.get("mode"), str):
                raise _protocol()
            entries[path] = {"sha": _sha(entry.get("sha")), "mode": entry["mode"], "type": entry["type"]}
        cache[sha] = entries
        return entries

    def inspect_paths(self, repository, commit, paths):
        paths = _paths(paths)
        root = self.get_commit(repository, commit)["tree"]
        cache, result = {}, []
        for path in paths:
            tree, entry = root, None
            parts = path.split("/")
            for number, name in enumerate(parts):
                entry = self._tree(repository, tree, cache).get(name)
                if entry is None:
                    break
                if number < len(parts) - 1:
                    if entry["type"] != "tree" or entry["mode"] != "040000":
                        raise GitHubError("Seçilen yolun üst bileşeni düzenli bir Git dizini değil.", code="unsupported_path")
                    tree = entry["sha"]
                elif entry["type"] != "blob" or entry["mode"] not in {"100644", "100755"}:
                    raise GitHubError("Yalnız düzenli Git dosyaları seçilebilir; bağlantı veya alt modül kabul edilmez.", code="unsupported_path")
            result.append({"path": path, "blob_sha": entry["sha"] if entry else None,
                           "mode": entry["mode"] if entry else None})
        return result

    def _blob(self, repository, sha):
        value = self._request("GET", self._root(repository) + "/git/blobs/" + sha)
        if (not isinstance(value, dict) or _sha(value.get("sha")) != sha
                or value.get("encoding") != "base64" or not isinstance(value.get("content"), str)
                or type(value.get("size")) is not int or not 0 <= value["size"] <= MAX_FILE_BYTES):
            raise _protocol()
        try:
            data = base64.b64decode("".join(value["content"].split()), validate=True)
        except (ValueError, binascii.Error):
            raise _protocol() from None
        if len(data) != value["size"] or len(data) > MAX_FILE_BYTES or git_blob_sha(data) != sha:
            raise _protocol()
        return data

    def files_at(self, repository, commit, paths):
        selection = self.inspect_paths(repository, _input_sha(commit), paths)
        result, blobs, total = [], {}, 0
        for entry in selection:
            sha = entry["blob_sha"]
            if sha is None:
                raise GitHubError("Seçilen dosya sabit Git commit'inde bulunamadı.", status=404, code="not_found")
            if sha not in blobs:
                blobs[sha] = self._blob(repository, sha)
            data = blobs[sha]
            total += len(data)
            if total > MAX_TOTAL_BYTES:
                raise GitHubError("GitHub dosya seçimi toplam boyut sınırını aşıyor.", code="size_limit")
            result.append({**entry, "bytes": len(data), "data": data})
        return result

    def create_blob(self, repository, data):
        if not isinstance(data, bytes) or len(data) > MAX_FILE_BYTES:
            raise _invalid("Blob bytes olmalı ve 8 MiB sınırını aşmamalı.")
        expected = git_blob_sha(data)
        value = self._request("POST", self._root(repository) + "/git/blobs",
                              {"content": base64.b64encode(data).decode("ascii"), "encoding": "base64"}, expected=201)
        if not isinstance(value, dict) or _sha(value.get("sha"), ambiguous=True) != expected:
            raise _protocol(ambiguous=True)
        return expected

    def create_tree(self, repository, base_tree, entries):
        base_tree = _input_sha(base_tree)
        if not isinstance(entries, list) or any(not isinstance(e, dict) for e in entries):
            raise _invalid()
        _paths([entry.get("path") for entry in entries])
        selected = []
        for entry in entries:
            if set(entry) != {"path", "mode", "type", "sha"} or entry["mode"] not in {"100644", "100755"} or entry["type"] != "blob":
                raise _invalid("Ağaç yazımı yalnız seçilmiş düzenli blob ekleme/değiştirmeyi destekler.")
            selected.append({**entry, "sha": _input_sha(entry["sha"])})
        value = self._request("POST", self._root(repository) + "/git/trees",
                              {"base_tree": base_tree, "tree": selected}, expected=201)
        if not isinstance(value, dict):
            raise _protocol(ambiguous=True)
        return _sha(value.get("sha"), ambiguous=True)

    def create_commit(self, repository, tree, parent, message):
        tree, parent = _input_sha(tree), _input_sha(parent)
        if not isinstance(message, str) or not message.strip() or len(message) > 65536 or "\0" in message:
            raise _invalid("Commit açıklaması gerekli ve 65536 karakteri aşmamalı.")
        value = self._request("POST", self._root(repository) + "/git/commits",
                              {"tree": tree, "parents": [parent], "message": message}, expected=201)
        commit = self._commit(value, write=True)
        if commit["tree"] != tree or commit["parents"] != [parent] or commit["message"] != message:
            raise _protocol(ambiguous=True)
        return commit["sha"]

    @staticmethod
    def _branch(value, branch, *, write=False):
        if (not isinstance(value, dict) or value.get("ref") != "refs/heads/" + branch
                or not isinstance(value.get("object"), dict) or value["object"].get("type") != "commit"):
            raise _protocol(ambiguous=write)
        return _sha(value["object"].get("sha"), ambiguous=write)

    def get_branch(self, repository, branch):
        branch = validate_branch(branch)
        try:
            value = self._request("GET", self._root(repository) + "/git/ref/heads/" + quote(branch, safe=""))
        except GitHubError as error:
            if error.status == 404:
                return None
            raise
        return self._branch(value, branch)

    def create_branch(self, repository, branch, commit):
        branch, commit = validate_branch(branch), _input_sha(commit)
        value = self._request("POST", self._root(repository) + "/git/refs",
                              {"ref": "refs/heads/" + branch, "sha": commit}, expected=201)
        actual = self._branch(value, branch, write=True)
        if actual != commit:
            raise _protocol(ambiguous=True)
        return actual

    @staticmethod
    def _pr(value, repository, branch, base, *, write=False):
        if not isinstance(value, dict):
            raise _protocol(ambiguous=write)
        number = value.get("number")
        if type(number) is not int or number <= 0 or value.get("state") not in {"open", "closed"} or type(value.get("draft")) is not bool:
            raise _protocol(ambiguous=write)
        for key, expected in (("head", branch), ("base", base)):
            ref = value.get(key)
            if (not isinstance(ref, dict) or ref.get("ref") != expected
                    or not isinstance(ref.get("repo"), dict)
                    or not isinstance(ref["repo"].get("full_name"), str)
                    or ref["repo"]["full_name"].casefold() != repository.casefold()):
                raise _protocol(ambiguous=write)
        url = value.get("html_url")
        if not isinstance(url, str) or url.casefold() != f"https://github.com/{repository}/pull/{number}".casefold():
            raise _protocol(ambiguous=write)
        return {"number": number, "url": url, "head_sha": _sha(value["head"].get("sha"), ambiguous=write),
                "head_ref": branch, "base_ref": base, "state": value["state"], "draft": value["draft"]}

    def find_pull_request(self, repository, branch, base):
        repository = validate_repository(repository)
        branch, base = validate_branch(branch), validate_branch(base)
        query = urlencode({"state": "all", "head": repository.split("/")[0] + ":" + branch,
                           "base": base, "per_page": 100})
        values = self._request("GET", self._root(repository) + "/pulls?" + query)
        if not isinstance(values, list) or len(values) >= 100:
            raise _protocol()
        selected = [self._pr(value, repository, branch, base) for value in values]
        if len(selected) > 1:
            raise GitHubConflict("Aynı aktarım dalı için tek bir PR belirlenemedi.", code="conflict")
        return selected[0] if selected else None

    def create_pull_request(self, repository, branch, base, title, body, draft=True):
        repository = validate_repository(repository)
        branch, base = validate_branch(branch), validate_branch(base)
        if (branch == base or not isinstance(title, str) or not title.strip() or len(title) > 256
                or not isinstance(body, str) or len(body) > 65536 or type(draft) is not bool
                or "\0" in title or "\0" in body):
            raise _invalid("PR başlığı, gövdesi veya dal seçimi geçersiz.")
        value = self._request("POST", self._root(repository) + "/pulls",
                              {"head": branch, "base": base, "title": title, "body": body, "draft": draft}, expected=201)
        result = self._pr(value, repository, branch, base, write=True)
        if result["state"] != "open" or result["draft"] != draft:
            raise _protocol(ambiguous=True)
        return result
