from core import Object
from core.types.Writeable import Writeable


class Object_Manager:
    objects: dict[str, Writeable] = {}

    @classmethod
    def add(cls, object: Writeable) -> None:
        cls.objects[object.name] = object

    @classmethod
    def remove(cls, obj_name) -> Writeable:
        ret = cls.objects[obj_name]
        del cls.objects[obj_name]
        return ret

    @classmethod
    def get_all_list(cls) -> list[Writeable]:
        return list(cls.objects.values())

    @classmethod
    def get_all_json(cls) -> dict[str, dict]:
        return {n: o.to_dict() for n, o in cls.objects.items()}

    @classmethod
    def set_from_json(cls, new_objects: dict[str, dict | type[Writeable]]) -> None:
        sanitized_objects = {}
        for n, o in new_objects.items():
            if not isinstance(o, Object):
                obj = Object(n)
                obj.from_dict(o)  # type: ignore
                sanitized_objects[n] = obj
        cls.objects = sanitized_objects

    @classmethod
    def set(cls, new_objects: dict[str, Writeable]) -> None:
        cls.objects = new_objects

    @classmethod
    def get_by_name(cls, obj_name) -> Writeable | None:
        obj_name = obj_name.lower()
        for obj_key, obj in cls.objects.items():
            if obj_key == obj_name or (
                obj.adjective and f"{obj.adjective} {obj_key}" == obj_name
            ):
                return obj

    @classmethod
    def reset(cls) -> None:
        cls.objects = {}
