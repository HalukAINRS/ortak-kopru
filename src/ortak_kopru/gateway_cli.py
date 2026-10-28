"""Explicit, task-independent file exchange commands.

Only plan/send/reconcile/fetch create a provider client from the environment;
inbox reads public issues with an anonymous client. Local preparation and
inspection need neither a provider credential nor the NT device. Nothing in
this entry point starts the existing task store or executes incoming content.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sqlite3
import sys

from . import gateway, inbox
from .adapters.github import GitHubClient, GitHubError
from .core import CoreError
from .exchange import ExchangeConflict, ExchangeStore
from .local_files import read_regular_file


MAX_SELECTION_BYTES = 1024 * 1024
_SCOPE = {"execution_scope": "user_mode_exchange", "kernel_scope": "not_requested"}


def print_json(value):
    sys.stdout.write(json.dumps({**_SCOPE, **value}, ensure_ascii=False,
                               allow_nan=False, indent=2) + "\n")
    sys.stdout.flush()


class JSONArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # argparse may echo arbitrary option values. In particular, an unknown
        # --token option must not print a credential entered by mistake.
        if message.startswith("the following arguments are required:"):
            detail = message.partition(":")[2].strip()
            message = "Gerekli bağımsız değişkenler eksik: " + detail
        else:
            message = "Komut veya bağımsız değişkenler geçersiz; kullanım için --help."
        print_json({"error": {"code": "arguments", "message": message}})
        self.exit(2)


def parser():
    root = JSONArgumentParser(
        description="Ortak Köprü — seçilmiş paylaşım ve kaynak tedariki")
    root.add_argument("--exchange-dir", type=Path, required=True,
                      help="Görev veritabanından ayrı, Git dışındaki özel aktarım dizini.")
    sub = root.add_subparsers(dest="command", required=True)

    prepare = sub.add_parser("prepare", help="Seçilmiş yerel dosyaları çevrimdışı olarak sabitle.")
    prepare.add_argument("--selection", type=Path, required=True,
                         help="[{source: yerel_yol, path: hedef_yol}] biçiminde UTF-8 JSON dosyası.")
    prepare.add_argument("--repo", dest="repository", required=True,
                         help="GitHub hedefi: sahip/depo.")
    prepare.add_argument("--base", dest="base_ref", default="main",
                         help="Yayın planının temel dalı; etiket/commit yerine dal adı verin.")
    prepare.add_argument("--branch", help="Henüz bulunmayan yayın dalı; verilmezse aktarım kimliğinden türetilir.")
    prepare.add_argument("--purpose", required=True, help="Bu seçilmiş paylaşımın amacı ve kapsamı.")
    prepare.add_argument("--request-key", required=True,
                         help="Aynı niyet ve içerikle tekrarda aynı anahtar.")

    plan = sub.add_parser("plan", help="Uzak sürümü okuyup gönderilecek değişikliği planla; GitHub'a yazmaz.")
    plan.add_argument("transfer_id")
    send = sub.add_parser("send", help="Kaydedilmiş planı yeni GitHub dalına gönder; ana dala birleştirmez.")
    send.add_argument("transfer_id")
    send.add_argument("--plan-hash", required=True,
                      help="plan çıktısındaki result.plan.plan_hash SHA-256 değeri.")
    send.add_argument("--pull-request", action="store_true",
                      help="Yeni yayın dalı için ayrıca taslak pull request oluştur.")
    reconcile = sub.add_parser("reconcile", help="Belirsiz gönderimin uzak sonucunu oku; GitHub'a yazmaz.")
    reconcile.add_argument("transfer_id")

    fetch = sub.add_parser("fetch", help="Seçilmiş GitHub dosyalarını kesin commit'e bağlayarak al.")
    fetch.add_argument("--repo", dest="repository", required=True)
    fetch.add_argument("--ref", required=True, help="Alınacak commit, dal veya etiket.")
    fetch.add_argument("--path", action="append", dest="paths", required=True,
                       help="Depo içindeki dosya yolu; birden çok kez verilebilir.")
    fetch.add_argument("--purpose", required=True)
    fetch.add_argument("--request-key", required=True)

    incoming = sub.add_parser(
        "inbox", help="Açık GitHub konularını anahtarsız oku ve özel gelen kutusuna (gelen/) indir.")
    incoming.add_argument("--repo", dest="repository", required=True, help="GitHub kaynağı: sahip/depo.")

    sub.add_parser("list", help="Kayıtlı aktarımları listele; yeni alan oluşturmaz.")
    for name, help_text in (
        ("show", "Bir aktarımın özel yerel kaydını göster."),
        ("events", "Bir aktarımın yerel olay geçmişini göster."),
        ("verify", "Paketin kayıtlı dosyalarını ve bütünlüğünü yeniden denetle."),
    ):
        command = sub.add_parser(name, help=help_text)
        command.add_argument("transfer_id")
    materialize = sub.add_parser(
        "materialize", help="Yalnız seçilmiş dosyaları inceleme için yeni özel dizine çıkar.")
    materialize.add_argument("transfer_id")
    materialize.add_argument("--output", type=Path, required=True,
                             help="Henüz bulunmayan, Git dışındaki hedef dizin; mevcut dosyalar ezilmez.")
    return root


def read_selection(path):
    def unique_pairs(pairs):
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("Seçimde yinelenen JSON alanı var.")
            value[key] = item
        return value

    def no_constant(_):
        raise ValueError("Seçimde sonlu olmayan JSON sayısı var.")

    raw = read_regular_file(path, maximum=MAX_SELECTION_BYTES)
    selection = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs,
                           parse_constant=no_constant)
    if not isinstance(selection, list) or not selection:
        raise ValueError("Seçim boş olmayan bir JSON listesi olmalı.")
    for item in selection:
        if (not isinstance(item, dict) or set(item) != {"source", "path"}
                or not all(isinstance(item[key], str) and item[key] for key in item)):
            raise ValueError("Her seçim yalnız source ve path metin alanlarını taşımalı.")
    return selection


def error_payload(error):
    if isinstance(error, GitHubError):
        status = getattr(error, "status", None)
        status = status if type(status) is int else None
        ambiguous = getattr(error, "ambiguous", False) is True
        code = getattr(error, "code", "github_error")
        if not isinstance(code, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", code):
            code = "github_error"
        message = "GitHub isteği tamamlanamadı."
        if ambiguous:
            message = "GitHub işleminin sonucu belirsiz; aktarım reconcile ile denetlenmeli."
        elif code == "invalid_input":
            message = "GitHub hedefi veya sürüm alanı geçersiz."
        elif code == "too_many_issues":
            message = "Açık konu sayısı gelen kutusunun bir okumada alabileceğinden fazla."
        elif code == "credentials_required":
            message = "GitHub yazımı için yerel ortamda hizmet erişim bilgisi gerekli."
        elif status in {401, 403}:
            message = "GitHub bu işlem için erişim vermedi; yerel hizmet yetkisini denetleyin."
        elif status == 404:
            message = "GitHub kaynağı bulunamadı veya bu kimlikle erişilemiyor."
        elif status in {409, 422}:
            message = "GitHub hedefi veya sürüm koşulu işlemle uyuşmuyor."
        result = {"code": code, "message": message, "ambiguous": ambiguous}
        if status is not None:
            result["status"] = status
        return result
    if isinstance(error, ExchangeConflict):
        return {"code": "conflict", "message": str(error)}
    if isinstance(error, CoreError):
        return {"code": "invalid_exchange", "message": str(error)}
    if isinstance(error, (UnicodeError, ValueError)):
        return {"code": "invalid_input", "message": "Girdi biçimi veya seçilmiş alanlar geçersiz."}
    if isinstance(error, OSError):
        return {"code": "io_error", "message": "Yerel dosya veya aktarım alanına erişilemedi."}
    if isinstance(error, sqlite3.Error):
        return {"code": "store_error", "message": "Aktarım kaydı okunamadı veya kaydedilemedi."}
    return {"code": "internal_error", "message": "Aktarım komutu tamamlanamadı."}


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    args = parser().parse_args(argv)
    try:
        command = args.command
        selection = read_selection(args.selection) if command == "prepare" else None
        store = ExchangeStore(args.exchange_dir, create=command in {"prepare", "fetch", "inbox"})
        if command == "prepare":
            result = gateway.prepare(
                store, selection, repository=args.repository, base_ref=args.base_ref,
                branch=args.branch, purpose=args.purpose, request_key=args.request_key)
        elif command in {"plan", "send", "reconcile", "fetch"}:
            client = GitHubClient.from_env()
            if command == "plan":
                result = gateway.plan(store, args.transfer_id, client)
            elif command == "send":
                result = gateway.send(
                    store, args.transfer_id, client, expected_plan_hash=args.plan_hash,
                    pull_request=args.pull_request)
            elif command == "reconcile":
                result = gateway.reconcile(store, args.transfer_id, client)
            else:
                result = gateway.fetch(
                    store, client, repository=args.repository, ref=args.ref,
                    paths=args.paths, purpose=args.purpose, request_key=args.request_key)
        elif command == "inbox":
            result = inbox.collect(store.directory, GitHubClient(), args.repository)
        elif command == "list":
            result = {"transfers": store.list_transfers()}
        elif command == "show":
            result = store.get(args.transfer_id)
        elif command == "events":
            result = {"transfer_id": args.transfer_id, "events": store.events(args.transfer_id)}
        elif command == "verify":
            result = store.verify(args.transfer_id)
        elif command == "materialize":
            result = store.materialize(args.transfer_id, args.output)
        else:
            raise ValueError("Bilinmeyen komut.")
        print_json({"result": result})
        if command == "send" and result.get("state") != "published":
            return 1
        if command in {"plan", "reconcile"} and result.get("state") in {"unknown", "failed", "conflict"}:
            return 1
        return 0
    except Exception as error:
        print_json({"error": error_payload(error)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
