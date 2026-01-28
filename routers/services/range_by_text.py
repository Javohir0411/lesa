from datetime import date, timedelta

def calc_range_by_text(text: str, lang: str) -> tuple[date, date] | None:
    t = (text or "").strip().lower()
    today = date.today()

    variants = {
        "today": ["📌 bugun", "bugun", "📌 бугун", "📌 сегодня", "сегодня"],
        "week": ["📅 bir haftalik", "bir haftalik", "📅 бир ҳафталик", "📅 неделя", "неделя"],
        "month": ["🗓 bir oylik", "bir oylik", "🗓 бир ойлик", "🗓 месяц", "месяц"],
        "year": ["📆 bir yillik", "bir yillik", "📆 бир йиллик", "📆 год", "год"],
    }

    if any(x in t for x in variants["today"]):
        return today, today

    if any(x in t for x in variants["week"]):
        return today - timedelta(days=6), today

    if any(x in t for x in variants["month"]):
        return today - timedelta(days=29), today

    if any(x in t for x in variants["year"]):
        return today - timedelta(days=364), today

    return None
