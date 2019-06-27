""" This problem was asked by Amazon.

There exists a staircase with N steps,
and you can climb up either 1 or 2 steps at
a time. Given N, write a function that returns
the number of unique ways you can climb the
staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps
at a time, you could climb any number from a set of
positive integers X? For example, if X = {1, 3, 5},
you could climb 1, 3, or 5 steps at a time. """

# Algorithm
def number_ways(N, steps, step = 0, count = 0):
    count += step

    if count >= N:
        return 1 if count == N else 0

    answer = 0
    for i in steps:
        answer += number_ways(N, steps, i, count)

    return answer

## Test
print(number_ways(4, {1, 2}))
