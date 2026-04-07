# Lab 12: Simple Code Generator

expr = input("Enter expression (e.g., A+B*C): ")

operators = []
operands = []

# Separate operators and operands
for ch in expr:
    if ch in "+-*/":
        operators.append(ch)
    else:
        operands.append(ch)

temp_count = 1
code = []

# Handle multiplication and division first
i = 0
while i < len(operators):
    if operators[i] in "*/":
        op = operators[i]
        arg1 = operands[i]
        arg2 = operands[i+1]

        temp = "t" + str(temp_count)
        temp_count += 1

        code.append(f"{temp} = {arg1} {op} {arg2}")

        operands[i] = temp
        operands.pop(i+1)
        operators.pop(i)
    else:
        i += 1

# Handle addition and subtraction
i = 0
while i < len(operators):
    op = operators[i]
    arg1 = operands[i]
    arg2 = operands[i+1]

    temp = "t" + str(temp_count)
    temp_count += 1

    code.append(f"{temp} = {arg1} {op} {arg2}")

    operands[i] = temp
    operands.pop(i+1)
    operators.pop(i)

# Output
print("\nGenerated Three Address Code:")
for line in code:
    print(line)