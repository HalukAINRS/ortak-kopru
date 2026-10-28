"""Çevrimdışı bakım sınamaları: yalnız geçici sayfalar ve sahte çağrılar."""
from concurrent.futures import ThreadPoolExecutor
import contextlib
import datetime
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "defter"))
import kopru_yanitla as bot
from kopru_oku import Ayristirici

ROOT = Path(__file__).resolve().parents[1]


class AppenderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.page = Path(self.temp.name) / "kopru.html"
        self.page.write_text('<html><body><!-- KAYIT-SONU --></body></html>', encoding="utf-8")

    def append(self, sender="Sen", body="Çevrimdışı sınama.", reply=""):
        return subprocess.run(
            [sys.executable, str(ROOT / "defter" / "kopru_ekle.py"), str(self.page),
             "--kimden", sender, "--kime", "Sen", "--konu", "Bakım sınaması",
             "--govde", body, "--yanit", reply],
            capture_output=True, text=True, encoding="utf-8", check=False,
        )

    def test_configured_google_signature_can_append(self):
        settings = json.loads((ROOT / "katilimcilar" / "ayarlar-yerel.json").read_text(encoding="utf-8"))
        google = next(p for p in settings["katilimcilar"] if p["ad"] == "Google")
        signature = bot.yol_kimligi(google["ad"], google, google)
        result = self.append(sender=signature)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(bot.kayitlari_oku(self.page)[0]["kimden"], "Google (CLI izleyici)")

    def test_reply_requires_record_not_merely_an_id_mention(self):
        self.assertEqual(self.append(body="Burada k-0099 yalnız metin olarak anılır.").returncode, 0)
        before = self.page.read_bytes()
        result = self.append(reply="k-0099")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("k-0099 sayfada yok", result.stderr)
        self.assertEqual(self.page.read_bytes(), before)

    def test_existing_reply_and_last_alias_still_work(self):
        self.assertEqual(self.append().returncode, 0)
        self.assertEqual(self.append(reply="k-0001").returncode, 0)
        self.assertEqual(self.append(reply="son").returncode, 0)
        self.assertEqual([r["yanit"] for r in bot.kayitlari_oku(self.page)], [None, "k-0001", "k-0002"])


class ParserTests(unittest.TestCase):
    def parse(self, body):
        parser = Ayristirici()
        parser.feed('<article class="kayit" id="k-0001"><h3>Başlık</h3>'
                    f'<div class="govde">{body}</div><footer>Dayanak: sınama</footer></article>')
        parser.close()
        return parser.kayitlar

    def test_void_elements_preserve_record_and_following_fields(self):
        for tag, separator in (("<br>", "\n"), ("<br/>", "\n"), ("<hr>", "\n\n"),
                               ("<hr/>", "\n\n"), ("<wbr>", "")):
            with self.subTest(tag=tag):
                records = self.parse(f"Bir{tag}İki")
                self.assertEqual(len(records), 1)
                self.assertEqual(records[0]["konu"], "Başlık")
                self.assertEqual(records[0]["govde"], f"Bir{separator}İki")
                self.assertEqual(records[0]["dayanak"], "sınama")

    def test_record_class_is_a_token(self):
        parser = Ayristirici()
        parser.feed('<article class="kayitlik" id="k-0001"><h3>Kayıt değil</h3></article>'
                    '<article class="kayit sablon" id="sablon"></article>'
                    '<article class="ek kayit" id="k-0002"><h3>Gerçek</h3></article>')
        self.assertEqual([r["id"] for r in parser.kayitlar], ["k-0002"])


class LogTests(unittest.TestCase):
    def test_same_second_concurrent_logs_never_overwrite(self):
        fixed = datetime.datetime(2026, 10, 26, 12, 0, tzinfo=datetime.timezone.utc)
        with tempfile.TemporaryDirectory() as directory, patch.object(bot, "KOK", directory), \
                patch.object(bot.datetime, "datetime") as clock:
            clock.now.return_value = fixed
            def write(index):
                raw = f"Sınama yanıtı {index}"
                path = bot.kayit_yaz("Google", "sahte", "cli", "sistem", "girdi", raw, "tamam")
                return path, raw
            with ThreadPoolExecutor(max_workers=8) as pool:
                results = list(pool.map(write, range(8)))
            self.assertEqual(len({p for p, _ in results}), 8)
            for path, raw in results:
                self.assertIn(raw, Path(path).read_text(encoding="utf-8"))


class IdentityTests(unittest.TestCase):
    def test_api_route_cannot_claim_google_cli_watcher_identity(self):
        participant = dict(ad="Google", saglayici="cli", imza="Google (CLI izleyici)")
        self.assertEqual(bot.yol_kimligi("Google", participant, {"saglayici": "google"}), "Google (API)")
        with self.assertRaises(ValueError):
            bot.yol_kimligi("Google", participant, {"saglayici": "google", "imza": "Google (CLI izleyici)"})

    def test_google_gemini_and_historical_copilot_remain_distinct(self):
        records = [dict(id=f"k-{i:04d}", kime=target, kimden="Sen", durum="acik", yanit=None)
                   for i, target in enumerate(("Google (CLI izleyici)", "Gemini (Şahit)", "Şahit"), 1)]
        records.append(dict(id="k-0004", kime="Sen", kimden="Google (CLI izleyici)",
                            durum="acik", yanit="k-0001"))
        self.assertEqual(bot.bekleyenler(records, "Google (CLI izleyici)"), [])
        self.assertEqual([r["id"] for r in bot.bekleyenler(records, "Gemini (Şahit)")], ["k-0002"])
        self.assertEqual([r["id"] for r in bot.bekleyenler(records, "Copilot (Şahit)")], ["k-0003"])


class ExitStatusTests(unittest.TestCase):
    def run_bot(self, participants, api_error=None, cli_error=None, raw='{"konu":"Sınama","govde":"Yanıt"}', append_error=None):
        records = [dict(id="k-0001", kime="ChatGPT, Claude", kimden="Sen", durum="acik", yanit=None)]
        with tempfile.TemporaryDirectory() as directory:
            settings = Path(directory) / "ayarlar.json"
            settings.write_text(json.dumps({"katilimcilar": participants}), encoding="utf-8")
            args = ["kopru_yanitla.py", "sahte.html", "--ayarlar", str(settings)]
            with patch.object(sys, "argv", args), \
                    patch.object(bot, "kayitlari_oku", return_value=records), \
                    patch.object(bot, "istem_kur", return_value=("sistem", "girdi")), \
                    patch.object(bot, "cagir", return_value=(raw, {}), side_effect=api_error) as api, \
                    patch.object(bot, "cli_cagir", return_value=(raw, {}), side_effect=cli_error), \
                    patch.object(bot, "ekle", return_value="k-0002", side_effect=append_error) as append, \
                    patch.object(bot, "kayit_yaz", return_value="sahte.md") as log, \
                    patch.object(bot, "atlandi_yaz") as skipped, \
                    patch.dict(bot.os.environ, {}, clear=True), \
                    contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                try:
                    bot.main()
                    status = 0
                except SystemExit as error:
                    status = error.code
                return status, api.call_count, append.call_count, log.call_args_list, skipped.call_count

    def api_participant(self):
        return {"ad": "ChatGPT", "saglayici": "openai", "model": "sahte"}

    def test_missing_credentials_remain_successful_skip(self):
        participant = self.api_participant()
        participant["anahtar_degiskeni"] = "KOPRU_TEST_MISSING_KEY"
        status, calls, writes, _, skipped = self.run_bot([participant])
        self.assertEqual((status, calls, writes, skipped), (0, 0, 0, 1))

    def test_missing_cli_remains_successful_skip(self):
        participant = dict(ad="ChatGPT", saglayici="cli", komut=["sahte-cli"])
        status, _, writes, _, skipped = self.run_bot([participant], cli_error=bot.KomutYok("sahte-cli"))
        self.assertEqual((status, writes, skipped), (0, 0, 1))

    def test_attempted_provider_failure_is_nonzero(self):
        status, calls, writes, _, skipped = self.run_bot([self.api_participant()], api_error=RuntimeError("sınama hatası"))
        self.assertEqual((status, calls, writes, skipped), (1, 1, 0, 1))

    def test_successful_fallback_clears_route_error(self):
        participant = dict(ad="ChatGPT", saglayici="cli", komut=["sahte-cli"], yedek=self.api_participant())
        status, calls, writes, _, _ = self.run_bot([participant], cli_error=RuntimeError("sınama hatası"))
        self.assertEqual((status, calls, writes), (0, 1, 1))

    def test_invalid_response_is_logged_and_nonzero(self):
        status, _, writes, logs, _ = self.run_bot([self.api_participant()], raw="JSON olmayan yanıt")
        self.assertEqual((status, writes, len(logs)), (1, 0, 1))
        self.assertIn("HATA:", logs[0].args[-1])

    def test_appender_rejection_is_logged_and_nonzero(self):
        status, _, writes, logs, _ = self.run_bot([self.api_participant()], append_error=RuntimeError("kayıt reddedildi"))
        self.assertEqual((status, writes, len(logs)), (1, 1, 1))
        self.assertIn("HATA:", logs[0].args[-1])

    def test_other_participants_finish_before_failure_exit(self):
        participants = [self.api_participant(), dict(ad="Claude", saglayici="anthropic", model="sahte")]
        errors = [RuntimeError("ilk sağlayıcı hatası"), ('{"konu":"Sınama","govde":"Yanıt"}', {})]
        status, calls, writes, logs, _ = self.run_bot(participants, api_error=errors)
        self.assertEqual((status, calls, writes, len(logs)), (1, 2, 1, 1))


if __name__ == "__main__":
    unittest.main()
