#!/usr/bin/env python3
"""Generate the offline handoff files from source.json using only the standard library."""
import argparse
import hashlib
import html
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUTS = ("handoff.txt", "handoff.html", "handoff.json", "START_HERE.md")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def stable_json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def text_lines(value, depth=0):
    indent = "  " * depth
    if isinstance(value, dict):
        out = []
        for key, item in value.items():
            out.append(f"{indent}{key}:")
            out.extend(text_lines(item, depth + 1))
        return out
    if isinstance(value, list):
        if not value:
            return [f"{indent}(none)"]
        out = []
        for item in value:
            if isinstance(item, (dict, list)):
                out.append(f"{indent}-")
                out.extend(text_lines(item, depth + 1))
            else:
                out.append(f"{indent}- {item}")
        return out
    return [f"{indent}{value}"]


def render_html(value, depth=2):
    if isinstance(value, dict):
        sections = []
        for key, item in value.items():
            label = html.escape(str(key))
            sections.append(
                f"<section><h{min(depth, 6)}>{label}</h{min(depth, 6)}>"
                f"{render_html(item, min(depth + 1, 6))}</section>"
            )
        return "\n".join(sections)
    if isinstance(value, list):
        if not value:
            return "<p>(none)</p>"
        items = "".join(f"<li>{render_html(item, depth)}</li>" for item in value)
        return f"<ul>{items}</ul>"
    return "<p>" + html.escape(str(value)).replace("\n", "<br>\n") + "</p>"


def generated_files(source):
    json_bytes = stable_json(source)
    title = html.escape(source["title"])
    body = render_html(source)
    html_bytes = (
        '<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n"
        "<style>body{font:16px/1.55 system-ui,sans-serif;max-width:78ch;margin:2rem auto;padding:0 1rem}"
        "section{margin:1.5rem 0}h1,h2,h3,h4,h5,h6{line-height:1.25}code,pre{font-family:monospace}"
        "li{margin:.35rem 0}</style>\n</head>\n<body>\n<main>\n"
        f"<h1>{title}</h1>\n{body}\n</main>\n</body>\n</html>\n"
    ).encode("utf-8")
    lines = text_lines(source)
    text_bytes = (source["title"] + "\n" + "=" * len(source["title"]) + "\n\n" + "\n".join(lines) + "\n").encode("utf-8")
    starter = (
        "# Şahit CLI başlangıç istemi\n\n"
        "Aşağıdaki metni, yerel Copilot CLI etkileşimli oturumuna kullanıcı olarak ver. "
        "Dosya-bağlama sözdizimini kurulu sürümün help'i doğrulamıyorsa kullanma; "
        "gerekirse dosya içeriğini kullanıcı kendisi yapıştırır.\n\n"
        "## İstem\n\n"
        + source["startup_prompt"]
        + "\n"
    ).encode("utf-8")
    return {
        "handoff.txt": text_bytes,
        "handoff.html": html_bytes,
        "handoff.json": json_bytes,
        "START_HERE.md": starter,
    }


def repository_source_hashes(source):
    hashes = {}
    for relative in source["verified_repository"]["manifested_repository_files"]:
        candidate = ROOT / relative
        if candidate.is_symlink():
            raise ValueError(f"Repository source cannot be a symlink: {relative}")
        path = candidate.resolve(strict=True)
        try:
            path.relative_to(ROOT)
        except ValueError:
            raise ValueError(f"Repository source escapes root: {relative}") from None
        if not path.is_file():
            raise ValueError(f"Expected repository source file: {relative}")
        hashes[relative] = sha256(path.read_bytes())
    return hashes


def expected_outputs():
    source_path = HERE / "source.json"
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes.decode("utf-8"))
    generated = generated_files(source)
    manifest = {
        "schema_version": 1,
        "source_file": "source.json",
        "source_sha256": sha256(source_bytes),
        "source_snapshot_commit": source["source_snapshot_commit"],
        "main_snapshot_commit": source["main_snapshot_commit"],
        "repo_sources_sha256": repository_source_hashes(source),
        "outputs_sha256": {name: sha256(data) for name, data in generated.items()},
        "manifest_self_hash": "omitted: self-referential hash is not meaningful",
        "privacy_boundary": source["scope"]["privacy_boundary"],
        "scan_limit": "Hashes and pattern scans do not prove truth, authorship, or absence of every secret or personal datum.",
    }
    generated["manifest.json"] = stable_json(manifest)
    return generated


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify checked-in outputs without writing")
    args = parser.parse_args(argv)
    outputs = expected_outputs()
    mismatches = []
    for name, expected in outputs.items():
        path = HERE / name
        if args.check:
            if not path.is_file() or path.read_bytes() != expected:
                mismatches.append(name)
        else:
            path.write_bytes(expected)
            print(f"generated {path.relative_to(ROOT)}")
    if mismatches:
        parser.exit(1, "Generated files differ: " + ", ".join(mismatches) + "\n")
    if args.check:
        print(f"OK: {len(outputs)} generated files match source.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
