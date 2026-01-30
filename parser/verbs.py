# verbs, their synonyms, and their verb default behaviors

from parser.types.Verb import Verb


VERBS = {
    "hit": Verb(
        lambda obj: f"You hit the {obj} but it doesn't do anything",
        synonyms=["whack", "thwack", "smack", "bop"],
    )
}
