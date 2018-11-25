from MisteriumGameParsers.PrecompiledExpressions import CLASS_NAME_EXPRESSIONS, PRQ_EXPRESSIONS, DESCRIPTION_START_EXPRESSION,\
                                                CLASS_ATTRIBUTES_START_EXPRESSION, CLASS_ABILITIES_START_EXPRESSION,\
                                                NOT_EXACT_ABILITIES_EXPRESSIONS, TECHNICAL_WORDS_EXPRESSIONS
from MisteriumGameParsers.PrecompiledExpressions import LEVEL_AND_COST_EXPRESSION, LEVEL_EXPRESSION,\
                                                        EXPERIENCE_COST_EXPR, ABILITY_TYPE_EXPRESSIONS
from MisteriumGameParsers.PrecompiledExpressions import PRQ_LEVEL_EXPRESSION, PRQ_GAMEPLAY_EXPRESSION,\
                                                        PRQ_CLASS_EXPRESSION, PRQ_CHARACTERISCTIC_EXPRESSIONS,\
                                                        PRQ_ABILITY_EXPRESSIONS, PRQ_GENDER_EXPRESSION
from MisteriumGameParsers.PrecompiledExpressions import makeSpecialWordsExpressions, make_special_expression
from MisteriumGameParsers.UtilityParsers import get_characteristic_from_line
from MisteriumGameParsers.DataStructures.ClassDataStructure import BASIC_CLASS
from MisteriumGameParsers.DataStructures.Utilities import PREREQUISITES, LEVEL, COST_SPECIAL_WORDS
from MisteriumGameParsers.DataStructures.AbilityDataStructure import GENERAL_ABILITY, ABILITIES_SPECIAL_WORDS
from MisteriumGameParsers.GameParameters.Characteristics import RUS_TO_ENGL_CHARACTERISCTICS
from MisteriumGameParsers.AttributeParser import AttributeParser

import json
import sys

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

        name = self.__post[0]
        print("XYI ! ! !", name)
        if not any(expr.match(name) for expr in CLASS_NAME_EXPRESSIONS):
            print("! ! ! THIS POST IS NOT A BASE CLASS POST ! ! !")
            return

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
                self.__stage = BaseClassParser.CLASS_ATTRIBUTES_FOUND
                self.__currentLineIndex = self.__post.index(line)

                ability_start_expression = CLASS_ABILITIES_START_EXPRESSION
                for index, search_line in enumerate(self.__post[self.__currentLineIndex+1::]):
                    if ability_start_expression.match(search_line):
                        self.__currentLineIndex = self.__post.index(search_line)
                        break
                    self.__buffer.append(search_line)
                self.class_attributes_handler(self.__buffer)
                return

    def class_attributes_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "class_attributes_handler should be provided with list of strings"

        parser = AttributeParser()

        for idx, line in enumerate(buffer):
                attr = parser.parse_attribute_string(line)
                if attr:
                    self.__gameClass.passive_attributes.append(attr)
                else:
                    self.__gameClass.string_attributes.append(line)

        self.__stage = BaseClassParser.CLASS_ATTRIBUTES_PARSED
        self.__buffer.clear()

    def abilities_searcher(self):
        expr = CLASS_ABILITIES_START_EXPRESSION
        for idx, line in enumerate(self.__post[self.__currentLineIndex::]):
            if expr.match(line):
                self.__stage = BaseClassParser.ABILITIES_FOUND
                self.__currentLineIndex = self.__post.index(line)

                for index, search_line in enumerate(self.__post[self.__currentLineIndex+1::]):
                    self.__buffer.append(search_line)
                self.abilities_handler(self.__buffer)
                return

    def abilities_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "abilities_handler should be provided with list of strings"

        inner_buffer = []
        for idx, line in enumerate(buffer):
            for expr in NOT_EXACT_ABILITIES_EXPRESSIONS:
                res = expr.match(line)
                if res and len(res.group()) == len(line):
                    current_ability_index = buffer.index(line)

                    inner_buffer.append(buffer[current_ability_index])
                    is_ability_found = False
                    for index, search_line in enumerate(buffer[current_ability_index+1::]):

                        for expr in NOT_EXACT_ABILITIES_EXPRESSIONS:
                            res = expr.match(search_line)
                            if res and len(res.group()) == len(search_line):
                                is_ability_found = True
                                break
                        if is_ability_found:
                            break

                        inner_buffer.append(search_line)

                    ability = self.__single_ability_handler(inner_buffer)
                    if ability.type == ABILITIES_SPECIAL_WORDS.PASSIVE:
                        self.__gameClass.passive_abilities.append(ability)
                    else:
                        self.__gameClass.active_abilities.append(ability)
                    inner_buffer.clear()
        # this is the last parsing stage for a normal base class
        self.__stage = BaseClassParser.ABILITIES_PARSED

    def __single_ability_handler(self, buffer):
        if not isinstance(buffer, list):
            assert "ability_handler should be provided with list of strings"

        # ====== Preparing ======
        style_expr = make_special_expression("стил бо")
        active_expr = makeSpecialWordsExpressions("активн")
        passive_expr = makeSpecialWordsExpressions("пассивн")
        is_skip_line_needed = False

        parser = AttributeParser()
        ability = GENERAL_ABILITY()
        ability.description = ""

        # ====== Parsing ======
        for line in buffer:
            # В некоторых случаях обработчик занимает 2 линии, а не одну. Поэтому нужен пропуск
            if is_skip_line_needed:
                is_skip_line_needed = False
                continue

            # Парсим имя
            is_name_found = False
            for expr in NOT_EXACT_ABILITIES_EXPRESSIONS:
                res = expr.match(line)
                if res and len(res.group()) == len(line):
                    ability.name = res.group()
                    is_name_found = True
                    break
            if is_name_found:
                continue

            # Парсим тип
            if any(expr.match(line) for expr in ABILITY_TYPE_EXPRESSIONS):
                if active_expr.match(line.split(" ")[0]):
                    ability.type = ABILITIES_SPECIAL_WORDS.ACTIVE
                    continue
                elif passive_expr.match(line.split(" ")[0]):
                    ability.type = ABILITIES_SPECIAL_WORDS.PASSIVE
                    continue
                elif style_expr.match(line):
                    ability.type = ABILITIES_SPECIAL_WORDS.STYLE
                    continue

            # Парсим уровень
            if LEVEL_AND_COST_EXPRESSION.match(line):
                level, experience_cost = self.__level_parser(line)
                new_level = LEVEL()
                new_level.level = level
                new_level.cost[COST_SPECIAL_WORDS.EXPERIENCE] = experience_cost
                print('TESTLOG! ! ! WEIRD LINE', line)
                next_line = buffer[buffer.index(line)+1]
                attr = parser.parse_attribute_string(next_line)
                if attr:
                    new_level.attributes.append(attr)
                else:
                    new_level.mechanic = next_line
                is_skip_line_needed = True
                ability.levels.append(new_level)
                continue

            ability.description += line + " "

        return ability

    def __level_parser(self, line):
        level = LEVEL_EXPRESSION.match(line).group().split(" ")[0]
        experience_cost = EXPERIENCE_COST_EXPR.search(line).group().split(" ")[0]
        return int(level), int(experience_cost)

    def class_verifier(self):
        pass

    def class_converter(self):
        pass

    def job_finished_handler(self):
        print("TESTLOG ! ! ! JOB FINISHED")
        with open('E:\\MisteriumUtilities\\Classes\\%s_class.json' % self.__gameClass.name, 'w') as file:
            json.dump(self.__gameClass.objToDict(), file)
        file.close()

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


