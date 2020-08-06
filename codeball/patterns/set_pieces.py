from typing import List
from codeball.models import PatternEvent
import codeball.models.visualizations as vizs
from .base import PatternAnalysis
import codeball.utils as utils
import pandas as pd


class SetPieces(PatternAnalysis):
    """
        This pattern computes Set Pieces (kick offs, throw ins, corner kicks,
        penalties, free kicks)

    """

    def __init__(self, game_dataset, pattern, parameters):
        super().__init__(game_dataset, pattern, parameters)

    def run(self) -> List[PatternEvent]:
        pattern_events = []
        for i, event in enumerate(self.game_dataset.events.dataset.records):
            if event.raw_event["type"]["id"] == 5:
                pattern_event = PatternEvent.create_from_event(
                    pattern_code=self.pattern.code, event_dict=event.raw_event,
                )
                pattern_event.add_spotlights(event.raw_event["from"]["id"])
                pattern_event.tags = event.raw_event["team"]["id"]
                pattern_event.coordinates = [
                    self.game_dataset.events.dataset.records[i + 1].raw_event[
                        "start"
                    ]["x"],
                    self.game_dataset.events.dataset.records[i + 1].raw_event[
                        "start"
                    ]["y"],
                ]
                pattern_events.append(pattern_event)

        return pattern_events