"""Salt okunur Steering kontrolü; kaynak gövdelerini veya erişim değerlerini dışa vermez."""
import argparse
import ast
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tomllib


def sha(data):
    return hashlib.sha256(data).hexdigest()


class Bootstrap(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'script' and dict(attrs).get('id') == 'client-bootstrap':
            self.inside = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.inside = False

    def handle_data(self, data):
        if self.inside:
            self.parts.append(data)


def html_summary(path):
    data = path.read_bytes()
    parser = Bootstrap()
    parser.feed(data.decode('utf-8-sig'))
    result = {'source_kind': 'user_supplied_saved_chatgpt_html', 'sha256': sha(data), 'bootstrap_present': bool(parser.parts)}
    if not parser.parts:
        return result
    bootstrap = json.loads(''.join(parser.parts))
    payload = bootstrap.get('statsigPayload')
    if isinstance(payload, str):
        payload = json.loads(payload)
    result['statsig_present'] = isinstance(payload, dict)
    if not isinstance(payload, dict):
        return result
    counts = {}
    for key in ('feature_gates', 'dynamic_configs', 'layer_configs'):
        rows = payload.get(key, {})
        values = [r.get('value') for r in rows.values() if isinstance(r, dict)]
        counts[key] = {'entries': len(rows), 'boolean_true': sum(v is True for v in values),
                       'boolean_false': sum(v is False for v in values),
                       'other_value_types': sum(type(v) is not bool for v in values)}
    result['structure_counts'] = counts
    layer = payload.get('layer_configs', {}).get('2023018368', {}).get('value', {})
    names = ('mainline_classifier_steering_enabled', 'imagegen_steerability_enabled', 'disney_steerability_enabled')
    result['three_saved_flags'] = {k: layer[k] for k in names if type(layer.get(k)) is bool}
    result['runtime_activation_verified'] = False
    return result


def function_node(path, name):
    tree = ast.parse(path.read_text(encoding='utf-8-sig'))
    return next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bridge-dir', required=True, type=Path)
    parser.add_argument('--codex-root', required=True, type=Path)
    parser.add_argument('--source-html', type=Path)
    parser.add_argument('--source-zip', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    steering = Path(__file__).resolve().parents[1]
    checked = []
    for line in (steering/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
        expected, name = line.split('  ', 1)
        path = (steering/name).resolve()
        if not path.is_relative_to(steering):
            raise ValueError('Karma listesi klasör dışına çıkıyor.')
        checked.append({'path': name, 'matches': path.is_file() and sha(path.read_bytes()) == expected})
    if not all(r['matches'] for r in checked):
        raise ValueError('Sabit inceleme dosyası farklı veya eksik.')
    bridge = args.bridge_dir.resolve()
    sys.path.insert(0, str(bridge))
    from kopru_oku import Ayristirici
    # Yalnız atama fonksiyonları yürütülür. Ana akış, CLI veya API çağrısı yok.
    source = bridge/'kopru_yanitla.py'
    names = ('ad_kok', 'hedef_kimligi', 'kime_adlari', 'numara', 'bekleyenler')
    available = {n.name for n in ast.parse(source.read_text(encoding='utf-8-sig')).body if isinstance(n, ast.FunctionDef)}
    nodes = [function_node(source, name) for name in names if name in available]
    namespace = {'re': __import__('re')}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(source), 'exec'), namespace)
    request = {'id': 'k-0001', 'kimden': 'Sen', 'kime': 'ChatGPT (Şaman)', 'durum': 'acik', 'yanit': None}
    reply = {'id': 'k-0002', 'kimden': 'ChatGPT (API)', 'kime': 'Sen', 'durum': 'kapandi', 'yanit': 'k-0001'}
    before = namespace['bekleyenler']([request], 'ChatGPT')
    after = namespace['bekleyenler']([request, reply], 'ChatGPT')
    cli_after = namespace['bekleyenler']([request, reply], 'ChatGPT (Şaman)')
    if 'hedef_kimligi' in available:
        assert before == [] and after == [] and cli_after == [request]
    else:
        assert before == [request] and after == []
    page = (bridge/'kopru.html').read_bytes()
    records = Ayristirici()
    records.feed(page.decode('utf-8'))
    codex = args.codex_root.resolve()
    exe = codex/'npm_global/node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe'
    binary = exe.read_bytes()
    endpoints = ('ab.chatgpt.com/otlp/v1/metrics', 'api.openai.com/v1/decisions', 'chatgpt.com/backend-api/cloud-config')
    cache_path = codex/'Home/.codex/models_cache.json'
    cache_data = cache_path.read_bytes()
    cache = json.loads(cache_data)
    config_path = codex/'Home/.codex/config.toml'
    config_data = config_path.read_bytes()
    config = tomllib.loads(config_data.decode('utf-8-sig'))
    selected = {k: config[k] for k in ('model', 'model_reasoning_effort', 'plan_mode_reasoning_effort', 'model_verbosity') if k in config}
    report = {'schema_version': 1, 'captured_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'operation': 'read_only_local_audit', 'provider_calls': 0, 'settings_changed': False,
              'fixed_steering_files': {'verified': len(checked), 'all_match': True},
              'bridge': {'sha256': sha(page), 'records': len(records.kayitlar),
                         'last_id': records.kayitlar[-1]['id'], 'parser_only_not_full_semantic_read': True},
              'routing_reproduction': {'synthetic_fixture': True, 'real_bridge_records_used': False,
                                      'source_sha256': sha(source.read_bytes()),
                                      'function_lines': [nodes[-1].lineno, nodes[-1].end_lineno],
                                      'role_address_accepted_by_producer_root': bool(before),
                                      'api_label_reply_hides_cli_label_request': bool(before) and not after,
                                      'explicit_cli_request_survives_api_reply': cli_after == [request],
                                      'actual_cli_delivery_proven': False},
              'binary': {'name': exe.name, 'sha256': sha(binary), 'bytes': len(binary),
                         'saved_endpoint_strings': {e: binary.count(e.encode()) for e in endpoints},
                         'network_usage_verified': False},
              'cache': {'sha256': sha(cache_data), 'models': len(cache.get('models', [])),
                        'marker_present': {k: k.encode() in cache_data for k in ('guardian_v2', 'auto_review', 'classifier_instructions')},
                        'loaded_or_effective_verified': False},
              'local_config': {'sha256': sha(config_data), 'selected_fields': selected,
                               'server_effective_behavior_verified': False},
              'source_zip': {'present': bool(args.source_zip and args.source_zip.is_file()),
                             'expected_bytes': 100641653,
                             'expected_sha256': '827bb9cac16fdb7b643c576a3bd41523e725ad4542ab023c5c4d45f3435b1009'}}
    if args.source_html:
        report['saved_html'] = html_summary(args.source_html)
    if report['source_zip']['present']:
        data = args.source_zip.read_bytes()
        report['source_zip'].update(bytes=len(data), sha256=sha(data))
        report['source_zip']['matches_expected'] = len(data) == 100641653 and sha(data) == report['source_zip']['expected_sha256']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
