"""Kök köprü araçlarının doğrudan regresyonları: yasak desenler, dış yükleme, JSON girişi, bölüm parçası, yanıtlayıcı süzgeci.

Sentetik sayfa ve geçici dizin kullanılır; kanonik kopru.html'e yazılmaz, sağlayıcı veya ağ çağrısı yapılmaz.
"""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import unittest.mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "defter"))

from kopru_ekle import dis_yukleme_kontrol, yasak_kontrol  # noqa: E402
import kopru_yanitla  # noqa: E402

SAYFA = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>Sentetik köprü</title>
<style>body { color: black; }</style>
</head>
<body>
<header>
<h1>Sentetik köprü</h1>
<p>Kayıt: <b id="kayit-sayisi">0</b></p>
<time id="son-guncelleme" datetime="2026-10-01T00:00:00+00:00">1 Eki 2026 00.00</time>
<p>Son kayıt: <a href="#k-0000">k-0000</a></p>
</header>
<section id="yonlendirme" class="dosya">
  <h2>Yönlendirme dosyası</h2>
  <div id="y-mimari" class="alt">
    <p>Mimari: ikimiz için.</p>
  </div>
</section>
<!-- KAYIT-SONU -->
</body>
</html>
'''


class YasakDesenTests(unittest.TestCase):
    def test_real_addresses_and_credentials_are_still_refused(self):
        for metin, beklenen in [
            ("bağlantı 192.168.1.20 üzerinden", "IP adresi"),
            ("ssh hacker@10.0.0.5", "IP adresi"),
            ("(8.8.8.8)", "IP adresi"),
            ("IP:172.16.0.1", "IP adresi"),
            ("550e8400-e29b-41d4-a716-446655440000", "UUID (cihaz ya da oturum kimliği olabilir)"),
            ("550E8400-E29B-41D4-A716-446655440000", "UUID (cihaz ya da oturum kimliği olabilir)"),
            ("ghp_" + "a" * 36, "GitHub belirteci"),
            ("sk-ant-" + "b" * 20, "Anthropic anahtarı"),
        ]:
            with self.subTest(metin=metin):
                self.assertIn(beklenen, yasak_kontrol(metin))

    def test_version_strings_attached_to_names_are_not_addresses(self):
        for metin in ("Git-Portable-2.56.0.2", r"Y:\x\Git-Portable-2.56.0.2\usr\bin\ssh.exe", "v1.2.3.4", "paket_1.2.3.4",
                      "999.1.1.1", "1.2.3", "2026.10.28"):
            with self.subTest(metin=metin):
                self.assertNotIn("IP adresi", yasak_kontrol(metin))

    def test_known_limit_bare_four_part_version_is_still_treated_as_address(self):
        # Boşlukla ayrılmış dört parçalı ve 0-255 aralığındaki sayı dizisi bağlamsız IP'den ayırt edilemez.
        self.assertIn("IP adresi", yasak_kontrol("python 3.14.9.1 sürümü"))


class DisYuklemeTests(unittest.TestCase):
    def test_loading_tags_and_attributes_are_reported(self):
        for parca in [
            '<script src="https://x/a.js"></script>',
            '<img src="//x/a.png">',
            '<link rel="stylesheet" href="https://x/a.css">',
            '<link rel="icon" href="https://x/f.ico">',
            '<link rel="modulepreload" href=https://x/y.js>',
            '<link rel="preload" as="script" href="https://x/y.js">',
            '<link rel="dns-prefetch" href="//x">',
            '<img srcset="a.png 1x, https://x/b.png 2x">',
            '<video poster="//x/p.jpg"></video>',
            '<object data="https://x/o"></object>',
            '<form action="https://x/f"></form>',
            '<button formaction="https://x/f">g</button>',
            '<style>@import "https://x/a.css";</style>',
            '<style>@import url(https://x/a.css);</style>',
            '<style>body{background:url("https://x/b.png")}</style>',
            '<meta http-equiv="refresh" content="0;url=https://x">',
        ]:
            with self.subTest(parca=parca):
                self.assertTrue(dis_yukleme_kontrol(parca))

    def test_links_escaped_bodies_and_data_attributes_are_not_loads(self):
        for parca in [
            '<a href="https://github.com/HalukAINRS/ortak-kopru">depo</a>',
            '<link rel="canonical" href="https://halukainrs.github.io/ortak-kopru/">',
            '<div data-kime="Sen, Claude" data-durum="acik"></div>',
            '&lt;img src="https://x/a.png"&gt;',
            '<img src="yerel.png">',
            '<meta http-equiv="refresh" content="300">',
            SAYFA,
        ]:
            with self.subTest(parca=parca[:40]):
                self.assertEqual(dis_yukleme_kontrol(parca), [])

    def test_canonical_page_passes_the_extended_rules(self):
        belge = (ROOT / "kopru.html").read_text(encoding="utf-8")
        self.assertEqual(dis_yukleme_kontrol(belge), [])
        self.assertEqual(yasak_kontrol(belge), [])


class AracKomutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="kopru-arac-")
        self.addCleanup(self.tmp.cleanup)
        self.dizin = Path(self.tmp.name)
        self.sayfa = self.dizin / "kopru.html"
        self.sayfa.write_text(SAYFA, encoding="utf-8", newline="\n")

    def calistir(self, betik, *args):
        return subprocess.run([sys.executable, str(ROOT / "defter" / betik), *map(str, args)], capture_output=True,
                              text=True, encoding="utf-8", cwd=self.dizin, timeout=60)

    def ekle(self, *args):
        return self.calistir("kopru_ekle.py", self.sayfa, *args)

    def kayitlar(self):
        sonuc = self.calistir("kopru_oku.py", self.sayfa)
        self.assertEqual(sonuc.returncode, 0, sonuc.stderr)
        return json.loads(sonuc.stdout)["kayitlar"]

    def test_json_input_is_extracted_from_surrounding_text_and_command_line_wins(self):
        govde = self.dizin / "yanit.json"
        govde.write_text('Model çıktısı:\n```json\n{"kimden": "Gemini (Şahit)", "kime": "Sen", "konu": "JSON konu",'
                         ' "govde": "Birinci.\\n\\n- madde", "dayanak": "k-0000 yok"}\n```\nson satır', encoding="utf-8")
        sonuc = self.ekle("--json", govde, "--kimden", "Gemini (API)")
        self.assertEqual(sonuc.returncode, 0, sonuc.stderr + sonuc.stdout)
        kayit = self.kayitlar()[0]
        self.assertEqual((kayit["id"], kayit["kimden"], kayit["konu"], kayit["durum"]),
                         ("k-0001", "Gemini (API)", "JSON konu", "acik"))
        self.assertIn("madde", kayit["govde"])

    def test_reply_to_last_record_and_missing_reply_target(self):
        self.assertEqual(self.ekle("--kimden", "Sen", "--kime", "Claude", "--konu", "İlk", "--govde", "Gövde").returncode, 0)
        ikinci = self.ekle("--kimden", "Claude (Hacker)", "--kime", "Sen", "--konu", "Yanıt", "--govde", "Gövde", "--yanit", "son")
        self.assertEqual(ikinci.returncode, 0, ikinci.stderr)
        self.assertEqual(self.kayitlar()[1]["yanit"], "k-0001")
        yok = self.ekle("--kimden", "Sen", "--kime", "Claude", "--konu", "Yok", "--govde", "Gövde", "--yanit", "k-0099")
        self.assertNotEqual(yok.returncode, 0)
        self.assertIn("sayfada yok", yok.stderr)

    def test_refused_record_and_unknown_sender_leave_page_unchanged(self):
        once = self.sayfa.read_bytes()
        ip = self.ekle("--kimden", "Sen", "--kime", "Claude", "--konu", "Adres", "--govde", "sunucu 192.168.1.20")
        self.assertNotEqual(ip.returncode, 0)
        self.assertIn("REDDEDİLDİ", ip.stderr)
        kim = self.ekle("--kimden", "Bilinmeyen", "--kime", "Sen", "--konu", "x", "--govde", "y")
        self.assertNotEqual(kim.returncode, 0)
        self.assertEqual(self.sayfa.read_bytes(), once)
        surum = self.ekle("--kimden", "Claude (Hacker)", "--kime", "Sen", "--konu", "Sürüm",
                          "--govde", r"Git-Portable-2.56.0.2\usr\bin\ssh.exe ile bağlanıldı")
        self.assertEqual(surum.returncode, 0, surum.stderr)

    def test_responder_rejects_unknown_participant_filter_instead_of_doing_nothing(self):
        sonuc = self.calistir("kopru_yanitla.py", self.sayfa, "--ayarlar", ROOT / "katilimcilar" / "ayarlar.json", "--yalniz", "Copilot", "--kuru")
        self.assertEqual(sonuc.returncode, 1)
        self.assertIn("--yalniz 'Copilot' bu ayar dosyasında yok", sonuc.stderr)
        self.assertIn("Claude, ChatGPT, Gemini", sonuc.stderr)


class YanitlayiciMetinTests(unittest.TestCase):
    def test_cloud_cli_route_does_not_receive_api_keys(self):
        ayar = json.loads((ROOT / "katilimcilar" / "ayarlar.json").read_text(encoding="utf-8"))
        claude = next(kat for kat in ayar["katilimcilar"] if kat["saglayici"] == "cli")
        self.assertEqual(claude["ortam"], {"ANTHROPIC_API_KEY": None, "OPENAI_API_KEY": None, "GEMINI_API_KEY": None})
        self.assertEqual(claude["yedek"]["anahtar_degiskeni"], "ANTHROPIC_API_KEY")

    def test_null_environment_entries_are_removed_from_the_cli_process(self):
        komut = [sys.executable, "-c", "import os, sys; sys.stdin.read(); "
                 "print(os.environ.get('ANTHROPIC_API_KEY', 'YOK'), os.environ.get('CLAUDE_CODE_OAUTH_TOKEN', 'YOK'))"]
        with unittest.mock.patch.dict("os.environ", {"ANTHROPIC_API_KEY": "sentetik-api", "CLAUDE_CODE_OAUTH_TOKEN": "sentetik-abonelik"}):
            cikti, _ = kopru_yanitla.cli_cagir(komut, "sistem", "kullanici", "stdin", "Claude", 60,
                                               {"ANTHROPIC_API_KEY": None})
        self.assertEqual(cikti.split(), ["YOK", "sentetik-abonelik"])


class IstemSablonuTests(unittest.TestCase):
    """28 Ekim 2026'da sıfırlanan bot istemi yalnız yanıt biçimini ve yasak içeriği taşır."""

    def test_bot_prompt_carries_only_the_reply_format(self):
        sistem, kullanici = kopru_yanitla.sablon_oku()
        for alan in ('"kime"', '"konu"', '"govde"', '"dayanak"'):
            self.assertIn(alan, sistem)
        self.assertIn("reddeder", sistem)
        # Rol, kişilik ve defterin kural ya da yönlendirme metni istemle gönderilmez.
        for iz in ("{ad}", "katılımcısısın", "{kurallar_metni}", "{dosya_metni}", "İş emri", "Haluk"):
            self.assertNotIn(iz, sistem + kullanici)
        for alan in ("{bekleyen_idler}", "{hedef_id}", "{bekleyen_json}", "{kayitlar_json}"):
            self.assertIn(alan, kullanici)
        self.assertLess(len(sistem.split()), 80)


if __name__ == "__main__":
    unittest.main()
