from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional, List, Dict
from enum import Enum
import pandas as pd
from kloppy.domain.models import Dataset, Team
from kloppy import (
    load_epts_tracking_data,
    load_metrica_json_event_data,
    to_pandas,
)


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
    tracking: DataPackage = None
    events: DataPackage = None

    @classmethod
    def initialize_game_dataset(
        cls,
        tracking_metadata_file: str,
        tracking_data_file: str = None,
        events_data_file: str = None,
        events_metadata_file: str = None,
    ) -> GameDataset:

        tracking_data_package = (
            DataPackage(
                data_type=DataType.TRACKING,
                data_file=tracking_data_file,
                metadata_file=tracking_metadata_file,
            )
            if tracking_data_file
            else None
        )

        events_data_package = (
            DataPackage(
                data_type=DataType.EVENT,
                data_file=events_data_file,
                metadata_file=events_metadata_file,
            )
            if events_data_file
            else None
        )

        return cls(tracking=tracking_data_package, events=events_data_package,)

    @property
    def game_dataset_type(self) -> GameDatasetType:
        if self.tracking is not None and self.tracking is not None:
            # TODO: handle different providers when available in the EPTS dataset
            return GameDatasetType.FULL_SAME_PROVIDER

        if self.tracking is not None:
            return GameDatasetType.ONLY_TRACKING

        if self.events is not None:
            return GameDatasetType.ONLY_EVENTS

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

    def load_data(self):
        if self.tracking is not None:
            self.tracking.load_dataset()
            self.tracking.build_dataframe()

        if self.events is not None:
            self.events.load_dataset()
            self.events.build_dataframe()
