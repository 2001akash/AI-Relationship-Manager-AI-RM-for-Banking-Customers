from models import ChatResponse
from config import PROFILE
from utils.formatting import format_currency


def extract_amount(query: str):
    tokens = query.replace(",", " ").split()
    for t in tokens:
        if t.replace("₹", "").isdigit():
            return int(t.replace("₹", ""))
    return None


def handle_personalized_recommendation(query: str) -> ChatResponse:
    amt = extract_amount(query)
    risk = PROFILE["risk_level"]

    reply = ""

    if amt:
        reply += f"You want to invest {format_currency(amt)}.\n\n"

    if risk == "low":
        suggestion = "Short-term debt funds or FDs are suitable for stable returns (~6–7%)."
    elif risk == "moderate":
        suggestion = "A mix of 60% equity and 40% debt funds will balance growth and safety."
    else:
        suggestion = "Higher allocation to equity mutual funds can help maximize growth."

    reply += suggestion
    reply += (
        "\n\nNote: These suggestions are generated based on your mock profile and sample data in this demo."

    )

    return ChatResponse(
        reply=reply,
        intent="personalized_recommendation",
        meta={"amount_detected": amt, "risk": risk}
    )
