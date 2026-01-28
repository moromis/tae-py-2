from shared.types.Room import Room

rooms: dict[str, Room] = {}


def add_room(room: Room) -> None:
    rooms[room.name] = room


def get_rooms() -> dict[str, Room]:
    return rooms
