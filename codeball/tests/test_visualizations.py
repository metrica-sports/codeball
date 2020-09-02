import codeball.visualizations as vizs
import pytest


class TestVisualizations:
    def test_players(self):

        with pytest.raises(TypeError):
            vizs.Players(50, 100)

        viz = vizs.Players(
            start_time=500, end_time=700, players=["P001", "P002"]
        )

        assert viz.start_time == 500
        assert len(viz.players) == 2
        assert viz.options["id"] is True

    def test_trails(self):
        with pytest.raises(TypeError):
            vizs.Trails(50, 100)

        viz = vizs.Trails(
            start_time=500, end_time=1000, players=["P001", "P002"]
        )

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert len(viz.players) == 2
        assert viz.options["width"] == 1

    def test_future_trails(self):
        with pytest.raises(TypeError):
            vizs.FutureTrails(50, 100)

        viz = vizs.FutureTrails(
            start_time=500, end_time=1000, players=["P001", "P002"]
        )

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert len(viz.players) == 2
        assert viz.options["width"] == 1

    def test_magnifiers(self):
        with pytest.raises(TypeError):
            vizs.Magnifiers(50, 100)

        viz = vizs.Magnifiers(
            start_time=500, end_time=1000, players=["P001", "P002"]
        )

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert len(viz.players) == 2
        assert viz.options["size"] == 1

    def test_measurer(self):
        with pytest.raises(TypeError):
            vizs.Measurer(50, 100)

        viz = vizs.Measurer(
            start_time=500, end_time=1000, players=["P001", "P002"]
        )

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert len(viz.players) == 2
        assert viz.options["closed"] is False

    def test_team_size(self):
        with pytest.raises(TypeError):
            vizs.TeamSize(50, 100)

        viz = vizs.TeamSize(start_time=500, end_time=1000, team="T001")

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert viz.options["color"] == "#E66F7E"

    def test_tactical_lines(self):
        with pytest.raises(TypeError):
            vizs.TacticalLines(50, 100)

        viz = vizs.TacticalLines(start_time=500, end_time=1000, team="T001")

        assert viz.start_time == 500
        assert viz.end_time == 1000
        assert viz.options["color"] == "#E66F7E"

    def test_pause(self):

        viz = vizs.Pause(start_time=500, end_time=500)

        assert viz.pause_time == 5000

    def test_chroma_key(self):

        viz = vizs.ChromaKey()

        assert viz.options["smoothing"] == 0.1

    def test_arrow(self):
        viz = vizs.Arrow(
            start_time=500,
            end_time=1000,
            points={
                "start": {"x": 0.5, "y": 0.5},
                "end": {"x": 0.8, "y": 0.9},
            },
            options={"pinned": True, "width": 0.3},
        )

        assert viz.options["pinned"] is True
