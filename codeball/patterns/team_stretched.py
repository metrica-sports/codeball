from typing import List
from codeball import GameDataset
from codeball.patterns import PatternEvent, Pattern


class TeamStretched(Pattern):
    def __init__(
        self,
        game_dataset: GameDataset,
        name: str,
        code: str,
        in_time: int = 0,
        out_time: int = 0,
        parameters: dict = None,
    ):
        super().__init__(
            name, code, in_time, out_time, parameters, game_dataset
        )
        self.game_dataset = game_dataset
        self.team_code = self.parameters["team_code"]
        self.threshold = self.parameters["threshold"]

    def run(self) -> List[PatternEvent]:

        # Computes frames in which the team is defending
        defending_indexes = self.game_dataset.tracking.phase(
            defending_team_id=self.team_code
        )

        # Computes frames in which the team is stretched horiontally
        stretched_indexes = (
            self.game_dataset.tracking.team(self.team_code)
            .players("field")
            .dimension("x")
            .stretched(self.threshold)
        )

        indexes = stretched_indexes & defending_indexes
        stretched_intervals = self.game_dataset.find_intervals(indexes)

        return [
            self.build_pattern_event(interval)
            for interval in stretched_intervals
        ]

    def build_pattern_event(self, interval: List[int]) -> PatternEvent:
        pattern_event = self.from_interval(interval)
        pattern_event.add_team_length(team_code=self.team_code)
        pattern_event.tags = self.team_code

        return pattern_event
