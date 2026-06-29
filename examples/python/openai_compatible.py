"""Minimal OpenAI-compatible Agnes AI client example."""

import os

from openai import OpenAI


def main() -> None:
    client = OpenAI(
        api_key=os.environ["AGNES_API_KEY"],
        base_url="https://apihub.agnes-ai.com/v1",
    )

    response = client.chat.completions.create(
        model="agnes-2.0-flash",
        messages=[
            {
                "role": "system",
                "content": "You are a concise API integration assistant.",
            },
            {
                "role": "user",
                "content": "Give three checks before shipping an API integration.",
            },
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
