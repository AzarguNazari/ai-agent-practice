import json
import os

from openai import OpenAI
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

schema = json.dumps(Person.model_json_schema())
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {
            "role": "user",
            "content": (
                "Describe a person named Ada who is 36. "
                f"Reply with a JSON object matching this schema: {schema}"
            ),
        }
    ],
    response_format={"type": "json_object"},
)

print(Person.model_validate_json(response.choices[0].message.content))
