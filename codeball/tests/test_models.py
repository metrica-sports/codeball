import pandas as pd
from codeball.models import (
    Coordinate,
    Visualization,
    PatternEvent,
    Pattern,
    GameDataset,
)


class TestModels:
    def test_coordinate(self):
        xy = Coordinate(x=0.3, y=0.6)
        assert xy.x == 0.3
        assert xy.y == 0.6

    def test_visualization(self):
        viz = Visualization(start_time=500, end_time=700, tool_id="player",)

        assert viz.start_time == 500

    def test_pattern_event(self):

        xy = Coordinate(x=0.3, y=0.6)

        viz = Visualization(
            start_time=500, end_time=700, players=[], tool_id="player", options=[]
        )

        pattern_event = PatternEvent(
            pattern="MET_001",
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

    def test_game_dataset(self):

        dataframe = pd.DataFrame()
        game_dataset = GameDataset(dataframe)

        assert len(game_dataset.patterns) == 0
