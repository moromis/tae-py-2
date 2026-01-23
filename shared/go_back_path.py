from shared.split import split_by_dot


def go_back_path(path):
    keys = split_by_dot(path)
    return ".".join(keys[:-1])
