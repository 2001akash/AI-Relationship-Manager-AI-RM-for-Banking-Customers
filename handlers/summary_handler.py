from models import ChatResponse
from config import TRANSACTIONS, INVESTMENTS
from utils.date_utils import detect_time_range
from utils.txn_utils import filter_transactions_by_date
from utils.formatting import format_currency


def handle_smart_summary(query: str) -> ChatResponse:
    start, end, label = detect_time_range(query)
    txns = filter_transactions_by_date(start, end, TRANSACTIONS)

    total = sum(t["amount"] for t in txns)
    invested = sum(i["invested_amount"] for i in INVESTMENTS)
    current = sum(i["current_value"] for i in INVESTMENTS)

    reply = (
        f"Summary for {label}:\n\n"
        f"- Total spending: {format_currency(total)}\n"
        f"- Transactions: {len(txns)}\n\n"
        f"Investments:\n"
        f"- Invested: {format_currency(invested)}\n"
        f"- Current Value: {format_currency(current)}\n"
        f"- Overall Return: {((current - invested) / invested * 100):.1f}%\n"
    )

    return ChatResponse(
        reply=reply,
        intent="smart_summary",
        meta={"label": label, "total_spent": total}
    )
