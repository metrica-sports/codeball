from typing import List
from kloppy.domain import EventType, PassResult
from codeball.models import PatternEvent, Pattern, GameDataset
from codeball.models import Zone
import codeball.models.visualizations as vizs


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
        super().__init__(name, code, in_time, out_time, parameters)
        self.game_dataset = game_dataset

    def run(self) -> List[PatternEvent]:

        passes = self.game_dataset.passes(
            into=Zone.OPPONENT_BOX, result=PassResult.COMPLETE
        )

        pattern_events = [self.build_pattern_event(event) for event in passes]

        return pattern_events

    def build_pattern_event(self, event) -> PatternEvent:
        pattern_event = self.from_event(event)
        pattern_event.add_arrow(event)
        pattern_event.add_pause(pause_time=2000)

        return pattern_event
