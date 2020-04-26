import pickle
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.constants import LEARNING_TYPE
from common.util import get_training_cmd_params, get_featured_dataset
from file_ops.reader import get_lines_from_file
from dt.class_util import build_tree, print_tree
from ada.ada import ada_boost


def main():
    training_data_file, hypothesis_out_file, learning_type = get_training_cmd_params()
    training_data = get_featured_dataset(training_data_file, True)
    hypothesis = None
    if learning_type == LEARNING_TYPE['ADABOOST']:
        hypothesis = ada_boost(training_data)
        for h in hypothesis:
            print(f"Stump: {h[0].question}, Z: {h[1]}")     
    else:
        hypothesis = build_tree(training_data)
        print_tree(hypothesis)
    pickle.dump(hypothesis, open(hypothesis_out_file, 'wb'))

if __name__ == "__main__":
    main()