import json
import os

import platform
import subprocess

from core.helpers.fprint import fprint
from core.managers import room_manager
from core.managers.meta import meta_manager
from core.managers.object_manager import Object_Manager
from core.types.Writeable import Writeable


# https://stackoverflow.com/questions/50860640/ask-a-user-to-select-folder-to-read-the-files-in-python
def select_folder():
    os_name = platform.system()

    # macOS: Use AppleScript 'choose folder'
    if os_name == "Darwin":
        cmd = 'osascript -e "POSIX path of (choose folder)" 2>/dev/null'
        try:
            return subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return None

    # Windows: Use PowerShell 'FolderBrowserDialog'
    elif os_name == "Windows":
        cmd = [
            "powershell",
            "-NoProfile",
            "-Command",
            "Add-Type -AssemblyName System.Windows.Forms; "
            "$f = New-Object System.Windows.Forms.FolderBrowserDialog; "
            "$f.ShowDialog() | Out-Null; $f.SelectedPath",
        ]
        try:
            return subprocess.check_output(cmd).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return None

    # Linux: Use Zenity with the --directory flag
    elif os_name == "Linux":
        try:
            # Zenity is standard for GTK; use --directory to restrict selection
            return (
                subprocess.check_output(["zenity", "--file-selection", "--directory"])
                .decode("utf-8")
                .strip()
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("Zenity not found. Install 'zenity' for Linux folder dialogs.")
            return None

    return None


def select_file():
    os_name = platform.system()

    # macOS: Use AppleScript for a native dialog
    if os_name == "Darwin":
        cmd = 'osascript -e "POSIX path of (choose file of type {\\"public.json\\"})" 2>/dev/null'
        try:
            return subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return None

    # Windows: Use PowerShell to open the native .NET OpenFileDialog
    elif os_name == "Windows":
        filter_str = "JSON Files (*.json)|*.json"
        cmd = [
            "powershell",
            "-NoProfile",
            "-Command",
            "Add-Type -AssemblyName System.Windows.Forms; "
            f"$f = New-Object System.Windows.Forms.OpenFileDialog; $f.Filter = '{filter_str}'; "
            "$f.ShowDialog() | Out-Null; $f.FileName",
        ]
        try:
            return subprocess.check_output(cmd).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return None

    # Linux: Use Zenity (common on GNOME/Ubuntu) or fallback
    elif os_name == "Linux":
        try:
            # Zenity is the standard CLI-to-GUI tool for Linux
            cmd = [
                "zenity",
                "--file-selection",
                "--file-filter=JSON files (*.json) | *.json",
            ]
            return subprocess.check_output(cmd).decode("utf-8").strip()
        except (
            subprocess.CalledProcessError,
            FileNotFoundError,
        ):  # TODO: install zenity as part of installation?
            print(
                "Zenity not found. Please install 'zenity' for file dialogs on Linux."
            )
            return None

    return None


def write_game_data():
    meta = meta_manager.get_meta()
    filepath = meta_manager.get_meta_by_key(meta_manager.META_KEYS.FILEPATH)
    create_json_file_if_not_exists(filepath)
    rooms = room_manager.get_rooms_json()
    objects = Object_Manager.get_all_json()
    game_json = form_game_json(meta, rooms, objects)
    write_data_json(filepath, game_json)


def create_json_file_if_not_exists(filename):
    if not os.path.exists(filename):
        with open(f"{filename}.json", "w") as file:
            file.write("{}")


def form_game_json(meta, rooms, objects):
    return {"meta": meta, "rooms": rooms, "objects": objects}


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
        fprint(f"Error: The file {filename} was not found.")
    except json.JSONDecodeError:
        fprint(f"Error: Could not decode JSON from the file {filename}.")


def write_data_json(filename, data):
    with open(f"{filename}.json", "w") as f:
        if isinstance(data, Writeable):
            data = data.to_dict()
        json.dump(data, f)
