# llm_client.py

import json
from groq import Groq

class LLMClient:
    def __init__(self, api_key: str):
        self.client = Groq(api_key=api_key)

    def analyze(self, system_prompt: str, user_prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.1,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        text = response.choices[0].message.content.strip()

        # strip markdown if present
        if text.startswith("```"):
            text = text.strip("`").replace("json", "", 1).strip()

        return json.loads(text)
