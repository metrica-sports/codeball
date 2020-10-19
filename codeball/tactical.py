from dataclasses import dataclass
from enum import Enum
from kloppy.domain.models import Team


class AreaType(Enum):
    RECTANGLE = "rectangle"
    POLYGON = "polygon"


class Area:
    def __init__(self, *points):
        self.__validate_points(points)
        self.points = points

    @staticmethod
    def __validate_points(points):

        for point in points:
            if isinstance(point, (tuple, list)) and len(point) != 2:
                raise TypeError(
                    "A point should be a tuple or a list of length 2"
                )

        if len(points) < 2:
            raise TypeError(
                "At least 2 points should be given to define an Area."
            )

    @property
    def type(self):
        if len(self.points) == 2:
            return AreaType.RECTANGLE
        else:
            return AreaType.POLYGON


class Zones(Enum):
    OPPONENT_BOX = Area((0.84, 0.2), (1, 0.8))
    OWN_BOX = Area((0, 0.2), (0.16, 0.8))

    ATTACKING_THIRD = Area((2 / 3, 0), (1, 1))
    MIDDLE_THIRD = Area((1 / 3, 0), (2 / 3, 1))
    DEFENDING_THIRD = Area((0, 0), (1 / 3, 1))

    OWN_HALF = Area((0, 0), (0.5, 1))
    OPPONENT_HALF = Area((0.5, 0), (1, 1))

    LEFT_HALF_SPACE = Area((0, 0.2), (1, 0.4))
    RIGHT_HALF_SPACE = Area((0, 0.6), (1, 0.8))
    HALF_SPACES = (Area((0, 0.2), (1, 0.4)), Area((0, 0.6), (1, 0.8)))

    CENTRE = Area((0, 0.4), (1, 0.6))

    LEFT_WING = Area((0, 0), (1, 0.2))
    RIGHT_WING = Area((0, 0.8), (1, 1))
    WINGS = (Area((0, 0), (1, 0.2)), Area((0, 0.8), (1, 1)))

    ZONE_14 = Area((2 / 3, 1 / 3), (5 / 6, 2 / 3))

    @property
    def areas(self):
        return self.value


@dataclass
class Possession:
    start: float
    end: float
    team: Team
