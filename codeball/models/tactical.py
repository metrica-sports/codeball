from dataclasses import dataclass
from enum import Enum
from kloppy.domain.models import Team


class Zone(Enum):
    OPPONENT_BOX = "opponent-box"

    @property
    def vertices(self):
        if self == Zone.OPPONENT_BOX:
            return Vertices(top_left=[0.84, 0.2], bottom_right=[1, 0.8],)


@dataclass
class Vertices:
    top_left: list
    bottom_right: list


@dataclass
class Possession:
    start: float
    end: float
    team: Team
