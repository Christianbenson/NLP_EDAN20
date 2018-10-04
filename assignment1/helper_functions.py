import os


def get_files(dir, suffix):
    """
    Returns all the files in a folder ending with suffix
    Author: Pierre Nugues
    :param dir:
    :param suffix:
    :return: the list of file names
    """
    files = []
    for file in os.listdir(dir):
        if file.endswith(suffix):
            files.append(file)
    return files

