# Lab 10: Infix to Postfix and Prefix

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# Infix to Postfix
def infix_to_postfix(expression):
    stack = []
    output = ""

    for char in expression:
        if char.isalnum():  # operand
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(char):
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output

# Infix to Prefix
def infix_to_prefix(expression):
    # Reverse expression
    expression = expression[::-1]

    # Swap brackets
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    postfix = infix_to_postfix(expression)

    # Reverse postfix to get prefix
    return postfix[::-1]

# Main
expr = input("Enter Infix Expression: ")

postfix = infix_to_postfix(expr)
prefix = infix_to_prefix(expr)

print("Postfix:", postfix)
print("Prefix :", prefix)