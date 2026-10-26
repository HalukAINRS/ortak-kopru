"""Offline integration tests: temporary Git remotes/worktrees and a fake CLI.

No network, installed Codex, existing user repository, or global Git config is used.
The fake CLI is a Python fixture; Windows/WinPE's actual Codex binary is not tested.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

MODULE_PATH = Path(__file__).with_name("saman_devral.py")
spec = importlib.util.spec_from_file_location("saman_devral_under_test", MODULE_PATH)
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class SamanLauncherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="saman-devir-test-")
        # Windows TEMP may use an 8.3 alias; the launcher resolves paths before
        # dispatch and recording. Build every fixture from that same full path.
        self.root = Path(self.temp.name).resolve()
        self.origin = self.root / "origin.git"
        self.seed = self.root / "seed"
        self.repo = self.root / "kaynak Şaman"
        self.target = self.root / "devam alanı Şaman"
        self.capture = self.root / "fake-cli-output.json"
        self.fake = self.root / "codex sahte Şaman.py"
        self.fake.write_text(
            "#!/usr/bin/env python3\n"
            "import json, os, sys\n"
            "from pathlib import Path\n"
            "Path(os.environ['SAMAN_TEST_CAPTURE']).write_text(json.dumps({\n"
            " 'args': sys.argv[1:], 'cwd': os.getcwd(),\n"
            " 'home': os.environ.get('HOME'), 'codex_home': os.environ.get('CODEX_HOME'),\n"
            " 'handoff_state': os.environ.get('SAMAN_DEVIR_STATE'),\n"
            " 'test_value': os.environ.get('SAMAN_TEST_VALUE'),\n"
            " 'openai_key_present': 'OPENAI_API_KEY' in os.environ,\n"
            " 'codex_key_present': 'CODEX_API_KEY' in os.environ,\n"
            "}, ensure_ascii=False), encoding='utf-8')\n",
            encoding="utf-8",
        )
        self.fake.chmod(0o700)
        self.real_run = subprocess.run
        self.git(self.root, "init", "--bare", "--quiet", str(self.origin))
        self.git(self.root, "init", "--quiet", "--initial-branch=main", str(self.seed))
        self.git(self.seed, "config", "user.name", "Offline Fixture")
        self.git(self.seed, "config", "user.email", "fixture@example.invalid")
        config = {
            "katilimcilar": [{
                "ad": "ChatGPT", "saglayici": "cli",
                "komut": [str(self.fake), "exec", "--legacy-flag", "-"],
                "ortam": {
                    "HOME": str(self.root / "private-home"),
                    "USERPROFILE": str(self.root / "private-home"),
                    "CODEX_HOME": str(self.root / "private-home" / ".codex"),
                    "OPENAI_API_KEY": None, "CODEX_API_KEY": None,
                    "SAMAN_TEST_CAPTURE": str(self.capture),
                    "SAMAN_TEST_VALUE": "yalnız çocuk süreç",
                },
            }],
        }
        (self.seed / "ayarlar-yerel.json").write_text(json.dumps(config), encoding="utf-8")
        (self.seed / "README.md").write_text("Existing project.\n", encoding="utf-8")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "--quiet", "-m", "existing main")
        self.git(self.seed, "remote", "add", "origin", str(self.origin))
        self.git(self.seed, "push", "--quiet", "origin", "main")
        self.git(self.origin, "symbolic-ref", "HEAD", "refs/heads/main")
        self.git(self.seed, "checkout", "--quiet", "-b", launcher.HANDOFF_BRANCH)
        contents = {
            "AGENTS.md": "Şaman devir yönergesi.\n",
            "devir/saman/CLI_BASLANGIC.md": "Özgün kaynakları oku ve devam et.\n",
            "devir/saman/GORUNUR_KONUSMA.md": "Kullanıcının görünür sözleri.\n",
            "devir/saman/DEVIR.md": "Sabit devir kapsamı.\n",
        }
        entries = []
        for relative, text in contents.items():
            path = self.seed / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            data = text.encode("utf-8")
            path.write_bytes(data)
            entries.append({"path": relative, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        (self.seed / launcher.MANIFEST_PATH).write_text(json.dumps({"files": entries}), encoding="utf-8")
        self.git(self.seed, "add", ".")
        self.git(self.seed, "commit", "--quiet", "-m", "fixed handoff")
        self.pin = self.git(self.seed, "rev-parse", "HEAD")
        self.git(self.seed, "push", "--quiet", "origin", launcher.HANDOFF_BRANCH)
        self.git(self.root, "clone", "--quiet", str(self.origin), str(self.repo))
        (self.repo / "README.md").write_text("User's existing uncommitted edit.\n", encoding="utf-8")
        (self.repo / "untouched.txt").write_text("User's existing untracked file.\n", encoding="utf-8")
        self.original_head = self.git(self.repo, "rev-parse", "HEAD")
        self.original_status = self.git(self.repo, "status", "--porcelain=v1")
        self.launch_calls = []

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args):
        result = self.real_run(
            ["git", "-C", str(repo), *args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
        )
        return result.stdout.decode("utf-8").strip()

    def invoke(self, *args):
        out, err = io.StringIO(), io.StringIO()

        def dispatch(command, *positional, **keyword):
            if command and str(command[0]) == str(self.fake):
                self.launch_calls.append({
                    "command": list(command), "cwd": keyword.get("cwd"),
                    "env": dict(keyword.get("env", {})),
                })
                # A portable executable fixture. The observed production call
                # remains [exe, prompt]; Python hosts only this fake process.
                return self.real_run([sys.executable, *command], *positional, **keyword)
            return self.real_run(command, *positional, **keyword)

        with mock.patch.object(launcher, "HANDOFF_COMMIT", self.pin):
            with mock.patch.object(launcher.subprocess, "run", side_effect=dispatch):
                with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                    result = launcher.main(["--repo", str(self.repo), "--hedef", str(self.target), *args])
        return result, out.getvalue(), err.getvalue()

    def assert_source_unchanged(self):
        self.assertEqual(self.git(self.repo, "rev-parse", "HEAD"), self.original_head)
        self.assertEqual(self.git(self.repo, "status", "--porcelain=v1"), self.original_status)
        self.assertEqual(self.git(self.repo, "branch", "--show-current"), "main")
        self.assertEqual((self.repo / "README.md").read_text(), "User's existing uncommitted edit.\n")
        self.assertEqual((self.repo / "untouched.txt").read_text(), "User's existing untracked file.\n")

    def status(self):
        files = list((self.repo / ".git" / "saman-devir").glob("*.json"))
        self.assertEqual(len(files), 1)
        return files[0], json.loads(files[0].read_text(encoding="utf-8"))

    def test_import_is_inert_and_unpinned_copy_fails_before_git(self):
        fresh_spec = importlib.util.spec_from_file_location("inert_saman", MODULE_PATH)
        fresh = importlib.util.module_from_spec(fresh_spec)
        with mock.patch.object(subprocess, "run", side_effect=AssertionError("unexpected process")):
            fresh_spec.loader.exec_module(fresh)
            # Bu test, yayın sırasında gerçek pin yerleştirildikten sonra da
            # geçerli kalır; yalnız bu import kopyasını sabitlenmemiş yapar.
            fresh.HANDOFF_COMMIT = "__HANDOFF_COMMIT__"
            with contextlib.redirect_stderr(io.StringIO()) as err:
                self.assertEqual(fresh.main(["--repo", str(self.repo), "--hazirla"]), 2)
        self.assertIn("sabitlenmemiş", err.getvalue())
        self.assertFalse(self.target.exists())

    def test_prepare_creates_worktree_without_launch_or_source_changes(self):
        result, out, err = self.invoke("--hazirla")
        self.assertEqual((result, err), (0, ""))
        self.assertFalse(self.capture.exists())
        self.assertEqual(self.launch_calls, [])
        self.assertEqual(self.git(self.target, "rev-parse", "HEAD"), self.pin)
        self.assertEqual(self.git(self.target, "branch", "--show-current"), launcher.DEFAULT_LOCAL_BRANCH)
        self.assertEqual(self.git(self.target, "status", "--porcelain=v1"), "")
        self.assertIn("CLI açılmadı", out)
        _, state = self.status()
        self.assertEqual(state["preparation"], "verified")
        self.assertFalse(state["reading_observed_by_launcher"])
        self.assertFalse(state["acceptance_observed_by_launcher"])
        self.assertEqual(state["cli"]["state"], "not_started")
        self.assert_source_unchanged()

    def test_launch_uses_exact_interactive_command_cwd_and_child_environment(self):
        parent_snapshot = os.environ.copy()
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": "fixture-only", "CODEX_API_KEY": "fixture-only"}):
            before = os.environ.copy()
            result, _, err = self.invoke()
            self.assertEqual(os.environ.copy(), before)
        self.assertEqual(os.environ.copy(), parent_snapshot)
        self.assertEqual((result, err), (0, ""))
        self.assertEqual(len(self.launch_calls), 1)
        call = self.launch_calls[0]
        self.assertEqual(len(call["command"]), 2)
        self.assertEqual(call["command"][0], str(self.fake))
        for source in launcher.REQUIRED_FILES:
            self.assertIn(source, call["command"][1])
        self.assertNotIn("--legacy-flag", call["command"][1])
        self.assertEqual(call["cwd"], str(self.target))
        actual = json.loads(self.capture.read_text(encoding="utf-8"))
        self.assertEqual(actual["args"], [call["command"][1]])
        self.assertEqual(actual["cwd"], str(self.target))
        self.assertEqual(actual["home"], str(self.root / "private-home"))
        self.assertEqual(actual["codex_home"], str(self.root / "private-home" / ".codex"))
        self.assertEqual(actual["test_value"], "yalnız çocuk süreç")
        self.assertFalse(actual["openai_key_present"])
        self.assertFalse(actual["codex_key_present"])
        _, state = self.status()
        self.assertEqual(state["cli"]["state"], "process_exited")
        self.assertEqual(state["cli"]["returncode"], 0)
        self.assertFalse(state["reading_observed_by_launcher"])
        state_path, _ = self.status()
        self.assertEqual(actual["handoff_state"], str(state_path))
        self.assert_source_unchanged()

    def test_windows_autocrlf_setting_cannot_rewrite_fixed_package_or_config(self):
        self.git(self.repo, "config", "core.autocrlf", "true")
        config = (self.repo / ".git" / "config").read_bytes()
        result, _, err = self.invoke("--hazirla")
        self.assertEqual((result, err), (0, ""))
        self.assertEqual((self.repo / ".git" / "config").read_bytes(), config)
        for item in launcher.REQUIRED_FILES:
            self.assertNotIn(b"\r\n", (self.target / item).read_bytes())
        self.assert_source_unchanged()

    def test_rerun_accepts_descendant_and_keeps_dirty_and_progress_files(self):
        self.assertEqual(self.invoke("--hazirla")[0], 0)
        (self.target / "notes.md").write_text("Committed progress.\n", encoding="utf-8")
        self.git(self.target, "add", "notes.md")
        self.git(
            self.target, "-c", "user.name=Offline Fixture", "-c", "user.email=fixture@example.invalid",
            "commit", "--quiet", "-m", "continue task",
        )
        head = self.git(self.target, "rev-parse", "HEAD")
        (self.target / "README.md").write_text("Keep this edit.\n", encoding="utf-8")
        progress = self.target / "devir/saman/DEVAM_DURUMU.json"
        progress.write_text('{"read_by_saman": false}\n', encoding="utf-8")
        before = self.git(self.target, "status", "--porcelain=v1")
        result, out, err = self.invoke("--hazirla")
        self.assertEqual((result, err), (0, ""))
        self.assertIn("doğrulandı", out)
        self.assertEqual(self.git(self.target, "rev-parse", "HEAD"), head)
        self.assertEqual(self.git(self.target, "status", "--porcelain=v1"), before)
        self.assertEqual(progress.read_text(), '{"read_by_saman": false}\n')
        self.assertEqual((self.target / "README.md").read_text(), "Keep this edit.\n")
        self.assert_source_unchanged()

    def test_modified_package_and_manifest_cannot_bypass_pin(self):
        self.assertEqual(self.invoke("--hazirla")[0], 0)
        package = self.target / "AGENTS.md"
        original = package.read_bytes()
        package.write_text("changed", encoding="utf-8")
        result, _, err = self.invoke()
        self.assertEqual(result, 2)
        self.assertIn("Sabit devir dosyası değişmiş", err)
        self.assertEqual(package.read_text(), "changed")
        self.assertFalse(self.capture.exists())
        package.write_bytes(original)
        manifest = self.target / launcher.MANIFEST_PATH
        manifest.write_text('{"files":[]}', encoding="utf-8")
        result, _, err = self.invoke()
        self.assertEqual(result, 2)
        self.assertIn("MANIFESTO.json sabit commit'ten farklı", err)
        self.assertEqual(manifest.read_text(), '{"files":[]}')
        self.assertFalse(self.capture.exists())
        self.assert_source_unchanged()

    def test_missing_registered_worktree_is_not_pruned_or_recreated(self):
        self.assertEqual(self.invoke("--hazirla")[0], 0)
        shutil.rmtree(self.target)
        result, _, err = self.invoke("--hazirla")
        self.assertEqual(result, 2)
        self.assertIn("eski worktree kaydı", err)
        self.assertFalse(self.target.exists())
        registered_paths = [
            Path(field[len("worktree "):]).resolve()
            for field in self.git(self.repo, "worktree", "list", "--porcelain", "-z").split("\0")
            if field.startswith("worktree ")
        ]
        self.assertIn(self.target.resolve(), registered_paths)
        self.assert_source_unchanged()

    def test_wrong_branch_is_not_checked_out(self):
        self.assertEqual(self.invoke("--hazirla")[0], 0)
        self.git(self.target, "checkout", "--quiet", "-b", "another-task")
        result, _, err = self.invoke("--hazirla")
        self.assertEqual(result, 2)
        self.assertIn("beklenen yerel dalda değil", err)
        self.assertEqual(self.git(self.target, "branch", "--show-current"), "another-task")
        self.assert_source_unchanged()

    def test_registered_path_replaced_by_foreign_git_dir_is_rejected(self):
        self.assertEqual(self.invoke("--hazirla")[0], 0)
        (self.target / ".git").unlink()
        self.git(self.root, "init", "--quiet", "--initial-branch=foreign", str(self.target))
        result, _, err = self.invoke("--hazirla")
        self.assertEqual(result, 2)
        self.assertIn("başka bir Git common-dir", err)
        self.assertTrue((self.target / ".git").is_dir())
        self.assert_source_unchanged()

    def test_missing_executable_is_clear_and_does_not_create_worktree(self):
        result, _, err = self.invoke("--codex", str(self.root / "missing-codex.exe"))
        self.assertEqual(result, 2)
        self.assertIn("Codex çalıştırılabilir dosyası bulunamadı", err)
        self.assertFalse(self.target.exists())
        self.assert_source_unchanged()

    def test_prepare_succeeds_without_installed_codex_but_launch_still_fails(self):
        self.fake.unlink()
        result, out, err = self.invoke("--hazirla")
        self.assertEqual((result, err), (0, ""))
        self.assertIn("CLI açılmadı", out)
        self.assertTrue((self.target / launcher.MANIFEST_PATH).is_file())
        self.assertEqual(self.git(self.target, "rev-parse", "HEAD"), self.pin)
        before = self.git(self.target, "status", "--porcelain=v1")
        result, _, err = self.invoke()
        self.assertEqual(result, 2)
        self.assertIn("Codex çalıştırılabilir dosyası bulunamadı", err)
        self.assertEqual(self.git(self.target, "status", "--porcelain=v1"), before)
        self.assertEqual(self.launch_calls, [])
        self.assertFalse(self.capture.exists())
        self.assert_source_unchanged()

    def test_pin_must_belong_to_expected_remote_branch(self):
        self.git(self.seed, "checkout", "--quiet", "--orphan", "unrelated")
        self.git(self.seed, "rm", "--quiet", "-r", "--cached", ".")
        self.git(self.seed, "commit", "--quiet", "--allow-empty", "-m", "unrelated")
        self.pin = self.git(self.seed, "rev-parse", "HEAD")
        self.git(self.seed, "push", "--quiet", "origin", "unrelated")
        self.git(self.repo, "fetch", "--quiet", "origin", "unrelated")
        result, _, err = self.invoke("--hazirla")
        self.assertEqual(result, 2)
        self.assertIn("beklenen origin dalının atası değil", err)
        self.assertFalse(self.target.exists())
        self.assert_source_unchanged()

    def test_optional_zip_is_hashed_and_path_only_written_to_private_git_status(self):
        archive = self.root / "private source.zip"
        archive.write_bytes(b"offline source fixture")
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        with mock.patch.object(launcher, "SOURCE_ZIP_SIZE", archive.stat().st_size):
            with mock.patch.object(launcher, "SOURCE_ZIP_SHA256", digest):
                result, _, err = self.invoke("--hazirla", "--kaynak-zip", str(archive))
                self.assertEqual((result, err), (0, ""))
                path, state = self.status()
                self.assertEqual(state["source_zip"]["path"], str(archive))
                self.assertEqual(state["source_zip"]["sha256"], digest)
                self.assertTrue(state["source_zip_checked_this_run"])
                self.assertTrue(path.is_relative_to(self.repo / ".git"))
                self.assertEqual(self.git(self.target, "status", "--porcelain=v1"), "")
                for relative in self.git(self.target, "ls-files").splitlines():
                    self.assertNotIn(str(archive).encode(), (self.target / relative).read_bytes())
                self.assertEqual(self.invoke("--hazirla")[0], 0)
                _, repeated = self.status()
                self.assertEqual(repeated["source_zip"], state["source_zip"])
                self.assertFalse(repeated["source_zip_checked_this_run"])
                archive.write_bytes(b"wrong contents")
                result, _, err = self.invoke("--hazirla", "--kaynak-zip", str(archive))
                self.assertEqual(result, 2)
                self.assertIn("ZIP boyutu", err)
        self.assert_source_unchanged()


if __name__ == "__main__":
    unittest.main()

