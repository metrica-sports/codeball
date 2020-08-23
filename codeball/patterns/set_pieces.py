from typing import List
from codeball.models import PatternEvent, Pattern, GameDataset


class SetPieces(Pattern):
    """
        This pattern computes Set Pieces (kick offs, throw ins, corner kicks,
        penalties, free kicks)

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

    def run(self) -> List[PatternEvent]:

        set_piece_events = self.game_dataset.set_pieces()

        return [self.build_pattern_event(event) for event in set_piece_events]

    def build_pattern_event(self, event: dict, event_idx=int) -> PatternEvent:
        pattern_event = self.from_event(event)
        pattern_event.add_spotlights(event.raw_event["from"]["id"])
        pattern_event.tags = event.raw_event["team"]["id"]
        pattern_event.coordinates = [
            self.game_dataset.events.dataset.records[
                event.raw_event["index"]
            ].raw_event["start"]["x"],
            self.game_dataset.events.dataset.records[
                event.raw_event["index"]
            ].raw_event["start"]["y"],
        ]

        if event.inverted:
            pattern_event.coordinates = [
                -pattern_event.coordinates[0] + 1,
                -pattern_event.coordinates[1] + 1,
            ]

        return pattern_event
