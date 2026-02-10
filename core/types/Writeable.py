from abc import ABC, abstractmethod


class Writeable(ABC):
    # TODO: separate out writeable and object, and then current object and character inherit
    # from new class, so Response class, which should be a writeable,
    # doesn't inherit all this stuff that doesn't apply to it
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
        self,
        **kwargs
        # verb: str,
        # object: Writeable | str | None = None,
        # rest: list[str] | None = None,
    ) -> str | bool:
        pass
