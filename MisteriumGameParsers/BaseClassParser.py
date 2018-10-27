from collections import deque
from MisteriumGameParsers.BasicParser import BasicParser
from MisteriumGameParsers.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS
from DataStructures.ClassDataStructure import BASIC_CLASS
from DataStructures.AbilityDataStructure import ABILITY
from DataStructures.Utilities import LEVEL, PREREQUISITES

import json

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser
# TODO: in the end we should have a data structure converted to JSon for further use

class BaseClassParser(BasicParser):
    def __init__(self):
        super(BaseClassParser, self).__init__()
        self.__gameClass = BASIC_CLASS() # resulting BASIC_CLASS dict
        self.__text = [] # resulting list of prepared lines if needed
        self.__currentLineIndex = 0 # index of the line that we are currently processing
        self.__buffer = [] # list of strings that we gathered for processing

    # processing

    def extractClass(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser extractClass should be provided with list of strings as rawData"

        for line in rawData:
            self.threeLineSegment.append(line)
            if len(self.threeLineSegment) == 3:
                self.beautifySegment()
        pass

    def process(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser process should be provided with list of strings as rawData"

        for line in rawData:
            self.__currentLineIndex = rawData.index(line)
            self.processLine(line)
            self.__text.append(line)
        self.show_buffer()
        self.__text.clear()

    pass

    def show_buffer(self):
        for line in self.__text:
            print(line)

    def beautifySegment(self):
        pass

    def classNameHandler(self, line):
        double_word_expression = WORD_COUNT_EXPRESSIONS.DOUBLE_WORD_EXPR
        if any(expr.match(line) for expr in SPECIAL_WORDS_EXPRESSIONS) and not double_word_expression.match(line):
            name = ""
            for c in line:
                if c == " ":
                    break
                name += c
            self.__gameClass.name = name
            return True


    # TODO: i_belekhov необходимо разбить обработчики на виды "начинает с", "оканчивается этим", "совпадает с паттерном"
    LINE_STARTSWITH_HANDLERS = (
    )

    STARTSWITH = (
    )

    LINE_ENDSWITH_HANDLERS = (
    )

    ENDSWITH = (
    )

    LINE_MATCH_HANDLERS = (
    )

    # Сначала начало линии, потом конец
    LINE_ALL_HANDLERS = LINE_MATCH_HANDLERS + LINE_STARTSWITH_HANDLERS + LINE_ENDSWITH_HANDLERS


