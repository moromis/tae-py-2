from logging import log
from core import logger
from core.managers.object_manager import Object_Manager
from core.types.Object import Object
from parser.verbs import verbs
from parser.types.Verb import Verb
from strings import DEFAULT_VERB_RESPONSE, GONE_WRONG
from prompt_toolkit.formatted_text import FormattedText

STRIP_LIST = ["to", "a", "an", "the", "about", "with"]


class Parser:
    def split_to_words(self, command: str) -> list[str]:
        return command.split(" ")

    def strip(self, command: list[str]) -> list[str]:
        for word in STRIP_LIST:
            command = [s for s in command if s != word]
        return command

    def parse(self, command: str) -> str | FormattedText:
        split = self.split_to_words(command)
        lower = [s.lower() for s in split]
        stripped = self.strip(lower)
        get_verb_res = self.get_verb(stripped)

        verb_name = DEFAULT_VERB_RESPONSE
        rest = []
        verb_obj = verbs.NO_RESPONSE_VERB

        if get_verb_res:
            verb_name, verb_obj, rest = get_verb_res
        object, rest = self.get_object(rest)
        indirect_object = self.get_indirect_object(rest)
        try:
            if indirect_object:
                handled = indirect_object.handle_command(
                    verb=verb_name, object=object, rest=rest
                )
                if not handled and object:
                    handled = object.handle_command(verb=verb_name, rest=rest)
                    if not handled:
                        return verb_obj.handle_command(
                            object=object, indirect_object=indirect_object, rest=rest
                        )
                    else:
                        return str(handled)
                else:
                    return str(handled)
            elif object:
                handled = object.handle_command(verb=verb_name, rest=rest)
                if not handled:
                    return verb_obj.handle_command(object=object, rest=rest)
                else:
                    if isinstance(handled, str) or isinstance(handled, FormattedText):
                        return handled
                    return str(handled)
            else:
                return verb_obj.handle_command(verb=verb_name, rest=rest)
        except Exception as e:
            logger.log(str(e))
            log(3, e)
        return GONE_WRONG

    def get_verb(self, command: list[str]) -> tuple[str, Verb, list[str]] | None:
        for i, s in enumerate(command):
            res = verbs.find_verb(s)
            if res:
                verb_name, verb = res
                return verb_name, verb, command[i + 1 :]
        return None

    def get_object(self, command: list[str]) -> tuple[Object | None, list[str]]:
        for i, s in enumerate(command):
            found = Object_Manager.get_by_name(s)
            if found:
                return found, command[i + 1 :]

        return None, command

    def get_indirect_object(self, command: list[str]) -> Object | None:
        for i, s in enumerate(command):
            found = Object_Manager.get_by_name(s)
            if found:
                return found

        return None


# NOTES:
# some commands don't have any sort of object, such as "inventory", but every command has an action/verb
# if we have an indirect object, we must also have an object
