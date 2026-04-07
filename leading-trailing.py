# LEADING and TRAILING computation 

grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "i"]   # i = id
}

leading = {nt: set() for nt in grammar}
trailing = {nt: set() for nt in grammar}

# Step 1: Add direct terminals
for nt in grammar:
    for prod in grammar[nt]:
        # LEADING
        if not prod[0].isupper():
            leading[nt].add(prod[0])
        # TRAILING
        if not prod[-1].isupper():
            trailing[nt].add(prod[-1])

# Step 2: Iteratively update
changed = True
while changed:
    changed = False
    for nt in grammar:
        for prod in grammar[nt]:

            # LEADING
            if prod[0].isupper():
                before = len(leading[nt])
                leading[nt] |= leading[prod[0]]
                if len(leading[nt]) > before:
                    changed = True

            # TRAILING
            if prod[-1].isupper():
                before = len(trailing[nt])
                trailing[nt] |= trailing[prod[-1]]
                if len(trailing[nt]) > before:
                    changed = True

# Output
print("LEADING:")
for nt in leading:
    print(nt, ":", leading[nt])

print("\nTRAILING:")
for nt in trailing:
    print(nt, ":", trailing[nt])