from core.types.Room import Room
from core.types.Writeable import Writeable


class Object(Writeable):
    """A custom type to represent an object"""

    def __init__(
        self,
        name: str,
        desc: str,
    ):
        self.name = name
        self.desc = desc

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return self.desc

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
        }
