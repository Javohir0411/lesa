from utils.enums import LanguageEnum, ProductTypeEnum


class ProductStrings:
    PRODUCT_TRANSLATION = {
        LanguageEnum.uzl.name: {
            ProductTypeEnum.lesa.name: "Lesa",
            ProductTypeEnum.monolit.name: "Monolit stoyka",
            ProductTypeEnum.taxta.name: "Taxta",
        },

        LanguageEnum.uzk.name: {
            ProductTypeEnum.lesa.name: "Леса",
            ProductTypeEnum.monolit.name: "Монолит стойка",
            ProductTypeEnum.taxta.name: "Тахта",
        },

        LanguageEnum.rus.name: {
            ProductTypeEnum.lesa.name: "Леса",
            ProductTypeEnum.monolit.name: "Монолитная стойка",
            ProductTypeEnum.taxta.name: "Доска"
        }
    }

