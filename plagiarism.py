import numpy as np
import pickle
from scipy.spatial import distance
import time


def generate_matrix(reader):
    """
    Matrix generation. Iterate over the rows, writing the index in the respective
    cell,if the word being checked is present in the sentence.
    :param reader: dictionary of shingled characters, or words
    :return: matrix (numpy array) shape = [len(unique_shingles), len(unique_files)]
    """
    unique_files = set(dic for dic in reader.keys())
    unique_shingles = set(shingle for val in reader.values() for shingle in val)
    matrix = np.empty([len(unique_shingles), len(unique_files)])

    random_rows = np.arange(len(matrix))
    np.random.shuffle(random_rows)

    for i, row_index in enumerate(random_rows):
        for j, col in enumerate(matrix[row_index,:]):
            file = list(reader.keys())[j]
            if row_index in reader[file]:
                matrix[i, j] = i + 1
            else:
                matrix[i, j] = 0

    return matrix


def plagiarism_check(shingled_data='./shingles.pkl', num_permutations=20):
    reader = pickle.load(open(shingled_data, 'rb'))
    unique_files = set(dic for dic in reader.keys())
    unique_shingles = set(shingle for val in reader.values() for shingle in val)

    perm_matrix = np.empty([len(unique_files), num_permutations])
    for perm in range(num_permutations):
        matrix = generate_matrix(reader)

        for col in range(matrix.shape[1]):
            first_nonzero = np.min(np.nonzero(matrix[:, col])) + 1
            perm_matrix[col, perm] = int(first_nonzero)

    for i, file_ in enumerate(perm_matrix):
        for sec_f in range(i, len(perm_matrix)-1):
            # The bigger the distance the less similar documents are
            dist = distance.jaccard(perm_matrix[i], perm_matrix[sec_f+1])
            if dist < 0.7:  # this parameter can vary, this is a confidence level
                print("Files: " + list(reader.keys())[i] + " and " + list(reader.keys())[sec_f+1])
                print(dist)

    np.savetxt("./matrix.txt", perm_matrix.astype(int))
    return 0

# st = time.time()
# plagiarism_check("./shingles.pkl")
#
# print(time.time() - st)