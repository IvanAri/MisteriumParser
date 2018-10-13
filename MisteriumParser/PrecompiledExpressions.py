import re

EXPERIENCE_EXPR = re.compile('балл[а-я]+\sопыт[а-я]+', re.IGNORECASE)
LONE_WORD_EXPR = re.compile('[а-я]+', re.IGNORECASE)


# Здесь храним выражения описывающие готовую строку, которую уже не надо обрабатывать

LEVEL_EXP_EXPRESSION = re.compile('[1-9]+\sуровень\s[-]\s[0-9]+\sбалл[а-я]+\sопыт[а-я]+', re.IGNORECASE)

FINISH_EXPRESSIONS = (
    LEVEL_EXP_EXPRESSION,
)