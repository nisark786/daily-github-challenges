#!/bin/bash

# ----------------------------
# CONFIG
# ----------------------------
REPO_DIR="$HOME/daily-github-challenges"
DAY_FILE="$REPO_DIR/.day"

# Initialize day counter if missing
if [ ! -f "$DAY_FILE" ]; then
  echo 1 > "$DAY_FILE"
fi

DAY=$(cat "$DAY_FILE")
DAY_DIR="$REPO_DIR/day$(printf "%02d" $DAY)"
mkdir -p "$DAY_DIR"

# ----------------------------
# AI Challenge Generation
# ----------------------------
# Rotate languages: JS, Python, SQL
LANGS=("JavaScript" "Python" "SQL")
LANG=${LANGS[$((DAY % 3))]}

PROMPT="Generate a simple $LANG coding challenge with problem statement and solution code. Keep it concise."

# Run AI and save output
AI_OUTPUT=$(ollama run phi3:mini "$PROMPT")  # lightweight and fast model
echo "$AI_OUTPUT" > "$DAY_DIR/challenge.md"

# ----------------------------
# Git commit & push
# ----------------------------
cd "$REPO_DIR" || exit 1
git add .
git commit -m "Day $DAY: $LANG Coding Challenge"
git push origin main

# ----------------------------
# Increment day counter
# ----------------------------
echo $((DAY + 1)) > "$DAY_FILE"

