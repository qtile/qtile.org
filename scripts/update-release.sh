#!/bin/bash
# Update currentRelease in config.toml with the latest qtile release tag.
set -euo pipefail

cd "$(dirname "$0")/.."

release=$(curl --fail -s https://api.github.com/repos/qtile/qtile/releases/latest)
tag=$(jq -r .tag_name <<<"$release")
date=$(date -d "$(jq -r .published_at <<<"$release")" '+%b %-d, %Y')

sed -i "s/^\(\s*currentRelease\s*=\s*\).*/\1\"$tag, $date\"/" config.toml
grep currentRelease config.toml

if git diff --quiet config.toml; then
    echo "already up to date, nothing to commit"
    exit 0
fi

git commit -s -m "update release for ${tag#v}" config.toml
