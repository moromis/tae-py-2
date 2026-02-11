from abc import ABC, abstractmethod


class Writeable(ABC):

    # transform this writeable into dict form and then pass it back to the caller
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    # given a dict, read in attributes to instantiate this writeable
    @abstractmethod
    def from_dict(self, d: dict):
        pass
