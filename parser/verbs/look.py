from core.managers import room_manager
from core.types.Character import Character
from core.types.Object import Object
from strings import DONT_SEE_HERE, FLOATING_IN_SPACE

LOOK_NOT_INTERESTING = lambda obj: f"The {obj} isn't too interesting..."


def look(obj: Object | None = None):
    current_room = room_manager.get_current_room()
    if current_room:
        obj_in_room = current_room.has_object(
            obj.name if obj and isinstance(obj, Object) else obj
        )
        if obj and obj_in_room:
            return obj.desc
        elif obj and not obj_in_room:
            return DONT_SEE_HERE
        return current_room.desc
    return FLOATING_IN_SPACE
