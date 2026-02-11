from core.managers import room_manager
from core.types.Object import Object
from parser import inventory
from strings import DONT_SEE_HERE, FLOATING_IN_SPACE, THE_WHAT_NOW


def take(**kwargs) -> str:
    obj: Object | None = kwargs.get("object")
    room = room_manager.get_current_room()
    if room and obj:
        if room.has_object(obj):
            inventory.add_to_inventory(obj)
            room_manager.remove_object_from_room(obj, room.name)
            return f"You take the {obj.name}."
        else:
            return DONT_SEE_HERE
    elif not obj:
        return THE_WHAT_NOW
    return FLOATING_IN_SPACE
