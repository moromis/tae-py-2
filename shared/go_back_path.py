from shared.split import split_by_dot
from strings import BASE_PATH


def go_back_path(path: str) -> str:
    if path == BASE_PATH:
        return BASE_PATH
    keys = split_by_dot(path)
    return ".".join(keys[:-1])
