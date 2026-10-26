"""Task-independent GitHub exchange, with explicit plans and recoverable writes.

The publisher only creates a new branch. It never updates an existing ref,
merges a PR, deletes a remote object or executes downloaded content. Purpose,
original local paths and private task context never become commit/PR text.
"""
from __future__ import annotations

from datetime import datetime, timezone
import difflib
import hashlib
import hmac
import json
import re
from urllib.parse import quote

from .adapters.github import (
    GitHubError, git_blob_sha, validate_branch, validate_ref, validate_repository,
)
from .exchange import (
    ExchangeConflict, ExchangeError, MAX_FILES, MAX_TOTAL_BYTES, validate_path,
)

PLAN_VERSION = 1
MAX_DIFF_CHARS = 128 * 1024
MAX_FILE_DIFF_CHARS = 16 * 1024
_SHA = re.compile(r"[0-9a-f]{40}\Z")
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")


def _now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


def _digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def _sha(value):
    if not isinstance(value, str) or not _SHA.fullmatch(value):
        raise ExchangeError("Uzak Git nesnesi için kesin commit/nesne kimliği gerekli.")
    return value


def _paths(values):
    if not isinstance(values, list) or not 1 <= len(values) <= MAX_FILES:
        raise ExchangeError(f"Tedarik 1–{MAX_FILES} dosya yolu içermeli.")
    paths = [validate_path(value) for value in values]
    folded = [path.casefold() for path in paths]
    if len(set(folded)) != len(paths):
        raise ExchangeError("Tedarik yolları birbiriyle çakışıyor.")
    components = {}
    for path in paths:
        parts = path.split("/")
        for end in range(1, len(parts) + 1):
            prefix = "/".join(parts[:end])
            if components.setdefault(prefix.casefold(), prefix) != prefix:
                raise ExchangeError("Tedarik dizinlerinin büyük/küçük harf yazımı çakışıyor.")
        if any("/".join(parts[:end]).casefold() in folded for end in range(1, len(parts))):
            raise ExchangeError("Bir tedarik yolu hem dosya hem dizin olamaz.")
    return sorted(paths)


def prepare(store, selections, *, repository, base_ref="main", branch=None,
            purpose, request_key):
    """Freeze selected local bytes; no client, network or task is required."""
    repository = validate_repository(repository)
    base_ref = validate_branch(base_ref)
    if branch is not None:
        branch = validate_branch(branch)
        if branch == base_ref:
            raise ExchangeError("Yayın dalı taban dalından farklı ve yeni olmalı.")
    return store.prepare_outbound(selections, {
        "provider": "github", "repository": repository,
        "base_ref": base_ref, "branch": branch,
    }, purpose, request_key)


def fetch(store, client, *, repository, ref, paths, purpose, request_key):
    """Fetch all selected files at one commit before recording an inbound copy."""
    repository = validate_repository(repository)
    ref = validate_ref(ref)
    paths = _paths(paths)
    resolved = client.resolve_ref(repository, ref)
    commit, tree = _sha(resolved["commit"]), _sha(resolved["tree"])
    remote = client.files_at(repository, commit, paths)
    if (len(remote) != len(paths) or {item["path"] for item in remote} != set(paths)):
        raise ExchangeError("Alınan dosyalar seçilmiş tedarik yollarıyla uyuşmuyor.")
    files, total = [], 0
    for item in remote:
        data = item["data"]
        if (not isinstance(data, bytes) or item["bytes"] != len(data)
                or git_blob_sha(data) != _sha(item["blob_sha"])
                or item["mode"] not in {"100644", "100755"}):
            raise ExchangeError("Alınan dosyanın Git nesnesi veya boyutu uyuşmuyor.")
        total += len(data)
        if total > MAX_TOTAL_BYTES:
            raise ExchangeError("Tedarik toplam boyut sınırını aşıyor.")
        files.append({"path": item["path"], "data": data, "source": {
            "provider": "github", "repository": repository, "commit": commit,
            "path": item["path"], "blob_sha": item["blob_sha"], "mode": item["mode"],
        }})
    return store.record_inbound(files, {
        "provider": "github", "repository": repository, "requested_ref": ref,
        "commit": commit, "tree": tree,
        "url": f"https://github.com/{repository}/tree/{commit}",
    }, purpose, request_key)


def _outbound(record):
    if record["direction"] != "outbound":
        raise ExchangeError("Bu işlem yalnız dışarı paylaşım kaydında kullanılabilir.")
    target = record["target"]
    if (not isinstance(target, dict)
            or set(target) != {"provider", "repository", "base_ref", "branch"}
            or target["provider"] != "github"):
        raise ExchangeError("Aktarımın GitHub hedefi desteklenmiyor.")
    validate_repository(target["repository"])
    validate_branch(target["base_ref"])
    branch = validate_branch(target["branch"] or "kopru/" + record["id"])
    if branch == target["base_ref"]:
        raise ExchangeError("Yayın dalı taban dalından farklı olmalı.")
    return target, branch


def _diff(old, new, path, budget):
    try:
        before, after = old.decode("utf-8"), new.decode("utf-8")
        if "\0" in before or "\0" in after:
            raise UnicodeError
    except UnicodeError:
        return {"binary": True, "diff": None, "diff_truncated": False}, budget
    limit = min(MAX_FILE_DIFF_CHARS, budget)
    parts, length, truncated = [], 0, False
    # This preview is explanatory, not an executable patch. Bound both the
    # stored result and work spent comparing very long text files.
    if len(before) + len(after) > 512 * 1024:
        return {"binary": False, "diff": None, "diff_truncated": True}, budget
    for line in difflib.unified_diff(before.splitlines(keepends=True),
                                     after.splitlines(keepends=True),
                                     fromfile="before/" + path, tofile="after/" + path):
        if length + len(line) > limit:
            parts.append(line[:max(0, limit - length)])
            truncated = True
            length = limit
            break
        parts.append(line)
        length += len(line)
    return {"binary": False, "diff": "".join(parts), "diff_truncated": truncated}, budget - length


def plan(store, transfer_id, client):
    """Read the base branch and save an exact content/target plan; no writes."""
    with store.operation(transfer_id):
        record = store.verify(transfer_id)
        target, branch = _outbound(record)
        if record["state"] == "published":
            return record
        if (record["state"] not in {"prepared", "planned", "failed", "conflict"}
                or (record.get("checkpoint") or {}).get("ref_confirmed")
                or record.get("receipt")):
            raise ExchangeConflict("Gönderim sonucu önce reconcile ile denetlenmeli; plan değiştirilemedi.")
        repo, base = target["repository"], target["base_ref"]
        base_commit = client.get_branch(repo, base)
        if base_commit is None:
            raise ExchangeError("GitHub taban dalı bulunamadı veya erişilemiyor.")
        base_commit = _sha(base_commit)
        commit = client.get_commit(repo, base_commit)
        if commit["sha"] != base_commit:
            raise ExchangeError("Taban commit yanıtı istenen sürüme ait değil.")
        base_tree = _sha(commit["tree"])
        if client.get_branch(repo, branch) is not None:
            raise ExchangeConflict("Yayın dalı zaten var; mevcut dal değiştirilmez.")
        entries = record["manifest"]["files"]
        existing = client.inspect_paths(repo, base_commit, [item["path"] for item in entries])
        before = {item["path"]: item for item in existing}
        if len(existing) != len(entries) or set(before) != {item["path"] for item in entries}:
            raise ExchangeError("Uzak karşılaştırma seçilmiş dosyalarla uyuşmuyor.")
        changes, budget = [], MAX_DIFF_CHARS
        for item in entries:
            data = store.read_object(transfer_id, item["sha256"])
            previous = before[item["path"]]
            old_sha = previous["blob_sha"]
            if old_sha is not None:
                _sha(old_sha)
                if previous["mode"] not in {"100644", "100755"}:
                    raise ExchangeError("Hedefteki öğe düzenli Git dosyası değil.")
            blob = git_blob_sha(data)
            action = "unchanged" if blob == old_sha else "add" if old_sha is None else "modify"
            change = {"path": item["path"], "bytes": item["bytes"], "sha256": item["sha256"],
                      "blob_sha": blob, "previous_blob": old_sha,
                      "mode": previous["mode"] if old_sha is not None else "100644", "action": action}
            if action == "unchanged":
                change.update(binary=None, diff=None, diff_truncated=False)
            else:
                old = b""
                if old_sha is not None:
                    old_file = client.files_at(repo, base_commit, [item["path"]])[0]
                    if old_file["blob_sha"] != old_sha:
                        raise ExchangeError("Karşılaştırılan kaynak sabit commit ile uyuşmuyor.")
                    old = old_file["data"]
                preview, budget = _diff(old, data, item["path"], budget)
                change.update(preview)
            changes.append(change)
        value = {"schema_version": PLAN_VERSION, "provider": "github", "repository": repo,
                 "base_ref": base, "base_commit": base_commit, "base_tree": base_tree,
                 "branch": branch, "manifest_sha256": _digest(record["manifest"]),
                 "changes": changes, "changed_files": sum(c["action"] != "unchanged" for c in changes),
                 "preview_only": True}
        value["plan_hash"] = _digest(value)
        return store.update(transfer_id, expected_states=[record["state"]], state="planned",
                            plan=value, checkpoint=None, receipt=None, error=None)


def _checked_plan(store, record, expected_hash=None):
    target, branch = _outbound(record)
    value = record.get("plan")
    if not isinstance(value, dict) or not isinstance(value.get("plan_hash"), str):
        raise ExchangeError("Gönderimden önce plan oluşturulmalı.")
    digest = value["plan_hash"]
    if (not _DIGEST.fullmatch(digest)
            or not hmac.compare_digest(digest, _digest({key: item for key, item in value.items() if key != "plan_hash"}))):
        raise ExchangeConflict("Kaydedilmiş planın karma denetimi başarısız.")
    if expected_hash is not None and (not isinstance(expected_hash, str)
            or not _DIGEST.fullmatch(expected_hash) or not hmac.compare_digest(expected_hash, digest)):
        raise ExchangeConflict("Gönderim istenen planla eşleşmiyor; güncel planın karması gerekli.")
    if (value.get("schema_version") != PLAN_VERSION or value.get("provider") != "github"
            or value.get("repository") != target["repository"]
            or value.get("base_ref") != target["base_ref"] or value.get("branch") != branch
            or value.get("manifest_sha256") != _digest(record["manifest"])):
        raise ExchangeConflict("Planın hedefi veya içeriği aktarım kaydıyla uyuşmuyor.")
    _sha(value.get("base_commit"))
    _sha(value.get("base_tree"))
    changes = value.get("changes")
    entries = record["manifest"]["files"]
    if not isinstance(changes, list) or len(changes) != len(entries):
        raise ExchangeConflict("Plan dosya listesi seçilmiş içerikle uyuşmuyor.")
    for item, change in zip(entries, changes):
        if (not isinstance(change, dict)
                or any(change.get(key) != item[key] for key in ("path", "bytes", "sha256"))
                or change.get("mode") not in {"100644", "100755"}
                or change.get("blob_sha") != git_blob_sha(store.read_object(record["id"], item["sha256"]))):
            raise ExchangeConflict("Plan dosyası saklanan baytlarla uyuşmuyor.")
    return value


def _update(store, record, state, **changes):
    return store.update(record["id"], expected_states=[record["state"]], state=state, **changes)


def _checkpoint(store, record, **changes):
    value = dict(record.get("checkpoint") or {})
    value.update(changes)
    return _update(store, record, "sending", checkpoint=value, error=None)


def _message(record):
    return ("Ortak Köprü: seçilmiş dosya aktarımı\n\n"
            f"Transfer: {record['id']}\nPlan-SHA256: {record['plan']['plan_hash']}")


def _failure(store, record, error, *, uncertain=False):
    status = getattr(error, "status", None)
    ambiguous = uncertain or getattr(error, "ambiguous", False) is True
    conflict = isinstance(error, ExchangeConflict) or status in {409, 422}
    state = "unknown" if ambiguous else "conflict" if conflict else "failed"
    information = {
        "code": "outcome_unknown" if ambiguous else "target_conflict" if conflict else "exchange_failed",
        "message": ("Uzak sonuç kesinleşmedi; reconcile ile denetlenmeli." if ambiguous else
                    "Hedef veya sürüm koşulu uyuşmuyor; mevcut uzak içerik değiştirilmedi." if conflict else
                    "Aktarım tamamlanamadı; kayıtlı kapsam korunuyor."),
        "ambiguous": ambiguous,
    }
    if type(status) is int:
        information["status"] = status
    provider_code = getattr(error, "code", None)
    if provider_code in {"authentication_required", "credentials_required", "unauthorized", "forbidden",
                         "rate_limited", "redirect_refused", "network_error", "http_error",
                         "protocol_error", "transport_error", "invalid_response", "conflict", "not_found"}:
        information["provider_code"] = provider_code
    if status in {401, 403} and not ambiguous:
        information["message"] = "GitHub erişimi yetersiz; yerel hizmet kimlik bilgisi ve depo yetkisi denetlenmeli."
    return _update(store, record, state, error=information)


def _publication(record, client, observed):
    value, checkpoint = record["plan"], record.get("checkpoint") or {}
    expected = checkpoint.get("commit")
    if (expected is None or checkpoint.get("tree") is None or observed != expected):
        raise ExchangeConflict("Yayın dalı bu aktarımın kayıtlı commit'iyle uyuşmuyor.")
    commit = client.get_commit(value["repository"], observed)
    if (commit["sha"] != expected or commit["tree"] != checkpoint["tree"]
            or commit["parents"] != [value["base_commit"]] or commit["message"] != _message(record)):
        raise ExchangeConflict("Uzak commit'in içeriği, tabanı veya aktarım bağı uyuşmuyor.")
    remote = client.inspect_paths(value["repository"], observed,
                                  [item["path"] for item in value["changes"]])
    by_path = {item["path"]: item for item in remote}
    if len(remote) != len(value["changes"]) or set(by_path) != {item["path"] for item in value["changes"]}:
        raise ExchangeConflict("Uzak commit seçilmiş dosyaların tamamını taşımıyor.")
    for item in value["changes"]:
        actual = by_path[item["path"]]
        if actual["blob_sha"] != item["blob_sha"] or actual["mode"] != item["mode"]:
            raise ExchangeConflict("Uzak commit'te seçilen dosyanın bayt kimliği uyuşmuyor.")
    return {"provider": "github", "repository": value["repository"],
            "branch": value["branch"], "commit": observed, "tree": commit["tree"],
            "base_commit": value["base_commit"], "plan_hash": value["plan_hash"],
            "url": f"https://github.com/{value['repository']}/commit/{observed}",
            "branch_url": f"https://github.com/{value['repository']}/tree/{quote(value['branch'], safe='/')}",
            "verified_at": _now(), "verified_scope": "commit_parent_tree_and_selected_blob_ids",
            "files": [{key: item[key] for key in ("path", "bytes", "sha256", "blob_sha")}
                      for item in value["changes"]], "pull_request": None}


def _pull_request(record, client, *, create):
    value = record["plan"]
    if create:
        result = client.create_pull_request(
            value["repository"], value["branch"], value["base_ref"],
            "Ortak Köprü aktarımı " + record["id"],
            f"Seçilmiş {len(value['changes'])} dosyanın aktarımı.\n\n"
            f"Aktarım: `{record['id']}`\n\nPlan SHA-256: `{value['plan_hash']}`", draft=True)
    else:
        result = client.find_pull_request(value["repository"], value["branch"], value["base_ref"])
    if result is not None and (result["head_sha"] != record["checkpoint"]["commit"]
            or result["head_ref"] != value["branch"] or result["base_ref"] != value["base_ref"]):
        raise ExchangeConflict("Pull request bu aktarımın commit veya hedefiyle uyuşmuyor.")
    return result


def _finish(store, record, client, observed, *, create_pr):
    try:
        receipt = _publication(record, client, observed)
    except GitHubError as error:
        # The ref may already have been created, including after a lost reply.
        # A failed read cannot establish that the remote write failed.
        return _failure(store, store.get(record["id"]), error, uncertain=True)
    record = _checkpoint(store, record, ref_confirmed=True)
    # Persist the verified branch before a possible, separately observable PR
    # operation. A PR failure must not erase proof that the branch was created.
    record = _update(store, record, "sending", receipt=receipt)
    if record["checkpoint"].get("pull_request"):
        try:
            result = _pull_request(record, client, create=False)
        except GitHubError as error:
            # A prior PR write may have completed. A failed lookup cannot
            # turn that unknown outcome into a definite failure.
            return _failure(store, store.get(record["id"]), error, uncertain=True)
        if result is None and create_pr:
            result = _pull_request(record, client, create=True)
        if result is None:
            return _update(store, record, "unknown", error={
                "code": "pull_request_not_observed", "ambiguous": True,
                "message": "Yayın dalı doğrulandı; istenen pull request henüz gözlenmedi."})
        receipt["pull_request"] = result
    return _update(store, record, "published", receipt=receipt, error=None)


def reconcile(store, transfer_id, client):
    """Observe a previous write and reconcile its receipt; never write remotely."""
    with store.operation(transfer_id):
        record = store.verify(transfer_id)
        value = _checked_plan(store, record)
        try:
            observed = client.get_branch(value["repository"], value["branch"])
            if observed is None:
                if (record.get("checkpoint") or {}).get("ref_confirmed") or record.get("receipt"):
                    raise ExchangeConflict("Önceden doğrulanmış yayın dalı artık bulunmuyor.")
                return _update(store, record, "planned", error=None)
            return _finish(store, record, client, observed, create_pr=False)
        except GitHubError as error:
            return _failure(store, store.get(transfer_id), error, uncertain=True)
        except ExchangeConflict as error:
            return _failure(store, store.get(transfer_id), error)


def send(store, transfer_id, client, *, expected_plan_hash, pull_request=False):
    """Publish frozen files on one new branch; retry only after observing it."""
    if type(pull_request) is not bool:
        raise ExchangeError("pull_request seçimi boolean olmalı.")
    with store.operation(transfer_id):
        record = store.verify(transfer_id)
        value = _checked_plan(store, record, expected_plan_hash)
        checkpoint = record.get("checkpoint") or {}
        if "pull_request" in checkpoint and checkpoint["pull_request"] != pull_request:
            raise ExchangeConflict("Başlamış gönderimin PR kapsamı değiştirilemez.")
        if record["state"] == "published":
            return record  # A replay cannot republish a subsequently removed branch.
        if pull_request and value["changed_files"] == 0:
            raise ExchangeError("İçerik farkı olmayan plan için pull request oluşturulamaz.")
        repo = value["repository"]
        try:
            # A process may have exited after a successful remote operation.
            # Always inspect the deterministic new branch before another write.
            try:
                observed = client.get_branch(repo, value["branch"])
            except GitHubError as error:
                return _failure(store, record, error, uncertain=(
                    record["state"] in {"sending", "unknown"}
                    or bool(checkpoint.get("ref_confirmed") or record.get("receipt"))))
            if observed is not None:
                return _finish(store, record, client, observed, create_pr=True)
            if checkpoint.get("ref_confirmed") or record.get("receipt"):
                raise ExchangeConflict("Önceden yayımlanan dal silinmiş; otomatik yeniden oluşturulmaz.")
            try:
                current_base = client.get_branch(repo, value["base_ref"])
            except GitHubError as error:
                return _failure(store, record, error,
                                uncertain=record["state"] in {"sending", "unknown"})
            if current_base != value["base_commit"]:
                raise ExchangeConflict("Taban dalı planlandıktan sonra değişti; yeni plan gerekli.")
            record = _checkpoint(store, record, pull_request=pull_request)
            if not client.authenticated:
                raise GitHubError("GitHub yazma işlemi için yerel hizmet yetkisi gerekli.",
                                  code="authentication_required", status=401)
            entries = []
            for change in value["changes"]:
                data = store.read_object(transfer_id, change["sha256"])
                blob = client.create_blob(repo, data)
                if blob != change["blob_sha"]:
                    raise ExchangeConflict("Oluşturulan Git nesnesi planlanan baytlarla uyuşmuyor.")
                entries.append({"path": change["path"], "mode": change["mode"], "type": "blob", "sha": blob})
            tree = _sha(client.create_tree(repo, value["base_tree"], entries))
            record = _checkpoint(store, record, tree=tree)
            # Reuse a known commit after a lost ref response; otherwise create
            # an unreferenced immutable object and durably record it first.
            commit = (record.get("checkpoint") or {}).get("commit")
            if commit is None:
                commit = _sha(client.create_commit(repo, tree, value["base_commit"], _message(record)))
                record = _checkpoint(store, record, commit=commit)
            # Verify the complete selected-file binding while the immutable
            # commit is still unreferenced. A bad/reused checkpoint must never
            # become a visible branch and only then be discovered as wrong.
            _publication(record, client, commit)
            observed = client.create_branch(repo, value["branch"], commit)
            if observed != commit:
                raise ExchangeConflict("Oluşturulan dal beklenen commit'e bağlı değil.")
            record = _checkpoint(store, record, ref_confirmed=True)
            return _finish(store, record, client, observed, create_pr=True)
        except GitHubError as error:
            return _failure(store, store.get(transfer_id), error)
        except ExchangeConflict as error:
            return _failure(store, store.get(transfer_id), error)
        except ExchangeError as error:
            current = store.get(transfer_id)
            return _failure(store, current, error,
                            uncertain=bool((current.get("checkpoint") or {}).get("ref_confirmed")))
