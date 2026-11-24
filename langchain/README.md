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
