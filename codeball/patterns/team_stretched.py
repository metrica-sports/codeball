from typing import List
from codeball.models import PatternEvent, Pattern, GameDataset


class TeamStretched(Pattern):
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

    def __init__(
        self,
        game_dataset: GameDataset,
        name: str,
        code: str,
        in_time: int = 0,
        out_time: int = 0,
        parameters: dict = None,
    ):
        super().__init__(name, code, in_time, out_time, parameters)
        self.game_dataset = game_dataset
        self.team_code = self.parameters["team_code"]
        self.threshold = self.parameters["threshold"]

    def run(self) -> List[PatternEvent]:

        stretched_intervals = self.game_dataset.stretched_frames_for_team(
            team_code=self.team_code, threshold=self.threshold
        )

        return [
            self.build_pattern_event(interval)
            for interval in stretched_intervals
        ]

    def build_pattern_event(self, interval: List[int]) -> PatternEvent:
        pattern_event = self.from_interval(interval)
        pattern_event.add_team_length(team_code=self.team_code)
        pattern_event.tags = self.team_code

        return pattern_event
