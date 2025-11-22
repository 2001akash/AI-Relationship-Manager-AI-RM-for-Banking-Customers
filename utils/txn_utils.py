from typing import List, Dict, Optional
from .date_utils import parse_iso


def filter_transactions_by_date(start, end, txns):
    result = []
    for t in txns:
        d = parse_iso(t["date"])
        if start and d < start:
            continue
        if end and d > end:
            continue
        result.append(t)
    return result


def detect_category(q: str) -> Optional[str]:
    categories = ["food", "travel", "bills", "shopping", "rent", "subscriptions"]
    for c in categories:
        if c in q.lower():
            return c
    return None
