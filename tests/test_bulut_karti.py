"""Bulut oturum kartı: kanca kartı yalnız uzak oturumda yazar; ağ ve sağlayıcı yok."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / 'docs' / 'BULUT_KARTI.md'
SETTINGS = ROOT / '.claude' / 'settings.json'
sys.path.insert(0, str(ROOT))

from kopru_ekle import yasak_kontrol  # noqa: E402


def load_settings():
    return json.loads(SETTINGS.read_text(encoding='utf-8'))


class CardSettingsTests(unittest.TestCase):
    def test_settings_register_only_one_session_start_command(self):
        settings = load_settings()
        self.assertEqual(list(settings), ['hooks'])
        self.assertEqual(list(settings['hooks']), ['SessionStart'])
        groups = settings['hooks']['SessionStart']
        self.assertEqual(len(groups), 1)
        # Eşleyici yok: kart açılışta, devamda ve bağlam özetinden sonra yeniden girer.
        self.assertEqual(list(groups[0]), ['hooks'])
        self.assertEqual(len(groups[0]['hooks']), 1)
        self.assertEqual(groups[0]['hooks'][0]['type'], 'command')

    def test_card_names_roles_and_passes_public_repository_guards(self):
        text = CARD.read_text(encoding='utf-8')
        for phrase in ('Claude (Code Bulut)', 'ChatGPT (Şaman)', 'Gemini (Şahit)',
                       'kopru_ekle.py', 'belirsiz'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        self.assertEqual(yasak_kontrol(text), [])
        self.assertIsNone(re.search(r'\b[A-Za-z]:\\', text), 'kartta yerel sürücü yolu olmamalı')


@unittest.skipUnless(os.name == 'posix' and shutil.which('sh'), 'Kanca sınaması POSIX kabuğu gerektirir.')
class SessionStartHookTests(unittest.TestCase):
    def run_hook(self, shell, remote, project_dir=ROOT):
        env = {key: value for key, value in os.environ.items()
               if key not in ('CLAUDE_CODE_REMOTE', 'CLAUDE_PROJECT_DIR')}
        if remote is not None:
            env['CLAUDE_CODE_REMOTE'] = remote
        if project_dir is not None:
            env['CLAUDE_PROJECT_DIR'] = str(project_dir)
        command = load_settings()['hooks']['SessionStart'][0]['hooks'][0]['command']
        return subprocess.run([shell, '-c', command], cwd=ROOT, env=env,
                              capture_output=True, timeout=30)

    def shells(self):
        return [path for path in (shutil.which('sh'), shutil.which('bash')) if path]

    def test_hook_is_silent_outside_cloud_sessions(self):
        for shell in self.shells():
            for remote in (None, '', 'false', 'TRUE'):
                with self.subTest(shell=shell, remote=remote):
                    result = self.run_hook(shell, remote)
                    self.assertEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, b'')
                    self.assertEqual(result.stderr, b'')

    def test_hook_prints_card_verbatim_in_cloud_sessions(self):
        for shell in self.shells():
            for project_dir in (ROOT, None):
                with self.subTest(shell=shell, project_dir=project_dir):
                    result = self.run_hook(shell, 'true', project_dir)
                    self.assertEqual(result.returncode, 0)
                    self.assertEqual(result.stdout, CARD.read_bytes())
                    self.assertEqual(result.stderr, b'')


if __name__ == '__main__':
    unittest.main()
