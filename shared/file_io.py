import json
import os
import io

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

from editor import character_manager, room_manager
from shared.types.Writeable import Writeable


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


def write_game_data(filepath):
    create_file_if_not_exists(filepath)
    rooms = room_manager.get_rooms()
    characters = character_manager.get_characters()
    add_key_to_json_file(filepath, "rooms", rooms)
    add_key_to_json_file(filepath, "characters", characters)


def create_file_if_not_exists(filename):
    with io.open(f"{filename}.json", "ab"):
        os.utime(filename, None)
    # if not os.path.exists(filename):
    #     with open(filename, 'w') as file:
    #         file.write("Hello, World! This file was created using os.path.")


def add_key_to_json_file(filename, key, data):
    try:
        with open(filename, "rw") as file:
            data = json.load(file)
            data[key] = data.to_dict()
            json.dump(data, file)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file {filename}.")


def write_data_json(filename, data):
    with open(f"{filename}.json", "a") as f:
        if isinstance(data, Writeable):
            data = data.to_dict()
        json.dump(data, f)
