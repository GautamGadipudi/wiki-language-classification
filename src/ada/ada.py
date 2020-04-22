import math
import random

from dt.util import get_gini_impurity, get_info_gain, get_label_count, is_numeric
from dt.class_util import get_best_split
from dt.classes import Question, DecisionNode
from ada.classes import Stump


class Stump:
    __slots__ = ['question']
    

    def __init__(self, question):
        self.question = question


    def classify(self, row):
        return self.question.match(row)


def ada_boost(rows):
    N = len(rows)
    feature_count = len(rows[0]) - 1
    results = [rows[i][-1] == 'nl' for i in range(N)]
    w = [(1 / N) for i in range(N)]
    z = [0 for i in range(feature_count)]
    h = [None for i in range(feature_count)]
    for k in range(feature_count):
        error = 0
        error_count = 0
        new_dataset = rows
        new_dataset, h[k] = learn(new_dataset, w)
        for j in range(N):
            if new_dataset[j][k] is not results[j]:
                error += w[j]
                error_count += 1
        for j in range(N):
            if new_dataset[j][k] is results[j]:
                w[j] *= error / (1 - error)
        w = normalize_weights(w)
        if error == 0:
            z[k] = float('inf')
        elif error == 1:
            z[k] = 0
        else:
            z[k] = math.log((1 - error) / error)
    hypothesis = [(h[k], z[k]) for k in range(feature_count)]
    return hypothesis


def normalize_weights(weights):
    total_weight = sum(weights)
    new_weights = []
    for weight in weights:
        new_weights.append(weight / total_weight)
    return new_weights


def learn(examples, weights):
    weight_limits = []
    curr_w = 0
    for w in weights:
        curr_w += w
        weight_limits.append(curr_w)
    new_dataset = []
    for i in range(len(examples)):
        rand_weight = random.uniform(0, 1)
        for j in range(len(examples)):
            if rand_weight < weight_limits[j]:
                new_dataset.append(examples[j])
                break
    info_gain, question = get_best_split(new_dataset)
    return new_dataset, Stump(question)

