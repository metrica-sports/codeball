from dataclasses import dataclass, field
from typing import Optional, List, Dict, TYPE_CHECKING
from kloppy.domain.models import Dataset
from codeball.models.visualizations import Visualization
import pandas as pd

if TYPE_CHECKING:
    from codeball.patterns.base import PatternAnalysis


@dataclass
class Coordinate:
    x: float
    y: float


@dataclass
class PatternEvent:
    pattern: str
    start_time: float
    event_time: float
    end_time: float
    coordinates: List[Coordinate] = field(default_factory=list)
    visualizations: List[Visualization] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)


@dataclass
class Pattern:
    name: str
    code: str
    in_time: int = 0
    out_time: int = 0
    pattern_analysis: List["PatternAnalysis"] = field(default_factory=list)
    events: List[PatternEvent] = field(default_factory=list)


@dataclass
class GameDataset:
    # metadata = [] TODO when metadata is added to Kloppy.
    data: pd.DataFrame
    patterns: List[Pattern] = field(default_factory=list)
