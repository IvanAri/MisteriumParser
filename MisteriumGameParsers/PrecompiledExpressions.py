import re
from MisteriumGameParsers.SpecialWordsConstants import SPECIAL_NAMES, MAIN_CLASSES_NAMES
from MisteriumGameParsers.SpecialWordsConstants import PREREQUISITES_GAMEPLAY, PREREQUISITES_CLASS, PREREQUISITES_LEVEL,\
                                                        PREREQUISITES_LEVEL, PREREQUISITES_ABILITIES,\
                                                        PREREQUISITES_CHARACTERISTICS, PREREQUISITES_WORDS


EXPERIENCE_EXPR = re.compile('балл[а-я]+\sопыт[а-я]+', re.IGNORECASE)

class WORD_COUNT_EXPRESSIONS:
    SINGLE_NON_SPECIAL_WORD_EXPR = re.compile('[а-я]+', re.IGNORECASE)
    DOUBLE_WORD_EXPR = re.compile("[а-я]+\s[0-9а-я]+", re.IGNORECASE)

# Здесь храним выражения описывающие готовую строку, которую уже не надо обрабатывать
FINISH_EXPRESSIONS = ()
SPECIAL_WORDS_EXPRESSIONS = ()

LEVEL_EXP_EXPRESSION = re.compile('[1-9]+\sуровень\s[-]\s[0-9]+\sбал[а-я]+\sопы[а-я]+', re.IGNORECASE)
ACTIVE_ABILITY_EXPR = re.compile('активн[а-я]+\s[-]перезаряд[а-я]+\s[1-9]+]', re.IGNORECASE)
SENTENCE_EXPRESSION = re.compile("([а-я]+[()!\s,;]*)*[.!?]", re.IGNORECASE)

def makeSpecialWordsExpressions(specialWord):
    return re.compile("%s[а-я]*" % specialWord, re.IGNORECASE)

for specialWord in SPECIAL_NAMES:
    SPECIAL_WORDS_EXPRESSIONS += (
        makeSpecialWordsExpressions(specialWord),
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

PRQ_GAMEPLAY_EXPRESSION = re.compile("требуе[а-я]+\sотыгры[а-я]+", re.IGNORECASE)
PRQ_LEVEL_EXPRESSION = re.compile("требуе[а-я]+\sуров[а-я]+", re.IGNORECASE)
PRQ_CLASS_EXPRESSION = re.compile("требуе[а-я]+\sклас[а-я]+", re.IGNORECASE)
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

PRQ_EXPRESSIONS = PRQ_ABILITY_EXPRESSIONS + PRQ_CHARACTERISCTIC_EXPRESSIONS + PRQ_CLASS_EXPRESSION +\
                  PRQ_GAMEPLAY_EXPRESSION + PRQ_LEVEL_EXPRESSION

DESCRIPTION_EXPRESSION = re.compile("описан[а-я]+", re.IGNORECASE)