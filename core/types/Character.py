import prompt_toolkit
from core.types.Object import Object
from core.types.ObjectProperties import OBJECT_PROPERTIES
from core.types.Response import Response
from parser.types.Verb import Verb
from strings import THEY_DONT_WANT_TO_TALK
from prompt_toolkit.formatted_text import FormattedText


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

    def handle_command(self, **kwargs) -> str | FormattedText | bool:
        verb: str | Verb | None = kwargs.get("verb", None)
        # object: Writeable | str | None = kwargs.get("object", None)
        # indirect_object: Writeable | str | None = kwargs.get("indirect_object", None)
        rest: list[str] | None = kwargs.get("rest", None)
        if verb == "talk":
            topic = " ".join(rest) if rest else None
            if topic in self.responses:
                response = self.responses[topic].response
                if isinstance(response, str):
                    return FormattedText([("bold", f"\n{self.name}: "), ("", response)])
            else:
                if len(self.responses):
                    topic = prompt_toolkit.choice(
                        f"What do you want to talk to the{f' {self.adjective}' if self.adjective else ''} {self.name} about?",
                        options=[(topic, topic) for topic in self.responses.keys()],
                    )
                    return self.handle_command(**{**kwargs, "rest": [topic]})
                else:
                    return THEY_DONT_WANT_TO_TALK
        return False

    def __str__(self) -> str:
        return super().__str__()

    # TODO: use this to print the character instead of directly accessing attributes
    def __desc__(self):
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
            OBJECT_PROPERTIES.IS_CHARACTER: True,
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
