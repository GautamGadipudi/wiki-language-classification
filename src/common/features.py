from common.constants import FEATURES

def is_feature_0(words: list):
    __feature = FEATURES.FEATURE_0
    count = 0
    for word in words:
        if __feature.IJ in word:
            count += 1
    if count >= __feature.IJ_COUNT_THRESHOLD:
        return True
    return False


def is_feature_1(words: list):
    __feature = FEATURES.FEATURE_1
    for word in words:
        if word in __feature.STRINGS:
            return True
    return False


def is_feature_2(words: list):
    __feature = FEATURES.FEATURE_2
    for word in words:
        if word == __feature.EN:
            return True
    return False


def is_feature_3(words: list):
    __feature = FEATURES.FEATURE_3
    for word in words:
        if word == __feature.AND:
            return True
    return False


def is_feature_4(words: list):
    __feature = FEATURES.FEATURE_4
    for word in words:
        if word in __feature.COMMON_NL_WORDS:
            return True
    return False


def is_feature_5(words: list):
    __feature = FEATURES.FEATURE_5
    for word in words:
        if word in __feature.COMMON_EN_WORDS:
            return True
    return False