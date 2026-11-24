# Java LLM practice playground

A minimal LangChain4j example that calls DeepSeek.

The code uses the framework-level `ChatModel` abstraction. LangChain4j still
needs one provider module to make the HTTP call; DeepSeek is OpenAI-compatible,
so `langchain4j-open-ai` is used only as the transport with a custom base URL.
There is no separate Anthropic path.

- Base URL: `https://api.deepseek.com`
- Model: `deepseek-chat`
- API key: the `DEEPSEEK_API_KEY` environment variable (already exported in this environment)

## Run

```bash
cd java
mvn compile exec:java
```
