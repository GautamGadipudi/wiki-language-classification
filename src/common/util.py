from sys import argv

from common.constants import TRAIN_ARGS
from file_ops.reader import get_lines_from_file
from common.features import is_feature_0,\
                            is_feature_1,\
                            is_feature_2,\
                            is_feature_3,\
                            is_feature_4,\
                            is_feature_5

def get_training_cmd_params():
    training_data_file = hypothesis_out_file = learning_type = ''
    if len(argv) > TRAIN_ARGS.COUNT:
        training_data_file \
            = argv[TRAIN_ARGS.INDEX_OF['examples']]
        hypothesis_out_file = \
            argv[TRAIN_ARGS.INDEX_OF['hypothesisOut']]
        learning_type = argv[TRAIN_ARGS.INDEX_OF['learning-type']]
    elif len(argv) == TRAIN_ARGS.COUNT:
        training_data_file \
            = argv[TRAIN_ARGS.INDEX_OF['examples']]
        hypothesis_out_file = \
            argv[TRAIN_ARGS.INDEX_OF['hypothesisOut']]
        learning_type = input('Please enter learning type: \"dt\" or \"ada\"')
    elif len(argv) == TRAIN_ARGS.COUNT - 1:
        training_data_file \
            = argv[TRAIN_ARGS.INDEX_OF['examples']]
        hypothesis_out_file = input('Please enter output file for hypothesis')
        learning_type = input('Please enter learning type: \"dt\" or \"ada\"')
    else:
        training_data_file = input('Please enter training data file: ')
        hypothesis_out_file = input('Please enter hypothesis output file: ')
        learning_type = input('Please enter learning type (\"dt\" or \"ada\"): ')
    
    return training_data_file, hypothesis_out_file, learning_type


def get_featured_dataset(sentence, label=None):
    result = []
    words = sentence.split()
    result.append(is_feature_0(words))
    result.append(is_feature_1(words))
    result.append(is_feature_2(words))
    result.append(is_feature_3(words))
    result.append(is_feature_4(words))
    result.append(is_feature_5(words))

    # For testing features
    if label is not None:
        result.append(label)

    return result

def get_parsed_dataset(rows):
    result = []
    for row in rows:
        [label, sentence] = row.split('|')
        result.append(get_featured_dataset(sentence, label))
    return result


def get_training_data(file_path):
    lines = get_lines_from_file(file_path)
    return get_parsed_dataset(lines)