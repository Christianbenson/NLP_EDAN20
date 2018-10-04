"""
    Script to load files from a given folder
    and extract words from any txt-documents in it
"""
import sys
import re
import pickle
from assignment1 import helper_functions as hf


WORD_REGEX = re.compile(r"[\w'-]+")


def main():
    if len(sys.argv) != 1:  # replace with 2 later on
        print("Please specify one folder to read from. Example: 'python indexer.py selma' ")
        sys.exit()
    path = "./" + "selma/"  # replace selma with sys.argv[]
    files = hf.get_files(path, "txt")
    if len(files) == 0:
        print("No txt-files found. Exiting.")
        sys.exit()
    indexer_dict = {}
    with open(path + files[0], 'r') as file:
        for word in WORD_REGEX.finditer(file.read(), re.IGNORECASE):
            if word.group(0) in indexer_dict:
                indexer_dict[word.group(0)].append(word.start())
            else:
                indexer_dict[word.group(0)] = [word.start()]
        index_name = path + files[0].split('.')[0] + '_dict' + '.idx'
    pickle.dump(indexer_dict, open(index_name, "wb"))


if __name__ == "__main__":
    main()
