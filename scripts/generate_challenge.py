import os
import requests

HF_API_KEY = os.environ["HF_API_KEY"]
CHALLENGE_FILE = os.environ.get("CHALLENGE_FILE", "challenge.md")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

PROMPT = """
Generate ONE daily coding challenge.

Include:
1. Problem statement
2. Example input/output
3. Solution code (JavaScript OR Python OR SQL)

Keep it simple and interview friendly.
"""

payload = {
    "inputs": PROMPT,
    "parameters": {
        "max_new_tokens": 400
    }
}

response = requests.post(API_URL, headers=HEADERS, json=payload)
response.raise_for_status()

data = response.json()

# flan-t5 returns dict
text = data.get("generated_text", str(data))

with open(CHALLENGE_FILE, "w", encoding="utf-8") as f:
    f.write(text)

print("Daily challenge generated successfully")
