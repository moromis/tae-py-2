from shared.types.Response import Response
from shared.types.Room import Room
from shared.types.Writeable import Writeable


class Character(Writeable):
    """A custom type to represent a character"""

    def __init__(
        self,
        name: str,
        desc: str,
        room: Room | None = None,
        responses: dict[str, Response] | None = None,
    ):
        self.name = name
        self.desc = desc
        self.room = room
        self.responses = responses

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        room_s = f"in {self.room.name}" if self.room else ""
        return f"({self.name}){room_s}"

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "room": self.room.to_dict() if self.room else None,
            "responses": (
                {t: r.to_dict() for t, r in self.responses.items()}
                if self.responses
                else None
            ),
        }
