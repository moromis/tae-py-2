from core.types.Object import Object
from strings import NO_INVENTORY


inventory = []


def add_to_inventory(obj_name: str) -> None:
    global inventory
    inventory.append(obj_name)


def remove_from_inventory(obj_name: str) -> None:
    global inventory
    inventory.remove(obj_name)


def get_inventory():
    global inventory
    return inventory


def has(obj_name):
    global inventory
    return obj_name in inventory


def reset():
    global inventory
    inventory = []


def get_inventory_string():
    global inventory
    inventory_string = NO_INVENTORY
    if len(inventory):
        inventory_string = "- "
        inventory_string += "\n- ".join(inventory)
    return inventory_string
