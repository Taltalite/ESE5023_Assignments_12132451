"""
Matrix multiplication
"""
import random


def matrix_gen(rows, cols):
    matrix = [[random.randint(0, 50) for i in range(cols)] for i in range(rows)]
    return matrix


def Matrix_multip(m1, m2):
    if len(m1[0]) != len(m2):
        raise ValueError("Matrix_multip: cols of m1 must be equal to rows of m2!")
    res_m = matrix_gen(len(m1), len(m2[0]))
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            res = 0
            for k in range(len(m2)):
                res += m1[i][k] * m2[k][j]
            res_m[i][j] = res

    return res_m


if __name__ == "__main__":
    m1 = matrix_gen(5, 10)
    m2 = matrix_gen(10, 5)
    res = Matrix_multip(m1, m2)
    print('m1:')
    print(m1)
    print('m2:')
    print(m2)
    print('m1 * m2:')
    print(res)
