"""Offline cross-witness report rendering with source linkage and HTML escaping."""

import html
import json
import re
from pathlib import Path

from .core import GovernanceError, pretty_json, validate_bundle


REDACTIONS = (
    (re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"), "[REDACTED:TOKEN]"),
    (re.compile(r"\b(?:sk-ant-|sk-|sess-|AIza|gh[pousr]_|glpat-)[A-Za-z0-9_-]{8,}", re.I), "[REDACTED:TOKEN]"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{8,}"), "[REDACTED:BEARER]"),
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----.*?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", re.S), "[REDACTED:PRIVATE-KEY]"),
    (re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token)\s*[:=]\s*\S+"), "[REDACTED:CREDENTIAL-FIELD]"),
    (re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"), "[REDACTED:IP]"),
    (re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I), "[REDACTED:IDENTIFIER]"),
)


def redact_text(text):
    if not isinstance(text, str):
        raise GovernanceError("witness claims must be text")
    value = text
    for pattern, replacement in REDACTIONS:
        value = pattern.sub(replacement, value)
    # A second pass is a fail-closed guard against a malformed redaction result.
    if any(pattern.search(value) for pattern, _ in REDACTIONS):
        raise GovernanceError("public-output secret scan failed; raw content was not published")
    return value


def _validate_claims(claims, source_ids):
    required = {"evidence", "interpretations", "recommendations", "user_approvals", "actions_taken", "uncertainties"}
    if not isinstance(claims, dict) or set(claims) != required:
        raise GovernanceError("witness claims must contain the six required categories")
    sanitized = {}
    for category, values in claims.items():
        if not isinstance(values, list):
            raise GovernanceError(f"witness {category} must be a list")
        sanitized[category] = []
        for item in values:
            if not isinstance(item, dict) or set(item) != {"text", "source_ids"}:
                raise GovernanceError(f"each {category} item needs text and source_ids")
            refs = item["source_ids"]
            if (not isinstance(refs, list) or not refs
                    or any(not isinstance(ref, str) or ref not in source_ids for ref in refs)):
                raise GovernanceError(f"{category} references an unknown source ID")
            sanitized[category].append({
                "text": redact_text(item["text"]),
                "source_ids": sorted(set(refs)),
            })
    return sanitized


def build_witness_report(bundle, witnesses):
    validate_bundle(bundle)
    manifest = bundle.get("manifest", {})
    context_hash = manifest.get("context_hash")
    if not context_hash or not isinstance(witnesses, list) or len(witnesses) < 2:
        raise GovernanceError("two or more independent witness imports are required")
    sources = manifest.get("sources")
    if not isinstance(sources, list):
        raise GovernanceError("compiled manifest has no source catalog")
    source_ids = {source["id"] for source in sources}
    checked = []
    for witness in witnesses:
        if not isinstance(witness, dict) or set(witness) != {
            "witness_id", "kind", "context_hash", "source_ids", "claims"
        }:
            raise GovernanceError("invalid witness import")
        if witness["kind"] not in ("fixture", "imported"):
            raise GovernanceError("witness kind must be fixture or imported")
        if witness["context_hash"] != context_hash:
            raise GovernanceError("witness context_hash does not match compiled task")
        refs = witness["source_ids"]
        if (not isinstance(refs, list) or not refs
                or any(not isinstance(ref, str) or ref not in source_ids for ref in refs)):
            raise GovernanceError("witness must reference known compiled source IDs")
        checked.append({
            "witness_id": redact_text(str(witness["witness_id"])),
            "kind": witness["kind"],
            "context_hash": context_hash,
            "source_ids": sorted(set(refs)),
            "claims": _validate_claims(witness["claims"], source_ids),
        })

    if len({w["witness_id"] for w in checked}) != len(checked):
        raise GovernanceError("witness_id values must be distinct")

    def claim_keys(category):
        return [
            {(item["text"], tuple(item["source_ids"])) for item in witness["claims"][category]}
            for witness in checked
        ]

    def render_claims(values):
        return [{"text": text, "source_ids": list(refs)} for text, refs in sorted(values)]

    evidence_sets = claim_keys("evidence")
    recommendation_sets = claim_keys("recommendations")
    evidence_common = set.intersection(*evidence_sets) if evidence_sets else set()
    recommendation_common = set.intersection(*recommendation_sets) if recommendation_sets else set()
    report = {
        "schema_version": 1,
        "context_hash": context_hash,
        "source_ids": sorted(source_ids),
        "source_hashes": {source["id"]: source["sha256"] for source in sources},
        "witnesses": checked,
        "comparison": {
            "evidence_overlap": render_claims(evidence_common),
            "evidence_disagreement": [
                {"witness_id": witness["witness_id"], "claims": render_claims(values - evidence_common)}
                for witness, values in zip(checked, evidence_sets)
            ],
            "recommendation_overlap": render_claims(recommendation_common),
            "recommendation_options": [
                {"witness_id": witness["witness_id"], "claims": render_claims(values - recommendation_common)}
                for witness, values in zip(checked, recommendation_sets)
            ],
            "epistemic_note": "Overlap or disagreement is a comparison result, not proof of factual correctness. Unsupported claims remain uncertainties.",
        },
        "fixtures_only": all(w["kind"] == "fixture" for w in checked),
        "notice": "Imported/fixture statements are not model verification. No hidden provider prompts or reasoning traces are collected.",
    }
    return report


def render_txt(report):
    lines = [
        "ORTAK KÖPRÜ — ÇAPRAZ ŞAHİTLİK RAPORU",
        f"Context hash: {report['context_hash']}",
        f"Fixture-only: {str(report['fixtures_only']).lower()}",
        "Source IDs: " + ", ".join(report["source_ids"]),
        "",
    ]
    for witness in report["witnesses"]:
        lines.extend([
            f"Şahit: {witness['witness_id']} ({witness['kind']})",
            "Kaynaklar: " + ", ".join(witness["source_ids"]),
        ])
        for category, values in witness["claims"].items():
            lines.append(f"{category}:")
            lines.extend(f"- {item['text']} [sources: {', '.join(item['source_ids'])}]" for item in values)
        lines.append("")
    lines.extend([
        "Karşılaştırma:",
        f"Evidence overlap: {report['comparison']['evidence_overlap']}",
        f"Evidence disagreement: {report['comparison']['evidence_disagreement']}",
        f"Recommendation overlap: {report['comparison']['recommendation_overlap']}",
        f"Options: {report['comparison']['recommendation_options']}",
        report["comparison"]["epistemic_note"],
        report["notice"],
    ])
    return "\n".join(lines) + "\n"


def render_html(report):
    esc = html.escape
    sections = []
    for witness in report["witnesses"]:
        sections.append(f"<section><h2>{esc(witness['witness_id'])} ({esc(witness['kind'])})</h2>")
        sections.append(f"<p>Source IDs: {esc(', '.join(witness['source_ids']))}</p>")
        for category, values in witness["claims"].items():
            sections.append(f"<h3>{esc(category.replace('_', ' ').title())}</h3><ul>")
            for item in values:
                refs = ", ".join(item["source_ids"])
                sections.append(f"<li>{esc(item['text'])} <small>[sources: {esc(refs)}]</small></li>")
            sections.append("</ul>")
        sections.append("</section>")
    sources = "".join(
        f"<li>{esc(source_id)}: <code>{esc(digest)}</code></li>"
        for source_id, digest in report["source_hashes"].items()
    )
    return (
        "<!doctype html>\n<html lang=\"tr\"><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>Çapraz şahitlik raporu</title>"
        "<body><main><h1>Çapraz şahitlik raporu</h1>"
        f"<p>Context hash: <code>{esc(report['context_hash'])}</code></p>"
        f"<p>Fixture-only: {str(report['fixtures_only']).lower()}</p>"
        f"<h2>Sources</h2><ul>{sources}</ul>{''.join(sections)}"
        "<h2>Comparison</h2>"
        f"<pre>{esc(json.dumps(report['comparison'], ensure_ascii=False, indent=2))}</pre>"
        f"<p>{esc(report['notice'])}</p>"
        f"<p>{esc(report['comparison']['epistemic_note'])}</p>"
        "</main></body></html>\n"
    )


def write_formats(report, output_prefix):
    prefix = Path(output_prefix)
    paths = {
        "txt": prefix.with_suffix(".txt"),
        "html": prefix.with_suffix(".html"),
        "json": prefix.with_suffix(".json"),
    }
    contents = {
        "txt": render_txt(report).encode("utf-8"),
        "html": render_html(report).encode("utf-8"),
        "json": pretty_json(report),
    }
    for extension, content in contents.items():
        paths[extension].parent.mkdir(parents=True, exist_ok=True)
        with paths[extension].open("xb") as stream:
            stream.write(content)
    return paths
