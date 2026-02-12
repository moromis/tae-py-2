import json
import os
from core import error_logger
from core.file_io import select_file
from core.helpers.fprint import fprint
from core.managers import room_manager
from core.managers.meta import meta_manager
from core.managers.meta.meta_manager import META_KEYS, CURRENT_SCHEMA_VERSION, set_meta
from core.managers.meta.migrations import Migrator
from core.managers.object_manager import Object_Manager


def _set_or_default(setter, data, key, default={}):
    if key in data:
        setter(data[key])
    else:
        setter(default)


def load_game(filepath: str | None = None) -> bool:
    # try and resolve relative paths
    if filepath and filepath[0] == ".":
        filepath = os.getcwd() + filepath[1:]
    # select file if we aren't passed one
    if not filepath:
        filepath = select_file()
    # load file
    try:
        with open(filepath) as file:
            file_contents = json.load(file)

            Migrator.set_json(file_contents)
            if Migrator.needs_migration():
                fprint("Game needs migration. Please wait.")
                filepath = f"{filepath.replace(".json", "")}_{CURRENT_SCHEMA_VERSION}"
                meta_manager.set_meta_by_key(META_KEYS.FILEPATH, filepath)
                file_contents["meta"][META_KEYS.FILEPATH.value] = f"filepath.json"
                file_contents = Migrator.migrate()
                input("Press Enter to continue...")

            # load file contents into managers
            _set_or_default(room_manager.set_rooms_json, file_contents, "rooms")
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
    Object_Manager.set({})
    set_meta({})
