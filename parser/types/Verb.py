from typing import Callable

from core.types.Writeable import Writeable
from strings import DEFAULT_VERB_RESPONSE


class Verb:
    def __init__(
        self,
        default_response: Callable | str = DEFAULT_VERB_RESPONSE,
        synonyms: list[str] = [],
        handlers: dict[str, Callable] = {},
    ) -> None:
        self.default_response = default_response
        self.synonyms = synonyms
        self.handlers = handlers

    def get_default_response(self):
        return self.default_response

    def get_synonyms(self):
        return self.synonyms

    def search_in_synonyms(self, search: str) -> bool:
        return search in self.synonyms

    # if we the verb are handling the command, then the indirect and direct objects have already had
    # their chance, so go ahead and do your thing
    def handle_command(self, **kwargs) -> str:
        object: str | Writeable | None = kwargs.get("object", None)
        indirect_object: str | Writeable | None = kwargs.get("indirect_object", None)
        rest: list[str] | None = kwargs.get("rest", None)

        if callable(self.default_response):
            if object and indirect_object:
                return self.default_response(object, indirect_object)
            elif object:
                return self.default_response(object)
            else:
                return self.default_response()
        else:
            return self.default_response
