from core.types.Object import Object
from core.types.Response import Response
from parser.types.Verb import Verb


class Character(Object):
    """A custom type to represent a character"""

    def __init__(
        self,
        name: str,
        desc: str = "",
        adjective: str = "",
        responses: dict[str, Response] = {},
    ):
        super().__init__(name, desc, adjective)
        self.responses = responses

    def handle_command(self, **kwargs) -> str | bool:
        verb: str | Verb | None = kwargs.get("verb", None)
        # object: Writeable | str | None = kwargs.get("object", None)
        # indirect_object: Writeable | str | None = kwargs.get("indirect_object", None)
        rest: list[str] | None = kwargs.get("rest", None)
        if verb == "talk":
            topic = " ".join(rest) if rest else None
            if topic in self.responses:
                response = self.responses[topic].response
                if isinstance(response, str):
                    return response
            else:
                return f"What do you want to talk to {self.name} about?"
        return False

    # TODO: use this to print the character instead of directly accessing attributes
    def __str__(self) -> str:
        """Provides a string representation for the character."""
        return f"{self.name}\n{self.desc}"

    def to_dict(self):
        base = super().to_dict()
        return {
            **base,
            "responses": (
                {t: r.to_dict() for t, r in self.responses.items()}
                if self.responses
                else None
            ),
            "is_character": True,
        }

    def from_dict(self, d: dict):
        for k, v in d.items():
            if k == "responses" and d["responses"] and len(d["responses"]):
                for topic, response in d["responses"].items():
                    self.responses[topic] = Response(**response)
            else:
                setattr(self, k, v)

    def add_response(
        self, topic: str, response: Response | str | list[str], condition=None
    ):
        if not self.responses:
            self.responses = {}
        if isinstance(response, Response):
            self.responses[topic] = response
        else:
            self.responses[topic] = Response(response, condition)
