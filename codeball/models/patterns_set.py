from __future__ import annotations
import json
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Dict
from kloppy.domain.models import Event
import codeball
import codeball.models.visualizations as vizs
import codeball.utils as utils
from codeball.models import GameDataset


@dataclass
class PatternEvent:
    pattern_code: str
    start_time: float
    event_time: float
    end_time: float
    coordinates: List[float] = field(default_factory=list)
    visualizations: List[vizs.Visualization] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    def add_spotlights(self, players_codes: List[str]):
        self.visualizations = vizs.Spotlight(
            start_time=self.start_time,
            end_time=self.end_time,
            players=players_codes,
        )

    def add_team_length(self, team_code: str):
        self.visualizations.append(
            vizs.TeamSize(
                start_time=self.start_time,
                end_time=self.end_time,
                team=team_code,
                line="length",
            )
        )

    def add_pause(self, start_time: float = None, pause_time: float = 1000):
        self.visualizations.append(
            vizs.Pause(
                start_time=self.event_time,
                end_time=self.event_time,
                pause_time=pause_time,
            )
        )

    def add_arrow(self, event: Event):
        # TODO: find a better way to retrieve video based coordinates vs field coordinates
        # when the event has been inverted.
        if event.inverted:
            points = {
                "start": {
                    "x": -self.coordinates[0][0] + 1,
                    "y": -self.coordinates[0][1] + 1,
                },
                "end": {
                    "x": -self.coordinates[1][0] + 1,
                    "y": -self.coordinates[1][1] + 1,
                },
            }
        else:
            points = {
                "start": {
                    "x": self.coordinates[0][0],
                    "y": self.coordinates[0][1],
                },
                "end": {
                    "x": self.coordinates[1][0],
                    "y": self.coordinates[1][1],
                },
            }

        self.visualizations.append(
            vizs.Arrow(
                start_time=self.event_time,
                end_time=self.event_time,
                points=points,
                options={"pinned": True, "width": 0.3},
            )
        )


@dataclass
class Pattern(ABC):
    def __init__(
        self,
        name: str,
        code: str,
        in_time: int,
        out_time: int,
        parameters: dict,
    ):
        self.name = name
        self.code = code
        self.in_time = in_time
        self.out_time = out_time
        self.parameters = parameters

    @abstractmethod
    def run(self, game_dataset: GameDataset) -> List[PatternEvent]:
        """ Runs the pattern to compute the PatternEvents"""
        raise NotImplementedError

    def from_event(self, event: Event) -> PatternEvent:

        coordinates = []
        if hasattr(event, "coordinates") and event.coordinates is not None:
            if (
                hasattr(event, "receiver_coordinates")
                and event.receiver_coordinates is not None
            ):
                coordinates = [
                    [event.coordinates.x, event.coordinates.y],
                    [
                        event.receiver_coordinates.x,
                        event.receiver_coordinates.y,
                    ],
                ]
            else:
                coordinates = [
                    event.coordinates.x,
                    event.coordinates.y,
                ]

        return PatternEvent(
            pattern_code=self.code,
            start_time=round(event.raw_event["start"]["time"] - self.in_time)
            * 1000,
            event_time=round(event.raw_event["start"]["time"]) * 1000,
            end_time=round(event.raw_event["end"]["time"] + self.out_time)
            * 1000,
            coordinates=coordinates,
        )

    def from_interval(self, interval: list) -> PatternEvent:
        return PatternEvent(
            pattern_code=self.code,
            start_time=utils.frame_to_milisecond(interval[0], 25)
            - self.in_time * 1000,
            event_time=utils.frame_to_milisecond(interval[0], 25),
            end_time=utils.frame_to_milisecond(interval[1], 25)
            + self.out_time * 1000,
        )


@dataclass
class PatternsSet:
    game_dataset: GameDataset
    patterns_config: Dict = field(default_factory=dict)
    patterns: List[Pattern] = field(default_factory=list)

    def load_patterns_config(self):
        self.patterns_config = codeball.get_patterns_config()

    def initialize_patterns(self):

        self.load_patterns_config()

        self.patterns = []
        for pattern_config in self.patterns_config:
            if pattern_config["include"]:
                pattern = self._initialize_pattern(pattern_config)
                self.patterns.append(pattern)

    def _initialize_pattern(self, pattern_config: Dict) -> Pattern:

        pattern_class = pattern_config["pattern_class"]
        pattern = pattern_class(
            game_dataset=self.game_dataset,
            name=pattern_config["name"],
            code=pattern_config["code"],
            parameters=pattern_config["parameters"],
            in_time=pattern_config["in_time"]
            if "in_time" in pattern_config
            else 0,
            out_time=pattern_config["out_time"]
            if "out_time" in pattern_config
            else 0,
        )

        return pattern

    def run_patterns(self):
        for pattern in self.patterns:
            pattern.events = pattern.run()

    def save_patterns_for_play(self, file_path: str):
        events_for_json = self._get_event_for_json()
        patterns_config = self._get_patterns_config_for_json()

        json_file_data = {
            "events": events_for_json,
            "insert": {"patterns": patterns_config},
        }

        with open(file_path, "w") as f:
            json.dump(json_file_data, f, cls=utils.DataClassEncoder, indent=4)

    def _get_event_for_json(self):
        events_for_json = []
        for pattern in self.patterns:
            events_for_json = events_for_json + pattern.events

        return events_for_json

    def _get_patterns_config_for_json(self):
        patterns_config = []
        for pattern in self.patterns_config:
            pattern_config = {"name": pattern["name"], "code": pattern["code"]}
            patterns_config.append(pattern_config)

        return patterns_config
