from typing import List
from kloppy.domain import EventType, PassResult
from codeball import GameDataset, Zone
from codeball.patterns import PatternEvent, Pattern


class PassesIntoTheBox(Pattern):
    """
    This pattern finds completed passes into the opponent box. For each one of those
    passes, it creates a pattern event that displays an arrow at the moment of the
    pass and a pause of 2s.
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
        super().__init__(
            name, code, in_time, out_time, parameters, game_dataset
        )

    def run(self) -> List[PatternEvent]:

        passes_into_the_box = (
            self.game_dataset.events.type("PASS")
            .into(Zone.OPPONENT_BOX)
            .result("COMPLETE")
        )

        return [
            self.build_pattern_event(event_row)
            for i, event_row in passes_into_the_box.iterrows()
        ]

    def build_pattern_event(self, event_row) -> PatternEvent:
        pattern_event = self.from_event(event_row)
        pattern_event.add_arrow(event_row)
        pattern_event.add_pause(pause_time=2000)

        return pattern_event
