from typing import List
from kloppy.domain import EventType, PassResult
from codeball.models import PatternEvent, Pattern, GameDataset
import codeball.models.visualizations as vizs


class PassesIntoTheBox(Pattern):
    """
        Pattern documentation
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

        # self.game_dataset.get_events(
        #     event_type=EventType.PASS,
        #     to=ZoneType.OPPONENT_BOX,
        #     outcome=PassResult.COMPLETE
        # )
        passes = []
        for event in self.game_dataset.events.dataset.records:
            if event.event_type == EventType.PASS:
                if event.result == PassResult.COMPLETE:
                    ends_in_box = (
                        event.receiver_coordinates.x >= 0.84
                        and 0.2 <= event.receiver_coordinates.y <= 0.8
                    )
                    starts_outside = event.coordinates.x < 0.8
                    if ends_in_box and starts_outside:
                        passes.append(event)

        pattern_events = []
        for event in passes:
            pattern_event = self.from_event(event_dict=event.raw_event)
            pattern_event.coordinates = [
                [event.raw_event["start"]["x"], event.raw_event["start"]["y"]],
                [event.raw_event["end"]["x"], event.raw_event["end"]["y"]],
            ]
            pattern_event.visualizations.append(
                vizs.Arrow(
                    start_time=pattern_event.event_time,
                    end_time=pattern_event.event_time,
                    points={
                        "start": {
                            "x": event.raw_event["start"]["x"],
                            "y": event.raw_event["start"]["y"],
                        },
                        "end": {
                            "x": event.raw_event["end"]["x"],
                            "y": event.raw_event["end"]["y"],
                        },
                    },
                    options={"pinned": True, "width": 0.3},
                )
            )
            pattern_event.visualizations.append(
                vizs.Pause(
                    start_time=pattern_event.event_time,
                    end_time=pattern_event.event_time,
                    pause_time=2000,
                )
            )
            pattern_events.append(pattern_event)

        return pattern_events

    def build_pattern_event(self) -> PatternEvent:
        pass
