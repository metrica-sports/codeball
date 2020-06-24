"""
    This pattern computes moments in the game in which the length of the
    team exceeds a cartain value for more than one second and returns those
    moments with a length visualization for the duration of the infringement.

    It takes two init fields:
        team: str -> code of the team: for now home or away
        threshold: float -> What is the stretch threshold in meters
"""
from typing import List
from codeball.models import PatternEvent
import codeball.models.visualizations as vizs
from .base import PatternAnalysis
import codeball.utils as utils
import pandas as pd


class TeamStretched(PatternAnalysis):
    def __init__(self, game_dataset, pattern, team_code, threshold):
        super().__init__(game_dataset, pattern)
        self.team_code = team_code
        self.threshold = threshold

    def run(self) -> List[PatternEvent]:

        team_dataframe = utils.get_team_dataframe(
            self.game_dataset.data, self.team_code
        )

        # Drop goalkeeper to only leave field players.
        field_players_dataframe = team_dataframe.drop(
            columns="player_home_13_x"
        )

        stretched_frames = self.find_stretched_frames(field_players_dataframe)

        intervals = utils.find_intervals(stretched_frames)

        pattern_events = []
        for i in intervals:

            visualization = vizs.TeamSize(
                start_time=utils.frame_to_milisecond(i[0], 25),
                end_time=utils.frame_to_milisecond(i[1], 25),
                team="T016",
                line="length",
            )

            pattern_events.append(
                PatternEvent(
                    self.pattern.code,
                    utils.frame_to_milisecond(i[0], 25),
                    utils.frame_to_milisecond(i[0], 25),
                    utils.frame_to_milisecond(i[1], 25),
                    visualizations=visualization,
                    tags="ESPRMA",
                )
            )

        return pattern_events

    def find_stretched_frames(self, team_dataframe: pd.DataFrame) -> pd.Series:
        team_span = team_dataframe.max(axis=1) - team_dataframe.min(axis=1)
        # TODO Only take into account moments with ball in play. Could also be attack or defence.
        # TODO replace 105 with field actual size
        team_stretched = team_span > self.threshold / 105
        return team_stretched
