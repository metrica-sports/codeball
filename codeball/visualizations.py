from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass  # Base Visualization Data Class
class Visualization:
    start_time: int
    end_time: int
    # tool_id: str
    # options: Optional[Dict] = field(default_factory=dict)


# Players
@dataclass
class Players(Visualization):
    players: List[str]
    tool_id: str = "players"
    options: Dict = field(
        default_factory=lambda: {
            "id": True,
            "speed": True,
            "size": 1.0,  # [0.2, 2.5]
            "color": "#000000",
            "boxPositionDown": False,
            "spotlight": False,
            "spotlightSize": 0.5,  # Multiplier [0.2, 4.0]
            "spotlightColor": "#FFFFFF",
            "spotlightOpacity": 0.43,  # [0.0, 1.0]
            "spotlightHeight": 2.0,  # [0.1, 10.0]
            "ringSize": 0.73,
            "ringBorder": False,
            "ringBorderColor": "#FFFFFF",
            "ringFill": False,
            "ringFillColor": "#DC3322",
            "is3d": True,
        }
    )


@dataclass
class Spotlight(Visualization):
    players: List[str]
    tool_id: str = "players"
    options: Dict = field(
        default_factory=lambda: {
            "id": False,
            "speed": False,
            "size": 1.0,  # [0.2, 2.5]
            "color": "#000000",
            "boxPositionDown": False,
            "spotlight": True,
            "spotlightSize": 0.5,  # Multiplier [0.2, 4.0]
            "spotlightColor": "#FFFFFF",
            "spotlightOpacity": 0.43,  # [0.0, 1.0]
            "spotlightHeight": 2.0,  # [0.1, 10.0]
            "ringSize": 0.73,
            "ringBorder": False,
            "ringBorderColor": "#FFFFFF",
            "ringFill": False,
            "ringFillColor": "#DC3322",
            "is3d": True,
        }
    )


@dataclass
class Ring(Visualization):
    players: List[str]
    tool_id: str = "players"
    options: Dict = field(
        default_factory=lambda: {
            "id": False,
            "speed": False,
            "size": 1.0,  # [0.2, 2.5]
            "color": "#000000",
            "boxPositionDown": False,
            "spotlight": False,
            "spotlightSize": 0.5,  # Multiplier [0.2, 4.0]
            "spotlightColor": "#FFFFFF",
            "spotlightOpacity": 0.43,  # [0.0, 1.0]
            "spotlightHeight": 2.0,  # [0.1, 10.0]
            "ringSize": 0.73,
            "ringBorder": True,
            "ringBorderColor": "#FFFFFF",
            "ringFill": True,
            "ringFillColor": "#DC3322",
            "is3d": True,
        }
    )


# Trails
@dataclass
class Trails(Visualization):
    players: List[str]
    tool_id: str = "trails"
    options: Dict = field(
        default_factory=lambda: {
            "color": "#0062ad",
            "continuous": True,
            "dotted": False,
            "dashSize": 1.0,  # Multiplier [0.2, 2.5]. Only Dotted
            "is3d": True,
            "ringBorder": True,
            "offsetOpacity": 0.26,  # [0.0, 1.0]
            "opacity": 1.0,  # [0.0, 1.0]
            "ringBorderColor": "#ffffff",
            "ringFill": True,
            "ringFillColor": "#009cdd",
            "ringSize": 1.0,  # Multiplier [0.6, 4.0]
            "seconds": 5.0,  # [1.0, 99.0]
            "thickness": 0.1,  # Multiplier [0.1, 5.0]. Only in 3D
            "width": 0.24,  # Multiplier [0.1, 2.0]
        }
    )


# FutureTrails
@dataclass
class FutureTrails(Visualization):
    players: List[str]
    tool_id: str = "futureTrails"
    options: Dict = field(
        default_factory=lambda: {
            "color": "#ff9e2d",
            "continuous": True,
            "dotted": False,
            "dashSize": 1.0,  # Multiplier [0.2, 2.5]. Only Dotted
            "is3d": True,
            "ringBorder": True,
            "offsetOpacity": 0.26,  # [0.0, 1.0]
            "opacity": 1.0,  # [0.0, 1.0]
            "ringBorderColor": "#ffffff",
            "ringFill": True,
            "ringFillColor": "#ffdc3a",
            "ringSize": 1.0,  # Multiplier [0.6, 4.0]
            "seconds": 5.0,  # [1.0, 99.0]
            "thickness": 0.1,  # Multiplier [0.1, 5.0]. Only in 3D
            "width": 0.24,  # Multiplier [0.1, 2.0]
        }
    )


# Magnifiers
@dataclass
class Magnifiers(Visualization):
    players: List[str]
    tool_id: str = "magnifiers"
    options: Dict = field(
        default_factory=lambda: {
            "color": "#ffffff",
            "zoom": 1.0,  # Multiplier, [0.2, 1.5]
            "size": 1.0,  # Multiplier, [0.5, 1.5]
        }
    )


# Measurer
@dataclass
class Measurer(Visualization):
    players: List[str]
    tool_id: str = "measurer"
    options: Dict = field(
        default_factory=lambda: {
            "borderColor": "#dc3322",
            "borderEdgeOpacity": 0.4,  # [0.0, 1.0]
            "borderOpacity": 0.9,  # [0.0, 1.0]
            "closed": False,
            "continuous": True,
            "dashSize": 1.45,  # Multiplier [0.2, 2.5]. Only Dotted
            "distance": True,
            "distanceColor": "#ffffff",
            "distanceIs3d": True,
            "distancePosition": 0.92,  # Multiplier [0.5, 2.0]
            "distanceOpacity": 1.0,  # [0.0, 1.0]
            "distanceSize": 1.01,  # Multiplier [0.5, 1.5]
            "dotted": False,
            "fillColor": "#dc3322",  # Only Closed
            "fillOpacity": 0.42,  # [0.0, 1.0]
            "is3d": True,
            "ringBorder": True,
            "ringBorderColor": "#ffffff",
            "ringFill": True,
            "ringFillColor": "#dc3322",
            "ringSize": 0.91,  # Multiplier [0.6, 4.0]
            "thickness": 0.13,  # Multiplier [0.0, 5.0]. Only in 3D
            "width": 0.23,  # Multiplier [0.15, 2.0]
        }
    )


# TeamSize
@dataclass
class TeamSize(Visualization):
    team: str
    line: str = "width"  # Values: 'width' or 'length'
    tool_id: str = "teamSize"
    options: Dict = field(
        default_factory=lambda: {
            "continuous": True,
            "dotted": False,
            "color": "#683391",
            "x": 0.0,
            "y": 0.0,
            "width": 0.23,  # [0.1, 5.0]
            "edgeOpacity": 0.0,  # [0.0, 1.0]
            "opacity": 1.0,  # [0.0, 1.0]
            "thickness": 0.22,  # Multiplier [0.0, 5.0]. Only in 3D
            "dashSize": 0.6,  # Multiplier [0.2, 2.5]. Only Dotted
            "distance": True,
            "distanceColor": "#ffffff",
            "distancePosition": 1.12,  # [0.5, 2.0]
            "distanceOpacity": 1.0,  # Multiplier [0.0, 1.0]
            "distanceSize": 1.3,  # Multiplier [0.5, 1.5]
            "distanceIs3d": True,
            "is3d": True,
        }
    )


# TacticalLines
@dataclass
class TacticalLines(Visualization):
    team: str
    line: str = "defenders"  # Values: 'defenders', 'midfielders' or 'strikers'
    tool_id: str = "tacticalLines"
    options: Dict = field(
        default_factory=lambda: {
            "borderColor": "#ffffff",
            "borderEdgeOpacity": 0.3,  # [0.1, 1.0]
            "borderOpacity": 1.0,  # [0.0, 1.0]
            "fillColor": "#ffffff",
            "fillOpacity": 0.4,  # [0.0, 1.0]
            "closed": False,  # Only used when line is 'midfielders'
            "width": 0.23,  # [0.1, 2.0]
            "thickness": 0.3,  # Multiplier [0.0, 5.0]. Only in 3D
            "dashSize": 1.0,  # Multiplier [0.2, 2.5]. Only Dotted
            "continuous": True,
            "dotted": False,
            "is3d": True,
            "ringBorder": True,
            "ringBorderColor": "#ffffff",
            "ringFill": True,
            "ringFillColor": "#ffffff",
            "ringSize": 0.6,  # [0.6, 4.0]
            "distance": True,
            "distanceColor": "#ffffff",
            "distancePosition": 0.5,  # Multiplier [0.5, 2.0]
            "distanceOpacity": 1.0,  # [0.0, 1.0]
            "distanceSize": 0.73,  # [0.5, 1.5]
            "distanceIs3d": True,
        }
    )


# Pause
@dataclass
class Pause(Visualization):
    pause_time: float = 5000  # Milliseconds
    tool_id: str = "pause"


# ChromaKey
@dataclass
class ChromaKey:
    tool_id: str = "chromaKey"
    options: Dict = field(
        default_factory=lambda: {
            "threshold": 0.01,  # [0.0, 1.0]
            "smoothing": 0.1,  # [0.0, 1.0]
        }
    )


@dataclass
class Arrow(Visualization):
    tool_id: str = "arrow"
    points: Dict = field(
        default_factory=lambda: {
            "start": {"x": 0.0, "y": 0.0},
            "end": {"x": 0.0, "y": 0.0},
        }
    )
    options: Dict = field(
        default_factory=lambda: {
            "arrowheadWidth": 1.5,  # [0.99, 2.0]
            "color": "#ff4f43",
            "continuous": True,
            "curvature": 0.0,  # Multiplier [-1.0, 1.0]. Only in 3D
            "dashSize": 0.4,  # Multiplier [0.2, 2.5]. Only Dotted
            "distance": False,
            "distanceColor": "#ffffff",
            "distancePosition": 0.92,  # Multiplier [0.5, 2.0]
            "distanceOpacity": 1.0,  # [0.0, 1.0]
            "distanceSize": 1.01,  # [0.5, 4.0]
            "distanceIs3d": True,
            "dotted": False,
            "dynamic": False,
            "edgeOpacity": 0.2,  # [0.0, 1.0]
            "opacity": 0.9,  # [0.0, 1.0]
            "height": 0.0,  # [0.0, 0.15]
            "heightCenter": 0.0,  # [-1.0, 1.0]
            "is3d": True,
            "pinned": False,
            "thickness": 0.15,  # Multiplier [0.0, 5.0]. Only in 3D
            "width": 0.5,  # [0.1, 5.0]
        }
    )

    # TODO Add other visualizations not here, specially shape.
