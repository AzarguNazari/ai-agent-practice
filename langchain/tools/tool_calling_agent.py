import logging
import os

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(name)s: %(message)s",
)
log = logging.getLogger("teaching.tools")


@tool(description="Add two numbers and return their sum.")
def add(a: int, b: int) -> int:
    log.info("add called: a=%s, b=%s", a, b)
    result = a + b
    log.info("add returned: %s", result)
    return result


@tool(description="Return a fixed demo temperature for a given city.")
def get_temperature(city: str) -> str:
    log.info("get_temperature called: city=%s", city)
    result = f"It is always 25 C in {city}."
    log.info("get_temperature returned: %s", result)
    return result


@tool(description="Get weather for a given city.")
def get_weather(city: str) -> str:
    log.info("get_weather called: city=%s", city)
    result = f"It's always sunny in {city}!"
    log.info("get_weather returned: %s", result)
    return result


if __name__ == "__main__":
    model = init_chat_model(
        "deepseek-flash",
        model_provider="openai",
        base_url="https://api.deepseek.com",
        api_key=os.environ["DEEPSEEK_API_KEY"],
    )

    agent = create_agent(
        model,
        tools=[add, get_temperature, get_weather],
        system_prompt=(
            "You are a teaching assistant. Use the provided tools whenever the user "
            "asks for a sum, a temperature, or the weather. Call every relevant tool "
            "and include all of the results in your final answer."
        ),
    )

    question = (
        "Using your tools: add 7 and 5, tell me the temperature in Tehran, "
        "and get the weather in Paris. Report all three results."
    )
    print(f"User: {question}")

    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print(f"Assistant: {response['messages'][-1].content}")
