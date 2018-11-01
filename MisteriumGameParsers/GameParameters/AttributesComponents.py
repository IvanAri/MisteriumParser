import re
from MisteriumGameParsers.GameParameters import Parameters
from MisteriumGameParsers.PrecompiledExpressions import makeSpecialWordsExpressions

# Общая логика такова:
# Аттрибут состоит изо всех или некоторых компонентов:
# Game action - игрового действия. То есть аттрибут применим лишь к этому действию и никак иначе.
# Game action modifier or specifier - уточнение игрового действия. То есть аттрибут применим лишь к действию, которое
# связано с определённым игровым объектом.
# Game action impact - влияние игрового действия. То влияние, которое оказывает совершение игрового действия, например
# истощение после применения техник или приёмов.
# Sign - знак параметра игрового действия. То есть уменьшение или увеличение
# параметра, связанного с вышеописанными частями.
# Parameter - собственно параметр, описываемый в сложносоставном аттрибуте.
# Value - численное значение параметра. И добавить нечего, часто выражается в процентах.
# Nature - природа аттрибута, то есть является он аддитивным или мультипликативным. Эту штуку надо проставлять руками.
# Specialization - специализация параметра. Есть далеко не всегда, но некоторые параметры
# имеют подвиды и их надо учитывать. Пример - типы затрат маны или параметры отдельно взятого типа заклинаний.

# ======================================================================================================================
# Игровые действия или нечто схожее с действием, квалификаторы действия
# ======================================================================================================================
WIELDING = (
    "влад",
)

USING = (
    "примен",
    "использ",
)

STRIKE = (
    "уда",

)

KNOWING = (
    "зна",
)

SPELL_CASTING = (
    "заклятия-выстре",
    "заклятия, накладываемые на область",
)

GAME_ACTIONS = (
    *WIELDING,
    *USING,
    *STRIKE,
    *KNOWING,
)

GAME_ACTIONS_CATEGORIES = (
    WIELDING,
    USING,
    STRIKE,
    KNOWING,
    SPELL_CASTING
)

GAME_ACTIONS_CATEGORIES_EXPRESSIONS = {
    WIELDING: (),
    USING: (),
    STRIKE: (),
    KNOWING: (),
    SPELL_CASTING: (),
}

for category in GAME_ACTIONS_CATEGORIES:
    for game_action in category:
        GAME_ACTIONS_CATEGORIES_EXPRESSIONS[category] += (
            makeSpecialWordsExpressions(game_action),
        )

GAME_ACTIONS_ALIASES = {
    WIELDING: "wielding",
    USING: "using",
    STRIKE: "strike",
    KNOWING: "knowing",
}

GAME_ACTIONS_EXPRESSIONS = ()

for game_action in GAME_ACTIONS:
    GAME_ACTIONS_EXPRESSIONS += (
        makeSpecialWordsExpressions(game_action),
    )

# ======================================================================================================================
# Модификаторы и спецификаторы игровых действий. То есть такие слова и выражения, которые уточняют игровое действие
# ======================================================================================================================

WEAPON = (
    "оруж",
)

METHOD = (
    "приё",
)

MAGIC = (
    "заклина",
    "маги",
)

GAME_ACTIONS_MODIFIERS = {
    WIELDING: (
        *WEAPON,
    ),
    USING: (
        *METHOD,
        *MAGIC,
    ),
    KNOWING: (
        *MAGIC,
    ),
}

ALL_GAME_ACTIONS_MODIFIERS = (
    *WEAPON,
    *METHOD,
    *MAGIC,
)

GAME_ACTIONS_MODIFIERS_EXPRESSIONS = ()

for game_action_modifier in ALL_GAME_ACTIONS_MODIFIERS:
    GAME_ACTIONS_MODIFIERS_EXPRESSIONS += (
        makeSpecialWordsExpressions(game_action_modifier),
    )

GAME_ACTIONS_MODIFIERS_CATEGORIES = (
    WEAPON,
    METHOD,
    MAGIC
)

GAME_ACTIONS_MODIFIERS_CATEGORIES_EXPRESSIONS = {
    WEAPON: (),
    METHOD: (),
    MAGIC: (),
}

for category in GAME_ACTIONS_MODIFIERS_CATEGORIES:
    for game_action_modifier in category:
        GAME_ACTIONS_MODIFIERS_CATEGORIES_EXPRESSIONS[category] += (
            makeSpecialWordsExpressions(game_action_modifier),
        )

GAME_ACTIONS_MODIFIERS_ALIASES = {
    WEAPON: "weapon",
    METHOD: "method",
    MAGIC: "magic",
}

# ======================================================================================================================
# Модификатор воздействия некоторого игрового действия. То есть нечто совершённое со спецификатором игрового действия
# ======================================================================================================================

TAKES = (
    "забира",
)

GAME_ACTION_IMPACT = {
    WIELDING: (
        *TAKES,
    ),
    USING: (
        *TAKES,
    ),
    SPELL_CASTING: (
        *TAKES,
    ),
}

ALL_GAME_ACTIONS_IMPACTS = (
    *TAKES,
)

GAME_ACTIONS_IMPACTS_EXPRESSIONS = ()

for game_action_impact in ALL_GAME_ACTIONS_IMPACTS:
    GAME_ACTIONS_IMPACTS_EXPRESSIONS += (
        makeSpecialWordsExpressions(game_action_impact),
    )

GAME_ACTIONS_IMPACTS_CATEGORIES = (
    TAKES,
)

GAME_ACTIONS_IMPACTS_CATEGORIES_EXPRESSIONS = {
    TAKES: (),
}

for category in GAME_ACTIONS_IMPACTS_CATEGORIES:
    for game_action_impact in category:
        GAME_ACTIONS_IMPACTS_CATEGORIES_EXPRESSIONS[category] += (
            makeSpecialWordsExpressions(game_action_impact),
        )

GAME_ACTIONS_IMPACTS_ALIASES = {
    TAKES: "takes",
}

# ======================================================================================================================
# Квалификаторы знака. Если они отсутствуют, то считается, что знак "+"
# ======================================================================================================================

POSITIVE = (
    'повышае',
    'пребавляе',
    'увеличивае',
    'больш'
)

NEGATIVE = (
    'понижае',
    'отнимае',
    'уменьшае',
    'мен',
    'снижен'
)

ALL_SIGN_QUALIFIERS = (
    *POSITIVE,
    *NEGATIVE,
)

SIGN_QUALIFIERS_EXPRESSIONS = ()

for sign_qualifier in ALL_SIGN_QUALIFIERS:
    SIGN_QUALIFIERS_EXPRESSIONS += (
        makeSpecialWordsExpressions(sign_qualifier),
    )

SIGN_QUALIFIERS_CATEGORIES = (
    POSITIVE,
    NEGATIVE,
)

SIGN_QUALIFIERS_CATEGORIES_EXPRESSIONS = {
    POSITIVE: (),
    NEGATIVE: (),
}

for category in SIGN_QUALIFIERS_CATEGORIES:
    for sign_qualifier in category:
        SIGN_QUALIFIERS_CATEGORIES_EXPRESSIONS[category] += (
            makeSpecialWordsExpressions(sign_qualifier),
        )

SIGN_QUALIFIERS_ALIASES = {
    POSITIVE: "+",
    NEGATIVE: "-",
}



