"""Black-box integration checks for the file exchange, isolated from live data."""
import concurrent.futures
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HELPER = Path(__file__).resolve().parents[1] / "bin" / "divan.py"


class FlowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="divan-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "divan"
        self.input = Path(self.temp.name) / "input.md"
        self.input.write_text("Bir sonraki çalışma için somut girdi.\n", encoding="utf-8")
        self.cli("init")

    def cli(self, *args, ok=True):
        result = subprocess.run(
            [sys.executable, str(HELPER), "--root", str(self.root), *args],
            text=True, capture_output=True, timeout=15,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def publish(self, member="codex_cli", to="claude_code_cli", **extra):
        args = ["publish", "--member", member, "--to", to,
                "--title", "İş girdisi", "--purpose", "Yeni çalışma başlat",
                "--expected", "Bir sonraki girdi taslağı", "--input", str(self.input)]
        for key, value in extra.items():
            args += ["--" + key.replace("_", "-"), value]
        return self.cli(*args).stdout.strip()

    def member_dir(self, member):
        group = {"codex_cli": "01_codex_karargahi",
                 "claude_code_cli": "01_claude_code_karargahi",
                 "gemini_sohbet": "01_antigravity_karargahi"}[member]
        return self.root / "02_karargahlar" / group / "uyeler" / member

    def inbox(self, member, all_items=False):
        args = ["inbox", "--member", member]
        if all_items:
            args.append("--all")
        return [json.loads(line) for line in self.cli(*args).stdout.splitlines()]

    def test_init_is_repeatable_and_preserves_user_data(self):
        control = self.root / "00_yonetim" / "denetim.json"
        user_data = {"durum": "duraklat", "aciklama": "Kullanıcı denemesi", "ozel": 17}
        control.write_text(json.dumps(user_data), encoding="utf-8")
        note = self.member_dir("codex_cli") / "calisma" / "not.md"
        note.write_text("korunacak", encoding="utf-8")
        self.cli("init")
        self.cli("init")
        self.assertEqual(json.loads(control.read_text()), user_data)
        self.assertEqual(note.read_text(), "korunacak")
        self.cli("doctor")

    def test_existing_registry_adds_cloud_actor_without_replacing_local_status(self):
        path = self.root / "00_yonetim/uyeler.json"
        registry = json.loads(path.read_text(encoding="utf-8"))
        del registry["codex_cloud"]
        registry["codex_cli"]["baglanti"] = "existing-user-evidence"
        registry["codex_cli"]["user_note"] = "must survive"
        path.write_text(json.dumps(registry), encoding="utf-8")
        self.cli("init")
        updated = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(updated["codex_cli"], registry["codex_cli"])
        self.assertEqual(updated["codex_cloud"]["baglanti"], "dogrulanmadi")
        self.cli("doctor")

    def test_cloud_sender_and_windows_cli_are_distinct_actors(self):
        ident = self.publish("codex_cloud", "codex_cli")
        data = json.loads(self.cli("read", ident).stdout)
        self.assertEqual(data["yazar"], "codex_cloud")
        self.assertEqual(self.inbox("codex_cli")[0]["id"], ident)
        self.assertEqual(self.inbox("codex_cloud"), [])

    def test_full_lineage_exchange_keeps_one_local(self):
        first = self.publish()
        self.assertEqual(self.inbox("claude_code_cli")[0]["id"], first)
        self.cli("claim", "--member", "claude_code_cli", first)
        self.assertEqual(self.inbox("claude_code_cli"), [])
        self.assertEqual(self.inbox("claude_code_cli", True)[0]["durum"], "calisiliyor")
        secret_marker = "YALNIZ_YEREL_SONUC_926"
        result_input = Path(self.temp.name) / "result.md"
        result_input.write_text(secret_marker, encoding="utf-8")
        self.cli("complete", "--member", "claude_code_cli", first, "--input", str(result_input))
        result = self.member_dir("claude_code_cli") / "sonuclar_1" / (first + ".md")
        self.assertIn(secret_marker, result.read_text(encoding="utf-8"))
        self.assertEqual(self.inbox("claude_code_cli", True)[0]["durum"], "tamamlandi_1")
        second = self.publish("claude_code_cli", "codex_cli", from_id=first, from_result=first)
        envelope = json.loads(self.cli("read", second).stdout)
        self.assertEqual(envelope["onceki_girdi"], first)
        self.assertEqual(envelope["yazar"], "claude_code_cli")
        self.assertEqual(self.inbox("codex_cli")[0]["id"], second)
        board = self.root / "01_ortak_alan" / "yeni_0"
        self.assertEqual(len(list(board.iterdir())), 2)
        self.assertTrue(all(p.suffix == ".json" for p in board.iterdir()))
        self.assertTrue(all(secret_marker not in p.read_text(encoding="utf-8") for p in board.iterdir()))
        self.cli("doctor")

    def test_targeting_excludes_other_members(self):
        ident = self.publish()
        self.assertEqual(self.inbox("gemini_sohbet"), [])
        self.cli("claim", "--member", "gemini_sohbet", ident, ok=False)
        self.cli("complete", "--member", "gemini_sohbet", ident, "--input", str(self.input), ok=False)
        self.assertFalse((self.member_dir("gemini_sohbet") / "alindi" / (ident + ".json")).exists())

    def test_duplicates_and_unclaimed_complete_rejected(self):
        ident = self.publish()
        self.cli("complete", "--member", "claude_code_cli", ident, "--input", str(self.input), ok=False)
        self.cli("claim", "--member", "claude_code_cli", ident)
        receipt = self.member_dir("claude_code_cli") / "alindi" / (ident + ".json")
        original_receipt = receipt.read_bytes()
        self.cli("claim", "--member", "claude_code_cli", ident, ok=False)
        self.assertEqual(receipt.read_bytes(), original_receipt)
        self.cli("complete", "--member", "claude_code_cli", ident, "--input", str(self.input))
        result = self.member_dir("claude_code_cli") / "sonuclar_1" / (ident + ".md")
        original_result = result.read_bytes()
        self.input.write_text("Önceki sonucun üstüne yazılmamalı", encoding="utf-8")
        self.cli("complete", "--member", "claude_code_cli", ident, "--input", str(self.input), ok=False)
        self.assertEqual(result.read_bytes(), original_result)

    def test_invalid_ids_and_empty_inputs_rejected(self):
        self.cli("read", "../../00_yonetim/denetim", ok=False)
        self.cli("claim", "--member", "codex_cli", "A" * 32, ok=False)
        self.cli("read", "0" * 32, ok=False)
        self.input.write_text(" \n\t", encoding="utf-8")
        self.cli("publish", "--member", "codex_cli", "--to", "all", "--title", "x",
                 "--purpose", "x", "--expected", "x", "--input", str(self.input), ok=False)
        self.assertEqual(list((self.root / "01_ortak_alan" / "yeni_0").iterdir()), [])

    def test_derivation_requires_existing_matching_local_result(self):
        first = self.publish()
        second = self.publish()
        self.cli("publish", "--member", "claude_code_cli", "--to", "codex_cli",
                 "--title", "x", "--purpose", "x", "--expected", "x", "--input", str(self.input),
                 "--from-id", first, "--from-result", first, ok=False)
        self.cli("claim", "--member", "claude_code_cli", first)
        self.cli("complete", "--member", "claude_code_cli", first, "--input", str(self.input))
        self.cli("publish", "--member", "claude_code_cli", "--to", "codex_cli",
                 "--title", "x", "--purpose", "x", "--expected", "x", "--input", str(self.input),
                 "--from-id", second, "--from-result", first, ok=False)

    def test_derived_publish_cannot_omit_local_result_flag(self):
        first = self.publish()
        before = {p.name for p in (self.root / "01_ortak_alan" / "yeni_0").iterdir()}
        for flags in (["--from-id", first], ["--from-result", first]):
            self.cli("publish", "--member", "claude_code_cli", "--to", "codex_cli",
                     "--title", "x", "--purpose", "x", "--expected", "x",
                     "--input", str(self.input), *flags, ok=False)
        after = {p.name for p in (self.root / "01_ortak_alan" / "yeni_0").iterdir()}
        self.assertEqual(before, after)

    def test_derived_publish_requires_addressed_claimed_work(self):
        first = self.publish()
        local = self.member_dir("gemini_sohbet")
        (local / "sonuclar_1" / (first + ".md")).write_text("Dosya var", encoding="utf-8")
        self.cli("publish", "--member", "gemini_sohbet", "--to", "codex_cli",
                 "--title", "x", "--purpose", "x", "--expected", "x",
                 "--input", str(self.input), "--from-id", first, "--from-result", first,
                 ok=False)
        local = self.member_dir("claude_code_cli")
        (local / "sonuclar_1" / (first + ".md")).write_text("Alınmamış iş", encoding="utf-8")
        self.cli("publish", "--member", "claude_code_cli", "--to", "codex_cli",
                 "--title", "x", "--purpose", "x", "--expected", "x",
                 "--input", str(self.input), "--from-id", first, "--from-result", first,
                 ok=False)

    def test_pause_stops_new_work_and_resume_restores_it(self):
        ident = self.publish()
        self.cli("control", "--state", "duraklat", "--reason", "Test: kullanıcı durdurdu")
        self.cli("claim", "--member", "claude_code_cli", ident, ok=False)
        self.cli("publish", "--member", "codex_cli", "--to", "all", "--title", "x",
                 "--purpose", "x", "--expected", "x", "--input", str(self.input), ok=False)
        self.cli("read", ident)
        self.cli("control", "--state", "devam", "--reason", "Test: kullanıcı devam dedi")
        self.cli("claim", "--member", "claude_code_cli", ident)

    def test_doctor_rejects_missing_parent_and_cycles(self):
        first = self.publish()
        second = self.publish()
        board = self.root / "01_ortak_alan" / "yeni_0"
        first_path = board / (first + ".json")
        second_path = board / (second + ".json")
        a = json.loads(first_path.read_text(encoding="utf-8"))
        b = json.loads(second_path.read_text(encoding="utf-8"))
        a["onceki_girdi"] = "f" * 32
        first_path.write_text(json.dumps(a), encoding="utf-8")
        self.cli("doctor", ok=False)
        a["onceki_girdi"] = second
        b["onceki_girdi"] = first
        first_path.write_text(json.dumps(a), encoding="utf-8")
        second_path.write_text(json.dumps(b), encoding="utf-8")
        self.cli("doctor", ok=False)
        b["onceki_girdi"] = None
        second_path.write_text(json.dumps(b), encoding="utf-8")
        self.cli("doctor")
        self.assertFalse(list(board.glob(".divan-probe-*")))

    def test_concurrent_publishing_does_not_clobber_messages(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            ids = list(pool.map(lambda _: self.publish(), range(12)))
        self.assertEqual(len(set(ids)), 12)
        board = self.root / "01_ortak_alan" / "yeni_0"
        self.assertEqual({p.stem for p in board.iterdir()}, set(ids))
        for ident in ids:
            data = json.loads((board / (ident + ".json")).read_text(encoding="utf-8"))
            self.assertEqual(data["id"], ident)
            self.assertEqual(data["girdi"], self.input.read_text(encoding="utf-8"))
        self.cli("doctor")


if __name__ == "__main__":
    unittest.main(verbosity=2)
