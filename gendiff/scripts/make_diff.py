def make_diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    result = {}
    for key in keys:
        if key not in dict1:
            result[key] = {
                "type": "option",
                "status": "added",
                "value": dict2[key],
            }
        elif key not in dict2:
            result[key] = {
                "type": "option",
                "status": "removed",
                "value": dict1[key],
            }
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            result[key] = {
                "type": "node",
                "childrens": make_diff(dict1[key], dict2[key]),
            }
        elif dict1[key] != dict2[key]:
            result[key] = {
                "type": "option",
                "status": "updated",
                "old_value": dict1[key],
                "new_value": dict2[key],
            }
        else:
            result[key] = {
                "type": "option",
                "status": "same",
                "value": dict1[key],
            }

    return result
