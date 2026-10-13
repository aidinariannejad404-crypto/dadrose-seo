#!/usr/bin/env bash
# Snapshot the two exam-night pages as plain static HTML (G2 "static fallback").
# Run ON THE SERVER (or any Linux box with wget), after the answer-key page is final
# and again every time it is edited on exam night.
#
#   sudo bash make-static-fallback.sh                 # writes /var/www/exam-fallback
#   OUT=/tmp/fb BASE=https://dadrose.com bash make-static-fallback.sh
#
# The web server then serves these copies only when WordPress fails (502/503/504),
# see nginx-exam-night.conf. Nothing here changes the live site by itself.
set -euo pipefail

BASE="${BASE:-https://dadrose.com}"
OUT="${OUT:-/var/www/exam-fallback}"
PAGES=(
  "/questions-and-answer-key-of-the-1405-bar-exam/"
  "/score-percentage-calculator/"
)

mkdir -p "$OUT"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

for p in "${PAGES[@]}"; do
  echo "snapshot: $BASE$p"
  # --page-requisites pulls CSS/JS/images the page needs; --convert-links makes them local;
  # --adjust-extension saves as index.html; -nH drops the host folder.
  wget --quiet --page-requisites --convert-links --adjust-extension \
       --no-host-directories --execute robots=off \
       --user-agent="dadrose-fallback-snapshot/1.0" \
       --directory-prefix="$TMP" "$BASE$p"
done

# Mark the copy so visitors know it may be a few minutes old.
# Do NOT add noindex: the copy is served at the real URL, so if Googlebot fetched it
# during an outage, a noindex would drop the real page from the index.
find "$TMP" -name 'index.html' -print0 | while IFS= read -r -d '' f; do
  sed -i 's#<body\([^>]*\)>#<body\1><div style="background:\#fff3cd;padding:8px;text-align:center;font-family:Tahoma">نسخهٔ پشتیبان صفحه؛ ممکن است چند دقیقه از نسخهٔ اصلی عقب‌تر باشد.</div>#' "$f"
done

# Atomic swap so a half-written snapshot is never served.
rm -rf "$OUT".new && cp -a "$TMP" "$OUT".new && chmod -R a+rX "$OUT".new   # mktemp is 0700; nginx must read it
rm -rf "$OUT".old
[ -d "$OUT" ] && mv "$OUT" "$OUT".old
mv "$OUT".new "$OUT"
echo "done → $OUT"
ls -R "$OUT" | head -30

# The calculator snapshot only works if the calculator runs in the browser (pure JS).
# If it posts to admin-ajax.php or a PHP form, the snapshot will look right but not
# calculate; in that case serve static-calculator.html (same folder as this script) instead.
if grep -qi "admin-ajax" "$OUT/score-percentage-calculator/index.html" 2>/dev/null; then
  echo "WARNING: calculator calls admin-ajax.php → use static-calculator.html as its fallback." >&2
fi
