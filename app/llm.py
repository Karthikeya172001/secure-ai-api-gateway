import os

from openai import OpenAI

api_key = os.getenv("GROQ_API_KEY")

client = None

if api_key:
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1",
    )


def ask_llm(prompt: str) -> str:
    if client is None:
        return f"Mock AI Response: {prompt}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content