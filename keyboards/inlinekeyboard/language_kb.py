from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.enums import LanguageEnum


class LanguageCB(CallbackData, prefix="language"):
    lang: LanguageEnum


def language_kb():
    kb = InlineKeyboardBuilder()

    for lang in LanguageEnum:
        kb.button(
            text=lang.value,
            callback_data=LanguageCB(lang=lang).pack()
        )

    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
