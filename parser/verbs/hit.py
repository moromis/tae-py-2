from core.types.Object import Object

# TODO: make a "What do you want to x" default behavior?
DEFAULT_HIT_RESPONSE = lambda s: f"You hit the {s} but it doesn't do anything."
INDIRECT_HIT_RESPONSE = (
    lambda o, i: f"You hit the {o} with the {i} but nothing happens..."
)
WHAT_HIT = "What do you want to hit?"


def hit(**kwargs):
    obj = kwargs.get("object")
    indirect_object = kwargs.get("indirect_object")
    if not obj:
        return WHAT_HIT
    elif isinstance(obj, Object):
        if isinstance(indirect_object, Object):
            return INDIRECT_HIT_RESPONSE(obj.name, indirect_object.name)
        return DEFAULT_HIT_RESPONSE(obj.name)
    else:
        return DEFAULT_HIT_RESPONSE(obj)
