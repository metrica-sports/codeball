"""
    This pattern computes moments in the game in which the length of the 
    team exceeds a cartain value for more than one second and returns those 
    moments with a length visualization for the duration of the infringement.
"""
from typing import List
from codeball.models import  PatternEvent
from .base import PatternAnalysis

class TeamStretched(PatternAnalysis):

    def run(self) -> List[PatternEvent]:
        match_string = self.options["team"] + "_[0-9]+_x"
        team_dataframe = self.game_dataset.data.filter(regex=match_string)
        team_span = team_dataframe.max(axis=1) - team_dataframe.min(axis=1)
        team_stretched = team_span > 0.4

        intervals = []
        interval_open = False
        for i, f in enumerate(team_stretched):
            if f is True and interval_open is False:
                interval_open = True
                start_interval = i
            elif f is False and interval_open is True:
                interval_open = False
                intervals.append([start_interval,i-1])
                 

