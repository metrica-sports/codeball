from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional, List, Dict
from enum import Enum
import pandas as pd
from kloppy.domain import (
    Dataset,
    Team,
    EventType,
    ResultType,
    AttackingDirection,
    Ground,
    Point,
)
from kloppy import (
    load_epts_tracking_data,
    load_metrica_json_event_data,
    to_pandas,
)

import codeball.utils as utils
from codeball.tactical import Zones, Possession
from codeball.codeball_frames import (
    EventsFrame,
    TrackingFrame,
    PossessionsFrame,
)


class DataType(Enum):
    TRACKING = "tracking"
    EVENT = "event"


class GameDatasetType(Enum):
    ONLY_TRACKING = "only_tracking"
    ONLY_EVENTS = "only_events"
    FULL_SAME_PROVIDER = "full_same_provider"
    FULL_MIXED_PROVIDERS = "full_mixed_providers"


class GameDataset:
    def __init__(
        self,
        tracking_metadata_file=None,
        tracking_data_file=None,
        events_metadata_file=None,
        events_data_file=None,
    ):
        self.files = {
            "tracking_metadata_file": tracking_metadata_file,
            "tracking_data_file": tracking_data_file,
            "events_metadata_file": events_metadata_file,
            "events_data_file": events_data_file,
        }

        if tracking_data_file is not None:
            tracking_dataset = load_epts_tracking_data(
                metadata_filename=tracking_metadata_file,
                raw_data_filename=tracking_data_file,
            )
            self.tracking = TrackingFrame(to_pandas(tracking_dataset))
            self.tracking.data_type = DataType.TRACKING
            self.tracking.metadata = tracking_dataset.metadata
            self.tracking.records = tracking_dataset.records
        else:
            self.tracking = None

        if events_data_file is not None:
            events_dataset = load_metrica_json_event_data(
                metadata_filename=events_metadata_file,
                raw_data_filename=events_data_file,
            )
            self.events = EventsFrame(to_pandas(events_dataset))
            self.events.data_type = DataType.EVENT
            self.events.metadata = events_dataset.metadata
            self.events.records = events_dataset.records
        else:
            self.events = None

        self._enrich_data()

    @property
    def game_dataset_type(self) -> GameDatasetType:
        if self.has_tracking_data and self.has_event_data:
            # TODO: handle different providers when available in the EPTS dataset
            return GameDatasetType.FULL_SAME_PROVIDER

        if self.has_tracking_data:
            return GameDatasetType.ONLY_TRACKING

        if self.has_event_data:
            return GameDatasetType.ONLY_EVENTS

    @property
    def metadata(self):
        if self.game_dataset_type == GameDatasetType.ONLY_TRACKING:
            return self.tracking.metadata

        if self.game_dataset_type == GameDatasetType.ONLY_EVENTS:
            return self.events.metadata

        if self.game_dataset_type == GameDatasetType.FULL_SAME_PROVIDER:
            return self.tracking.metadata

        if self.game_dataset_type == GameDatasetType.FULL_MIXED_PROVIDERS:
            raise AttributeError(
                f"Can't retrieve a common metadata for the game_dataset "
                f"because it's of type: {self.game_dataset_type}"
            )

    @property
    def has_tracking_data(self):
        if self.tracking is None:
            return False
        else:
            return True

    @property
    def has_event_data(self):
        if self.events is None:
            return False
        else:
            return True

    def _enrich_data(self):
        if self.has_tracking_data:
            self._set_periods_attacking_direction()

        if self.has_event_data:
            self._build_possessions()
            self._enrich_events()

        if self.has_tracking_data and self.has_event_data:
            self._enrich_tracking()

    def _build_possessions(self):
        start_event_types = ["RECOVERY", "SET PIECE"]
        end_event_types = ["FAULT RECEIVED", "SHOT", "BALL OUT", "BALL LOST"]

        possessions = []
        for event in self.events.records:
            if event.raw_event["type"]["name"] in start_event_types:
                possession_start = event.timestamp

            if event.raw_event["type"]["name"] in end_event_types:
                if (
                    hasattr(event, "receive_timestamp")
                    and event.receive_timestamp
                ):
                    possession_end = event.receive_timestamp
                else:
                    possession_end = event.timestamp

                possessions.append(
                    [
                        event.raw_event["team"]["id"],
                        possession_start,
                        possession_end,
                    ]
                )

        self.possessions = PossessionsFrame(
            possessions, columns=["team_id", "start", "end"]
        )

    def _set_periods_attacking_direction(self):
        for i, period in enumerate(self.metadata.periods):

            start = period.start_timestamp
            end = period.end_timestamp
            period_idx = (self.tracking["timestamp"] >= start) & (
                self.tracking["timestamp"] <= end
            )

            home_x_mean = (
                self.tracking.team(self.metadata.teams[0].team_id)
                .dimension("x")
                .loc[period_idx]
                .mean()
                .mean()
            )

            away_x_mean = (
                self.tracking.team(self.metadata.teams[1].team_id)
                .dimension("x")
                .loc[period_idx]
                .mean()
                .mean()
            )

            # TODO: check if there is a way to set the metadata on the game_dataset and
            # get that to set the periods on each data package.
            if home_x_mean <= away_x_mean:
                self.tracking.metadata.periods[
                    i
                ].attacking_direction = AttackingDirection.HOME_AWAY

                if self.has_event_data:
                    self.events.metadata.periods[
                        i
                    ].attacking_direction = AttackingDirection.HOME_AWAY
            else:
                self.tracking.metadata.periods[
                    i
                ].attacking_direction = AttackingDirection.AWAY_HOME

                if self.has_event_data:
                    self.events.metadata.periods[
                        i
                    ].attacking_direction = AttackingDirection.AWAY_HOME

    def _enrich_events(self):
        for index, event_row in self.events.iterrows():

            team = self.events.get_team_by_id(event_row["team_id"])
            period = self.events.get_period_by_id(event_row["period_id"])

            revert_home = (
                team.ground == Ground.HOME
                and period.attacking_direction == AttackingDirection.AWAY_HOME
            )
            revert_away = (
                team.ground == Ground.AWAY
                and period.attacking_direction == AttackingDirection.HOME_AWAY
            )

            if revert_home or revert_away:

                self.events.at[index, "inverted"] = True

                self.events.at[index, "coordinates_x"] = (
                    -event_row["coordinates_x"] + 1
                )
                self.events.at[index, "coordinates_y"] = (
                    -event_row["coordinates_y"] + 1
                )

                self.events.at[index, "end_coordinates_x"] = (
                    -event_row["end_coordinates_x"] + 1
                )
                self.events.at[index, "end_coordinates_y"] = (
                    -event_row["end_coordinates_y"] + 1
                )

            else:
                self.events.at[index, "inverted"] = False

        for index, event_row in self.events.iterrows():

            # Renrich set pieces with coordiants and end time of next event
            if event_row["event_type"] == "GENERIC:SET PIECE":
                self.events.at[index, "coordinates_x"] = self.events.at[
                    index + 1, "coordinates_x"
                ]
                self.events.at[index, "coordinates_y"] = self.events.at[
                    index + 1, "coordinates_y"
                ]
                self.events.at[index, "end_coordinates_x"] = self.events.at[
                    index + 1, "end_coordinates_x"
                ]
                self.events.at[index, "end_coordinates_y"] = self.events.at[
                    index + 1, "end_coordinates_y"
                ]
                self.events.at[index, "end_timestamp"] = self.events.at[
                    index + 1, "end_timestamp"
                ]

    def _enrich_tracking(self):
        for i, possession in self.possessions.iterrows():
            indexes = (self.tracking["timestamp"] >= possession["start"]) & (
                self.tracking["timestamp"] <= possession["end"]
            )
            self.tracking.loc[indexes, "ball_owning_team_id"] = possession[
                "team_id"
            ]

    def find_intervals(
        self, boolean_series: pd.Series, minimum_interval: float = 5
    ) -> List:
        intervals = []
        interval_open = False
        for i, f in enumerate(boolean_series):
            if f is True and interval_open is False:
                interval_open = True
                start_interval = i
            elif f is False and interval_open is True:
                interval_open = False
                end_interval = i - 1
                if (
                    end_interval - start_interval
                ) > self.tracking.metadata.frame_rate * minimum_interval:
                    intervals.append([start_interval, end_interval])

        return intervals

    def frame_to_misliseconds(self, frame: int) -> float:
        return frame * 1000 / self.tracking.metadata.frame_rate
