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


"""
    PRODUCT_TRANSLATION = {
        ProductTypeEnum.lesa.name: {
            LanguageEnum.uzl.name: "Lesa",
            LanguageEnum.uzk.name: "Леса",
            LanguageEnum.rus.name: "Леса"
        },

        ProductTypeEnum.monolit.name: {
            LanguageEnum.uzl.name: "Monolit stoyka",
            LanguageEnum.uzk.name: "Монолит стойка",
            LanguageEnum.rus.name: "Монолитная стойка"
        },

        ProductTypeEnum.taxta.name: {
            LanguageEnum.uzl.name: "Taxta",
            LanguageEnum.uzk.name: "Тахта",
            LanguageEnum.rus.name: "Доска"
        },
    }
"""
