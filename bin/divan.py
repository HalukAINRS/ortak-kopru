#!/usr/bin/env python3
"""Divan: standard-library-only file exchange for agents sharing a filesystem."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from uuid import uuid4

MEMBERS = {
    "chatgpt_sohbet": "01_codex_karargahi",
    "codex_cli": "01_codex_karargahi",
    "codex_cloud": "01_codex_karargahi",
    "claude_sohbet": "01_claude_code_karargahi",
    "claude_code_cli": "01_claude_code_karargahi",
    "gemini_sohbet": "01_antigravity_karargahi",
    "antigravity_cli": "01_antigravity_karargahi",
}
TSI = timezone(timedelta(hours=3))


def now():
    return datetime.now(TSI).isoformat(timespec="seconds")


def put_new(path, data):
    """Publish a whole file atomically without replacing an existing file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".divan-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.link(tmp, path)
    finally:
        os.unlink(tmp)


def json_text(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_id(value):
    if not re.fullmatch(r"[a-f0-9]{32}", value):
        raise ValueError("Girdi kimliği 32 küçük onaltılık karakter olmalı.")
    return value


def member_dir(root, member):
    return root / "02_karargahlar" / MEMBERS[member] / "uyeler" / member


def board(root):
    return root / "01_ortak_alan" / "yeni_0"


def message(root, ident):
    ident = check_id(ident)
    data = read_json(board(root) / (ident + ".json"))
    validate(data, ident)
    return data


def validate(data, ident):
    if not isinstance(data, dict):
        raise ValueError(f"Yeni 0 zarfı bir JSON nesnesi olmalı: {ident}")
    if data.get("id") != ident or data.get("tur") != "yeni_0" or data.get("surum") != 1:
        raise ValueError(f"Geçersiz yeni 0 zarfı: {ident}")
    if data.get("yazar") not in MEMBERS:
        raise ValueError(f"Bilinmeyen yazar: {ident}")
    targets = data.get("hedefler")
    if not isinstance(targets, list) or not targets or any(t not in MEMBERS for t in targets):
        raise ValueError(f"Geçersiz hedefler: {ident}")
    for key in ("baslik", "amac", "beklenen_cikti", "girdi", "olusma_zamani"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"Eksik {key}: {ident}")
    datetime.fromisoformat(data["olusma_zamani"])
    if data.get("onceki_girdi") is not None:
        check_id(data["onceki_girdi"])


def validate_lineage(messages):
    """A derived new 0 must have an existing, acyclic chain of starting inputs."""
    done = set()
    for ident in messages:
        chain = set()
        current = ident
        while current is not None and current not in done:
            if current in chain:
                raise ValueError(f"Girdi zinciri döngü içeriyor: {current}")
            if current not in messages:
                raise ValueError(f"Önceki girdi panoda yok: {current}")
            chain.add(current)
            current = messages[current].get("onceki_girdi")
        done.update(chain)


def ensure_running(root):
    control = read_json(root / "00_yonetim" / "denetim.json")
    if control.get("durum") != "devam":
        raise ValueError("Kullanıcı denetimi: akış duraklatılmış. Yeni iş alınamaz/yayımlanamaz.")


def addressed(root, member, ident):
    data = message(root, ident)
    if member not in data["hedefler"]:
        raise ValueError("Bu girdi belirtilen üyeye yöneltilmemiş.")
    return data


def init(root):
    paths = [board(root), root / "00_yonetim" / "kaynaklar", root / "03_sablonlar"]
    for member in MEMBERS:
        paths += [member_dir(root, member) / p for p in ("calisma", "sonuclar_1", "alindi")]
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
    defaults = {
        "denetim.json": {"durum": "devam", "aciklama": "Kullanıcının açık talimatları önceliklidir."},
        "uyeler.json": {
            member: {"karargah": group, "baglanti": "dogrulanmadi"}
            for member, group in MEMBERS.items()
        },
    }
    for name, data in defaults.items():
        try:
            put_new(root / "00_yonetim" / name, json_text(data))
        except FileExistsError:
            pass
    # Add newly supported actors without replacing existing member status.
    registry_path = root / "00_yonetim" / "uyeler.json"
    original = registry_path.read_bytes()
    registry = json.loads(original)
    if not isinstance(registry, dict):
        raise ValueError("Üye kaydı bir JSON nesnesi olmalı.")
    missing = {member: {"karargah": group, "baglanti": "dogrulanmadi"}
               for member, group in MEMBERS.items() if member not in registry}
    if missing:
        registry.update(missing)
        fd, temporary = tempfile.mkstemp(prefix=".uyeler-", dir=registry_path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as out:
                out.write(json_text(registry))
                out.flush()
                os.fsync(out.fileno())
            if registry_path.read_bytes() != original:
                raise ValueError("Üye kaydı eşzamanlı değişti; değişiklikleri koruyup init'i tekrar deneyin.")
            os.replace(temporary, registry_path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    print(f"Hazırlandı (var olan kayıtlar korundu): {root}")


def doctor(root):
    if not board(root).is_dir() or not os.access(board(root), os.W_OK):
        raise ValueError("Ortak pano eksik veya yazılamıyor.")
    for member in MEMBERS:
        for name in ("calisma", "sonuclar_1", "alindi"):
            path = member_dir(root, member) / name
            if not path.is_dir() or not os.access(path, os.W_OK):
                raise ValueError(f"Dizin eksik/yazılamıyor: {path}")
    control = read_json(root / "00_yonetim" / "denetim.json")
    if control.get("durum") not in ("devam", "duraklat"):
        raise ValueError("Geçersiz denetim durumu.")
    registry = read_json(root / "00_yonetim" / "uyeler.json")
    if set(registry) != set(MEMBERS):
        raise ValueError("Üye kaydı eksik veya bilinmeyen üye içeriyor.")
    messages = {}
    for path in sorted(board(root).glob("*.json")):
        messages[path.stem] = message(root, path.stem)
    validate_lineage(messages)
    probe = board(root) / (".divan-probe-" + uuid4().hex)
    try:
        put_new(probe, "atomic-file-check\n")
        if probe.read_text(encoding="utf-8") != "atomic-file-check\n":
            raise ValueError("Atomik dosya yayımlama denetimi başarısız.")
    finally:
        probe.unlink(missing_ok=True)
    print(f"OK: {len(MEMBERS)} üye dizini, atomik dosya yazımı, {len(messages)} geçerli yeni 0 ve girdi zincirleri.")
    print("Bu kontrol dış ürün oturumlarını veya bulutlar arası erişimi doğrulamaz.")


def run(args, root):
    if args.command == "init":
        return init(root)
    if args.command == "doctor":
        return doctor(root)
    if args.command == "status":
        print(json_text({
            "root": str(root),
            "denetim": read_json(root / "00_yonetim" / "denetim.json"),
            "uyeler": read_json(root / "00_yonetim" / "uyeler.json"),
            "yeni_0_sayisi": len(list(board(root).glob("*.json"))),
        }), end="")
    elif args.command == "publish":
        ensure_running(root)
        if bool(args.from_id) != bool(args.from_result):
            raise ValueError("Türetilmiş yeni 0 için --from-id ve --from-result birlikte gerekli.")
        if args.from_id:
            addressed(root, args.member, args.from_id)
        if args.from_result:
            check_id(args.from_result)
            if args.from_id != args.from_result:
                raise ValueError("--from-result, --from-id ile aynı başlangıç girdisini göstermeli.")
            result = member_dir(root, args.member) / "sonuclar_1" / (args.from_result + ".md")
            if not result.is_file():
                raise ValueError("Üyenin bu girdiye ait yerel 1 sonucu yok.")
            receipt = member_dir(root, args.member) / "alindi" / (args.from_result + ".json")
            if not receipt.is_file():
                raise ValueError("Üyenin bu girdiye ait alındı kaydı yok.")
        targets = list(MEMBERS) if args.to == ["all"] else args.to
        if "all" in targets or any(t not in MEMBERS for t in targets):
            raise ValueError("--to için üye kimlikleri veya tek başına all kullanın.")
        body = Path(args.input).read_text(encoding="utf-8")
        ident = uuid4().hex
        data = {"surum": 1, "tur": "yeni_0", "id": ident, "yazar": args.member,
                "hedefler": list(dict.fromkeys(targets)), "olusma_zamani": now(),
                "onceki_girdi": args.from_id, "baslik": args.title,
                "amac": args.purpose, "beklenen_cikti": args.expected, "girdi": body}
        validate(data, ident)
        put_new(board(root) / (ident + ".json"), json_text(data))
        print(ident)
    elif args.command == "inbox":
        for path in sorted(board(root).glob("*.json")):
            data = message(root, path.stem)
            if args.member not in data["hedefler"]:
                continue
            local = member_dir(root, args.member)
            state = "yeni"
            if (local / "alindi" / path.name).exists():
                state = "calisiliyor"
            if (local / "sonuclar_1" / (path.stem + ".md")).exists():
                state = "tamamlandi_1"
            if not args.all and state != "yeni":
                continue
            print(json.dumps({"id": data["id"], "baslik": data["baslik"], "durum": state}, ensure_ascii=False))
    elif args.command == "read":
        print(json_text(message(root, args.id)), end="")
    elif args.command == "claim":
        ensure_running(root)
        addressed(root, args.member, args.id)
        put_new(member_dir(root, args.member) / "alindi" / (args.id + ".json"),
                json_text({"girdi": args.id, "uye": args.member, "zaman": now()}))
        print(f"Alındı: {args.id}")
    elif args.command == "complete":
        addressed(root, args.member, args.id)
        local = member_dir(root, args.member)
        if not (local / "alindi" / (args.id + ".json")).is_file():
            raise ValueError("Önce claim ile işi alın.")
        body = Path(args.input).read_text(encoding="utf-8")
        if not body.strip():
            raise ValueError("Boş sonuç kaydedilemez.")
        path = local / "sonuclar_1" / (args.id + ".md")
        put_new(path, f"# Yerel 1 sonucu\n\nGirdi: {args.id}\nÜye: {args.member}\nTSİ: {now()}\n\n{body}\n")
        print(path)
    elif args.command == "control":
        # Only use in response to an explicit user instruction (see AGENTS.md).
        path = root / "00_yonetim" / "denetim.json"
        data = {"durum": args.state, "aciklama": args.reason, "zaman": now()}
        fd, temp = tempfile.mkstemp(prefix=".denetim-", dir=path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as out:
                out.write(json_text(data))
                out.flush()
                os.fsync(out.fileno())
            os.replace(temp, path)
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
        print(args.state)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(os.environ.get("DIVAN_ROOT", Path(__file__).resolve().parents[1])))
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "doctor", "status"):
        sub.add_parser(name)
    for name in ("publish", "inbox", "claim", "complete"):
        p = sub.add_parser(name)
        p.add_argument("--member", choices=MEMBERS, required=True)
        if name in ("claim", "complete"):
            p.add_argument("id", type=check_id)
        if name in ("publish", "complete"):
            p.add_argument("--input", required=True)
        if name == "publish":
            p.add_argument("--to", nargs="+", required=True)
            p.add_argument("--title", required=True)
            p.add_argument("--purpose", required=True)
            p.add_argument("--expected", required=True)
            p.add_argument("--from-id", type=check_id)
            p.add_argument("--from-result", type=check_id)
        if name == "inbox":
            p.add_argument("--all", action="store_true")
    p = sub.add_parser("read")
    p.add_argument("id", type=check_id)
    p = sub.add_parser("control")
    p.add_argument("--state", choices=("devam", "duraklat"), required=True)
    p.add_argument("--reason", required=True)
    args = parser.parse_args()
    try:
        run(args, args.root.resolve())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"HATA: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
