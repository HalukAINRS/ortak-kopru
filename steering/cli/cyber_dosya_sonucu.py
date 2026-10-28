"""Compare a stopped Write's declared bytes with today's file; never execute or retry it."""
import hashlib
from pathlib import Path


def _fingerprint(stat):
    return stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns


def verify_write(path, expected_content, allowed_root):
    """Return metadata only. A current match is not proof of completion at interruption time."""
    result = {'current_state': 'unknown', 'automatic_retry': False,
              'completed_at_interruption_proven': False, 'safety_decision_prevented': False}
    if not isinstance(expected_content, str):
        return dict(result, current_state='invalid_expected_content')
    expected = expected_content.encode('utf-8')
    result.update(expected_bytes=len(expected), expected_sha256=hashlib.sha256(expected).hexdigest())
    root = Path(allowed_root).resolve(strict=True)
    target = Path(path)
    if not target.is_absolute():
        return dict(result, current_state='absolute_target_required')
    try:
        resolved = target.resolve(strict=True)
        if target.is_symlink() or not resolved.is_relative_to(root):
            return dict(result, current_state='outside_scope_or_symlink')
        if not resolved.is_file():
            return dict(result, current_state='not_regular_file')
        before = resolved.stat()
        first = resolved.read_bytes()
        middle = resolved.stat()
        second = resolved.read_bytes()
        after = resolved.stat()
        if (target.resolve(strict=True) != resolved or _fingerprint(before) != _fingerprint(middle)
                or _fingerprint(middle) != _fingerprint(after) or first != second):
            return dict(result, current_state='changed_during_read')
    except FileNotFoundError:
        return dict(result, current_state='missing')
    except OSError:
        return dict(result, current_state='unreadable')
    result.update(current_bytes=len(first), current_sha256=hashlib.sha256(first).hexdigest(),
                  observation_stability='two_equal_reads_and_equal_file_metadata; not an atomic historical snapshot',
                  current_state='matches_declared_write_now' if first == expected else 'differs_now_do_not_overwrite')
    return result
