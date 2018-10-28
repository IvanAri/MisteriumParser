# not finale data structure, that is easy to work with
# TODO: Добавь для Далендора полное содержание распаршеных постов


from MisteriumGameParsers.DataStructures import PREREQUISITES

BASIC_CLASS_STRUCTURE = {
    "name": "Some class name", #
    "description": "Some non-mechanic description", # non-mechanic description string
    "prerequisites": {}, # PREREQUISITES dict
    "string_attributes": [], # something that can't be described as ATTRIBUTE objs
    "passive_attributes": [], # should be list of ATTRIBUTE objs
    "abilities":{
        "passives": [], # should be list of ability objects, in future - dicts
        "actives": [], # should be list of ability objects, in future - dicts
    }
}

class BASIC_CLASS:

    def __init__(self):
        self.__name = ""
        self.__description = ""
        self.__prerequisites = None  # PREREQUISITES obj
        self.__string_attributes = [] # something that can't be described as ATTRIBUTE objs
        self.__passive_attributes = [] # list of ATTRIBUTE objs
        self.__abilities = {
            "passive": [], # list of ABILITY objs
            "active": [], # list of ABILITY objs
        }

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string):
        self.__name = name_string

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, descr):
        self.__description = descr

    @property
    def string_attributes(self):
        return self.__string_attributes

    @property
    def passive_attributes(self):
        return self.__passive_attributes

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
    def passive_abilities(self):
        return self.__abilities["passive"]

    @property
    def active_abilities(self):
        return self.__abilities["active"]

    # dict converter
    def objToDict(self):
        return {
            "name": self.name,  # name string
            "description": self.description,  # non-mechanic description string
            "prerequisites": self.__prerequisites.objToDict(),  # PREREQUISITES dict
            "string_attributes": self.__string_attributes,
            "passive_attributes": [attr.objToDict() for attr in self.__passive_attributes],  # should be list of ATTRIBUTE objs
            "abilities": {
                "passives": [],  # should be list of ability objects, in future - dicts
                "actives": [],  # should be list of ability objects, in future - dicts
            }
        }


