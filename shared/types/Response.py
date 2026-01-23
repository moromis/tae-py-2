from shared.types.Writeable import Writeable


class Response(Writeable):
    def __init__(self, response: str, condition) -> None:
        self.response = response
        self.condition = condition

    def __str__(self) -> str:
        return ""

    def to_dict(self):
        return {"response": self.response, "condition": self.condition}
