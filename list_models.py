import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MODELAPI_API_KEY"],
    base_url="https://api.aimodelapi.ai/v1",
)

for model in client.models.list().data:
    print(model.id)

