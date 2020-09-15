from __future__ import annotations
import json
import os
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Dict
import numpy as np
from kloppy.domain.models import Event
import codeball.visualizations as vizs
import codeball.utils as utils
from codeball import GameDataset


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

    def add_arrow(self, event):
        if event["inverted"]:
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
        game_dataset: GameDataset,
    ):
        self.name = name
        self.code = code
        self.in_time = in_time
        self.out_time = out_time
        self.parameters = parameters
        self.game_dataset = game_dataset

    @abstractmethod
    def run(self, game_dataset: GameDataset) -> List[PatternEvent]:
        """ Runs the pattern to compute the PatternEvents"""
        raise NotImplementedError

    @abstractmethod
    def build_pattern_event(
        self, game_dataset: GameDataset
    ) -> List[PatternEvent]:
        """ Builds each pattern event"""
        raise NotImplementedError

    def from_event(self, event) -> PatternEvent:

        coordinates = []
        if np.isnan(event["end_coordinates_x"]):

            coordinates = [
                event["coordinates_x"],
                event["coordinates_y"],
            ]

            end_time = event["timestamp"]

        else:
            coordinates = [
                [event["coordinates_x"], event["coordinates_y"]],
                [event["end_coordinates_x"], event["end_coordinates_y"]],
            ]

            end_time = event["end_timestamp"]

        return PatternEvent(
            pattern_code=self.code,
            start_time=round(event["timestamp"] - self.in_time) * 1000,
            event_time=round(event["timestamp"]) * 1000,
            end_time=round(end_time + self.out_time) * 1000,
            coordinates=coordinates,
        )

    def from_interval(self, interval: list) -> PatternEvent:
        return PatternEvent(
            pattern_code=self.code,
            start_time=self.game_dataset.frame_to_misliseconds(interval[0])
            - self.in_time * 1000,
            event_time=self.game_dataset.frame_to_misliseconds(interval[0]),
            end_time=self.game_dataset.frame_to_misliseconds(interval[1])
            + self.out_time * 1000,
        )


@dataclass
class PatternsSet:
    game_dataset: GameDataset
    patterns_config: Dict = field(default_factory=dict)
    patterns: List[Pattern] = field(default_factory=list)

    def load_patterns_config(self, config_file: str):

        with open(config_file) as json_file:
            self.patterns_config = json.load(json_file)

    def initialize_patterns(self, config_file: str):

        self.load_patterns_config(config_file)

        self.patterns = []
        for pattern_config in self.patterns_config:
            if pattern_config["include"]:
                pattern = self._initialize_pattern(pattern_config)
                self.patterns.append(pattern)

    def _initialize_pattern(self, pattern_config: Dict) -> Pattern:

        import codeball

        pattern_class = getattr(codeball, pattern_config["pattern_class"])
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
