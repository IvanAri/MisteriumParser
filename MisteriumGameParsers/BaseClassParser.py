from collections import deque
from MisteriumGameParsers.BasicParser import BasicParser
import json

from MisteriumGameParsers.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser
# TODO: in the end we should have a data structure converted to JSon for further use

class BaseClassParser(BasicParser):
    def __init__(self):
        super(BaseClassParser, self).__init__()
        self.__classContent = {} # resulting BASIC_CLASS dict

    # In this method we do main processing
    def extractClass(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser should be provided with list of strings as rawData"

        for line in rawData:
            self.threeLineSegment.append(line)
            if len(self.threeLineSegment) == 3:
                self.beautifySegment()
        pass

    # special post pre-processing

    def beautifySegment(self):
        pass

    # TODO: i_belekhov необходимо разбить обработчики на виды "начинает с", "оканчивается этим", "совпадает с паттерном"
    STARTSWITH = (
    )

    ENDSWITH = (
    )


