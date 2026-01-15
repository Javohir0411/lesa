from aiogram.types import InlineKeyboardMarkup


def build_pagination_keyboard(current_page: int, total_pages: int):
    kb = InlineKeyboardMarkup(row_width=2)
    buttons = []

    if current_page > 1:
        buttons.append(InlineKeyboardButton(
            text="⬅️ Oldingi",
            callback_data=LeasedPaginationCallback(page=current_page-1).pack()
        ))

    if current_page < total_pages:
        buttons.append(InlineKeyboardButton(
            text="Keyingi ➡️",
            callback_data=LeasedPaginationCallback(page=current_page+1).pack()
        ))

    kb.add(*buttons)
    return kb
