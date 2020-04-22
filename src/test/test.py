import pickle
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.util import classify
from common.util import get_featured_dataset, get_testing_cmd_params


def main():
    hypothesis_in_file, testing_data_file = get_testing_cmd_params()
    node = pickle.load(open(hypothesis_in_file, 'rb'))
    testing_data = get_featured_dataset(testing_data_file)
    for data in testing_data:
        x = classify(data, node)
        print(x)

if __name__ == "__main__":
    main()

