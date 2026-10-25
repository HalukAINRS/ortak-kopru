import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cyber_dosya_sonucu import verify_write


class WriteRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.file = self.root / 'result.txt'

    def check(self, expected):
        return verify_write(self.file, expected, self.root)

    def test_current_match_never_proves_historical_completion(self):
        self.file.write_bytes('Türkçe\n'.encode())
        result = self.check('Türkçe\n')
        self.assertEqual(result['current_state'], 'matches_declared_write_now')
        self.assertFalse(result['completed_at_interruption_proven'])
        self.assertFalse(result['automatic_retry'])

    def test_missing_does_not_authorize_replay(self):
        result = self.check('expected')
        self.assertEqual(result['current_state'], 'missing')
        self.assertFalse(result['automatic_retry'])

    def test_later_successor_is_preserved(self):
        self.file.write_bytes(b'later user contribution')
        result = self.check('old write')
        self.assertEqual(result['current_state'], 'differs_now_do_not_overwrite')
        self.assertEqual(self.file.read_bytes(), b'later user contribution')

    def test_newline_difference_is_not_silently_normalized(self):
        self.file.write_bytes(b'line\r\n')
        self.assertEqual(self.check('line\n')['current_state'], 'differs_now_do_not_overwrite')

    def test_outside_scope_is_not_read(self):
        outside = self.root / 'other'
        outside.mkdir()
        self.file.write_bytes(b'private')
        self.assertEqual(verify_write(self.file, 'private', outside)['current_state'], 'outside_scope_or_symlink')

    def test_changed_content_even_with_same_size_is_rejected(self):
        self.file.write_bytes(b'old')
        original = Path.read_bytes
        reads = 0

        def changing_read(path):
            nonlocal reads
            data = original(path)
            reads += 1
            if reads == 1:
                path.write_bytes(b'new')
            return data

        with patch.object(Path, 'read_bytes', changing_read):
            self.assertEqual(self.check('old')['current_state'], 'changed_during_read')

    def test_directory_and_invalid_expected_content_are_not_accepted(self):
        self.assertEqual(verify_write(self.root, '', self.root)['current_state'], 'not_regular_file')
        self.assertEqual(self.check(None)['current_state'], 'invalid_expected_content')


if __name__ == '__main__':
    unittest.main()
