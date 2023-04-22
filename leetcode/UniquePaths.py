"""Unique Paths"""

import numpy as np


def Matrix(m, n):
    Mat = np.ones((m, n), int)
    i, j = 1, 1
    for i in range(1, m):
        for j in range(1, n):
            Mat[i][j] = Mat[i - 1][j] + Mat[i][j - 1]

    return Mat[m - 1][n - 1]


# Matrix(20, 20)

"""OR"""
#main branch
#some changes

def Ones(m, n):
    Mat = [1] * n
    # Mat = np.ones((0,n),int)
    for i in range(1, m):
        for j in range(1, n):
            Mat[j] += Mat[j - 1]
    return Mat[n - 1]


# Ones(5, 5)

if __name__ == "__main__":
    print(Ones(5, 5))
    print(Matrix(5, 5))
