from sys import argv

from common.constants import TRAIN_ARGS
from file_ops.reader import get_lines_from_file

def get_training_cmd_params():
    training_data_file = hypothesis_out_file = learning_type = ''
    if len(argv) > TRAIN_ARGS.COUNT:
        training_data_file \
            = argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['examples']]
        hypothesis_out_file = \
            argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['hypothesisOut']]
        learning_type = argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['learning-type']]
    elif len(argv) == TRAIN_ARGS.COUNT:
        training_data_file \
            = argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['examples']]
        hypothesis_out_file = \
            argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['hypothesisOut']]
        learning_type = input('Please enter learning type: \"dt\" or \"ada\"')
    elif len(argv) == TRAIN_ARGS.COUNT - 1:
        training_data_file \
            = argv[TRAIN_ARGS.TRAIN_ARGS_INDICES['examples']]
        hypothesis_out_file = input('Please enter output file for hypothesis')
        learning_type = input('Please enter learning type: \"dt\" or \"ada\"')
    else:
        training_data_file = input('Please enter training data file: ')
        hypothesis_out_file = input('Please enter hypothesis output file: ')
        learning_type = input('Please enter learning type (\"dt\" or \"ada\"): ')
    
    return training_data_file, hypothesis_out_file, learning_type


def get_parsed_dataset(rows):
    result = []
    for row in rows:
        [label, sentence] = row.split('|')
        word_list = sentence.split()
        word_list.append(label)
        result.append(word_list)
    return result


def get_training_data(file_path):
    lines = get_lines_from_file(file_path)
    return get_parsed_dataset(lines)