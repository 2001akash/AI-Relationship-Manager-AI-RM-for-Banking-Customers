from models import ChatResponse
from config import TRANSACTIONS
from utils.txn_utils import detect_category, filter_transactions_by_date
from utils.date_utils import detect_time_range
from utils.formatting import format_currency


def handle_transaction_insights(query: str) -> ChatResponse:
    category = detect_category(query)
    start, end, label = detect_time_range(query)

    txns = filter_transactions_by_date(start, end, TRANSACTIONS)

    if category:
        txns = [t for t in txns if t["category"] == category]

    if not txns:
        return ChatResponse(
            reply=f"No {category or ''} transactions found for {label}.",
            intent="transaction_insights",
            meta={}
        )

    total = sum(t["amount"] for t in txns)
    highest = max(txns, key=lambda x: x["amount"])

    reply = (
        f"Here is your {category or 'overall'} spending for {label}:\n\n"
        f"- Total spent: {format_currency(total)}\n"
        f"- Transactions: {len(txns)}\n"
        f"- Highest transaction: {format_currency(highest['amount'])} "
        f"on {highest['date']} ({highest['notes']})"
    )

    return ChatResponse(
        reply=reply,
        intent="transaction_insights",
        meta={"total": total, "category": category, "label": label}
    )
