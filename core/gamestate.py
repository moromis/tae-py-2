import json
from core import error_logger
from core.file_io import select_file
from core.managers import character_manager, room_manager
from core.managers.meta_manager import META_KEYS, set_meta
from core.managers.object_manager import Object_Manager


def _set_or_default(setter, data, key, default={}):
    if key in data:
        setter(data[key])
    else:
        setter(default)


def load_game() -> bool:
    global filepath
    # select file
    filepath = select_file()
    # load file
    try:
        with open(filepath) as file:
            file_contents = json.load(file)
            # load file contents into managers
            _set_or_default(room_manager.set_rooms_json, file_contents, "rooms")
            _set_or_default(
                character_manager.set_characters_json, file_contents, "characters"
            )
            _set_or_default(Object_Manager.set_from_json, file_contents, "objects")
            _set_or_default(
                set_meta,
                file_contents,
                "meta",
                {META_KEYS.TITLE.value: "NULL", META_KEYS.FILEPATH.value: filepath},
            )
    except Exception as e:
        error_logger.log_error(e)
        return False
    return True


def unload_game():
    room_manager.set_rooms({})
    character_manager.set_characters({})
    Object_Manager.set({})
    set_meta({})
