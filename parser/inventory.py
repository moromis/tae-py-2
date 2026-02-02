from core.types.Object import Object


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
