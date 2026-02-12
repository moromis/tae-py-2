# verbs, their synonyms, and their verb default behaviors

import os
from signal import Signals
from core.helpers.confirm import confirm
from editor.shared.directions import DIRECTIONS
from parser.inventory import get_inventory_string
from parser.types.Verb import Verb
from parser.verbs.drop import drop
from parser.verbs.hit import hit
from parser.verbs.look import look
from parser.verbs.move import move
from parser.verbs.take import take
from parser.verbs.open import open
from strings import DEFAULT_VERB_RESPONSE, TALK_TO_WHOM

NO_RESPONSE_VERB = Verb(DEFAULT_VERB_RESPONSE)

MOVE = Verb(move, synonyms=["go", "walk"])

NO_OBJECT_VERBS = {
    "inventory": Verb(get_inventory_string),
    "save": Verb("save"),
    "exit": Verb(
        lambda **kwargs: confirm(lambda: os.kill(os.getpid(), Signals.SIGINT))
    ),
    "talk": Verb(TALK_TO_WHOM, synonyms=["ask", "inquire", "query"]),
    "move": MOVE,
    **{d.value: MOVE for d in DIRECTIONS},
}

VERBS = {
    "look": Verb(
        look,
        synonyms=["look at, inspect, examine"],
    ),
    "hit": Verb(
        hit,
        synonyms=["whack", "thwack", "smack", "bop"],
    ),
    "drop": Verb(drop),
    "take": Verb(take, ["pick up", "grab"]),
    "open": Verb(open),
    **NO_OBJECT_VERBS,
}


# search all verbs and their synonyms
# future: may want to have groups of verbs, or order verbs based on frequency
def find_verb(s: str) -> tuple[str, Verb] | None:
    s = s.lower()
    for k, v in VERBS.items():
        if s == k.lower():
            return k, v
        elif v.search_in_synonyms(s):
            return k, v
    return None
