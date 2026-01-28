from aiogram.fsm.context import FSMContext

from routers.services.rent_report_query import get_rents_for_report
from routers.services.build_excel import build_excel
from database.session import async_session_maker, get_user_language
from states import ReportState
from utils.admin_only import AdminOnly
from aiogram.types import FSInputFile
from datetime import datetime, date
from aiogram import Router, types
from sqlalchemy import select
from db.models import User
import logging
import os

logging.basicConfig(level=logging.INFO)
router = Router(name=__name__)


def parse_two_dates(text: str, lang: str) -> tuple[date, date]:
    parts = text.strip().split()  # yuborilgan matnni boshi va oxiridagi bo'shliqni olib tashlaydi va o'rtasidagi bo'sh joydan ikkiga bo'ladi
    if len(parts) != 2:  # Agar xabar 2 ga bo'linmasa, ya'ni, sanalar alohida-alohida yuborilmasa, XATOLIK chiqadi
        raise ValueError(
            {
                "uzl": "Ikkita sana yuborilishi kerak!",
                "uzk": "Иккита сана юборилиши керак!",
                "rus": "Необходимо прислать две даты!",
            }[lang]
        )
    d1 = datetime.strptime(parts[0], "%d.%m.%Y").date()  # birinchi qismini faqat sanasini oladi, vaqtni olmaydi
    d2 = datetime.strptime(parts[1], "%d.%m.%Y").date()  # bu ham xuddi shunday 👆
    if d2 < d1:  # agar user sananni o'rnini almashtirib qo'ysa:
        d1, d2 = d2, d1  # o'rnini almashtirib, to'g'irlab qo'yadi
    return d1, d2  # Natija


@router.message(AdminOnly(), ReportState.get_start_end_dates)
async def rent_report_dates_input(message: types.Message, state: FSMContext):
    lang = await get_user_language(message)
    logging.info(f"RENT REPORT INPUT TEXT: {message.text}")
    try:
        start_date, end_date = parse_two_dates(message.text, lang)
        logging.info(f"START DATE: {start_date}, END DATE {end_date}")
    except ValueError as e:
        await message.answer(
            {
                "uzl": f"❌ Xatolik: {e}\n\n "
                       f"✅ To‘g‘ri format:\n "
                       f"`01.01.2026 10.01.2026`",

                "uzk": f"❌ Хатолик: {e}\n\n "
                       f"✅ Тўғри формат:\n "
                       f"`01.01.2026 10.01.2026`",

                "rus": f"❌ Ошибка: {e}\n\n "
                       f"✅ Правильный формат:\n "
                       f"`01.01.2026 10.01.2026`",
            }[lang],
            parse_mode='Markdown'
        )
        return

    except Exception as e:
        logging.info(f"EXCEPTION: {e}")
        await message.answer(
            {
                "uzl": "❌ Sana formati noto‘g‘ri.\n\n"
                       "✅ To‘g‘ri format:\n"
                       "`01.01.2026 10.01.2026`",

                "uzk": "❌ Сана формати нотўғри.\n\n"
                       "✅ Тўғри формат:\n"
                       "`01.01.2026 10.01.2026`",

                "rus": "❌ Неверный формат даты.\n\n"
                       "✅ Правильный формат:\n"
                       "`01.01.2026 10.01.2026`",
            }[lang],
            parse_mode="Markdown"
        )
        return

    async with async_session_maker() as session:
        user = await session.scalar(
            select(User).where(User.telegram_id == message.from_user.id)
        )
        if not user:
            await message.answer("❗ Сиз базада рўйхатдан ўтмагансиз.")
            return

        rents = await get_rents_for_report(session, user.id, start_date, end_date)

    if not rents:
        await message.answer(
            {
                "uzl": "📭 Bu sana oralig‘ida ma’lumot topilmadi.",
                "uzk": "📭 Бу сана оралиғида маълумот топилмади.",
                "rus": "📭 Информация по данному временному диапазону не найдена.",
            }
        )
        return

    stream = build_excel(rents, start_date, end_date)

    os.makedirs("tmp", exist_ok=True)
    filename = f"rent_report_{start_date.isoformat()}_to_{end_date.isoformat()}.xlsx"
    tmp_path = os.path.join("tmp", filename)

    with open(tmp_path, "wb") as f:
        f.write(stream.getvalue())

    text = {
        "uzl": f"📊 Ijara hisobot\n{start_date.isoformat()} — {end_date.isoformat()}\nJami: {len(rents)} ta yozuv",
        "uzk": f"📊 Ижара ҳисобот\n{start_date.isoformat()} — {end_date.isoformat()}\nЖами: {len(rents)} та ёзув",
        "rus": f"📊 Отчет об аренде\n{start_date.isoformat()} — {end_date.isoformat()}\nОбщий: {len(rents)} записи",
    }[lang]

    await message.answer_document(
        document=FSInputFile(tmp_path),
        caption=text
    )

    try:
        os.remove(tmp_path)
        await state.clear()
    except OSError as e:
        logging.warning(f"TEMP FAYL O'CHIRILMADI: {e}")
        pass


@router.message(ReportState.get_start_end_dates)
async def rent_report_dates_input_not_admin(message: types.Message):
    lang = await get_user_language(message)
    await message.answer(
        {
            "uzl": "Sizga ruxsat yo'q❌ \nMa'lumotlar faqat admin uchun",
            "uzk": "Сизга рухсат йўқ ❌ \nМаълумотлар фақат админ учун",
            "rus": "Вам запрещено ❌ \nИнформация только для администратора.",
        }.get(lang, "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун")
    )




@router.message(ReportState.get_start_end_dates)
async def rent_report_dates_input_not_admin(message: types.Message):
    lang = await get_user_language(message)
    await message.answer(
        {
            "uzl": "Sizga ruxsat yo'q❌ \nMa'lumotlar faqat admin uchun",
            "uzk": "Сизга рухсат йўқ ❌ \nМаълумотлар фақат админ учун",
            "rus": "Вам запрещено ❌ \nИнформация только для администратора.",
        }.get(lang, "Сизга рухсат йўқ ❌\nМаълумотлар фақат админ учун")
    )
