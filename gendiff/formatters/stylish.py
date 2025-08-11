SEPARATORS = {
    "unchanged": "  ",
    "added": "+ ",
    "deleted": "- ",
    "tab": "    "
}

diff = {
    'common': ('nested', {
        'follow': ('added', 'false'),
        'setting1': ('unchanged', 'Value 1'),
        'setting2': ('deleted', '200'),
        'setting3': ('changed', 'true', 'null'),
        'setting4': ('added', 'blah blah'),
        'setting5': ('added', {
            'key5': ('usual', 'value5')
        }),
        'setting6': ('nested', {
            'doge': ('nested', {
                'wow': ('changed', '', 'so much')
            }),
            'key': ('unchanged', 'value'),
            'ops': ('added', 'vops')
        })
    }),
    'group1': ('nested', {
        'baz': ('changed', 'bas', 'bars'),
        'foo': ('unchanged', 'bar'),
        'nest': ('changed', {
            'key': ('usual', 'value')
        }, 'str')
    }),
    'group2': ('deleted', {
        'abc': ('usual', '12345'),
        'deep': {
            'id': ('usual', '45')}
    }),
    'group3': ('added', {
        'deep': {
            'id': {
                'number': ('usual', '45')
            }
        },
        'fee': ('usual', '100500')
    })
}


def concat_line(option, key, value, level):
    separator = f"{SEPARATORS["tab"] * (level - 1)}{SEPARATORS["unchanged"]}{SEPARATORS[option]}"
    return f"{separator}{key}: {value}"


def format_stylish(difference):  # noqa: C901
    lines = []
    open = "{"
    close = "}"
    lines.append(open)

    def build_lines(difference, level=1):
        nonlocal lines
        for k, v in difference.items():
            if len(v) == 1:
                option, value = "usual", v
            else:
                option, value = v[0], v[1]

            match option:
                case "usual":
                    if isinstance(value, dict):
                        lines.append(concat_line("unchanged", k, open, level))
                        build_lines(value, level + 1)
                    else:
                        lines.append(concat_line("unchanged", k, value, level))

                case "nested":
                    lines.append(concat_line("unchanged", k, open, level))
                    build_lines(value, level + 1)

                case "changed":
                    value1, value2 = value, v[2]
                    if isinstance(value1, dict):
                        lines.append(concat_line("deleted", k, open, level))
                        build_lines(value1, level + 1)
                    else:
                        lines.append(concat_line("deleted", k, value1, level))
                    if isinstance(value2, dict):
                        lines.append(concat_line("added", k, open, level))
                        build_lines(value2, level + 1)
                    else:
                        lines.append(concat_line("added", k, value2, level))

                case _:
                    if isinstance(value, dict):
                        lines.append(concat_line(option, k, open, level))
                        build_lines(value, level + 1)
                    else:
                        lines.append(concat_line(option, k, value, level))

        lines.append(f"{'    ' * (level - 1)}{close}")

    build_lines(difference)
    res = "\n".join(lines)
    return res
