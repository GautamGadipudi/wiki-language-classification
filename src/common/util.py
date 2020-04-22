from sys import argv
import re

from common.constants import TRAIN_ARGS, TEST_ARGS, LANGUAGE
from file_ops.reader import get_lines_from_file
from common.features import is_feature_0,\
                            is_feature_1,\
                            is_feature_2,\
                            is_feature_3,\
                            is_feature_4,\
                            is_feature_5
from ada.util import ada_classify
from dt.util import predict
from dt.classes import Leaf


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


def get_testing_cmd_params():
    testing_data_file = hypothesis_in_file = ''
    if len(argv) > TEST_ARGS.COUNT:
        testing_data_file \
            = argv[TEST_ARGS.INDEX_OF['file']]
        hypothesis_in_file = \
            argv[TEST_ARGS.INDEX_OF['hypothesis']]
    elif len(argv) == TRAIN_ARGS.COUNT:
        hypothesis_in_file = \
            argv[TEST_ARGS.INDEX_OF['hypothesis']]
        testing_data_file = input('Please enter predicting/testing data file: ')
    else:
        hypothesis_in_file = input('Please enter hypothesis pickle file: ')
        testing_data_file = input('Please enter predicting/testing data file: ')
    
    return hypothesis_in_file, testing_data_file


def get_list_of_words(sentence: str) -> list:
    word_list = re.sub('[^A-Za-záéíóúàèëïöüĳÁÉÍÓÚÀÈËÏÖÜĲ ]+', '', sentence) \
                    .lower() \
                    .strip() \
                    .split()
    
    return word_list


def get_featured_row(sentence, label=None):
    result = []
    words = get_list_of_words(sentence)
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

def get_parsed_dataset(rows, is_training_file=False):
    result = []
    for row in rows:
        label = None
        sentence = ''
        if is_training_file:
            [label, sentence] = row.split('|')
        else:
            sentence = row
        result.append(get_featured_row(sentence, label))
    return result


def get_featured_dataset(file_path, is_training_file=False):
    lines = get_lines_from_file(file_path)
    return get_parsed_dataset(lines, is_training_file)


def classify(row, node) -> list:
    """
    Classify an example into a class/classes.
    :param row: Example/testing data
    :type row: list
    :param node: Node which has question/prediction
    :type node: DecisionNode or Leaf
    :return: List of possible classes
    :rtype: list
    """
    if isinstance(node, list): #ADA
        return ada_classify(row, trees=node)
    else: #DT
        if isinstance(node, Leaf):
            return predict(node.predictions)

        if node.question.match(row):
            return classify(row, node.true_branch)
        else:
            return classify(row, node.false_branch)