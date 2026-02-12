from typing import Callable
from core.types.ObjectProperties import OBJECT_PROPERTIES
from core.types.Writeable import Writeable
from parser.types.Verb import Verb


class Object(Writeable):
    """A custom type to represent an object"""

    def __init__(
        self,
        name: str,
        desc: str = "",
        adjective: str = "",
        handlers: dict[str, Callable] = {},
        properties: dict[OBJECT_PROPERTIES, bool] = {},
    ):
        self.name = name
        self.desc = desc
        self.adjective = adjective
        self.handlers = handlers
        self.properties = properties

    def handle_command(self, **kwargs):
        verb: str | Verb | None = kwargs.get("verb", None)
        object: Writeable | str | None = kwargs.get("object", None)
        indirect_object: Writeable | str | None = kwargs.get("indirect_object", None)
        rest: list[str] | None = kwargs.get("rest", None)
        if verb in self.handlers:
            return self.handlers[verb](
                object=object, indirect_object=indirect_object, rest=rest
            )
        return False

    def get_property(self, prop: OBJECT_PROPERTIES) -> bool | None:
        return self.properties.get(prop)

    def set_property(self, prop: OBJECT_PROPERTIES, to_set: bool) -> None:
        self.properties[prop] = to_set

    def __str__(self) -> str:
        return f"{f"{self.adjective} " if self.adjective else ""}{self.name}"

    def __desc__(self) -> str:
        """Provides a description for the object."""
        return self.desc

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "desc": self.desc,
            "adjective": self.adjective,
            "properties": self.properties,
            # TODO: figure out how to serialize handlers
        }

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)
