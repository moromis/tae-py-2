# DIRECTIONS = [
#     ("n", "North"),
#     ("ne", "Northeast"),
#     ("e", "East"),
#     ("se", "Southeast"),
#     ("s", "South"),
#     ("sw", "Southwest"),
#     ("w", "West"),
#     ("nw", "Northwest"),
# ]

from enum import StrEnum, auto


class DIRECTIONS(StrEnum):
    NORTH = auto()
    NORTHEAST = auto()
    EAST = auto()
    SOUTHEAST = auto()
    SOUTH = auto()
    SOUTHWEST = auto()
    WEST = auto()
    NORTHWEST = auto()


def reverse_direction(dir: str):
    match dir:
        case DIRECTIONS.NORTH:
            return DIRECTIONS.SOUTH
        case DIRECTIONS.NORTHEAST:
            return DIRECTIONS.SOUTHWEST
        case DIRECTIONS.EAST:
            return DIRECTIONS.WEST
        case DIRECTIONS.SOUTHEAST:
            return DIRECTIONS.NORTHWEST
        case DIRECTIONS.SOUTH:
            return DIRECTIONS.NORTH
        case DIRECTIONS.SOUTHWEST:
            return DIRECTIONS.NORTHEAST
        case DIRECTIONS.WEST:
            return DIRECTIONS.EAST
        case DIRECTIONS.NORTHWEST:
            return DIRECTIONS.SOUTHEAST
