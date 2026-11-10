#!/usr/bin/env bash
set -euo pipefail

if (($# > 1)); then
  echo 'Usage: bash install_clients.sh [/absolute/user-owned/prefix]' >&2
  exit 2
fi

clients_prefix="${1:-/workspace/tools/divan-clients}"
case "$clients_prefix" in
  /*) ;;
  *) echo 'The installation prefix must be an absolute path.' >&2; exit 2 ;;
esac

clients_config_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
command -v node >/dev/null
command -v npm >/dev/null
node -e 'if (Number(process.versions.node.split(".")[0]) < 22) { console.error("Node.js 22 or newer is required."); process.exit(1); }'

# Validate all existing manifests before copying anything; never replace local work.
for clients_manifest in package.json package-lock.json; do
  test -f "$clients_config_dir/clients/$clients_manifest"
  if [[ -e "$clients_prefix/$clients_manifest" ]] && ! cmp -s -- "$clients_config_dir/clients/$clients_manifest" "$clients_prefix/$clients_manifest"; then
    echo "Existing different manifest preserved: $clients_prefix/$clients_manifest" >&2
    exit 1
  fi
done

mkdir -p -- "$clients_prefix"
for clients_manifest in package.json package-lock.json; do
  if [[ ! -e "$clients_prefix/$clients_manifest" ]]; then
    cp --no-clobber -- "$clients_config_dir/clients/$clients_manifest" "$clients_prefix/$clients_manifest"
  fi
  cmp -s -- "$clients_config_dir/clients/$clients_manifest" "$clients_prefix/$clients_manifest"
done

# npm verifies the pinned registry artifacts using the lockfile integrity values.
# This installs CLI programs only; it does not log in or invoke a model.
npm ci --prefix "$clients_prefix" --no-audit --no-fund
"$clients_prefix/node_modules/.bin/claude" --version
"$clients_prefix/node_modules/.bin/gemini" --version
