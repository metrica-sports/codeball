from __future__ import annotations
import json
from dataclasses import dataclass, field
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
class Pattern:
    name: str
    code: str
    in_time: int = 0
    out_time: int = 0
    events: List[PatternEvent] = field(default_factory=list)


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

    def _initialize_pattern(self, pattern_config: Dict):
        pattern = Pattern(
            name=pattern_config["name"], code=pattern_config["code"]
        )

        pattern.pattern_analysis = []
        for pattern_analysis_config in pattern_config["pattern_analysis"]:
            pattern_analysis = self._initialize_pattern_analysis(
                pattern, pattern_analysis_config
            )
            pattern.pattern_analysis.append(pattern_analysis)

        return pattern

    def _initialize_pattern_analysis(
        self, pattern: Pattern, pattern_analysis_config: dict
    ):
        pattern_analysis_class = pattern_analysis_config["class"]
        return pattern_analysis_class(
            self.game_dataset, pattern, pattern_analysis_config["parameters"]
        )

    def run_patterns(self):
        for pattern in self.patterns:
            for analysis in pattern.pattern_analysis:
                pattern.events = pattern.events + analysis.run()

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