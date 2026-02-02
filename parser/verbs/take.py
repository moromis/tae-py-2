from core.managers import room_manager
from parser import inventory
from strings import DONT_SEE_HERE, FLOATING_IN_SPACE


def take(obj_name: str) -> str:
    room = room_manager.get_current_room()
    if room:
        if room.has_object(obj_name):
            inventory.add_to_inventory(obj_name)
            room_manager.remove_object_from_room(obj_name, room.name)
            return f"You take the {obj_name}."
        else:
            return DONT_SEE_HERE
    return FLOATING_IN_SPACE
