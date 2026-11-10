#!/usr/bin/env python3
"""Exchange only new-0 envelopes over an explicitly invoked Git branch."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from uuid import uuid4

import divan


def git(repo, *args, data=None, env=None):
    return subprocess.run(["git", "-C", str(repo), *args], input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          check=True, env=env).stdout


def remote_snapshot(repo, remote, branch):
    ref = "refs/heads/" + branch
    git(repo, "check-ref-format", ref)
    if not git(repo, "ls-remote", "--exit-code", remote, ref).strip():
        return None
    # Each transfer owns its ref. FETCH_HEAD is shared by all fetch commands in
    # a checkout and cannot identify a particular concurrent transfer.
    private_ref = "refs/divan/transfers/" + uuid4().hex
    try:
        git(repo, "fetch", "--quiet", "--no-tags", "--no-write-fetch-head",
            "--refmap=", remote, ref + ":" + private_ref)
        return git(repo, "rev-parse", "--verify", private_ref + "^{commit}").decode().strip()
    finally:
        git(repo, "update-ref", "-d", private_ref)


def fetch_snapshot(repo, remote, branch):
    try:
        return remote_snapshot(repo, remote, branch)
    except subprocess.CalledProcessError as exc:
        # ls-remote --exit-code returns 2 only when no matching ref exists.
        if exc.returncode == 2 and "ls-remote" in exc.cmd:
            return None
        raise


def import_snapshot(root, repo, commit):
    combined = {path.stem: divan.message(root, path.stem)
                for path in divan.board(root).glob("*.json")}
    if commit is None:
        divan.validate_lineage(combined)
        return 0
    entries = git(repo, "ls-tree", "-rz", "--full-tree", commit).split(b"\0")
    pending = []
    for entry in filter(None, entries):
        meta, path = entry.split(b"\t", 1)
        mode, kind, oid = meta.split()
        name = path.decode("utf-8")
        # Other branch content is not a command or an instruction to execute.
        if not name.startswith("yeni_0/"):
            continue
        ident = name.removeprefix("yeni_0/").removesuffix(".json")
        divan.check_id(ident)
        if name != f"yeni_0/{ident}.json" or mode != b"100644" or kind != b"blob":
            raise ValueError(f"Geçersiz Git paylaşım girdisi: {name}")
        raw = git(repo, "cat-file", "blob", oid.decode())
        data = json.loads(raw)
        divan.validate(data, ident)
        dest = divan.board(root) / (ident + ".json")
        if ident in combined:
            if combined[ident] != data:
                raise ValueError(f"Aynı kimlik için farklı içerik: {ident}")
        else:
            combined[ident] = data
            pending.append((dest, data))
    # Validate the complete local + incoming graph before publishing any files.
    # Remote filename order need not put parents before their children.
    divan.validate_lineage(combined)
    for dest, data in pending:
        try:
            divan.put_new(dest, divan.json_text(data))
        except FileExistsError:
            if divan.read_json(dest) != data:
                raise ValueError(f"Eşzamanlı içerik çakışması: {dest.stem}")
    return len(pending)


def export_snapshot(root, repo, remote, branch, parent):
    divan.ensure_running(root)
    messages = []
    graph = {}
    for path in sorted(divan.board(root).glob("*.json")):
        data = divan.message(root, path.stem)
        graph[path.stem] = data
        messages.append((f"yeni_0/{path.name}", divan.json_text(data).encode()))
    divan.validate_lineage(graph)
    if not messages:
        print("Yayımlanacak yeni 0 yok; uzak dal değiştirilmedi.")
        return
    # An isolated index leaves the checkout, current branch and user's index intact.
    with tempfile.TemporaryDirectory(prefix="divan-index-") as tmp:
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(Path(tmp) / "index")
        env.update({"GIT_AUTHOR_NAME": "Divan Dosya Koprusu",
                    "GIT_AUTHOR_EMAIL": "divan@localhost",
                    "GIT_COMMITTER_NAME": "Divan Dosya Koprusu",
                    "GIT_COMMITTER_EMAIL": "divan@localhost"})
        git(repo, "read-tree", parent if parent else "--empty", env=env)
        for name, raw in messages:
            oid = git(repo, "hash-object", "-w", "--stdin", data=raw, env=env).decode().strip()
            git(repo, "update-index", "--add", "--cacheinfo", "100644", oid, name, env=env)
        tree = git(repo, "write-tree", env=env).decode().strip()
        if parent and tree == git(repo, "rev-parse", parent + "^{tree}").decode().strip():
            print("Git paylaşımı zaten güncel.")
            return
        args = ["commit-tree", tree]
        if parent:
            args += ["-p", parent]
        commit = git(repo, *args, data=b"Divan: yeni 0 girdileri\n", env=env).decode().strip()
        # No force push: concurrent writers must pull and retry, preserving all work.
        git(repo, "push", "--porcelain", remote, commit + ":refs/heads/" + branch, env=env)
        print(f"Yayımlandı: {branch} ({len(messages)} yeni 0 toplamı)")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("pull", "push"))
    p.add_argument("--root", type=Path,
                   default=Path(os.environ.get("DIVAN_ROOT", Path(__file__).resolve().parents[1])))
    p.add_argument("--repo", type=Path, default=Path("/workspace/ortak-kopru"))
    p.add_argument("--remote", default="origin")
    p.add_argument("--branch", default="divan-paylasim")
    args = p.parse_args()
    try:
        if args.remote.startswith("-") or args.branch.startswith("-"):
            raise ValueError("Geçersiz uzak depo/dal adı.")
        root = args.root.resolve()
        repo = args.repo.resolve()
        commit = fetch_snapshot(repo, args.remote, args.branch)
        imported = import_snapshot(root, repo, commit)
        print(f"Alınan yeni 0: {imported}")
        if args.action == "push":
            export_snapshot(root, repo, args.remote, args.branch, commit)
        elif commit is None:
            print("Uzak paylaşım dalı henüz yok; ilk push ile oluşturulabilir.")
    except subprocess.CalledProcessError as exc:
        # Do not print URLs, environment, auth headers or raw transport errors.
        command = next((s for s in exc.cmd[3:] if not s.startswith("-")), "git")
        print(f"HATA: Git {command} başarısız (kod {exc.returncode}). "
              "Ağ/erişim veya eşzamanlı push durumunu kontrol edin. "
              "Push çakışmasında pull yapıp yeniden deneyin.", file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"HATA: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
