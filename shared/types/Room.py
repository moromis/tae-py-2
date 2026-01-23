from shared.types.Writeable import Writeable


class Room(Writeable):
    """A custom type to represent a room"""

    def __init__(self, name: str, desc: str, x: float, y: float):
        self.name = name
        self.desc = desc
        self.x = x
        self.y = y
        self.adjacencies = {}

    def add_adjacency(self, room: str, direction: str) -> None:
        self.adjacencies |= {f"{direction}": room}

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return f"({self.name}, {self.x}, {self.y})"

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "x": self.x,
            "y": self.y,
        }
