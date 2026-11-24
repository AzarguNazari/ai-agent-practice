import os

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "deepseek-chat",
    model_provider="openai",
    base_url="https://api.deepseek.com",
    api_key=os.environ["DEEPSEEK_API_KEY"],
)

print(model.invoke("Say hello from DeepSeek in one sentence.").content)
