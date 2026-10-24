import concurrent.futures
import hashlib
import json
from pathlib import Path
import tempfile
import subprocess
import sys
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from bridge import Conflict, Store, handler


class BridgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store = Store(self.temp.name)
        self.session = self.store.connect('Şaman','real-session-A','Açık CLI')['session_id']
        self.other = self.store.connect('Şaman','real-session-B','Diğer CLI')['session_id']
        self.source = Path(self.temp.name)/'kaynak.txt'
        self.source.write_text('O > I\n0 -> 1\n',encoding='utf-8')

    def submit(self, key='request-1', text='  Özgün söz\n> ve -> ayrı.  ', **kwargs):
        return self.store.submit(self.session,text,key,**kwargs)

    def test_original_words_and_retry_are_exact(self):
        job=self.submit();same=self.submit()
        self.assertEqual(job,same)
        self.assertEqual(job['turns'][0]['original_words'],'  Özgün söz\n> ve -> ayrı.  ')
        self.assertEqual(len(self.store.state()['jobs']),1)
        with self.assertRaises(Conflict):self.submit(text='Değiştirilmiş söz')

    def test_wrong_session_and_unclaimed_reply_rejected(self):
        job=self.submit()
        self.assertIsNone(self.store.receive(self.other)['request'])
        with self.assertRaises(Conflict):self.store.reply(self.session,job['id'],1,'Yanıt',[])
        self.store.receive(self.session)
        with self.assertRaises(Conflict):self.store.reply(self.other,job['id'],1,'Yanıt',[])

    def test_restart_redelivers_same_claim_without_second_delivery(self):
        job=self.submit();first=self.store.receive(self.session)['request']
        restarted=Store(self.temp.name);again=restarted.receive(self.session)['request']
        self.assertEqual(first['id'],job['id']);self.assertEqual(again['id'],job['id'])
        self.assertTrue(again['redelivered'])
        with self.store.db() as db:self.assertEqual(db.execute("SELECT count(*) FROM events WHERE kind='cli_received'").fetchone()[0],1)

    def test_parallel_receive_is_one_claim(self):
        job=self.submit()
        with concurrent.futures.ThreadPoolExecutor(2) as pool:
            results=list(pool.map(lambda _:self.store.receive(self.session)['request'],range(2)))
        self.assertEqual({r['id'] for r in results},{job['id']})
        self.assertEqual(sorted(r['redelivered'] for r in results),[False,True])

    def test_reply_keeps_source_bytes_and_cannot_be_overwritten(self):
        job=self.submit();self.store.receive(self.session)
        answer=self.store.reply(self.session,job['id'],1,'Kaynaklı yanıt',[self.source])
        self.assertEqual(answer['turns'][0]['sources'][0]['sha256'],hashlib.sha256(self.source.read_bytes()).hexdigest())
        self.assertEqual(answer,self.store.reply(self.session,job['id'],1,'Kaynaklı yanıt',[self.source]))
        with self.assertRaises(Conflict):self.store.reply(self.session,job['id'],1,'Başka yanıt',[self.source])

    def test_separate_processes_share_one_claim(self):
        job=self.submit()
        code="import sys,json;sys.path.insert(0,sys.argv[3]);from bridge import Store;print(json.dumps(Store(sys.argv[1]).receive(sys.argv[2])))"
        children=[subprocess.Popen([sys.executable,'-c',code,self.temp.name,self.session,str(Path(__file__).parent.resolve())],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,encoding='utf-8') for _ in range(2)]
        outputs=[child.communicate(timeout=15) for child in children]
        results=[]
        for child,(output,error) in zip(children,outputs):
            self.assertEqual(child.returncode,0,error);results.append(json.loads(output)['request'])
        self.assertEqual({r['id'] for r in results},{job['id']})
        self.assertEqual(sorted(r['redelivered'] for r in results),[False,True])

    def test_correction_keeps_job_session_and_prior_words(self):
        job=self.submit();self.store.receive(self.session)
        self.store.submit(self.session,'Düzeltme: > akış değildir.','correction',job_id=job['id'])
        self.assertEqual(self.store.receive(self.session)['request']['revision'],1)
        self.store.reply(self.session,job['id'],1,'İlk karşılık',[])
        next_turn=self.store.receive(self.session)['request']
        self.assertEqual(next_turn['id'],job['id']);self.assertEqual(next_turn['revision'],2)
        self.assertEqual(next_turn['turns'][1]['original_words'],'Düzeltme: > akış değildir.')
        with self.assertRaises(Conflict):self.store.submit(self.other,'X','bad-target',job_id=job['id'])

    def test_http_roundtrip_and_origin(self):
        server=ThreadingHTTPServer(('localhost',0),handler(self.store))
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        self.addCleanup(server.server_close);self.addCleanup(server.shutdown)
        base=f'http://localhost:{server.server_port}'
        opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
        payload=json.dumps({'session_id':self.session,'words':'Gerçek HTTP isteği','request_key':'wire'}).encode()
        request=urllib.request.Request(base+'/api/messages',data=payload,headers={'Content-Type':'application/json','Origin':base})
        with opener.open(request) as response:job=json.load(response)
        received=self.store.receive(self.session)['request'];self.assertEqual(received['id'],job['id'])
        self.store.reply(self.session,job['id'],1,'CLI karşılığı',[self.source])
        with opener.open(base+'/api/state') as response:state=json.load(response)
        self.assertEqual(state['jobs'][0]['turns'][0]['response'],'CLI karşılığı')
        request=urllib.request.Request(base+'/api/messages',data=payload,headers={'Content-Type':'application/json','Origin':'https://example.invalid'})
        with self.assertRaises(urllib.error.HTTPError) as error:opener.open(request)
        self.assertEqual(error.exception.code,403)
        error.exception.close()
        request=urllib.request.Request(base+'/api/state',headers={'Host':'example.invalid'})
        with self.assertRaises(urllib.error.HTTPError) as error:opener.open(request)
        self.assertEqual(error.exception.code,403)
        error.exception.close()
        with opener.open(base+'/') as response:
            self.assertIn(b'deus_ex_machina',response.read());self.assertIn("frame-ancestors 'none'",response.headers['Content-Security-Policy'])


if __name__=='__main__':unittest.main()
