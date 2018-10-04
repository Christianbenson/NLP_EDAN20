import os
import re
import pickle
import sys


WORD_REGEX = re.compile(r"[\w'-]+")


def check_input_args(arguments):
    if len(arguments) != 1:  # replace with 2 later on
        print("Please specify one folder to read from. Example: 'python indexer.py selma' ")
        sys.exit()


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


def check_text_files_exist(path):
    files = get_files(path, "txt")
    if len(files) == 0:
        print("No txt-files found. Exiting.")
        sys.exit()


def create_index_from_file(path, input_file):
    indexer_dict = {}
    with open(path + input_file, 'r') as file:
        for word in WORD_REGEX.finditer(file.read(), re.IGNORECASE):
            if word.group(0) in indexer_dict:
                indexer_dict[word.group(0)].append(word.start())
            else:
                indexer_dict[word.group(0)] = [word.start()]
        index_name = path + input_file.split('.')[0] + '_dict' + '.idx'
    pickle.dump(indexer_dict, open(index_name, "wb"))

