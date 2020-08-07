from __future__ import annotations
import json
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Dict
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

    @classmethod
    def create_from_event(
        cls, pattern_code: str, event_dict: dict
    ) -> PatternEvent:

        return cls(
            pattern_code=pattern_code,
            start_time=round(event_dict["start"]["time"] - 2) * 1000,
            event_time=round(event_dict["start"]["time"]) * 1000,
            end_time=round(event_dict["end"]["time"] + 2) * 1000,
        )

    def add_spotlights(self, players_codes: List[str]):
        self.visualizations = vizs.Spotlight(
            start_time=self.start_time,
            end_time=self.end_time,
            players=players_codes,
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
