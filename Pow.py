""" This problem was asked by Google.

Implement integer exponentiation. That is,
implement the pow(x, y) function, where x
and y are integers and returns x^y.

Do this faster than the naive method of
repeated multiplication.

For example, pow(2, 10) should return 1024. """

from math import log2

class Power():
    mem = {0: 1}

    def pow(x, y):
        if y in Power.mem: return Power.mem[y]

        Power.mem[y] = pow(x, y // 2)

        return Power.mem[y] * Power.mem[y] * (1 if y % 2 == 0 else x)

print(Power.pow(3, 10))
