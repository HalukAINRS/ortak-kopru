"""Bulut gönderiminin hedef, kimlik ve komut sınırlarını sınar."""
import contextlib
import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock

sys.dont_write_bytecode = True
KAYNAK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAYNAK / 'araclar'))
import bulut_bag


class BulutBagSinamalari(unittest.TestCase):
    def setUp(self):
        self.ayar = json.loads((KAYNAK / 'yapilandirma' / 'bulut_bag.json').read_text(encoding='utf-8'))

    def test_ortamsiz_gonderim_surec_baslatmaz(self):
        self.ayar['codex_bulut']['ortam_kimligi'] = None
        with mock.patch.object(bulut_bag, 'ayar_oku', return_value=self.ayar), \
                mock.patch.object(bulut_bag, 'komut') as calistir, \
                contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(bulut_bag.ana(['gonder', 'Deneme']), 2)
        calistir.assert_not_called()

    def test_gorev_metni_kabuga_girmeden_tek_arguman_kalir(self):
        self.ayar['codex_bulut']['ortam_kimligi'] = 'env_sinama'
        gorev = 'Türkçe "alıntı"; $() ve `işaret`\niki satır'
        with mock.patch.object(bulut_bag, 'ayar_oku', return_value=self.ayar), \
                mock.patch.object(Path, 'is_file', return_value=True), \
                mock.patch.object(Path, 'is_dir', return_value=True), \
                mock.patch.object(subprocess, 'run', return_value=subprocess.CompletedProcess([], 0)) as calistir:
            self.assertEqual(bulut_bag.ana(['gonder', gorev]), 0)
        argumanlar = calistir.call_args.args[0]
        secenekler = calistir.call_args.kwargs
        self.assertEqual(argumanlar[-2:], ['--', gorev])
        self.assertFalse(secenekler['shell'])
        self.assertEqual(secenekler['cwd'], KAYNAK)
        self.assertEqual(secenekler['env']['CODEX_HOME'], str(KAYNAK / self.ayar['codex_cli']['profil']))

    def test_gecersiz_gorev_kimligi_komut_olamaz(self):
        for kimlik in ('--help', '../main', 'gorev iki'):
            with self.subTest(kimlik=kimlik), \
                    mock.patch.object(bulut_bag, 'ayar_oku', return_value=copy.deepcopy(self.ayar)), \
                    mock.patch.object(bulut_bag, 'komut') as calistir, \
                    contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(bulut_bag.ana(['sonuc', '--', kimlik]), 2)
                calistir.assert_not_called()

    def test_karargah_disindaki_program_baslatilamaz(self):
        self.ayar['codex_cli']['yurutulebilir'] = '../dis_program.exe'
        with mock.patch.object(subprocess, 'run') as calistir:
            with self.assertRaises(bulut_bag.BaglantiHatasi):
                bulut_bag.komut(self.ayar, ['--version'])
        calistir.assert_not_called()

    def test_durum_kimlik_sorgusunun_icerigini_yazmaz(self):
        kimlik_metni = 'KIMLIK_CIKTISI_YAYIMLANMAMALI'
        yanitlar = [subprocess.CompletedProcess([], 0, 'codex-cli sınama', ''),
                    subprocess.CompletedProcess([], 0, kimlik_metni, kimlik_metni)]
        cikti = io.StringIO()
        with mock.patch.object(bulut_bag, 'ayar_oku', return_value=self.ayar), \
                mock.patch.object(bulut_bag, 'komut', side_effect=yanitlar), \
                contextlib.redirect_stdout(cikti):
            self.assertEqual(bulut_bag.ana(['durum']), 0)
        self.assertNotIn(kimlik_metni, cikti.getvalue())
        self.assertTrue(json.loads(cikti.getvalue())['giris_var'])


if __name__ == '__main__':
    unittest.main()
