#!/usr/bin/env python3
"""Validate configured provenance/integrity contracts; does not detect hidden steering."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ortak_kopru.context import ContextError, compile_context, load_json, validate_policy  # noqa: E402
from ortak_kopru.runs import verify_runs  # noqa: E402


def main():
    root = Path(__file__).resolve().parents[1]
    try:
        policy_path = root / "policy" / "policy.json"
        policy = validate_policy(load_json(policy_path))
        artifact, _, _ = compile_context(root, policy_path, "Offline policy/manifest contract check.")
        errors = verify_runs(root / "runs")
        if errors:
            print("\n".join(errors), file=sys.stderr)
            return 1
        print(
            json.dumps(
                {
                    "result": "ok",
                    "policy_sha256": artifact["policy_sha256"],
                    "context_sha256": artifact["context_sha256"],
                    "source_count": len(artifact["sources"]),
                    "network_allowed": policy["permissions"]["allow_network"],
                    "hidden_steering_detection": False,
                },
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 0
    except (ContextError, OSError, UnicodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
