""" Given an array, return the two numbers who add up to
    a number 'k', just scan the array once """

""" Solution: Look for pairs max() and min() as:
    $(k - i) + i$ """

from random import random

# Algorithm
def solve(arr, k):
    pairs = []
    for i in range(len(arr)):
        if arr[i] > k:
            continue
        x = arr[i]

        if abs(x - k) in pairs:
            return x, abs(x-k)

        pairs.append(x)

# Create array
arr = [int(random()*10) for x in range(10)]

# Print array
print('Array Chosen:',arr, sep='\t')

# Get 'k'
k = int(random() * 10)

# Print 'k'
print('K Chosen:', k, sep='\t')

# Get pairs
print(solve(arr, k))

