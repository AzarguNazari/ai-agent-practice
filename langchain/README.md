# Python LangChain practice playground

A minimal LangChain example that calls DeepSeek. DeepSeek is OpenAI-compatible,
so the OpenAI provider is used only as the transport with a custom base URL.

- Base URL: `https://api.deepseek.com`
- Model: `deepseek-chat`
- API key: the `DEEPSEEK_API_KEY` environment variable

## Run

```bash
cd langchain
./run.sh
```

`run.sh` creates a local `.venv` with `uv` if needed, installs `requirements.txt`, and runs the example.

## Tool calling

`tools/tool_calling_agent.py` is a small agent with three tools: `add`,
`get_temperature`, and `get_weather`. Each tool logs its arguments and result, so
you can see exactly which tool the model calls.

```bash
cd langchain
.venv/bin/python tools/tool_calling_agent.py
```

For a first exercise, ask one thing at a time (for example, "add 7 and 5"), then
change the question in the script to ask for all three results in one turn.
