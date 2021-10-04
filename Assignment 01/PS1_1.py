"""
Flowchart
"""
import random


def Print_values(a, b, c):
    if a > b:
        if b > c:
            print('a: %s, b: %s, c: %s.' % (a, b, c))
        elif a > c:
            print('a: %s, c: %s, b: %s.' % (a, c, b))
        else:
            print('c: %s, a: %s, b: %s.' % (c, a, b))
    elif not b > c:
        print('c: %s, b: %s, a: %s.' % (c, b, a))
    return


if __name__ == "__main__":
    a = random.randint(0, 10000)
    b = random.randint(0, 10000)
    c = random.randint(0, 10000)
    # print(a, b, c)
    Print_values(a, b, c)
