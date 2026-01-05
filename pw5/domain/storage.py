import pickle
import gzip
import os

FILE_NAME = "students.dat"

def save_data(data):
    with gzip.open(FILE_NAME, "wb") as f:
        pickle.dump(data, f)


def load_data():
    if not os.path.exists(FILE_NAME):
        return None

    with gzip.open(FILE_NAME, "rb") as f:
        return pickle.load(f)