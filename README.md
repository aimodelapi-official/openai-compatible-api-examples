# OpenAI-Compatible API Examples

Use the official OpenAI SDK with ModelAPI by changing two settings:

```text
API key:  MODELAPI_API_KEY
Base URL: https://api.aimodelapi.ai/v1
```

This repository contains minimal examples for:

- non-streaming chat completions
- streaming responses
- tool calling
- listing available models

## Run

```bash
export MODELAPI_API_KEY="sk-ama-YOUR_KEY"
python -m pip install openai
python streaming.py
```

See the [OpenAI-compatible integration guide](https://aimodelapi.ai/openai-compatible-api?utm_source=github&utm_medium=repository&utm_campaign=openai_compatible_examples) and [live model catalog](https://aimodelapi.ai/models?utm_source=github&utm_medium=repository&utm_campaign=openai_compatible_examples).

Never commit a real API key. Validate model capabilities in the catalog because tool, image, video, and context-window support varies by model.

