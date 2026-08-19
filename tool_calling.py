import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MODELAPI_API_KEY"],
    base_url="https://api.aimodelapi.ai/v1",
)

response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": "What is the weather in Singapore?"}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string"}},
                "required": ["city"],
            },
        },
    }],
)

message = response.choices[0].message
print(json.dumps([call.model_dump() for call in message.tool_calls or []], indent=2))

