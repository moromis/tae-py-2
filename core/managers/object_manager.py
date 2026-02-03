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


def set_objects_json(new_objects: dict[str, dict | Object]) -> None:
    global objects
    sanitized_objects = {}
    for n, o in new_objects.items():
        if not isinstance(o, Object):
            obj = Object(n)
            obj.from_dict(o)
            sanitized_objects[n] = obj
    objects = sanitized_objects


def get_object_by_name(obj_name: str) -> Object | None:
    global objects
    obj_name = obj_name.lower()
    for obj_key, obj in objects.items():
        if obj_key == obj_name or (
            obj.adjective and f"{obj.adjective} {obj_key}" == obj_name
        ):
            return obj
