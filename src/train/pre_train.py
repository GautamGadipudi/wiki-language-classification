import re
import os, sys
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import LANGUAGE
from file_ops.reader import get_lines_from_file
from file_ops.writer import put_lines_into_file         

def get_list_of_words(sentence: str) -> list:
    word_list = re.sub('[^A-Za-z ]+', '', sentence) \
                    .lower() \
                    .strip() \
                    .split()
    
    return word_list
                                            

def get_compiled_training_set(file_path: str, lang_short_hand: str) -> list:
    lines = get_lines_from_file(file_path)
    training_data = []
    for line in lines:
        words = get_list_of_words(line)
        while True:
            if len(words) < 15:
                break
            training_data.append(f"{lang_short_hand}|{' '.join(words[:15])}")
            words = words[15:]
    return training_data


def put_training_data_into_file(file_path: str, training_data: list):
    put_lines_into_file(file_path, training_data)


def main():
    en_training_data = get_compiled_training_set('./input/pre_train/en_pre_train.txt', LANGUAGE['ENGLISH'])
    nl_training_data = get_compiled_training_set('./input/pre_train/nl_pre_train.txt', LANGUAGE['DUTCH'])
    training_data = en_training_data + nl_training_data
    random.shuffle(training_data)
    put_training_data_into_file('./input/train/train.dat', training_data)

if __name__ == "__main__":
    main()