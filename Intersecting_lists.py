""" This problem was asked by Google.

Given two singly linked lists that intersect
at some point, find the intersecting node. The
lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and
B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value
are the exact same node objects.

Do this in O(M + N) time (where M and N are the
lengths of the lists) and constant space. """

# Algorithm
def get_common_node(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    diff = abs(len1 - len2)

    i, j = diff, 0

    if len2 > len1:
        j, i = i, j

    for x1, x2 in zip(list1[i:], list2[j:]):
        if x1 == x2:
            return x1

    return

# Test
list1, list2 = [3, 7, 8, 10], [99, 1, 8, 10]

print(get_common_node(list1, list2))
