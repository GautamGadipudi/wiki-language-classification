import re
import os, sys
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import LANGUAGE

def get_lines_from_file(file_path: str) -> list:
    try:
        file = open(file_path, 'r', encoding='utf-8')
        lines = file.readlines()
        return lines
    except IOError as e:
        print('File error!')
        print(e)
    except Exception as e: 
        print('Some other error!')
        print(e)
    finally:
        if not file.closed:
            file.close()
            

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


def main():
    en_training_data = get_compiled_training_set('./input/en_pre_train.txt', LANGUAGE['ENGLISH'])
    nl_training_data = get_compiled_training_set('./input/nl_pre_train.txt', LANGUAGE['DUTCH'])
    training_data = en_training_data + nl_training_data
    random.shuffle(training_data)
    print(training_data[:15])


if __name__ == "__main__":
    main()