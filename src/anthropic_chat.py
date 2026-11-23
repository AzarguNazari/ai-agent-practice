import os

import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/anthropic",
)

message = client.messages.create(
    model="deepseek-flash",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hi, how are you?"}],
)

for block in message.content:
    if block.type == "text":
        print(block.text)
