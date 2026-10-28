"""PowerShell gönderici/izleyici: geçici Git depoları; gerçek ağ veya sağlayıcı çağrısı yok."""
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.test_bakim import CANONICAL, expected_mirror


ROOT = Path(__file__).resolve().parents[1]
PWSH = shutil.which('pwsh')


@unittest.skipUnless(PWSH and shutil.which('git'), 'PowerShell 7 ve Git gerekli.')
class PowerShellSenderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='kopru powershell ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / 'remote.git'
        self.local = self.root / 'local'
        self.local.mkdir()
        self.env = os.environ.copy()
        for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE'):
            self.env.pop(key, None)
        self.env.update({
            'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
            'GIT_TERMINAL_PROMPT': '0', 'KOPRU_PYTHON': sys.executable, 'PYTHONUTF8': '1',
            'GIT_AUTHOR_NAME': 'Synthetic test', 'GIT_AUTHOR_EMAIL': 'test@example.invalid',
            'GIT_COMMITTER_NAME': 'Synthetic test', 'GIT_COMMITTER_EMAIL': 'test@example.invalid',
        })
        self.git(self.root, 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.git(self.local, 'init', '--initial-branch=main')
        self.configure(self.local)
        self.git(self.local, 'remote', 'add', 'origin', str(self.remote))
        # Depodaki yerleşim aynen kurulur: betikler yerel/, kayıt araçları defter/, ayarlar katilimcilar/ altında.
        for name in ('yerel/kopru_gonder.ps1', 'yerel/kopru_izle.ps1', 'defter/kopru_birlestir.py',
                     'defter/kopru_ekle.py', 'defter/kopru_oku.py', 'defter/kopru_ayna_uret.py'):
            (self.local / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, self.local / name)
        (self.local / 'katilimcilar').mkdir()
        (self.local / '.gitignore').write_text('__pycache__/\n*.pyc\n', encoding='utf-8')
        (self.local / 'kopru.html').write_text(CANONICAL, encoding='utf-8')
        (self.local / 'katilimcilar' / 'ayarlar-yerel.json').write_text('{"katilimcilar": []}\n', encoding='utf-8')
        (self.local / 'settings.txt').write_text('base\n', encoding='utf-8', newline='\n')
        # İzleyici sınamasındaki tek sağlayıcı, bir günlük yazıp başarısız çıkan yerel taklittir.
        (self.local / 'defter' / 'kopru_yanitla.py').write_text(
            'from pathlib import Path\n'
            'Path("kayit").mkdir(exist_ok=True)\n'
            'Path("kayit/response-error.md").write_text("synthetic failure\\n", encoding="utf-8", newline="\\n")\n'
            'raise SystemExit(1)\n', encoding='utf-8',
        )
        self.append(self.local, 'Base', '2026-10-01T00:00:00+00:00')
        self.generate(self.local)
        self.commit(self.local, 'base')
        self.git(self.local, 'push', '-q', 'origin', 'main')
        self.initial = self.remote_head()

    def run_command(self, directory, *args, check=True):
        result = subprocess.run(args, cwd=directory, env=self.env, capture_output=True,
                                text=True, encoding='utf-8', errors='replace', timeout=60)
        if check:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def git(self, directory, *args):
        return self.run_command(directory, 'git', *args).stdout.strip()

    def configure(self, repo):
        self.git(repo, 'config', 'core.autocrlf', 'false')
        self.git(repo, 'config', 'commit.gpgsign', 'false')
        self.git(repo, 'config', 'user.name', 'Synthetic test')
        self.git(repo, 'config', 'user.email', 'test@example.invalid')

    def append(self, repo, topic, time):
        self.run_command(repo, sys.executable, 'defter/kopru_ekle.py', 'kopru.html', '--kimden', 'Sen',
                         '--kime', 'Sen', '--konu', topic, '--govde', topic + ' synthetic body.',
                         '--dayanak', 'tests/test_powershell.py', '--durum', 'kapandi', '--zaman', time)

    def generate(self, repo):
        self.run_command(repo, sys.executable, 'defter/kopru_ayna_uret.py', 'kopru.html', 'ayna/kopru.html')

    def commit(self, repo, message):
        self.git(repo, 'add', '.')
        self.git(repo, 'commit', '-q', '-m', message)

    def writer(self):
        writer = self.root / 'other writer'
        self.git(self.root, 'clone', '-q', str(self.remote), str(writer))
        self.configure(writer)
        return writer

    def remote_head(self):
        return self.git(self.remote, 'rev-parse', 'main')

    def remote_bytes(self, path):
        return subprocess.check_output(['git', 'show', 'main:' + path], cwd=self.remote, env=self.env)

    def run_ps(self, script='yerel/kopru_gonder.ps1', *args):
        return self.run_command(self.local, PWSH, '-NoLogo', '-NoProfile', '-NonInteractive',
                                '-ExecutionPolicy', 'Bypass', '-File', script, *args, check=False)

    def guarded_state(self):
        return {
            'head': self.git(self.local, 'rev-parse', 'HEAD'),
            'status': self.git(self.local, 'status', '--porcelain'),
            'index': self.git(self.local, 'ls-files', '--stage'),
            'canonical': (self.local / 'kopru.html').read_bytes(),
            'mirror': (self.local / 'ayna/kopru.html').read_bytes(),
            'mirror_mtime': (self.local / 'ayna/kopru.html').stat().st_mtime_ns,
            'remote': self.remote_head(),
        }

    def test_concurrent_append_and_mirror_are_pushed_together(self):
        writer = self.writer()
        self.append(writer, 'Remote', '2026-10-02T00:00:00+00:00')
        self.generate(writer)
        self.commit(writer, 'remote append')
        self.git(writer, 'push', '-q', 'origin', 'main')
        self.append(self.local, 'Local', '2026-10-03T00:00:00+00:00')
        result = self.run_ps()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        bridge = self.remote_bytes('kopru.html')
        mirror = self.remote_bytes('ayna/kopru.html')
        self.assertEqual(bridge.count(b'<article class="kayit"'), 3)
        self.assertIn(b'<h3>Remote</h3>', bridge)
        self.assertIn(b'<h3>Local</h3>', bridge)
        self.assertEqual(mirror, expected_mirror(bridge.decode('utf-8')))
        self.assertEqual((self.local / 'kopru.html').read_bytes(), bridge)
        self.assertEqual((self.local / 'ayna/kopru.html').read_bytes(), mirror)
        self.assertEqual(self.git(self.local, 'status', '--porcelain'), '')

    def test_wrong_branch_is_refused_without_mutating_work(self):
        self.git(self.local, 'switch', '-c', 'feature/maintenance')
        self.append(self.local, 'Unpublished', '2026-10-02T00:00:00+00:00')
        before = self.guarded_state()
        result = self.run_ps()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.guarded_state(), before)

    def test_source_conflict_aborts_without_overwriting_either_side(self):
        writer = self.writer()
        (writer / 'settings.txt').write_text('remote value\n', encoding='utf-8', newline='\n')
        self.commit(writer, 'remote settings')
        self.git(writer, 'push', '-q', 'origin', 'main')
        remote_head = self.remote_head()
        (self.local / 'settings.txt').write_text('local value\n', encoding='utf-8', newline='\n')
        result = self.run_ps()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.remote_head(), remote_head)
        self.assertEqual(self.remote_bytes('settings.txt'), b'remote value\n')
        self.assertEqual((self.local / 'settings.txt').read_bytes(), b'local value\n')
        self.assertFalse((self.local / '.git/rebase-merge').exists())
        self.assertFalse((self.local / '.git/rebase-apply').exists())
        self.assertEqual(self.git(self.local, 'diff', '--name-only', '--diff-filter=U'), '')

    def test_three_rejected_pushes_return_failure_and_keep_local_commit(self):
        hook = self.local / '.git/hooks/pre-push'
        hook.write_text(
            '#!/bin/sh\n'
            'printf "attempt\\n" >> "$(git rev-parse --git-path rejection-count)"\n'
            'exit 1\n', encoding='utf-8', newline='\n',
        )
        hook.chmod(0o755)
        self.append(self.local, 'Local', '2026-10-02T00:00:00+00:00')
        result = self.run_ps()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.remote_head(), self.initial)
        self.assertNotEqual(self.git(self.local, 'rev-parse', 'HEAD'), self.initial)
        self.assertEqual((self.local / '.git/rejection-count').read_text().splitlines(), ['attempt'] * 3)

    def test_watcher_publishes_error_log_and_returns_failure(self):
        result = self.run_ps('yerel/kopru_izle.ps1', '-TekSefer')
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.remote_bytes('kayit/response-error.md'), b'synthetic failure\n')
        self.assertIn('[skip ci]', self.git(self.remote, 'log', '-1', '--format=%s'))
        self.assertEqual(self.remote_bytes('kopru.html').count(b'<article class="kayit"'), 1)

    def test_watcher_does_not_call_provider_after_failed_fetch(self):
        self.git(self.local, 'remote', 'set-url', 'origin', str(self.root / 'missing.git'))
        result = self.run_ps('yerel/kopru_izle.ps1', '-TekSefer')
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertFalse((self.local / 'kayit/response-error.md').exists())
        self.assertEqual(self.remote_head(), self.initial)


if __name__ == '__main__':
    unittest.main()
