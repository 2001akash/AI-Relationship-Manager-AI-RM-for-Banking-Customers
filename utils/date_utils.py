from datetime import date, datetime, timedelta


MONTH_NAMES = [
    "", "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december"
]


def parse_iso(d: str) -> date:
    return datetime.fromisoformat(d).date()


def detect_time_range(query: str):
    q = query.lower()
    today = date.today()

    if "last month" in q:
        first_this_month = today.replace(day=1)
        last_month_end = first_this_month - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)
        return last_month_start, last_month_end, "last month"

    if "this month" in q or "current month" in q:
        return today.replace(day=1), today, "this month"

    if "last week" in q:
        return today - timedelta(days=7), today, "last week"

    for idx, m in enumerate(MONTH_NAMES):
        if m and m in q:
            start = date(today.year, idx, 1)
            end = start.replace(month=start.month + 1) - timedelta(days=1) if idx < 12 else date(today.year, 12, 31)
            return start, end, start.strftime("%B")

    return None, None, "overall"
