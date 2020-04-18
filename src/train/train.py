import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.util import get_training_cmd_params, get_training_data
from file_ops.reader import get_lines_from_file

def main():
    training_data_file, hypothesis_out_file, learning_type = get_training_cmd_params()
    training_data = get_training_data(training_data_file)
    print(training_data[:15])


if __name__ == "__main__":
    main()