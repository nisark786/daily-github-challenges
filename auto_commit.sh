#!/bin/bash

DAY_FILE=".day"
LANGS=("js" "py" "sql")

if [ ! -f "$DAY_FILE" ]; then
  echo 1 > "$DAY_FILE"
fi

DAY=$(cat "$DAY_FILE")
LANG=${LANGS[$((DAY % 3))]}

FOLDER="day$(printf "%02d" $DAY)"
mkdir -p "$FOLDER"

# -------- Problem generation (placeholder for AI) --------
cat <<EOF > "$FOLDER/problem.md"
## Day $DAY Coding Practice

Write a solution in ${LANG^^}.
EOF

# -------- Solution placeholder (AI will replace this later) --------
case "$LANG" in
  js)
    echo "console.log('Day $DAY solution');" > "$FOLDER/solution.js"
    ;;
  py)
    echo "print('Day $DAY solution')" > "$FOLDER/solution.py"
    ;;
  sql)
    echo "-- Day $DAY SQL solution" > "$FOLDER/solution.sql"
    ;;
esac

git add .
git commit -m "Day $DAY coding practice (${LANG})"
git push origin main

echo $((DAY + 1)) > "$DAY_FILE"

