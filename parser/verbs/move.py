from core.managers import room_manager
from editor.shared.directions import DIRECTIONS
from strings import CANT_MOVE_THAT_WAY, GO_WHERE, NOTHING_THAT_DIRECTION


def move(**kwargs) -> str | None:
    rest = kwargs.get("rest")
    verb_name = kwargs.get("verb")
    direction = None
    if verb_name and (not rest or len(rest) == 0):
        direction = DIRECTIONS[verb_name.upper()]
    elif rest:
        direction = DIRECTIONS[" ".join(rest).upper()]
    if direction:
        current = room_manager.get_current_room()
        adj = room_manager.get_current_room_adjacency(direction)
        if not current:
            return CANT_MOVE_THAT_WAY
        if adj:
            room_manager.set_current_room(adj)
            return adj.desc
        else:
            return NOTHING_THAT_DIRECTION
    return GO_WHERE
