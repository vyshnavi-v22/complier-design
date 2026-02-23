# Elimination of Left Recursion

def eliminate_left_recursion(non_terminal, productions):
    alpha = []
    beta = []

    for prod in productions:
        if prod.startswith(non_terminal):
            alpha.append(prod[len(non_terminal):])
        else:
            beta.append(prod)

    if not alpha:
        return productions

    new_non_terminal = non_terminal + "'"
    new_productions = []

    for b in beta:
        new_productions.append(b + new_non_terminal)

    new_alpha = []
    for a in alpha:
        new_alpha.append(a + new_non_terminal)
    new_alpha.append("ε")

    return new_productions, new_alpha, new_non_terminal


# Left Factoring

def left_factoring(non_terminal, productions):
    prefix = productions[0]
    for prod in productions[1:]:
        i = 0
        while i < min(len(prefix), len(prod)) and prefix[i] == prod[i]:
            i += 1
        prefix = prefix[:i]

    if prefix == "":
        return productions

    new_non_terminal = non_terminal + "'"
    factored = [prefix + new_non_terminal]
    remaining = [prod[len(prefix):] if prod[len(prefix):] != "" else "ε"
                 for prod in productions]

    return factored, remaining, new_non_terminal


# Example Grammar
non_terminal = "A"
productions = ["Aa", "Ab", "c"]

print("Original Productions:", productions)

print("\nAfter Eliminating Left Recursion:")
lr = eliminate_left_recursion(non_terminal, productions)
print(lr)

print("\nAfter Left Factoring:")
lf = left_factoring("A", ["ab", "ac"])
print(lf)