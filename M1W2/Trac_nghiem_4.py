# Câu 4 c) 3.0
import numpy as np

def levenshtein_distance(token1, token2):
    # Your Code Here
    source = "#" + token1
    target = "#" + token2
    source_len = len(source)
    target_len = len(target)
    D = np.zeros((source_len, target_len))
    for i in range(source_len):
        D[i,0] = i
    for j in range(target_len):
        D[0,j] = j

    for i in range(1, source_len):
        for j in range(1, target_len):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1
            D[i,j] = min(D[i - 1, j] + 1,  # deletion
                        D[i, j - 1] + 1,  # insertion
                        D[i - 1, j - 1] + cost)  # substitution
    distance = D[source_len - 1, target_len - 1]
    # End Code Here
    return distance

if __name__ == '__main__':
    assert levenshtein_distance ("hi", "hello") == 4.0
    print ( levenshtein_distance ("hola", "hello") )
