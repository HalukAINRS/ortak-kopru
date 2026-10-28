"""Yalnız sentetik kayıtlar; gerçek CLI/API çağrısı veya köprü yazımı yok."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'defter'))
import kopru_yanitla as k


def row(i, to, sender='Sen', reply=None, status='acik'):
    return {'id':f'k-{i:04d}','kime':to,'kimden':sender,'yanit':reply,'durum':status}


class IdentityTests(unittest.TestCase):
    def test_api_reply_cannot_cover_cli_target(self):
        request=row(1,'ChatGPT (Şaman)')
        api=row(2,'Sen','ChatGPT (API)','k-0001')
        self.assertEqual(k.bekleyenler([request,api],'ChatGPT (Şaman)'),[request])
        self.assertEqual(k.bekleyenler([request,api],'ChatGPT'),[])
        self.assertEqual(k.bekleyenler([request,api],'ChatGPT (API)'),[])

    def test_exact_cli_reply_covers_cli_target(self):
        request=row(1,'ChatGPT (Şaman)')
        cli=row(2,'Sen','ChatGPT (Şaman)','k-0001')
        self.assertEqual(k.bekleyenler([request,cli],'ChatGPT (Şaman)'),[])

    def test_generic_historical_coverage_unchanged(self):
        request=row(1,'ChatGPT')
        cli=row(2,'Sen','ChatGPT (Şaman)','k-0001')
        self.assertEqual(k.bekleyenler([request],'ChatGPT (API)'),[request])
        self.assertEqual(k.bekleyenler([request,cli],'ChatGPT (API)'),[])
        self.assertEqual(k.bekleyenler([request,cli],'ChatGPT'),[])

    def test_aliases_and_separate_participants(self):
        for alias in ['Şaman','Saman','ChatGPT (Saman)','CHATGPT ( ŞAMAN )']:
            self.assertEqual(k.hedef_kimligi(alias),('chatgpt','şaman'))
        request=row(1,'Şahit, Şaman')
        self.assertEqual(k.bekleyenler([request],'Copilot (Şahit)'),[request])
        self.assertEqual(k.bekleyenler([request],'Claude (Hacker)'),[])
        self.assertEqual(k.bekleyenler([request],'ChatGPT (API)'),[])

    def test_own_root_other_layer_request_can_reach_cli(self):
        request=row(1,'ChatGPT (Şaman)','ChatGPT (API)')
        self.assertEqual(k.bekleyenler([request],'ChatGPT (Şaman)'),[request])
        self.assertEqual(k.bekleyenler([row(2,'Sen',status='kapandi')],'ChatGPT (Şaman)'),[])

    def test_fallback_identity_never_inherits_cli_label(self):
        kat={'ad':'ChatGPT','saglayici':'cli','imza':'ChatGPT (Şaman)'}
        self.assertEqual(k.yol_kimligi('ChatGPT',kat,kat),'ChatGPT (Şaman)')
        self.assertEqual(k.yol_kimligi('ChatGPT',kat,{'saglayici':'openai'}),'ChatGPT (API)')
        for path in [{'saglayici':'openai','imza':'ChatGPT (Şaman)'},{'saglayici':'cli','imza':'ChatGPT (API)'}]:
            with self.assertRaises(ValueError):k.yol_kimligi('ChatGPT',kat,path)


class RouteTests(unittest.TestCase):
    def run_routes(self, records, cli_missing=True, dry=False):
        kat={'ad':'ChatGPT','saglayici':'cli','imza':'ChatGPT (Şaman)','komut':['synthetic-cli'],
             'yedek':{'saglayici':'openai','model':'synthetic-api'}}
        with tempfile.TemporaryDirectory() as d:
            settings=Path(d)/'settings.json'
            settings.write_text(json.dumps({'katilimcilar':[kat]}),encoding='utf-8')
            seen=[]; written=[]
            def prompt(path,identity,pending):
                seen.append((identity,[r['id'] for r in pending]))
                return 'synthetic-system',json.dumps([r['id'] for r in pending])
            cli_effect=k.KomutYok('synthetic-cli') if cli_missing else None
            argv=['kopru_yanitla.py','synthetic-page.html','--ayarlar',str(settings)]+(['--kuru'] if dry else [])
            with patch.object(sys,'argv',argv),patch.object(k,'kayitlari_oku',return_value=records), \
                 patch.object(k,'istem_kur',side_effect=prompt), \
                 patch.object(k,'cli_cagir',side_effect=cli_effect,return_value=('{"govde":"synthetic response"}',{})) as cli, \
                 patch.object(k,'cagir',return_value=('{"govde":"synthetic response"}',{})) as api, \
                 patch.object(k,'ekle',side_effect=lambda p,v:written.append(v) or 'k-0099'), \
                 patch.object(k,'kayit_yaz',return_value='synthetic-log'),patch.object(k,'atlandi_yaz'), \
                 contextlib.redirect_stdout(io.StringIO()):
                k.main()
            return seen,written,cli.call_count,api.call_count

    def test_cli_only_request_never_reaches_api_fallback(self):
        seen,written,cli,api=self.run_routes([row(1,'ChatGPT (Şaman)')])
        self.assertEqual(seen,[('ChatGPT (Şaman)',['k-0001'])])
        self.assertEqual((written,cli,api),([],1,0))

    def test_mixed_requests_recomputed_for_fallback(self):
        seen,written,cli,api=self.run_routes([row(1,'ChatGPT (Şaman)'),row(2,'ChatGPT')])
        self.assertEqual(seen,[('ChatGPT (Şaman)',['k-0001','k-0002']),('ChatGPT (API)',['k-0002'])])
        self.assertEqual(written[0]['kimden'],'ChatGPT (API)')
        self.assertEqual(written[0]['yanit'],'k-0002')
        remaining=k.bekleyenler([row(1,'ChatGPT (Şaman)'),row(2,'ChatGPT'),row(3,'Sen','ChatGPT (API)','k-0002')],'ChatGPT (Şaman)')
        self.assertEqual([r['id'] for r in remaining],['k-0001'])

    def test_actual_cli_route_signature_used(self):
        _,written,cli,api=self.run_routes([row(1,'Şaman')],cli_missing=False)
        self.assertEqual(written[0]['kimden'],'ChatGPT (Şaman)')
        self.assertEqual((cli,api),(1,0))

    def test_dry_run_does_not_call_any_provider_or_write_bridge(self):
        _,written,cli,api=self.run_routes([row(1,'Şaman')],dry=True)
        self.assertEqual((written,cli,api),([],0,0))


if __name__=='__main__':unittest.main()
