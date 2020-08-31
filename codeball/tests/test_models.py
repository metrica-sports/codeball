import os

import pandas as pd

from codeball.models import (
    PatternEvent,
    Pattern,
    GameDataset,
    DataType,
    PatternsSet,
)

import codeball.models.visualizations as vizs


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
                game_dataset: GameDataset,
                name: str,
                code: str,
                in_time: int = 0,
                out_time: int = 0,
                parameters: dict = None,
            ):
                super().__init__(name, code, in_time, out_time, parameters)
                self.game_dataset = game_dataset

            def run(self):
                return True

        test_pattern = pattern_class(
            game_dataset=None,
            name="Test Pattern",
            code="MET_001",
            in_time=3,
            out_time=2,
            parameters=None,
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
                game_dataset: GameDataset,
                name: str,
                code: str,
                in_time: int = 0,
                out_time: int = 0,
                parameters: dict = None,
            ):
                super().__init__(name, code, in_time, out_time, parameters)
                self.game_dataset = game_dataset

            def run(self):
                return True

        test_pattern = pattern_class(
            game_dataset=game_dataset,
            name="Test Pattern",
            code="MET_001",
            in_time=3,
            out_time=2,
            parameters=None,
        )

        patterns_set = PatternsSet(game_dataset=game_dataset)
        patterns_set.patterns = [test_pattern, test_pattern]

        assert patterns_set.game_dataset.events.data_type == DataType.EVENT
        assert len(patterns_set.patterns) == 2
