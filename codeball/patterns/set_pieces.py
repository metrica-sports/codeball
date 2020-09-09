from typing import List
from codeball import GameDataset
from codeball.patterns import PatternEvent, Pattern


class SetPieces(Pattern):
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

    def run(self) -> List[PatternEvent]:

        set_pieces = self.game_dataset.events.type("GENERIC:SET PIECE")

        return [
            self.build_pattern_event(event_row)
            for i, event_row in set_pieces.iterrows()
        ]

    def build_pattern_event(self, event_row) -> PatternEvent:
        pattern_event = self.from_event(event_row)
        pattern_event.add_spotlights(event_row["player_id"])
        pattern_event.tags = event_row["team_id"]
        return pattern_event
