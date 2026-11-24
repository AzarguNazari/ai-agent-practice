# Python LLM practice playground

Two minimal structured-output examples that call the DeepSeek API with different
SDKs.

## Setup

From this directory:

```bash
uv sync
source .venv/bin/activate
export DEEPSEEK_API_KEY="sk-..."
```

## Run

```bash
./openai_run.sh
./anthropic_run.sh
```

Or run the scripts directly:

```bash
python3 src/structured_output/openai_structured.py
python3 src/structured_output/anthropic_structured.py
```

- `src/structured_output/openai_structured.py` uses the OpenAI SDK at `https://api.deepseek.com`.
- `src/structured_output/anthropic_structured.py` uses the Anthropic SDK at `https://api.deepseek.com/anthropic`.

`max_tokens` is required by the Anthropic SDK; everything else is just `model`
and `messages`.
