#!/usr/bin/env python3
"""Şaman devrini ayrı Git worktree'sinde doğrular ve mevcut Codex CLI'ı açar.

Python standart kütüphanesi ve git gerekir. Varsayılan çalışma, bu betiğin
bulunduğu depoya dokunmadan yanındaki <depo-adı>-saman dizinini hazırlar.
--hazirla yalnız hazırlar. Model, sandbox veya onay seçenekleri eklenmez.
Bu modül import edildiğinde dosya, süreç veya ağ işlemi yapmaz.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile

HANDOFF_COMMIT = 'a3e34ad2e486e1a723a9a64257b63cbc5af366ed'
HANDOFF_BRANCH = "deus-ex-machina-2026-10-24"
DEFAULT_LOCAL_BRANCH = "saman-devam-2026-10-24"
MANIFEST_PATH = "devir/saman/MANIFESTO.json"
REQUIRED_FILES = {
    "AGENTS.md",
    "devir/saman/CLI_BASLANGIC.md",
    "devir/saman/GORUNUR_KONUSMA.md",
}
SOURCE_ZIP_SHA256 = "827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009"
SOURCE_ZIP_SIZE = 100641653


class DevirError(Exception):
    """Kullanıcıya gösterilebilen, işlemi durduran doğrulama hatası."""


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def git(repo, *words, allowed=(0,)):
    result = subprocess.run(
        ["git", "-C", str(repo), *words],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode not in allowed:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise DevirError(
            "Git işlemi başarısız ({}; kod {}): {}".format(
                words[0], result.returncode, detail[:4000] or "ayrıntı verilmedi"
            )
        )
    return result


def git_text(repo, *words):
    return git(repo, *words).stdout.decode("utf-8").strip()


def common_dir(repo):
    path = Path(git_text(repo, "rev-parse", "--git-common-dir"))
    return (path if path.is_absolute() else repo / path).resolve()


def same_path(left, right):
    return os.path.normcase(str(Path(left).resolve())) == os.path.normcase(str(Path(right).resolve()))


def is_within(path, parent):
    try:
        Path(path).resolve().relative_to(Path(parent).resolve())
        return True
    except ValueError:
        return False


def is_link(path):
    junction = getattr(path, "is_junction", None)
    return path.is_symlink() or (junction is not None and junction())


def read_json(data, label):
    try:
        def unique_pairs(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError("yinelenen JSON alanı: " + key)
                result[key] = value
            return result
        return json.loads(data.decode("utf-8"), object_pairs_hook=unique_pairs)
    except (UnicodeError, ValueError) as exc:
        raise DevirError("{} okunamadı: {}".format(label, exc)) from None


def child_configuration(repo, override, require_executable=True):
    path = repo / "katilimcilar" / "ayarlar-yerel.json"
    try:
        config = read_json(path.read_bytes(), "ayarlar-yerel.json")
    except OSError as exc:
        raise DevirError("Yerel CLI ayarları okunamadı: {}".format(exc)) from None
    if not isinstance(config, dict) or not isinstance(config.get("katilimcilar"), list):
        raise DevirError("ayarlar-yerel.json içinde katilimcilar listesi bulunamadı.")
    matches = [
        item for item in config["katilimcilar"]
        if isinstance(item, dict) and item.get("ad") == "ChatGPT" and item.get("saglayici") == "cli"
    ]
    if len(matches) != 1:
        raise DevirError("Tam bir ChatGPT/cli katılımcısı bulunmalı; mevcut sayı: {}.".format(len(matches)))
    entry = matches[0]
    command = entry.get("komut")
    if not isinstance(command, list) or not command or not isinstance(command[0], str):
        raise DevirError("ChatGPT CLI komut[0] alanı bulunamadı.")
    overrides = entry.get("ortam", {})
    if not isinstance(overrides, dict):
        raise DevirError("ChatGPT ortam alanı bir nesne olmalı.")
    environment = os.environ.copy()
    for key, value in overrides.items():
        if not isinstance(key, str) or not key or "=" in key or "\0" in key:
            raise DevirError("Geçersiz ortam değişkeni adı.")
        if value is not None and (not isinstance(value, str) or "\0" in value):
            raise DevirError("Ortam değerleri metin veya null olmalı: " + key)
        for current in list(environment):
            if current == key or (os.name == "nt" and current.casefold() == key.casefold()):
                del environment[current]
        if value is not None:
            environment[key] = value

    # Yalnız executable kullanılır. Eski köprü komutundaki exec/efor/diğer
    # argümanlar etkileşimli oturuma taşınmaz.
    supplied = override if override is not None else command[0]
    if not supplied or "\0" in supplied:
        raise DevirError("Codex çalıştırılabilir dosyası belirtilmedi.")
    if not require_executable:
        # Paket hazırlığı Codex kurulumu gerektirmez. Bu değer hazırlık
        # yolunda çalıştırılmaz; gerçek açılış aynı sıkı denetimden geçer.
        return supplied, environment
    executable = Path(supplied).expanduser()
    if not executable.is_absolute():
        base = Path.cwd() if override is not None else repo
        candidate = base / executable
        if candidate.is_file() or "/" in supplied or "\\" in supplied:
            executable = candidate
        else:
            found = shutil.which(supplied, path=environment.get("PATH", ""))
            if not found:
                raise DevirError("Codex çalıştırılabilir dosyası bulunamadı: " + supplied)
            executable = Path(found)
    if not executable.is_file():
        raise DevirError("Codex çalıştırılabilir dosyası bulunamadı: " + str(executable))
    executable = executable.resolve()
    if os.name != "nt" and not os.access(executable, os.X_OK):
        raise DevirError("Codex dosyası çalıştırılabilir değil: " + str(executable))
    return str(executable), environment


def validate_manifest_path(value):
    if not isinstance(value, str) or not value or any(c in value for c in "\\:\0*?[]"):
        raise DevirError("Manifestte geçersiz dosya yolu.")
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value:
        raise DevirError("Manifest yolu köke göre, normalleştirilmiş olmalı: " + value)
    reserved = {"CON", "PRN", "AUX", "NUL"}
    reserved.update("COM" + str(i) for i in range(1, 10))
    reserved.update("LPT" + str(i) for i in range(1, 10))
    for part in path.parts:
        if part in (".", "..") or part.casefold() == ".git" or part.endswith((".", " ")):
            raise DevirError("Manifest yolu depo dışına veya Git verisine açılamaz: " + value)
        if part.split(".", 1)[0].upper() in reserved:
            raise DevirError("Manifestte Windows için ayrılmış dosya adı: " + value)
    if value == MANIFEST_PATH:
        raise DevirError("Manifest kendi files listesine konamaz.")
    return value


def manifest_from_commit(repo, pin):
    raw = git(repo, "show", pin + ":" + MANIFEST_PATH).stdout
    value = read_json(raw, MANIFEST_PATH)
    if not isinstance(value, dict) or not isinstance(value.get("files"), list):
        raise DevirError("MANIFESTO.json içinde files listesi bulunamadı.")
    entries, seen = [], set()
    for item in value["files"]:
        if not isinstance(item, dict):
            raise DevirError("Manifest files girdisi nesne olmalı.")
        path = validate_manifest_path(item.get("path"))
        key = path.casefold()
        if key in seen:
            raise DevirError("Manifestte yinelenen dosya yolu: " + path)
        seen.add(key)
        size, sha = item.get("size"), item.get("sha256")
        if type(size) is not int or size < 0 or not isinstance(sha, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", sha):
            raise DevirError("Manifest size/sha256 alanları geçersiz: " + path)
        data = git(repo, "show", pin + ":" + path).stdout
        if len(data) != size or hashlib.sha256(data).hexdigest() != sha.lower():
            raise DevirError("Sabit commit içeriği manifestle eşleşmiyor: " + path)
        entries.append({"path": path, "size": size, "sha256": sha.lower()})
    if not REQUIRED_FILES.issubset({item["path"] for item in entries}):
        raise DevirError("Manifestte AGENTS.md, CLI_BASLANGIC.md ve GORUNUR_KONUSMA.md bulunmalı.")
    return raw, entries


def regular_package_file(target, relative):
    current = target
    for part in PurePosixPath(relative).parts:
        current = current / part
        if is_link(current):
            raise DevirError("Sabit paket yolunda sembolik bağ/junction kabul edilmez: " + relative)
    if not current.is_file() or not is_within(current, target):
        raise DevirError("Sabit paket dosyası bulunamadı veya kökün dışında: " + relative)
    return current


def verify_package(target, raw_manifest, entries):
    actual = regular_package_file(target, MANIFEST_PATH).read_bytes()
    if actual != raw_manifest:
        raise DevirError("Çalışma ağacındaki MANIFESTO.json sabit commit'ten farklı; değiştirilmedi.")
    for item in entries:
        path = regular_package_file(target, item["path"])
        digest = hashlib.sha256()
        size = 0
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                size += len(block)
                digest.update(block)
        if size != item["size"] or digest.hexdigest() != item["sha256"]:
            raise DevirError("Sabit devir dosyası değişmiş; üzerine yazılmadı: " + item["path"])


def worktrees(repo):
    result = []
    current = {}
    for token in git(repo, "worktree", "list", "--porcelain", "-z").stdout.decode("utf-8").split("\0"):
        if not token:
            if current:
                result.append(current)
                current = {}
            continue
        key, _, value = token.partition(" ")
        current[key] = value
    if current:
        result.append(current)
    return result


def assert_ancestor(repo, ancestor, descendant, message):
    result = git(repo, "merge-base", "--is-ancestor", ancestor, descendant, allowed=(0, 1))
    if result.returncode:
        raise DevirError(message)


def verify_worktree(repo, target, branch, pin, common):
    if not same_path(git_text(target, "rev-parse", "--show-toplevel"), target):
        raise DevirError("Hedef dizin ayrı worktree kökü değil; değiştirilmedi.")
    if not same_path(common_dir(target), common):
        raise DevirError("Hedef başka bir Git common-dir'e bağlı; değiştirilmedi.")
    actual_branch = git(target, "symbolic-ref", "--quiet", "--short", "HEAD", allowed=(0, 1))
    if actual_branch.returncode or actual_branch.stdout.decode("utf-8").strip() != branch:
        raise DevirError("Hedef beklenen yerel dalda değil ({}); dal değiştirilmedi.".format(branch))
    head = git_text(target, "rev-parse", "--verify", "HEAD")
    assert_ancestor(
        repo, pin, head,
        "Hedef dal sabit devir commit'inden türemiyor; reset/checkout yapılmadı.",
    )
    return head


def ensure_worktree(repo, target, branch, pin, common):
    if is_within(target, repo) or is_within(target, common):
        raise DevirError("Hedef, kaynak çalışma ağacı ve Git veri dizininin dışında olmalı.")
    registered = [entry for entry in worktrees(repo) if same_path(entry["worktree"], target)]
    exists = target.exists() or target.is_symlink()
    if registered:
        if not exists:
            raise DevirError("Hedef için eski worktree kaydı var ama dizin yok; otomatik prune/temizlik yapılmadı.")
        verify_worktree(repo, target, branch, pin, common)
        return False
    if exists:
        raise DevirError("Hedef mevcut, fakat bu depoya kayıtlı worktree değil; üzerine yazılmadı.")
    branch_exists = git(repo, "show-ref", "--verify", "--quiet", "refs/heads/" + branch, allowed=(0, 1))
    if branch_exists.returncode == 0:
        raise DevirError("Yerel dal zaten var; yeniden kullanılmadı veya sıfırlanmadı. --dal/--hedef seçimini denetleyin.")
    # Windows'taki core.autocrlf ayarı sabit Git bloblarını değiştirmesin.
    # Bu iki seçenek yalnız bu Git komutuna aittir; hiçbir config yazılmaz.
    git(repo, "-c", "core.autocrlf=false", "-c", "core.eol=lf",
        "worktree", "add", "--no-track", "-b", branch, "--", str(target), pin)
    verify_worktree(repo, target, branch, pin, common)
    return True


def verify_source_zip(value):
    if value is None:
        return None
    path = Path(value).expanduser().resolve()
    if not path.is_file():
        raise DevirError("Kaynak ZIP bulunamadı: " + str(path))
    if path.stat().st_size != SOURCE_ZIP_SIZE:
        raise DevirError("Kaynak ZIP boyutu beklenen {} bayt değil.".format(SOURCE_ZIP_SIZE))
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(block)
            digest.update(block)
    if size != SOURCE_ZIP_SIZE or digest.hexdigest() != SOURCE_ZIP_SHA256:
        raise DevirError("Kaynak ZIP SHA-256 doğrulaması başarısız; kopyalanmadı veya açılmadı.")
    return {"path": str(path), "size": size, "sha256": digest.hexdigest(), "verified_at": utc_now()}


def private_status_path(common, target):
    directory = common / "saman-devir"
    if is_link(directory):
        raise DevirError("Özel durum dizini sembolik bağ/junction olamaz.")
    directory.mkdir(mode=0o700, exist_ok=True)
    key = hashlib.sha256(os.path.normcase(str(target)).encode("utf-8")).hexdigest()[:20]
    path = directory / (key + ".json")
    if is_link(path):
        raise DevirError("Özel durum dosyası sembolik bağ/junction olamaz.")
    return path


def write_status(path, value):
    data = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix=".saman-", suffix=".tmp", dir=str(path.parent))
    try:
        if os.name != "nt":
            os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hazirla", action="store_true", help="CLI açmadan ayrı çalışma ağacını hazırla ve doğrula")
    parser.add_argument("--hedef", help="ayrı worktree dizini; varsayılan kaynak deponun yanındaki <depo-adı>-saman")
    parser.add_argument("--dal", default=DEFAULT_LOCAL_BRANCH, help="yerel devam dalı")
    parser.add_argument("--codex", help="katilimcilar/ayarlar-yerel.json komut[0] yerine kullanılacak mevcut çalıştırılabilir dosya")
    parser.add_argument("--kaynak-zip", help="özgün Steering ZIP'i; yalnız boyut ve SHA-256 doğrulanır, çıkarılmaz")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1], help=argparse.SUPPRESS)
    return parser


def prepare(args):
    if not re.fullmatch(r"[0-9a-f]{40}", HANDOFF_COMMIT):
        raise DevirError("Bu başlatıcı yayımlanmış devir commit'ine henüz sabitlenmemiş.")
    if not shutil.which("git"):
        raise DevirError("git bulunamadı; mevcut Git kurulumunun PATH'te olması gerekir.")
    repo = Path(git_text(args.repo.resolve(), "rev-parse", "--show-toplevel")).resolve()
    common = common_dir(repo)
    branch = args.dal
    if not branch or branch.startswith("-") or branch == "HEAD":
        raise DevirError("Geçersiz yerel dal adı.")
    if git_text(repo, "check-ref-format", "--branch", branch) != branch:
        raise DevirError("Dal adı bir kısaltma yerine açık yerel ad olmalı.")
    target = (Path(args.hedef).expanduser() if args.hedef else repo.with_name(repo.name + "-saman")).resolve()
    executable, environment = child_configuration(repo, args.codex, require_executable=not args.hazirla)
    source_zip = verify_source_zip(args.kaynak_zip)

    remote_ref = "refs/remotes/origin/" + HANDOFF_BRANCH
    git(repo, "fetch", "--no-tags", "origin", "refs/heads/" + HANDOFF_BRANCH + ":" + remote_ref)
    tip = git_text(repo, "rev-parse", "--verify", remote_ref + "^{commit}")
    pin = git_text(repo, "rev-parse", "--verify", HANDOFF_COMMIT + "^{commit}")
    if pin != HANDOFF_COMMIT:
        raise DevirError("Devir nesnesi beklenen commit değil.")
    assert_ancestor(repo, pin, tip, "Sabit devir commit'i beklenen origin dalının atası değil.")
    raw_manifest, entries = manifest_from_commit(repo, pin)
    created = ensure_worktree(repo, target, branch, pin, common)
    verify_package(target, raw_manifest, entries)

    status_path = private_status_path(common, target)
    environment["SAMAN_DEVIR_STATE"] = str(status_path)
    previous_zip = None
    if status_path.exists():
        previous = read_json(status_path.read_bytes(), "Önceki özel hazırlık kaydı")
        if isinstance(previous, dict) and previous.get("handoff_commit") == pin:
            value = previous.get("source_zip")
            if isinstance(value, dict) and value.get("sha256") == SOURCE_ZIP_SHA256 and value.get("size") == SOURCE_ZIP_SIZE:
                previous_zip = value
    status = {
        "schema_version": 1,
        "prepared_at": utc_now(),
        "handoff_commit": pin,
        "source_branch": HANDOFF_BRANCH,
        "source_tip_at_fetch": tip,
        "worktree": str(target),
        "local_branch": branch,
        "fixed_file_count": len(entries),
        "manifest_sha256": hashlib.sha256(raw_manifest).hexdigest(),
        "source_zip": source_zip if source_zip is not None else previous_zip,
        "source_zip_checked_this_run": source_zip is not None,
        "preparation": "verified",
        "reading_observed_by_launcher": False,
        "acceptance_observed_by_launcher": False,
        "cli": {"state": "not_started"},
    }
    write_status(status_path, status)
    return {
        "target": target, "executable": executable, "environment": environment,
        "status_path": status_path, "status": status, "created": created,
    }


def startup_prompt(status_path):
    return (
        "Şaman olarak bu devirden devam et. Önce AGENTS.md, "
        "devir/saman/CLI_BASLANGIC.md ve devir/saman/GORUNUR_KONUSMA.md dosyalarını oku. "
        "Özgün kullanıcı talebi, yapılmış işler ve açık işleri ayır; gerçekten gördüğün "
        "kaynakları bildir ve yetkilendirilmiş işi kaldığı yerden sürdür. Hazırlık, "
        "senin okuma veya kabul beyanın değildir. Varsa özel kaynak ZIP yolu şu "
        "yerel hazırlık kaydındadır: " + str(status_path)
    )


def run(args):
    prepared = prepare(args)
    target = prepared["target"]
    status_path, status = prepared["status_path"], prepared["status"]
    print("Ayrı çalışma ağacı {}: {}".format("hazırlandı" if prepared["created"] else "doğrulandı", target))
    print("Sabit devir paketi doğrulandı: " + HANDOFF_COMMIT)
    print("Özel hazırlık kaydı: " + str(status_path))
    if args.hazirla:
        print("CLI açılmadı. Hazırlık, Şaman'ın paketi okuduğu veya devri kabul ettiği anlamına gelmez.")
        return 0
    status["cli"] = {"state": "starting", "started_at": utc_now()}
    write_status(status_path, status)
    print("Şaman için mevcut Codex CLI etkileşimli olarak açılıyor.", flush=True)
    try:
        result = subprocess.run(
            [prepared["executable"], startup_prompt(status_path)],
            cwd=str(target), env=prepared["environment"], check=False,
        )
    except OSError as exc:
        status["cli"].update({"state": "failed_to_start", "finished_at": utc_now()})
        write_status(status_path, status)
        raise DevirError("Codex CLI başlatılamadı: " + str(exc)) from None
    except KeyboardInterrupt:
        status["cli"].update({"state": "interrupted", "finished_at": utc_now()})
        write_status(status_path, status)
        raise
    status["cli"].update({"state": "process_exited", "finished_at": utc_now(), "returncode": result.returncode})
    write_status(status_path, status)
    print("CLI işlemi sonlandı (kod {}). Okuma ve devir sonucu, CLI'ın kendi geri anlatımında doğrulanmalıdır.".format(result.returncode))
    return result.returncode


def main(argv=None):
    args = argument_parser().parse_args(argv)
    try:
        return run(args)
    except (DevirError, OSError, UnicodeError) as exc:
        print("HATA: " + str(exc), file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("İşlem kesildi; çalışma ağacı ve mevcut değişiklikler korundu.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())

