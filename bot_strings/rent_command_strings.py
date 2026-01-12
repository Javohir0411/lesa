from utils.enums import LanguageEnum, ProductTypeEnum, LesaSizeEnum, LocationTypeEnum


class RentStrings:
    RENT_STARTING_PROCESS = {
        LanguageEnum.uzl.name:
            "Unday bo'lsa, ijaraga berish jarayonini boshlaymiz.\n"
            "Quyidan, ijaraga bermoqchi bo'lgan mahsulotingizni tanlang\n\n",

        LanguageEnum.uzk.name:
            "Ундай бўлса, ижарага бериш жараёнини бошлаймиз.\n"
            "Қуйидан, ижарага бермоқчи бўлган маҳсулотингизни танланг\n\n",

        LanguageEnum.rus.name:
            "Затем мы начнем процесс аренды.\n"
            "Ниже выберите товар, который хотите арендовать.\n\n"
    }

    CHOOSE_PRODUCT_KEYBOARD = {
        LanguageEnum.uzl.name: {
            ProductTypeEnum.lesa.name: {
                LesaSizeEnum.katta.name: "Lesa Katta",
                LesaSizeEnum.orta.name: "Lesa O'rta",
                LesaSizeEnum.kichik.name: "Lesa Kichik",
            },

            ProductTypeEnum.monolit.name: "Monolit stoyka",
            ProductTypeEnum.taxta.name: "Taxta",
        },

        LanguageEnum.uzk.name: {
            ProductTypeEnum.lesa.name: {
                LesaSizeEnum.katta.name: "Леса Катта",
                LesaSizeEnum.orta.name: "Леса Ўрта",
                LesaSizeEnum.kichik.name: "Леса Кичик",
            },

            ProductTypeEnum.monolit.name: "Монолит стойка",
            ProductTypeEnum.taxta.name: "Тахта",
        },

        LanguageEnum.rus.name: {
            ProductTypeEnum.lesa.name: {
                LesaSizeEnum.katta.name: "Большая Леса",
                LesaSizeEnum.orta.name: "Средняя Леса",
                LesaSizeEnum.kichik.name: "Маленькая Леса",
            },

            ProductTypeEnum.monolit.name: "Монолитный стенд",
            ProductTypeEnum.taxta.name: "Доска",
        },
    }

    SELECT_INVALID_PRODUCT = {
        LanguageEnum.uzl.name: "Iltimos, quyidan kerakli mahsulotni birini tanlang!",
        LanguageEnum.uzk.name: "Илтимос, қуйидан керакли маҳсулотни бирини танланг!",
        LanguageEnum.rus.name: "Пожалуйста, выберите нужный вам товар ниже!",
    }

    INSERT_QUANTITY_PRODUCT = {
        LanguageEnum.uzl.name: "Kerakli miqdorni kiriting: ⬇️",
        LanguageEnum.uzk.name: "Керакли миқдорни киритинг: ⬇️",
        LanguageEnum.rus.name: "Введите необходимое количество: ⬇️",
    }

    LESA_SIZE_TRANSLATION = {
        "uzl": {
            LesaSizeEnum.katta.name: "Katta",
            LesaSizeEnum.orta.name: "O'rta",
            LesaSizeEnum.kichik.name: "Kichik",
        },
        "uzk": {
            LesaSizeEnum.katta.name: "Катта",
            LesaSizeEnum.orta.name: "Ўрта",
            LesaSizeEnum.kichik.name: "Кичик",
        },
        "rus": {
            LesaSizeEnum.katta.name: "Большой",
            LesaSizeEnum.orta.name: "Середина",
            LesaSizeEnum.kichik.name: "Маленький",
        }
    }

    INSERT_INVALID_SIZE = {
        "uzl": "Iltimos, quyidan kerakli hajmni tanlang!",
        "uzk": "Илтимос, қуйидан керакли ҳажмни танланг!",
        "rus": "Пожалуйста, выберите необходимый размер ниже!",
    }

    CHOOSE_ANOTHER_PRODUCT = {
        "uzl": "Yana qo'shmoqchi bo'lgan mahsulotingizni belgilang: \n\n",
        "uzk": "Яна қўшмоқчи бўлган маҳсулотингизни белгиланг: \n\n",
        "rus": "Выберите товар, который хотите добавить: \n\n",
    }

    YES_NO_TEXT = {
        "uzl": {"yes": "Ha", "no": "Yo‘q"},
        "uzk": {"yes": "Ха", "no": "Йўқ"},
        "rus": {"yes": "Да", "no": "Нет"},
    }

    ASK_RENTER_FULLNAME = {
        "uzl": "Yaxshi, endi navbatda, ijaraga oluvchining ism va familiyasini kiriting(masalan, Ali Valiyev): ",
        "uzk": "Яхши, энди навбатда, ижарага олувчининг исм ва фамилиясини киритинг(масалан, Али Валиев):",
        "rus": "Хорошо, теперь введите имя и фамилию арендатора (например, Али Валиев):",
    }

    INVALID_YES_NO = {
        "uzl": "Iltimos, javobingizni quyidagi tugmalar orqali bering⬇️",
        "uzk": "Илтимос, жавобингизни қуйидаги тугмалар орқали беринг⬇️",
        "rus": "Пожалуйста, ответьте, используя кнопки ниже⬇️",
    }

    GET_RENT_START_DATE = {
        "uzl": "Ijarani boshlanish sanasini kiriting <b>(DD.MM.YYYY)</b>: ",
        "uzk": "Ижарани бошланиш санасини киритинг <b>(ДД.ММ.ЙЙЙЙ)</b>: ",
        "rus": "Введите дату начала аренды <b>(ДД.ММ.ГГГГ)</b>:",
    }

    GET_RENT_END_DATE = {
        "uzl": "Ijarani tugash sanasini ham kiriting <b>(DD.MM.YYYY)</b>: ",
        "uzk": "Ижарани тугаш санасини ҳам киритинг <b>(ДД.ММ.ЙЙЙЙ)</b>: ",
        "rus": "Также укажите дату окончания аренды <b>(ДД.ММ.ГГГГ)</b>: ",
    }

    ASK_LOCATION_TYPE = {
        "uzl": "Joylashuvni qaysi ko'rinishda yuborasiz?",
        "uzk": "Жойлашувни қайси кўринишда юборасиз?",
        "rus": "В каком формате вы отправляете местоположение?",
    }

    LOCATION_KB_TRANSLATION = {
        "uzl": {
            LocationTypeEnum.map.name: "Xarita📍",
            LocationTypeEnum.text.name: "Matn📝",
        },
        "uzk": {
            LocationTypeEnum.map.name: "Харита📍",
            LocationTypeEnum.text.name: "Матн📝",
        },
        "rus": {
            LocationTypeEnum.map.name: "Карта📍",
            LocationTypeEnum.text.name: "Текст📝",
        },
    }
