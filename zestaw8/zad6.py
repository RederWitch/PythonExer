"""
P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.
"""

RESULT = {(0, 0): 0.5}


def P(i, j):
    global RESULT
    if (i < 0) or (j < 0):
        raise ValueError("funkcja nie osługuje argumentów mniejszych od 0")
    if (i, j) not in RESULT:
        if j == 0:
            RESULT[i, j] = 0
        elif i == 0:
            RESULT[i, j] = 1
        else:
            RESULT[i, j] = 0.5*P(i-1, j) + P(i, j-1)
    return RESULT[i, j]


print(P(0, 0))
print(P(0, 2))
print(P(1, 0))
print(P(2, 3))
print(P(3, 1))
