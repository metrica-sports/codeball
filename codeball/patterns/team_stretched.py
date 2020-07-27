from typing import List
from codeball.models import PatternEvent
import codeball.models.visualizations as vizs
from .base import PatternAnalysis
import codeball.utils as utils
import pandas as pd


class TeamStretched(PatternAnalysis):
    """
        This pattern computes moments in the game in which the length of the
        team exceeds a cartain value for more than one second and returns those
        moments with a TeamSize length visualization for the duration of the infringement.

        Attributes:
            team: str
                code of the team (for now home or away)
            threshold: float
                What is the stretch threshold in meters
    """

    def __init__(self, game_dataset, pattern, parameters):
        super().__init__(game_dataset, pattern)
        self.team_code = parameters["team_code"]
        self.threshold = parameters["threshold"]

    def run(self) -> List[PatternEvent]:

        team_dataframe = self.game_dataset.tracking.get_team_tracking_dataframe(
            self.team_code, with_goalkeeper=False
        )

        stretched_frames = self.find_stretched_frames(team_dataframe)

        intervals = utils.find_intervals(stretched_frames)

        pattern_events = self.build_pattern_events(intervals=intervals)

        return pattern_events

    def find_stretched_frames(self, team_dataframe: pd.DataFrame) -> pd.Series:
        team_x_coordinates = team_dataframe.filter(regex="_x")
        team_span = team_x_coordinates.max(axis=1) - team_x_coordinates.min(
            axis=1
        )
        # TODO Only take into account moments with ball in play. Could also be attack or defence.
        # TODO replace 105 with field actual size
        team_stretched = team_span > self.threshold / 105
        return team_stretched

    def build_pattern_events(self, intervals: List[int]) -> List[PatternEvent]:

        pattern_events = []
        for i in intervals:
            viz = self.build_visualization(interval=i)
            event = self.build_event(interval=i, visualization=viz)
            pattern_events.append(event)

        return pattern_events

    def build_visualization(self, interval: List[int]) -> vizs.TeamSize:

        return vizs.TeamSize(
            start_time=utils.frame_to_milisecond(interval[0], 25),
            end_time=utils.frame_to_milisecond(interval[1], 25),
            team="T016",
            line="length",
        )

    def build_event(
        self, interval: List[int], visualization: vizs.TeamSize
    ) -> PatternEvent:

        return PatternEvent(
            self.pattern.code,
            utils.frame_to_milisecond(interval[0], 25),
            utils.frame_to_milisecond(interval[0], 25),
            utils.frame_to_milisecond(interval[1], 25),
            visualizations=visualization,
            tags="ESPRMA",
        )
