from core.types.Object import Object
from core.types.Writeable import Writeable
from editor.shared.directions import DIRECTIONS


class Room(Writeable):
    """A custom type to represent a room"""

    def __init__(
        self,
        name: str,
        desc: str = "",
        adjacencies: dict[str, str] = {},
        is_entrance=False,
    ):
        self.name = name
        self.desc = desc
        self.adjacencies = adjacencies
        self.characters = []
        self.objects = []
        self.is_entrance = is_entrance

    def add_adjacency(self, room: str, direction: DIRECTIONS) -> None:
        self.adjacencies |= {f"{direction.value}": room}

    def has_adjacency(self, direction: DIRECTIONS) -> bool:
        return direction.value in self.adjacencies

    def get_adjacency(self, direction: DIRECTIONS) -> str | None:
        if self.has_adjacency(direction):
            return self.adjacencies[direction.value]

    def add_object(self, obj: str) -> None:
        self.objects.append(obj)

    def remove_object(self, obj: str) -> None:
        if obj in self.objects:
            self.objects.remove(obj)

    def get_object(self, obj_name: str) -> str | None:
        for obj in self.objects:
            if obj == obj_name:
                return obj
        return None

    def add_character(self, character: str) -> None:
        self.characters.append(character)

    def has_object(self, obj: Object | str | None) -> bool:
        if isinstance(obj, Object):
            return obj.name in self.objects
        return obj in self.objects

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

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)

    def handle_command(self, verb, object=None):
        return self.desc

    def __eq__(self, other) -> bool:
        if not isinstance(other, Room):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.name == other.name
            and self.adjacencies == other.adjacencies
            and self.objects == other.objects
            and self.characters == other.characters
        )
