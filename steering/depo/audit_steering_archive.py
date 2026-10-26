#!/usr/bin/env python3
"""Reproduce the 26 October 2026 Steering archive/publication reconciliation.

The source ZIP is required locally and is not part of the public publication.
Only the requested JSON output is written; source data and Git refs stay unchanged.
The root-path substitution is inferred internally from paired catalog entries.
"""

from pathlib import Path
from collections import Counter
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re
import subprocess
import zipfile

parser = argparse.ArgumentParser(
    description=(
        'Compare the original Steering archive with a pinned Git publication. '
        'Repository and archive inputs are read-only; only --output is written.'
    )
)
parser.add_argument('--repo', type=Path, required=True, help='Local Git repository path')
parser.add_argument('--archive', type=Path, required=True, help='Original Steering ZIP path')
parser.add_argument(
    '--ref', default='80fd42db48e91104383b47b6b4144f01790999be',
    help='Immutable publication commit or other Git ref (default: audited 24 October commit)'
)
parser.add_argument('--output', type=Path, required=True, help='Destination audit JSON path')
args = parser.parse_args()
REPO = args.repo.resolve()
ZIP = args.archive.resolve()
REF = args.ref
OUTPUT = args.output.resolve()
if OUTPUT == ZIP:
    parser.error('--output must differ from the archive input')
PREFIX = 'Steering_Evrak_Okuma_Paketi/'
ARCHIVE_SOURCE_ROOT = None


def infer_archive_source_root(original, published):
    """Infer the documented root substitution without embedding a private local path."""
    candidates = Counter()

    def visit(source_value, public_value):
        if isinstance(source_value, dict) and isinstance(public_value, dict):
            for key in source_value.keys() & public_value.keys():
                visit(source_value[key], public_value[key])
        elif isinstance(source_value, list) and isinstance(public_value, list):
            for source_item, public_item in zip(source_value, public_value):
                visit(source_item, public_item)
        elif isinstance(source_value, str) and isinstance(public_value, str):
            marker = '[ARSIV_KOKU]/'
            if public_value.startswith(marker):
                tail = public_value.removeprefix(marker)
                if tail and source_value.endswith(tail):
                    prefix = source_value[:-len(tail)]
                    if prefix:
                        candidates[prefix] += 1

    visit(original, published)
    if len(candidates) != 1:
        raise ValueError(
            'Expected exactly one archival source root from paired inventory paths; '
            f'found {len(candidates)}. No output was written.'
        )
    return next(iter(candidates))

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def transform_value(value):
    if isinstance(value, dict):
        return {k:transform_value(v) for k,v in value.items()}
    if isinstance(value, list):
        return [transform_value(v) for v in value]
    if isinstance(value, str):
        value = value.replace(ARCHIVE_SOURCE_ROOT, '[ARSIV_KOKU]/')
        value = re.sub(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b','[UUID_MASKELENDI]',value)
        value = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b','[IP_BICIMLI_DEGER_MASKELENDI]',value)
    return value

def report_normalize(value):
    value = value.replace(ARCHIVE_SOURCE_ROOT, '[ARSIV_KOKU]/')
    value = re.sub(r'\[([^\]]+)\]\(sandbox:([^\)]+)\)',lambda m:m.group(1)+' (ozgun arsiv konumu: `'+m.group(2)+'`; [kaynak katalogu](../kaynaklar.json))',value)
    # Destination-only comparison, after independent local-link existence verification.
    value = re.sub(r'\]\([^)]+\)', '](LINK)', value)
    return value

paths = git('ls-tree', '-r', '--name-only', REF, 'steering').decode().splitlines()
published = {p.removeprefix('steering/'): git('show', f'{REF}:{p}') for p in paths}
manifest = json.loads(published['aktarim_manifestosu.json'])
records = manifest['records']
manifest_by_path = {r['source_path']: r for r in records}
issues = []
source_results = []
included_results = []
report_results = []
excluded_candidates = []
duplicate_report_checks = []
all_json = {}
for path, data in published.items():
    if path.endswith('.json'):
        try:
            all_json[path] = json.loads(data)
        except Exception as exc:
            issues.append({'kind':'invalid_published_json','path':path,'error':str(exc)})

with zipfile.ZipFile(ZIP) as z:
    ARCHIVE_SOURCE_ROOT = infer_archive_source_root(
        json.loads(z.read(PREFIX + 'Envanter.json')),
        all_json['kaynaklar.json']['source_inventory'],
    )
    members = {i.filename.removeprefix(PREFIX):i for i in z.infolist() if not i.is_dir()}
    if len(members) != sum(not i.is_dir() for i in z.infolist()):
        issues.append({'kind':'duplicate_zip_member'})
    missing_members = sorted(set(manifest_by_path) - set(members))
    unlisted_members = sorted(set(members) - set(manifest_by_path))
    for path, info in members.items():
        data = z.read(info.filename)
        actual = sha(data)
        expected = manifest_by_path.get(path)
        if expected is None:
            continue
        expected_bytes = expected.get('original_bytes', expected['bytes'])
        expected_sha = expected.get('original_sha256', expected['sha256'])
        ok = len(data) == expected_bytes and actual == expected_sha
        source_results.append({'path':path,'bytes':len(data),'sha256':actual,'matches_manifest':ok})
        if not ok:
            issues.append({'kind':'source_mismatch','path':path,'expected_bytes':expected_bytes,'actual_bytes':len(data),'expected_sha256':expected_sha,'actual_sha256':actual})
        if expected['decision'] == 'aktarildi':
            target = expected['target']
            item = {'source_path':path,'target':target,'role':expected['role'],'target_exists':target in published}
            if target not in published:
                issues.append({'kind':'missing_publication_target','source_path':path,'target':target})
            if 'object_key' in expected and target in all_json:
                key = expected['object_key']
                target_item = all_json[target].get('records',{}).get(key)
                item['object_key'] = key
                item['object_exists'] = target_item is not None
                item['recorded_original_sha256_matches'] = bool(target_item and target_item.get('original_sha256') == actual)
                if target_item is None:
                    issues.append({'kind':'missing_consolidated_object','source_path':path,'target':target,'object_key':key})
                else:
                    item['parsed_json_equal_before_documented_transforms'] = target_item.get('content') == json.loads(data)
                    item['parsed_json_equal_after_documented_transforms'] = target_item.get('content') == transform_value(json.loads(data))
                    if not item['parsed_json_equal_after_documented_transforms']:
                        issues.append({'kind':'unreconciled_consolidated_json','source_path':path,'target':target})
            elif expected['role'] == 'tam_kaynak_kunyesi' and target in all_json:
                key = {'Atif_Kaynaklari.json':'citation_registry','Envanter.json':'source_inventory','Sayfa_Dizini.json':'original_page_directory'}[path]
                item['catalog_section'] = key
                item['parsed_json_equal_after_documented_transforms'] = all_json[target][key] == transform_value(json.loads(data))
                if not item['parsed_json_equal_after_documented_transforms']:
                    issues.append({'kind':'unreconciled_catalog_json','source_path':path,'target':target})
            elif expected['role'] == 'tam_guncel_okuma_durumu':
                actual_status = dict(all_json[target])
                item['added_publication_metadata'] = {'publication_notice':actual_status.pop('publication_notice',None)}
                item['parsed_json_equal_after_documented_transforms'] = actual_status == transform_value(json.loads(data))
                if not item['parsed_json_equal_after_documented_transforms']:
                    issues.append({'kind':'unreconciled_reading_status_json','source_path':path,'target':target})
            included_results.append(item)
            if expected['role'] in ('tam_analitik_rapor','tam_tamamlayici_rapor'):
                source = data.decode('utf-8')
                dest = published[target].decode('utf-8')
                firstline = source.splitlines()[0]
                content_start = dest.find(firstline)
                body = dest[content_start:] if content_start >= 0 else dest
                reconciled = report_normalize(source) == report_normalize(body)
                report_results.append({'source_path':path,'target':target,'source_chars':len(source),'published_chars':len(dest),'source_body_exact_substring':source in dest,'source_body_preserved_after_documented_transforms':reconciled,'body_status':'exact_source_body_with_publication_note' if source in dest else ('body_preserved_with_documented_path_or_link_transforms' if reconciled else 'unreconciled')})
                if not reconciled:
                    issues.append({'kind':'unreconciled_report','source_path':path,'target':target})
        elif path.startswith('incelemeler/') and path.endswith(('.md','.json')):
            excluded_candidates.append({'source_path':path,'reason':expected.get('reason'),'bytes':len(data)})
        if expected['decision'] != 'aktarildi' and (path.endswith('/report.json') or path.endswith('/document_status.json') or path == 'Steering_Incelemesi.json'):
            body = json.loads(data).get('text')
            text_path = 'Steering_Incelemesi.txt' if path == 'Steering_Incelemesi.json' else path.removesuffix('.json')+'.md'
            equal = isinstance(body,str) and text_path in members and body == z.read(members[text_path].filename).decode('utf-8')
            duplicate_report_checks.append({'source_json':path,'source_text':text_path,'text_field_exactly_equal':equal})
            if not equal:
                issues.append({'kind':'unreconciled_duplicate_report_json','path':path,'text_path':text_path})

checksum_results = []
for line in published['SHA256SUMS'].decode().splitlines():
    if not line.strip():
        continue
    expected, path = line.split(maxsplit=1)
    path = path.lstrip('*')
    actual = sha(published[path]) if path in published else None
    checksum_results.append({'path':path,'expected_sha256':expected,'actual_sha256':actual,'matches':actual == expected})
    if actual != expected:
        issues.append({'kind':'published_checksum_mismatch','path':path,'expected_sha256':expected,'actual_sha256':actual})

links = []
for path, data in published.items():
    if not path.endswith('.md'):
        continue
    text = data.decode('utf-8')
    for match in re.finditer(r'\[[^\]\n]*\]\(([^\n)]+)\)', text):
        href = match.group(1).strip().strip('<>')
        if urlsplit(href).scheme or href.startswith(('#','//')):
            continue
        target_path = unquote(href.split('#',1)[0].split('?',1)[0])
        full = Path(path).parent / target_path
        stack = []
        for part in full.parts:
            if part == '..':
                if stack: stack.pop()
                else: stack.append('..')
            elif part != '.': stack.append(part)
        resolved = '/'.join(stack)
        ok = resolved in published or any(p.startswith(resolved.rstrip('/') + '/') for p in published)
        links.append({'source':path,'href':href,'resolved_path':resolved,'exists':ok})
        if not ok:
            issues.append({'kind':'unresolved_relative_markdown_link','source':path,'href':href,'resolved_path':resolved})

result = {
    'schema_version':'1.0',
    'audit_date':'2026-10-26',
    'repository':'HalukAINRS/ortak-kopru',
    'publication_ref':REF,
    'archive':{'name':ZIP.name,'bytes':ZIP.stat().st_size,'sha256':sha(ZIP.read_bytes()),'file_members':len(members),'uncompressed_bytes':sum(i.file_size for i in members.values()),'all_members_decompressed_and_crc_checked':True,'matches_declared_archive_size_and_sha256':ZIP.stat().st_size==manifest['source_package_bytes'] and sha(ZIP.read_bytes())==manifest['source_package_sha256']},
    'source_manifest':{'entries':len(records),'unique_paths':len(manifest_by_path),'checked_entries':len(source_results),'matching_entries':sum(x['matches_manifest'] for x in source_results),'missing_zip_members':missing_members,'unlisted_zip_members':unlisted_members,'decisions':dict(Counter(r['decision'] for r in records)),'excluded_reasons':dict(Counter(r.get('reason','') for r in records if r['decision']!='aktarildi'))},
    'publication':{'files':len(published),'sha256sum_entries':len(checksum_results),'sha256sum_matches':sum(x['matches'] for x in checksum_results),'files_not_listed_in_sha256sums':sorted(set(published)-{x['path'] for x in checksum_results}),'json_files_parsed':len(all_json),'relative_markdown_links_checked':len(links),'relative_markdown_links_resolved':sum(x['exists'] for x in links),'included_source_records':len(included_results),'included_roles':dict(Counter(x['role'] for x in included_results)),'exact_report_bodies_with_optional_publication_note':sum(x['source_body_exact_substring'] for x in report_results),'all_report_bodies_checked':len(report_results),'report_bodies_preserved_after_documented_transforms':sum(x['source_body_preserved_after_documented_transforms'] for x in report_results),'json_source_records_compared':sum('parsed_json_equal_after_documented_transforms' in x for x in included_results),'json_source_records_preserved_after_documented_transforms':sum(x.get('parsed_json_equal_after_documented_transforms',False) for x in included_results)},
    'included_source_records':included_results,
    'duplicate_report_container_checks':duplicate_report_checks,
    'report_body_comparison':report_results,
    'excluded_analysis_directory_candidates':excluded_candidates,
    'published_checksum_results':checksum_results,
    'issues':issues,
    'limits':['This is byte, metadata, target-existence and representation reconciliation. It does not re-read 460800693 uncompressed source bytes semantically.','Source strings can differ from public strings because recorded redactions, path substitutions and link relocation were applied. No private source bodies or removed bridge content were restored.','Earlier report dates and scope remain historical; newer main-branch corrections must qualify current interpretation.']
}
OUTPUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['archive','source_manifest','publication','issues']},ensure_ascii=False,indent=2))
print('Reports with transformed bodies:',json.dumps([r for r in report_results if not r['source_body_exact_substring']],ensure_ascii=False))
