import os
from transformers import pipeline

hf_api_key = os.environ['HF_API_KEY']
challenge_file = os.environ['CHALLENGE_FILE']

generator = pipeline(
    "text-generation",
    model="bigcode/starcoder",
    use_auth_token=hf_api_key
)

prompt = (
    "Generate a concise coding challenge with a problem statement and "
    "solution code in JavaScript, Python, or SQL."
)

result = generator(prompt, max_new_tokens=400)

# result is a list of dicts with 'generated_text'
challenge_text = result[0]['generated_text']

with open(challenge_file, "w") as f:
    f.write(challenge_text)
