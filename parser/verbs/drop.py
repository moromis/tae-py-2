from core.managers import room_manager
from parser import inventory
from strings import DONT_HAVE_THAT, FLOATING_IN_SPACE


def drop(obj_name: str) -> str:
    room = room_manager.get_current_room()
    if room:
        if room.has_object(obj_name):
            inventory.remove_from_inventory(obj_name)
            room_manager.add_object_to_room(obj_name, room.name)
            return f"You drop the {obj_name}."
        else:
            return DONT_HAVE_THAT
    return FLOATING_IN_SPACE
