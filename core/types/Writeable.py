from abc import ABC, abstractmethod


class Writeable(ABC):
    name: str
    desc: str
    adjective = ""

    is_character = False

    @abstractmethod
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "desc": self.desc,
            "adjective": self.adjective,
            "is_character": self.is_character,
        }

    @abstractmethod
    def from_dict(self, d: dict):
        self.name = d["name"]
        self.desc = d["desc"]

    @abstractmethod
    def handle_command(
        self, verb: str, object: Writeable | str | None = None
    ) -> str | bool:
        pass
