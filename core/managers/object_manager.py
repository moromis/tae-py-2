from core import Object
from core.types.Character import Character


class Object_Manager:
    objects: dict[str, Object] = {}

    @classmethod
    def add(cls, object: Object) -> None:
        cls.objects[object.name] = object

    @classmethod
    def remove(cls, obj_name) -> Object:
        ret = cls.objects[obj_name]
        del cls.objects[obj_name]
        return ret

    @classmethod
    def get_all_list(cls) -> list[Object]:
        return list(cls.objects.values())

    @classmethod
    def get_all_json(cls) -> dict[str, dict]:
        return {n: o.to_dict() for n, o in cls.objects.items()}

    @classmethod
    def set_from_json(cls, new_objects: dict[str, dict | Object]) -> None:
        sanitized_objects = {}
        for n, o in new_objects.items():
            if not isinstance(o, Object):
                if o.get("is_character", False):
                    obj = Character(n)
                else:
                    obj = Object(n)
                obj.from_dict(o)  # type: ignore
                sanitized_objects[n] = obj
            else:
                sanitized_objects[n] = o
        cls.objects = sanitized_objects

    @classmethod
    def set(cls, new_objects: dict[str, Object]) -> None:
        cls.objects = new_objects

    @classmethod
    def get_by_name(cls, obj_name) -> Object | None:
        obj_name = obj_name.lower()
        for obj_key, obj in cls.objects.items():
            if obj_key == obj_name or (
                obj.adjective and f"{obj.adjective} {obj_key}" == obj_name
            ):
                return obj

    @classmethod
    def reset(cls) -> None:
        cls.objects = {}
