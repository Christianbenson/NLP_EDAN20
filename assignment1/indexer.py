import os
import sys


def main():
    if len(sys.argv) != 1:
        print("Please specify one folder to read from. Example: 'python indexer.py selma' ")
        sys.exit()
    path = "./" + sys.argv[0]
    files = get_files(path, "txt")
    if len(files) == 0:
        print("No txt-files found. Exiting.")
        sys.exit()


if __name__ == "__main__":
    main()


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