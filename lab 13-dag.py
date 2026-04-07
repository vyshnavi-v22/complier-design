# Lab 13: DAG Implementation 

class Node:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.left} {self.op} {self.right})"
        return self.op


# DAG storage
dag = {}

def get_node(op, left=None, right=None):
    key = (op, left, right)

    if key in dag:
        return dag[key]   # reuse existing node

    node = Node(op, left, right)
    dag[key] = node
    return node


# Operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


# Convert infix to postfix
def infix_to_postfix(expr):
    stack = []
    output = []

    for ch in expr:
        if ch.isalnum():
            output.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return output


# Build DAG from postfix
def build_dag(postfix):
    stack = []

    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            right = stack.pop()
            left = stack.pop()
            node = get_node(token, left, right)
            stack.append(node)

    return stack[-1]


# MAIN
expr = input("Enter expression: ")

postfix = infix_to_postfix(expr)
root = build_dag(postfix)

print("\nDAG Nodes:")
for k in dag:
    print(k)