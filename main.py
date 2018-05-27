import numpy
import sys
from plagiarism import plagiarism_check
from shingling import shingle_files
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('path_files', metavar='f', type=str,
                            help='path to files to check plagiarism')
        parser.add_argument('k_shingle', metavar='k', type=int, help='number of k for shringling')
        parser.add_argument('shingle_res_file', metavar='sh_res', type=str, help='file name to save dictionary from '
                                                                                 'shingling')

        args = parser.parse_args()
        files_path = args.path_files
        k_arg = args.k_shingle
        file_name_shingles = args.shingle_res_file

        all_files = shingle_files(files_path, file_name_shingles, k_arg)
        results = plagiarism_check(file_name_shingles)   # "./docShingleDict.pkl"

        # write results to file

    except Exception as ex:
        print('here')
        return 1


if __name__ == '__main__':
    main()