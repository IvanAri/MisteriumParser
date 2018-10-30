from MisteriumGameParsers.PrecompiledExpressions import CLASS_NAME_EXPRESSIONS, PRQ_EXPRESSIONS, DESCRIPTION_START_EXPRESSION,\
                                                CLASS_ATTRIBUTES_START_EXPRESSION, CLASS_ABILITIES_START_EXPRESSION
from MisteriumGameParsers.PrecompiledExpressions import PRQ_LEVEL_EXPRESSION, PRQ_GAMEPLAY_EXPRESSION,\
                                                        PRQ_CLASS_EXPRESSION, PRQ_CHARACTERISCTIC_EXPRESSIONS,\
                                                        PRQ_ABILITY_EXPRESSIONS, PRQ_GENDER_EXPRESSION
from MisteriumGameParsers.UtilityParsers import get_characteristic_from_line
from MisteriumGameParsers.DataStructures.ClassDataStructure import BASIC_CLASS
from MisteriumGameParsers.DataStructures.Utilities import PREREQUISITES
from MisteriumGameParsers.GameParameters.Characteristics import RUS_TO_ENGL_CHARACTERISCTICS


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
            handler(self)

        self.show_class()

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

    def show_class(self):
        print("=== PARSED CLASS ===")
        print(self.__gameClass.objToDict())

    # stage handlers

    def class_name_searcher(self):
        for idx, line in enumerate(self.__post):
            if any(expr.match(line) for expr in CLASS_NAME_EXPRESSIONS):
                self.__stage = BaseClassParser.CLASS_NAME_FOUND
                self.__currentLineIndex = idx
                self.class_name_handler(line)
                return

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
                self.__currentLineIndex = self.__post.index(line)
                self.__gameClass.prerequisites = PREREQUISITES()

                descr_expr = DESCRIPTION_START_EXPRESSION
                for index, search_line in enumerate(self.__post[self.__currentLineIndex::]):
                    if descr_expr.match(search_line):
                        self.__currentLineIndex = self.__post.index(search_line)
                        break
                    self.__buffer.append(search_line)
                self.prerequisites_handler(self.__buffer)
                return

    def prerequisites_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "prerequisites_handler should be provided with list of strings"

        for idx, line in enumerate(buffer):
            for expr in PRQ_EXPRESSIONS:
                if expr.match(line):
                    # TODO: здесь начинается портянка из вариантов, которые потом как-нибудь надо разбить
                    if expr == PRQ_LEVEL_EXPRESSION:
                        self.__gameClass.prerequisites.level = int(buffer[idx+1])
                    elif expr == PRQ_GENDER_EXPRESSION:
                        self.__gameClass.prerequisites.gender = buffer[idx+1].strip()
                    elif expr == PRQ_GAMEPLAY_EXPRESSION:
                        self.__gameClass.prerequisites.behaviour = buffer[idx+1].strip()
                    elif expr == PRQ_CLASS_EXPRESSION:
                        self.__gameClass.prerequisites.gameClass = buffer[idx+1].strip()
                    elif expr in PRQ_CHARACTERISCTIC_EXPRESSIONS:
                        characteristic = get_characteristic_from_line(line)
                        char_type = RUS_TO_ENGL_CHARACTERISCTICS[characteristic]
                        value = int(buffer[idx+1]) # magic number cause of the structure of the post
                        self.__gameClass.prerequisites.set_characteristic_value(char_type, value)
                    elif expr in PRQ_ABILITY_EXPRESSIONS:
                        self.__gameClass.prerequisites.abilities.append(buffer[idx+1])

        self.__stage = BaseClassParser.PREREQUISITES_PARSED
        self.__buffer.clear()

    def description_searcher(self):
        expr = DESCRIPTION_START_EXPRESSION
        for idx, line in enumerate(self.__post[self.__currentLineIndex::]):
            if expr.match(line):
                self.__stage = BaseClassParser.DESCRIPTION_FOUND
                self.__currentLineIndex = self.__post.index(line)
                self.description_handler(self.__post[self.__currentLineIndex+1])
                return

    def description_handler(self, line):
        self.__gameClass.description = line
        self.__currentLineIndex+=1
        self.__stage = BaseClassParser.DESCRIPTION_PARSED

    def class_attributes_searcher(self):
        expr = CLASS_ATTRIBUTES_START_EXPRESSION
        for idx, line in enumerate(self.__post[self.__currentLineIndex::]):
            if expr.match(line):
                # TODO: оставились на обработке аттрибутов, какие-то из них сможем запарсить сходу, какие-то нет.
                #  Очень много специфичных формулировок
                self.__stage = BaseClassParser.CLASS_ATTRIBUTES_FOUND
                self.__currentLineIndex = self.__post.index(line)

                ability_start_expression = CLASS_ABILITIES_START_EXPRESSION
                for index, search_line in enumerate(self.__post[self.__currentLineIndex::]):
                    if ability_start_expression.match(search_line):
                        self.__currentLineIndex = self.__post.index(search_line)
                        break
                    self.__buffer.append(search_line)
                self.class_attributes_handler(self.__buffer)
                return

    def class_attributes_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "class_attributes_handler should be provided with list of strings"

        for idx, line in enumerate(buffer):
            for expr in PRQ_EXPRESSIONS:
                if expr.match(line):
                    # TODO: здесь начинается портянка из вариантов, которые потом как-нибудь надо разбить
                    pass
                else:
                    self.__gameClass.string_attributes.append(line)

        self.__stage = BaseClassParser.CLASS_ATTRIBUTES_PARSED
        self.__buffer.clear()

    def abilities_searcher(self):
        pass

    def class_verifier(self):
        pass

    def class_converter(self):
        pass

    def job_finished_handler(self):
        pass

    STAGE_HANDLERS = (
        class_name_searcher,
        prerequisites_searcher,
        description_searcher,
        class_attributes_searcher,
        abilities_searcher,
        class_verifier,
        class_converter,
        job_finished_handler,
    )


