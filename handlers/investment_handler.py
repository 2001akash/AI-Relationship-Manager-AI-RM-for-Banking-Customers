from models import ChatResponse
from config import INVESTMENTS
from utils.formatting import format_currency


def handle_investment_overview(query: str) -> ChatResponse:
    q = query.lower()
    filtered = INVESTMENTS

    if "equity" in q:
        filtered = [i for i in INVESTMENTS if i["asset_class"] == "equity"]
    elif "debt" in q:
        filtered = [i for i in INVESTMENTS if i["asset_class"] == "debt"]
    elif "fd" in q:
        filtered = [i for i in INVESTMENTS if i["asset_class"] == "fd"]

    total_invested = sum(i["invested_amount"] for i in filtered)
    total_current = sum(i["current_value"] for i in filtered)
    abs_return = total_current - total_invested
    pct_return = abs_return / total_invested * 100

    lines = []
    for i in filtered:
        r = i["current_value"] - i["invested_amount"]
        p = r / i["invested_amount"] * 100
        lines.append(
            f"- {i['product_name']} ({i['asset_class']}): {p:.1f}% returns"
        )

    reply = (
        f"Your investment performance:\n\n"
        + "\n".join(lines)
        + f"\n\nTotal invested: {format_currency(total_invested)}"
        + f"\nCurrent value: {format_currency(total_current)}"
        + f"\nOverall return: {pct_return:.1f}%"
    )

    return ChatResponse(
        reply=reply,
        intent="investment_overview",
        meta={"return_percent": pct_return}
    )
