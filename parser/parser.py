from http.client import GONE
from logging import log
from core import logger
from core.managers.object_manager import get_object_by_name
from core.types.Object import Object
from parser.verbs import verbs
from parser.history import History
from parser.types.Verb import Verb
from strings import DEFAULT_VERB_RESPONSE, GONE_WRONG


class Parser:
    def __init__(self) -> None:
        self.history = History()

    def add_to_history(self, command: str) -> None:
        self.history.push_history(command)

    def split_to_words(self, command: str) -> list[str]:
        return command.split(" ")

    def parse(self, command: str) -> str:
        split = self.split_to_words(command)
        verb_name, verb_obj, rest = self.get_verb(split)
        object, rest = self.get_object(rest)
        indirect_object = self.get_indirect_object(rest)
        try:
            if indirect_object:
                handled = indirect_object.handle_command(verb_name, object)
                if not handled and object:
                    handled = object.handle_command(verb_name)
                    if not handled:
                        return verb_obj.handle_command(
                            object.name, indirect_object.name
                        )
                    else:
                        return str(handled)
                else:
                    return str(handled)
            elif object:
                handled = object.handle_command(verb_name)
                if not handled:
                    return verb_obj.handle_command(object.name)
                else:
                    return str(handled)
            else:
                return verb_obj.handle_command()
        except Exception as e:
            logger.log(str(e))
            log(3, e)
        return GONE_WRONG

    def get_verb(self, command: list[str]) -> tuple[str, Verb, list[str]]:
        for i, s in enumerate(command):
            verb_name, verb = verbs.find_verb(s)
            if verb:
                return verb_name, verb, command[i + 1 :]
        return DEFAULT_VERB_RESPONSE, verbs.NO_RESPONSE_VERB, []

    def get_object(self, command: list[str]) -> tuple[Object | None, list[str]]:
        for i, s in enumerate(command):
            found = get_object_by_name(s)
            if found:
                return found, command[i + 1 :]

        return None, []

    def get_indirect_object(self, command: list[str]) -> Object | None:
        for i, s in enumerate(command):
            found = get_object_by_name(s)
            if found:
                return found

        return None


# NOTES:
# some commands don't have any sort of object, such as "inventory", but every command has an action/verb
# if we have an indirect object, we must also have an object
