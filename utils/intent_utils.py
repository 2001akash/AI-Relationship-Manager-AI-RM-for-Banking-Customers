def detect_intent(query: str) -> str:
    q = query.lower()

    if any(x in q for x in ["spend", "spent", "expense", "transactions"]):
        return "transaction_insights"

    if any(x in q for x in ["mutual", "portfolio", "fund", "equity", "debt", "fd", "sip"]):
        return "investment_overview"

    if any(x in q for x in ["recommend", "suggest", "low-risk", "invest"]):
        return "personalized_recommendation"

    if any(x in q for x in ["summary", "overview", "recurring"]):
        return "smart_summary"

    return "small_talk"
