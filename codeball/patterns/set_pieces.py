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

        return [
            self.build_pattern_event(event_dict=event.raw_event)
            for event in set_piece_events
        ]

    def build_pattern_event(
        self, event_dict: dict, event_idx=int
    ) -> PatternEvent:
        pattern_event = self.from_event(event_dict)
        pattern_event.add_spotlights(event_dict["from"]["id"])
        pattern_event.tags = event_dict["team"]["id"]
        pattern_event.coordinates = [
            self.game_dataset.events.dataset.records[
                event_dict["index"] + 1
            ].raw_event["start"]["x"],
            self.game_dataset.events.dataset.records[
                event_dict["index"] + 1
            ].raw_event["start"]["y"],
        ]

        return pattern_event
