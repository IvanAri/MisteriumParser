# Без последней буквы т.к. последнюю букву отрабатывает соответствующий regexp
# на случай опечаток или использований в тексте
MAIN_CLASSES_NAMES = (
    "солдат",
    "адепт",
    "маг",
    "волшебник",
    "разведчик",
    "воин",
    "чародей",
    "мистик",
    "шаман",
    "заклинатель",
    "рыцарь",
    "знаменосец",
    "боец",
    "следопыт",
    "убийца",
    "архимаг",
    "мастер рун",
    "магистр",
    "элементалист",
    "медиум",
    "ассасин",
    "снайпер",
    "егерь",
    "монстроборец",
    "командир",
    "берсерк",
    "чемпион",
    "святой рыцарь",
    "черный рыцарь",
    "богатырь"
)

# Без последней буквы т.к. последнюю букву отрабатывает соответствующий regexp
# на случай опечаток или использований в тексте
NOT_EXACT_ABILITY_NAMES = (
    # солдат
    "боевой ду",
    "боевая реакци",
    "безоружный рукопашный бо",
    # адепт
    "волшебная ясност",
    "управление потокам",
    "всплеск эфир",
    # маг
    "уплотнение эфир",
    "удержание закляти",
    "всплеск дар",
    # волшебник
    "переплетение осно",
    "подпитка щито",
    "мистический магни",
    # разведчик
    "быстрый бе",
    "проворност",
    "быстрый боевой стил",
    "бдительност",
    # воин
    "боевая выносливост",
    "рыво",
    "силовой боевой стил",
    "стойкост",
    # чародей
    "чистая мощ",
    "ментальный жес",
    "рвение сил",
    "иссушение эфир",
    # Мистик
    "магическое отрицани",
    "мастерство абсорбци",
    "мистическая теплот",
    "захват контрол",
    # Шаман
    "мастерство призыв",
    "ментальное слов",
    "помощь духо",
    "духовный призы",
    # Заклинатель
    "владение магие",
    "ментальное сосредоточени",
    "уплотнение маги",
    # Рыцарь
    "оболочка дух",
    "оболочка вол",
    "защитный боевой стил",
    "наско",
    # Знаменосец
    "командный ду",
    "сила единени",
    "рог пробуждени",
    "стремление к жизн",
    # Боец
    "кулак дух",
    "дубленая кож",
    "атакующий боевой стил",
    "стремительный прыжо",
    # Следопыт
    "град ударо",
    "мастерство уклонени",
    "точност",
    # Убийца
    "разител",
    "сосредоточенное стремлени",
    "убийств",
    "решающий момен",
    # Архимаг
    "единство со стихие",
    "фильтрация эфир",
    "высшая маги",
    "мистическая печат",
    "подавление сило",
    # Мастер рун
    "возгорание ру",
    "фильтрация эфир",
    "эфирное выжиган",
    "мистическое единени",
    "стихийное сердц",
    # Магистр
    "энергетическая аур",
    "внутренний пото",
    "великая медитаци",
    # Элементалист
    "познание первоосно",
    "волшебный кана",
    "управление элементам",
    # Ассасин
    "дух затаившегося зме",
    "молниеносност",
    "танец смерт",
    "стремительная изворотливост",
    # Снайпер
    "разящий выстре",
    "духовные стрел",
    "невероятная меткост",
    "помощь ветро",
    # Егерь
    "единство с природо",
    "партизанский ду",
    "ускоренное стремлени",
    "прицельный выстре",
    # Монстроборец
    "болевая точк",
    "бесстраши",
    "великая охот",
    "неизлечимая ран",
    "пробивной уда",
    "ярый бросо",
    # Командир
    "командное стремлени",
    "подавление магии духо",
    "мастерство сражени",
    "крик императорской стал",
    # Берсерк
    "безумный натис",
    "жажда бо",
    "режим берсерк",
    # Чемпион
    "превосходств",
    "активный бло",
    "мастерский боевой стил",
    "акцент мастер",
    # Святой рыцарь
    "непоколебимая вер",
    "божественное вдохновени",
    "оболочка вер",
    "священная клятв",
    # Черный рыцарь
    "несущий смерт",
    "темный чемпио",
    "рывок смерт",
    "призрачный ме",
    "угнетени",
    # Богатырь
    "богатырская сил",
    "пограничный стра",
    "боевая импровизаци",
    "могучий взма",
    # Медиум
    "идеальный контрол",
    "путь в утопию духо",
    "покровительство хранител",
)

NON_EXACT_SOCIAL_ABILITY_NAMES = (
    # добыча сырья
    "рубка лес",
    "добыча камн",
    "добыча металл",
    "охотни",
    "собирател",
    "рыба",
    "ферме",
    "садово",
    "скотово",
    "травни",
    "старател",
    "собиратель энерги"
    # ремесло и производство
    "плотни",
    "резчи",
    "строител",
    "кузне",
    "оружейни",
    "кожевни",
    "тка",
    "портно",
    "пова",
    "ювели",
    "парфюме",
    "алхими",
    "руническое дел",
    "инжене",
    "гонча",
    # наука и знания
    "грамотност",
    "ботани",
    "зоологи",
    "монстрологи",
    "астрономи",
    "географи",
    "картографи",
    "криптографи",
    "археологи",
    "математик",
    "истори",
    "литератур",
    "экономи",
    "анатоми",
    "дипломати",
    "закон",
    "религи",
    "мистик",
    "спектрологи",
    "эфирологи",
    "психологи",
    "этике",
    "некрологи",
    "демонологи",
    # социальные, культурные и прочие
    "лекар",
    "бар",
    "танц",
    "музыкан",
    "акте",
    "торгове",
    "управляющи",
    "охранни",
    "пала",
    "художни",
    "моря",
    "дрессировщи",
    "цирюльни",
    # спортивные
    "акробатик",
    "легкая атлетик",
    "тяжелая атлетик",
    "скольжени",
    "плавани",
    "балан",
    # ориентирование на местности
    "ориентирование в лес",
    "альпиниз",
    "знание боло",
    "знание пустын",
    "знание тундр",
    "знание пеще",
    "маскировка на местност",
    # особые умения
    "верховая езд",
    "ораторств",
    "лидерств",
    "тактик",
    "использование тяжелой брон",
    "бле",
    "добродуши",
    "мужественност",
    "очаровани",
    "концентрация внимани",
    "ловкость ру",
    "запугивани",
    "взло",
    "чтение следо",
    "мастерство ловуше",
    "маскировка в город",
    # знание языков
    "наречие синдарин",
    "наречие нур",
    "ашрэфи",
    "ману",
    "язык гномов",
    "язык вифрэев",
    "язык архонов",
    "язык орков",
    "эредан",
    "язык драконов",
    "калимаг"
)

TECHNICAL_SINGLE_WORDS = (
    "пассивн",
    "активн",
    "описан",
    "муж",
    "жен"
)

CHARACTERISTICS = (
    "сила",
    "ловкость",
    "выносливость",
    "живучесть",
    "одарённость"
)

# PREREQUISITES

PREREQUISITES_CHARACTERISTICS = (
    "сил",
    "ловкост",
    "выносливост",
    "живучест",
    "одарённост",
)

PREREQUISITES_ABILITIES = (
    "способност",
    "навы",
)

PREREQUISITES_LEVEL = (
    "урове"
)

PREREQUISITES_CLASS = (
    "клас",
)

PREREQUISITES_GAMEPLAY = (
    "отыгры"
)

PREREQUISITES_WORDS = PREREQUISITES_CHARACTERISTICS + PREREQUISITES_ABILITIES +\
                      (PREREQUISITES_LEVEL,) + (PREREQUISITES_CLASS,) + (PREREQUISITES_GAMEPLAY,)

SPECIAL_NAMES_FOR_BASIC_PARSER = MAIN_CLASSES_NAMES + NOT_EXACT_ABILITY_NAMES + TECHNICAL_SINGLE_WORDS