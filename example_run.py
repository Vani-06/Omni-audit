# example_run.py

import json
from analyzer import FinancialCallAnalyzer
from human_readable import humanize_analysis
from config import GROQ_API_KEY,TRANSCRIPT

analyzer = FinancialCallAnalyzer(GROQ_API_KEY)
result = analyzer.analyze_transcript(TRANSCRIPT)

print("\nHUMAN READABLE SUMMARY")
print("=====================")
print(humanize_analysis(result))

print("\nRAW JSON")
print("========")
print(json.dumps(result, indent=2))
