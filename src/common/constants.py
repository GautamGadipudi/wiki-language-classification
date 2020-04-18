# train args
class TRAIN_ARGS:
    TRAIN_ARGS_INDICES = {
        'examples': 1,
        'hypothesisOut': 2,
        'learning-type': 3
    }
    COUNT = len(TRAIN_ARGS_INDICES)

TEST_ARG_COUNT = 2
LANGUAGE = {
    'ENGLISH': 'en', 
    'DUTCH': 'nl'
}

# file paths
EN_PRE_TRAINING_DATA_FILE_PATH = f"./input/pre_train/{LANGUAGE['ENGLISH']}_pre_train.txt"
NL_PRE_TRAINING_DATA_FILE_PATH = f"./input/pre_train/{LANGUAGE['DUTCH']}_pre_train.txt"
TRAINING_DATA_FILE_PATH = './input/train/train.dat'