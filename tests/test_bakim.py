"""Ayna ve gönderim regresyonları: sentetik sayfa, geçici depolar, ağ yok."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MIRROR_HEAD = (
    '<title>Sentetik köprü</title>\n'
    '<meta name="description" content="Çevrimdışı sınama">\n'
    '<style>body { color: black; }</style>\n'
)
CANONICAL = '''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sentetik köprü</title>
<meta name="description" content="Çevrimdışı sınama">
<style>body { color: black; }</style>
</head>
<body>
<header>
<h1>Sentetik köprü</h1>
<p>Kayıt: <b id="kayit-sayisi">0</b></p>
<time id="son-guncelleme" datetime="2026-10-01T00:00:00+00:00">1 Eki 2026 00.00</time>
<p>Son kayıt: <a href="#k-0000">k-0000</a></p>
</header>
<!-- KAYIT-SONU -->
</body>
</html>
'''


def expected_mirror(canonical):
    """Bu sabit test sayfasının bağımsız beklenen yayım biçimi."""
    body = canonical.split('<body>', 1)[1].split('</body>', 1)[0]
    return (MIRROR_HEAD + body.strip() + '\n').encode('utf-8')


class MirrorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='kopru-ayna-')
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.source = self.folder / 'kopru.html'
        self.target = self.folder / 'ayna' / 'kopru.html'
        self.source.write_text(CANONICAL, encoding='utf-8')

    def run_mirror(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / 'defter' / 'kopru_ayna_uret.py'),
             str(self.source), str(self.target), *args],
            capture_output=True, text=True, encoding='utf-8', timeout=20,
        )

    def test_generation_preserves_existing_mirror_format(self):
        result = self.run_mirror()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.target.read_bytes(), expected_mirror(CANONICAL))
        self.assertEqual(self.source.read_text(encoding='utf-8'), CANONICAL)

    def test_check_missing_target_fails_without_creating_directory(self):
        result = self.run_mirror('--kontrol')
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.target.exists())
        self.assertFalse(self.target.parent.exists())

    def test_check_stale_target_fails_without_writing(self):
        self.target.parent.mkdir()
        self.target.write_bytes(b'previous mirror\n')
        os.utime(self.target, (1_600_000_000, 1_600_000_000))
        before = self.target.stat().st_mtime_ns
        result = self.run_mirror('--kontrol')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.target.read_bytes(), b'previous mirror\n')
        self.assertEqual(self.target.stat().st_mtime_ns, before)

    def test_current_target_check_and_generation_do_not_rewrite(self):
        self.target.parent.mkdir()
        self.target.write_bytes(expected_mirror(CANONICAL))
        os.utime(self.target, (1_600_000_000, 1_600_000_000))
        before = self.target.stat().st_mtime_ns
        for args in [('--kontrol',), ()]:
            with self.subTest(args=args):
                result = self.run_mirror(*args)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertEqual(self.target.read_bytes(), expected_mirror(CANONICAL))
                self.assertEqual(self.target.stat().st_mtime_ns, before)

    def test_malformed_source_preserves_previous_target(self):
        self.target.parent.mkdir()
        self.target.write_bytes(b'previous mirror\n')
        os.utime(self.target, (1_600_000_000, 1_600_000_000))
        before = self.target.stat().st_mtime_ns
        for tag in ('head', 'body', 'title', 'style'):
            with self.subTest(missing_tag=tag):
                self.source.write_text(
                    CANONICAL.replace('</' + tag + '>', ''), encoding='utf-8',
                )
                result = self.run_mirror()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(self.target.read_bytes(), b'previous mirror\n')
                self.assertEqual(self.target.stat().st_mtime_ns, before)
                self.assertEqual(list(self.target.parent.iterdir()), [self.target])


@unittest.skipUnless(
    os.name == 'posix' and shutil.which('bash') and shutil.which('git'),
    'Bash gönderim sınamaları POSIX, bash ve git gerektirir.',
)
class SenderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='kopru gonderim ')
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.remote = self.folder / 'remote.git'
        self.local = self.folder / 'local'
        self.local.mkdir()
        # Betik `python` çağırır; sınanan yorumlayıcıyı PATH üzerinden sabitleriz.
        binary = self.folder / 'bin'
        binary.mkdir()
        (binary / 'python').symlink_to(sys.executable)
        self.env = os.environ.copy()
        for key in ('GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE'):
            self.env.pop(key, None)
        self.env.update({
            'PATH': str(binary) + os.pathsep + self.env.get('PATH', ''),
            'GIT_CONFIG_NOSYSTEM': '1',
            'GIT_CONFIG_GLOBAL': os.devnull,
            'GIT_TERMINAL_PROMPT': '0',
            'GIT_AUTHOR_NAME': 'Sentetik sınama',
            'GIT_AUTHOR_EMAIL': 'test@example.invalid',
            'GIT_COMMITTER_NAME': 'Sentetik sınama',
            'GIT_COMMITTER_EMAIL': 'test@example.invalid',
        })
        self.git(self.folder, 'init', '--bare', '--initial-branch=main', str(self.remote))
        self.git(self.local, 'init', '--initial-branch=main')
        self.configure(self.local)
        self.git(self.local, 'remote', 'add', 'origin', str(self.remote))
        for name in ('defter/kopru_ekle.py', 'defter/kopru_ayna_uret.py',
                     'defter/kopru_birlestir.py', 'defter/kopru_oku.py',
                     '.github/scripts/kopru_gonder.sh'):
            destination = self.local / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        (self.local / '.gitignore').write_text('__pycache__/\n*.pyc\n', encoding='utf-8')
        (self.local / 'kopru.html').write_text(CANONICAL, encoding='utf-8')
        (self.local / 'kayit').mkdir()
        (self.local / 'kayit' / 'same.md').write_text('başlangıç\n', encoding='utf-8')
        self.append(self.local, 'Başlangıç', '2026-10-01T00:00:00+00:00')
        self.generate(self.local)
        self.commit(self.local, 'sentetik başlangıç')
        self.git(self.local, 'push', '-q', 'origin', 'main')
        self.initial = self.remote_head()

    def command(self, cwd, *command, check=True):
        result = subprocess.run(
            list(command), cwd=cwd, env=self.env, capture_output=True,
            text=True, encoding='utf-8', errors='replace', timeout=30,
        )
        if check:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def git(self, cwd, *args):
        return self.command(cwd, 'git', *args).stdout.strip()

    def configure(self, repo):
        self.git(repo, 'config', 'core.autocrlf', 'false')
        self.git(repo, 'config', 'commit.gpgsign', 'false')
        self.git(repo, 'config', 'user.name', 'Sentetik sınama')
        self.git(repo, 'config', 'user.email', 'test@example.invalid')

    def append(self, repo, topic, timestamp, reply=''):
        args = [sys.executable, 'defter/kopru_ekle.py', 'kopru.html',
                '--kimden', 'Sen', '--kime', 'Sen', '--konu', topic,
                '--govde', topic + ' için sentetik gövde.',
                '--dayanak', 'tests/test_bakim.py', '--durum', 'kapandi',
                '--zaman', timestamp]
        if reply:
            args += ['--yanit', reply]
        self.command(repo, *args)

    def generate(self, repo):
        self.command(repo, sys.executable, 'defter/kopru_ayna_uret.py',
                     'kopru.html', 'ayna/kopru.html')

    def commit(self, repo, message):
        self.git(repo, 'add', '.')
        self.git(repo, 'commit', '-q', '-m', message)

    def clone_writer(self):
        writer = self.folder / 'other writer'
        self.git(self.folder, 'clone', '-q', str(self.remote), str(writer))
        self.configure(writer)
        return writer

    def remote_head(self):
        return self.git(self.remote, 'rev-parse', 'main')

    def remote_bytes(self, path):
        return subprocess.check_output(
            ['git', 'show', 'main:' + path], cwd=self.remote, env=self.env,
        )

    def send(self):
        return self.command(
            self.local, 'bash', '.github/scripts/kopru_gonder.sh', check=False,
        )

    def assert_no_rebase(self):
        self.assertFalse((self.local / '.git' / 'rebase-merge').exists())
        self.assertFalse((self.local / '.git' / 'rebase-apply').exists())
        self.assertEqual(self.git(self.local, 'diff', '--name-only', '--diff-filter=U'), '')

    def assert_mirror_matches_remote_bridge(self):
        bridge = self.remote_bytes('kopru.html')
        mirror = self.remote_bytes('ayna/kopru.html')
        self.assertEqual(mirror, expected_mirror(bridge.decode('utf-8')))
        self.assertEqual((self.local / 'kopru.html').read_bytes(), bridge)
        self.assertEqual((self.local / 'ayna' / 'kopru.html').read_bytes(), mirror)

    def guarded_state(self):
        """Önkoşul reddi, eldeki işi ve Git durumunu değiştirmemeli."""
        mirror = self.local / 'ayna' / 'kopru.html'
        return {
            'head': self.git(self.local, 'rev-parse', 'HEAD'),
            'branch': self.git(self.local, 'symbolic-ref', '--short', 'HEAD'),
            'status': self.git(self.local, 'status', '--porcelain'),
            'index': self.git(self.local, 'ls-files', '--stage'),
            'staged': self.git(self.local, 'diff', '--cached', '--binary'),
            'config': (self.local / '.git' / 'config').read_bytes(),
            'bridge': (self.local / 'kopru.html').read_bytes(),
            'mirror': mirror.read_bytes(),
            'mirror_mtime': mirror.stat().st_mtime_ns,
            'remote': self.remote_head(),
        }

    def test_feature_branch_cannot_publish_main_or_regenerate_mirror(self):
        self.git(self.local, 'switch', '-c', 'feature/maintenance')
        (self.local / 'feature.txt').write_text('henüz birleşmemiş özellik\n', encoding='utf-8')
        self.commit(self.local, 'özellik dalındaki çalışma')
        self.append(self.local, 'Özellik kaydı', '2026-10-02T00:00:00+00:00')
        before = self.guarded_state()
        result = self.send()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('main', result.stderr)
        self.assertEqual(self.guarded_state(), before)
        self.assertEqual(self.remote_head(), self.initial)

    def test_active_merge_is_preserved_and_stops_before_mirror_generation(self):
        self.git(self.local, 'switch', '-c', 'other-change')
        (self.local / 'kayit' / 'same.md').write_text('diğer dal\n', encoding='utf-8')
        self.commit(self.local, 'diğer dal değişikliği')
        self.git(self.local, 'switch', 'main')
        (self.local / 'kayit' / 'same.md').write_text('ana dal değişikliği\n', encoding='utf-8')
        self.commit(self.local, 'ana dal değişikliği')
        merge = self.command(self.local, 'git', 'merge', '--no-edit', 'other-change', check=False)
        self.assertNotEqual(merge.returncode, 0, merge.stdout + merge.stderr)
        marker = self.local / '.git' / 'MERGE_HEAD'
        marker_before = marker.read_bytes()
        conflict_before = (self.local / 'kayit' / 'same.md').read_bytes()
        self.append(self.local, 'Bekleyen birleşme', '2026-10-02T00:00:00+00:00')
        before = self.guarded_state()
        result = self.send()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('MERGE_HEAD', result.stderr)
        self.assertEqual(marker.read_bytes(), marker_before)
        self.assertEqual((self.local / 'kayit' / 'same.md').read_bytes(), conflict_before)
        self.assertEqual(self.guarded_state(), before)

    def test_staged_unrelated_file_is_refused_and_preserved(self):
        unrelated = self.local / 'unrelated.txt'
        unrelated.write_text('ayrı iş için hazırlanmış dosya\n', encoding='utf-8')
        self.git(self.local, 'add', 'unrelated.txt')
        self.append(self.local, 'Bekleyen kayıt', '2026-10-02T00:00:00+00:00')
        before = self.guarded_state()
        result = self.send()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('unrelated.txt', result.stderr)
        self.assertEqual(unrelated.read_text(encoding='utf-8'), 'ayrı iş için hazırlanmış dosya\n')
        self.assertEqual(self.guarded_state(), before)

    def test_success_publishes_regenerated_mirror_and_log(self):
        self.append(self.local, 'Yeni kayıt', '2026-10-02T00:00:00+00:00')
        (self.local / 'kayit' / 'result.md').write_text('sentetik sonuç\n', encoding='utf-8')
        self.assertNotIn('Yeni kayıt', (self.local / 'ayna' / 'kopru.html').read_text(encoding='utf-8'))
        result = self.send()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotEqual(self.remote_head(), self.initial)
        self.assertEqual(self.remote_bytes('kayit/result.md'), 'sentetik sonuç\n'.encode('utf-8'))
        self.assert_mirror_matches_remote_bridge()
        self.assertEqual(self.git(self.local, 'status', '--porcelain'), '')

    def test_rejected_push_fails_after_three_attempts_and_keeps_local_commit(self):
        self.append(self.local, 'Gönderilmeyen kayıt', '2026-10-02T00:00:00+00:00')
        hook = self.remote / 'hooks' / 'pre-receive'
        hook.write_text("#!/bin/sh\nprintf 'attempt\\n' >> push-attempts.log\nexit 1\n", encoding='utf-8')
        hook.chmod(0o755)
        result = self.send()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual((self.remote / 'push-attempts.log').read_text().splitlines(), ['attempt'] * 3)
        self.assertEqual(self.remote_head(), self.initial)
        self.assertIn('Gönderilmeyen kayıt', self.git(self.local, 'show', 'HEAD:kopru.html'))
        self.assertEqual(self.git(self.local, 'status', '--porcelain'), '')
        self.assert_no_rebase()

    def test_unknown_conflict_aborts_without_losing_either_version(self):
        writer = self.clone_writer()
        (writer / 'kayit' / 'same.md').write_text('uzak değişiklik\n', encoding='utf-8')
        self.commit(writer, 'uzak günlük düzenlemesi')
        self.git(writer, 'push', '-q', 'origin', 'main')
        remote_before = self.remote_head()
        (self.local / 'kayit' / 'same.md').write_text('yerel değişiklik\n', encoding='utf-8')
        result = self.send()
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('kayit/same.md', result.stdout + result.stderr)
        self.assertEqual(self.remote_head(), remote_before)
        self.assertEqual(self.remote_bytes('kayit/same.md'), 'uzak değişiklik\n'.encode('utf-8'))
        self.assertEqual((self.local / 'kayit' / 'same.md').read_text(encoding='utf-8'), 'yerel değişiklik\n')
        self.assertEqual(self.git(self.local, 'show', 'HEAD:kayit/same.md'), 'yerel değişiklik')
        self.assertEqual(self.git(self.local, 'merge-base', 'HEAD', 'origin/main'), self.initial)
        self.assertEqual(self.git(self.local, 'status', '--porcelain'), '')
        self.assert_no_rebase()

    def test_concurrent_appends_preserve_records_reply_links_and_mirror(self):
        writer = self.clone_writer()
        self.append(writer, 'Uzak ek', '2026-10-02T00:00:00+00:00')
        self.generate(writer)
        self.commit(writer, 'uzak kayıt')
        self.git(writer, 'push', '-q', 'origin', 'main')
        self.append(self.local, 'Yerel ek', '2026-10-03T00:00:00+00:00', reply='k-0001')
        self.append(self.local, 'Yerel yanıt', '2026-10-04T00:00:00+00:00', reply='k-0002')
        result = self.send()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        bridge = self.remote_bytes('kopru.html').decode('utf-8')
        self.assertEqual(re.findall(r'<h3>(.*?)</h3>', bridge),
                         ['Başlangıç', 'Uzak ek', 'Yerel ek', 'Yerel yanıt'])
        self.assertEqual(
            re.findall(r'<article class="kayit" id="([^"]+)"[^>]*data-yanit="([^"]*)"', bridge),
            [('k-0001', ''), ('k-0002', ''), ('k-0003', 'k-0001'), ('k-0004', 'k-0003')],
        )
        self.assert_mirror_matches_remote_bridge()
        self.assertEqual(self.git(self.local, 'status', '--porcelain'), '')
        self.assert_no_rebase()


if __name__ == '__main__':
    unittest.main()
