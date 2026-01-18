from keyboards.inlinekeyboard.language_kb import language_kb
from utils.enums import SettingsCB, SettingsActions
from database.session import get_user_language
from aiogram import Router, types
import logging


router = Router(name=__name__)

logging.basicConfig(level=logging.INFO)


@router.callback_query(SettingsCB.filter())
async def settings_callback(call: types.CallbackQuery, callback_data: SettingsCB):
    logging.info(f"SETTING HANDLE CALLBACK DATA : {callback_data}")
    action = callback_data.action
    logging.info(f"SETTING CALLBACK ACTION : {action}")
    lang = await get_user_language(call.message)

    if action == SettingsActions.language:
        await call.message.edit_text(
            text={
                "uzl": "Tilni tanlang: ",
                "uzk": "Тилни танланг: ",
                "rus": "Выберите язык: ",
            }[lang],
            reply_markup=language_kb()
        )
    await call.answer()







    # elif action == SettingsActions.renter:
    #     lang = await get_user_language(call.message)
    #
    #     async with async_session_maker() as session:
    #         result = await session.execute(select(Renter))
    #         renters = result.scalars().all()
    #
    #     if not renters:
    #         await call.message.edit_text(
    #             {
    #                 "uzl": "Hozircha ijarachilar mavjud emas",
    #                 "uzk": "Ҳозирча ижарачилар мавжуд эмас",
    #                 "rus": "Пока нет арендаторов",
    #             }[lang]
    #         )
    #     buttons = []
    #     for renter in renters:
    #         buttons.append([
    #             InlineKeyboardButton(
    #                 text=renter.renter_fullname,
    #                 callback_data=f"select_renter:{renter.id}"
    #             )
    #         ])
    #     buttons.append([
    #         InlineKeyboardButton(
    #             text={"uzl": "⬅️ Orqaga", "uzk": "⬅️ Орқага", "rus": "⬅️ Назад"}[lang],
    #             callback_data="settings:renter",
    #         )
    #     ])
    #
    #     kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    #     await call.message.edit_text(
    #         {
    #             "uzl": "Ijarachini tanlang:",
    #             "uzk": "Ижарачини танланг:",
    #             "rus": "Выберите арендатора:",
    #         }[lang],
    #         reply_markup=kb
    #     )
    #
    # elif action == SettingsActions.products:
    #     await call.message.edit_text(
    #         "📦 Mahsulotlarni boshqarish (qo‘shish / tahrirlash)"
    #     )
    #
    # elif action == SettingsActions.user_info:
    #     await call.message.edit_text(
    #         "👤 Shaxsiy ma’lumotlaringizni tahrirlash"
    #     )
