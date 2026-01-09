from aiogram.utils import markdown

from keyboards.get_phone_number import get_phone_number_kb
from bot_strings.start_command_strings import StartStrings
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
from states import Register

router = Router(name=__name__)


@router.message(F.text, Register.full_name)
async def handle_user_fullname(message: types.Message, state: FSMContext):
    user_fullname = message.text

    await state.update_data(user_fullname=user_fullname)
    await state.set_state(Register.phone_number)

    data = await state.get_data()

    lang = data.get("selected_language")
    message_text = StartStrings.GET_USER_FULLNAME[lang].format(
        user_fullname= markdown.hbold(user_fullname),
    )
    # matnlarga dynamic o'zgaruvchi qildik .format yordamida

    kb = await get_phone_number_kb(state)

    if lang == "uzl":
        await message.answer(
            text=message_text,
            reply_markup=kb
        )

    elif lang == 'uzk':
        await message.answer(
            text=message_text,
            reply_markup=kb
        )

    elif lang == 'rus':
        await message.answer(
            text=message_text,
            reply_markup=kb
        )


@router.message(Register.full_name)
async def handle_invalid_fullname(message: types.Message):
    await message.reply(
        text="Илтимос, исмингизни матн кўринишида киритинг.\nEслатма, сиз киритган матн сизнинг исмингиз сифатида сақланади"
    )
