import os
import re
import pickle


WORD_REGEX = re.compile(r"[\w'-]+")


def get_files(directory, suffix):
    """
    Returns all the files in a folder ending with suffix
    Author: Pierre Nugues
    :param dir:
    :param suffix:
    :return: the list of file names
    """
    files = []
    for file in os.listdir(directory):
        if file.endswith(suffix):
            files.append(file)
    return files


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

