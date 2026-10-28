"""schemas/ altındaki sözleşmeler, çekirdeğin gerçekten ürettiği verilerle denetlenir.

Dış paket yok; sağlayıcı, ağ veya canlı CLI çağrısı yok. Amaç, şema dosyalarının
belge olarak durmakla kalmayıp kodun çıktısına bağlı kalmasıdır: kod veya şema
değişip ayrışırsa bu testler kırılır.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from ortak_kopru.core import Store  # noqa: E402
from ortak_kopru.exchange import ExchangeStore  # noqa: E402
from ortak_kopru.handoff import create_handoff  # noqa: E402
import sema_denetle  # noqa: E402


class ValidatorRulesTests(unittest.TestCase):
    """Denetleyicinin kendisi: her desteklenen kural somut bir örnekle sınanır."""

    def assertHatalar(self, sema, veri, *beklenen_parcalar):
        hatalar = sema_denetle.dogrula(sema, veri)
        self.assertTrue(hatalar, f"hata bekleniyordu: {veri!r}")
        birlesik = "\n".join(hatalar)
        for parca in beklenen_parcalar:
            self.assertIn(parca, birlesik)

    def test_every_schema_file_stays_inside_the_supported_subset(self):
        semalar = sema_denetle.butun_semalar()
        self.assertEqual(sorted(semalar), [
            "depo-tanimi.schema.json", "deus-assign-request.schema.json", "deus-checks.schema.json", "deus-event.schema.json",
            "deus-handoff.schema.json", "deus-task.schema.json", "exchange-manifest.schema.json",
            "rafine-bulgu.schema.json"])
        for ad, sema in semalar.items():
            self.assertEqual(sema_denetle.sema_bicimini_denetle(sema), [], ad)
            self.assertIn("title", sema, ad)

    def test_unsupported_keywords_and_broken_refs_are_reported_not_ignored(self):
        self.assertEqual(sema_denetle.sema_bicimini_denetle({"type": "object", "allOf": []}),
                         ["#: desteklenmeyen anahtar 'allOf'"])
        self.assertEqual(sema_denetle.sema_bicimini_denetle({"$ref": "#/$defs/yok"}),
                         ["#: $ref çözülemedi: #/$defs/yok"])
        self.assertEqual(sema_denetle.sema_bicimini_denetle(
            {"type": "object", "additionalProperties": False, "required": ["a"], "properties": {}}),
            ["#: zorunlu 'a' properties içinde tanımlı değil"])
        self.assertEqual(sema_denetle.sema_bicimini_denetle({"type": "string", "pattern": "("})[0][:21],
                         "#: geçersiz desen (mi")
        self.assertEqual(sema_denetle.sema_bicimini_denetle({"type": "string", "format": "uri"}),
                         ["#: desteklenmeyen biçim 'uri'"])

    def test_type_const_enum_and_bool_integer_distinction(self):
        self.assertEqual(sema_denetle.dogrula({"type": "integer"}, 3), [])
        self.assertEqual(sema_denetle.dogrula({"type": "integer"}, 3.0), [])
        self.assertHatalar({"type": "integer"}, True, "tür integer bekleniyor")
        self.assertHatalar({"type": "integer"}, 3.5, "tür integer bekleniyor")
        self.assertHatalar({"type": "number"}, "3", "tür number bekleniyor")
        self.assertEqual(sema_denetle.dogrula({"const": 1}, 1), [])
        self.assertHatalar({"const": 1}, True, "1 olmalı")
        self.assertHatalar({"const": False}, 0, "False olmalı")
        self.assertHatalar({"enum": ["a", "b"]}, "c", "izin verilen değerlerden değil")
        self.assertEqual(sema_denetle.dogrula({"type": "null"}, None), [])

    def test_string_number_and_array_bounds(self):
        self.assertHatalar({"type": "string", "minLength": 2}, "a", "en az 2 karakter")
        self.assertHatalar({"type": "string", "maxLength": 1}, "ab", "en çok 1 karakter")
        self.assertHatalar({"type": "string", "pattern": "^[0-9a-f]{4}$"}, "zzzz", "desenine uymuyor")
        self.assertEqual(sema_denetle.dogrula({"type": "string", "format": "date-time"}, "2026-10-28T09:33:00+00:00"), [])
        self.assertEqual(sema_denetle.dogrula({"type": "string", "format": "date-time"}, "2026-10-28T09:33:00.123456Z"), [])
        self.assertHatalar({"type": "string", "format": "date-time"}, "28 Ekim 2026", "date-time biçiminde değil")
        self.assertHatalar({"type": "integer", "minimum": 1}, 0, "en az 1")
        self.assertHatalar({"type": "integer", "maximum": 5}, 6, "en çok 5")
        self.assertHatalar({"type": "array", "minItems": 1}, [], "en az 1 öğe")
        self.assertHatalar({"type": "array", "maxItems": 1}, [1, 2], "en çok 1 öğe")
        self.assertHatalar({"type": "array", "items": {"type": "string"}}, ["a", 1], "$[1]: tür string")

    def test_objects_required_additional_properties_and_local_refs(self):
        sema = {"type": "object", "additionalProperties": False, "required": ["id"],
                "properties": {"id": {"$ref": "#/$defs/hex"}, "etiket": {"type": "string"}},
                "$defs": {"hex": {"type": "string", "pattern": "^[0-9a-f]{4}$"}}}
        self.assertEqual(sema_denetle.dogrula(sema, {"id": "0abc", "etiket": "x"}), [])
        self.assertHatalar(sema, {"etiket": "x"}, "zorunlu alan 'id' yok")
        self.assertHatalar(sema, {"id": "0abc", "fazla": 1}, "beklenmeyen alan 'fazla'")
        self.assertHatalar(sema, {"id": "XYZ"}, "$.id: ")
        acik = {"type": "object", "additionalProperties": {"type": "integer"}}
        self.assertEqual(sema_denetle.dogrula(acik, {"a": 1}), [])
        self.assertHatalar(acik, {"a": "1"}, "$.a: tür integer")

    def test_one_of_requires_exactly_one_matching_branch(self):
        sema = {"oneOf": [{"type": "string", "pattern": "^[0-9a-f]{32}$"}, {"type": "null"}]}
        self.assertEqual(sema_denetle.dogrula(sema, None), [])
        self.assertEqual(sema_denetle.dogrula(sema, "0" * 32), [])
        self.assertHatalar(sema, "kısa", "oneOf dallarından tam biri uymalı (0 uydu)")
        belirsiz = {"oneOf": [{"type": "integer"}, {"type": "number"}]}
        self.assertHatalar(belirsiz, 1, "(2 uydu)")

    def test_command_line_reports_shape_and_data_results(self):
        with tempfile.TemporaryDirectory() as tmp:
            veri = Path(tmp) / "olay.json"
            veri.write_text(json.dumps({"seq": 1, "id": "a" * 32, "task_id": "b" * 32, "revision": 1,
                                        "kind": "task_created", "at": "2026-10-28T00:00:00+00:00", "data": {}}),
                            encoding="utf-8")
            ok = subprocess.run([sys.executable, "-I", str(ROOT / "tools/sema_denetle.py"),
                                 "--sema", "deus-event", "--veri", str(veri)],
                                capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
            self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
            self.assertIn("UYUMLU", ok.stdout)
            veri.write_text(json.dumps({"seq": 0}), encoding="utf-8")
            bad = subprocess.run([sys.executable, "-I", str(ROOT / "tools/sema_denetle.py"),
                                  "--sema", "deus-event", "--veri", str(veri)],
                                 capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
            self.assertEqual(bad.returncode, 1)
            self.assertIn("zorunlu alan 'id' yok", bad.stdout)
            self.assertIn("$.seq: en az 1", bad.stdout)
        shape = subprocess.run([sys.executable, "-I", str(ROOT / "tools/sema_denetle.py")],
                               capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(shape.returncode, 0, shape.stdout + shape.stderr)
        self.assertIn("8 şema", shape.stdout)


class CoreOutputContractTests(unittest.TestCase):
    """Çekirdeğin ürettiği gerçek nesneler sözleşmelere uyar; uydurulmuş örnek kullanılmaz."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-sema-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.store = Store(self.root / "private")
        self.counter = 0
        self.semalar = {ad.removesuffix(".schema.json"): sema for ad, sema in sema_denetle.butun_semalar().items()}

    def key(self):
        self.counter += 1
        return f"sema-request-{self.counter}"

    def uyumlu(self, sema_adi, veri, etiket=""):
        hatalar = sema_denetle.dogrula(self.semalar[sema_adi], veri)
        self.assertEqual(hatalar, [], f"{sema_adi} {etiket}: " + "; ".join(hatalar))

    def test_task_projection_events_checks_and_assign_request_follow_their_contracts(self):
        source = self.root / "kaynak.txt"
        source.write_bytes("özgün kaynak\n".encode())
        task = self.store.create_task("  Kaynağı incele.\nÖzgün sözümü koru.  ",
                                      {"actor": "Haluk", "source": "current-local-input", "scope": "selected file review"},
                                      ["Kaynak aynı", "Sonuç denetlendi"], self.key(), sources=[str(source)])
        self.uyumlu("deus-task", task, "ready")
        assign_request = {"participant": "ChatGPT (Şaman)", "session_id": "session-A", "expected_revision": task["revision"],
                          "request_key": self.key(), "expected_active_attempt_id": task["active_attempt_id"]}
        self.uyumlu("deus-assign-request", assign_request)
        assigned = self.store.assign(task["id"], assign_request["participant"], assign_request["session_id"],
                                     assign_request["expected_revision"], assign_request["request_key"],
                                     expected_active_attempt_id=assign_request["expected_active_attempt_id"])
        self.uyumlu("deus-task", assigned, "assigned")
        attempt = assigned["active_attempt_id"]
        received = self.store.receive(attempt, "session-A", self.key())
        self.assertEqual(set(received), {"task", "context"})
        self.uyumlu("deus-task", received["task"], "running")
        artifact = self.root / "sonuc.txt"
        artifact.write_bytes(b"actual output")
        result = self.store.submit_result(attempt, "session-A", "Gerçek dosya", [str(artifact)], self.key())
        self.uyumlu("deus-task", result, "awaiting_verification")
        checks = [{"criterion_id": criterion["id"], "result_id": result["current_result_id"], "passed": True,
                   "evidence": "fixture check result", "verifier": "offline test"} for criterion in result["criteria"]]
        self.uyumlu("deus-checks", checks)
        done = self.store.verify_task(task["id"], checks, 1, self.key())
        self.uyumlu("deus-task", done, "completed")
        self.assertEqual(done["status"], "completed")
        self.uyumlu("deus-checks", done["verification"], "recorded")
        events = self.store.events(task["id"])
        self.assertEqual([event["kind"] for event in events][:3], ["task_created", "attempt_assigned", "attempt_received"])
        for event in events:
            self.uyumlu("deus-event", event, event["kind"])
        other = self.store.create_task("İkinci iş", {"actor": "Haluk", "source": "current-local-input",
                                                     "scope": "fixture"}, ["Ölçüt"], self.key())
        revised = self.store.revise_task(other["id"], "Düzeltilmiş söz", other["revision"], self.key())
        self.assertEqual(revised["revision"], 2)
        self.uyumlu("deus-task", revised, "revised")
        paused = self.store.control_task(other["id"], "pause", revised["revision"], self.key())
        self.uyumlu("deus-task", paused, "paused")
        for event in self.store.events(other["id"]):
            self.uyumlu("deus-event", event, event["kind"])

    def test_handoff_manifest_follows_its_contract(self):
        source = self.root / "kaynak.bin"
        source.write_bytes(b"\xff\x00source bytes")
        task = self.store.create_task("Bu işi aynen sürdür.", {"actor": "Local owner", "source": "offline fixture",
                                                               "scope": "fixture files"}, ["Result checked"],
                                      self.key(), sources=[str(source)])
        assigned = self.store.assign(task["id"], "Local receiver", "session-A", 1, self.key())
        manifest = create_handoff(self.store, assigned["active_attempt_id"], "session-A", self.root / "handoff")
        self.uyumlu("deus-handoff", manifest, "assigned")
        self.assertEqual(manifest["preparation"]["task_status"], "ready")
        self.store.receive(assigned["active_attempt_id"], "session-A", self.key())
        received = create_handoff(self.store, assigned["active_attempt_id"], "session-A", self.root / "handoff-2")
        self.uyumlu("deus-handoff", received, "received")
        self.assertEqual(received["preparation"]["task_status"], "running")

    def test_exchange_manifest_follows_its_contract(self):
        source = self.root / "rapor.txt"
        source.write_bytes(b"selected bytes\x00\xff")
        store = ExchangeStore(self.root / "exchange")
        record = store.prepare_outbound([{"source": str(source), "path": "reports/result.bin"}],
                                        {"provider": "github", "repository": "example/project", "base_ref": "main"},
                                        "Seçilmiş raporu paylaş", "prepare-1")
        self.uyumlu("exchange-manifest", record["manifest"], "in-memory")
        written = json.loads((store.packages / record["id"] / "manifest.json").read_text(encoding="utf-8"))
        self.uyumlu("exchange-manifest", written, "on-disk")


class RafineKayitTests(unittest.TestCase):
    """docs/rafine/ altındaki her bulgu kaydı kendi sözleşmesine uyar ve kimlikleri tekildir."""

    def test_every_refinement_record_follows_its_contract(self):
        sema = sema_denetle.sema_yukle("rafine-bulgu")
        kayitlar = sorted((ROOT / "docs" / "rafine").glob("*.json"))
        self.assertTrue(kayitlar)
        for yol in kayitlar:
            veri = json.loads(yol.read_text(encoding="utf-8"))
            with self.subTest(kayit=yol.name):
                self.assertEqual(sema_denetle.dogrula(sema, veri), [])
                kimlikler = [bulgu["id"] for bulgu in veri["findings"]]
                self.assertEqual(len(kimlikler), len(set(kimlikler)))
                for bulgu in veri["findings"]:
                    if bulgu["resolution"] == "düzeltildi":
                        self.assertTrue(bulgu.get("change"), bulgu["id"])


if __name__ == "__main__":
    unittest.main()
