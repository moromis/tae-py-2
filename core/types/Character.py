from shared.types.Response import Response
from shared.types.Room import Room
from shared.types.Writeable import Writeable


class Character(Writeable):
    """A custom type to represent a character"""

    def __init__(
        self,
        name: str,
        desc: str,
        responses: dict[str, Response] | None = None,
    ):
        self.name = name
        self.desc = desc
        self.responses = responses

    def __str__(self) -> str:
        """Provides a string representation for the character."""
        return f"{self.name}\n{self.desc}"

    def to_dict(self):
        return {
            "name": self.name,
            "desc": self.desc,
            "responses": (
                {
                    t: r.to_dict() if isinstance(r, Writeable) else r
                    for t, r in self.responses.items()
                }
                if self.responses
                else None
            ),
        }

    def add_response(self, topic: str, response: str | list[str], condition):
        if not self.responses:
            self.responses = {}
        self.responses[topic] = Response(response, condition)
