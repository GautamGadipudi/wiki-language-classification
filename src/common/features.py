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


def is_feature_6(words: list):
    __feature = FEATURES.FEATURE_6
    sum = 0
    for word in words:
        word_length = len(word)
        sum += word_length
    
    avg_word_length = sum / len(words)
    if avg_word_length >= __feature.AVG_WORD_LENGTH:
        return True
    return False


def is_feature_7(words: list):
    __feature = FEATURES.FEATURE_7
    two_char_word_count = 0
    for word in words:
        if len(word) == 2:
            two_char_word_count += 1
    if two_char_word_count / len(words) >= __feature.AVG_FREQ:
        return True
    return False


def is_feature_8(words: list):
    __feature = FEATURES.FEATURE_8
    for word in words:
        for bigram in __feature.COMMON_BIGRAMS:
            if bigram in word:
                return True
    return False


def is_feature_9(words: list):
    __feature = FEATURES.FEATURE_9
    for word in words:
        for trigram in __feature.COMMON_TRIGRAMS:
            if trigram in word:
                return True
    return False 