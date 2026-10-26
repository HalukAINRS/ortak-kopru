#!/usr/bin/env python3
"""Read-only audit of a pinned ortak-kopru snapshot; emits compact evidence JSON.
Usage: python repo-log-equivalence.py REPO OUTPUT_JSON
Does not invoke a bot, CLI, workflow, publisher, cleanup, or repository main().
"""
import argparse
import ast
import collections
import hashlib
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess

COMMIT = "8571ddf8e3a33b432cc1c7ef88b69a902f390e5c"
LOG_RX = re.compile(
    r"## Sonuç\n\n(.*?)\n\n## Sistem istemi\n\n\x60{3}\n(.*?)\n\x60{3}\n\n"
    r"## Kullanıcı iletisi\n\n\x60{3}\n(.*?)\n\x60{3}\n\n"
    r"## Ham yanıt\n\n\x60{3}\n(.*?)\n\x60{3}\n?$", re.S
)

def digest(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()

def norm(text):
    return re.sub(r"\s+", " ", text or "").strip()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()

    def git(*words):
        return subprocess.check_output(["git", "-C", str(args.repo), *words])

    files = {}
    for row in git("ls-tree", "-rz", COMMIT).split(b"\0"):
        if not row:
            continue
        info, name = row.split(b"\t", 1)
        mode, kind, blob = info.decode().split()
        assert kind == "blob"
        path = name.decode()
        data = git("cat-file", "blob", blob)
        files[path] = {"blob": blob, "bytes": len(data), "sha256": digest(data), "data": data}
    ns = {"re": re, "html": html, "HTMLParser": HTMLParser}
    pure_sources = [
        ("kopru_oku.py", "Ayristirici"),
        ("kopru_ekle.py", "govde_html"),
        ("kopru_yanitla.py", "bolum_metni"),
    ]
    for filename, definition in pure_sources:
        tree = ast.parse(files[filename]["data"].decode())
        nodes = [node for node in tree.body if getattr(node, "name", None) == definition]
        assert len(nodes) == 1
        # Only the reviewed parser/pure rendering definition is compiled.
        # No repository import statements or entrypoints are executed.
        exec(compile(ast.Module(body=nodes, type_ignores=[]), filename, "exec"), ns)

    canonical = files["kopru.html"]["data"].decode()
    parsed = ns["Ayristirici"]()
    parsed.feed(canonical)
    records = parsed.kayitlar
    identity = lambda item: (item["kimden"], item["zaman"], norm(item["konu"]))
    lookup = {identity(item): item for item in records}
    assert len(lookup) == len(records)
    content_lookup = collections.defaultdict(list)
    for item in records:
        content_lookup[(norm(item["konu"]), norm(item["govde"]))].append(item["id"])

    systems, sections, rows = {}, {}, []
    totals = collections.Counter()
    differences = []
    raw_values = set()
    log_names = sorted(path for path in files if re.fullmatch(r"kayit/20\d{6}-\d{6}Z-.+\.md", path))
    for filename in log_names:
        log_text = files[filename]["data"].decode().replace("\r\n", "\n").replace("\r", "\n")
        m = LOG_RX.search(log_text)
        assert m is not None, filename
        status, system, user, raw = m.groups()
        status_kind = status.split(":", 1)[0]
        totals["status_" + status_kind] += 1
        raw_values.add(raw)
        section = user.split("Sayfadaki “Yönlendirme dosyası” bölümü, metin olarak:\n", 1)[1]
        section = section.rsplit("\n\nŞimdi yalnız JSON nesnesini ver.", 1)[0]
        for text, registry, prefix in ((system, systems, "system"), (section, sections, "section")):
            if text not in registry:
                registry[text] = {
                    "id": f"{prefix}-{len(registry) + 1}",
                    "sha256": digest(text),
                    "characters": len(text),
                    "first_log": filename,
                    "log_count": 0,
                }
            registry[text]["log_count"] += 1
        all_records = json.JSONDecoder().raw_decode(user.split("Sayfadaki bütün kayıtlar (JSON, zaman sırasıyla):\n", 1)[1])[0]
        pending = json.JSONDecoder().raw_decode(user.split("Sana düşen kayıtlar (JSON):\n", 1)[1])[0]
        missing = 0
        changed = 0
        for scope, items in (("all", all_records), ("pending", pending)):
            totals[scope + "_record_occurrences"] += len(items)
            for old in items:
                current = lookup.get(identity(old))
                if current is None:
                    missing += 1
                    totals[scope + "_unmatched_identity"] += 1
                    continue
                for field in ("govde", "dayanak", "kime", "durum", "id", "yanit"):
                    before, after = old[field], current[field]
                    if field in ("govde", "dayanak"):
                        before, after = norm(before), norm(after)
                    if before == after:
                        continue
                    totals[scope + "_" + field + "_different"] += 1
                    diff = {"log": filename, "scope": scope, "record": current["id"], "field": field}
                    if field == "dayanak":
                        only_periods = before.rstrip(".") == after.rstrip(".")
                        diff["only_trailing_period_count"] = only_periods
                        diff["before_sha256"] = digest(before)
                        diff["after_sha256"] = digest(after)
                        diff["before_trailing_periods"] = len(before) - len(before.rstrip("."))
                        diff["after_trailing_periods"] = len(after) - len(after.rstrip("."))
                    else:
                        diff["before"] = before
                        diff["after"] = after
                    differences.append(diff)
                    changed += field == "govde"
        raw_matches = []
        if raw:
            value = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
            rendered = '<article class="kayit"><h3>' + html.escape(value["konu"]) + '</h3><div class="govde">' + ns["govde_html"](value["govde"]) + "</div></article>"
            q = ns["Ayristirici"]()
            q.feed(rendered)
            got = q.kayitlar[0]
            raw_matches = content_lookup[(norm(got["konu"]), norm(got["govde"]))]
            totals["nonempty_raw"] += 1
            totals["raw_matched_to_canonical"] += bool(raw_matches)
        else:
            totals["empty_raw"] += 1
        rows.append([
            filename, files[filename]["sha256"], files[filename]["bytes"], status_kind,
            raw_matches, len(all_records), len(pending), missing, changed,
            systems[system]["id"], sections[section]["id"],
        ])

    # Reproduce the reviewed mirror transformation in memory; never write the mirror.
    head = re.search(r"<head>(.*?)</head>", canonical, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", canonical, re.S).group(1)
    title = re.search(r"<title>.*?</title>", head, re.S).group(0)
    metas = [m for m in re.findall(r"<meta [^>]*>", head) if "charset" not in m and 'name="viewport"' not in m]
    style = re.search(r"<style>.*?</style>", head, re.S).group(0)
    mirror = title + "\n" + "\n".join(metas) + "\n" + style + "\n" + body.strip() + "\n"
    mirror_equal = mirror.encode() == files["ayna/kopru.html"]["data"]

    for name in (
        "all_unmatched_identity", "pending_unmatched_identity", "all_govde_different",
        "pending_govde_different", "all_kime_different", "pending_kime_different",
        "all_durum_different", "pending_durum_different", "all_yanit_different",
        "pending_yanit_different", "pending_id_different", "pending_dayanak_different",
    ):
        totals[name] += 0
    output = {
        "schema_version": 1,
        "repository": "HalukAINRS/ortak-kopru",
        "commit": COMMIT,
        "tree": git("rev-parse", COMMIT + "^{tree}").decode().strip(),
        "method": {
            "log_split": LOG_RX.pattern,
            "source_text_decoding": "UTF-8 with universal-newline normalization; file hashes and sizes remain original blob bytes",
            "identity": ["kimden", "zaman", "whitespace_normalized_konu"],
            "body_comparison": "canonical parser text; raw JSON rendered by pinned govde_html then parsed by pinned Ayristirici; collapse whitespace only",
            "input_comparison": "all historical full-list and pending-list identities and body/evidence/recipient/state/id/reply fields compared with canonical records",
            "scope_limit": "This is text equivalence, not proof of factual truth, origin, successful tools, model identity or live provider behavior.",
            "execution_limit": "Read-only git object reads and reviewed pure parser/render definitions; no bot, cleanup, provider request, script entrypoint or test suite executed.",
            "code_file": "repo-log-equivalence.py",
            "code_sha256": digest(Path(__file__).read_bytes()),
            "pinned_parser_files": {f: files[f]["sha256"] for f, _ in pure_sources},
        },
        "counts": {
            "tracked_files": len(files),
            "canonical_records": len(records),
            "dated_logs": len(log_names),
            "dated_log_bytes": sum(files[f]["bytes"] for f in log_names),
            "distinct_system_prompts": len(systems),
            "distinct_steering_sections": len(sections),
            "distinct_raw_strings_including_empty": len(raw_values),
            "distinct_raw_characters_total": sum(map(len, raw_values)),
            **dict(totals),
        },
        "system_versions": list(systems.values()),
        "steering_section_versions": list(sections.values()),
        "latest_section_equals_canonical": list(sections)[-1] == ns["bolum_metni"](canonical, "yonlendirme"),
        "mirror_exactly_matches_current_generator": mirror_equal,
        "metadata_differences": differences,
        "log_row_fields": [
            "path", "sha256", "bytes", "status", "canonical_raw_matches",
            "all_record_occurrences", "pending_record_occurrences",
            "unmatched_identities", "different_bodies", "system_version", "steering_section_version"
        ],
        "logs": rows,
    }
    assert output["latest_section_equals_canonical"]
    assert mirror_equal
    assert totals["raw_matched_to_canonical"] == totals["nonempty_raw"]
    assert not totals["all_unmatched_identity"] and not totals["pending_unmatched_identity"]
    assert not totals["all_govde_different"] and not totals["pending_govde_different"]
    assert all(x.get("only_trailing_period_count", True) for x in differences)
    args.output_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"counts": output["counts"], "mirror_equal": mirror_equal, "latest_section_equal": output["latest_section_equals_canonical"], "output_bytes": args.output_json.stat().st_size}, ensure_ascii=False))

if __name__ == "__main__":
    main()

