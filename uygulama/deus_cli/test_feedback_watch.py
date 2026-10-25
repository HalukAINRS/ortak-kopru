import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from feedback_watch import Watcher,digest,read_sources,bridge_results


class FeedbackTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)
        notes=self.root/'Ortak_Notlar';notes.mkdir()
        self.source=notes/'result.json'
        self.config={'bridge_root':str(self.root),'codex_exe':'codex-test',
            'workspace':str(self.root),'target_thread':'existing-thread',
            'authorized_jobs':{'job-1':'Haluk authorized test task'},
            'sources':[{'id':'one','job':'job-1','role':'Şahit','transport':'local','path':str(self.source)}]}
        self.path=self.root/'config.json';self.write_config()
        self.calls=[]
        def runner(arguments,**kwargs):
            self.calls.append(arguments)
            return subprocess.CompletedProcess(arguments,0)
        self.watcher=Watcher(self.path,runner)

    def tearDown(self):self.tmp.cleanup()
    def write_config(self):self.path.write_text(json.dumps(self.config),encoding='utf-8')
    def dispatch(self):
        self.source.write_bytes(b'{"actual_result":"ready"}')
        self.assertEqual(self.watcher.once(),[])
        return self.watcher.once()[0]

    def test_two_stable_reads_and_exact_existing_thread(self):
        result=self.dispatch()
        self.assertEqual(result['phase'],'queued')
        self.assertEqual(self.calls[0][1:4],['queue','--thread','existing-thread'])
        self.assertNotIn('exec',self.calls[0]);self.assertNotIn('resume',self.calls[0])

    def test_restart_never_requeues_same_result(self):
        self.dispatch()
        restarted=Watcher(self.path,lambda *a,**k:self.fail('Duplicate dispatch'))
        self.assertEqual(restarted.once()[0]['phase'],'queued')
        self.assertEqual(len(self.calls),1)

    def test_delivery_uncertainty_is_preserved(self):
        result=self.dispatch();path=self.root/'events'/result['event']/'delivery.json'
        record=json.loads(path.read_bytes());record['phase']='before_queue';path.write_text(json.dumps(record))
        self.assertEqual(self.watcher.once()[0]['phase'],'uncertain')
        self.assertEqual(len(self.calls),1)

    def test_snapshot_tampering_is_rejected(self):
        result=self.dispatch()
        (self.root/'events'/result['event']/'source.bin').write_bytes(b'changed')
        with self.assertRaises(ValueError):self.watcher.once()

    def test_partial_write_is_not_first_dispatch(self):
        self.source.write_bytes(b'first');self.watcher.once()
        self.source.write_bytes(b'second');self.assertEqual(self.watcher.once(),[])
        self.assertEqual(self.watcher.once()[0]['phase'],'queued')
        self.assertEqual(len(self.calls),1)

    def test_known_baseline_is_not_new_feedback(self):
        self.source.write_bytes(b'old')
        self.config['sources'][0]['baseline_sha256']=digest(b'old');self.write_config()
        self.assertEqual(self.watcher.once(),[]);self.assertEqual(self.watcher.once(),[])

    def test_same_peer_result_from_two_channels_queues_once(self):
        second={**self.config['sources'][0],'id':'second-channel'}
        self.config['sources'].append(second);self.write_config()
        samples={'one':b'same result','second-channel':b'same result'}
        self.watcher.once(samples);self.watcher.once(samples)
        self.assertEqual(len(self.calls),1)

    def test_credentials_directory_is_not_accepted(self):
        self.config['sources'][0]['path']=str(self.root/'Home/auth.json')
        with self.assertRaises(ValueError):read_sources(self.config)

    def test_oversized_result_is_not_dispatched(self):
        self.source.write_bytes(b'x'*(2*1024*1024+1))
        with self.assertRaises(ValueError):self.watcher.once()

    def test_unknown_role_is_not_accepted(self):
        self.config['sources'][0]['role']='Haluk';self.write_config()
        with self.assertRaises(ValueError):self.watcher.once({'one':b'fake'})

    def test_standalone_isolated_entry_point_loads(self):
        run=subprocess.run([sys.executable,'-I','-B','-X','utf8',str(Path(__file__).with_name('feedback_watch.py')),'--help'],capture_output=True,timeout=10)
        self.assertEqual(run.returncode,0)

    def test_bridge_filters_baseline_self_and_other_recipients(self):
        bridge=self.root/'kopru.html'
        def article(number,sender,target):
            return f'<article class="kayit" id="k-{number:04d}" data-kimden="{sender}" data-kime="{target}"><h3>Result</h3><div class="govde">Evidence</div></article>'
        bridge.write_text(article(1,'Claude (Hacker)','Şaman')+article(2,'ChatGPT (Şaman)','Şaman')+
            article(3,'Claude (Hacker)','Other')+article(4,'Claude (Hacker)','ChatGPT (Şaman)'),encoding='utf-8')
        self.config['bridge_feedback']={'path':str(bridge),'baseline_ids':['k-0001'],
            'senders':{'Claude (Hacker)':'Hacker'}}
        rows=bridge_results(self.config)
        self.assertEqual(len(rows),1)
        self.assertTrue(rows[0][0]['id'].endswith('-k-0004'))


if __name__=='__main__':unittest.main()
