import logging

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.session import get_user_language
from keyboards.report_range_kb import report_range_kb
from states import ReportState
from utils.admin_only import AdminOnly

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


@router.message(F.text, AdminOnly(), Command("rent_report", prefix="/!"))
async def rent_report_start(message: types.Message, state: FSMContext):
    lang = await get_user_language(message)
    logging.info(f"RENT REPORT TEXT: {message.text}")
    await message.answer(
        {
            "uzl":"📅 Sana oralig‘ini yuboring (faqat sana):\n `DD.MM.YYYY DD.MM.YYYY`\n Masalan: `01.01.2026 10.01.2026`",
            "uzk":"📅 Сана оралиғини юборинг (фақат сана):\n `ДД.ММ.ГГГГ ДД.ММ.ГГГГ` \n Масалан: `01.01.2026 10.01.2026`",
            "rus":"📅 Укажите диапазон дат (только даты).:\n `ДД.ММ.ГГГГ ДД.ММ.ГГГГ` \n Например: `01.01.2026 10.01.2026`",
        }.get(lang, "📅 Сана оралиғини юборинг (фақат сана):\n `ДД.ММ.ГГГГ ДД.ММ.ГГГГ` \n Масалан: `01.01.2026 10.01.2026`"),
        parse_mode="Markdown",
        # reply_markup=report_range_kb(lang)
    )
    await state.set_state(ReportState.get_start_end_dates)


@router.message(F.text, Command("rent_report", prefix="/!"))
async def rent_report_no_access(message: types.Message):
    lang = await get_user_language(message)
    await message.answer(
        {
            "uzl": "Sizga ruxsat yo'q ❌\nMa'lumotlar faqat admin uchun",
            "uzk": "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун",
            "rus": "Вам запрещено ❌\nИнформация только для администратора.",
        }.get(lang, "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун")
    )