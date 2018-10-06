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
    files = get_files(path, 'txt')
    if len(files) == 0:
        print('No txt-files found. Exiting.')
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
    pickle.dump(indexer_dict, open(index_name, 'wb'))


def create_index_from_directory(path):
    for file in get_files(path, 'txt'):
        create_index_from_file(path, file)


def merge_indices_in_directory(path):
    merged_dict = {}
    for file in get_files(path, 'idx'):
        index = pickle.load(open(path + file, 'rb'))
        for key in index:
            if key in merged_dict:
                merged_dict[key][file.split('_')[0]] = index[key]
            else:
                merged_dict[key] = {file.split('_')[0]: index[key]}
    delete_indices_in_directory(path)
    index_name = path + 'merged_dict' + '.idx'
    pickle.dump(merged_dict, open(index_name, 'wb'))


def words_in_text(input_file):
    with open(input_file, 'r') as file:
        return len(file.read())


def calc_and_dump_tf(path):
    tf_dict = {}
    merged_dict = get_files(path, 'merged_dict.idx')[0]
    index = pickle.load(open(path + merged_dict, 'rb'))
    for word in index:
        for text in index[word]:
            if word in tf_dict:
                tf_dict[word][text] = len(index[word][text]) / words_in_text(path + text + '.txt')
            else:
                tf_dict[word] = {text: len(index[word][text]) / words_in_text(path + text + '.txt')}

    tf_name = path + 'tf_dict' + '.csv'
    pickle.dump(index, open(tf_name, 'wb'))


def calc_and_dump_idf(path):
    print('not finished')

def delete_indices_in_directory(path):
    for file in get_files(path, 'idx'):
        os.remove(path + file)

