# verbs, their synonyms, and their verb default behaviors

from core.confirm import confirm
from parser.types.Verb import Verb
from parser.verbs.look import look
from parser.verbs.take import take
from strings import DEFAULT_VERB_RESPONSE

NO_RESPONSE_VERB = Verb(DEFAULT_VERB_RESPONSE)

NO_OBJECT_VERBS = {
    "inventory": Verb("You look at your inventory."),
    "save": Verb("save"),
    "exit": Verb(lambda: confirm(lambda: exit(0))),
}

VERBS = {
    "look": Verb(
        look,
        synonyms=["look at, inspect, examine"],
    ),
    "hit": Verb(
        lambda obj: f"You hit the {obj.name if "name" in obj else obj} but it doesn't do anything.",
        synonyms=["whack", "thwack", "smack", "bop"],
    ),
    "drop": Verb("Dropped."),
    "take": Verb(take, ["pick up", "grab"]),
    **NO_OBJECT_VERBS,
}


# search all verbs and their synonyms
# future: may want to have groups of verbs, or order verbs based on frequency
def find_verb(s: str) -> tuple[str, Verb | None]:
    s = s.lower()
    for k, v in VERBS.items():
        if s == k.lower():
            return k, v
        elif v.search_in_synonyms(s):
            return k, v
    return DEFAULT_VERB_RESPONSE, NO_RESPONSE_VERB
