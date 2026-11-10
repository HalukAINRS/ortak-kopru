#!/usr/bin/env bash
set -euo pipefail
# Run from the retained snapshot or an extracted portable package.
# No package install, checkout mutation, credentials copy or desktop app is needed.
divan_setup_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$divan_setup_root"
command -v python3 >/dev/null
command -v git >/dev/null
test -f bin/divan.py
test -f bin/divan_git.py
python3 bin/divan.py --root "$divan_setup_root" init
python3 bin/divan.py --root "$divan_setup_root" doctor
