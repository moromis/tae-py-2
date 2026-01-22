# from https://stackoverflow.com/questions/31033549/nested-dictionary-value-from-key-path
from shared.split import split_by_dot


def get_from_path(path, obj):
    keys = split_by_dot(path)
    relative_value = obj
    for key in keys:
        relative_value = relative_value[key]
    return relative_value
