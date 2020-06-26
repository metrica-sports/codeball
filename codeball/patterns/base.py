from typing import Optional, List, Dict
from codeball.models import PatternEvent, GameDataset, Pattern


class PatternAnalysis(object):
    def __init__(self, game_dataset: GameDataset = [], pattern: Pattern = []):
        self.game_dataset = game_dataset
        self.pattern = pattern

    def run(self) -> List[PatternEvent]:
        """ Runs the pattern to compute the PatternEvents"""
        pass
