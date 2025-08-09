OPTIONS = {
    "added": "  + ",
    "deleted": "  - ",
    "unchanged": "    "
}


def concat_line(option, key, value):
    return f"{OPTIONS[option]}{key}: {value}"


def format1(difference):
    lines = []
    open = "{"
    close = "}"
    lines.append(open)
    for k, v in difference.items():
        option, value = v[0], v[1:]
        match option:
            case "changed":
                lines.append(concat_line("deleted", k, value[0]))
                lines.append(concat_line("added", k, value[1]))
            case _:
                lines.append(concat_line(option, k, value[0]))
    lines.append(close)
    res = "\n".join(lines)
    return res