# Lab 11: Quadruple, Triple, Indirect Triple

expr = input("Enter expression (e.g., A+B*C): ")

operators = []
operands = []

for ch in expr:
    if ch in "+-*/":
        operators.append(ch)
    else:
        operands.append(ch)

quadruple = []
triple = []
indirect = []

temp_count = 1

# Handle multiplication first
if '*' in operators:
    i = operators.index('*')
    op = '*'
    arg1 = operands[i]
    arg2 = operands[i+1]
    res = "t" + str(temp_count)
    
    quadruple.append((op, arg1, arg2, res))
    triple.append((op, arg1, arg2))
    indirect.append(len(triple)-1)
    
    operands[i] = res
    operands.pop(i+1)
    operators.pop(i)
    temp_count += 1

# Handle addition
if '+' in operators:
    i = operators.index('+')
    op = '+'
    arg1 = operands[i]
    arg2 = operands[i+1]
    res = "t" + str(temp_count)
    
    quadruple.append((op, arg1, arg2, res))
    triple.append((op, arg1, arg2))
    indirect.append(len(triple)-1)

# Output
print("\nQuadruple:")
for q in quadruple:
    print(q)

print("\nTriple:")
for i, t in enumerate(triple):
    print(i, ":", t)

print("\nIndirect Triple:")
for i, ind in enumerate(indirect):
    print(i, "->", ind)