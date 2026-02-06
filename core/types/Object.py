from typing import Callable
from core.types.Writeable import Writeable


class Object(Writeable):
    """A custom type to represent an object"""

    def __init__(
        self,
        name: str,
        desc: str = "",
        adjective: str = "",
        handlers: dict[str, Callable] = {},
    ):
        self.name = name
        self.desc = desc
        self.adjective = adjective
        self.handlers = handlers

    def handle_command(self, verb, object=None):
        if verb in self.handlers:
            return self.handlers[verb](object)
        return False

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return f"There is a {self.desc} here."

    def to_dict(self) -> dict:
        return super().to_dict()

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)
