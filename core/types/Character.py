from core.types.Response import Response
from core.types.Writeable import Writeable


class Character(Writeable):
    """A custom type to represent a character"""

    is_character = True

    def __init__(self, name: str, desc: str = "", responses: dict[str, Response] = {}):
        self.name = name
        self.desc = desc
        self.responses = responses

    def handle_command(
        self, verb: str | None, object: Writeable | str | None = None
    ) -> str | bool:
        if verb == "talk":
            if object and isinstance(object, str) and object in self.responses:
                response = self.responses[object].response
                if isinstance(response, str):
                    return response
        return False

    def __str__(self) -> str:
        """Provides a string representation for the character."""
        return f"{self.name}\n{self.desc}"

    def to_dict(self):
        base = super().to_dict()
        return {
            **base,
            "responses": (
                {
                    t: r.to_dict() if isinstance(r, Writeable) else r
                    for t, r in self.responses.items()
                }
                if self.responses
                else None
            ),
            "is_character": self.is_character,
        }

    def from_dict(self, d: dict):
        for k, v in d.items():
            setattr(self, k, v)

    def add_response(self, topic: str, response: str | list[str], condition):
        if not self.responses:
            self.responses = {}
        self.responses[topic] = Response(response, condition)
