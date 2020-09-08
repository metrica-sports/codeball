from pandas import DataFrame, Series
from codeball.tactical import Zone


class BaseDataFrame(DataFrame):
    """This is a base dataframe"""

    _internal_names = DataFrame._internal_names + ["records"]
    _internal_names_set = set(_internal_names)

    _metadata = ["metadata", "data_type"]

    @property
    def _constructor(self):
        return BaseDataFrame

    def get_team_by_id(self, team_id):
        return next(
            team for team in self.metadata.teams if team.team_id == team_id
        )

    def get_period_by_id(self, period_id):
        return next(
            period
            for period in self.metadata.periods
            if period.id == period_id
        )

    def get_other_team_id(self, team_id):
        if self.metadata.teams[0].team_id == team_id:
            return self.metadata.teams[1].team_id

        if self.metadata.teams[1].team_id == team_id:
            return self.metadata.teams[0].team_id


class TrackingDataFrame(BaseDataFrame):
    @property
    def _constructor(self):
        return TrackingDataFrame

    def team(self, team_id):
        team = self.get_team_by_id(team_id)
        players_ids = [player.player_id for player in team.players]

        column_names = []
        for player_id in players_ids:
            if f"{player_id}_x" in self.columns:
                column_names.extend([f"{player_id}_x", f"{player_id}_y"])

        return self[column_names]

    def dimension(self, dimension):
        return self.filter(regex=f"_{dimension}")

    def players(self, group=None):

        column_names = []
        for team in self.metadata.teams:
            for player in team.players:
                if f"{player.player_id}_x" in self.columns:
                    column_names.extend(
                        [f"{player.player_id}_x", f"{player.player_id}_y"]
                    )

        if group == "field":
            for team in self.metadata.teams:
                for player in team.players:
                    if player.position.position_id == 0:
                        if f"{player.player_id}_x" in column_names:
                            column_names.remove(f"{player.player_id}_x")
                        if f"{player.player_id}_y" in column_names:
                            column_names.remove(f"{player.player_id}_y")

        return self[column_names]

    def phase(self, defending_team_id=None, attacking_team_id=None):

        if defending_team_id:
            attacking_team_id = self.get_other_team_id(defending_team_id)

        if attacking_team_id:
            return self["ball_owning_team_id"] == attacking_team_id

    def stretched(self, threshold):
        team_span = self.max(axis=1) - self.min(axis=1)
        pitch_length = (
            self.metadata.pitch_dimensions.x_dim.max
            / self.metadata.pitch_dimensions.x_per_meter
        )
        return team_span > (threshold / pitch_length)


class EventsDataFrame(BaseDataFrame):

    _internal_names = DataFrame._internal_names + ["records"]
    _internal_names_set = set(_internal_names)

    _metadata = ["metadata", "data_type"]

    @property
    def _constructor(self):
        return EventsDataFrame

    def type(self, type):
        return self.loc[self["event_type"] == type]

    def result(self, result):
        return self.loc[self["result"] == result]

    def into(self, zone: Zone):
        return self.starts_outside(zone).ends_inside(zone)

    def starts_inside(self, zone: Zone):
        for i, box in enumerate(zone.boxes):
            x_indexes = (self["coordinates_x"] > box.top_left[0]) & (
                self["coordinates_x"] < box.bottom_right[0]
            )
            y_indexes = (self["coordinates_y"] > box.top_left[1]) & (
                self["coordinates_y"] < box.bottom_right[1]
            )
            box_indexes = x_indexes & y_indexes
            if i == 0:
                event_idexes = box_indexes
            else:
                event_idexes = event_idexes | box_indexes

        return self.loc[event_idexes]

    def starts_outside(self, zone: Zone):
        for i, box in enumerate(zone.boxes):
            x_indexes = (self["coordinates_x"] < box.top_left[0]) | (
                self["coordinates_x"] > box.bottom_right[0]
            )
            y_indexes = (self["coordinates_y"] < box.top_left[1]) | (
                self["coordinates_y"] > box.bottom_right[1]
            )
            box_indexes = x_indexes | y_indexes
            if i == 0:
                event_idexes = box_indexes
            else:
                event_idexes = event_idexes | box_indexes

        return self.loc[event_idexes]

    def ends_inside(self, zone: Zone):
        for i, box in enumerate(zone.boxes):
            x_indexes = (self["end_coordinates_x"] > box.top_left[0]) & (
                self["end_coordinates_x"] < box.bottom_right[0]
            )
            y_indexes = (self["end_coordinates_y"] > box.top_left[1]) & (
                self["end_coordinates_y"] < box.bottom_right[1]
            )
            box_indexes = x_indexes & y_indexes
            if i == 0:
                event_idexes = box_indexes
            else:
                event_idexes = event_idexes | box_indexes

        return self.loc[event_idexes]

    def ends_outside(self, zone: Zone):
        for i, box in enumerate(zone.boxes):
            x_indexes = (self["end_coordinates_x"] < box.top_left[0]) | (
                self["end_coordinates_x"] > box.bottom_right[0]
            )
            y_indexes = (self["end_coordinates_y"] < box.top_left[1]) | (
                self["end_coordinates_y"] > box.bottom_right[1]
            )
            box_indexes = x_indexes | y_indexes
            if i == 0:
                event_idexes = box_indexes
            else:
                event_idexes = event_idexes | box_indexes

        return self.loc[event_idexes]


class PossessionsDataFrame(BaseDataFrame):
    @property
    def _constructor(self):
        return PossessionsDataFrame
