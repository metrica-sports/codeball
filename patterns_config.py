import codeball.patterns as patt

PATTERNS_CONFIG = [
    {
        "include": True,
        "name": "Team Stretched",
        "code": "MET_001",
        "pattern_class": patt.TeamStretched,
        "parameters": {"team_code": "FIFATMA", "threshold": 40},
    },
    {
        "include": True,
        "name": "Set Pieces",
        "code": "MET_002",
        "pattern_class": patt.SetPieces,
        "parameters": None,
    },
    {
        "include": True,
        "name": "Passes into the box",
        "code": "MET_003",
        "pattern_class": patt.PassesIntoTheBox,
        "parameters": None,
    },
]


def get_patterns_config():
    return PATTERNS_CONFIG
