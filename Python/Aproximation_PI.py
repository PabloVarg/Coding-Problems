""" This problem was asked by Google.

The area of a circle is defined as πr^2.
Estimate π to 3 decimal places using a
Monte Carlo method.

Hint: The basic equation of a circle is
x2 + y2 = r2. """

import random as rand

# Algorithm
def getPi(cycles):
    r = 1
    count = 0

    for _ in range(cycles):
        count += 1 if rand.random()**2 + rand.random()**2 <= r else 0

    return 4 * count / cycles

cycles = 1_000_000_000
print(getPi(cycles))
