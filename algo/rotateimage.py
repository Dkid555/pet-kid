import numpy as np

def Matrixrotate(matrix):
    n = len(matrix)
    i = 0
    j = 0
    while i < n and j < n + 1:
        if j != n:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1
        else:
            i += 1
            j = i
            if j == n:
                j += 1

    for k in range(n):
        matrix[k] = matrix[k][::-1]




if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
   # a = np.empty(len(matrix))
    a = np.array(matrix[::-1])
    print(a)
    a = np.rot90(a)
    matrix = a.tolist()[::-1]
    print(matrix)

    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Matrixrotate(matrix1)
    print(matrix1)
