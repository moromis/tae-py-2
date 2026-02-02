from core.types.Object import Object


class Inventory:
    def __init__(self) -> None:
        self.inventory = {}

    def add_to_inventory(self, obj: Object) -> None:
        self.inventory[obj.name] = obj

    def remove_from_inventory(self, obj_name: str) -> Object:
        return self.inventory.pop(obj_name)

    def get_inventory(self):
        return self.inventory
