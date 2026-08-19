import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MODELAPI_API_KEY"],
    base_url="https://api.aimodelapi.ai/v1",
)

stream = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "Explain API gateways in three bullets."}],
    stream=True,
)

for chunk in stream:
    text = chunk.choices[0].delta.content
    if text:
        print(text, end="", flush=True)
print()

