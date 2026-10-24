import html
import json
from pathlib import Path

from .context import ContextError, canonical_bytes, verify_compiled
from .runs import contains_secret


def build_witness_report(compiled, witnesses, example=False):
    context_id = verify_compiled(compiled)
    source_ids = {item["sha256"] for item in compiled["sources"]}
    normalized = []
    for witness in witnesses:
        if not isinstance(witness, dict):
            raise ContextError("Each imported witness must be a JSON object")
        if contains_secret(witness):
            raise ContextError("Witness output failed secret-pattern screening; report was not published")
        refs = witness.get("source_ids", [])
        if not isinstance(refs, list) or not all(isinstance(item, str) for item in refs) or not set(refs).issubset(source_ids):
            raise ContextError("Witness source IDs must refer to the compiled context")
        categories = ("claims", "interpretations", "recommendations", "user_approvals", "actions", "uncertainties")
        if any(key in witness and not isinstance(witness[key], list) for key in categories):
            raise ContextError("Witness classifications must be arrays")
        normalized.append(
            {
                "provider": str(witness.get("provider", "unknown")),
                "model": str(witness.get("model", "unknown")),
                "provenance": "user-imported; independent provider execution is not verified",
                "source_ids": sorted(set(refs)),
                "output": str(witness.get("output", "")),
                "classification": {
                    key: list(witness.get(key, []))
                    for key in categories
                },
            }
        )
    comparisons = []
    for left in range(len(normalized)):
        for right in range(left + 1, len(normalized)):
            comparisons.append(
                {
                    "left": left,
                    "right": right,
                    "exact_text_match": normalized[left]["output"] == normalized[right]["output"],
                    "shared_source_ids": sorted(
                        set(normalized[left]["source_ids"]) & set(normalized[right]["source_ids"])
                    ),
                    "epistemic_accuracy": "not_assessed",
                }
            )
    report = {
        "schema_version": 1,
        "example": bool(example),
        "context_sha256": context_id,
        "source_ids": sorted(source_ids),
        "witnesses": normalized,
        "comparison": {
            "pairwise": comparisons,
            "caveat": "Textual agreement or disagreement is not evidence of correctness.",
        },
    }
    return report


def write_witness_report(report, output_base):
    output_base = Path(output_base)
    output_base.parent.mkdir(parents=True, exist_ok=True)
    json_path = output_base.with_suffix(".json")
    txt_path = output_base.with_suffix(".txt")
    html_path = output_base.with_suffix(".html")
    json_path.write_bytes(canonical_bytes(report))
    lines = [
        "Ortak Köprü — offline cross-witness report",
        f"Example fixture: {'yes' if report['example'] else 'no'}",
        f"Context SHA-256: {report['context_sha256']}",
        "Source IDs: " + ", ".join(report["source_ids"]),
        report["comparison"]["caveat"],
    ]
    for pair in report["comparison"]["pairwise"]:
        lines.append(
            f"Comparison {pair['left'] + 1}/{pair['right'] + 1}: "
            f"exact_text_match={pair['exact_text_match']}; epistemic_accuracy=not_assessed"
        )
    for index, witness in enumerate(report["witnesses"], 1):
        lines.extend(
            [
                "",
                f"Witness {index}: {witness['provider']} / {witness['model']}",
                "Sources: " + ", ".join(witness["source_ids"]),
                "Output: " + witness["output"],
            ]
        )
        for category, values in witness["classification"].items():
            lines.append(f"{category}: " + " | ".join(map(str, values)))
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    escaped = html.escape("\n".join(lines))
    html_path.write_text(
        "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><title>Cross-witness report</title>"
        f"<main><pre>{escaped}</pre></main></html>\n",
        encoding="utf-8",
        newline="\n",
    )
    return json_path, txt_path, html_path
