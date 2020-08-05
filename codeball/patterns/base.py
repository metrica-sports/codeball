from typing import Optional, List, Dict
from abc import ABC, abstractmethod
from codeball.models import PatternEvent, GameDataset, Pattern


class PatternAnalysis(ABC):
    def __init__(
        self,
        game_dataset: GameDataset = None,
        pattern: Pattern = None,
        parameters: dict = None,
    ):
        self.game_dataset = game_dataset
        self.pattern = pattern
        self.parameters = parameters

    @abstractmethod
    def run(self) -> List[PatternEvent]:
        """ Runs the pattern to compute the PatternEvents"""
        raise NotImplementedError
