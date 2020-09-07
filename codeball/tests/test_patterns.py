import pickle
import os
from codeball import GameDataset, Pattern
from codeball import TeamStretched, PassesIntoTheBox, SetPieces


class TestPatterns:
    def setup_class(self):
        base_dir = os.path.dirname(__file__)

        self.game_dataset = GameDataset(
            tracking_metadata_file=f"{base_dir}/files/metadata.xml",
            tracking_data_file=f"{base_dir}/files/tracking.txt",
            events_metadata_file=f"{base_dir}/files/metadata.xml",
            events_data_file=f"{base_dir}/files/events.json",
        )

    def test_team_stretched(self):
        parameters = {"team_code": "FIFATMA", "threshold": 40}
        team_stretched = TeamStretched(
            game_dataset=self.game_dataset,
            name="Test Team Stretched",
            code="TEST_001",
            parameters=parameters,
        )
        events = team_stretched.run()

        assert "events" in locals()

    def test_set_pieces(self):
        set_pieces = SetPieces(
            game_dataset=self.game_dataset, name="Set Pieces", code="TEST_002"
        )
        events = set_pieces.run()

        assert "events" in locals()

    def test_passes_into_the_box(self):
        passes_into_the_box = PassesIntoTheBox(
            game_dataset=self.game_dataset,
            name="Passes into the box",
            code="TEST_003",
        )
        events = passes_into_the_box.run()

        assert "events" in locals()
