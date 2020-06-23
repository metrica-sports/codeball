from typing import Optional, List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from codeball.models import PatternEvent, GameDataset, Pattern


class PatternAnalysis(object):
    def __init__(
        self, game_dataset: "GameDataset" = [], pattern: "Pattern" = []
    ):
        self.game_dataset = game_dataset
        self.pattern = pattern

    def run(self) -> List["PatternEvent"]:
        pass
