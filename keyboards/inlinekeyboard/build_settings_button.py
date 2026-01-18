import logging

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils.enums import SettingsCB, SettingsActions

logging.basicConfig(level=logging.INFO)


def build_settings_button(lang: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    logging.info(f"BUILD SETTINGS BUTTON LANGUAGE : {lang}")

    builder.button(
        text={
            "uzl": "Tilni o'zgartirish 🌐",
            "uzk": "Тилни ўзгартириш 🌐",
            "rus": "Изменить язык 🌐",
        }[lang],
        callback_data=SettingsCB(action=SettingsActions.language).pack()
    )

    builder.button(
        text={
            "uzl": "👨‍💻 Dasturchi bilan aloqa",
            "uzk": "👨‍💻 Дастурчи билан алоқа",
            "rus": "👨‍💻 Свяжитесь с разработчиком",
        }[lang],
        url="https://t.me/javohir_abduhakimoff"
    )
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def back_kb(lang: str):
    kb = InlineKeyboardBuilder()
    kb.button(
        text={
            "uzl": "⬅️ Orqaga",
            "uzk": "⬅️ Орқага",
            "rus": "⬅️ Назад",
        }[lang],
        callback_data=SettingsCB(action=SettingsActions.back))
    return kb.as_markup()



    builder.button(
        text={
            "uzl": "Ijara holatini boshqarish 📊",
            "uzk": "Ижара ҳолатини бошқариш 📊",
            "rus": "Управление статусом аренды 📊",
        }[lang],
        callback_data=SettingsCB(action=SettingsActions.renter).pack()
    )
    builder.button(
        text={
            "uzl": "Mahsulot / Qo'shimchalar 🛠",
            "uzk": "Маҳсулот / Қўшимчалар 🛠",
            "rus": "Продукт / Добавки 🛠",
        }[lang],
        callback_data=SettingsCB(action=SettingsActions.products).pack()
    )
    builder.button(
        text={
            "uzl": "Shaxsiy ma'lumotlar ✍️",
            "uzk": "Шахсий маълумотлар ✍️",
            "rus": "Персональная информация ✍️",
        }[lang],
        callback_data=SettingsCB(action=SettingsActions.user_info).pack()
    )