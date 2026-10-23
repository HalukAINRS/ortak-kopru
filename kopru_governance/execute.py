"""Fail-closed single-call coordinator. The provider adapter is injected for tests."""

import re

from .core import GovernanceError, validate_approval, validate_compiled, verify_current_snapshot
from .runs import append_event, create_run, write_private_output


def execute_once(root, compiled, approval_path, runs_dir, provider_call, provider_preflight=None):
    """Perform at most one approved call; never retry after a possibly billable attempt."""
    from pathlib import Path

    root = Path(root).resolve(strict=True)
    runs_dir = Path(runs_dir)
    if not runs_dir.is_absolute():
        runs_dir = root / runs_dir
    runs_root = root / "runs"
    if runs_root.is_symlink() or runs_dir.resolve() != runs_root.resolve():
        raise GovernanceError("run ledger path must be the repository's non-symlink runs/ directory")
    validate_compiled(compiled)
    run_id, ledger, private_root = create_run(runs_dir, compiled["bundle"])
    try:
        verify_current_snapshot(root, compiled)
    except (OSError, GovernanceError):
        append_event(ledger, "skipped", {"reason": "source_snapshot_changed"})
        return {"run_id": run_id, "status": "skipped", "ledger": str(ledger)}
    policy = compiled["policy"]
    request = compiled["bundle"]["manifest"]["request"]
    provider = request.get("provider")
    model = request.get("model")
    limits = policy["limits"]
    if "provider_call" not in policy["approval_required"]:
        append_event(ledger, "skipped", {"reason": "required_approval_policy_missing"})
        return {"run_id": run_id, "status": "skipped", "ledger": str(ledger)}
    allowed = any(
        entry["provider"] == provider and entry["model"] == model
        for entry in policy["allowed_providers"]
    )
    if not policy["permissions"]["network"] or not allowed:
        append_event(ledger, "skipped", {"reason": "network_or_provider_not_allowed"})
        return {"run_id": run_id, "status": "skipped", "ledger": str(ledger)}
    if limits["max_calls"] < 1 or limits["max_turns"] < 1:
        append_event(ledger, "skipped", {"reason": "budget_exhausted"})
        return {"run_id": run_id, "status": "skipped", "ledger": str(ledger)}
    try:
        grant = validate_approval(root, approval_path, compiled, "provider_call")
    except (OSError, GovernanceError):
        append_event(ledger, "waiting_approval", {"reason": "approval_missing_or_invalid"})
        return {"run_id": run_id, "status": "waiting_approval", "ledger": str(ledger)}

    if provider_preflight:
        try:
            provider_preflight()
        except Exception:
            append_event(ledger, "skipped", {"reason": "provider_preflight_failed"})
            return {"run_id": run_id, "status": "skipped", "ledger": str(ledger)}

    # A failed ledger write here is deliberately allowed to abort before the adapter is invoked.
    append_event(ledger, "attempted", {
        "operation": "provider_call",
        "approval_scope_sha256": grant["scope_sha256"],
        "approved_by_label": grant["approved_by"],
        "approval_expires_at": grant["expires_at"],
        "turn": 1,
        "call": 1,
        "provider_requested": provider,
        "model_requested": model,
        "reasoning_requested": request.get("reasoning_requested"),
        "tools_requested": policy["allowed_tools"],
        "max_output_tokens": limits["max_output_tokens"],
        "timeout_seconds": limits["timeout_seconds"],
    })
    try:
        request_count = 0

        def record_request(metadata):
            nonlocal request_count
            verify_current_snapshot(root, compiled)
            request_count += 1
            if request_count > limits["max_calls"]:
                raise GovernanceError("provider call budget exceeded")
            if not isinstance(metadata, dict) or set(metadata) != {"request_body_sha256", "target"}:
                raise GovernanceError("provider request metadata is invalid")
            if not isinstance(metadata["request_body_sha256"], str) or not re.fullmatch(
                r"[a-f0-9]{64}", metadata["request_body_sha256"]
            ):
                raise GovernanceError("provider request body hash is invalid")
            if not isinstance(metadata["target"], str) or not metadata["target"] or "@" in metadata["target"]:
                raise GovernanceError("provider target metadata is invalid")
            append_event(ledger, "attempted", {
                "request_body_sha256": metadata["request_body_sha256"],
                "target": metadata["target"],
            })

        output, observed = provider_call(
            provider=provider,
            model=model,
            messages=compiled["bundle"]["messages"],
            max_output_tokens=limits["max_output_tokens"],
            timeout_seconds=limits["timeout_seconds"],
            reasoning=request.get("reasoning_requested"),
            on_request=record_request,
        )
        if request_count != 1:
            raise GovernanceError("provider adapter did not record exactly one serialized request")
    except Exception as exc:  # provider errors may contain secrets or raw response bodies
        try:
            metadata = {"error_type": type(exc).__name__, "error_detail": "redacted"}
            status_code = getattr(exc, "status_code", None)
            if type(status_code) is int and 100 <= status_code <= 599:
                metadata["http_status"] = status_code
            status = "recovery_required" if request_count else "failed"
            if status == "recovery_required":
                metadata["reason"] = "provider_result_may_be_ambiguous"
            append_event(ledger, status, metadata)
        except Exception:
            pass
        return {
            "run_id": run_id,
            "status": "recovery_required" if request_count else "failed",
            "ledger": str(ledger),
        }

    try:
        _, output_hash = write_private_output(private_root, run_id, output)
        details = observed if isinstance(observed, dict) else {}
        append_event(ledger, "succeeded", {
            "output_sha256": output_hash,
            "provider_observed": details.get("provider_observed", "unknown"),
            "model_observed": details.get("model_observed", "unknown"),
            "reasoning_applied": details.get("reasoning_applied", "unknown"),
            "usage_metadata": details.get("usage_metadata"),
        })
        return {"run_id": run_id, "status": "succeeded", "ledger": str(ledger)}
    except Exception:
        # The call may already have incurred cost; recovery is manual and never retries it.
        try:
            append_event(ledger, "recovery_required", {"reason": "post_call_recording_failed"})
        except Exception:
            pass
        return {"run_id": run_id, "status": "recovery_required", "ledger": str(ledger)}
