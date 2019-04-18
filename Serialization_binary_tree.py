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
serie = []
def serialize(root):
    global serie
    if root == None:
        serie.append(root)
        return
    serie.append(root.val)
    serialize(root.left)
    serialize(root.right)
    return serie

def deserialize(serie):
    if len(serie) == 0 or serie[0] == 'None':
       return
    node = Node(serie[0])
    serie.pop(0)
    node.left = deserialize(serie)
    node.right = deserialize(serie)
    return node

# Test given by the problem
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
