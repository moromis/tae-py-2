from core import Writeable, Room

rooms: dict[str, Room] = {}


def add_room(room: Room) -> None:
    global rooms
    rooms[room.name] = room


def get_rooms() -> dict[str, Room]:
    global rooms
    return rooms


def get_rooms_json():
    global rooms
    return {n: r.to_dict() if isinstance(r, Writeable) else r for n, r in rooms.items()}


def set_rooms(new_rooms: dict[str, Room]) -> None:
    global rooms
    rooms = new_rooms


def add_object_to_room(object: str, room_name: str) -> None:
    global rooms
    rooms[room_name].add_object(object)


def add_character_to_room(character: str, room_name: str) -> None:
    global rooms
    rooms[room_name].add_character(character)
