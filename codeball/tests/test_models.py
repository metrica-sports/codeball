import pandas as pd
from codeball.models import (
    Coordinate,
    PatternEvent,
    Pattern,
    GameDataset,
    DataPackage,
    DataType,
)

import codeball.models.visualizations as vizs


class TestModels:
    def test_coordinate(self):
        xy = Coordinate(x=0.3, y=0.6)
        assert xy.x == 0.3
        assert xy.y == 0.6

    def test_pattern_event(self):

        xy = Coordinate(x=0.3, y=0.6)

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
        assert pattern_event.coordinates[0].x == 0.3
        assert pattern_event.visualizations[0].start_time == 500

    def test_pattern(self):

        pattern = Pattern(name="Test Pattern", code="MET_001", in_time=3)

        assert pattern.in_time == 3
        assert len(pattern.events) == 0

    def test_data_package(self):

        data_package = DataPackage(
            data_type=DataType.TRACKING, data_file="file/name/path",
        )

        assert data_package.data_type == DataType.TRACKING
        assert data_package.metadata_file is None

    def test_game_dataset(self):

        data_package = DataPackage(
            data_type=DataType.TRACKING, data_file="file/name/path",
        )

        game_dataset = GameDataset(tracking=data_package)

        assert len(game_dataset.patterns) == 0
