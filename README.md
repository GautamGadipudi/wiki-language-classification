# wiki-language-classification

For this assignment, we will be investigating the use of decision trees and boosted decision stumps to classify text as one of two languages. Specifically, your task is to collect data and train (in several different ways) some decision stumps/trees so that when given a 15 word segment of text from either the English or Dutch Wikipedia, your code will state to the best of its ability which language the text is in.

# Pre-training

Note: The pre-training is used only to read random sentences in Dutch and English from a file and create a training set containing both languages with 15 words on each line with a label. This is not necessarily required because I am already also submitting a training_set: `./input/train/train.dat` which is the output of this.

Run the following in the **root** of the repo:
```bash
python3 ./src/train/pre_train.py
```

# Training

Training the model.
## Training using Decision Tree learning:

Run the following in the **root** of the repo:
```bash
python3 ./src/train/train.py ./input/train/train.dat ./output/tree_node.p dt
```
Tree will be printed on the console.

## Training using Adaboost ensemble learning:

Run the following in the **root** of the repo:
```bash
python3 ./src/train/train.py ./input/train/train.dat ./output/ada_node.p ada
```
Model will be printed on the console.

## Providing own parameters for training:
If you want to give your own parameters use the below snippet or simply run `python3 ./src/train/train.py`
```bash
python3 ./src/train/train.py {training-set-file} {hypothesis-file} {learning-type}
```
Where, 
* `training-set-file` is a file containing labeled examples.
* `hypothesis-file` specifies the file name to write your model to.
* `learning-type` specifies the type of learning algorithm you will run, it is either "dt" or "ada".

# Testing

Testing/predicting examples
Run the following in the **root** of the repo:
## Testing using Decision Tree model:

Run the following in the **root** of the repo:
```bash
python3 ./src/test/test.py ./output/tree_node.p ./input/test/test.dat
```
## Testing using Adaboost ensemble model:

Run the following in the **root** of the repo:
```bash
python3 ./src/test/test.py ./output/ada_node.p ./input/test/test.dat
```

## Providing own parameters for training:
If you want to give your own parameters use the below snippet or simply run `python3 ./src/test/test.py`
```bash
python3 ./src/test/test.py {hypothesis-file} {predictions-file}
```
Where, 
* `hypothesis-file` is a trained decision tree or ensemble created by training program.
* `predictions-file` is a file containing lines of 15 word sentence fragments in either English or Dutch.