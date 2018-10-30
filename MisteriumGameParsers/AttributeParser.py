from MisteriumGameParsers.GameParameters import Attributes
from MisteriumGameParsers.DataStructures.Utilities import ATTRIBUTE

# Классификация различных элементов аттрибута
GAME_ACTIONS = "game_actions"
GAME_ACTIONS_MODIFIERS = "game_actions_modifiers"
GAME_ACTIONS_IMPACTS = "game_actions_impact_modifiers"
EXPRESSIONS_BY_CATEGORIES = {
    GAME_ACTIONS: Attributes.GAME_ACTIONS_CATEGORIES_EXPRESSIONS,
    GAME_ACTIONS_MODIFIERS: Attributes.GAME_ACTIONS_MODIFIERS_CATEGORIES_EXPRESSIONS,
    GAME_ACTIONS_IMPACTS: Attributes.GAME_ACTIONS_IMPACTS_CATEGORIES_EXPRESSIONS,
}

ALIASES_BY_CATEGORIES = {
    GAME_ACTIONS: Attributes.GAME_ACTIONS_ALIASES,
    GAME_ACTIONS_MODIFIERS: Attributes.GAME_ACTIONS_MODIFIERS_ALIASES,
    GAME_ACTIONS_IMPACTS: Attributes.GAME_ACTIONS_IMPACTS_ALIASES,
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
        print('Game actions: ', game_actions)
        print('Game actions modifiers: ', game_actions_modifiers)
        print('Game actions impacts: ', game_actions_impacts)
        print("!!! Закончили парсить аттрибутную строку !!!")
        pass

    # TODO: объединить методы в один, скармливать туда stage'ы
    def find_game_action(self):
        game_actions = []
        for expr in Attributes.GAME_ACTIONS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action = self.search_alias(res.group(), GAME_ACTIONS)
                game_actions.append(game_action)
        return game_actions

    def find_game_action_modifiers(self):
        game_actions_modifiers = []
        for expr in Attributes.GAME_ACTIONS_MODIFIERS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action_modifier = self.search_alias(res.group(), GAME_ACTIONS_MODIFIERS)
                game_actions_modifiers.append(game_action_modifier)
        return game_actions_modifiers

    def find_game_action_impacts(self):
        game_actions_impacts = []
        for expr in Attributes.GAME_ACTIONS_IMPACTS_EXPRESSIONS:
            res = expr.search(self.__attribute_string)
            if res:
                game_action_impact = self.search_alias(res.group(), GAME_ACTIONS_IMPACTS)
                game_actions_impacts.append(game_action_impact)
        return game_actions_impacts

    # utilities
    def search_alias(self, name, category):
        expr_category = EXPRESSIONS_BY_CATEGORIES[category]
        for type in expr_category:
            for expr in expr_category[type]:
                if expr.match(name):
                    return ALIASES_BY_CATEGORIES[category][type]


