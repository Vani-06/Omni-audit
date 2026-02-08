# human_readable.py

def fmt_amount(a):
    if not a:
        return ""
    if a.get("min_value") and a.get("max_value"):
        return f"{a['min_value']}–{a['max_value']} {a['currency']}"
    if a.get("value"):
        return f"{a['value']} {a['currency']}"
    return ""

def humanize_analysis(data):
    lines = []

    intent = data["intent"]
    lines.append("CALL SUMMARY")
    lines.append("------------")
    lines.append(
        f"Intent: {intent['primary']} "
        f"({int(intent['confidence'] * 100)}%)"
    )
    if intent.get("secondary"):
        lines.append(f"Secondary: {', '.join(intent['secondary'])}")
    lines.append("")

    lines.append("Financial Events:")
    for e in data["financial_events"]:
        amt = fmt_amount(e.get("amount"))
        date = f" by {e['date']}" if e.get("date") else ""
        lines.append(
            f"• [{e['event_type'].replace('_', ' ').title()}] "
            f"{amt}{date} — {e['text']} "
            f"({e['certainty']} certainty)"
        )
    lines.append("")

    emotion = data["emotion_and_stress"]
    lines.append("Emotional State:")
    lines.append(f"• Sentiment: {emotion['overall_sentiment']}")
    lines.append(f"• Stress markers: {', '.join(emotion['stress_markers'])}")
    lines.append("")

    if data["regulatory_phrases"]:
        lines.append("Compliance Notes:")
        for r in data["regulatory_phrases"]:
            lines.append(f"• {r['phrase']}")

    return "\n".join(lines)
