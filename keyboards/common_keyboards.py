from typing import Iterable

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def choose_language_kb():
    button_uzl = KeyboardButton(text="O'zbek tili (lotin) 🇺🇿")
    button_uzk = KeyboardButton(text="Ўзбек тили (крилл) 🇺🇿")
    button_rus = KeyboardButton(text="Русский язык 🇷🇺")
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [button_uzl],
            [button_uzk],
            [button_rus]
        ],
        resize_keyboard=True
    )
    return markup


def build_select_keyboard(options: Iterable[str]) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for option in options:
        builder.button(text=option)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
