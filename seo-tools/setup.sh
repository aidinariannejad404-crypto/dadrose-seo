#!/usr/bin/env bash
# Sets up the dadrose SEO toolkit on a machine with Python 3.11+ and git.
# Pins the two reviewed third-party repos to the commits reviewed on 2026-10-13.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
VENV="${SEO_VENV:-$HOME/seo-venv}"
VENDOR="${SEO_VENDOR:-$HOME/seo-vendor}"

python3 -m venv "$VENV"
"$VENV/bin/pip" install --upgrade pip
"$VENV/bin/pip" install -r "$HERE/requirements.txt"

mkdir -p "$VENDOR"
clone_pinned() { # url dir commit
  [ -d "$VENDOR/$2/.git" ] || git clone -q "$1" "$VENDOR/$2"
  git -C "$VENDOR/$2" fetch -q origin "$3" && git -C "$VENDOR/$2" checkout -q "$3"
}
clone_pinned https://github.com/AminForou/mcp-gsc mcp-gsc d49eea9e5efb5eb645b722249303179b2c150b49
clone_pinned https://github.com/AgriciDaniel/claude-seo claude-seo 4b99de2f7de7e7d5247042e5fb5b4ea9368ef734
"$VENV/bin/pip" install -r "$VENDOR/mcp-gsc/requirements.txt"

echo "Done. Next: put the Search Console service-account JSON at \$HOME/.config/gsc/service-account.json"
echo "and copy mcp.json.example into your project's .mcp.json (edit the paths)."
