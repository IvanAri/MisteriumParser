# parameters
PHYSICAL_ATTACK = (
    "атака",
)
PHYSICAL_FORTITUDE = (
    "физические силы",
)
MENTAL_FORTITUDE = (
    "ментальные силы",
)
MANA = (
    "запас энергии",
)

SMALL_ENERGY_USAGE = (
    "малая затрата",
)
MEDIUM_ENERGY_USAGE = (
    "средняя затрата",
)
HIGH_ENERGY_USAGE = (
    "высокая затрата",
)
VERY_HIGH_ENERGY_USAGE = (
    "высшая затрата",
)
GLOBAL_ENERGY_USAGE = (
    "глобальная затрата",
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