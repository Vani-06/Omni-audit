# schema.py

FINANCIAL_ANALYSIS_SCHEMA = {
    "type": "object",
    "properties": {

        # ======================
        # INTENT
        # ======================
        "intent": {
            "type": "object",
            "properties": {
                "primary": {"type": "string"},
                "secondary": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "confidence": {"type": "number"}
            },
            "required": ["primary", "confidence"]
        },

        # ======================
        # FINANCIAL EVENTS (CORE FIX)
        # ======================
        "financial_events": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "event_type": {
                        "type": "string",
                        "enum": [
                            "outstanding_balance",
                            "past_payment",
                            "proposed_payment",
                            "conditional_payment",
                            "confirmed_payment",
                            "penalty",
                            "interest_information"
                        ]
                    },
                    "speaker": {
                        "type": "string",
                        "enum": ["Customer", "Agent", "System"]
                    },
                    "amount": {
                        "type": ["object", "null"],
                        "properties": {
                            "value": {"type": ["number", "null"]},
                            "min_value": {"type": ["number", "null"]},
                            "max_value": {"type": ["number", "null"]},
                            "currency": {"type": "string"}
                        }
                    },
                    "date": {
                        "type": ["string", "null"],
                        "description": "Exact or vague date expression (e.g. 'today', 'next week', '25th')"
                    },
                    "certainty": {
                        "type": "string",
                        "enum": ["high", "medium", "low"]
                    },
                    "text": {
                        "type": "string",
                        "description": "Exact transcript snippet describing this event"
                    }
                },
                "required": [
                    "event_type",
                    "speaker",
                    "certainty",
                    "text"
                ]
            }
        },

        # ======================
        # OBLIGATIONS / PROMISES
        # ======================
        "obligations_and_promises": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "commitment_type": {
                        "type": "string",
                        "enum": ["confirmed", "conditional", "soft", "refusal"]
                    },
                    "speaker": {"type": "string"},
                    "text": {"type": "string"},
                    "due_date": {"type": ["string", "null"]},
                    "confidence": {"type": "number"}
                },
                "required": [
                    "commitment_type",
                    "speaker",
                    "text",
                    "due_date",
                    "confidence"
                ]
            }
        },

        # ======================
        # EMOTION & STRESS
        # ======================
        "emotion_and_stress": {
            "type": "object",
            "properties": {
                "overall_sentiment": {"type": "string"},
                "stress_markers": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "emotion_confidence": {"type": "number"}
            },
            "required": [
                "overall_sentiment",
                "stress_markers",
                "emotion_confidence"
            ]
        },

        # ======================
        # REGULATORY / COMPLIANCE
        # ======================
        "regulatory_phrases": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "phrase": {"type": "string"},
                    "category": {"type": "string"}
                },
                "required": ["phrase", "category"]
            }
        }
    },

    # ======================
    # REQUIRED ROOT FIELDS
    # ======================
    "required": [
        "intent",
        "financial_events",
        "obligations_and_promises",
        "emotion_and_stress",
        "regulatory_phrases"
    ]
}
