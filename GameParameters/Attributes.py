# TODO: Далендор, глядь сюда. Здесь памятка о том как нужно их заполнять
# Писать стоит неполные названия, т.к. используя их в регулярках можно будет получить разные окончания.
# Например: сила атак - сила атаки, сила удара - сила ударов и так далее

# TODO: НЕТОЧНЫЕ НАЗВАНИЯ ПЕРЕНЕСТИ В ПАРСЕР I_belekhov
# TODO: НЕ ЗАБЫТЬ СДЕЛАТЬ ТОЧНЫЕ НАЗВАНИЯ ДЛЯ КОНВЕРСИИ И ПРИМЕНЕНИЯ В ТАБЛИЦАХ, СРАЗУ НА ДВУХ ЯЗЫКАХ

# Physical section

PHYSICAL_ATTACK_ATTRIBUTES_NAMES = (
    "сила атак",
)

PHYSICAL_DEFENCE_ATTRIBUTES_NAMES = (

)
# Magic section

MAGIC_ATTACK_ATTRIBUTES_NAMES = (

)

MAGIC_DEFENCE_ATTRIBUTES_NAMES = (

)

MAGIC_ATTRIBUTES_NAMES = MAGIC_ATTACK_ATTRIBUTES_NAMES + MAGIC_DEFENCE_ATTRIBUTES_NAMES

# Resists

RESISTS_NAMES = (

)

ATTRIBUTES_NAMES = ()

class ATTRIBUTE:

    def __init__(self, **kwargs):
        pass