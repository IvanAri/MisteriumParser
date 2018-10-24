# not finale data structure, that is easy to work with

BASIC_CLASS_STRUCTURE = {
    "name": "Some class name",
    "main_description": "Some description",
    "prerequisites": {}, # PREREQUISITES dict
    "benefits": [], # should be list of strings
    "abilities":{
        "passives": [], # should be list of ability objects, in future - dicts
        "actives": [], # should be list of ability objects, in future - dicts
    }
}

class BASIC_CLASS:

    def __init__(self):
        self.__name = None
        self.__main_description = None
        self.__prerequisities = None