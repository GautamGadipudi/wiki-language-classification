import pickle
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dt.class_util import classify, print_tree
from common.util import get_featured_dataset


def main():
    node = pickle.load(open('./output/train/tree_node.p', 'rb'))
    print_tree(node)
    example = 'hi my name is blah what is your name very nice to meet you man'
    example_features = get_featured_dataset(example)
    x = classify(example_features, node)
    print(x)

if __name__ == "__main__":
    main()