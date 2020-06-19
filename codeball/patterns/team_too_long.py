"""
    This pattern computes moments in the game in which the length of the 
    team exceeds a cartain value for more than one second and returns those 
    moments with a length visualization for the duration of the infringement.
"""
from typing import List
from codeball.models import  PatternEvent
from . import PatternAnalysis

class TeamTooLong(PatternAnalysis):

    def run(self) -> List[PatternEvent]:
        print(f'Pattern computed!')



