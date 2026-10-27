"""Bounded local operations: synthetic Git repositories and real fixed processes."""
import errno
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru import operations  # noqa: E402
from ortak_kopru.operations import MAX_OUTPUT_BYTES, MAX_TIMEOUT_SECONDS, OPERATIONS, run_local  # noqa: E402

GIT = shutil.which("git")
REAL_POPEN = subprocess.Popen


def temporary_root(test, prefix):
    temporary = tempfile.TemporaryDirectory(prefix=prefix, dir="/tmp" if os.name != "nt" else None)
    test.addCleanup(temporary.cleanup)
    return Path(temporary.name).resolve()


def git(cwd, *args):
    env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
    env.update({
        "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull, "GIT_TERMINAL_PROMPT": "0",
        "GIT_AUTHOR_NAME": "Sentetik sınama", "GIT_AUTHOR_EMAIL": "test@example.invalid",
        "GIT_COMMITTER_NAME": "Sentetik sınama", "GIT_COMMITTER_EMAIL": "test@example.invalid",
    })
    return subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True).stdout


def assert_json_ready(test, receipt):
    encoded = json.dumps(receipt, ensure_ascii=False, allow_nan=False).encode("utf-8")
    test.assertEqual(receipt, json.loads(encoded.decode("utf-8")))


class InputContractTests(unittest.TestCase):
    """Rejected input never reaches subprocess creation."""

    def setUp(self):
        self.base = temporary_root(self, "deus-operations-input-")
        self.repo = self.base / "depo"
        (self.repo / ".git").mkdir(parents=True)
        (self.repo / ".git" / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        (self.repo / "alt").mkdir()
        (self.repo / "dosya.txt").write_text("veri\n", encoding="utf-8")
        (self.base / "git-disi").mkdir()
        patcher = mock.patch.object(operations.subprocess, "Popen",
                                    side_effect=AssertionError("Geçersiz istekte süreç başlatılmamalı."))
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_only_named_operations_are_accepted(self):
        for value in ("", "rm", "repo_status ", "REPO_STATUS", "repo_status; rm -rf /",
                      "git status", None, 7, b"repo_status", ["repo_status"]):
            with self.subTest(operation=value), self.assertRaises(ValueError):
                run_local(value, self.repo)

    def test_cwd_must_be_an_explicit_git_working_tree_root(self):
        for value in ("depo", "", self.base / "yok", self.repo / "dosya.txt", self.repo / "alt",
                      self.base / "git-disi", None, True, os.fsencode(str(self.repo)), str(self.repo) + "\0"):
            with self.subTest(cwd=value), self.assertRaises(ValueError):
                run_local("repo_status", value)

    def test_linked_worktree_pointer_is_accepted_as_root(self):
        worktree = self.base / "bagli"
        worktree.mkdir()
        (worktree / ".git").write_text("gitdir: /bir/depo/.git/worktrees/bagli\n", encoding="utf-8")
        self.assertEqual(worktree, operations._repository_root(worktree))
        (worktree / ".git").write_text("bozuk\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            operations._repository_root(worktree)

    def test_limits_are_validated(self):
        for value in (0, -1, float("nan"), float("inf"), True, "10", MAX_TIMEOUT_SECONDS + 1):
            with self.subTest(timeout=value), self.assertRaises(ValueError):
                run_local("repo_status", self.repo, timeout_seconds=value)
        for value in (0, -1, MAX_OUTPUT_BYTES + 1, True, 1.5, "64"):
            with self.subTest(limit=value), self.assertRaises(ValueError):
                run_local("repo_status", self.repo, output_limit=value)

    def test_callers_cannot_add_argv_or_shell(self):
        with self.assertRaises(TypeError):
            run_local("repo_status", self.repo, argv=["rm", "-rf", "/"])
        with self.assertRaises(TypeError):
            run_local("repo_status", self.repo, shell=True)


@unittest.skipUnless(GIT, "git gerekli")
class RepositoryOperationTests(unittest.TestCase):
    def setUp(self):
        self.base = temporary_root(self, "deus-operations-")
        self.home = self.base / "ev"
        self.home.mkdir()
        # The child keeps HOME for the owner's git config; tests give it an empty one.
        patcher = mock.patch.dict(os.environ, {"HOME": str(self.home), "USERPROFILE": str(self.home),
                                               "XDG_CONFIG_HOME": str(self.home)})
        patcher.start()
        self.addCleanup(patcher.stop)
        self.repo = self.make_repo("depo", {"izlenen.txt": "ilk\n", "sabit.txt": "değişmeyecek\n"})
        self.head = git(self.repo, "rev-parse", "HEAD").decode("ascii").strip()

    def make_repo(self, name, files):
        repo = self.base / name
        repo.mkdir()
        git(repo, "init", "-q")
        for path, text in files.items():
            (repo / path).write_text(text, encoding="utf-8")
        if files:
            git(repo, "add", *files)
            git(repo, "commit", "-q", "-m", "sentetik başlangıç")
        return repo

    def test_repo_revision_records_the_real_head(self):
        receipt = run_local("repo_revision", self.repo)
        self.assertEqual("completed", receipt["status"])
        self.assertEqual(0, receipt["exit_code"])
        self.assertIsNone(receipt["error"])
        self.assertEqual(self.head, receipt["stdout"]["text"].strip())
        raw = receipt["stdout"]["text"].encode("utf-8")
        self.assertEqual({"text": receipt["stdout"]["text"], "captured_bytes": len(raw),
                          "sha256": hashlib.sha256(raw).hexdigest(), "truncated": False}, receipt["stdout"])
        self.assertTrue(Path(receipt["argv"][0]).is_absolute())
        self.assertEqual(list(OPERATIONS["repo_revision"][1:]), receipt["argv"][1:])
        self.assertEqual(str(self.repo), receipt["cwd"])
        self.assertEqual({"system", "release", "machine", "python_implementation", "python_version"},
                         set(receipt["platform"]))
        self.assertLessEqual(receipt["started_at"], receipt["finished_at"])
        self.assertIsInstance(receipt["duration_ms"], int)
        self.assertEqual(("user_mode", "not_requested"), (receipt["execution_scope"], receipt["kernel_scope"]))
        assert_json_ready(self, receipt)

    def test_repo_status_reports_changes_without_rewriting_the_index(self):
        (self.repo / "izlenen.txt").write_text("değişti\n", encoding="utf-8")
        (self.repo / "yeni.txt").write_text("izlenmiyor\n", encoding="utf-8")
        # Same bytes, newer mtime: an ordinary status would refresh and rewrite the index.
        unchanged = self.repo / "sabit.txt"
        stamp = unchanged.stat().st_mtime_ns + 5_000_000_000
        os.utime(unchanged, ns=(stamp, stamp))
        index = self.repo / ".git" / "index"
        before = index.read_bytes()

        receipt = run_local("repo_status", self.repo)

        self.assertEqual("completed", receipt["status"])
        lines = receipt["stdout"]["text"].splitlines()
        self.assertTrue(lines[0].startswith("## "))
        self.assertIn(" M izlenen.txt", lines)
        self.assertIn("?? yeni.txt", lines)
        self.assertNotIn("sabit.txt", receipt["stdout"]["text"])
        self.assertEqual(before, index.read_bytes())
        git(self.repo, "status", "--porcelain")
        self.assertNotEqual(before, index.read_bytes(), "Kontrol: olağan status bu dizinde index'i yeniler.")
        assert_json_ready(self, receipt)

    def test_failure_keeps_the_real_exit_code_and_stderr(self):
        empty = self.make_repo("bos", {})
        receipt = run_local("repo_revision", empty)
        self.assertEqual("failed", receipt["status"])
        self.assertNotIn(receipt["exit_code"], (None, 0))
        self.assertEqual(0, receipt["stdout"]["captured_bytes"])
        self.assertGreater(receipt["stderr"]["captured_bytes"], 0)
        self.assertIsNone(receipt["error"])
        assert_json_ready(self, receipt)

    def test_parent_git_routing_and_credentials_do_not_reach_the_child(self):
        other = self.make_repo("baska", {"baska.txt": "başka depo\n"})
        calls = []

        def recording_popen(*args, **kwargs):
            calls.append((args, kwargs))
            return REAL_POPEN(*args, **kwargs)

        planted = {"GIT_DIR": str(other / ".git"), "GIT_WORK_TREE": str(other),
                   "GIT_INDEX_FILE": str(other / ".git" / "index"),
                   "GH_TOKEN": "sentetik-deger", "GITHUB_TOKEN": "sentetik-deger",
                   "ORTAK_KOPRU_GITHUB_TOKEN": "sentetik-deger", "ANTHROPIC_API_KEY": "sentetik-deger",
                   "OPENAI_API_KEY": "sentetik-deger", "GEMINI_API_KEY": "sentetik-deger"}
        with mock.patch.dict(os.environ, planted), \
                mock.patch.object(operations.subprocess, "Popen", side_effect=recording_popen):
            receipt = run_local("repo_revision", self.repo)
        self.assertEqual(self.head, receipt["stdout"]["text"].strip())
        (argv,), kwargs = calls[0]
        self.assertEqual(receipt["argv"], argv)
        self.assertIs(False, kwargs["shell"])
        self.assertEqual(subprocess.DEVNULL, kwargs["stdin"])
        self.assertEqual(self.repo, Path(kwargs["cwd"]))
        env = {key.upper(): value for key, value in kwargs["env"].items()}
        self.assertFalse(set(planted) & set(env))
        self.assertEqual(("0", "0"), (env["GIT_OPTIONAL_LOCKS"], env["GIT_TERMINAL_PROMPT"]))

    def test_python_version_uses_the_running_interpreter(self):
        receipt = run_local("python_version", self.repo)
        self.assertEqual("completed", receipt["status"])
        self.assertEqual([sys.executable, "--version"], receipt["argv"])
        self.assertIn(platform.python_version(), receipt["stdout"]["text"] + receipt["stderr"]["text"])

    def test_missing_git_is_a_spawn_error_without_a_process(self):
        empty_path = self.base / "bos-path"
        empty_path.mkdir()
        with mock.patch.dict(os.environ, {"PATH": str(empty_path)}), \
                mock.patch.object(operations.subprocess, "Popen", side_effect=AssertionError("başlatılmamalı")):
            receipt = run_local("repo_status", self.repo)
        self.assertEqual("spawn_error", receipt["status"])
        self.assertIsNone(receipt["exit_code"])
        self.assertIn("git", receipt["error"])
        self.assertEqual(list(OPERATIONS["repo_status"]), receipt["argv"])
        for name in ("stdout", "stderr"):
            self.assertEqual({"text": "", "captured_bytes": 0, "sha256": hashlib.sha256(b"").hexdigest(),
                              "truncated": False}, receipt[name])
        assert_json_ready(self, receipt)

    def test_start_failure_is_recorded_as_spawn_error(self):
        denied = OSError(errno.EACCES, "Erişim reddedildi")
        with mock.patch.object(operations.subprocess, "Popen", side_effect=denied):
            receipt = run_local("repo_status", self.repo)
        self.assertEqual("spawn_error", receipt["status"])
        self.assertIsNone(receipt["exit_code"])
        self.assertIn("Erişim reddedildi", receipt["error"])


@unittest.skipUnless(os.name == "posix" and " " not in sys.executable,
                     "Sahte git süreçleri POSIX betik başlığı gerektirir.")
class BoundedProcessTests(unittest.TestCase):
    """A synthetic `git` on PATH drives the real capture, limit and timeout paths."""

    def setUp(self):
        self.base = temporary_root(self, "deus-operations-bounds-")
        self.repo = self.base / "depo"
        (self.repo / ".git").mkdir(parents=True)
        (self.repo / ".git" / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        self.bin = self.base / "bin"
        self.bin.mkdir()
        patcher = mock.patch.dict(os.environ, {"PATH": str(self.bin) + os.pathsep + os.environ.get("PATH", "")})
        patcher.start()
        self.addCleanup(patcher.stop)

    def fake_git(self, body):
        script = self.bin / "git"
        script.write_text(f"#!{sys.executable}\nimport os, sys, time, json, subprocess\n{body}\n", encoding="utf-8")
        script.chmod(0o755)

    def test_stdout_is_bounded_while_the_process_still_writes(self):
        self.fake_git("chunk = b'x' * 65536\nwhile True:\n    sys.stdout.buffer.write(chunk)\n    sys.stdout.buffer.flush()")
        receipt = run_local("repo_status", self.repo, timeout_seconds=30, output_limit=1024)
        self.assertEqual("output_limit", receipt["status"])
        self.assertEqual({"text": "x" * 1024, "captured_bytes": 1024,
                          "sha256": hashlib.sha256(b"x" * 1024).hexdigest(), "truncated": True}, receipt["stdout"])
        self.assertEqual(0, receipt["stderr"]["captured_bytes"])
        self.assertLess(receipt["exit_code"], 0, "Sınır aşılınca süreç durdurulmalı.")
        self.assertLess(receipt["duration_ms"], 10_000)
        assert_json_ready(self, receipt)

    def test_stderr_has_its_own_bound(self):
        self.fake_git("sys.stdout.write('on bayt!!\\n')\nsys.stdout.flush()\n"
                      "while True:\n    sys.stderr.buffer.write(b'e' * 65536)\n    sys.stderr.buffer.flush()")
        receipt = run_local("repo_revision", self.repo, output_limit=2048)
        self.assertEqual("output_limit", receipt["status"])
        self.assertEqual(("on bayt!!\n", False), (receipt["stdout"]["text"], receipt["stdout"]["truncated"]))
        self.assertEqual((2048, True), (receipt["stderr"]["captured_bytes"], receipt["stderr"]["truncated"]))

    def test_timeout_stops_the_process_and_its_helpers(self):
        pids = self.base / "pids.json"
        self.fake_git(
            "helper = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
            f"open({str(pids)!r}, 'w').write(json.dumps([os.getpid(), helper.pid]))\n"
            "time.sleep(60)")
        # Without a group kill the helper keeps the pipes open until this drain limit.
        with mock.patch.object(operations, "_DRAIN_SECONDS", 30):
            receipt = run_local("repo_status", self.repo, timeout_seconds=2)
        self.assertEqual("timeout", receipt["status"])
        self.assertLess(receipt["exit_code"], 0)
        self.assertLess(receipt["duration_ms"], 10_000)
        self.assertIn("Süre sınırı", receipt["error"])
        child, helper = json.loads(pids.read_text(encoding="utf-8"))
        with self.assertRaises(ProcessLookupError):
            os.kill(child, 0)
        stat = Path(f"/proc/{helper}/stat")
        if stat.exists():
            self.assertIn(stat.read_text().rsplit(")", 1)[1].split()[0], {"Z", "X"})

    def test_clean_exit_with_a_helper_holding_the_pipes_is_not_success(self):
        pids = self.base / "pids.json"
        self.fake_git(
            "helper = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
            f"open({str(pids)!r}, 'w').write(json.dumps([os.getpid(), helper.pid]))\n"
            "print('ust surec bitti', flush=True)\n"
            "sys.exit(0)")
        with mock.patch.object(operations, "_DRAIN_SECONDS", 0.5):
            receipt = run_local("repo_status", self.repo)
        self.assertEqual((0, "failed"), (receipt["exit_code"], receipt["status"]))
        self.assertEqual("ust surec bitti\n", receipt["stdout"]["text"])
        self.assertEqual((True, True), (receipt["stdout"]["truncated"], receipt["stderr"]["truncated"]))
        self.assertIn("süreç grubu sonlandırıldı", receipt["error"])
        self.assertIn("Çıktı eksik", receipt["error"])
        self.assertLess(receipt["duration_ms"], 10_000)
        _, helper = json.loads(pids.read_text(encoding="utf-8"))
        stat = Path(f"/proc/{helper}/stat")
        if stat.exists():
            self.assertIn(stat.read_text().rsplit(")", 1)[1].split()[0], {"Z", "X"})
        assert_json_ready(self, receipt)

    def test_invalid_utf8_and_exit_code_are_preserved(self):
        self.fake_git("sys.stdout.buffer.write(b'ok\\xff\\xfe\\n')\nsys.stderr.buffer.write(b'hata\\xc3(\\n')\nsys.exit(3)")
        receipt = run_local("repo_status", self.repo)
        self.assertEqual(("failed", 3), (receipt["status"], receipt["exit_code"]))
        self.assertEqual(hashlib.sha256(b"ok\xff\xfe\n").hexdigest(), receipt["stdout"]["sha256"])
        self.assertEqual(5, receipt["stdout"]["captured_bytes"])
        self.assertEqual("ok\\xff\\xfe\n", receipt["stdout"]["text"])
        self.assertEqual("hata\\xc3(\n", receipt["stderr"]["text"])
        assert_json_ready(self, receipt)

    def test_git_is_found_only_in_absolute_path_entries(self):
        self.fake_git("sys.exit(0)")
        self.assertEqual(str(self.bin / "git"), operations._find("git", str(self.bin)))
        self.assertIsNone(operations._find("git", os.path.relpath(self.bin)))
        self.assertIsNone(operations._find("git", ""))

    def test_the_child_receives_only_the_fixed_argv(self):
        seen = self.base / "seen.json"
        self.fake_git(f"open({str(seen)!r}, 'w').write(json.dumps({{'argv': sys.argv[1:], "
                      "'locks': os.environ.get('GIT_OPTIONAL_LOCKS'), 'git_dir': os.environ.get('GIT_DIR')}))")
        with mock.patch.dict(os.environ, {"GIT_DIR": str(self.base)}):
            receipt = run_local("repo_status", self.repo)
        self.assertEqual("completed", receipt["status"])
        self.assertEqual({"argv": list(OPERATIONS["repo_status"][1:]), "locks": "0", "git_dir": None},
                         json.loads(seen.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
