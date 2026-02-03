from typing import Any
from core.types.Writeable import Writeable


class Room(Writeable):
    """A custom type to represent a room"""

    def __init__(self, name: str, desc: str = "", adjacencies={}, is_entrance=False):
        self.name = name
        self.desc = desc
        self.adjacencies = adjacencies
        self.characters = []
        self.objects = []
        self.is_entrance = is_entrance

    def add_adjacency(self, room: str, direction: str) -> None:
        self.adjacencies |= {f"{direction}": room}

    def add_object(self, obj: str) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: str) -> None:
        if obj in self.objects:
            self.objects.remove(obj)

    def add_character(self, character: str) -> None:
        self.characters.append(character)

    def has_object(self, obj_name: str) -> bool:
        return obj_name in self.objects

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return self.desc

    # TODO: see if this can be automated... same with other types of course
    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "adjacencies": self.adjacencies,
            "objects": self.objects,
            "characters": self.characters,
        }

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)
