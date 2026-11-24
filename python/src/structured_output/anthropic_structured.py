import json
import os

import anthropic
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


client = anthropic.Anthropic(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com/anthropic",
)

schema = json.dumps(Person.model_json_schema())
message = client.messages.create(
    model="deepseek-flash",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": (
                "Describe a person named Ada who is 36. "
                f"Reply with a JSON object matching this schema: {schema}"
            ),
        }
    ],
    output_config={"format": {"type": "json_schema", "schema": Person.model_json_schema()}},
)

text = next(block.text for block in message.content if block.type == "text")
print(Person.model_validate_json(text))
