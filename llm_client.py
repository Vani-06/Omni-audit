# llm_client.py

import json
import re
from groq import Groq

class LLMClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise RuntimeError("LLM API key missing")

        self.client = Groq(api_key=api_key)

    def _extract_json(self, raw: str) -> dict:
        """
        Robust JSON extraction:
        - Handles empty output
        - Handles leading text
        - Handles markdown
        """

        if not raw or not raw.strip():
            raise RuntimeError("LLM returned empty output")

        text = raw.strip()

        # Remove markdown fences if present
        if text.startswith("```"):
            text = re.sub(r"^```[a-zA-Z]*", "", text)
            text = text.replace("```", "").strip()

        # Find first JSON object
        match = re.search(r"\{[\s\S]*\}", text)
        if not match:
            raise RuntimeError(
                f"No JSON object found in model output:\n{raw}"
            )

        json_text = match.group(0)

        try:
            return json.loads(json_text)
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"JSON parsing failed.\n"
                f"Extracted JSON:\n{json_text}\n\n"
                f"Original output:\n{raw}\n\n"
                f"Error: {e}"
            )

    def analyze(self, system_prompt: str, user_prompt: str) -> dict:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.1,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        raw_output = response.choices[0].message.content
        return self._extract_json(raw_output)
