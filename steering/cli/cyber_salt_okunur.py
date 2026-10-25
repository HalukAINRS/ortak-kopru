"""JSONL içinden yalnız kesinti metaverisi çıkarır; araç/model/ağ çağırmaz."""
import argparse
import hashlib
import json
from pathlib import Path
import re

META_PREFIX = 'Your response above was stopped by a safety classifier'


def safe_label(value):
    if isinstance(value, str) and re.fullmatch(r'[A-Za-z0-9_.:-]{1,100}', value):
        return value
    return None


def scan(raw):
    events, stops, interrupted, invalid = [], [], [], []
    calls = {}
    models = []
    lines = raw.splitlines()
    partial_tail = bool(raw and not raw.endswith(b'\n'))
    for number, line in enumerate(lines, 1):
        try:
            row = json.loads(line)
        except (ValueError, UnicodeDecodeError):
            invalid.append(number)
            continue
        if not isinstance(row, dict):
            invalid.append(number)
            continue
        if row.get('type') == 'system' and row.get('subtype') == 'model_refusal_fallback' and row.get('apiRefusalCategory') == 'cyber':
            events.append({'line': number, 'category': 'cyber',
                           'original_model': safe_label(row.get('originalModel')),
                           'fallback_model': safe_label(row.get('fallbackModel')),
                           'scope': safe_label(row.get('scope')),
                           'explanation_present': row.get('apiRefusalExplanation') is not None})
        message = row.get('message')
        if not isinstance(message, dict):
            continue
        content = message.get('content', [])
        blocks = content if isinstance(content, list) else []
        texts = [content] if isinstance(content, str) else [b.get('text', '') for b in blocks if isinstance(b, dict) and b.get('type') == 'text']
        if (row.get('type') == 'user' and message.get('role') == 'user'
                and row.get('isMeta') is True and any(isinstance(t, str) and t.startswith(META_PREFIX) for t in texts)):
            stops.append({'line': number, 'producer': 'client_meta', 'user_decision': False})
        if row.get('type') == 'assistant':
            model = safe_label(message.get('model'))
            if model and (not models or models[-1]['model'] != model):
                models.append({'line': number, 'model': model})
        for block in blocks:
            if not isinstance(block, dict):
                continue
            if row.get('type') == 'assistant' and block.get('type') == 'tool_use':
                calls[block.get('id')] = {'line': number, 'tool': safe_label(block.get('name'))}
            if row.get('type') == 'user' and block.get('type') == 'tool_result':
                call = calls.pop(block.get('tool_use_id'), None)
                result = block.get('content')
                # Never emit tool input, result body, message ID, path, or thinking body.
                if (block.get('is_error') is True and isinstance(result, str)
                        and result.lstrip().startswith('Interrupted:')):
                    interrupted.append({'result_line': number, 'call': call,
                                        'is_error': block.get('is_error') is True,
                                        'disk_state': 'unknown_requires_file_check', 'automatic_retry': False})
    return {'source_sha256': hashlib.sha256(raw).hexdigest(), 'source_bytes': len(raw),
            'source_lines': len(lines), 'invalid_lines': invalid, 'unterminated_tail': partial_tail,
            'complete_parse': not invalid and not partial_tail, 'cyber_events': events,
            'meta_stops': stops, 'model_labels': models, 'interrupted_tools': interrupted,
            'event_and_meta_counts_are_additive': False, 'safety_decision_prevented': False,
            'recovery_completed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    output = args.output.resolve()
    if source == output:
        parser.error('Çıktı kaynak olamaz.')
    report = scan(source.read_bytes())
    # A fresh receipt is required. An old result is never silently replaced.
    with output.open('xb') as stream:
        stream.write((json.dumps(report, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
    print(json.dumps({'events': len(report['cyber_events']), 'meta_stops': len(report['meta_stops']),
                      'complete_parse': report['complete_parse'], 'output': str(output)}))
    return 0 if report['complete_parse'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
