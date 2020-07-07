from dataclasses import dataclass, field
from typing import Optional, List, Dict, TYPE_CHECKING
from enum import Enum
from kloppy.domain.models import Dataset
from kloppy import load_epts_tracking_data, to_pandas
from codeball.models.visualizations import Visualization
import codeball


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
    events: List[PatternEvent] = field(default_factory=list)


class DataType(Enum):
    TRACKING = "tracking"
    EVENT = "event"


@dataclass
class DataPackage:
    data_type: DataType
    data_file: str
    meta_data_file: str = None

    def load_dataset(self):
        self.dataset = load_epts_tracking_data(
            self.meta_data_file, self.data_file
        )

    def build_dataframe(self):
        self.dataframe = to_pandas(self.dataset)


@dataclass
class GameDataset:
    tracking_data: DataPackage = None
    event_data: DataPackage = None

    def load_patterns_config(self):
        self.patterns_config = codeball.get_patterns_config()

    def initialize_patterns(self):

        self.load_patterns_config()

        self.patterns = []
        for pattern_config in self.patterns_config:
            if pattern_config["include"]:
                pattern = self._initialize_pattern(pattern_config)
                self.patterns.append(pattern)

    def _initialize_pattern(self, pattern_config: Dict):
        pattern = Pattern(
            name=pattern_config["name"], code=pattern_config["code"]
        )

        pattern.pattern_analysis = []
        for pattern_analysis_config in pattern_config["pattern_analysis"]:
            pattern_analysis = self._initialize_pattern_analysis(
                pattern, pattern_analysis_config
            )
            pattern.pattern_analysis.append(pattern_analysis)

        return pattern

    def _initialize_pattern_analysis(
        self, pattern: Pattern, pattern_analysis_config: dict
    ):

        pattern_analysis_class = pattern_analysis_config["class"]
        return pattern_analysis_class(
            self, pattern, pattern_analysis_config["parameters"]
        )

    def run_patterns(self):
        for pattern in self.patterns:
            for analysis in pattern.pattern_analysis:
                pattern.events = pattern.events + analysis.run()
