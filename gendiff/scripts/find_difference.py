def to_string(data):
    if isinstance(data, bool):
        str_data = str(data)
        return f"{str_data[0].lower()}{str_data[1:]}"
    return str(data)


def find_diff(dict1, dict2):
    added = "added"
    deleted = "deleted"
    changed = "changed"
    unchanged = "unchanged"

    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    ans = dict()

    for key in keys:
        if key in dict1 and not key in dict2:
            ans[key] = (deleted, to_string(dict1[key]))
        elif key not in dict1 and key in dict2:
            ans[key] = (added, to_string(dict2[key]))
        elif dict1[key] == dict2[key]:
            ans[key] = (unchanged, to_string(dict2[key]))
        else:
            ans[key] = (changed, to_string(dict1[key]), to_string(dict2[key]))

    return ans


# .\.venv\Scripts\python.exe -m gendiff.scripts.find_difference