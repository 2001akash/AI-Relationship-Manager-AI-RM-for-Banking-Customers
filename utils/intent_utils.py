def detect_intent(query: str) -> str:
    q = query.lower().strip()

    # --------------------------------
    # SMALL TALK MUST BE FIRST
    # --------------------------------
    if q in ["hi", "hello", "hey", "hi!", "hello!"]:
        return "greeting"

    if q in ["bye", "byy","goodbye", "see you", "see ya", "bye!", "good night", "goodnight"]:
        return "farewell"

    if q in ["thanks", "thank you", "thankyou", "thx"]:
        return "thanks"

    # --------------------------------
    # TRANSACTION INSIGHTS
    # --------------------------------
    if any(x in q for x in ["spend", "spent", "expense", "expenses", "transactions"]):
        return "transaction_insights"

    # --------------------------------
    # INVESTMENT OVERVIEW
    # --------------------------------
    if any(x in q for x in ["mutual", "portfolio", "fund", "equity", "debt", "fd", "sip", "stocks"]):
        return "investment_overview"

    # --------------------------------
    # RECOMMENDATIONS
    # --------------------------------
    if any(x in q for x in ["recommend", "suggest", "low-risk", "invest", "where should i invest"]):
        return "personalized_recommendation"

    # --------------------------------
    # SMART SUMMARY
    # --------------------------------
    if any(x in q for x in ["summary", "overview", "recurring", "report"]):
        return "smart_summary"

    # --------------------------------
    # FALLBACK
    # --------------------------------
    return "small_talk"
