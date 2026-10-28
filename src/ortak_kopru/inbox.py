"""Gelen kutusu: GitHub'daki açık konuları yerel, özel bir dizine indirir.

Konular herkese açıktır ve anahtarsız okunur; ortamdaki bir belirteç bu yolda
kullanılmaz. Her konu, kimin ne zaman yazdığı ve formdaki "yer" alanıyla tek bir
JSON dosyası olur. Dosyalar aktarım dizininin altındaki `gelen/` dizinine
yazılır; o dizin bir Git çalışma ağacının içinde olamaz. İçerik veridir:
çalıştırılmaz, yerel çalışmaya uygulanmaz, var olan bir dosyanın üstüne yazılmaz.
Başlığı ya da gövdesi değişen konu yeni bir dosya olur; önceki hâli kalır. Dosya adı deponun
adını da karmaya katar; aynı aktarım dizini birden çok depoyla kullanılsa da kayıtlar karışmaz.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json

from .local_files import private_path, write_private_file

KIND = "ortak_kopru_gelen"
SCHEMA_VERSION = 1
DIRECTORY = "gelen"
# Karşılık formunun (.github/ISSUE_TEMPLATE/karsilik.yml) alan etiketleri.
FORM_FIELDS = {"tur": "Ne getiriyorsunuz?", "yer": "Hangi yazı, hangi bölüm?"}
_EMPTY = "_No response_"


def form_fields(body):
    """Read the form's answers from an issue body rendered by GitHub."""
    sections, heading, lines = {}, None, []
    for line in body.replace("\r\n", "\n").split("\n") + ["### "]:
        if line.startswith("### "):
            if heading is not None:
                sections.setdefault(heading, "\n".join(lines).strip())
            heading, lines = line[4:].strip(), []
        elif heading is not None:
            lines.append(line)
    result = {}
    for key, label in FORM_FIELDS.items():
        value = sections.get(label, "")
        result[key] = value[:512] if value and value != _EMPTY else None
    return result


def _sha256(value):
    text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def content_digest(issue):
    return _sha256({"title": issue["title"], "body": issue["body"]})


def file_name(repository, issue):
    """Same repository, number and content → same name; anything else → a new file."""
    key = _sha256({"repository": repository, "number": issue["number"],
                   "title": issue["title"], "body": issue["body"]})
    return f"konu-{issue['number']:06d}-{key[:16]}.json"


def collect(exchange_directory, client, repository):
    """Write every new or changed open issue to the private inbox."""
    inbox = private_path(exchange_directory / DIRECTORY)
    inbox.mkdir(mode=0o700, exist_ok=True)
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    new, unchanged = [], 0
    for issue in client.open_issues(repository):
        digest = content_digest(issue)
        name = file_name(repository, issue)
        path = private_path(inbox / name)
        if path.exists():
            unchanged += 1
            continue
        fields = form_fields(issue["body"])
        record = {"kind": KIND, "schema_version": SCHEMA_VERSION, "repository": repository,
                  **issue, **fields, "content_sha256": digest, "fetched_at": fetched_at}
        write_private_file(path, (json.dumps(record, ensure_ascii=False, indent=2,
                                             sort_keys=True) + "\n").encode("utf-8"))
        new.append({"number": issue["number"], "file": name, "author": issue["author"],
                    "yer": fields["yer"]})
    return {"repository": repository, "inbox": str(inbox), "credentials": "none",
            "new": new, "unchanged": unchanged}
