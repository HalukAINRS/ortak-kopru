"""Exchange workflows against a synthetic remote Git graph; no live services."""
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru import gateway  # noqa: E402
from ortak_kopru.adapters.github import GitHubError, GitHubConflict, git_blob_sha  # noqa: E402
from ortak_kopru.exchange import ExchangeConflict, ExchangeStore  # noqa: E402


def identity(value):
    return hashlib.sha1(json.dumps(value, sort_keys=True).encode(), usedforsecurity=False).hexdigest()


class Remote:
    """Independent observable remote state with failures before/after effects."""

    authenticated = True

    def __init__(self):
        self.blobs, self.trees, self.commits = {}, {}, {}
        entries = {}
        for path, data, mode in [
            ("report.txt", b"previous report\n", "100644"),
            ("keep.bin", b"\xffunselected unchanged", "100644"),
            ("run.sh", b"echo before\n", "100755"),
        ]:
            blob = git_blob_sha(data)
            self.blobs[blob] = data
            entries[path] = {"sha": blob, "mode": mode}
        tree = identity(entries)
        self.trees[tree] = entries
        commit = identity({"tree": tree, "parent": None})
        self.commits[commit] = {"sha": commit, "tree": tree, "parents": [], "message": "initial"}
        self.branches = {"main": commit}
        self.initial = commit
        self.prs = []
        self.calls, self.writes = [], []
        self.fail_after = set()
        self.fail_reads_after_branch = False
        self.omit_selected = False
        self.advance_after_resolve = False
        self.advance_on_blob = False
        self.fail_branch_reads = False
        self.fail_pr_reads = False

    def _write(self, method, value):
        self.writes.append((method, deepcopy(value)))

    def _after(self, method):
        if method in self.fail_after:
            self.fail_after.remove(method)
            raise GitHubError("raw-secret-must-not-enter-ledger", code="transport_error", ambiguous=True)

    def advance_main(self):
        base = self.commits[self.branches["main"]]
        entries = deepcopy(self.trees[base["tree"]])
        data = b"independent change\n"
        blob = git_blob_sha(data)
        self.blobs[blob] = data
        entries["independent.txt"] = {"sha": blob, "mode": "100644"}
        tree = identity(entries)
        self.trees[tree] = entries
        commit = identity({"tree": tree, "parent": self.branches["main"]})
        self.commits[commit] = {"sha": commit, "tree": tree,
                                "parents": [self.branches["main"]], "message": "other writer"}
        self.branches["main"] = commit
        return commit

    def get_branch(self, repo, branch):
        self.calls.append(("get_branch", repo, branch))
        if self.fail_branch_reads:
            self.fail_branch_reads = False
            raise GitHubError("read failed", code="transport_error")
        return self.branches.get(branch)

    def resolve_ref(self, repo, ref):
        commit = self.branches.get(ref, ref)
        result = {"commit": commit, "tree": self.commits[commit]["tree"]}
        if self.advance_after_resolve:
            self.advance_main()
        return result

    def get_commit(self, repo, commit):
        if self.fail_reads_after_branch and any(branch != "main" for branch in self.branches):
            self.fail_reads_after_branch = False
            raise GitHubError("read failed", code="transport_error")
        return deepcopy(self.commits[commit])

    def inspect_paths(self, repo, commit, paths):
        self.calls.append(("inspect_paths", repo, commit, tuple(paths)))
        entries = self.trees[self.commits[commit]["tree"]]
        return [{"path": path, "blob_sha": entries.get(path, {}).get("sha"),
                 "mode": entries.get(path, {}).get("mode")} for path in paths]

    def files_at(self, repo, commit, paths):
        self.calls.append(("files_at", repo, commit, tuple(paths)))
        entries = self.trees[self.commits[commit]["tree"]]
        result = []
        for path in paths:
            if path not in entries:
                raise GitHubError("missing", status=404, code="not_found")
            entry = entries[path]
            data = self.blobs[entry["sha"]]
            result.append({"path": path, "blob_sha": entry["sha"], "mode": entry["mode"],
                           "bytes": len(data), "data": data})
        return result

    def create_blob(self, repo, data):
        self._write("blob", {"repo": repo, "data_hex": data.hex()})
        blob = git_blob_sha(data)
        self.blobs[blob] = data
        if self.advance_on_blob:
            self.advance_on_blob = False
            self.advance_main()
        self._after("blob")
        return blob

    def create_tree(self, repo, base_tree, entries):
        self._write("tree", {"repo": repo, "base_tree": base_tree, "entries": entries})
        value = deepcopy(self.trees[base_tree])
        for entry in entries:
            if not self.omit_selected:
                value[entry["path"]] = {"sha": entry["sha"], "mode": entry["mode"]}
        tree = identity(value)
        self.trees[tree] = value
        self._after("tree")
        return tree

    def create_commit(self, repo, tree, parent, message):
        self._write("commit", {"repo": repo, "tree": tree, "parent": parent, "message": message})
        commit = identity({"tree": tree, "parents": [parent], "message": message})
        self.commits[commit] = {"sha": commit, "tree": tree, "parents": [parent], "message": message}
        self._after("commit")
        return commit

    def create_branch(self, repo, branch, commit):
        self._write("branch", {"repo": repo, "branch": branch, "commit": commit})
        if branch in self.branches:
            raise GitHubConflict("exists", status=422, code="conflict")
        self.branches[branch] = commit
        self._after("branch")
        return commit

    def find_pull_request(self, repo, branch, base):
        if self.fail_pr_reads:
            self.fail_pr_reads = False
            raise GitHubError("read failed", code="transport_error")
        result = [pr for pr in self.prs if pr["head_ref"] == branch and pr["base_ref"] == base]
        if len(result) > 1:
            raise GitHubConflict("ambiguous", code="conflict")
        return deepcopy(result[0]) if result else None

    def create_pull_request(self, repo, branch, base, title, body, draft=True):
        self._write("pull_request", {"repo": repo, "branch": branch, "base": base,
                                     "title": title, "body": body, "draft": draft})
        pr = {"number": len(self.prs) + 1, "url": f"https://github.com/{repo}/pull/{len(self.prs) + 1}",
              "head_sha": self.branches[branch], "head_ref": branch, "base_ref": base,
              "state": "open", "draft": draft}
        self.prs.append(pr)
        self._after("pull_request")
        return deepcopy(pr)


class GatewayTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="kopru-gateway-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.store = ExchangeStore(self.root / "exchange")
        self.file = self.root / "private-original-name.txt"
        self.file.write_bytes(b"selected report\n")
        self.remote = Remote()
        self.purpose = "private purpose that must stay local"

    def prepared(self, *, path="report.txt", key="first", branch=None):
        return gateway.prepare(self.store, [{"source": str(self.file), "path": path}],
                               repository="example/project", base_ref="main", branch=branch,
                               purpose=self.purpose, request_key=key)

    def planned(self, **kwargs):
        record = self.prepared(**kwargs)
        return gateway.plan(self.store, record["id"], self.remote)

    def send(self, record, **kwargs):
        return gateway.send(self.store, record["id"], self.remote,
                            expected_plan_hash=record["plan"]["plan_hash"], **kwargs)

    def test_selected_snapshot_publish_preserves_other_files_and_private_metadata(self):
        record = self.planned()
        self.assertEqual([], self.remote.writes)
        self.assertIn("selected report", record["plan"]["changes"][0]["diff"])
        self.file.write_bytes(b"later private edit must not be sent")
        self.file.unlink()
        sent = self.send(record, pull_request=True)
        self.assertEqual("published", sent["state"])
        self.assertTrue(sent["receipt"]["pull_request"]["draft"])
        self.assertEqual(self.remote.initial, self.remote.branches["main"])
        commit = self.remote.commits[sent["receipt"]["commit"]]
        entries = self.remote.trees[commit["tree"]]
        self.assertEqual(b"selected report\n", self.remote.blobs[entries["report.txt"]["sha"]])
        self.assertEqual(b"\xffunselected unchanged", self.remote.blobs[entries["keep.bin"]["sha"]])
        wire = json.dumps(self.remote.writes)
        for private in (self.purpose, str(self.file), "private-original-name", "later private edit"):
            self.assertNotIn(private, wire)
        count = len(self.remote.writes)
        self.assertEqual(sent, self.send(record, pull_request=True))
        self.assertEqual(count, len(self.remote.writes))
        self.assertFalse((self.store.directory / "deus.sqlite3").exists())

    def test_wrong_plan_hash_and_concurrent_operation_cannot_write(self):
        record = self.planned()
        with self.assertRaises(ExchangeConflict):
            gateway.send(self.store, record["id"], self.remote, expected_plan_hash="0" * 64)
        with self.store.operation(record["id"]):
            with self.assertRaises(ExchangeConflict):
                self.send(record)
        self.assertEqual([], self.remote.writes)

    def test_changed_base_requires_new_plan_before_any_write(self):
        record = self.planned()
        changed = self.remote.advance_main()
        result = self.send(record)
        self.assertEqual("conflict", result["state"])
        self.assertEqual([], self.remote.writes)
        current = gateway.plan(self.store, record["id"], self.remote)
        self.assertEqual(changed, current["plan"]["base_commit"])
        self.assertNotEqual(record["plan"]["plan_hash"], current["plan"]["plan_hash"])
        with self.assertRaises(ExchangeConflict):
            self.send(record)
        self.assertEqual("published", self.send(current)["state"])

    def test_concurrent_base_advance_does_not_overwrite_base_and_keeps_pinned_parent(self):
        record = self.planned()
        self.remote.advance_on_blob = True
        sent = self.send(record)
        self.assertEqual("published", sent["state"])
        self.assertNotEqual(self.remote.initial, self.remote.branches["main"])
        commit = self.remote.commits[sent["receipt"]["commit"]]
        self.assertEqual([self.remote.initial], commit["parents"])
        self.assertEqual(self.remote.initial, sent["receipt"]["base_commit"])

    def test_existing_or_raced_branch_is_never_replaced(self):
        self.remote.branches["already-there"] = self.remote.initial
        record = self.prepared(branch="already-there")
        with self.assertRaises(ExchangeConflict):
            gateway.plan(self.store, record["id"], self.remote)
        record = self.planned(key="new-target")
        self.remote.branches[record["plan"]["branch"]] = self.remote.initial
        self.assertEqual("conflict", self.send(record)["state"])
        self.assertEqual(self.remote.initial, self.remote.branches[record["plan"]["branch"]])
        self.assertEqual([], self.remote.writes)

    def test_lost_branch_response_recovers_without_another_write_even_if_base_moves(self):
        record = self.planned()
        self.remote.fail_after.add("branch")
        uncertain = self.send(record)
        self.assertEqual("unknown", uncertain["state"])
        self.assertNotIn("raw-secret", json.dumps(uncertain))
        self.assertIsNotNone(uncertain["checkpoint"]["commit"])
        self.remote.advance_main()
        writes = deepcopy(self.remote.writes)
        reopened = ExchangeStore(self.store.directory, create=False)
        done = gateway.reconcile(reopened, record["id"], self.remote)
        self.assertEqual("published", done["state"])
        self.assertEqual(writes, self.remote.writes)
        self.assertEqual(1, sum(name == "branch" for name, _ in writes))

    def test_lost_pr_response_retains_branch_receipt_and_closed_pr_is_not_recreated(self):
        record = self.planned()
        self.remote.fail_after.add("pull_request")
        uncertain = self.send(record, pull_request=True)
        self.assertEqual("unknown", uncertain["state"])
        self.assertEqual(self.remote.branches[record["plan"]["branch"]], uncertain["receipt"]["commit"])
        self.remote.prs[0]["state"] = "closed"
        writes = deepcopy(self.remote.writes)
        done = gateway.reconcile(self.store, record["id"], self.remote)
        self.assertEqual("published", done["state"])
        self.assertEqual("closed", done["receipt"]["pull_request"]["state"])
        self.assertEqual(writes, self.remote.writes)
        with self.assertRaises(ExchangeConflict):
            self.send(record, pull_request=False)

    def test_unverified_read_after_branch_creation_stays_unknown(self):
        record = self.planned()
        self.remote.fail_reads_after_branch = True
        uncertain = self.send(record)
        self.assertEqual("unknown", uncertain["state"])
        self.assertTrue(uncertain["checkpoint"]["ref_confirmed"])
        self.assertEqual("published", gateway.reconcile(self.store, record["id"], self.remote)["state"])

    def test_failed_recovery_reads_preserve_prior_branch_and_pr_uncertainty(self):
        for stage, read_flag, want_pr in (("branch", "fail_branch_reads", False),
                                         ("pull_request", "fail_pr_reads", True)):
            with self.subTest(stage=stage):
                record = self.planned(key="recovery-read-" + stage)
                self.remote.fail_after.add(stage)
                self.assertEqual("unknown", self.send(record, pull_request=want_pr)["state"])
                writes = deepcopy(self.remote.writes)
                setattr(self.remote, read_flag, True)
                uncertain = self.send(record, pull_request=want_pr)
                self.assertEqual("unknown", uncertain["state"])
                self.assertEqual("transport_error", uncertain["error"]["provider_code"])
                self.assertEqual(writes, self.remote.writes)
                self.assertEqual("published", self.send(record, pull_request=want_pr)["state"])

    def test_lost_object_response_can_retry_after_observing_absent_branch(self):
        record = self.planned()
        self.remote.fail_after.add("commit")
        uncertain = self.send(record)
        self.assertEqual("unknown", uncertain["state"])
        self.assertNotIn(record["plan"]["branch"], self.remote.branches)
        self.assertEqual("published", self.send(record)["state"])
        self.assertEqual(1, sum(name == "branch" for name, _ in self.remote.writes))

    def test_wrong_created_tree_and_bad_saved_commit_are_rejected_before_ref_creation(self):
        record = self.planned()
        self.remote.omit_selected = True
        self.assertEqual("conflict", self.send(record)["state"])
        self.assertFalse(any(name == "branch" for name, _ in self.remote.writes))
        self.remote.omit_selected = False
        record = gateway.plan(self.store, record["id"], self.remote)
        record = self.store.update(record["id"], expected_states=["planned"], state="unknown",
                                   checkpoint={"commit": self.remote.initial, "pull_request": False})
        self.assertEqual("conflict", self.send(record)["state"])
        self.assertFalse(any(name == "branch" for name, _ in self.remote.writes))

    def test_published_replay_never_recreates_a_deleted_branch(self):
        record = self.planned()
        sent = self.send(record)
        del self.remote.branches[record["plan"]["branch"]]
        writes = deepcopy(self.remote.writes)
        self.assertEqual(sent, self.send(record))
        changed = gateway.reconcile(self.store, record["id"], self.remote)
        self.assertEqual("conflict", changed["state"])
        self.assertEqual(sent["receipt"], changed["receipt"])
        self.assertEqual("conflict", self.send(record)["state"])
        self.assertEqual(writes, self.remote.writes)

    def test_fetch_pins_source_and_materializes_binary_without_local_application(self):
        self.remote.advance_after_resolve = True
        record = gateway.fetch(self.store, self.remote, repository="example/project", ref="main",
                               paths=["report.txt", "keep.bin"], purpose="source", request_key="fetch")
        self.assertEqual("received", record["state"])
        self.assertEqual(self.remote.initial, record["origin"]["commit"])
        self.assertNotEqual(self.remote.initial, self.remote.branches["main"])
        fetched = [call for call in self.remote.calls if call[0] == "files_at"]
        self.assertTrue(all(call[2] == self.remote.initial for call in fetched))
        destination = self.root / "review-copy"
        self.store.materialize(record["id"], destination)
        self.assertEqual(b"previous report\n", (destination / "report.txt").read_bytes())
        self.assertEqual(b"\xffunselected unchanged", (destination / "keep.bin").read_bytes())
        self.assertEqual(b"selected report\n", self.file.read_bytes())
        self.assertEqual([], self.remote.writes)
        self.assertFalse((destination / "manifest.json").exists())
        self.assertEqual([record], self.store.list_transfers())

    def test_incomplete_fetch_creates_no_successful_transfer_or_partial_package(self):
        with self.assertRaises(GitHubError):
            gateway.fetch(self.store, self.remote, repository="example/project", ref="main",
                          paths=["report.txt", "missing.txt"], purpose="source", request_key="fetch")
        self.assertEqual([], self.store.list_transfers())
        self.assertEqual([], list(self.store.packages.iterdir()))
        self.assertEqual([], self.remote.writes)

    def test_missing_credentials_has_actionable_failure_without_remote_mutation(self):
        record = self.planned()
        self.remote.authenticated = False
        result = self.send(record)
        self.assertEqual("failed", result["state"])
        self.assertEqual(401, result["error"]["status"])
        self.assertEqual("authentication_required", result["error"]["provider_code"])
        self.assertEqual([], self.remote.writes)

    def test_preserves_existing_executable_mode_and_limits_text_preview(self):
        self.file.write_bytes(b"echo after\n" + b"# long\n" * 100000)
        record = self.planned(path="run.sh")
        change = record["plan"]["changes"][0]
        self.assertEqual("100755", change["mode"])
        self.assertTrue(change["diff_truncated"])
        self.assertIsNone(change["diff"])
        self.assertEqual("published", self.send(record)["state"])


if __name__ == "__main__":
    unittest.main()
