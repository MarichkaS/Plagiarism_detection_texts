import numpy
import sys
from plagiraism import plagiarism_check
from shingling import shingle_files
import argparse


def main():
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('path_files', metavar='f', type=str,
                            help='path to files to check plagiarism')
        parser.add_argument('k_shingle', metavar='k', type=int, help='number of k for shringling')

        args = parser.parse_args()
        files_path = args.path_files
        k = args.k_shingle

        all_files = shingle_files(files_path, "./docShingleDict.pkl", k)
        results = plagiarism_check("./docShingleDict.pkl")

        # write results to file

    except Exception as ex:
        print('here')
        return 1


if __name__ == '__main__':
    main()