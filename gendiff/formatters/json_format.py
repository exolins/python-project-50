import json


def json_view(diff_value):
    return json.dumps(diff_value, indent=4, sort_keys=True)
