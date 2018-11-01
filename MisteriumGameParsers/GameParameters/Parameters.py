from MisteriumGameParsers.PrecompiledExpressions import makeSpecialWordsExpressions,\
    make_pair_special_expression, make_triplet_special_expression, make_special_expression

# ======================================================================================================================
# Параметры. Базовая сущность, на которую аттрибут накидывает всякие уточнения и ограничения
# ======================================================================================================================

PHYSICAL_ATTACK = (
    "атак",
)
PHYSICAL_FORTITUDE = (
    "физическ си",
)
MENTAL_FORTITUDE = (
    "ментальн си",
)
MANA = (
    "запа энерги",
)

SMALL_ENERGY_USAGE = (
    "мал затра",
)
MEDIUM_ENERGY_USAGE = (
    "средн затра",
)
HIGH_ENERGY_USAGE = (
    "высок затра",
)
VERY_HIGH_ENERGY_USAGE = (
    "высш затра",
)
GLOBAL_ENERGY_USAGE = (
    "глобальн затра",
)

PARAMETERS = (
    *PHYSICAL_ATTACK,
    *PHYSICAL_FORTITUDE,
    *MENTAL_FORTITUDE,
    *MANA,
    *SMALL_ENERGY_USAGE,
    *MEDIUM_ENERGY_USAGE,
    *HIGH_ENERGY_USAGE,
    *VERY_HIGH_ENERGY_USAGE,
    *GLOBAL_ENERGY_USAGE,
)

PARAMETERS_EXPRESSIONS = ()

for parameter in PARAMETERS:
    param_list = parameter.split(" ")
    if len(param_list) == 1:
        PARAMETERS_EXPRESSIONS += (
            makeSpecialWordsExpressions(param_list[0]),
        )
    elif len(param_list) == 2:
        PARAMETERS_EXPRESSIONS += (
            make_pair_special_expression(param_list[0], param_list[1]),
        )
    elif len(param_list) == 3:
        PARAMETERS_EXPRESSIONS += (
            make_triplet_special_expression(param_list[0], param_list[1], param_list[2]),
        )
    else:
        assert "Not supported parameter"

PARAMETERS_CATEGORIES = (
    PHYSICAL_ATTACK,
    PHYSICAL_FORTITUDE,
    MENTAL_FORTITUDE,
    MANA,
    SMALL_ENERGY_USAGE,
    MEDIUM_ENERGY_USAGE,
    HIGH_ENERGY_USAGE,
    VERY_HIGH_ENERGY_USAGE,
    GLOBAL_ENERGY_USAGE,
)

PARAMETERS_CATEGORIES_EXPRESSIONS = {
    PHYSICAL_ATTACK: (),
    PHYSICAL_FORTITUDE: (),
    MENTAL_FORTITUDE: (),
    MANA: (),
    SMALL_ENERGY_USAGE: (),
    MEDIUM_ENERGY_USAGE: (),
    HIGH_ENERGY_USAGE: (),
    VERY_HIGH_ENERGY_USAGE: (),
    GLOBAL_ENERGY_USAGE: (),
}

for category in PARAMETERS_CATEGORIES_EXPRESSIONS:
    for parameter in category:
        param_list = parameter.split(" ")
        if len(param_list) == 1:
            PARAMETERS_CATEGORIES_EXPRESSIONS[category] += (
                makeSpecialWordsExpressions(param_list[0]),
            )
        elif len(param_list) == 2:
            PARAMETERS_CATEGORIES_EXPRESSIONS[category] += (
                make_pair_special_expression(param_list[0], param_list[1]),
            )
        elif len(param_list) == 3:
            PARAMETERS_CATEGORIES_EXPRESSIONS[category] += (
                make_triplet_special_expression(param_list[0], param_list[1], param_list[2]),
            )
        else:
            assert "Not supported parameter"

PARAMETERS_ALIASES = {
    PHYSICAL_ATTACK: "physical attack",
    PHYSICAL_FORTITUDE: "physical fortitude",
    MENTAL_FORTITUDE: "mental fortitude",
    MANA: "mana",
    SMALL_ENERGY_USAGE: "small energy usage",
    MEDIUM_ENERGY_USAGE: "medium energy usage",
    HIGH_ENERGY_USAGE: "high energy usage",
    VERY_HIGH_ENERGY_USAGE: "very high energy usage",
    GLOBAL_ENERGY_USAGE: "global energy usage",
}

# ======================================================================================================================
# Специализаторы параметра. Уточнения, к какой именно части параметра относится значение аттрибута
# ======================================================================================================================

SPEED_MODIFIER = "скорость"
STRENGTH_MODIFIER = "сила"

MAX = "максимальный"
CURRENT = "текущий"

ALL_MODIFIERS = (
    SPEED_MODIFIER,
    STRENGTH_MODIFIER,
    MAX,
    CURRENT,
)

PARAMETERS_MODIFIERS = {
    PHYSICAL_ATTACK: (
        SPEED_MODIFIER,
        STRENGTH_MODIFIER,
    ),
}

