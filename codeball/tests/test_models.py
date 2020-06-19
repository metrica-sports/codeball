from codeball.models import(
    Coordinate,
    Visualization,
    PatternEvent
)

class TestModels:
    def test_coordinate(self):
        xy = Coordinate(x=0.3, y=0.6)
        assert xy.x == 0.3
        assert xy.y ==0.6

    def test_visualization(self):
        viz = Visualization(
            start_time = 500,
            end_time = 700,
            players = [],
            tool_id = 'player',
            options = []
        )

        assert viz.start_time == 500

    def test_pattern_event(self):

        xy = Coordinate(x=0.3, y=0.6)

        viz = Visualization(
            start_time = 500,
            end_time = 700,
            players = [],
            tool_id = 'player',
            options = []
        )

        pattern_event = PatternEvent(
            pattern = 'MET_001',
            start_time = 400,
            event_time = 500,
            end_time = 800,
            coordinates = [xy, xy],
            visualizations = [viz, viz],
            tags = ['T001']
        )

        assert pattern_event.end_time == 800
        assert pattern_event.coordinates[0].x == 0.3
        assert pattern_event.visualizations[0].start_time == 500