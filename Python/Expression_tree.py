# Postfix expression tree creator and evaluator

operators = {"+", "-", "/", "**", "*"}

class Node:
    def __init__(self, val, left = None, right = None):
        self.val   = val
        self.left  = left
        self.right = right

def evaluate(node):
    if node:
        if node.val not in operators:
            return node.val

        x = evaluate(node.right)
        y = evaluate(node.left)
        return str(eval(node.val.join([x, y])))

def construct_tree(expr):
    operands = list()
    for token in expr:
        if token in operators:
            operands.append(Node(token, operands.pop(), operands.pop()))
        elif token.isnumeric():
            operands.append(Node(token))
    return operands.pop()

if __name__ == '__main__':
    expression_tree = construct_tree(input("Expr: ").split())
    print("Result: ", evaluate(expression_tree))
