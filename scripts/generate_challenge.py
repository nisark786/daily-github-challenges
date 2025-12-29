import os
from huggingface_hub import InferenceClient

hf_api_key = os.environ['HF_API_KEY']
challenge_file = os.environ['CHALLENGE_FILE']

client = InferenceClient(token=hf_api_key)

prompt = (
    "Generate a concise coding challenge with a problem statement and "
    "solution code in JavaScript, Python, or SQL."
)

response = client.text_generation(model="bigcode/starcoder", inputs=prompt, max_new_tokens=400)

if isinstance(response, list) and "generated_text" in response[0]:
    challenge_text = response[0]["generated_text"]
else:
    challenge_text = str(response)

with open(challenge_file, "w") as f:
    f.write(challenge_text)

