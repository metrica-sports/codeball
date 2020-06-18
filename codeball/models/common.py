from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class Coordinate:
    x: float
    y: float

@dataclass
class Visualization:
    start_time: int
    end_time: int
    players: List[str]
    tool_id: str
    options: Dict

@dataclass
class PatternEvent:
    pattern: str
    start_time: int
    event_time: int
    end_time: int
    coordinates: List[Coordinate]
    visualizations: List[Visualization]
    tags: List[str]

@dataclass
class Pattern:
    name: str
    code: str
    events: List[PatternEvent]
    in_time: int = 0
    out_time: int = 0

