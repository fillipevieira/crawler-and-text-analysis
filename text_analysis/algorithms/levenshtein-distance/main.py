import numpy as np
from itertools import product

def levenshtein_distance(text1, text2):
    size1 = len(text1) + 1
    size2 = len(text2) + 1
    matrix = np.zeros((size1, size2))
    for x in range(size1):
        matrix[x, 0] = x
    for y in range(size2):
        matrix[0, y] = y

    for x, y in product(range(1, size1), range(1, size2)):
        if text1[x-1] == text2[y-1]:
            minimum = min(
                matrix[x-1, y],
                matrix[x-1, y-1],
                matrix[x, y-1]
            )
            matrix[x, y] = minimum
        else:
            minimum_plus_one = min(
                matrix[x-1, y] + 1,
                matrix[x-1, y-1] + 1,
                matrix[x, y-1] + 1
            )
            matrix[x, y] = minimum_plus_one

    print(matrix)
    return matrix[size1 - 1, size2 - 1]


result = levenshtein_distance('azced', 'abcdef')
print(result)
