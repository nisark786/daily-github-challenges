#!/bin/bash

DAY_FILE=".day"
BRANCH="main"

# Initialize day counter
if [ ! -f "$DAY_FILE" ]; then
  echo 1 > "$DAY_FILE"
fi

DAY=$(cat "$DAY_FILE")

# Create folder for this day
FOLDER="day$(printf "%02d" $DAY)"
mkdir -p "$FOLDER"

# Create or update solution file
echo "Daily challenge – Day $DAY" > "$FOLDER/solution.txt"

# Commit and push
git add .
git commit -m "Day $DAY challenge"
git push origin $BRANCH

# Increment counter
echo $((DAY + 1)) > "$DAY_FILE"

