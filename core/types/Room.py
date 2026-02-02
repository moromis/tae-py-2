from typing import Any
from core.types.Writeable import Writeable


class Room(Writeable):
    """A custom type to represent a room"""

    def __init__(self, name: str, desc: str, adjacencies={}, is_entrance=False):
        self.name = name
        self.desc = desc
        self.adjacencies = adjacencies
        self.characters = []
        self.objects = []
        self.is_entrance = is_entrance

    def add_adjacency(self, room: str, direction: str) -> None:
        self.adjacencies |= {f"{direction}": room}

    def add_object(self, object: str) -> None:
        self.objects.append(object)

    def add_character(self, character: str) -> None:
        self.characters.append(character)

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return self.desc

    def __getitem__(self, item):
        return self[item]

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "adjacencies": self.adjacencies,
            "objects": self.objects,
            "characters": self.characters,
        }
