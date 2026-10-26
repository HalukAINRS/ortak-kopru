"""GitHub protocol tests use in-memory HTTP responses, never live services."""
from email.message import Message
from http.client import IncompleteRead
import base64
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ortak_kopru.adapters import github as gh

COMMIT = "1" * 40
TREE = "2" * 40
SUBTREE = "3" * 40
OTHER = "4" * 40
REPO = "owner/project"
ROOT = "/repos/" + REPO


class Response(io.BytesIO):
    def __init__(self, value, url, *, status=200, headers=None, raw=False):
        super().__init__(value if raw else json.dumps(value).encode())
        self.status = status
        self.headers = headers or {}
        self.url = url

    def geturl(self):
        return self.url


class Opener:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.requests = []

    def open(self, request, *, timeout):
        self.requests.append(request)
        assert request.full_url.startswith(gh.API_ROOT + "/repos/")
        assert timeout > 0
        if not self.responses:
            raise AssertionError("Unexpected request: " + request.full_url)
        item = self.responses.pop(0)
        if isinstance(item, Exception):
            raise item
        if callable(item):
            return item(request)
        return Response(item, request.full_url, status=201 if request.method == "POST" else 200)


def commit(sha=COMMIT, tree=TREE, parents=None, message="message"):
    return {"sha": sha, "tree": {"sha": tree},
            "parents": [{"sha": p} for p in (parents if parents is not None else [OTHER])], "message": message}


def tree(*entries, sha=TREE, truncated=False):
    return {"sha": sha, "truncated": truncated, "tree": list(entries)}


def entry(path, sha, mode="100644", kind="blob"):
    return {"path": path, "sha": sha, "mode": mode, "type": kind}


def blob(data):
    return {"sha": gh.git_blob_sha(data), "size": len(data), "encoding": "base64",
            "content": base64.encodebytes(data).decode()}


def branch(name="kapi/x_123", sha=COMMIT):
    return {"ref": "refs/heads/" + name, "object": {"type": "commit", "sha": sha}}


def pr(*, state="open", draft=True, sha=COMMIT):
    return {"number": 17, "html_url": "https://github.com/owner/project/pull/17", "state": state,
            "draft": draft, "head": {"ref": "kapi/x_123", "sha": sha, "repo": {"full_name": REPO}},
            "base": {"ref": "main", "sha": OTHER, "repo": {"full_name": REPO}}}


def http_error(code, message="ignored response secret"):
    return HTTPError(gh.API_ROOT + ROOT, code, message, Message(), io.BytesIO(message.encode()))


class GitHubReadTests(unittest.TestCase):
    def test_literal_refs_and_repository_validation_prevent_url_or_revision_injection(self):
        self.assertEqual(gh.validate_repository("HalukAINRS/ortak-kopru"), "HalukAINRS/ortak-kopru")
        for value in ("https://github.com/o/r", "o/r/extra", "o/..", "o/r?token=x", "user@host/r"):
            with self.subTest(repository=value), self.assertRaises(gh.GitHubError):
                gh.validate_repository(value)
        for value in ("main", "release/v1.0", "refs/tags/v1", COMMIT, "geliştirme/kapı"):
            self.assertEqual(gh.validate_ref(value), value)
        for value in ("../main", "main^", "main~1", "feature//x", "main.lock", "x/.hidden", "@", "x@{1}", "x\ny", "-main", "x\ud800"):
            with self.subTest(ref=value), self.assertRaises(gh.GitHubError):
                gh.validate_ref(value)
        for value in ("HEAD", "refs/heads/main"):
            with self.assertRaises(gh.GitHubError):
                gh.validate_branch(value)

    def test_public_ref_resolution_is_anonymous_and_header_version_is_pinned(self):
        opener = Opener({"sha": COMMIT, "commit": {"tree": {"sha": TREE}}})
        client = gh.GitHubClient(opener=opener)
        self.assertFalse(client.authenticated)
        self.assertEqual(client.resolve_ref(REPO, "feature/v1"), {"commit": COMMIT, "tree": TREE})
        request = opener.requests[0]
        self.assertTrue(request.full_url.endswith("/commits/feature%2Fv1"))
        self.assertIsNone(request.get_header("Authorization"))
        self.assertEqual(request.get_header("X-github-api-version"), gh.API_VERSION)
        with self.assertRaises(gh.GitHubError):
            gh.GitHubClient(opener=Opener({"sha": OTHER, "commit": {"tree": {"sha": TREE}}})).resolve_ref(REPO, COMMIT)

    def test_nested_binary_fetch_uses_only_pinned_git_objects_and_deduplicates_blobs(self):
        data = b"\0\xff\xfe\r\n" + "Türkçe".encode()
        digest = gh.git_blob_sha(data)
        opener = Opener(commit(), tree(entry("src", SUBTREE, "040000", "tree")),
                        tree(entry("a.bin", digest), entry("b.bin", digest, "100755"), sha=SUBTREE), blob(data))
        files = gh.GitHubClient(opener=opener).files_at(REPO, COMMIT, ["src/a.bin", "src/b.bin"])
        self.assertEqual([value["data"] for value in files], [data, data])
        self.assertEqual([value["mode"] for value in files], ["100644", "100755"])
        paths = [urlsplit(request.full_url).path for request in opener.requests]
        self.assertEqual(paths, [ROOT + "/git/commits/" + COMMIT, ROOT + "/git/trees/" + TREE,
                                 ROOT + "/git/trees/" + SUBTREE, ROOT + "/git/blobs/" + digest])

    def test_inspection_reports_absent_leaves_and_parents_without_following_links(self):
        opener = Opener(commit(), tree(entry("src", SUBTREE, "040000", "tree")), tree(sha=SUBTREE))
        result = gh.GitHubClient(opener=opener).inspect_paths(REPO, COMMIT, ["missing.txt", "src/missing.txt", "none/file.txt"])
        self.assertTrue(all(value["blob_sha"] is None and value["mode"] is None for value in result))
        self.assertEqual(len(opener.requests), 3)

    def test_selected_symlink_submodule_directory_or_non_directory_parent_is_rejected(self):
        for mode, kind, path in (("120000", "blob", "file"), ("160000", "commit", "file"),
                                  ("040000", "tree", "file"), ("100644", "blob", "file/child")):
            opener = Opener(commit(), tree(entry("file", OTHER, mode, kind)))
            with self.subTest(mode=mode, path=path), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient(opener=opener).files_at(REPO, COMMIT, [path])
            self.assertEqual(error.exception.code, "unsupported_path")
            self.assertEqual(len(opener.requests), 2)

    def test_truncated_or_wrong_tree_and_wrong_commit_identity_are_not_accepted(self):
        variants = [tree(truncated=True), tree(sha=OTHER), tree(entry("x", OTHER), entry("x", OTHER))]
        for response in variants:
            with self.subTest(response=response), self.assertRaises(gh.GitHubError):
                gh.GitHubClient(opener=Opener(commit(), response)).inspect_paths(REPO, COMMIT, ["x"])
        with self.assertRaises(gh.GitHubError):
            gh.GitHubClient(opener=Opener(commit(sha=OTHER))).get_commit(REPO, COMMIT)

    def test_blob_declared_hash_bytes_size_and_encoding_are_all_checked(self):
        original = b"original"
        digest = gh.git_blob_sha(original)
        good = blob(original)
        variants = [{**good, "sha": OTHER}, {**good, "content": base64.b64encode(b"tampered").decode()},
                    {**good, "size": len(original) + 1}, {**good, "size": True},
                    {**good, "encoding": "utf-8"}, {**good, "content": "not!!base64"}]
        for response in variants:
            opener = Opener(commit(), tree(entry("a", digest)), response)
            with self.subTest(response=response), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient(opener=opener).files_at(REPO, COMMIT, ["a"])
            self.assertEqual(error.exception.code, "invalid_response")

    def test_file_and_total_limits_fail_without_partial_success(self):
        data = b"1234"
        digest = gh.git_blob_sha(data)
        with patch.object(gh, "MAX_FILE_BYTES", 3), self.assertRaises(gh.GitHubError):
            gh.GitHubClient(opener=Opener(commit(), tree(entry("a", digest)), blob(data))).files_at(REPO, COMMIT, ["a"])
        with patch.object(gh, "MAX_TOTAL_BYTES", 7), self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient(opener=Opener(commit(), tree(entry("a", digest), entry("b", digest)), blob(data))).files_at(REPO, COMMIT, ["a", "b"])
        self.assertEqual(error.exception.code, "size_limit")

    def test_invalid_selection_is_rejected_before_http(self):
        opener = Opener()
        client = gh.GitHubClient(opener=opener)
        for paths in ([], ["a"] * 65, ["a", "a"], ["a", "a/b"], ["../a"], ["/a"], [".git/config"], ["a\\b"], ["a\0b"]):
            with self.subTest(paths=paths), self.assertRaises(gh.GitHubError):
                client.inspect_paths(REPO, COMMIT, paths)
        self.assertFalse(opener.requests)


class GitHubTransportTests(unittest.TestCase):
    def test_redirects_are_disabled_and_token_stays_on_the_single_fixed_host_request(self):
        client = gh.GitHubClient("synthetic-secret")
        redirect = next(h for h in client._opener.handlers if isinstance(h, gh._NoRedirect))
        for status in (301, 302, 303, 307, 308):
            self.assertIsNone(redirect.redirect_request(None, None, status, "", {}, "https://elsewhere.test/"))
        opener = Opener(http_error(302, "synthetic-secret"))
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient("synthetic-secret", opener=opener).create_branch(REPO, "kapi/x", COMMIT)
        self.assertEqual(error.exception.code, "redirect_refused")
        self.assertTrue(error.exception.ambiguous)
        self.assertEqual(len(opener.requests), 1)
        self.assertEqual(urlsplit(opener.requests[0].full_url).netloc, "api.github.com")
        self.assertNotIn("synthetic-secret", str(error.exception))

    def test_oversized_invalid_duplicate_or_redirected_response_is_rejected(self):
        responses = [
            lambda request: Response(b"x" * 33, request.full_url, raw=True),
            lambda request: Response({}, request.full_url, headers={"Content-Length": "33"}),
            lambda request: Response(b'{"sha":1,"sha":2}', request.full_url, raw=True),
            lambda request: Response(b"synthetic-secret", request.full_url, raw=True),
            lambda request: Response({}, "https://elsewhere.test/"),
        ]
        for response in responses:
            with self.subTest(response=response), patch.object(gh, "MAX_RESPONSE_BYTES", 32), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient(opener=Opener(response)).resolve_ref(REPO, "main")
            self.assertNotIn("synthetic-secret", str(error.exception))

    def test_only_404_branch_read_means_absent_and_writes_report_uncertain_failures(self):
        self.assertIsNone(gh.GitHubClient(opener=Opener(http_error(404))).get_branch(REPO, "main"))
        for code in (401, 403, 429):
            with self.subTest(status=code), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient(opener=Opener(http_error(code))).get_branch(REPO, "main")
            self.assertEqual(error.exception.status, code)
            self.assertFalse(error.exception.ambiguous)
        for response in (URLError("synthetic-secret"), TimeoutError("synthetic-secret"),
                         IncompleteRead(b"synthetic-secret", 99), http_error(500), http_error(503)):
            with self.subTest(response=type(response)), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient("synthetic-secret", opener=Opener(response)).create_branch(REPO, "kapi/x", COMMIT)
            self.assertTrue(error.exception.ambiguous)
            self.assertNotIn("synthetic-secret", str(error.exception))
            self.assertTrue(error.exception.__suppress_context__)
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient(opener=Opener(URLError("read timeout"))).get_branch(REPO, "main")
        self.assertFalse(error.exception.ambiguous)

    def test_unexpected_success_status_on_write_is_ambiguous(self):
        response = lambda request: Response({}, request.full_url, status=202)
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient("secret", opener=Opener(response)).create_branch(REPO, "kapi/x", COMMIT)
        self.assertEqual(error.exception.status, 202)
        self.assertTrue(error.exception.ambiguous)

    def test_credentials_are_read_only_from_explicit_environment_and_required_for_writes(self):
        opener = Opener()
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient(opener=opener).create_blob(REPO, b"x")
        self.assertEqual(error.exception.code, "credentials_required")
        self.assertFalse(opener.requests)
        with patch.dict(gh.os.environ, {"ORTAK_KOPRU_GITHUB_TOKEN": "chosen", "GH_TOKEN": "other", "GITHUB_TOKEN": "third"}, clear=True):
            client = gh.GitHubClient.from_env()
            self.assertEqual(client._token, "chosen")
        with patch.dict(gh.os.environ, {}, clear=True):
            self.assertFalse(gh.GitHubClient.from_env().authenticated)
        for token in ("x\ny", "x y", "", "ı"):
            with self.subTest(token=token), self.assertRaises(gh.GitHubError):
                gh.GitHubClient(token)


class GitHubWriteTests(unittest.TestCase):
    def test_blob_and_tree_requests_contain_only_selected_objects_and_base_tree(self):
        data = b"binary\xff\0"
        digest = gh.git_blob_sha(data)
        opener = Opener({"sha": digest}, {"sha": OTHER})
        client = gh.GitHubClient("synthetic-secret", opener=opener)
        self.assertEqual(client.create_blob(REPO, data), digest)
        selected = [{"path": "out/a.bin", "mode": "100644", "type": "blob", "sha": digest}]
        self.assertEqual(client.create_tree(REPO, TREE, selected), OTHER)
        blob_payload = json.loads(opener.requests[0].data)
        self.assertEqual(base64.b64decode(blob_payload["content"]), data)
        self.assertEqual(blob_payload["encoding"], "base64")
        self.assertEqual(json.loads(opener.requests[1].data), {"base_tree": TREE, "tree": selected})
        for request in opener.requests:
            self.assertEqual(request.get_header("Authorization"), "Bearer synthetic-secret")
            self.assertNotIn(b"synthetic-secret", request.data)
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient("secret", opener=Opener({"sha": OTHER})).create_blob(REPO, data)
        self.assertTrue(error.exception.ambiguous)

    def test_tree_cannot_delete_install_links_or_smuggle_inline_unselected_content(self):
        client = gh.GitHubClient("secret", opener=Opener())
        valid = {"path": "a", "mode": "100644", "type": "blob", "sha": COMMIT}
        for value in ({**valid, "sha": None}, {**valid, "mode": "120000"}, {**valid, "content": "surprise"}, {**valid, "type": "tree"}):
            with self.subTest(entry=value), self.assertRaises(gh.GitHubError):
                client.create_tree(REPO, TREE, [value])

    def test_commit_reply_must_bind_tree_parent_and_message(self):
        opener = Opener(commit(tree=TREE, parents=[OTHER], message="public marker"))
        client = gh.GitHubClient("secret", opener=opener)
        self.assertEqual(client.create_commit(REPO, TREE, OTHER, "public marker"), COMMIT)
        self.assertEqual(json.loads(opener.requests[0].data), {"tree": TREE, "parents": [OTHER], "message": "public marker"})
        for response in (commit(tree=OTHER), commit(parents=[]), commit(message="other")):
            with self.subTest(response=response), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient("secret", opener=Opener(response)).create_commit(REPO, TREE, OTHER, "public marker")
            self.assertTrue(error.exception.ambiguous)

    def test_new_branch_creation_never_updates_and_response_must_match(self):
        opener = Opener(branch(), branch())
        client = gh.GitHubClient("secret", opener=opener)
        self.assertEqual(client.get_branch(REPO, "kapi/x_123"), COMMIT)
        self.assertEqual(client.create_branch(REPO, "kapi/x_123", COMMIT), COMMIT)
        self.assertEqual([request.method for request in opener.requests], ["GET", "POST"])
        self.assertTrue(opener.requests[1].full_url.endswith("/git/refs"))
        with self.assertRaises(gh.GitHubConflict) as error:
            gh.GitHubClient("secret", opener=Opener(http_error(422))).create_branch(REPO, "kapi/x_123", COMMIT)
        self.assertFalse(error.exception.ambiguous)
        for value in (branch(name="main"), branch(sha=OTHER)):
            with self.subTest(response=value), self.assertRaises(gh.GitHubError) as error:
                gh.GitHubClient("secret", opener=Opener(value)).create_branch(REPO, "kapi/x_123", COMMIT)
            self.assertTrue(error.exception.ambiguous)

    def test_pr_reconciliation_includes_closed_prs_and_rejects_duplicate_or_foreign_matches(self):
        opener = Opener([pr(state="closed")])
        result = gh.GitHubClient(opener=opener).find_pull_request(REPO, "kapi/x_123", "main")
        self.assertEqual(result["state"], "closed")
        query = parse_qs(urlsplit(opener.requests[0].full_url).query)
        self.assertEqual(query["state"], ["all"])
        self.assertEqual(query["head"], ["owner:kapi/x_123"])
        self.assertEqual(query["base"], ["main"])
        foreign = pr()
        foreign["head"]["repo"]["full_name"] = "someone/else"
        wrong_url = pr()
        wrong_url["html_url"] = "https://elsewhere.test/pull/17"
        for values in ([pr(), pr()], [foreign], [wrong_url], [pr()] * 100):
            with self.subTest(values=values[:1]), self.assertRaises(gh.GitHubError):
                gh.GitHubClient(opener=Opener(values)).find_pull_request(REPO, "kapi/x_123", "main")

    def test_draft_pr_creation_returns_bound_receipt_and_does_not_merge(self):
        opener = Opener(pr())
        client = gh.GitHubClient("secret", opener=opener)
        result = client.create_pull_request(REPO, "kapi/x_123", "main", "Selected files", "Public marker")
        self.assertEqual(result, {"number": 17, "url": "https://github.com/owner/project/pull/17", "head_sha": COMMIT,
                                  "head_ref": "kapi/x_123", "base_ref": "main", "state": "open", "draft": True})
        self.assertEqual(json.loads(opener.requests[0].data), {"head": "kapi/x_123", "base": "main", "title": "Selected files", "body": "Public marker", "draft": True})
        self.assertEqual(len(opener.requests), 1)
        with self.assertRaises(gh.GitHubError) as error:
            gh.GitHubClient("secret", opener=Opener(pr(draft=False))).create_pull_request(REPO, "kapi/x_123", "main", "title", "body")
        self.assertTrue(error.exception.ambiguous)


if __name__ == "__main__":
    unittest.main()
