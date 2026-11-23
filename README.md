# LLM practice playground

Two minimal chat examples that call the DeepSeek API with different SDKs.

## Setup

```bash
uv sync
source .venv/bin/activate
export DEEPSEEK_API_KEY="sk-..."
```

## Run

```bash
python3 src/openai_chat.py
python3 src/anthropic_chat.py
```

- `src/openai_chat.py` uses the OpenAI SDK at `https://api.deepseek.com`.
- `src/anthropic_chat.py` uses the Anthropic SDK at `https://api.deepseek.com/anthropic`.

`max_tokens` is required by the Anthropic SDK; everything else is just `model`
and `messages`.
