from core.managers import room_manager
from core.types.Object import Object
from parser import inventory
from strings import DONT_HAVE_THAT, FLOATING_IN_SPACE, THE_WHAT_NOW


def drop(**kwargs) -> str:
    obj: Object | None = kwargs.get("object")
    room = room_manager.get_current_room()
    if room and obj:
        obj_name = obj.name
        if obj_name and inventory.has(obj_name):
            inventory.remove_from_inventory(obj_name)
            room_manager.add_object_to_room(obj_name, room.name)
            return f"You drop the {obj_name}."
        elif not obj_name:
            return THE_WHAT_NOW
        else:
            return DONT_HAVE_THAT
    elif not obj:
        return THE_WHAT_NOW
    return FLOATING_IN_SPACE
