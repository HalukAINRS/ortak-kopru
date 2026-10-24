import argparse
import json
import sys
from pathlib import Path

from .context import (
    ContextError,
    UNKNOWN_LAYERS,
    compile_context,
    create_approval,
    load_json,
    validate_policy,
    verify_approval,
    verify_compiled,
)
from .reports import build_witness_report, write_witness_report
from .runs import _write_exclusive, verify_runs


def _default_private(root):
    root = Path(root).resolve()
    runs = root / "runs"
    private = runs / "private"
    if runs.is_symlink() or private.is_symlink():
        raise ContextError("Private run directory cannot be a symlink")
    private.mkdir(parents=True, exist_ok=True)
    try:
        private.resolve(strict=True).relative_to(root)
    except (OSError, ValueError):
        raise ContextError("Private run directory must stay inside repository root") from None
    return private


def _private_child(root, name):
    private = _default_private(root)
    child = private / name
    if child.is_symlink():
        raise ContextError(f"Private {name} directory cannot be a symlink")
    child.mkdir(parents=True, exist_ok=True)
    try:
        child.resolve(strict=True).relative_to(private.resolve(strict=True))
    except (OSError, ValueError):
        raise ContextError(f"Private {name} directory must stay inside local run storage") from None
    return child


def main(argv=None):
    parser = argparse.ArgumentParser(description="Offline transparent context and run-record tools.")
    commands = parser.add_subparsers(dest="command", required=True)

    compile_parser = commands.add_parser("compile", help="compile and print exact application messages")
    compile_parser.add_argument("--root", default=".")
    compile_parser.add_argument("--policy", default="policy/policy.json")
    compile_parser.add_argument("--task-file", required=True)
    compile_parser.add_argument("--strict", action="store_true")

    approve_parser = commands.add_parser("approve", help="create a scoped local approval after review")
    approve_parser.add_argument("--root", default=".")
    approve_parser.add_argument("--policy", default="policy/policy.json")
    approve_parser.add_argument("--artifact", required=True)
    approve_parser.add_argument("--expires", required=True)
    approve_parser.add_argument("--confirm-reviewed", action="store_true")

    verify_parser = commands.add_parser("verify", help="verify a compiled context and optional approval")
    verify_parser.add_argument("--root", default=".")
    verify_parser.add_argument("--policy", default="policy/policy.json")
    verify_parser.add_argument("--artifact", required=True)
    verify_parser.add_argument("--approval")

    runs_parser = commands.add_parser("verify-runs", help="verify public run event chains")
    runs_parser.add_argument("--runs", default="runs")

    witness_parser = commands.add_parser("witness", help="render offline cross-witness TXT/HTML/JSON")
    witness_parser.add_argument("--artifact", required=True)
    witness_parser.add_argument("--input", required=True, help="JSON containing imported witness outputs")
    witness_parser.add_argument("--output", required=True, help="output base path without extension")
    witness_parser.add_argument("--example", action="store_true")

    args = parser.parse_args(argv)
    try:
        if args.command == "compile":
            root = Path(args.root).resolve()
            task_path = (root / args.task_file).resolve(strict=True)
            task_path.relative_to(root)
            task = task_path.read_text(encoding="utf-8")
            compiled, data, policy = compile_context(
                root, root / args.policy, task, task_path.relative_to(root).as_posix(), task_is_file=True
            )
            if args.strict and (set(UNKNOWN_LAYERS) - set(policy["layers"]["accepted_unknown"])):
                raise ContextError("Strict compilation refuses unknown provider layers")
            output = _private_child(root, "prepared") / f"{compiled['context_sha256']}.json"
            if output.is_symlink():
                raise ContextError("Prepared artifact path cannot be a symlink")
            if output.exists():
                if output.read_bytes() != data:
                    raise ContextError("Existing prepared artifact differs; refusing to overwrite")
            else:
                try:
                    _write_exclusive(output, data)
                except OSError:
                    if output.is_symlink() or not output.is_file() or output.read_bytes() != data:
                        raise ContextError("Could not safely create prepared artifact") from None
            print(f"Compiled SHA-256: {compiled['context_sha256']}")
            print(f"Artifact (local only): {output}")
            print("Exact messages to be sent:")
            print(json.dumps(compiled["messages"], ensure_ascii=False, indent=2))
            print("Layer visibility:", compiled["layers"]["visibility"])
            print(compiled["layers"]["warning"])
            return 0
        if args.command == "approve":
            if not args.confirm_reviewed:
                raise ContextError("Pass --confirm-reviewed only after inspecting the exact messages")
            root = Path(args.root).resolve()
            policy_path = Path(args.policy)
            if not policy_path.is_absolute():
                policy_path = root / policy_path
            compiled = load_json(args.artifact)
            policy = validate_policy(load_json(policy_path))
            destination = _private_child(root, "approvals") / f"{verify_compiled(compiled)}.json"
            approval = create_approval(compiled, policy, policy_path, args.expires, destination, root)
            print(f"Local approval created: {destination}")
            print("This local file is not a verified user identity or cryptographic signature.")
            print(approval["context_sha256"])
            return 0
        if args.command == "verify":
            root = Path(args.root).resolve()
            policy_path = Path(args.policy)
            if not policy_path.is_absolute():
                policy_path = root / policy_path
            compiled = load_json(args.artifact)
            digest = verify_compiled(compiled)
            policy = validate_policy(load_json(policy_path))
            if args.approval:
                verify_approval(compiled, policy, policy_path, args.approval, root)
            print(f"OK context {digest}")
            return 0
        if args.command == "verify-runs":
            errors = verify_runs(args.runs)
            print("\n".join(errors) if errors else "OK: run event chains verified")
            return 1 if errors else 0
        if args.command == "witness":
            compiled = load_json(args.artifact)
            data = load_json(args.input)
            report = build_witness_report(compiled, data.get("witnesses", []), args.example)
            paths = write_witness_report(report, args.output)
            print("\n".join(str(path) for path in paths))
            return 0
    except (ContextError, OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
