def handle_new_list(list_versions, current_version, order):
    while current_version < len(list_versions) - 1:
        list_versions.pop()
    list_versions.append(order)
    return list_versions


def handle_undo(list_versions, current_version):
    if current_version < 0:
        raise ValueError("Can't undo anymore!")
    return list_versions[current_version]


def handle_redo(list_versions, current_version):
    if current_version == len(list_versions) - 1:
        raise ValueError("You're running on the latest version.")
    return list_versions[current_version]
