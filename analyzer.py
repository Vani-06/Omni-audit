# analyzer.py

from llm_client import LLMClient
from prompts import SYSTEM_PROMPT, build_user_prompt
from schema import FINANCIAL_ANALYSIS_SCHEMA
from validator import validate_output

class FinancialCallAnalyzer:
    def __init__(self, api_key: str):
        self.client = LLMClient(api_key)

    def analyze_transcript(self, transcript: str) -> dict:
        prompt = build_user_prompt(transcript, FINANCIAL_ANALYSIS_SCHEMA)
        result = self.client.analyze(SYSTEM_PROMPT, prompt)
        validate_output(result, FINANCIAL_ANALYSIS_SCHEMA)
        return result
