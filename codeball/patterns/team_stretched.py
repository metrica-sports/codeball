"""
    This pattern computes moments in the game in which the length of the
    team exceeds a cartain value for more than one second and returns those
    moments with a length visualization for the duration of the infringement.

    It takes two init fields:
        team: str -> code of the team
        threshold: float -> What is the stretch threshold in the interval [0.0,1.0]
"""
from typing import List
from codeball.models import PatternEvent
import codeball.models.visualizations as vizs
from .base import PatternAnalysis


class TeamStretched(PatternAnalysis):
    def __init__(self, game_dataset, pattern, team_code, threshold):
        super().__init__(game_dataset, pattern)
        self.team_code = team_code
        self.threshold = threshold

    def run(self) -> List[PatternEvent]:
        match_string = self.team_code + "_[0-9]+_x"
        # TODO Also filter goalkeeper so only field players left
        team_dataframe = self.game_dataset.data.filter(regex=match_string)
        team_span = team_dataframe.max(axis=1) - team_dataframe.min(axis=1)
        # TODO Only take into account moments with ball in play. Could also be attack or defence.
        team_stretched = team_span > self.threshold

        # TODO Refactor to utils folder
        intervals = []
        interval_open = False
        for i, f in enumerate(team_stretched):
            if f is True and interval_open is False:
                interval_open = True
                start_interval = i
            elif f is False and interval_open is True:
                interval_open = False
                intervals.append([start_interval, i - 1])

        pattern_events = []
        for i in intervals:
            # TODO change visualization for a team length one (currently crashing Play)
            visualization = vizs.PlayersVisualization(
                start_time=i[0] * 1000 / 25,
                end_time=i[1] * 1000 / 25,
                players="P2288",
                options={"spotlight": True},
            )

            pattern_events.append(
                PatternEvent(
                    self.pattern.code,
                    i[0] * 1000 / 25,
                    i[0] * 1000 / 25,
                    i[1] * 1000 / 25,
                    visualizations=visualization,
                    tags="ESPRMA",
                )
            )

        return pattern_events
