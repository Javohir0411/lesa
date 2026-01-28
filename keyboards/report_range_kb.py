from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

def report_range_kb(lang: str) -> ReplyKeyboardMarkup:
    t = {
        "uzl": ["📌 Bugun", "📅 Bir haftalik", "🗓 Bir oylik", "📆 Bir yillik", "✍️ Sana kiritaman"],
        "uzk": ["📌 Бугун", "📅 Бир ҳафталик", "🗓 Бир ойлик", "📆 Бир йиллик", "✍️ Сана киритаман"],
        "rus": ["📌 Сегодня", "📅 Неделя", "🗓 Месяц", "📆 Год", "✍️ Ввести даты"],
    }.get(lang, ["📌 Bugun", "📅 Bir haftalik", "🗓 Bir oylik", "📆 Bir yillik", "✍️ Sana kiritaman"])

    kb = ReplyKeyboardBuilder()
    kb.button(text=t[0])
    kb.button(text=t[1])
    kb.button(text=t[2])
    kb.button(text=t[3])
    kb.button(text=t[4])
    kb.adjust(2, 2, 1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
