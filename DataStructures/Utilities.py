PREREQUISITES_STRUCTURE = {
        "level": 100, # should be int
        "class": "some class name", # string with class name
        "characteristics": {
            "strength" : 0, # some ints
            "agility" : 0,
            "stamina" : 0,
            "gift" : 0,
        },
        "behaviour": [], # should be list of strings
    }

LEVEL_STRUCTURE = {
    "level": 0, # int with actual level number
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

class ABILITY_PREREQUISITY:
    def __init__(self):
        self.__name = ""
        self.__level = 0 # some int value that describes



class PREREQUISITES:

    def __init__(self):
        self.__level = 0
        self.__gameClass = ""
        self.__mainCharacteristics = {
            "strength": 0,  # some ints
            "agility": 0,
            "stamina": 0,
            "gift": 0,
        }
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
            "characteristics": {
                "strength"  : self.strength, # some ints
                "agility"   : self.agility,
                "stamina"   : self.stamina,
                "gift"      : self.gift,
            },
            "behaviour": self.behaviour, # should be string
        }

class LEVEL:

    def __init__(self):
        self.__level = 0
        self.__attributes = {} # dict of ATTRIBUTE objects
        self.__mechanic = "" # mechanic string
        self.__prerequisites = None # should be a PREREQUISITES object


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

    @attributes.setter
    def attributes(self, attribute):
        if isinstance(attribute, ATTRIBUTE):
            self.__attributes[attribute.type] = attribute
        else:
            assert "Something went wrong %s is not a valid attribute" % attribute

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
        return self.__prerequisites.objToDict()

    @prerequisites.setter
    def prerequisites(self, prerequisitesObj):
        if isinstance(prerequisitesObj, PREREQUISITES):
            self.__prerequisites = prerequisitesObj
        else:
            assert "Something went wrong %s is not a valid prerequisitesObj" % prerequisitesObj

    # dict converter
    def objToDict(self):
        return {
            "level": self.level, # int with actual level number
            "attributes": self.attributes, # list of attributes objects that can be converted to game characteristics
            "mechanic": self.mechanic, # general mechanic description, if can't be parsed into bonuses
            "prerequisites": self.prerequisites, # PREREQUISITES dict or obj that can be converted to dict
        }

# ! ! ! NOT any attribute can be described as an object, that's why sometimes we will use game-description strings
class ATTRIBUTE:

    def __init__(self):
        self.__type = ""
        self.__additive = False
        self.__multiplicative = False
        self.__value = 0

    # Setters and getters

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, attributeName):
        if isinstance(attributeName, str):
            self.__type += '\n' + attributeName
        else:
            assert "Something went wrong %s is not a valid attributeName" % attributeName

    @property
    def isAdditive(self):
        return self.__additive

    @isAdditive.setter
    def isAdditive(self, value):
        self.__additive = value

    @property
    def isMultiplicative(self):
        return self.__multiplicative

    @isMultiplicative.setter
    def isMultiplicative(self, value):
        self.__multiplicative = value

    @property
    def value(self):
        return self.__additive

    @value.setter
    def value(self, attributeValue):
        self.__additive = attributeValue

    # dict converter
    def objToDict(self):
        return {
            "type": self.type,
            "isAdditive": self.isAdditive,  # True or False depending on mechanic
            "isMultiplicative": self.isMultiplicative,
            # True or False depending on mechanic structure.
            # Additive and multiplicative can't be True together
            "value": self.value,  # positive or negative int value
        }

