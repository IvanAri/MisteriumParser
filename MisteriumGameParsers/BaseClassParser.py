from collections import deque
import json

from MisteriumGameParsers.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser
# TODO: in the end we should have a data structure converted to JSon for further use

class BaseClassParser:
    def __init__(self):
        self.__classContent = {} # resulting BASIC_CLASS dict
        self.threeLineSegment = deque(maxlen=3)

    # In this method we do main processing
    def process(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser should be provided with list of strings as rawData"
        pass




