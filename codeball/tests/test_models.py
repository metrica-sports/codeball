import os

import pandas as pd

from kloppy import (
    load_epts_tracking_data,
    to_pandas,
    load_metrica_json_event_data,
)

from codeball import (
    GameDataset,
    DataType,
    TrackingFrame,
    EventsFrame,
    PossessionsFrame,
    BaseFrame,
    Zones,
    Area,
    PatternEvent,
    Pattern,
    PatternsSet,
)

import codeball.visualizations as vizs


class TestModels:
    def test_pattern_event(self):

        xy = [0.3, 0.6]

        viz = vizs.Players(
            start_time=500, end_time=700, players=[], options=[]
        )

        pattern_event = PatternEvent(
            pattern_code="MET_001",
            start_time=400,
            event_time=500,
            end_time=800,
            coordinates=[xy, xy],
            visualizations=[viz, viz],
            tags=["T001"],
        )

        assert pattern_event.end_time == 800
        assert pattern_event.coordinates[0][0] == 0.3
        assert pattern_event.visualizations[0].start_time == 500

    def test_pattern(self):
        class pattern_class(Pattern):
            def __init__(
                self,
                name: str,
                code: str,
                in_time: int = 0,
                out_time: int = 0,
                parameters: dict = None,
                game_dataset: GameDataset = None,
            ):
                super().__init__(
                    name, code, in_time, out_time, parameters, game_dataset
                )

            def run(self):
                return True

            def build_pattern_event(self):
                pass

        test_pattern = pattern_class(
            name="Test Pattern",
            code="MET_001",
            in_time=3,
            out_time=2,
            parameters=None,
            game_dataset=None,
        )

        assert test_pattern.in_time == 3
        assert test_pattern.run() is True

    def test_game_dataset(self):

        base_dir = os.path.dirname(__file__)

        game_dataset = GameDataset(
            tracking_metadata_file=f"{base_dir}/files/metadata.xml",
            tracking_data_file=f"{base_dir}/files/tracking.txt",
            events_metadata_file=f"{base_dir}/files/metadata.xml",
            events_data_file=f"{base_dir}/files/events.json",
        )

        assert game_dataset.tracking.data_type == DataType.TRACKING
        assert game_dataset.events.data_type == DataType.EVENT

    def test_tracking_game_dataset(self):

        base_dir = os.path.dirname(__file__)

        game_dataset = GameDataset(
            tracking_metadata_file=f"{base_dir}/files/metadata.xml",
            tracking_data_file=f"{base_dir}/files/tracking.txt",
        )

        assert game_dataset.tracking.data_type == DataType.TRACKING
        assert game_dataset.has_event_data is False

    def test_pattern_set(self):

        base_dir = os.path.dirname(__file__)

        game_dataset = GameDataset(
            tracking_metadata_file=f"{base_dir}/files/metadata.xml",
            tracking_data_file=f"{base_dir}/files/tracking.txt",
            events_metadata_file=f"{base_dir}/files/metadata.xml",
            events_data_file=f"{base_dir}/files/events.json",
        )

        class pattern_class(Pattern):
            def __init__(
                self,
                name: str,
                code: str,
                in_time: int = 0,
                out_time: int = 0,
                parameters: dict = None,
                game_dataset: GameDataset = None,
            ):
                super().__init__(
                    name, code, in_time, out_time, parameters, game_dataset
                )

            def run(self):
                return True

            def build_pattern_event(self):
                pass

        test_pattern = pattern_class(
            name="Test Pattern",
            code="MET_001",
            in_time=3,
            out_time=2,
            parameters=None,
            game_dataset=game_dataset,
        )

        patterns_set = PatternsSet(game_dataset=game_dataset)
        patterns_set.patterns = [test_pattern, test_pattern]

        assert patterns_set.game_dataset.events.data_type == DataType.EVENT
        assert len(patterns_set.patterns) == 2

    def test_base_data_frame(self):
        data = {
            "player1_x": [1, 2, 3, 4],
            "player2_x": [5, 6, 7, 8],
            "player3_x": [9, 10, 11, 12],
        }
        base_df = BaseFrame(data)
        base_df.metadata = "metadata"
        base_df.records = [1, 2, 3, 4]
        base_df.data_type = "test"

        assert isinstance(base_df, BaseFrame)
        assert hasattr(base_df, "metadata")
        assert hasattr(base_df, "records")

        assert isinstance(base_df[["player1_x", "player2_x"]], BaseFrame)
        assert hasattr(base_df[["player1_x", "player2_x"]], "metadata")
        assert not hasattr(base_df[["player1_x", "player2_x"]], "records")

    def test_tracking_data_frame(self):

        base_dir = os.path.dirname(__file__)

        tracking_dataset = load_epts_tracking_data(
            metadata_filename=f"{base_dir}/files/metadata.xml",
            raw_data_filename=f"{base_dir}/files/tracking.txt",
        )
        tracking = TrackingFrame(to_pandas(tracking_dataset))
        tracking.data_type = DataType.TRACKING
        tracking.metadata = tracking_dataset.metadata
        tracking.records = tracking_dataset.records

        assert tracking.get_team_by_id("FIFATMA").team_id == "FIFATMA"
        assert tracking.get_period_by_id(1).id == 1
        assert tracking.get_other_team_id("FIFATMA") == "FIFATMB"
        assert tracking.team("FIFATMA").shape[1] == 22
        assert tracking.dimension("x").shape[1] == 23
        assert tracking.players().shape[1] == 44
        assert tracking.players("field").shape[1] == 40
        assert sum(tracking.phase(defending_team_id="FIFATMA")) == 0
        assert sum(tracking.team("FIFATMA").stretched(90)) == 863

    def test_events_data_frame(self):

        base_dir = os.path.dirname(__file__)

        events_dataset = load_metrica_json_event_data(
            metadata_filename=f"{base_dir}/files/metadata.xml",
            raw_data_filename=f"{base_dir}/files/events.json",
        )
        events = EventsFrame(to_pandas(events_dataset))
        events.data_type = DataType.EVENT
        events.metadata = events_dataset.metadata
        events.records = events_dataset.records

        assert events.type("PASS").shape[0] == 26
        assert events.result("COMPLETE").shape[0] == 45
        assert events.into(Zones.OPPONENT_BOX).shape[0] == 1
        assert events.starts_inside(Zones.OPPONENT_BOX).shape[0] == 2
        assert events.ends_inside(Zones.OPPONENT_BOX).shape[0] == 2
        assert events.ends_outside(Zones.OPPONENT_BOX).shape[0] == 43

        # Test diferent ways to input Zones and areas

        custom_area = Area((0.25, 0.2), (0.75, 0.8))

        assert (
            events.ends_outside(Zones.OPPONENT_BOX, Zones.OWN_BOX).shape[0]
            == 45
        )
        assert (
            events.ends_inside(Zones.OPPONENT_BOX, custom_area).shape[0] == 14
        )
        assert events.ends_inside(custom_area, custom_area).shape[0] == 12
