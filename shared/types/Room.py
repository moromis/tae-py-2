from shared.types.Writeable import Writeable


class Room(Writeable):
    """A custom type to represent a room"""

    def __init__(self, name: str, desc: str, adjacencies={}):
        self.name = name
        self.desc = desc
        self.adjacencies = adjacencies
        self.characters = []
        self.objects = []

    def add_adjacency(self, room: str, direction: str) -> None:
        self.adjacencies |= {f"{direction}": room}

    def add_object(self, object: str) -> None:
        self.objects.append(object)

    def add_character(self, character: str) -> None:
        self.characters.append(character)

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return self.desc

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "adjacencies": self.adjacencies,
            "objects": self.objects,
            "characters": self.characters,
        }
