from enum import Enum
from shared.fprint import fprint


class META_KEYS(Enum):
    TITLE = "title"
    FILEPATH = "filepath"


meta: dict[str, str] = {META_KEYS.TITLE.value: "No game loaded"}


def print_title():
    global meta
    if meta[META_KEYS.TITLE.value]:
        fprint(f"Selected Game: {meta[META_KEYS.TITLE.value]}\n", bold=True)
    else:
        fprint("No title found", bold=True)


def set_meta(new_meta):
    global meta
    meta = new_meta


def set_meta_by_key(key: META_KEYS, data):
    global meta
    meta[key.value] = data


def get_meta():
    global meta
    return meta


def get_meta_by_key(key: META_KEYS):
    global meta
    return meta[key.value]
