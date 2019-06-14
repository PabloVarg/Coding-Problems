""" This problem was asked by Google.

Implement integer exponentiation. That is,
implement the pow(x, y) function, where x
and y are integers and returns x^y.

Do this faster than the naive method of
repeated multiplication.

For example, pow(2, 10) should return 1024. """

from math import log2

def pow(x, y):
    if y == 0: return 1

    return pow(x, y // 2) * pow(x, y // 2) * (1 if y % 2 == 0 else x)

print(pow(2, 10))
