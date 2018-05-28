from plagiarism import plagiarism_check
from shingling import shingle_files
import argparse


def main():

        parser = argparse.ArgumentParser(description='Running MinHash for plagiarism detection')
        parser.add_argument('path_files', metavar='f', type=str,
                            help='path to files to check plagiarism')
        parser.add_argument('k_shingle', metavar='k', type=int, help='number of k for shringling')
        parser.add_argument('num_permutations', metavar='n_perm', type=int, help='number of permutations for minhash')

        args = parser.parse_args()
        files_path = args.path_files
        k_arg = args.k_shingle
        num_permutations = args.num_permutations

        shingle_files(files_path, './shingles.pkl', k_arg)
        plagiarism_check('./shingles.pkl', num_permutations)


if __name__ == '__main__':
    main()