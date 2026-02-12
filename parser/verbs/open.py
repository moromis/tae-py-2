from core.types.Object import Object
from core.types.ObjectProperties import OBJECT_PROPERTIES
from strings import CANT_OPEN, DONT_SEE_HERE


def open(**kwargs):
    object: Object | None = kwargs.get("object")
    if object:
        if object.get_property(OBJECT_PROPERTIES.OPEN) == False:
            object.set_property(OBJECT_PROPERTIES.OPEN, True)
            return f"The {object.name} is now open"
        elif object.get_property(OBJECT_PROPERTIES.OPEN) == True:
            return f"The {object.name} is already open"
        else:
            return CANT_OPEN
    else:
        return DONT_SEE_HERE
