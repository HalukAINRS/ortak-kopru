"""Black-box Git exchange checks with two peers and an isolated local remote."""
import json
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest import mock


BIN = Path(__file__).resolve().parents[1] / "bin"


def load_transport():
    # The production command imports divan.py from its adjacent bin directory.
    # Mirror that search only while loading the real implementation under test.
    sys.path.insert(0, str(BIN))
    try:
        spec = importlib.util.spec_from_file_location("divan_transport_test", BIN / "divan_git.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


class GitExchangeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="divan-git-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.remote = self.base / "remote.git"
        self.shell("git", "init", "--bare", str(self.remote))
        self.peers = []
        for name in ("a", "b"):
            repo = self.base / name / "repo"
            root = self.base / name / "divan"
            repo.mkdir(parents=True)
            self.shell("git", "-C", str(repo), "init", "--initial-branch=main")
            self.git(repo, "config", "user.name", "Local Test")
            self.git(repo, "config", "user.email", "local-test@localhost")
            (repo / "tracked.txt").write_text("original\n", encoding="utf-8")
            self.git(repo, "add", "tracked.txt")
            self.git(repo, "commit", "-m", "Local initial")
            self.git(repo, "remote", "add", "origin", str(self.remote))
            self.flow(root, "init")
            self.peers.append((repo, root))
        self.body = self.base / "body.md"
        self.body.write_text("Yeni çalışma girdisi.\n", encoding="utf-8")

    def shell(self, *args, ok=True, input=None):
        result = subprocess.run(args, text=True, capture_output=True, timeout=20, input=input)
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def git(self, repo, *args):
        return self.shell("git", "-C", str(repo), *args).stdout.strip()

    def flow(self, root, *args):
        return self.shell(sys.executable, str(BIN / "divan.py"), "--root", str(root), *args).stdout.strip()

    def exchange(self, peer, action, ok=True, branch=None):
        repo, root = self.peers[peer]
        extra = ["--branch", branch] if branch else []
        return self.shell(sys.executable, str(BIN / "divan_git.py"), action,
                          "--root", str(root), "--repo", str(repo), *extra, ok=ok)

    def publish(self, peer, member="codex_cli", to="claude_code_cli", from_id=None):
        args = ["publish", "--member", member, "--to", to,
                "--title", "Yeni 0", "--purpose", "Çalışmayı ilerlet",
                "--expected", "Yeni inceleme girdisi", "--input", str(self.body)]
        if from_id:
            args += ["--from-id", from_id, "--from-result", from_id]
        return self.flow(self.peers[peer][1], *args)

    def board(self, peer):
        return self.peers[peer][1] / "01_ortak_alan" / "yeni_0"

    def remote_commit(self):
        return self.git(self.remote, "rev-parse", "refs/heads/divan-paylasim")

    def raw_remote_messages(self, messages):
        """Construct deliberately invalid remote data without the exporter."""
        self.git(self.remote, "config", "user.name", "Local Raw Fixture")
        self.git(self.remote, "config", "user.email", "local-fixture@localhost")
        entries = []
        for data in messages:
            oid = self.shell("git", "-C", str(self.remote), "hash-object", "-w", "--stdin",
                             input=json.dumps(data, ensure_ascii=False)).stdout.strip()
            entries.append(f"100644 blob {oid}\t{data['id']}.json\n")
        inner = self.shell("git", "-C", str(self.remote), "mktree",
                           input="".join(sorted(entries))).stdout.strip()
        tree = self.shell("git", "-C", str(self.remote), "mktree",
                          input=f"040000 tree {inner}\tyeni_0\n").stdout.strip()
        commit = self.git(self.remote, "commit-tree", tree, "-m", "Raw graph fixture")
        self.git(self.remote, "update-ref", "refs/heads/divan-paylasim", commit)

    def test_missing_remote_branch_pull_succeeds(self):
        for peer in (0, 1):
            result = self.exchange(peer, "pull")
            self.assertIn("Alınan yeni 0: 0", result.stdout)
            self.assertEqual(list(self.board(peer).iterdir()), [])
        self.assertEqual(self.git(self.remote, "for-each-ref", "--format=%(refname)"), "")

    def test_two_peer_roundtrip_transfers_new_zero_not_private_one(self):
        first = self.publish(0)
        self.exchange(0, "push")
        self.exchange(1, "pull")
        imported = json.loads((self.board(1) / (first + ".json")).read_text(encoding="utf-8"))
        self.assertEqual(imported["tur"], "yeni_0")
        self.assertEqual(imported["id"], first)
        root_b = self.peers[1][1]
        self.flow(root_b, "claim", "--member", "claude_code_cli", first)
        private = self.base / "private.md"
        private.write_text("YEREL_1_OZEL_SONUC_19573", encoding="utf-8")
        self.flow(root_b, "complete", "--member", "claude_code_cli", first, "--input", str(private))
        second = self.publish(1, "claude_code_cli", "codex_cli", first)
        self.exchange(1, "push")
        self.exchange(0, "pull")
        reply = json.loads((self.board(0) / (second + ".json")).read_text(encoding="utf-8"))
        self.assertEqual(reply["onceki_girdi"], first)
        self.assertEqual(reply["yazar"], "claude_code_cli")
        commit = self.remote_commit()
        paths = self.git(self.remote, "ls-tree", "-r", "--name-only", commit).splitlines()
        self.assertEqual(set(paths), {f"yeni_0/{first}.json", f"yeni_0/{second}.json"})
        for path in paths:
            raw = self.git(self.remote, "show", f"{commit}:{path}")
            self.assertNotIn("YEREL_1_OZEL_SONUC_19573", raw)
        self.assertFalse(any(p.suffix == ".md" for p in self.board(0).iterdir()))
        results_a = self.peers[0][1] / "02_karargahlar"
        self.assertEqual(list(results_a.rglob(first + ".md")), [])

    def test_repeated_push_is_noop(self):
        self.publish(0)
        self.exchange(0, "push")
        first = self.remote_commit()
        self.exchange(0, "push")
        self.assertEqual(self.remote_commit(), first)
        self.exchange(1, "pull")
        self.exchange(1, "push")
        self.assertEqual(self.remote_commit(), first)

    def test_exchange_preserves_checkout_head_index_and_user_files(self):
        before = []
        for repo, root in self.peers:
            (repo / "tracked.txt").write_text("staged change\n", encoding="utf-8")
            self.git(repo, "add", "tracked.txt")
            (repo / "tracked.txt").write_text("unstaged change\n", encoding="utf-8")
            (repo / "mine.txt").write_text("untracked user file\n", encoding="utf-8")
            before.append((self.git(repo, "rev-parse", "HEAD"),
                           (repo / ".git" / "index").read_bytes(),
                           self.git(repo, "status", "--porcelain"),
                           (repo / "tracked.txt").read_bytes(),
                           (repo / "mine.txt").read_bytes()))
        self.publish(0)
        self.exchange(0, "push")
        self.exchange(1, "pull")
        self.exchange(1, "push")
        for (repo, root), expected in zip(self.peers, before):
            actual = (self.git(repo, "rev-parse", "HEAD"),
                      (repo / ".git" / "index").read_bytes(),
                      self.git(repo, "status", "--porcelain"),
                      (repo / "tracked.txt").read_bytes(),
                      (repo / "mine.txt").read_bytes())
            self.assertEqual(actual, expected)

    def test_same_id_different_content_fails_without_overwriting(self):
        ident = self.publish(0)
        self.exchange(0, "push")
        self.exchange(1, "pull")
        path = self.board(1) / (ident + ".json")
        altered = json.loads(path.read_text(encoding="utf-8"))
        altered["girdi"] = "Aynı kimlikte çakışan içerik"
        path.write_text(json.dumps(altered, ensure_ascii=False), encoding="utf-8")
        before = path.read_bytes()
        commit = self.remote_commit()
        for action in ("pull", "push"):
            result = self.exchange(1, action, ok=False)
            self.assertIn("Aynı kimlik için farklı içerik", result.stderr)
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(self.remote_commit(), commit)

    def test_concurrent_pulls_pin_independent_commits_and_preserve_fetch_head(self):
        first = self.publish(0)
        second = self.publish(1)
        self.exchange(0, "push", branch="alpha")
        self.exchange(1, "push", branch="beta")
        expected = {branch: self.git(self.remote, "rev-parse", f"refs/heads/{branch}")
                    for branch in ("alpha", "beta")}
        repo = self.peers[0][0]
        self.git(repo, "update-ref", "refs/divan/user-kept", "HEAD")
        before_refs = self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)")
        fetch_head = repo / ".git" / "FETCH_HEAD"
        fetch_head.write_bytes(b"pre-existing user FETCH_HEAD\n")
        transport = load_transport()
        real_git = transport.git
        both_fetched = threading.Barrier(2, timeout=10)

        def pause_after_fetch(*args, **kwargs):
            result = real_git(*args, **kwargs)
            if args[1] == "fetch":
                # Both fetches finish before either caller resolves its commit.
                # With shared FETCH_HEAD both callers return the same commit.
                both_fetched.wait()
            return result

        with mock.patch.object(transport, "git", side_effect=pause_after_fetch):
            with ThreadPoolExecutor(max_workers=2) as pool:
                futures = {branch: pool.submit(transport.fetch_snapshot, repo, "origin", branch)
                           for branch in ("alpha", "beta")}
                actual = {branch: future.result(timeout=15) for branch, future in futures.items()}
        self.assertEqual(actual, expected)
        self.assertEqual(fetch_head.read_bytes(), b"pre-existing user FETCH_HEAD\n")
        self.assertEqual(self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)"), before_refs)
        for branch, ident in (("alpha", first), ("beta", second)):
            root = self.base / ("import-" + branch)
            self.flow(root, "init")
            transport.import_snapshot(root, repo, actual[branch])
            self.assertEqual({p.stem for p in (root / "01_ortak_alan/yeni_0").glob("*.json")}, {ident})

    def test_concurrent_pushes_same_checkout_preserve_separate_branches(self):
        first = self.publish(0)
        second = self.publish(1)
        repo = self.peers[0][0]
        self.git(repo, "update-ref", "refs/divan/user-kept", "HEAD")
        before_refs = set(self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)").splitlines())

        def push(peer, branch):
            return self.shell(sys.executable, str(BIN / "divan_git.py"), "push",
                              "--root", str(self.peers[peer][1]), "--repo", str(repo),
                              "--branch", branch)

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(push, peer, branch)
                       for peer, branch in ((0, "alpha"), (1, "beta"))]
            for future in futures:
                future.result(timeout=20)
        for branch, ident in (("alpha", first), ("beta", second)):
            paths = self.git(self.remote, "ls-tree", "-r", "--name-only", f"refs/heads/{branch}")
            self.assertEqual(paths, f"yeni_0/{ident}.json")
        after_refs = set(self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)").splitlines())
        self.assertTrue(before_refs.issubset(after_refs))
        # Git itself records successful pushes in their matching tracking refs.
        extra_names = {line.split()[0] for line in after_refs - before_refs}
        self.assertEqual(extra_names, {"refs/remotes/origin/alpha", "refs/remotes/origin/beta"})

    def test_failed_snapshot_resolution_cleans_up_only_its_private_ref(self):
        self.publish(0)
        self.exchange(0, "push")
        repo = self.peers[1][0]
        self.git(repo, "update-ref", "refs/divan/user-kept", "HEAD")
        before_refs = self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)")
        transport = load_transport()
        real_git = transport.git

        def fail_resolution(*args, **kwargs):
            if args[1] == "rev-parse":
                raise subprocess.CalledProcessError(1, ["git", "rev-parse"])
            return real_git(*args, **kwargs)

        with mock.patch.object(transport, "git", side_effect=fail_resolution):
            with self.assertRaises(subprocess.CalledProcessError):
                transport.fetch_snapshot(repo, "origin", "divan-paylasim")
        self.assertEqual(self.git(repo, "for-each-ref", "--format=%(refname) %(objectname)"), before_refs)

    def test_remote_orphan_or_cycle_refused_before_any_board_write(self):
        first = self.publish(0)
        original = json.loads((self.board(0) / (first + ".json")).read_text(encoding="utf-8"))
        for problem in ("orphan", "cycle"):
            with self.subTest(problem=problem):
                a = dict(original, id="a" * 32, onceki_girdi="b" * 32)
                messages = [original, a]
                if problem == "cycle":
                    messages.append(dict(original, id="b" * 32, onceki_girdi="a" * 32))
                self.raw_remote_messages(messages)
                result = self.exchange(1, "pull", ok=False)
                self.assertIn("girdi" if problem == "orphan" else "döngü", result.stderr)
                self.assertEqual(list(self.board(1).glob("*.json")), [])

    def test_remote_child_can_reference_existing_local_parent(self):
        parent = self.publish(1)
        original = json.loads((self.board(1) / (parent + ".json")).read_text(encoding="utf-8"))
        child = dict(original, id="a" * 32, onceki_girdi=parent)
        self.raw_remote_messages([child])
        self.exchange(1, "pull")
        self.assertEqual({p.stem for p in self.board(1).glob("*.json")}, {parent, "a" * 32})

    def test_export_rejects_invalid_local_graph_before_creating_remote_ref(self):
        ident = self.publish(0)
        path = self.board(0) / (ident + ".json")
        data = json.loads(path.read_text(encoding="utf-8"))
        data["onceki_girdi"] = "a" * 32
        path.write_text(json.dumps(data), encoding="utf-8")
        transport = load_transport()
        repo, root = self.peers[0]
        with self.assertRaisesRegex(ValueError, "Önceki girdi"):
            transport.export_snapshot(root, repo, "origin", "divan-paylasim", None)
        self.assertEqual(self.git(self.remote, "for-each-ref", "--format=%(refname)"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
