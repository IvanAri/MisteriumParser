from MisteriumGameParsers.GameParameters import AttributesComponents
from MisteriumGameParsers.GameParameters import Parameters
from MisteriumGameParsers.DataStructures.Utilities import ATTRIBUTE

# TODO: i_belekhov перенеси это в AttributesComponents
# Классификация различных элементов аттрибута
GAME_ACTIONS = "game_actions"
GAME_ACTIONS_MODIFIERS = "game_actions_modifiers"
GAME_ACTIONS_IMPACTS = "game_actions_impact_modifiers"
SIGN_QUALIFIERS = "sign_qualifiers"
PARAMETERS = "parameters"
PARAMETERS_MODIFIERS = "parameters modifiers"
EXPRESSIONS_BY_CATEGORIES = {
    GAME_ACTIONS: AttributesComponents.GAME_ACTIONS_CATEGORIES_EXPRESSIONS,
    GAME_ACTIONS_MODIFIERS: AttributesComponents.GAME_ACTIONS_MODIFIERS_CATEGORIES_EXPRESSIONS,
    GAME_ACTIONS_IMPACTS: AttributesComponents.GAME_ACTIONS_IMPACTS_CATEGORIES_EXPRESSIONS,
    SIGN_QUALIFIERS: AttributesComponents.SIGN_QUALIFIERS_CATEGORIES_EXPRESSIONS,
    PARAMETERS: Parameters.PARAMETERS_CATEGORIES_EXPRESSIONS,
    PARAMETERS_MODIFIERS: Parameters.PARAMETERS_MODIFIERS_CATEGORIES_EXPRESSIONS,
}

ALIASES_BY_CATEGORIES = {
    GAME_ACTIONS: AttributesComponents.GAME_ACTIONS_ALIASES,
    GAME_ACTIONS_MODIFIERS: AttributesComponents.GAME_ACTIONS_MODIFIERS_ALIASES,
    GAME_ACTIONS_IMPACTS: AttributesComponents.GAME_ACTIONS_IMPACTS_ALIASES,
    SIGN_QUALIFIERS: AttributesComponents.SIGN_QUALIFIERS_ALIASES,
    PARAMETERS: Parameters.PARAMETERS_ALIASES,
    PARAMETERS_MODIFIERS: Parameters.PARAMETERS_MODIFIERS_ALIASES,
}

class AttributeParser:

    def __init__(self):
        self.__attribute_string = ""
        self.__attributes = {} # list of ATTRIBUTE objects

    # main parsing process

    # TODO: вот здесь будет твориться вся магия с аттрибутами
    def parse_attribute_string(self, attribute_string):
        if isinstance(attribute_string, str):
            self.__attribute_string = attribute_string
        else:
            assert "Something went wrong %s is not a valid attribute_string" % attribute_string

        game_actions = self.find_game_action()
        game_actions_modifiers = self.find_game_action_modifiers()
        game_actions_impacts = self.find_game_action_impacts()
        sign_qualifiers = self.find_parameters_sign()
        parameters = self.find_parameter()
        parameters_modifiers = self.find_parameter_modifier()
        values = self.find_value()
        print('Game actions: ', game_actions)
        print('Game actions modifiers: ', game_actions_modifiers)
        print('Game actions impacts: ', game_actions_impacts)
        print('Sign qualifiers: ', sign_qualifiers)
        print('Parameters: ', parameters)
        print('Parameters modifiers: ', parameters_modifiers)
        print('Values: ', values)
        print("!!! Закончили парсить аттрибутную строку !!!")
        pass

    # TODO: объединить методы в один, скармливать туда stage'ы
    def find_game_action(self):
        game_actions = []
        for expr in AttributesComponents.GAME_ACTIONS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action = self.search_alias(res.group(), GAME_ACTIONS)
                game_actions.append(game_action)
        return game_actions

    def find_game_action_modifiers(self):
        game_actions_modifiers = []
        for expr in AttributesComponents.GAME_ACTIONS_MODIFIERS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action_modifier = self.search_alias(res.group(), GAME_ACTIONS_MODIFIERS)
                game_actions_modifiers.append(game_action_modifier)
        return game_actions_modifiers

    def find_game_action_impacts(self):
        game_actions_impacts = []
        for expr in AttributesComponents.GAME_ACTIONS_IMPACTS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action_impact = self.search_alias(res.group(), GAME_ACTIONS_IMPACTS)
                game_actions_impacts.append(game_action_impact)
        return game_actions_impacts

    def find_parameters_sign(self):
        sign_qualifiers = []
        for expr in AttributesComponents.SIGN_QUALIFIERS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                sign_qualifier = self.search_alias(res.group(), SIGN_QUALIFIERS)
                sign_qualifiers.append(sign_qualifier)
        return sign_qualifiers

    def find_parameter(self):
        parameters = []
        for expr in Parameters.PARAMETERS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                parameter = self.search_alias(res.group(), PARAMETERS)
                parameters.append(parameter)
        return parameters

    def find_parameter_modifier(self):
        parameters_modifiers = []
        for expr in Parameters.PARAMETERS_MODIFIERS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                parameter_modifier = self.search_alias(res.group(), PARAMETERS_MODIFIERS)
                parameters_modifiers.append(parameter_modifier)
        return parameters_modifiers

    def find_value(self):
        values = AttributesComponents.VALUE_EXPRESSION.findall(self.__attribute_string)
        return values

    # utilities
    def search_alias(self, name, category):
        expr_category = EXPRESSIONS_BY_CATEGORIES[category]
        for type in expr_category:
            for expr in expr_category[type]:
                if expr.match(name):
                    return ALIASES_BY_CATEGORIES[category][type]


