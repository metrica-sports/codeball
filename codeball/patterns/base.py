from typing import Optional, List, Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from codeball.models import PatternEvent, GameDataset, Pattern

class PatternAnalysis(object): 
    def __init__(self, 
    game_dataset: "GameDataset"  = [], 
    pattern: "Pattern" = [], 
    options: dict = []
    ):
        self.game_dataset = game_dataset
        self.pattern = pattern
        self.options = options

    def run(self) -> List["PatternEvent"]:
        pass