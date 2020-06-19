"""
    This pattern computes moments in the game in which the length of the 
    team exceeds a cartain value for more than one second and returns those 
    moments with a length visualization for the duration of the infringement.
"""

import sys
from codeball.models import  PatternEvent
from . import Pattern

PATTERN_CODE = 'MET_001'
PATTERN_NAME = 'Team length'


class TeamTooLong(Pattern):

    def __init__(self):
        super(TeamTooLong, self).__init__()
        self.name = PATTERN_NAME
        self.code = PATTERN_CODE

    def run(self):
        print(f'Pattern with code {self.code} computed!')



