from huggingface_hub import InferenceClient
import os

HF_API_KEY = os.getenv("HF_API_KEY")

client = InferenceClient(
    model="tiiuae/falcon-7b-instruct",
    token=HF_API_KEY
)

prompt = """
Generate a daily coding challenge.
Difficulty: Easy
Language: Python
Include:
- Problem statement
- Example input/output
- Constraints
"""

response = client.text_generation(
    prompt,
    max_new_tokens=300,
    temperature=0.7
)

with open(".current_file", "r") as f:
    challenge_file = f.read().strip()

with open(challenge_file, "w") as f:
    f.write(response)

print("Challenge generated successfully.")
