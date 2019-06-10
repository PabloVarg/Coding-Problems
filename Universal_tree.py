""" This problem was asked by Google.

A unival tree (which stands for "universal value")
is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of
unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

# Node class definition
class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm
def isUnival(node):
    # Definition of helper methods
    def isLeafe(node):
        return node.left == None and node.right == None

    def hasEqualChilds(node):
        return node.left.val == node.right.val

    # Return on None
    if node == None:
        return 0

    # Logic
    count = 1 if isLeafe(node) or hasEqualChilds(node) else 0

    # Continue traversing
    return isUnival(node.left) + isUnival(node.right) + count

# Run
node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

assert isUnival(node) == 5, "It is wrong"
print("It is right")
