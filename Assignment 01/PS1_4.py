"""
Add or double
"""
import math


def Least_moves(x):
    cnt = 0
    while x > 1:
        cnt += x % 2
        x = math.floor(x / 2)
        cnt += 1
    return cnt


if __name__ == "__main__":
    print(Least_moves(10))
    print(Least_moves(50))
    print(Least_moves(99))
