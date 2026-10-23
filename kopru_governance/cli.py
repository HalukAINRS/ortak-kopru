"""Local CLI for compiling, verifying and rendering governed-run artifacts."""

import argparse
import json
import sys
from pathlib import Path

from .core import GovernanceError, _parse_json, compile_context, pretty_json, validate_bundle
from .runs import public_metadata, verify_run, write_private_artifact
from .witness import build_witness_report, write_formats


def _load_json(path):
    try:
        return _parse_json(Path(path).read_text(encoding="utf-8"), str(path))
    except (OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise GovernanceError(f"cannot read JSON input: {path}") from exc


def _compile(args):
    task = args.task
    if args.task_file:
        if task is not None:
            raise GovernanceError("use either --task or --task-file")
        relative = Path(args.task_file).as_posix()
        task_source_path = relative
    else:
        task_source_path = None
    if task is None and task_source_path is None:
        raise GovernanceError("a user task is required")
    request = _load_json(args.request) if args.request else {}
    result = compile_context(
        args.root, task, request, args.policy, task_source_path=task_source_path,
    )
    if args.output:
        write_private_artifact(args.root, args.output, result["bundle_bytes"])
    print(json.dumps({
        "context_hash": result["bundle"]["manifest"]["context_hash"],
        "policy_sha256": result["policy_hash"],
        "source_hashes": result["source_hashes"],
        "bundle_sha256": result["compile_hash"],
        "output": args.output or "stdout",
        "visibility": result["bundle"]["manifest"]["visibility"],
    }, ensure_ascii=False, indent=2))
    if not args.quiet:
        for message in result["bundle"]["messages"]:
            print(f"\n--- EXACT MESSAGE ROLE: {message['role']} ---\n{message['content']}")


def _approval_template(args):
    bundle = _load_json(args.bundle)
    validate_bundle(bundle)
    manifest = bundle.get("manifest", {})
    scopes = {
        "policy_sha256": manifest.get("policy_sha256"),
        "context_hash": manifest.get("context_hash"),
        "source_hashes": {s["path"]: s["sha256"] for s in manifest.get("sources", [])},
    }
    template = {
        "granted": False,
        "approved_by": "",
        "operation": "provider_call",
        "scope": scopes,
        "expires_at": "",
    }
    write_private_artifact(args.root, args.output, pretty_json(template))
    print("Approval template created with granted=false; inspect messages and explicitly edit locally.")


def _verify(args):
    print(json.dumps(verify_run(args.ledger), ensure_ascii=False, indent=2))


def _export(args):
    metadata = public_metadata(args.ledger)
    raw = pretty_json(metadata)
    # The public view is an allowlist of metadata; still scan before writing it.
    from .witness import redact_text
    if redact_text(raw.decode("utf-8")) != raw.decode("utf-8"):
        raise GovernanceError("redaction required; public export blocked")
    with Path(args.output).open("xb") as stream:
        stream.write(raw)
    print(f"Redacted metadata written: {args.output}")


def _witness(args):
    bundle = _load_json(args.bundle)
    witnesses = [_load_json(path) for path in args.witness]
    report = build_witness_report(bundle, witnesses)
    paths = write_formats(report, args.output_prefix)
    print(json.dumps({key: str(value) for key, value in paths.items()}, ensure_ascii=False, indent=2))


def _demo(args):
    bundle = _load_json(args.bundle)
    source_ids = [source["id"] for source in bundle["manifest"]["sources"]]
    ref = source_ids[0]
    context_hash = bundle["manifest"]["context_hash"]
    claims_a = {
        "evidence": [{"text": "Fixture: source is present in the compiled snapshot.", "source_ids": [ref]}],
        "interpretations": [{"text": "Fixture interpretation only.", "source_ids": [ref]}],
        "recommendations": [{"text": "Option A: review offline; no provider call.", "source_ids": [ref]}],
        "user_approvals": [],
        "actions_taken": [{"text": "No action taken; illustrative fixture.", "source_ids": [ref]}],
        "uncertainties": [{"text": "This fixture cannot establish model or provider behavior.", "source_ids": [ref]}],
    }
    claims_b = {
        "evidence": [{"text": "Fixture: source is present in the compiled snapshot.", "source_ids": [ref]}],
        "interpretations": [{"text": "A second fixture interpretation.", "source_ids": [ref]}],
        "recommendations": [{"text": "Option B: inspect provider limits before any call.", "source_ids": [ref]}],
        "user_approvals": [],
        "actions_taken": [{"text": "No action taken; illustrative fixture.", "source_ids": [ref]}],
        "uncertainties": [{"text": "Agreement does not establish factual correctness.", "source_ids": [ref]}],
    }
    report = build_witness_report(bundle, [
        {"witness_id": "offline-fixture-A", "kind": "fixture", "context_hash": context_hash,
         "source_ids": [ref], "claims": claims_a},
        {"witness_id": "offline-fixture-B", "kind": "fixture", "context_hash": context_hash,
         "source_ids": [ref], "claims": claims_b},
    ])
    paths = write_formats(report, args.output_prefix)
    print("Fixture-only report (no live models called):")
    print(json.dumps({key: str(value) for key, value in paths.items()}, ensure_ascii=False, indent=2))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Ortak Köprü governed-path offline tools")
    sub = parser.add_subparsers(dest="command", required=True)
    compile_parser = sub.add_parser("compile", help="compile and print exact messages; performs no calls")
    compile_parser.add_argument("--root", default=".")
    compile_parser.add_argument("--policy", default="policy/policy.json")
    group = compile_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--task")
    group.add_argument("--task-file")
    compile_parser.add_argument("--request", help="JSON request metadata file")
    compile_parser.add_argument("--output", help="write compiled bundle")
    compile_parser.add_argument("--quiet", action="store_true", help="do not print exact messages")
    compile_parser.set_defaults(func=_compile)

    approval_parser = sub.add_parser("approval-template", help="create an unapproved scoped template")
    approval_parser.add_argument("--bundle", required=True)
    approval_parser.add_argument("--root", default=".")
    approval_parser.add_argument("--output", required=True)
    approval_parser.set_defaults(func=_approval_template)

    verify_parser = sub.add_parser("verify-run", help="verify a local JSONL run hash chain")
    verify_parser.add_argument("ledger")
    verify_parser.set_defaults(func=_verify)

    export_parser = sub.add_parser("export-run", help="export allowlisted redacted metadata only")
    export_parser.add_argument("ledger")
    export_parser.add_argument("--output", required=True)
    export_parser.set_defaults(func=_export)

    witness_parser = sub.add_parser("witness", help="render imported offline witness JSON as TXT/HTML/JSON")
    witness_parser.add_argument("--bundle", required=True)
    witness_parser.add_argument("--witness", action="append", required=True)
    witness_parser.add_argument("--output-prefix", required=True)
    witness_parser.set_defaults(func=_witness)

    demo_parser = sub.add_parser("witness-demo", help="render a clearly marked fixture-only report")
    demo_parser.add_argument("--bundle", required=True)
    demo_parser.add_argument("--output-prefix", required=True)
    demo_parser.set_defaults(func=_demo)

    args = parser.parse_args(argv)
    try:
        args.func(args)
    except (GovernanceError, OSError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
