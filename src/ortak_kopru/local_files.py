"""Private, verified local files and atomic publication without replacement.

These helpers protect against ordinary write failures and concurrent creators.
The local account controlling the parent directory is trusted. SHA-256 detects
changed bytes; it does not authenticate the person who supplied those bytes.
"""
from __future__ import annotations

from contextlib import contextmanager
import ctypes
import errno
import hashlib
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile

from .core import CoreError

_CHUNK_BYTES = 1024 * 1024
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")


class LocalFileError(CoreError):
    """A private local file could not be safely read, written or published."""


def private_path(value):
    """Resolve a local path and refuse an actual Git worktree or its contents."""
    try:
        if not isinstance(value, (str, os.PathLike)) or not os.fspath(value):
            raise LocalFileError("Özel dosya veya dizin yolu gerekli.")
        supplied = Path(value).expanduser().absolute()
        for candidate in (supplied, *supplied.parents):
            try:
                info = candidate.lstat()
            except FileNotFoundError:
                continue
            if stat.S_ISLNK(info.st_mode) or _is_reparse(info):
                raise LocalFileError("Özel yol simgesel bağlantı veya yeniden ayrıştırma noktası içeremez.")
        path = supplied.resolve()
        for parent in (path, *path.parents):
            marker = parent / ".git"
            if marker.is_file() or (marker / "HEAD").is_file():
                raise LocalFileError("Özel veriler bir Git çalışma ağacının içinde olamaz.")
        return path
    except (OSError, RuntimeError, TypeError, ValueError) as exc:
        if isinstance(exc, LocalFileError):
            raise
        raise LocalFileError("Özel dosya veya dizin yolu çözümlenemedi.") from exc


def _is_reparse(info):
    return bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    )


def _is_regular(info):
    # Windows junctions and other reparse points also require explicit refusal.
    return stat.S_ISREG(info.st_mode) and not _is_reparse(info)


@contextmanager
def _regular_reader(path):
    """Open a regular file, refusing a symlink before and during POSIX open."""
    path = Path(path)
    descriptor = None
    try:
        before = path.lstat()
        if not _is_regular(before):
            raise LocalFileError("Yalnız bağlantı olmayan düzenli dosyalar kullanılabilir.")
        flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        opened = os.fstat(descriptor)
        after = path.lstat()
        if not _is_regular(opened) or not _is_regular(after) or not os.path.samestat(before, opened) or not os.path.samestat(after, opened):
            raise LocalFileError("Dosya açılırken değişti veya bir bağlantı üzerinden açıldı.")
        stream = os.fdopen(descriptor, "rb")
        descriptor = None
        with stream:
            yield stream
    except OSError as exc:
        raise LocalFileError(f"Yerel dosya güvenle okunamadı: {path.name}") from exc
    finally:
        if descriptor is not None:
            os.close(descriptor)


def _limit(maximum):
    if maximum is not None and (type(maximum) is not int or maximum < 0):
        raise LocalFileError("Dosya boyutu sınırı sıfır veya pozitif tam sayı olmalı.")


def read_regular_file(path, *, maximum=None):
    """Read bounded bytes with the same regular-file/no-follow checks as copies."""
    _limit(maximum)
    with _regular_reader(path) as stream:
        if maximum is not None and os.fstat(stream.fileno()).st_size > maximum:
            raise LocalFileError("Dosya izin verilen boyut sınırını aşıyor.")
        data = stream.read() if maximum is None else stream.read(maximum + 1)
        if maximum is not None and len(data) > maximum:
            raise LocalFileError("Dosya izin verilen boyut sınırını aşıyor.")
        return data


def file_record(path, *, relative_path=None, maximum=None):
    """Hash actual regular-file bytes; optionally include a manifest path."""
    _limit(maximum)
    digest, size = hashlib.sha256(), 0
    with _regular_reader(path) as stream:
        if maximum is not None and os.fstat(stream.fileno()).st_size > maximum:
            raise LocalFileError("Dosya izin verilen boyut sınırını aşıyor.")
        while data := stream.read(_CHUNK_BYTES):
            size += len(data)
            if maximum is not None and size > maximum:
                raise LocalFileError("Dosya izin verilen boyut sınırını aşıyor.")
            digest.update(data)
    result = {"bytes": size, "sha256": digest.hexdigest()}
    if relative_path is not None:
        result["path"] = relative_path
    return result


def _expected_record(expected, maximum):
    _limit(maximum)
    if not isinstance(expected, dict) or type(expected.get("bytes")) is not int or expected["bytes"] < 0:
        raise LocalFileError("Beklenen dosya boyutu geçersiz.")
    if not isinstance(expected.get("sha256"), str) or not _DIGEST.fullmatch(expected["sha256"]):
        raise LocalFileError("Beklenen SHA-256 değeri geçersiz.")
    if maximum is not None and expected["bytes"] > maximum:
        raise LocalFileError("Dosya izin verilen boyut sınırını aşıyor.")


@contextmanager
def _new_file(path):
    """Create a mode-0600 file exclusively; remove incomplete writes on error."""
    path = Path(path)
    created = False
    descriptor = None
    try:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_BINARY", 0)
        descriptor = os.open(path, flags, 0o600)
        created = True
        stream = os.fdopen(descriptor, "wb")
        descriptor = None
        with stream:
            yield stream
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        if descriptor is not None:
            os.close(descriptor)
        if created:
            path.unlink(missing_ok=True)
        raise


def write_private_file(path, data):
    """Write and flush new bytes without replacing an existing file."""
    if not isinstance(data, bytes):
        raise LocalFileError("Kaydedilecek içerik bytes olmalı.")
    try:
        with _new_file(path) as stream:
            stream.write(data)
    except OSError as exc:
        raise LocalFileError(f"Özel dosya yazılamadı: {Path(path).name}") from exc


def copy_verified_file(source, destination, expected, *, maximum=None):
    """Copy to a new file, checking the size and digest while reading.

    The destination parent must already exist. A failed copy leaves no partial
    destination. Extra fields in expected are ignored, so core reference records
    and manifest records may be supplied directly.
    """
    _expected_record(expected, maximum)
    digest, size = hashlib.sha256(), 0
    try:
        with _regular_reader(source) as original:
            if os.fstat(original.fileno()).st_size != expected["bytes"]:
                raise LocalFileError("Dosyanın boyutu kayıtlı değerle uyuşmuyor.")
            with _new_file(destination) as copied:
                while data := original.read(_CHUNK_BYTES):
                    size += len(data)
                    if size > expected["bytes"]:
                        raise LocalFileError("Dosya kopyalanırken kayıtlı boyutu aştı.")
                    digest.update(data)
                    copied.write(data)
                if size != expected["bytes"] or digest.hexdigest() != expected["sha256"]:
                    raise LocalFileError("Dosyanın SHA-256 veya boyut denetimi başarısız.")
    except OSError as exc:
        raise LocalFileError("Doğrulanmış dosya kopyası yazılamadı.") from exc
    result = {"bytes": size, "sha256": digest.hexdigest()}
    if "path" in expected:
        result["path"] = expected["path"]
    return result


def _sync_directory(path):
    # Windows has no portable Python directory-fsync operation. File contents
    # are still flushed before the atomic rename on both supported platforms.
    if os.name == "nt":
        return
    descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _publish_no_replace(staging, destination):
    if os.name == "nt":
        os.rename(staging, destination)  # Windows refuses an existing target.
        return
    if not sys.platform.startswith("linux"):
        raise LocalFileError("Atomik ve üzerine yazmayan yayım bu platformda desteklenmiyor.")
    try:
        renameat2 = ctypes.CDLL(None, use_errno=True).renameat2
    except AttributeError as exc:
        raise LocalFileError("renameat2 desteği olmadan güvenli dizin yayımı yapılamaz.") from exc
    renameat2.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    renameat2.restype = ctypes.c_int
    if renameat2(-100, os.fsencode(staging), -100, os.fsencode(destination), 1):
        error = ctypes.get_errno()
        if error in (errno.ENOSYS, errno.EINVAL, errno.EOPNOTSUPP):
            raise LocalFileError("Dosya sistemi atomik, üzerine yazmayan dizin yayımını desteklemiyor.")
        raise OSError(error, os.strerror(error), os.fspath(destination))


def _private_parents(path):
    if path.is_dir():
        return
    if os.path.lexists(path):
        raise LocalFileError("Hedefin üst yolu bir dizin değil.")
    _private_parents(path.parent)
    try:
        path.mkdir(mode=0o700)
    except FileExistsError:
        if not path.is_dir():
            raise


@contextmanager
def new_private_directory(destination):
    """Build privately and atomically publish to a completely new directory.

    The yielded staging directory is a sibling of destination. Normal exit
    publishes it; any failure removes that staging directory. Existing targets,
    including empty directories and symlinks, are never replaced.
    """
    staging = None
    try:
        target = private_path(destination)
        unresolved = Path(destination).expanduser().absolute()
        if os.path.lexists(unresolved) or os.path.lexists(target):
            raise LocalFileError("Hedef zaten var; tamamen yeni bir dizin seçilmeli.")
        _private_parents(target.parent)
        staging = Path(tempfile.mkdtemp(prefix=".deus-stage-", dir=target.parent))
        yield staging
        # Sync entries bottom-up before exposing the root directory.
        for current, directories, _ in os.walk(staging, topdown=False, followlinks=False):
            for name in directories:
                if (Path(current) / name).is_symlink():
                    raise LocalFileError("Özel pakette dizin bağlantısı bulunamaz.")
            _sync_directory(current)
        _publish_no_replace(staging, target)
        staging = None
        _sync_directory(target.parent)
    except OSError as exc:
        raise LocalFileError("Özel dizin tamamlanamadı veya hedef zaten var.") from exc
    finally:
        if staging is not None:
            shutil.rmtree(staging)
