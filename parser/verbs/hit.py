from core.types.Character import Character
from core.types.Object import Object

# TODO: make a "What do you want to x" default behavior?
DEFAULT_HIT_RESPONSE = lambda s: f"You hit the {s} but it doesn't do anything."
WHAT_HIT = "What do you want to hit?"


def hit(obj: Object | Character | None = None):
    if not obj:
        return WHAT_HIT
    elif isinstance(obj, Object) or isinstance(obj, Character):
        return DEFAULT_HIT_RESPONSE(obj.name)
    else:
        return DEFAULT_HIT_RESPONSE(obj)
