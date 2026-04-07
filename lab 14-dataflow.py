# Lab 14: Global Data Flow Analysis (Reaching Definitions)

print("Enter number of statements:")
n = int(input())

statements = []

for i in range(n):
    stmt = input()
    statements.append(stmt)

# GEN and KILL sets
GEN = []
KILL = []

for i in range(n):
    var = statements[i].split('=')[0].strip()
    
    gen = {f"{var}{i}"}  # unique definition
    kill = set()

    for j in range(n):
        if i != j:
            other_var = statements[j].split('=')[0].strip()
            if other_var == var:
                kill.add(f"{var}{j}")

    GEN.append(gen)
    KILL.append(kill)

# IN and OUT sets
IN = [set() for _ in range(n)]
OUT = [set() for _ in range(n)]

changed = True

while changed:
    changed = False

    for i in range(n):
        if i == 0:
            IN[i] = set()
        else:
            IN[i] = OUT[i-1]

        new_out = GEN[i] | (IN[i] - KILL[i])

        if new_out != OUT[i]:
            OUT[i] = new_out
            changed = True

# Output
print("\nGEN sets:")
for i in range(n):
    print(f"{i+1}:", GEN[i])

print("\nKILL sets:")
for i in range(n):
    print(f"{i+1}:", KILL[i])

print("\nIN sets:")
for i in range(n):
    print(f"{i+1}:", IN[i])

print("\nOUT sets:")
for i in range(n):
    print(f"{i+1}:", OUT[i])