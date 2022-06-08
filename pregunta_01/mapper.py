#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import string
import glob
import os

def load_data(file_path):
    # -----------------------------------------------------------------------------------
    def make_iterator_from_single_file(file_path):
        
        primera_linea = True
        
        with open(file_path, "rt") as file: ##Reading and text mode (default)
            for line in file:
                if primera_linea is True:
                    primera_linea = False
                    continue
                line = line.split(",")[2]#+";"+line.split(";")[-1]
                yield line
    # -----------------------------------------------------------------------------------
    if os.path.isfile(file_path):
        return make_iterator_from_single_file(file_path)
    return make_iterator_from_multiple_files(file_path)

def tolower(x):
    return x.lower()

def remove_punctuation(x):
    return x.translate(str.maketrans("", "", string.punctuation))

def remove_newline(x):
    return x.replace("\n", "")

def split_lines(x):
    return x.split(",")

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt, 0) + 1
    return acc


def sum_counts(left, right):
    for key in right.keys():
        left[key] = left.get(key, 0) + right[key]
    return left

from multiprocessing import Pool
from toolz.functoolz import compose
from toolz.itertoolz import concat

compose_pipeline = compose(
    remove_newline,
    remove_punctuation,
    tolower
)

with Pool() as pool:
    result = pool.map(split_lines, load_data("credit.csv"))
    result = concat(result)
    result = pool.map(compose_pipeline, result)

result
