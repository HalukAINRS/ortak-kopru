#!/usr/bin/env python3
"""Validate only repository-visible policy, integrity and provenance facts."""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from kopru_governance.core import GovernanceError, compile_context, load_policy, validate_approval  # noqa: E402
from kopru_governance.runs import (  # noqa: E402
    append_event,
    create_run,
    public_metadata,
    verify_run,
    write_private_output,
)


def check(root):
    failures = []
    policy, _, _ = load_policy(root)
    for schema_name in (
        "policy.schema.json", "approval.schema.json", "manifest.schema.json", "run-event.schema.json"
    ):
        try:
            json.loads((root / "policy" / schema_name).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError, UnicodeDecodeError):
            failures.append(f"invalid or missing policy contract: {schema_name}")
    if policy["limits"]["max_calls"] != 1 or policy["limits"]["max_turns"] < 1:
        failures.append("provider call/turn budget is invalid")
    task = "Offline lint fixture. No model is invoked."
    first = compile_context(root, task, {"provider": "offline-fixture"})
    second = compile_context(root, task, {"provider": "offline-fixture"})
    if first["compile_hash"] != second["compile_hash"] or first["bundle_bytes"] != second["bundle_bytes"]:
        failures.append("context compilation is not reproducible")
    roles = {source["role"] for source in first["bundle"]["manifest"]["sources"]}
    if not {"untrusted_evidence", "user_task"}.issubset(roles):
        failures.append("source trust roles are missing from manifest")
    if not first["bundle"]["manifest"]["visibility"]["layers"]["provider_system_and_safety"] == "unknown":
        failures.append("provider visibility is overstated")
    source_hashes = first["source_hashes"]
    if any(len(digest) != 64 for digest in source_hashes.values()):
        failures.append("manifest contains an invalid source hash")
    try:
        validate_approval(root, "missing-approval.json", first, "provider_call")
        failures.append("missing scoped approval was accepted")
    except (GovernanceError, OSError):
        pass

    # Fake private output verifies the public exporter is an allowlist, not a raw-log copier.
    with tempfile.TemporaryDirectory() as temporary:
        fake_run_id, fake_ledger, private_root = create_run(Path(temporary) / "runs", first["bundle"])
        append_event(fake_ledger, "attempted", {"operation": "offline-fixture"})
        write_private_output(private_root, fake_run_id, "access_token=fixture-not-a-real-credential")
        append_event(fake_ledger, "succeeded", {"output_sha256": "0" * 64})
        if "fixture-not-a-real-credential" in json.dumps(public_metadata(fake_ledger)):
            failures.append("public metadata includes private provider output")

    ignore_probe = "runs/private/secret-probe.json"
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "check-ignore", "-q", ignore_probe],
            capture_output=True, timeout=5,
        )
        ignored = result.returncode == 0
    except (OSError, subprocess.SubprocessError):
        ignored = "/runs/" in (root / ".gitignore").read_text(encoding="utf-8")
    if not ignored:
        failures.append("runs/ private data is not ignored")

    runs_dir = root / "runs"
    if runs_dir.is_dir():
        for ledger in runs_dir.glob("*.jsonl"):
            try:
                verify_run(ledger)
            except (GovernanceError, OSError) as exc:
                failures.append(f"invalid run ledger {ledger.name}: {exc}")
    return failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    failures = check(args.root.resolve())
    if failures:
        for failure in failures:
            print("FAIL:", failure, file=sys.stderr)
        return 1
    print("steering-lint: policy, source roles, repeatability, visibility, budgets and local-ledger checks passed")
    print("This checks repository-visible configuration/integrity only; it does not detect hidden steering.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
