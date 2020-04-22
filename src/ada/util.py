from common.constants import LANGUAGE


def ada_classify(row, trees):
    nl_total_weight = 0
    en_total_weight = 0
    for tree in trees:
        x = tree[0].classify(row)
        if x:
            nl_total_weight += tree[1]
        else:
            en_total_weight += tree[1]
    if nl_total_weight < en_total_weight:
        return LANGUAGE['DUTCH']
    else:
        return LANGUAGE['ENGLISH']