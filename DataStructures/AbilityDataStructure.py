# Abilities have levels so this file contains more then one structure xD

from DataStructures.Utilities import PREREQUISITES, LEVEL

ABILITY = {
    "name": "some name", # string with abilities name
    "type": "active or passive",
    "isUnique": False, # is ability unique or not
    "description": "some description string", # general ability description
    "prerequisites": {}, # PREREQUISITES dict or obj
    "levels": [], #list of LEVEL dicts or objs
}

class ABILITY_DESCRIPTION:
    def __init__(self):
        self.__name = "" # just some string
        self.__level = "" # some level, that can be string or number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    # string converter
    def getStringFromObj(self):
        return "%s - %s" % (self.name, self.level)

class GENERAL_ABILITY:
    def __init__(self):
        self.__name = ""
        self.__type = ""
        self.__isUnique = False
        self.__description = ""
        self.__prerequisites = None # should be a prerequisites obj
        self.__levels = []

    # Setters and getters

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, ability_type):
        self.__type = ability_type

    @property
    def isUnique(self):
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, value):
        self.__isUnique = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, descr):
        self.__description = descr

    @property
    def prerequisites(self):
        return self.__prerequisites.objToDict()

    @prerequisites.setter
    def prerequisites(self, prerequisitesObj):
        if isinstance(prerequisitesObj, PREREQUISITES):
            self.__prerequisites = prerequisitesObj
        else:
            assert "Something went wrong %s is not a valid prerequisitesObj" % prerequisitesObj

    @property
    def levels(self):
        return [level.objToDict() for level in self.__levels]

    @levels.setter
    def levels(self, level):
        if isinstance(level, LEVEL):
            self.__levels.append(level)
        else:
            assert "Something went wrong %s is not a valid level" % level

    # dict converter
    def objToDict(self):
        return {
            "name": self.name,  # string with abilities name
            "type": self.type,
            "isUnique": self.isUnique,  # is ability unique or not
            "description": self.description,  # general ability description
            "prerequisites": self.prerequisites,  # PREREQUISITES dict
            "levels": [level.objToDict() for level in self.__levels],  # list of LEVEL dicts
        }
