import json
import unittest
from cyber_salt_okunur import META_PREFIX, scan


def rows(*items):
    return b''.join((json.dumps(x) + '\n').encode() for x in items)


class CyberAuditTest(unittest.TestCase):
    def test_only_direct_category_events_count(self):
        event = {'type': 'system', 'subtype': 'model_refusal_fallback', 'apiRefusalCategory': 'cyber'}
        raw = rows(event, {'type': 'assistant', 'message': {'content': json.dumps(event)}},
                   dict(event, apiRefusalCategory='other'))
        self.assertEqual([x['line'] for x in scan(raw)['cyber_events']], [1])

    def test_user_quote_does_not_become_meta(self):
        user = {'type': 'user', 'message': {'role': 'user', 'content': META_PREFIX}}
        report = scan(rows(user, dict(user, isMeta=True)))
        self.assertEqual([x['line'] for x in report['meta_stops']], [2])
        self.assertFalse(report['meta_stops'][0]['user_decision'])

    def test_interrupted_write_is_not_failed_or_complete_disk_write(self):
        call = {'type': 'assistant', 'message': {'content': [{'type': 'tool_use', 'id': 'private-id',
                'name': 'Write', 'input': {'file_path': '/private/source', 'content': 'SECRET'}}]}}
        result = {'type': 'user', 'message': {'content': [{'type': 'tool_result', 'tool_use_id': 'private-id',
                  'is_error': True, 'content': 'Interrupted: partial completion possible SECRET'}]}}
        report = scan(rows(call, result))
        item = report['interrupted_tools'][0]
        self.assertEqual(item['call']['line'], 1)
        self.assertEqual(item['disk_state'], 'unknown_requires_file_check')
        self.assertFalse(item['automatic_retry'])
        for private in ('SECRET', 'private-id', '/private/source'):
            self.assertNotIn(private, json.dumps(report))

    def test_tool_output_quoting_interrupted_is_not_an_interruption(self):
        def result(error, text):
            return {'type': 'user', 'message': {'content': [{'type': 'tool_result',
                    'is_error': error, 'content': text}]}}
        report = scan(rows(result(False, 'Interrupted: a line printed by grep'),
                           result(True, 'Read error in a source containing Interrupted: quoted text')))
        self.assertEqual(report['interrupted_tools'], [])

    def test_truncated_live_tail_is_incomplete(self):
        report = scan(rows({'type': 'user'}) + b'{"type":')
        self.assertFalse(report['complete_parse'])
        self.assertEqual(report['invalid_lines'], [2])

    def test_valid_unterminated_tail_still_not_full_snapshot(self):
        self.assertFalse(scan(b'{"type":"user"}')['complete_parse'])

    def test_malformed_middle_does_not_silently_pass(self):
        self.assertFalse(scan(b'bad\n' + rows({'type': 'user'}))['complete_parse'])

    def test_thinking_and_explanation_bodies_are_not_exported(self):
        report = scan(rows({'type': 'assistant', 'message': {'content': [{'type': 'thinking', 'thinking': 'PRIVATE'}]}},
                           {'type': 'system', 'subtype': 'model_refusal_fallback', 'apiRefusalCategory': 'cyber',
                            'apiRefusalExplanation': 'PRIVATE'}))
        self.assertTrue(report['cyber_events'][0]['explanation_present'])
        self.assertNotIn('PRIVATE', json.dumps(report))

    def test_detection_never_closes_prevention_or_recovery(self):
        report = scan(b'')
        self.assertFalse(report['safety_decision_prevented'])
        self.assertFalse(report['recovery_completed'])
        self.assertFalse(report['event_and_meta_counts_are_additive'])


if __name__ == '__main__':
    unittest.main()
