PREREQUISITES_STRUCTURE = {
        "level": 100, # should be int
        "class": "some class name", # string with class name
        "gender": "man or woman", # gender prerequisity, yep
        "characteristics": {
            "strength" : 0, # some ints
            "agility" : 0,
            "stamina" : 0,
            "gift" : 0,
        },
        "abilities": [], # list of ability description strings like "Кулак духа - 4 уровень"
        "behaviour": [], # should be list of strings
    }

LEVEL_STRUCTURE = {
    "level": 0, # int with actual level number
    "cost": {
        "experience": 0,
        "honour": 0,
        "loyalty": 0,
    },
    "attributes": [], # list of attributes objects that can be converted to game characteristics
    "mechanic": "some description string", # general mechanic description, if can't be parsed into bonuses
    "prerequisites": {}, # PREREQUISITES dict or obj that can be converted to dict
}

ATTRIBUTE_STRUCTURE = {
    "type": "some attribute unique name",
    "additive": False, # True or False depending on mechanic
    "multiplicative": False,
    # True or False depending on mechanic structure.
    # Additive and multiplicative can't be True together
    "value": 0, # positive or negative int value
}

class PREREQUISITES:

    def __init__(self):
        self.__level = 0
        self.__gameClass = ""
        self.__gender = ""
        self.__mainCharacteristics = {
            "strength": 0,  # some ints
            "agility": 0,
            "stamina": 0,
            "gift": 0,
        }
        self.__abilities = [] # should be a list of strings that suit the ABILITY_DESCRIPTION
        self.__behaviour = "" # should be a string

    # Setters and getters

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def gameClass(self):
        return self.__gameClass

    @gameClass.setter
    def gameClass(self, gameClassName):
        if isinstance(gameClassName, str):
            self.__gameClass = gameClassName
        else:
            assert "Something went wrong %s is not a valid gameClassName" % gameClassName

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    def set_characteristic_value(self, char_type, value):
        self.__mainCharacteristics[char_type] = value

    @property
    def strength(self):
        return self.__mainCharacteristics["strength"]

    @strength.setter
    def strength(self, value):
        self.__mainCharacteristics["strength"] = value

    @property
    def agility(self):
        return self.__mainCharacteristics["agility"]

    @agility.setter
    def agility(self, value):
        self.__mainCharacteristics["agility"] = value

    @property
    def stamina(self):
        return self.__mainCharacteristics["stamina"]

    @stamina.setter
    def stamina(self, value):
        self.__mainCharacteristics["stamina"] = value

    @property
    def gift(self):
        return self.__mainCharacteristics["gift"]

    @gift.setter
    def gift(self, value):
        self.__mainCharacteristics["gift"] = value

    @property
    def abilities(self):
        return self.__abilities

    @property
    def behaviour(self):
        return self.__behaviour

    @behaviour.setter
    def behaviour(self, behaviourString):
        if isinstance(behaviourString, str):
            self.__behaviour += '\n' + behaviourString
        else:
            print("Something went wrong %s is not a valid behaviourString" % behaviourString)

    # dict converter
    def objToDict(self):
        return {
            "level": self.level, # should be int
            "class": self.gameClass, # string with class name
            "gender": self.gender,
            "characteristics": {
                "strength"  : self.strength, # some ints
                "agility"   : self.agility,
                "stamina"   : self.stamina,
                "gift"      : self.gift,
            },
            "abilities": self.abilities,
            "behaviour": self.behaviour, # should be string
        }

# TODO: make a cost object in the future

class COST_SPECIAL_WORDS:
    EXPERIENCE = "experience"
    HONOUR = "honour"
    LOYALTY = "loyalty"

class LEVEL:

    def __init__(self):
        self.__level = 0
        self.__attributes = [] # dict of ATTRIBUTE objects
        self.__mechanic = "" # mechanic string
        self.__prerequisites = None # should be a PREREQUISITES object
        self.__cost = {
            COST_SPECIAL_WORDS.EXPERIENCE: 0,
            COST_SPECIAL_WORDS.HONOUR: 0,
            COST_SPECIAL_WORDS.LOYALTY: 0,
        } # dict of costs

    # Setters and getters

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def attributes(self):
        return self.__attributes

    @property
    def mechanic(self):
        return self.__mechanic

    @mechanic.setter
    def mechanic(self, mechanicString):
        if isinstance(mechanicString, str):
            self.__mechanic += '\n' + mechanicString
        else:
            print("Something went wrong %s is not a valid mechanicString" % mechanicString)

    @property
    def prerequisites(self):
        return self.__prerequisites

    @prerequisites.setter
    def prerequisites(self, prerequisitesObj):
        if isinstance(prerequisitesObj, PREREQUISITES):
            self.__prerequisites = prerequisitesObj
        else:
            assert "Something went wrong %s is not a valid prerequisitesObj" % prerequisitesObj

    @property
    def cost(self):
        return self.__cost

    def set_cost(self, cost_type, value):
        self.__cost[cost_type] = value

    # dict converter
    def objToDict(self):
        return {
            "level": self.level, # int with actual level number
            "cost": self.cost, # dict with costs in exp and other types of game currencies
            "attributes": [attr.objToDict() for attr in self.__attributes], # list of attributes objects that can be converted to game characteristics
            "mechanic": self.mechanic, # general mechanic description, if can't be parsed into bonuses
            "prerequisites": self.prerequisites.objToDict(), # PREREQUISITES dict or obj that can be converted to dict
        }

# ! ! ! NOT any attribute can be described as an object, that's why sometimes we will use game-description strings
class ATTRIBUTE:

    def __init__(self):
        self.__name = ""
        self.__game_action = ""
        self.__game_action_modifier = ""
        self.__game_action_impact = ""
        self.__parameter = "" # should be a PARAMETER string
        self.__parameter_specifier = "" # some specifier name
        self.__basic = False
        self.__additive = False
        self.__multiplicative = False
        self.__sign = 1  # 1 or -1
        self.__parameter_value = 0

    # Setters and getters

    @property
    def name(self):
        return self.__name

    @property
    def game_action(self):
        return self.__game_action

    @game_action.setter
    def game_action(self, value):
        self.__game_action = value

    @property
    def game_action_modifier(self):
        return self.__game_action_modifier

    @game_action_modifier.setter
    def game_action_modifier(self, value):
        self.__game_action_modifier = value

    @property
    def game_action_impact(self):
        return self.__game_action_impact

    @game_action_impact.setter
    def game_action_impact(self, value):
        self.__game_action_impact = value

    @property
    def is_additive(self):
        return self.__additive

    @is_additive.setter
    def is_additive(self, value):
        self.__additive = value

    @property
    def is_multiplicative(self):
        return self.__multiplicative

    @is_multiplicative.setter
    def is_multiplicative(self, value):
        self.__multiplicative = value

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        self.__parameter = value

    @property
    def parameter_specifier(self):
        return self.__parameter_specifier

    @parameter_specifier.setter
    def parameter_specifier(self, value):
        self.__parameter_specifier = value

    @property
    def parameter_value(self):
        return self.__parameter_value

    @parameter_value.setter
    def parameter_value(self, value):
        self.__parameter_value = value
        
    @property
    def sign(self):
        return self.__sign
    
    @sign.setter
    def sign(self, sign_modificator):
        self.__sign = sign_modificator

    # dict converter
    def objToDict(self):
        return {
            "type": self.name,
            "is_additive": self.is_additive,  # True or False depending on mechanic
            "is_multiplicative": self.is_multiplicative,
            "is_basic": self.__basic,
            # True or False depending on mechanic structure.
            # Additive and multiplicative can't be True together
            "game_action": self.game_action,
            "game_action_modifier": self.game_action_modifier,
            "game_action_impact": self.game_action_impact,
            "parameter": self.parameter,
            "parameter_specifier": self.parameter_specifier,
            "sign": self.sign, # sign for further calculations, can be 1 or -1
            "parameter_value": self.parameter_value,  # positive or negative int value
        }

