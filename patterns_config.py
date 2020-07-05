import codeball.patterns as patt

PATTERNS_CONFIG = [
    {
        "include": True,
        "name": "Team Stretched",
        "code": "MET_001",
        "pattern_analysis": [
            {
                "class": patt.TeamStretched,
                "parameters": {"team_code": "home", "threshold": 40},
            }
        ],
    }
]


def get_patterns_config():
    return PATTERNS_CONFIG
