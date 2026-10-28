"""Gelen kutusu: açık konular anahtarsız okunur ve Git dışındaki özel dizine iner.

Ağ yok; GitHub yanıtları bellekte üretilir.
"""
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru import inbox  # noqa: E402
from ortak_kopru.adapters import github as gh  # noqa: E402
from ortak_kopru.gateway_cli import main  # noqa: E402

REPO = "owner/project"
FORM_BODY = (
    "### Ne getiriyorsunuz?\n\nSoru\n\n"
    "### Hangi yazı, hangi bölüm?\n\nacilis.html#niyet\n\n"
    "### Karşılığınız\n\nBu paragraftaki kapı kimin için?\n\n"
    "### Dayanak (isteğe bağlı)\n\n_No response_\n\n"
    "### Sınır\n\n- [X] Bu yazıda şifre, anahtar, kişisel bilgi ya da bana ait olmayan özel bir içerik yok.\n"
)


def issue(number=7, body=FORM_BODY, title="[Karşılık] acilis.html · Niyet", login="okur-1"):
    return {"number": number, "title": title, "body": body, "user": {"login": login},
            "html_url": f"https://github.com/{REPO}/issues/{number}",
            "created_at": "2026-10-28T20:00:00Z", "updated_at": "2026-10-28T20:05:00Z"}


class Response(io.BytesIO):
    def __init__(self, value, url):
        super().__init__(json.dumps(value).encode("utf-8"))
        self.status, self.headers, self.url = 200, {}, url

    def geturl(self):
        return self.url


class Opener:
    def __init__(self, *pages):
        self.pages, self.requests = list(pages), []

    def open(self, request, *, timeout):
        self.requests.append(request)
        return Response(self.pages.pop(0), request.full_url)


class InboxTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="gelen-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.exchange = self.root / "aktarim"

    def run_inbox(self, opener, directory=None):
        out = io.StringIO()
        with mock.patch.dict(os.environ, {"GH_TOKEN": "synthetic-secret"}), \
             mock.patch.object(gh, "build_opener", return_value=opener), redirect_stdout(out):
            code = main(["--exchange-dir", str(directory or self.exchange), "inbox", "--repo", REPO])
        return code, json.loads(out.getvalue())

    def test_issue_lands_in_private_inbox_with_provenance(self):
        pull_request = {**issue(number=8), "pull_request": {"url": "x"}}
        opener = Opener([issue(), pull_request])
        code, output = self.run_inbox(opener)
        self.assertEqual(code, 0, output)
        request = opener.requests[0]
        self.assertTrue(request.full_url.startswith(gh.API_ROOT + "/repos/owner/project/issues?"))
        self.assertIn("state=open", request.full_url)
        self.assertEqual(request.get_method(), "GET")
        self.assertIsNone(request.get_header("Authorization"), "gelen kutusu anahtarsız okur")
        result = output["result"]
        self.assertEqual(result["credentials"], "none")
        self.assertEqual([item["number"] for item in result["new"]], [7])
        files = sorted((self.exchange / "gelen").iterdir())
        self.assertEqual(len(files), 1)
        record = json.loads(files[0].read_text(encoding="utf-8"))
        self.assertEqual(record["kind"], "ortak_kopru_gelen")
        self.assertEqual((record["author"], record["number"], record["yer"], record["tur"]),
                         ("okur-1", 7, "acilis.html#niyet", "Soru"))
        self.assertEqual(record["url"], f"https://github.com/{REPO}/issues/7")
        self.assertEqual(record["updated_at"], "2026-10-28T20:05:00Z")
        self.assertEqual(record["content_sha256"], inbox.content_digest(issue()))
        self.assertIn("Bu paragraftaki kapı kimin için?", record["body"])
        if os.name != "nt":
            self.assertEqual(files[0].stat().st_mode & 0o777, 0o600)

    def test_unchanged_issue_is_not_written_twice_and_an_edit_keeps_the_old_text(self):
        self.run_inbox(Opener([issue()]))
        code, output = self.run_inbox(Opener([issue()]))
        self.assertEqual((code, output["result"]["new"], output["result"]["unchanged"]), (0, [], 1))
        edited = issue(body=FORM_BODY.replace("kimin için", "nereye açılıyor"))
        code, output = self.run_inbox(Opener([edited]))
        self.assertEqual(len(output["result"]["new"]), 1)
        self.assertEqual(len(list((self.exchange / "gelen").iterdir())), 2)

    def test_inbox_refuses_a_directory_inside_a_git_work_tree(self):
        project = self.root / "depo"
        (project / ".git").mkdir(parents=True)
        (project / ".git" / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        opener = Opener([issue()])
        code, output = self.run_inbox(opener, project / "aktarim")
        self.assertEqual(code, 1)
        self.assertEqual(output["error"]["code"], "invalid_exchange")
        self.assertEqual(opener.requests, [])
        self.assertFalse((project / "aktarim").exists())

    def test_malformed_issue_is_refused_before_anything_is_written(self):
        for broken in ({**issue(), "html_url": "https://example.com/x"},
                       {**issue(), "user": {"login": "a b"}},
                       {**issue(), "number": True}):
            with self.subTest(broken=broken):
                code, output = self.run_inbox(Opener([broken]))
                self.assertEqual((code, output["error"]["code"]), (1, "invalid_response"))
                self.assertEqual(list((self.exchange / "gelen").iterdir()), [])

    def test_form_labels_match_the_reply_form(self):
        form = (ROOT / ".github" / "ISSUE_TEMPLATE" / "karsilik.yml").read_text(encoding="utf-8")
        for label in inbox.FORM_FIELDS.values():
            self.assertIn("label: " + label, form)
        self.assertEqual(inbox.form_fields("serbest metin"), {"tur": None, "yer": None})


if __name__ == "__main__":
    unittest.main()
