from collections import deque
from MisteriumGameParsers.BasicParser import BasicParser
from MisteriumGameParsers.PrecompiledExpressions import EXPERIENCE_EXPR, FINISH_EXPRESSIONS, \
    WORD_COUNT_EXPRESSIONS, SPECIAL_WORDS_EXPRESSIONS, CLASS_NAME_EXPRESSIONS, PRQ_EXPRESSIONS, DESCRIPTION_EXPRESSION
from DataStructures.ClassDataStructure import BASIC_CLASS
from DataStructures.AbilityDataStructure import ABILITY
from DataStructures.Utilities import LEVEL, PREREQUISITES

import json

# TODO: i_belekhov remake this class to work with strings and post content itself and not a feed from parser
# TODO: in the end we should have a data structure converted to JSon for further use

class BaseClassParser:

    NO_POST = "no_post"
    NEW_POST = "new_post"
    CLASS_NAME_FOUND = "class_name_found"
    CLASS_NAME_PARSED = "class_name_parsed"
    PREREQUISITES_FOUND = "prerequisites_found"
    PREREQUISITES_PARSED = "prerequisites_parsed"
    DESCRIPTION_FOUND = "description_found"
    DESCRIPTION_PARSED = "description_parsed"
    CLASS_ATTRIBUTES_FOUND = "class_attributes_found"
    CLASS_ATTRIBUTES_PARSED = "class_attributes_parsed"
    ABILITIES_FOUND = "class_abilities_found"
    ABILITIES_PARSED = "class_abilities_parsed"
    CLASS_PARSED = "class_parsed"
    CLASS_CONVERTED = "class_converted"

    TERMINATE = "terminate"
    UNKNOWN_STAGE = "unknown"

    STAGES = (
        NO_POST,
        NEW_POST,
        CLASS_NAME_FOUND,
        CLASS_NAME_PARSED,
        PREREQUISITES_FOUND,
        PREREQUISITES_PARSED,
        DESCRIPTION_FOUND,
        DESCRIPTION_PARSED,
        CLASS_ATTRIBUTES_FOUND,
        CLASS_ATTRIBUTES_PARSED,
        ABILITIES_FOUND,
        ABILITIES_PARSED,
        CLASS_PARSED,
        CLASS_CONVERTED
    )

    def __init__(self):
        super(BaseClassParser, self).__init__()
        self.__gameClass = BASIC_CLASS() # resulting BASIC_CLASS dict
        self.__text = [] # resulting list of prepared lines if needed
        self.__currentLineIndex = 0 # index of the line that we are currently processing
        self.__post = []  # list of strings of unrefined initial post

        self.__buffer = [] # list of strings that we gathered for processing
        self.__buffer_start_idx = 0
        self.__buffer_end_idx = 0 # all indexes are related to initial post

        self.__stage = BaseClassParser.NO_POST
    # processing

    # here the magic starts
    def extract_class(self):
        if self.__stage != BaseClassParser.NEW_POST:
            assert "Something gone wrong, not expected stage: %s" % self.__stage

        # для каждой стадии вызываем своего обработчика.
        # обработка поточная, а поэтому если где-то прервалась итерация, значит мы накосячили
        for handler in BaseClassParser.STAGE_HANDLERS:
            try:
                handler()
            except:
                print("Something get wrong for stage: %s" % self.__stage)
                break

        print("==== EXTRACTING COMPLETE! ====")

    def process(self, rawData):
        if not isinstance(rawData, list):
            assert "BaseClassParser process should be provided with list of strings as rawData"

        self.__post = rawData # list of strings
        self.__stage = BaseClassParser.NEW_POST
        self.extract_class()

        print("==== PROCESSING COMPLETE! ====")

    # utilities

    def show_buffer(self):
        for line in self.__text:
            print(line)

    def beautifySegment(self):
        pass

    # stage handlers

    def class_name_searcher(self):
        for idx, line in enumerate(self.__post):
            if any(expr.match(line) for expr in CLASS_NAME_EXPRESSIONS):
                self.__stage = BaseClassParser.CLASS_NAME_FOUND
                self.__currentLineIndex = idx
                self.class_name_handler(line)

    def class_name_handler(self, line):
        name = ""
        for c in line:
            if c == " ":
                break
            name += c
        self.__gameClass.name = name
        self.__stage = BaseClassParser.CLASS_NAME_PARSED

    def prerequisites_searcher(self):
        for idx, line in enumerate(self.__post[self.__currentLineIndex::]):
            if any(expr.match(line) for expr in PRQ_EXPRESSIONS):
                self.__stage = BaseClassParser.PREREQUISITES_FOUND
                self.__currentLineIndex = idx
                self.__buffer_start_idx = idx
                self.__gameClass.prerequisites = PREREQUISITES()

                descr_expr = DESCRIPTION_EXPRESSION
                for index, search_line in enumerate(self.__post[self.__buffer_start_idx::]):
                    if descr_expr.match(search_line):
                        self.__buffer_end_idx = index
                        break
                    self.__buffer.append(search_line)
                self.prerequisites_handler(self.__buffer)
        pass

    def prerequisites_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "prerequisites_handler should be provided with list of strings"



        pass

    def description_searcher(self):
        pass

    def class_attributes_searcher(self):
        pass

    def abilities_searcher(self):
        pass

    def class_verifier(self):
        pass

    def class_converter(self):
        pass

    def job_finished_handler(self):
        pass

    STAGE_HANDLERS = {
        NEW_POST: class_name_searcher,
        CLASS_NAME_PARSED: prerequisites_searcher,
        PREREQUISITES_PARSED: description_searcher,
        DESCRIPTION_PARSED: class_attributes_searcher,
        CLASS_ATTRIBUTES_PARSED: abilities_searcher,
        ABILITIES_PARSED: class_verifier,
        CLASS_PARSED: class_converter,
        CLASS_CONVERTED: job_finished_handler,
    }


