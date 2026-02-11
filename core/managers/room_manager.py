from core import Writeable, Room
from core.types.Character import Character
from core.types.Object import Object
from editor.shared.directions import DIRECTIONS


# TODO: make class, DRY with other managers
rooms: dict[str, Room] = {}
current_room = None


def add_room(room: Room) -> None:
    global rooms
    global current_room
    if len(rooms) == 0:
        current_room = room
        room.is_entrance = True
    rooms[room.name] = room


def add_adjacency(adjacent: str, to_add: str, direction: DIRECTIONS) -> None:
    global rooms
    if len(rooms) == 0:
        raise ValueError("No rooms to add adjacency to")
    rooms[adjacent].add_adjacency(to_add, direction)


# TODO: test
def get_adjacency(r: Room | str, direction: DIRECTIONS) -> Room | None:
    global rooms
    if isinstance(r, str) and r in rooms:
        current = rooms[r]
        str_adj = current.get_adjacency(direction)
        if str_adj:
            return rooms[str_adj]


# TODO: test
def get_current_room_adjacency(direction: DIRECTIONS) -> Room | None:
    global rooms
    global current_room
    if current_room:
        str_adj = current_room.get_adjacency(direction)
        if str_adj:
            return rooms[str_adj]


def get_rooms() -> dict[str, Room]:
    global rooms
    return rooms


def get_rooms_json():
    global rooms
    return {n: r.to_dict() if isinstance(r, Writeable) else r for n, r in rooms.items()}


def set_entrance_room(room: str | Room) -> None:
    global rooms
    if room == None:
        return
    elif isinstance(room, Room):
        room = room.name
    if not len(rooms):
        return

    # clear any other entrances -- there can only be one
    for name, room in rooms.items():
        if room.is_entrance and name != room:
            room.is_entrance = False
        elif name == room:
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


def set_current_room(r: Room):
    global current_room
    current_room = r


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


def add_object_to_room(obj: Object | str, room: Room | str) -> None:
    global rooms
    if isinstance(obj, Object):
        obj = obj.name
    if isinstance(room, Room):
        room = room.name
    rooms[room].add_object(obj)


def remove_object_from_room(obj: Object | str, room: Room | str) -> None:
    global rooms
    if isinstance(obj, Object):
        obj = obj.name
    if isinstance(room, Room):
        room = room.name
    rooms[room].remove_object(obj)


def get_object_from_room(obj: Object | str, room: Room | str) -> str | None:
    global rooms
    if isinstance(obj, Object):
        obj = obj.name
    if isinstance(room, Room):
        room = room.name
    return rooms[room].get_object(obj)


def add_character_to_room(character: Character | str, room: Room | str) -> None:
    global rooms
    if isinstance(character, Character):
        if character.adjective:
            character = f"{character.adjective} {character.name}"
        else:
            character = character.name
    if isinstance(room, Room):
        room = room.name
    rooms[room].add_character(character)


def reset():
    global rooms
    global current_room
    rooms = {}
    current_room = None
