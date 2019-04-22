""" Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well. """

# Achieved linear time and linear spece
from random import random

# Algorithm
def findminimum(arr):
    mem = set()
    for x in arr:
        if x >= 0:
            mem.add(x)
    return choose(mem)

def choose(memory):
    x = 0
    while True:
        if x not in memory:
            return x
        x += 1

# Generate random array
arr = [int(random()*20-10) for x in range(int(random()*10))]
print(arr)

# Test of algorithm
print(findminimum(arr))
