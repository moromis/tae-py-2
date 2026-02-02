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


def get_object_by_name(obj_name: str) -> Object | None:
    global objects
    obj_name = obj_name.lower()
    for k, v in objects.items():
        if k == obj_name or "adjective" in v and f"{v["adjective"]} {k}" == obj_name:
            return v
