from utils.enums import LanguageEnum
from aiogram.utils import markdown


class StartStrings:
    SELECT_LANGUAGE = {
        LanguageEnum.uzl.name:
            f"Yaxshi, demak sizga botning interfeysini {markdown.hbold(LanguageEnum.uzl.value)} tilida taqdim etaman\n\n"
            "Iltimos, endi to'liq ism-familiyangizni kiriting (masalan, Ali Valiyev):\n\n"
            "Eslatma! Siz kiritgan matn ismingiz sifatida tanlanadi.",

        LanguageEnum.uzk.name:
            f"Яхши, демак сизга ботнинг интерфейсини {markdown.hbold(LanguageEnum.uzk.value)} да тақдим этаман\n\n"
            f"Илтимос, энди тўлиқ исм-фамилиянгизни киритинг(масалан, Али Валиев): \n\n"
            f"Эслатма! Сиз киритган матн исмингиз сифатида танланади.",

        LanguageEnum.rus.name:
            f"Хорошо, тогда я покажу вам интерфейс бота на {markdown.hbold(LanguageEnum.rus.value)}\n\n"
            f"Теперь, пожалуйста, введите ваше полное имя (например, Али Валиев): \n\n"
            f"Напоминание! Введенный вами текст будет выделен в качестве вашего имени.",
    }

    GET_USER_FULLNAME = {
        LanguageEnum.uzl.name:
            "{user_fullname}, siz bilan tanishganimdan xursandman,\n"
            "Iltimos, endi telefon raqamni kiriting:",

        LanguageEnum.uzk.name:
            "{user_fullname}, сиз билан танишганимдан хурсандман,\n"
            "Илтимос, энди телефон рақамни киритинг:",

        LanguageEnum.rus.name:
            "{user_fullname}, рад встрече,\n"
            "Введите свой номер телефона прямо сейчас:"
    }

    GET_PHONE_NUMBER = {
        LanguageEnum.uzl.name:
            "Ma'lumotlaringiz saqlandi:\n\n"
            "Ismingiz: {user_fullname}\n"
            "Telefon raqamingiz: {user_phone_number}",

        LanguageEnum.uzk.name:
            "Маълумотларингиз сақланди:\n\n"
            "Исмингиз: {user_fullname}\n"
            "Телефон рақамингиз: {user_phone_number}",

        LanguageEnum.rus.name:
            "Ваши данные сохранены:\n\n"
            "Ваше имя: {user_fullname}\n"
            "Ваш номер телефона: {user_phone_number}",

    }

    GET_INVALID_PHONE_NUBER = {
        LanguageEnum.uzl.name: "Iltimos, pastdagi tugmani bosing!",
        LanguageEnum.uzk.name: "Илтимос, пастдаги тугмани босинг!",
        LanguageEnum.rus.name: "Пожалуйста, нажмите кнопку ниже!",
    }

    EXISTING_USER = {
        LanguageEnum.uzl.name: "❗ Siz avval ro‘yxatdan o‘tgansiz.",
        LanguageEnum.uzk.name: "❗ Сиз аввал рўйхатдан ўтгансиз.",
        LanguageEnum.rus.name: "❗ Вы уже зарегистрированы.",
    }
