from core.types.Writeable import Writeable


class Response(Writeable):
    def __init__(self, response: str | list[str], condition=None) -> None:
        self.response = response
        self.condition = condition

    def __str__(self) -> str:
        return ""

    def to_dict(self):
        return {"response": self.response, "condition": self.condition}

    def from_dict(self, d):
        self.response = d["response"]
        self.condition = d["condition"]

    def handle_command(
        self, verb: str, object: Writeable | str | None = None
    ) -> str | bool:
        return False
