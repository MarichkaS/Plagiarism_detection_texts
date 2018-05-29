from plagiarism import plagiarism_check_minhash_permutations, plagiarism_check_minhash
from shingling import shingle_files
import argparse
import time

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

        st = time.time()
        shingle_files(files_path, './shingles.pkl', k_arg)
        # plagiarism_check_minhash_permutations('./shingles.pkl', num_permutations)
        plagiarism_check_minhash('./shingles.pkl', num_hash=num_permutations)
        print("Done in ",time.time() - st, " seconds")

if __name__ == '__main__':
    main()