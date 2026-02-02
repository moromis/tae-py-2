from typing import Callable
from core.types.Writeable import Writeable


class Object(Writeable):
    """A custom type to represent an object"""

    def __init__(
        self,
        name: str,
        desc: str = "",
        adjective: str | None = None,
        handlers: dict[str, Callable] = {},
    ):
        self.name = name
        self.desc = desc
        self.adjective = adjective
        self.handlers = handlers

    def handle_command(
        self, verb: str | None, object: Object | None = None
    ) -> str | bool:
        if verb in self.handlers:
            return self.handlers[verb](object)
        return False

    def __str__(self) -> str:
        """Provides a string representation for the object."""
        return f"There is a {self.desc} here."

    def to_dict(self):
        # TODO: write handlers... to python? game file could be zip folder w/ renamed extension
        return {"name": self.name, "desc": self.desc, "adjective": self.adjective}

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)

    def __getitem__(self, item):
        return self[item]
