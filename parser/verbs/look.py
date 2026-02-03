from core.managers import room_manager
from core.types.Character import Character
from core.types.Object import Object
from strings import FLOATING_IN_SPACE


def look(obj=None):
    if obj:
        if isinstance(obj, Object) or isinstance(obj, Character):
            return obj.desc
        else:
            return f"The {obj} isn't too interesting..."
    current_room = room_manager.get_current_room()
    if current_room:
        return current_room.desc
    return FLOATING_IN_SPACE
