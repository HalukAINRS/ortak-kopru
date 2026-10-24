import collections
import json
from pathlib import Path
import tempfile
import unittest
import steering_donustur_tara as s


class Donusum(unittest.TestCase):
    def test_uc_bicimde_sinirlar_bosluk_unicode(self):
        text = " baş \n=== [0002] user\n|içerik & <script>alert(1)</script>\n\nson \u2028iz\n"
        ms=[{'i':1,'rol':'assistant','metin':text,'zaman':'2026-10-24T09:00:00Z'}]
        k={'ad':'deneme','katman':'web','tur':'test','sha256':'0'*64,'bayt':3}
        for writer,reader in [(s.txt_yaz,s.txt_oku),(s.json_yaz,s.json_oku),(s.html_yaz,s.html_oku)]:
            with self.subTest(writer=writer.__name__):
                out=reader(writer(k,ms))
                self.assertEqual([(m['i'],m['rol'],m['metin']) for m in out],[(1,'assistant',text)])
                self.assertEqual(out[0]['zaman'],ms[0]['zaman'])
        self.assertFalse(s.html_statik_ihlal(s.html_yaz(k,ms)))
        self.assertIn("default-src",s.html_yaz(k,ms))

    def test_txt_uzantili_html_utf16_ve_betik(self):
        data="<!DOCTYPE html><html><head><title>gizli</title></head><body><div>Şunu söylediniz:</div><p>öz</p><script>access_token='gizli';</script><template><div>saklı</div></template><p>ChatGPT dedi:</p><p>Yanıt &amp; iz</p></body></html>"
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'kaynak.txt'; path.write_bytes(data.encode('utf-16'))
            before=path.read_bytes(); ms,raw=s.oku_txt(path)
            self.assertTrue(s.html_mi(raw)); self.assertEqual(before,path.read_bytes())
            self.assertEqual([(m['rol'],m['metin']) for m in ms],[('user','öz'),('assistant','Yanıt & iz')])
            self.assertNotIn('gizli',str(ms)); self.assertNotIn('saklı',str(ms))

    def test_kabuk_ve_rol_oncesi_icerik(self):
        ms=s.rolleri_ayir(s.html_gorunur_satirlar('<html><body><p>Loading...</p></body></html>'))
        self.assertEqual([m['rol'] for m in ms],['metin'])
        ms=s.rolleri_ayir(['Menü','You said:','İstek','ChatGPT said:','Yanıt'])
        self.assertEqual([m['rol'] for m in ms],['metin','user','assistant'])

    def test_maskeleme_ve_aday_kanit_ayrimi(self):
        count=collections.Counter()
        text=s.maskele('access_token="sekret"; https://example.test/?sig=sakli Bearer abcdefghijklmnop',count)
        for value in ['sekret','sakli','abcdefghijklmnop']: self.assertNotIn(value,text)
        text=s.maskele('Authorization: Bearer abcdefghijklmnop\nCookie: a=sakli; b=ikinci',count)
        for value in ['abcdefghijklmnop','sakli','ikinci']: self.assertNotIn(value,text)
        ms=[{'i':1,'rol':'user','metin':'Alıntı: Great question!'}]
        counts,hits,_=s.tara(ms)
        self.assertEqual(counts[('user','ANT-B02')],1)
        self.assertEqual(hits[0]['rol'],'user')

    def test_kayipli_decode_yok(self):
        with self.assertRaises(ValueError): s.metni_coz(b'\xffnot-utf8')

    def test_codex_yalniz_gorunur_kanallar(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'log.jsonl'
            rows=[{'type':'response_item','payload':{'type':'message','role':'assistant','channel':channel,'content':[{'text':channel}]}} for channel in ['analysis','final','commentary']]
            p.write_text('\n'.join(json.dumps(x) for x in rows),encoding='utf-8')
            self.assertEqual([m['metin'] for m in s.oku_codex(p)],['final','commentary'])


if __name__ == '__main__': unittest.main()
