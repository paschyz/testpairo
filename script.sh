#!/bin/sh
# Copy users.py to users<N>.py (next free N), commit and push on feature/users.
set -e
cd "$(dirname "$0")"
[ "$(git branch --show-current)" = test1 ] || { echo "not on feature/users" >&2; exit 1; }
n=1
while [ -e "users$n.py" ]; do n=$((n+1)); done
cp users.py "users$n.py"
git add "users$n.py"
git commit -m "Add snapshot users$n.py"
git push -u origin test1
