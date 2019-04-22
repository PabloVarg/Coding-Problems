""" Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the numbers
in the original array except the one at i. """

from random import random

# Algorithm
def calculate_mul(arr):
    mul = 1
    for x in arr:
        mul*=x
    return mul

def generate_mul(arr):
    product = calculate_mul(arr)
    new = []
    for x in arr:
        if x == 0:
            continue
        new.append(product / x)
    return new

# Generate initial array
arr = [int(random()*10)+1 for x in range(int(random()*10)+1)]

# Show array
print('Array', arr, sep=': ')

# Show new array
print('New Array', generate_mul(arr), sep=': ')
