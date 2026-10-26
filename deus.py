#!/usr/bin/env python3
"""Stable repository entry point; Python 3.12 standard library is sufficient."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ortak_kopru.cli import main  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(main())
