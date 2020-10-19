from typing import List
from codeball import GameDataset, Zones
from codeball.patterns import PatternEvent, Pattern


class PassesIntoTheBox(Pattern):
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
            .into(Zones.OPPONENT_BOX)
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
