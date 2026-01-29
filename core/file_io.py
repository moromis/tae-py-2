import json
import os

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from core.managers import character_manager, object_manager, room_manager, meta_manager
from core.types.Writeable import Writeable


# https://stackoverflow.com/questions/50860640/ask-a-user-to-select-folder-to-read-the-files-in-python
def select_folder() -> str:
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    path = askdirectory(title="Select Folder")  # shows dialog box and return the path
    return path


# https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog
def select_file() -> str:
    filename = (
        askopenfilename()
    )  # show an "Open" dialog box and return the path to the selected file
    return filename


def write_game_data():
    meta = meta_manager.get_meta()
    filepath = meta_manager.get_meta_by_key(meta_manager.META_KEYS.FILEPATH)
    create_json_file_if_not_exists(filepath)
    rooms = room_manager.get_rooms_json()
    characters = character_manager.get_characters_json()
    objects = object_manager.get_objects_json()
    game_json = form_game_json(meta, rooms, characters, objects)
    write_data_json(filepath, game_json)


def create_json_file_if_not_exists(filename):
    if not os.path.exists(filename):
        with open(f"{filename}.json", "w") as file:
            file.write("{}")


def form_game_json(meta, rooms, characters, objects):
    return {"meta": meta, "rooms": rooms, "characters": characters, "objects": objects}


def add_key_to_json_file(filename, key, data):
    try:
        file_contents = None
        if isinstance(data, Writeable):
            data = data.to_dict()
        with open(f"{filename}.json", "r") as file:
            file_contents = json.load(file)
            file_contents[key] = data
        with open(f"{filename}.json", "w") as file:
            json.dump(file_contents, file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {filename}.")


def write_data_json(filename, data):
    with open(f"{filename}.json", "w") as f:
        if isinstance(data, Writeable):
            data = data.to_dict()
        json.dump(data, f)
