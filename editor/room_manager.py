from shared.types.Room import Room

rooms: dict[str, Room] = {}


def add_room(room: Room) -> None:
    rooms[room.name] = room


def get_rooms() -> dict[str, Room]:
    return rooms


# https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
# def get_room_by_name(room_name: str) -> Room | None:
#     next((x for x in rooms if x.name == room_name), None)
