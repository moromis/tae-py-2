import json

from shared.types.Writeable import Writeable


def write_data_json(filename, data):
    with open(f"{filename}.json", "w") as f:
        if isinstance(data, Writeable):
            data = data.to_dict()
        json.dump(data, f)
