from enum import Enum
from core.helpers.fprint import fprint
from strings import NONE

SCHEMA_VERSION = "0.0.1"


class META_KEYS(Enum):
    TITLE = "title"
    FILEPATH = "filepath"
    SCHEMA = "schema"


meta: dict[str, str] = {
    META_KEYS.TITLE.value: NONE,
    META_KEYS.SCHEMA.value: SCHEMA_VERSION,
}


def print_title():
    global meta
    if META_KEYS.TITLE.value in meta:
        fprint(f"Selected Game: {meta[META_KEYS.TITLE.value]}\n", bold=True)
    else:
        fprint(f"Selected Game: {NONE}\n", bold=True)


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
