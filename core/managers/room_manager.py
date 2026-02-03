from core import Writeable, Room


# TODO: make class, DRY with other managers
rooms: dict[str, Room] = {}
current_room = None


def add_room(room: Room) -> None:
    global rooms
    global current_room
    if len(rooms) == 0:
        current_room = room
    rooms[room.name] = room


def get_rooms() -> dict[str, Room]:
    global rooms
    return rooms


def get_rooms_json():
    global rooms
    return {n: r.to_dict() if isinstance(r, Writeable) else r for n, r in rooms.items()}


def set_entrance_room(room_name: str) -> None:
    global rooms
    if not len(rooms):
        return

    # clear any other entrances -- there can only be one
    for name, room in rooms.items():
        if room.is_entrance and name != room_name:
            room.is_entrance = False
        elif name == room_name:
            room.is_entrance = True


def get_entrance_room() -> Room | None:
    global rooms
    if not len(rooms):
        return None

    for name, room in rooms.items():
        if room.is_entrance:
            return room

    return rooms[list(rooms.keys())[0]]


def get_current_room():
    global current_room
    return current_room


# TODO: DRY w/ other managers
def set_rooms(new_rooms: dict[str, Room]) -> None:
    global rooms
    global current_room
    rooms = new_rooms
    # TODO: DRY?
    entrance_room = get_entrance_room()
    if entrance_room:
        current_room = entrance_room


# TODO: DRY w/ other managers
def set_rooms_json(new_rooms: dict[str, Room | dict]) -> None:
    global rooms
    global current_room
    sanitized_rooms = {}
    for n, o in new_rooms.items():
        if not isinstance(o, Room):
            obj = Room(n)
            obj.from_dict(o)
            sanitized_rooms[n] = obj
    rooms = sanitized_rooms
    entrance_room = get_entrance_room()
    if entrance_room:
        current_room = entrance_room


def add_object_to_room(obj_name: str, room_name: str) -> None:
    global rooms
    rooms[room_name].add_object(obj_name)


def remove_object_from_room(obj_name: str, room_name: str) -> None:
    global rooms
    rooms[room_name].remove_object(obj_name)


def get_object_from_room(obj_name: str, room_name: str) -> str | None:
    global rooms
    return rooms[room_name].get_object(obj_name)


def add_character_to_room(character: str, room_name: str) -> None:
    global rooms
    rooms[room_name].add_character(character)


def reset():
    global rooms
    global current_room
    rooms = {}
    current_room = None
