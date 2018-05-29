import pickle
from os import listdir
from os.path import isfile, join
import string


def shingle_files(path_to_files, file_output='./shingles.pkl', k=2):
    """
    Division of each file into shingles of a given length. With hashing values of each shingle.
    Each shingle consists of k number of words.
    :param path_to_files:
    :param k: number of words for shingling
    :return: creates pickle file with dictionary
    """
    files_list = [path_to_files + '/' + f for f in listdir(path_to_files) if isfile(join(path_to_files, f))]

    files_shingle_dict, shingle_dict = {}, {}

    count = 0
    for file in files_list:
        f = open(file, "r", encoding='latin-1')
        words = f.read().split(" ")

        # get rid of punctuation
        exclude = set(string.punctuation)
        words = [''.join(ch for ch in w if ch not in exclude) for w in words]

        temp = set()
        for index in range(0, len(words) - k):
            shingle = ''
            for k_gram in range(k):
                shingle += words[index+k_gram] + " "

            if shingle not in shingle_dict.keys():
                shingle_dict[shingle] = count
                count += 1
            temp.add(shingle_dict[shingle])

        name_file = file.split("/")[-1].split(".")[0]
        files_shingle_dict[name_file] = temp

    # print(shingleDict)
    output = open(file_output, 'wb')
    pickle.dump(files_shingle_dict, output)
    output.close()

    return 0

# shingle_files('/home/maria/Documents/Courses_UCU/mmds/corpus', "./shingles.pkl",  3)
