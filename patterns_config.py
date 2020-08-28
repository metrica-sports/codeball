import codeball.patterns as patt

PATTERNS_CONFIG = [
    {
        "include": True,
        "name": "Team Stretched",
        "code": "MET_001",
        "pattern_class": patt.TeamStretched,
        "parameters": {"team_code": "FIFATMA", "threshold": 35},
        "in_time": 2,
        "out_time": 2,
    },
    {
        "include": True,
        "name": "Set Pieces",
        "code": "MET_002",
        "pattern_class": patt.SetPieces,
        "parameters": None,
        "in_time": 2,
        "out_time": 2,
    },
    {
        "include": True,
        "name": "Passes into the box",
        "code": "MET_003",
        "pattern_class": patt.PassesIntoTheBox,
        "parameters": None,
        "in_time": 2,
        "out_time": 2,
    },
]


def get_patterns_config():
    return PATTERNS_CONFIG
