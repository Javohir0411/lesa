from utils.enums import LanguageEnum, ProductTypeEnum, LesaSizeEnum
from aiogram.utils import markdown


class RentStrings:
    RENT_STARTING_PROCESS = {
        LanguageEnum.uzl.name:
            "Unday bo'lsa, ijaraga berish jarayonini boshlaymiz.\n"
            "Quyidan, ijaraga bermoqchi bo'lgan mahsulotingizni tanlang",

        LanguageEnum.uzk.name:
            "Ундай бўлса, ижарага бериш жараёнини бошлаймиз.\n"
            "Қуйидан, ижарага бермоқчи бўлган маҳсулотингизни танланг",

        LanguageEnum.rus.name:
            "Затем мы начнем процесс аренды.\n"
            "Ниже выберите товар, который хотите арендовать."
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