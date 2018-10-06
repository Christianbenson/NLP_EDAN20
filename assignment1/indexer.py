"""
    Script to load files from a given folder
    and extract words from any txt-documents in it
"""
import sys
from assignment1 import helper_functions as hf


def main():
    hf.check_input_args(sys.argv)
    path = "./" + "selma/"  # replace selma with sys.argv[]
    hf.check_text_files_exist(path)
    hf.create_index_from_directory(path)
    hf.merge_indices_in_directory(path)
    hf.calc_and_dump_tf(path)
    hf.calc_and_dump_idf(path)


if __name__ == "__main__":
    main()
