from dataclasses import dataclass, field
from typing import Optional, List, Dict, TYPE_CHECKING
from kloppy.domain.models import Dataset
from codeball.patterns import PatternAnalysis

@dataclass
class Coordinate:
    x: float
    y: float

@dataclass
class Visualization:
    start_time: int
    end_time: int
    tool_id: str
    players: List[str] = field(default_factory=list)
    options: Dict = field(default_factory=dict)

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
    in_time: int = 0 
    out_time: int = 0
    events: List[PatternEvent] = field(default_factory=list) 
    pattern_analysis: List[PatternAnalysis] = field(default_factory=list)

@dataclass
class GameDataset:
    # metadata = [] TODO when metadata is added to Kloppy. 
    dataset: Dataset = field(default_factory=list)
    patterns: List[Pattern] = field(default_factory=list)

