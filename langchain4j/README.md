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
cd langchain4j
mvn compile exec:java
```

## Tool calling

`src/main/java/com/example/tools/` contains the same teaching exercise as the
Python example: three tools (`add`, `getTemperature`, `getWeather`) that each log
their arguments and result when the model calls them.

```bash
cd langchain4j
mvn -Dexec.mainClass=com.example.tools.ToolCallingAgentExample compile exec:java
```

The log format comes from the `logging.format` property in `pom.xml`; the exec
plugin passes it to the JVM, so no logging setup is needed in the Java code.
