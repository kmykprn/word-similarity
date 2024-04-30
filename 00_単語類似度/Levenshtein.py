import numpy as np
from Levenshtein import ratio, distance


def levenshtein_distance(word_a, word_b):
    return distance(word_a, word_b)


def levenshtein_ratio(word_a, word_b):
    return ratio(word_a, word_b)


# 最も編集距離の小さい値を返す
def compute_similarity(word_list1, word_list2):
    result = []
    for w1 in word_list1:
        max_r = 0
        min_d = 0
        max_w2 = 0
        for w2 in word_list2:
            r = levenshtein_ratio(w1, w2)
            if max_r < r:
                max_r = r
                min_d = levenshtein_distance(w1, w2)
                max_w2 = w2
        # 単語1, 単語2, 最大値, 編集距離
        result.append([w1, max_w2, max_r, min_d])

    return result
    

word_list1 = ["appli","banana","lennon","grap","おざなり"]
word_list2 = ["grape", "apple", "banana", "lemon","なおざり"]
result = compute_similarity(word_list1, word_list2)
print(result)