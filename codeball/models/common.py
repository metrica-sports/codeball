import json
from dataclasses import dataclass, field
from typing import Optional, List, Dict, TYPE_CHECKING
from enum import Enum
import pandas as pd
from kloppy.domain.models import Dataset, Team
from kloppy import (
    load_epts_tracking_data,
    load_metrica_json_event_data,
    to_pandas,
)
from codeball.models.visualizations import Visualization
import codeball
import codeball.utils as utils


if TYPE_CHECKING:
    from codeball.patterns.base import PatternAnalysis


@dataclass
class Coordinate:
    x: float
    y: float


@dataclass
class PatternEvent:
    pattern: str
    start_time: float
    event_time: float
    end_time: float
    coordinates: List[Coordinate] = field(default_factory=list)
    visualizations: List[Visualization] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)


@dataclass
class Pattern:
    name: str
    code: str
    in_time: int = 0
    out_time: int = 0
    events: List[PatternEvent] = field(default_factory=list)


class DataType(Enum):
    TRACKING = "tracking"
    EVENT = "event"


@dataclass
class DataPackage:
    data_type: DataType
    data_file: str
    metadata_file: str = None
    dataset: Dataset = None
    dataframe: pd.DataFrame = None

    def load_dataset(self):

        if self.data_type == DataType.TRACKING:
            self.dataset = load_epts_tracking_data(
                metadata_filename=self.metadata_file,
                raw_data_filename=self.data_file,
            )

        if self.data_type == DataType.EVENT:
            self.dataset = load_metrica_json_event_data(
                metadata_filename=self.metadata_file,
                raw_data_filename=self.data_file,
            )

    def build_dataframe(self):
        self.dataframe = to_pandas(self.dataset)

    def get_team_dataframe(
        self, team_code: str, with_goalkeeper: bool = True
    ) -> pd.DataFrame:

        if self.data_type == DataType.TRACKING:
            team = self.get_team_by_code(team_code)

            players_ids = self.get_players_ids_for_team(
                team=team, with_goalkeeper=with_goalkeeper
            )

            column_names = []
            for player_id in players_ids:
                column_names.extend([player_id + "_x", player_id + "_y"])

            return self.dataframe[column_names]

    def get_team_by_code(self, team_code: str):
        for team in self.dataset.metadata.teams:
            if team.team_id == team_code:
                return team

    def get_players_ids_for_team(self, team: Team, with_goalkeeper: bool):
        if with_goalkeeper:
            return [player.player_id for player in team.players]
        else:
            return [
                player.player_id
                for player in team.players
                if player.position.name != "Goalkeeper"
            ]


class GameDatasetType(Enum):
    ONLY_TRACKING = "only_tracking"
    ONLY_EVENTS = "only_events"
    FULL_SAME_PROVIDER = "full_same_provider"
    FULL_MIXED_PROVIDERS = "full_mixed_providers"


@dataclass
class GameDataset:
    game_dataset_type: GameDatasetType = None
    tracking: DataPackage = None
    events: DataPackage = None
    patterns_config: Dict = field(default_factory=dict)
    patterns: List[Pattern] = field(default_factory=list)

    @property
    def metadata(self):
        if self.game_dataset_type == GameDatasetType.ONLY_TRACKING:
            return self.tracking.dataset.metadata

        if self.game_dataset_type == GameDatasetType.ONLY_EVENTS:
            return self.events.dataset.metadata

        if self.game_dataset_type == GameDatasetType.FULL_SAME_PROVIDER:
            return self.tracking.dataset.metadata

        if self.game_dataset_type == GameDatasetType.FULL_MIXED_PROVIDERS:
            raise AttributeError(
                f"Can't retrieve a common metadata for the game_dataset "
                f"because it's of type: {self.game_dataset_type}"
            )

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
            self, pattern, pattern_analysis_config["parameters"]
        )

    def run_patterns(self):
        for pattern in self.patterns:
            for analysis in pattern.pattern_analysis:
                pattern.events = pattern.events + analysis.run()

    def save_patterns_for_play(self, file_path: str):
        events_for_json = self._get_event_for_json()
        patterns_config = self._get_patterns_config()

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

    def _get_patterns_config(self):
        patterns_config = []
        for pattern in self.patterns_config:
            pattern_config = {"name": pattern["name"], "code": pattern["code"]}
            patterns_config.append(pattern_config)

        return patterns_config


def initialize_game_dataset(
    metadata_file: str,
    tracking_data_file: str = None,
    events_data_file: str = None,
) -> GameDataset:

    tracking_data_package = (
        _initialize_data_package(
            data_type=DataType.TRACKING,
            data_file=tracking_data_file,
            metadata_file=metadata_file,
        )
        if tracking_data_file
        else None
    )

    events_data_package = (
        _initialize_data_package(
            data_type=DataType.EVENT,
            data_file=events_data_file,
            metadata_file=metadata_file,
        )
        if events_data_file
        else None
    )

    game_dataset_type = _get_game_dataset_type(
        tracking_data_package, events_data_package
    )

    return GameDataset(
        game_dataset_type=game_dataset_type,
        tracking=tracking_data_package,
        events=events_data_package,
    )


def _get_game_dataset_type(
    tracking_data_package: DataPackage, events_data_package: DataPackage,
) -> GameDatasetType:

    if tracking_data_package is not None and events_data_package is not None:
        # TODO: handle different providers when available in the EPTS dataset
        return GameDatasetType.FULL_SAME_PROVIDER

    if tracking_data_package is not None:
        return GameDatasetType.ONLY_TRACKING

    if events_data_package is not None:
        return GameDatasetType.ONLY_EVENTS


def _initialize_data_package(
    data_type: DataType, data_file: str, metadata_file: str
) -> DataPackage:

    data_package = DataPackage(
        data_type=data_type, data_file=data_file, metadata_file=metadata_file,
    )

    data_package.load_dataset()

    data_package.build_dataframe()

    return data_package
