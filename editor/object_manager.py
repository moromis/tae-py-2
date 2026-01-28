from shared.types.Object import Object


objects: dict[str, Object] = {}


def add_object(object: Object) -> None:
    objects[object.name] = object


def get_objects() -> dict[str, Object]:
    return objects
