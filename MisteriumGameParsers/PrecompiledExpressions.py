import re
from MisteriumGameParsers.SpecialWordsConstants import SPECIAL_NAMES

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
