"""
    Script to load files from a given folder
    and extract words from any txt-documents in it
"""
import sys
from assignment1 import helper_functions as hf


def main():
    if len(sys.argv) != 1:  # replace with 2 later on
        print("Please specify one folder to read from. Example: 'python indexer.py selma' ")
        sys.exit()
    path = "./" + "selma/"  # replace selma with sys.argv[]
    files = hf.get_files(path, "txt")
    if len(files) == 0:
        print("No txt-files found. Exiting.")
        sys.exit()
    hf.create_index_from_file(path, files[0])


if __name__ == "__main__":
    main()
