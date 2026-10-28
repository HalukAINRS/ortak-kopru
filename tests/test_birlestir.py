"""Sentetik HTML ve geçici Git depoları: gerçek köprüye veya uzak sunucuya yazılmaz."""
import contextlib
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "defter"))
import kopru_birlestir as birlestir


SAYFA = '''<!DOCTYPE html>
<html><head><title>Sentetik köprü</title><style>body { color: black; }</style></head>
<body><header><b id="kayit-sayisi">0</b>
<time id="son-guncelleme" datetime="">Henüz yok</time>
Son kayıt: <a href="#k-0000">k-0000</a></header>
<section id="yonlendirme"><h2>Kurallar</h2><p>Sentetik bağlam.</p></section>
<section id="kayitlar">
<!-- KAYIT-SONU -->
</section></body></html>
'''


class MergeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.output = self.root / 'output.html'
        self.serial = 0

    def page(self, *records, source=SAYFA):
        self.serial += 1
        path = self.root / f'fixture-{self.serial}.html'
        path.write_text(source, encoding='utf-8')
        for record in records:
            fields = {
                'kimden': 'ChatGPT (GitHub incelemesi)', 'kime': 'Sen',
                'govde': 'Sentetik gövde.', 'dayanak': 'sentetik test', 'durum': 'kapandi',
                'zaman': '2026-10-26T12:00:00+00:00',
            }
            fields.update(record)
            birlestir.ekle(str(path), fields)
        return path.read_text(encoding='utf-8')

    def merge(self, remote, local, base=None):
        with contextlib.redirect_stdout(io.StringIO()):
            if base is None:
                result = birlestir.birlestir(remote, local, str(self.output))
            else:
                result = birlestir.birlestir(remote, local, str(self.output), base)
        return result, self.output.read_text(encoding='utf-8')

    def test_concurrent_records_replies_and_raw_markup_are_preserved(self):
        base = self.page({'konu': 'Ortak'})
        remote = self.page({'konu': 'Uzak'}, source=base)
        local = self.page({'konu': 'Yerel'}, {'konu': 'Yerel yanıt', 'yanit': 'k-0002'}, source=base)
        # Zengin HTML yalnız yeni kayda ait olsun; ortak geçmiş değişmez.
        index = local.index('<article class="kayit" id="k-0002"')
        local = local[:index] + local[index:].replace('<p>Sentetik gövde.</p>',
            '<p><strong>Sentetik</strong> <a href="https://github.com/example/project">gövde</a>.</p>', 1)
        mapping, merged = self.merge(remote, local, base)
        self.assertEqual(mapping, {'k-0002': 'k-0003', 'k-0003': 'k-0004'})
        records = birlestir.kayitlar(merged)
        self.assertEqual([r['konu'] for r in records], ['Ortak', 'Uzak', 'Yerel', 'Yerel yanıt'])
        self.assertEqual(records[-1]['yanit'], 'k-0003')
        self.assertIn('Yanıt: <a href="#k-0003">k-0003</a>', merged)
        remote_blocks = birlestir.KAYIT.findall(remote)
        self.assertEqual(birlestir.KAYIT.findall(merged)[:2], remote_blocks)
        expected = birlestir.numarala(birlestir.KAYIT.findall(local)[1], 'k-0002', 'k-0003', '', '')
        self.assertEqual(birlestir.KAYIT.findall(merged)[2], expected)
        self.assertIn('<b id="kayit-sayisi">4</b>', merged)
        again, repeated = self.merge(merged, local, base)
        self.assertEqual(again, {})
        self.assertEqual(repeated, merged)

    def test_reply_to_shared_record_uses_its_remote_number(self):
        remote = self.page({'konu': 'Başka uzak kayıt'}, {'konu': 'Ortak kayıt'})
        local = self.page({'konu': 'Ortak kayıt'}, {'konu': 'Yanıt', 'yanit': 'k-0001'})
        _, merged = self.merge(remote, local)
        self.assertEqual(birlestir.kayitlar(merged)[-1]['yanit'], 'k-0002')

    def test_same_identity_with_different_body_is_not_silently_dropped(self):
        remote = self.page({'konu': 'Aynı konu', 'govde': 'Birinci içerik.'})
        local = self.page({'konu': 'Aynı konu', 'govde': 'İkinci içerik.'})
        self.output.write_text('önceki çıktı', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'farklı içerik'):
            self.merge(remote, local)
        self.assertEqual(self.output.read_text(encoding='utf-8'), 'önceki çıktı')

    def test_same_identity_with_different_markup_is_not_discarded(self):
        remote = self.page({'konu': 'Ortak'})
        local = remote.replace('<p>Sentetik gövde.</p>', '<p><b>Sentetik</b> gövde.</p>')
        with self.assertRaisesRegex(ValueError, 'farklı içerik'):
            self.merge(remote, local)

    def test_same_numeric_reply_to_different_logical_record_is_conflict(self):
        remote = self.page({'konu': 'Uzak soru'}, {'konu': 'Aynı yanıt', 'yanit': 'k-0001'})
        local = self.page({'konu': 'Yerel soru'}, {'konu': 'Aynı yanıt', 'yanit': 'k-0001'})
        with self.assertRaisesRegex(ValueError, 'farklı içerik'):
            self.merge(remote, local)

    def test_failed_second_append_does_not_replace_existing_output(self):
        remote = self.page({'konu': 'Ortak'})
        local = self.page({'konu': 'Yerel bir'}, {'konu': 'Yerel iki'}, source=remote)
        self.output.write_text('korunacak çıktı', encoding='utf-8')
        original = birlestir.ekle
        calls = []
        def fail_later(path, fields):
            calls.append(fields)
            if len(calls) == 2:
                raise RuntimeError('Sentetik ekleme hatası')
            return original(path, fields)
        with patch.object(birlestir, 'ekle', side_effect=fail_later):
            with self.assertRaisesRegex(RuntimeError, 'Sentetik'):
                self.merge(remote, local)
        self.assertEqual(self.output.read_text(encoding='utf-8'), 'korunacak çıktı')
        self.assertEqual(list(self.root.glob('kopru-birlestir-*')), [])

    def test_remote_only_section_change_is_kept_with_three_way_base(self):
        base = self.page({'konu': 'Ortak'})
        remote = base.replace('Sentetik bağlam.', 'Uzaktaki yeni bağlam.')
        local = self.page({'konu': 'Yerel'}, source=base)
        _, merged = self.merge(remote, local, base)
        self.assertIn('Uzaktaki yeni bağlam.', merged)
        self.assertEqual(len(birlestir.kayitlar(merged)), 2)

    def test_local_section_change_stops_instead_of_losing_content(self):
        base = self.page({'konu': 'Ortak'})
        remote = self.page({'konu': 'Uzak'}, source=base)
        local = base.replace('Sentetik bağlam.', 'Yereldeki yeni bağlam.')
        with self.assertRaisesRegex(ValueError, 'kayıt dışı'):
            self.merge(remote, local, base)
        self.assertFalse(self.output.exists())

    def test_two_file_merge_does_not_choose_between_section_changes(self):
        remote = self.page({'konu': 'Ortak'})
        local = remote.replace('Sentetik bağlam.', 'Başka bağlam.')
        with self.assertRaisesRegex(ValueError, 'kayıt dışı'):
            self.merge(remote, local)

    def test_deleted_historical_record_stops_merge(self):
        base = self.page({'konu': 'Ortak'})
        remote = self.page({'konu': 'Uzak'}, source=base)
        local = self.page({'konu': 'Ortak yerine'})
        with self.assertRaisesRegex(ValueError, 'geçmiş'):
            self.merge(remote, local, base)

    def test_both_sides_changing_history_is_rejected(self):
        base = self.page({'konu': 'Ortak'})
        changed = base.replace('Sentetik gövde.', 'Değiştirilen eski gövde.')
        with self.assertRaisesRegex(ValueError, 'geçmiş'):
            self.merge(changed, changed, base)

    def test_missing_reply_target_is_rejected(self):
        page = self.page({'konu': 'Ortak'}, {'konu': 'Yanıt', 'yanit': 'k-0001'})
        broken = page.replace('data-yanit="k-0001"', 'data-yanit="k-0099"')
        with self.assertRaisesRegex(ValueError, 'yanıt verilen'):
            self.merge(page, broken)

    def test_duplicate_record_ids_are_rejected(self):
        page = self.page({'konu': 'Bir'}, {'konu': 'İki'})
        broken = page.replace('id="k-0002"', 'id="k-0001"')
        with self.assertRaisesRegex(ValueError, 'Yinelenen'):
            self.merge(page, broken)

    def test_duplicate_logical_identity_is_rejected(self):
        page = self.page({'konu': 'Bir'}, {'konu': 'İki'})
        broken = page.replace('<h3>İki</h3>', '<h3>Bir</h3>')
        with self.assertRaisesRegex(ValueError, 'Yinelenen'):
            self.merge(page, broken)

    def test_final_raw_html_is_validated_before_replacing_output(self):
        remote = self.page({'konu': 'Ortak'})
        local = self.page({'konu': 'Yerel'}, source=remote)
        i = local.index('<article class="kayit" id="k-0002"')
        local = local[:i] + local[i:].replace('<p>Sentetik gövde.</p>',
            '<p>Sentetik gövde.<img src="https://example.invalid/image.png"></p>', 1)
        self.output.write_text('korunacak çıktı', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'denetimden geçmedi'):
            self.merge(remote, local)
        self.assertEqual(self.output.read_text(encoding='utf-8'), 'korunacak çıktı')

    def test_raw_preservation_does_not_introduce_executable_html(self):
        remote = self.page({'konu': 'Ortak'})
        local = self.page({'konu': 'Yerel'}, source=remote)
        i = local.index('<article class="kayit" id="k-0002"')
        for unsafe in ('<script>void(0)</script>', '<span onclick="void(0)">metin</span>',
                       '<a href="jav&#x61;script:void(0)">bağlantı</a>'):
            with self.subTest(markup=unsafe):
                broken = local[:i] + local[i:].replace('<p>Sentetik gövde.</p>', '<p>Gövde.</p>' + unsafe, 1)
                with self.assertRaisesRegex(ValueError, 'denetimden geçmedi'):
                    self.merge(remote, broken)
                self.assertFalse(self.output.exists())

    @unittest.skipUnless(shutil.which('git'), 'Git gerekli')
    def test_real_git_rebase_preserves_both_sides_and_remote_section(self):
        repo = self.root / 'repo'
        repo.mkdir()
        def git(*args, expected=0):
            result = subprocess.run(['git', *args], cwd=repo, text=True, capture_output=True,
                                    encoding='utf-8')
            self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
            return result.stdout
        git('init', '-q', '-b', 'main')
        git('config', 'user.name', 'Synthetic test')
        git('config', 'user.email', 'test@example.invalid')
        base = self.page({'konu': 'Ortak'})
        (repo / 'kopru.html').write_text(base, encoding='utf-8')
        git('add', 'kopru.html')
        git('commit', '-qm', 'base')
        git('branch', 'local')
        remote = self.page({'konu': 'Uzak'}, source=base).replace('Sentetik bağlam.', 'Uzak düzenleme.')
        (repo / 'kopru.html').write_text(remote, encoding='utf-8')
        git('commit', '-qam', 'remote')
        git('checkout', '-q', 'local')
        local = self.page({'konu': 'Yerel', 'yanit': 'k-0001'}, source=base)
        (repo / 'kopru.html').write_text(local, encoding='utf-8')
        git('commit', '-qam', 'local')
        git('rebase', 'main', expected=1)
        result = subprocess.run([sys.executable, '-I', '-X', 'utf8', birlestir.__file__,
                                 '--rebase', 'kopru.html'], cwd=repo, capture_output=True, text=True,
                                encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        git('add', 'kopru.html')
        git('-c', 'core.editor=true', 'rebase', '--continue')
        merged = (repo / 'kopru.html').read_text(encoding='utf-8')
        self.assertEqual([r['konu'] for r in birlestir.kayitlar(merged)], ['Ortak', 'Uzak', 'Yerel'])
        self.assertIn('Uzak düzenleme.', merged)
        self.assertEqual(git('status', '--porcelain'), '')


if __name__ == '__main__':
    unittest.main()
