# example_run.py

from groq import Groq
from config import GROQ_API_KEY,TRANSCRIPT
from prompts import SYSTEM_PROMPT


def main():
    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.1,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": TRANSCRIPT}
        ]
    )

    print("\n=== CALL ANALYSIS SUMMARY ===\n")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
