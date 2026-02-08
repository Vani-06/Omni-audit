# postprocess.py

def filter_regulatory_phrases(phrases):
    keywords = ["recorded", "legal notice", "compliance", "quality"]
    return [
        p for p in phrases
        if any(k in p["phrase"].lower() for k in keywords)
    ]


def calibrate_obligation_confidence(obligations):
    for o in obligations:
        if o["commitment_type"] == "refusal":
            o["confidence"] = min(o["confidence"], 0.3)
        elif o["commitment_type"] == "soft":
            o["confidence"] = min(o["confidence"], 0.5)
        elif o["commitment_type"] == "conditional":
            o["confidence"] = min(o["confidence"], 0.6)
    return obligations
