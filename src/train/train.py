import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.util import get_training_cmd_params, get_training_data
from file_ops.reader import get_lines_from_file
from dt.class_util import build_tree, print_tree

def main():
    training_data_file, hypothesis_out_file, learning_type = get_training_cmd_params()
    training_data = get_training_data(training_data_file)
    # Do feature extraction
    # node = build_tree(training_data)
    # print_tree(node)


if __name__ == "__main__":
    main()