from core import Writeable, Object


objects: dict[str, Object] = {}


def add_object(object: Object) -> None:
    global objects
    objects[object.name] = object


def get_objects() -> dict[str, Object]:
    global objects
    return objects


def get_objects_json():
    global objects
    return {
        n: o.to_dict() if isinstance(o, Writeable) else o for n, o in objects.items()
    }


def set_objects(new_objects: dict[str, Object]) -> None:
    global objects
    objects = new_objects
