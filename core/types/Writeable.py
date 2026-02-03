from abc import ABC, abstractmethod


class Writeable:
    name: str
    desc: str

    def to_dict(self) -> dict:
        return {}

    def from_dict(self, d: dict):
        self.name = d["name"]
        self.desc = d["desc"]
