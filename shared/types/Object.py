from shared.types.Room import Room
from shared.types.Writeable import Writeable


class Object(Writeable):
    """A custom type to represent an object"""

    def __init__(
        self,
        name: str,
        desc: str,
        room: Room | None = None,
    ):
        self.name = name
        self.desc = desc
        self.room = room

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        room_s = f"in {self.room.name}" if self.room else ""
        return f"({self.name}){room_s}"

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "room": self.room.to_dict() if self.room else None,
        }
