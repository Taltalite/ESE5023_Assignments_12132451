"""
Pascal triangle
"""
import math


def combination(n, k):
    com = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return com


def Pascal_triangle(k):
    kthentry = []
    for i in range(k + 1):
        kthentry.append(int(combination(k, i)))
    print(kthentry)


if __name__ == "__main__":
    Pascal_triangle(100)
