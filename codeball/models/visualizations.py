from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass
class Visualization:
    start_time: int
    end_time: int
    tool_id: str
    players: List[str] = field(default_factory=list)
    options: Dict = field(default_factory=dict)


@dataclass
class PlayerVisualization(Visualization):
    players: List[str] = field(default_factory=list)
