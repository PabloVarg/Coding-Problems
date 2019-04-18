""" Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree. """

# Class node given by the problem
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Algorithm
def serialize(root, serie):
    if root == None:
        serie.append(root)
        return
    serie.append(root.val)
    serialize(root.left, serie)
    serialize(root.right, serie)
    return serie

def deserialize(serie):
        def _helper(index):
            if serie[index] == None:
                return None, index + 1

            value = serie[index]
            left, index = _helper(index + 1)
            right, index = _helper(index)
            return Node(value, left, right), index
        return _helper(0)[0]

# Test given by the problem
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node, list())).left.left.val == 'left.left'
