import re
from MisteriumGameParsers.SpecialWordsConstants import SPECIAL_NAMES_FOR_BASIC_PARSER, MAIN_CLASSES_NAMES, CHARACTERISTICS
from MisteriumGameParsers.SpecialWordsConstants import PREREQUISITES_GAMEPLAY, PREREQUISITES_CLASS, PREREQUISITES_LEVEL,\
                                                        PREREQUISITES_LEVEL, PREREQUISITES_ABILITIES,\
                                                        PREREQUISITES_CHARACTERISTICS, PREREQUISITES_WORDS,\
                                                        NOT_EXACT_ABILITY_NAMES
from MisteriumGameParsers.SpecialWordsConstants import TECHNICAL_SINGLE_WORDS


EXPERIENCE_EXPR = re.compile('балл[а-я]+\sопыт[а-я]+', re.IGNORECASE)

class WORD_COUNT_EXPRESSIONS:
    SINGLE_NON_SPECIAL_WORD_EXPR = re.compile('[а-я]+', re.IGNORECASE)
    DOUBLE_WORD_EXPR = re.compile("[а-я]+\s[0-9а-я]+", re.IGNORECASE)
    DOUBLE_EXPR = re.compile("([а-я]+\s)*[-]\s([0-9а-я]+(\s)*)*", re.IGNORECASE)

# Здесь храним выражения описывающие готовую строку, которую уже не надо обрабатывать
FINISH_EXPRESSIONS = ()
SPECIAL_WORDS_EXPRESSIONS = ()
CHARACTERISTIC_EXPRESSIONS = ()
TECHNICAL_WORDS_EXPRESSIONS = ()

LEVEL_EXP_EXPRESSION = re.compile('[1-9]+\sуровень\s[-]\s[0-9]+\sбал[а-я]+\sопы[а-я]+', re.IGNORECASE)
ACTIVE_ABILITY_EXPR = re.compile('активн[а-я]+\s[-]перезаряд[а-я]+\s[1-9]+]', re.IGNORECASE)
SENTENCE_EXPRESSION = re.compile("([а-я]+[()!\s,;]*)*[.!?]", re.IGNORECASE)
PROCENT_EXPRESSION = re.compile("^[1-9][0-9]+%")

def makeSpecialWordsExpressions(specialWord):
    return re.compile("%s[а-я]*" % specialWord, re.IGNORECASE)

def make_pair_special_expression(word1, word2):
    return re.compile("%s[а-я]+[,]*\s%s[а-я]+[.,!?]*" % (word1, word2), re.IGNORECASE)

def make_triplet_special_expression(word1, word2, word3):
    return re.compile("%s[а-я]+[,]*\s%s[а-я]+[,]*\s%s[а-я]+[.,!?]*" % (word1, word2, word3), re.IGNORECASE)

def make_special_expression(special_string):
    special_words_list = special_string.split(" ")
    result = None
    if len(special_words_list) == 1:
        result = makeSpecialWordsExpressions(special_words_list[0])
    elif len(special_words_list) == 2:
        result = make_pair_special_expression(special_words_list[0], special_words_list[1])
    elif len(special_words_list) == 3:
        result = make_triplet_special_expression(special_words_list[0], special_words_list[1], special_words_list[2])
    else:
        assert "Not supported parameter"
    return result

for specialWord in SPECIAL_NAMES_FOR_BASIC_PARSER:
    SPECIAL_WORDS_EXPRESSIONS += (
        makeSpecialWordsExpressions(specialWord),
    )

for special_word in CHARACTERISTICS:
    CHARACTERISTIC_EXPRESSIONS += (
        makeSpecialWordsExpressions(special_word),
    )

for special_word in TECHNICAL_SINGLE_WORDS:
    TECHNICAL_WORDS_EXPRESSIONS += (
        makeSpecialWordsExpressions(special_word),
    )

FINISH_EXPRESSIONS += SPECIAL_WORDS_EXPRESSIONS

FINISH_EXPRESSIONS += (
    LEVEL_EXP_EXPRESSION,
    ACTIVE_ABILITY_EXPR,
    # SENTENCE_EXPRESSION
)

# отсюда идёт обработка для базовых классов

CLASS_NAME_EXPRESSIONS = ()

for specialWord in MAIN_CLASSES_NAMES:
    CLASS_NAME_EXPRESSIONS += (
        makeSpecialWordsExpressions(specialWord),
    )

# prerequisites expression

PRQ_GAMEPLAY_EXPRESSION = re.compile("требуе[а-я]+\sотыгры[а-я]+", re.IGNORECASE)
PRQ_LEVEL_EXPRESSION = re.compile("требуе[а-я]+\sуров[а-я]+", re.IGNORECASE)
PRQ_CLASS_EXPRESSION = re.compile("требуе[а-я]+\sклас[а-я]+", re.IGNORECASE)
PRQ_GENDER_EXPRESSION = re.compile("требуе[а-я]+\sпо[а-я]+", re.IGNORECASE)
PRQ_CHARACTERISCTIC_EXPRESSIONS = ()
PRQ_ABILITY_EXPRESSIONS = ()

def makePrerequisitesExpressions(specialWord):
    return re.compile("требуе[а-я]+\s%s[а-я]+" % specialWord, re.IGNORECASE)

for specialWord in PREREQUISITES_CHARACTERISTICS:
    PRQ_CHARACTERISCTIC_EXPRESSIONS += (
        makePrerequisitesExpressions(specialWord),
    )

for specialWord in PREREQUISITES_ABILITIES:
    PRQ_ABILITY_EXPRESSIONS += (
        makePrerequisitesExpressions(specialWord),
    )

PRQ_EXPRESSIONS = PRQ_ABILITY_EXPRESSIONS + PRQ_CHARACTERISCTIC_EXPRESSIONS + (PRQ_CLASS_EXPRESSION,) +\
                  (PRQ_GAMEPLAY_EXPRESSION,) + (PRQ_LEVEL_EXPRESSION,) + (PRQ_GENDER_EXPRESSION,)

# a bit of stage start expressions

DESCRIPTION_START_EXPRESSION = re.compile("описан[а-я]+", re.IGNORECASE)
CLASS_ATTRIBUTES_START_EXPRESSION = re.compile("дополнит[а-я]+\sсвойс[а-я]+", re.IGNORECASE)
CLASS_ABILITIES_START_EXPRESSION = re.compile("доступ[а-я]+\sнавы[а-я]+", re.IGNORECASE)

# attribute expressions

# abilities expressions

NOT_EXACT_ABILITIES_EXPRESSIONS = ()

for abilitiy_name in NOT_EXACT_ABILITY_NAMES:
    NOT_EXACT_ABILITIES_EXPRESSIONS += (
        make_special_expression(abilitiy_name),
    )