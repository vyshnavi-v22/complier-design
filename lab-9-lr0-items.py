# LR(0) Items Computation (Simple Version)

grammar = [
    "E->E+T",
    "E->T",
    "T->T*F",
    "T->F",
    "F->(E)",
    "F->i"
]

def generate_items(production):
    left, right = production.split("->")
    items = []

    for i in range(len(right) + 1):
        item = right[:i] + "." + right[i:]
        items.append(left + "->" + item)

    return items

# Generate LR(0) items
print("LR(0) ITEMS:\n")

for prod in grammar:
    items = generate_items(prod)
    for item in items:
        print(item)
    print()