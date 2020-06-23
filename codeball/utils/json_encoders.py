import json
from dataclasses import is_dataclass


class DataClassEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return obj.__dict__

        return json.JSONEncoder.default(self, obj)
