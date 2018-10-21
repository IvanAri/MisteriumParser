PREREQUISITES = {
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

LEVEL = {
    "number": 0, # int with actual level
    "bonuses": [], # list of bonuses that can be converted to game characteristics
    "mechanic_description": "some description string", # general mechanic description, if can't be parsed into bonuses
    "description": "some description string", # general description
    "prerequisites": {}, # PREREQUISITES dict
}