#!/usr/bin/env python3
"""Generate the offline handoff files from source.json using only the standard library."""
import argparse
import hashlib
import html
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUTS = ("handoff.txt", "handoff.html", "handoff.json", "START_HERE.md")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def stable_json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def validate(value, schema, path="$"):
    """JSON Schema alt kümesi (type, const, enum, required, properties, additionalProperties, items, minItems, minLength, minimum, pattern); yalnız stdlib."""
    kinds = {"object": dict, "array": list, "string": str, "boolean": bool, "integer": int}
    kind = schema.get("type")
    if kind and (not isinstance(value, kinds[kind]) or (kind == "integer" and isinstance(value, bool))):
        return [f"{path}: expected {kind}"]
    errors = []
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in {schema['enum']}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: does not match {schema['pattern']}")
    if isinstance(value, int) and not isinstance(value, bool) and value < schema.get("minimum", value):
        errors.append(f"{path}: below {schema['minimum']}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than {schema['minItems']} items")
        for index, item in enumerate(value):
            errors += validate(item, schema.get("items", {}), f"{path}[{index}]")
    if isinstance(value, dict):
        errors += [f"{path}: missing {key}" for key in schema.get("required", []) if key not in value]
        properties = schema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                errors += validate(item, properties[key], f"{path}.{key}")
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: unexpected {key}")
    return errors


def load_schema(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


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


def read_lf(path):
    """Satır sonları LF'ye çevrilerek okunur; autocrlf açık bir checkout'ta hash'ler değişmesin."""
    return Path(path).read_bytes().replace(b"\r\n", b"\n")


def file_hashes(relatives, strict=True):
    hashes = {}
    for relative in relatives:
        candidate = ROOT / relative
        if candidate.is_symlink():
            raise ValueError(f"Repository source cannot be a symlink: {relative}")
        if not strict and not candidate.is_file():
            hashes[relative] = None
            continue
        path = candidate.resolve(strict=True)
        try:
            path.relative_to(ROOT)
        except ValueError:
            raise ValueError(f"Repository source escapes root: {relative}") from None
        if not path.is_file():
            raise ValueError(f"Expected repository source file: {relative}")
        hashes[relative] = sha256(read_lf(path))
    return hashes


def expected_outputs(refresh_observed=False):
    """pinned: pakete ait, sıkı denetlenen dosyalar. observed: yalnız gözlenen, anlık görüntü hash'i; sapma bilgidir (--drift)."""
    source_bytes = (HERE / "source.json").read_bytes()
    source = json.loads(source_bytes.decode("utf-8"))
    problems = validate(source, load_schema("handoff.schema.json"))
    if problems:
        raise ValueError("source.json violates handoff.schema.json: " + "; ".join(problems))
    generated = generated_files(source)
    repository = source["verified_repository"]
    pinned = file_hashes(repository["pinned_repository_files"])
    manifest_path = HERE / "manifest.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")).get("observed_sources_sha256", {}) if manifest_path.is_file() else {}
    if refresh_observed or set(previous) != set(repository["observed_repository_files"]):
        observed = file_hashes(repository["observed_repository_files"])
    else:
        observed = previous
    outputs = {name: sha256(data) for name, data in generated.items()}
    source_sha256 = sha256(source_bytes)
    manifest = {
        "schema_version": 2,
        "bundle_version": source["bundle_version"],
        "prepared_on": source["prepared_on"],
        "source_file": "source.json",
        "source_sha256": source_sha256,
        "source_snapshot_commit": source["source_snapshot_commit"],
        "main_snapshot_commit": source["main_snapshot_commit"],
        "outputs_sha256": outputs,
        "pinned_sources_sha256": pinned,
        "observed_sources_sha256": observed,
        "bundle_sha256": sha256(stable_json({"source": source_sha256, "outputs": outputs, "pinned": pinned})),
        "manifest_self_hash": "omitted: self-referential hash is not meaningful",
        "line_endings": "hashes are computed over LF-normalized bytes",
        "privacy_boundary": source["scope"]["privacy_boundary"],
        "scan_limit": "Hashes and pattern scans do not prove truth, authorship, or absence of every secret or personal datum.",
    }
    problems = validate(manifest, load_schema("manifest.schema.json"))
    if problems:
        raise ValueError("manifest violates manifest.schema.json: " + "; ".join(problems))
    generated["manifest.json"] = stable_json(manifest)
    return generated


def drift():
    observed = json.loads((HERE / "manifest.json").read_text(encoding="utf-8"))["observed_sources_sha256"]
    current = file_hashes(observed, strict=False)
    return {name: ("missing" if current[name] is None else "changed") for name, digest in observed.items() if current[name] != digest}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify checked-in outputs, schemas and pinned files without writing")
    mode.add_argument("--drift", action="store_true", help="informational: list observed files that differ from the manifest snapshot")
    args = parser.parse_args(argv)
    if args.drift:
        changed = drift()
        for name, state in changed.items():
            print(f"DRIFT {state}: {name}")
        print(f"{len(changed)} observed file(s) differ from the snapshot (informational; not an integrity failure)")
        return 0
    outputs = expected_outputs(refresh_observed=not args.check)
    mismatches = []
    for name, expected in outputs.items():
        path = HERE / name
        if args.check:
            if not path.is_file() or read_lf(path) != expected:
                mismatches.append(name)
        else:
            path.write_bytes(expected)
            print(f"generated {path.relative_to(ROOT)}")
    if mismatches:
        parser.exit(1, "Generated files differ: " + ", ".join(mismatches) + "\n")
    if args.check:
        bundle = json.loads(outputs["manifest.json"].decode("utf-8"))["bundle_sha256"]
        print(f"OK: {len(outputs)} generated files match source.json; bundle_sha256 {bundle[:12]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
