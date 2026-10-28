import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from bridge import Store
from queue_consumer import Consumer


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.store=Store(self.temp.name)
        self.thread='synthetic-current-thread'
        self.session=self.store.connect('Şaman',self.thread,'Sentetik test')['session_id']
        self.runner=Mock(return_value=SimpleNamespace(returncode=0))
        self.consumer=Consumer(self.store,self.thread,'synthetic-codex',self.temp.name,self.runner)
        self.job=self.store.submit(self.session,' Özgün > söz\n-> ayrı. ','queue-test',
            context={'speaker':'Sentetik test kullanıcısı','branch':'test'})

    def test_queue_uses_exact_thread_and_preserves_full_source_context(self):
        result=self.consumer.once()
        self.assertEqual(result['phase'],'queued')
        args=self.runner.call_args.args[0]
        self.assertEqual(args[:4],['synthetic-codex','queue','--thread',self.thread])
        self.assertNotIn('exec',args)
        envelope=next(self.consumer.directory.glob('*.request.json'))
        source=json.loads(envelope.read_text(encoding='utf-8'))
        turn=source['request']['turns'][0]
        self.assertEqual(turn['original_words'],self.job['turns'][0]['original_words'])
        self.assertEqual(turn['source_context'],self.job['turns'][0]['source_context'])
        self.assertFalse(turn['source_context_verified'])
        delivery=self.store.job(self.job['id'])['turns'][0]['delivery']
        self.assertEqual(delivery['phase'],'queued')
        self.assertFalse(delivery['model_received_verified'])

    def test_restart_after_success_does_not_queue_twice(self):
        self.consumer.once()
        restarted=Consumer(self.store,self.thread,'synthetic-codex',self.temp.name,self.runner)
        self.assertEqual(restarted.once()['phase'],'queued')
        self.assertEqual(self.runner.call_count,1)
        with self.store.db() as db:
            self.assertEqual(db.execute("select count(*) from events where kind='cli_received'").fetchone()[0],1)

    def test_ambiguous_timeout_is_not_retried(self):
        self.runner.side_effect=subprocess.TimeoutExpired('synthetic-codex',35)
        self.assertEqual(self.consumer.once()['phase'],'uncertain')
        self.assertEqual(self.consumer.once()['phase'],'uncertain')
        self.assertEqual(self.runner.call_count,1)

    def test_crash_after_before_queue_marker_is_not_retried(self):
        self.runner.side_effect=SystemExit('synthetic process interruption')
        with self.assertRaises(SystemExit):self.consumer.once()
        self.assertEqual(self.consumer.once()['phase'],'uncertain')
        self.assertEqual(self.store.job(self.job['id'])['turns'][0]['delivery']['phase'],'uncertain')
        self.assertEqual(self.runner.call_count,1)

    def test_reply_completes_then_correction_is_a_new_dispatch(self):
        self.consumer.once()
        self.store.reply(self.session,self.job['id'],1,'Sentetik karşılık',[])
        self.assertEqual(self.consumer.once()['phase'],'idle')
        self.store.submit(self.session,'Yeni düzeltme','queue-test-2',job_id=self.job['id'])
        self.assertEqual(self.consumer.once()['revision'],2)
        self.assertEqual(self.runner.call_count,2)
        self.assertEqual(len(list(self.consumer.directory.glob('*.request.json'))),2)

    def test_wrong_session_is_not_silently_registered_or_selected(self):
        with self.assertRaises(ValueError):
            Consumer(self.store,'other-thread','synthetic-codex',self.temp.name,self.runner)
        self.assertEqual(len(self.store.state()['sessions']),1)


if __name__=='__main__':unittest.main()
