"""Explicit local commands for durable work and source-backed continuation."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

from .core import Store
from .server import create_server, decode_json, error_response, runtime_status


class JSONArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print_json({"error": {"code": "arguments", "message": message}})
        self.exit(2)


def _words(parser, name="words"):
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--" + name)
    group.add_argument("--" + name + "-file", type=Path)


def _write_args(parser, *, revision=False):
    parser.add_argument("--request-key", required=True,
                        help="Aynı niyetin tekrarında aynı anahtarı kullanın.")
    if revision:
        parser.add_argument("--revision", required=True, type=int)


def parser():
    root = JSONArgumentParser(description="deus_ex_machina — kaynaklı iş ve devamlılık")
    root.add_argument("--state-dir", type=Path,
                      help="Git çalışma ağaçlarının dışında kalıcı özel veri dizini.")
    root.add_argument("--backend", choices=("nt-kernel", "portable"), default="nt-kernel",
                      help="Varsayılan gerçek NT sürücüsü gerektirir; portable açık geliştirme kipidir.")
    sub = root.add_subparsers(dest="command", required=True)
    sub.add_parser("runtime", help="Seçilen çalışma katmanının gerçek durumunu bildir.")
    make = sub.add_parser("create", help="Özgün söz, yetki dayanağı ve ölçütlerle iş oluştur.")
    _words(make)
    make.add_argument("--actor", default="Haluk")
    make.add_argument("--authority-source", required=True)
    make.add_argument("--authority-scope", required=True)
    criteria = make.add_mutually_exclusive_group(required=True)
    criteria.add_argument("--criterion", action="append")
    criteria.add_argument("--criteria-file", type=Path)
    make.add_argument("--source", action="append", type=Path, default=[])
    make.add_argument("--sources-file", type=Path)
    _write_args(make)
    sub.add_parser("list", help="Güncel işleri listele.")
    for name in ("get", "context"):
        p = sub.add_parser(name)
        p.add_argument("task_id")
    p = sub.add_parser("events")
    p.add_argument("--task", dest="task_id")
    p = sub.add_parser("revise", help="Özgün geçmişi koruyarak yeni kullanıcı düzeltmesi ekle.")
    p.add_argument("task_id")
    _words(p)
    _write_args(p, revision=True)
    p = sub.add_parser("control")
    p.add_argument("task_id")
    p.add_argument("action", choices=("pause", "resume", "cancel"))
    _write_args(p, revision=True)
    p = sub.add_parser("assign")
    p.add_argument("task_id")
    p.add_argument("--participant", required=True)
    p.add_argument("--session", dest="session_id", required=True)
    p.add_argument("--expected-active-attempt-id",
                   help="Devretmede mevcut çalıştırma kimliği; eski atamayı sessizce ezmez.")
    _write_args(p, revision=True)
    p = sub.add_parser("receive")
    p.add_argument("attempt_id")
    p.add_argument("--session", dest="session_id", required=True)
    _write_args(p)
    p = sub.add_parser("result")
    p.add_argument("attempt_id")
    p.add_argument("--session", dest="session_id", required=True)
    _words(p, "summary")
    p.add_argument("--artifact", action="append", type=Path, default=[])
    p.add_argument("--artifacts-file", type=Path)
    _write_args(p)
    p = sub.add_parser("verify")
    p.add_argument("task_id")
    p.add_argument("--checks-file", type=Path, required=True)
    _write_args(p, revision=True)
    p = sub.add_parser("export", help="Özel kayıtları yerel JSON olarak dışa aktar.")
    p.add_argument("--output", type=Path)
    p = sub.add_parser("serve", help="Yalnız loopback üzerinde yerel yüzeyi aç.")
    p.add_argument("--port", type=int, default=8765)
    return root


def read_json(path):
    return decode_json(path.read_bytes())


def read_words(args, name="words"):
    file = getattr(args, name + "_file")
    return file.read_bytes().decode("utf-8") if file is not None else getattr(args, name)


def refs(files, json_file):
    values = read_json(json_file) if json_file else []
    if not isinstance(values, list):
        raise ValueError("Kaynak veya çıktı dosyası bir JSON listesi olmalı.")
    return values + [str(file) for file in files]


def print_json(value):
    sys.stdout.write(json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n")
    sys.stdout.flush()


def save_export(path, value):
    path = path.resolve()
    if any((ancestor / ".git").is_file() or (ancestor / ".git" / "HEAD").is_file()
           for ancestor in (path.parent, *path.parent.parents)):
        raise ValueError("Özel dışa aktarım Git çalışma ağacına yazılamaz.")
    data = (json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n").encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    ap = parser()
    args = ap.parse_args(argv)
    if args.command != "runtime" and args.state_dir is None:
        ap.error("Bu komut --state-dir gerektirir.")
    try:
        metadata_stop = args.command == "control" and args.action in {"pause", "cancel"}
        runtime = runtime_status(args.backend, strict=args.command != "runtime" and not metadata_stop)
        if args.command == "runtime":
            print_json({"runtime": runtime})
            return 0 if runtime["ready"] else 1
        if args.command == "serve":
            server = create_server(args.state_dir, backend=args.backend, port=args.port)
            base_url = f"http://127.0.0.1:{server.server_address[1]}"
            print_json({"runtime": runtime, "url": base_url,
                        "launch_url": f"{base_url}/#token={server.token}",
                        "launch_url_scope": "Başlatan kullanıcıya özel erişim bağlantısı; paylaşılacak kayıt değildir.",
                        "authority": "Yerel dosya sahibinin beyanı; bağımsız kimlik doğrulaması değil."})
            try:
                server.serve_forever(poll_interval=0.25)
            except KeyboardInterrupt:
                pass
            finally:
                server.server_close()
            return 0
        store = Store(args.state_dir)
        command = args.command
        if command == "create":
            result = store.create_task(read_words(args),
                {"actor": args.actor, "source": args.authority_source, "scope": args.authority_scope},
                read_json(args.criteria_file) if args.criteria_file else args.criterion,
                args.request_key, sources=refs(args.source, args.sources_file))
        elif command == "list":
            result = {"tasks": store.list_tasks()}
        elif command == "get":
            result = store.get_task(args.task_id)
        elif command == "context":
            result = store.context_bundle(args.task_id)
        elif command == "events":
            result = {"events": store.events(args.task_id)}
        elif command == "revise":
            result = store.revise_task(args.task_id, read_words(args), args.revision, args.request_key)
        elif command == "control":
            result = store.control_task(args.task_id, args.action, args.revision, args.request_key)
        elif command == "assign":
            result = store.assign(args.task_id, args.participant, args.session_id, args.revision, args.request_key,
                                  expected_active_attempt_id=args.expected_active_attempt_id)
        elif command == "receive":
            result = store.receive(args.attempt_id, args.session_id, args.request_key)
        elif command == "result":
            result = store.submit_result(args.attempt_id, args.session_id, read_words(args, "summary"),
                                         refs(args.artifact, args.artifacts_file), args.request_key)
        elif command == "verify":
            result = store.verify_task(args.task_id, read_json(args.checks_file), args.revision, args.request_key)
        elif command == "export":
            result = store.export_data()
            if args.output:
                save_export(args.output, result)
                result = {"export_path": str(args.output.resolve()), "publication": "private_local_export"}
        else:
            raise ValueError("Bilinmeyen komut.")
        print_json({"runtime": runtime, "result": result})
        return 0
    except Exception as error:
        _, code, message = error_response(error)
        print_json({"error": {"code": code, "message": message}})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
