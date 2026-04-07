# FIRST and FOLLOW computation

grammar = {
    'E': ['TR'],
    'R': ['+TR', 'ε'],
    'T': ['FY'],
    'Y': ['*FY', 'ε'],
    'F': ['(E)', 'i']
}

non_terminals = list(grammar.keys())
terminals = ['+', '*', '(', ')', 'i']
start_symbol = 'E'

FIRST = {nt: set() for nt in non_terminals}
FOLLOW = {nt: set() for nt in non_terminals}


def compute_first(symbol):
    if symbol in terminals:
        return {symbol}
    if symbol == 'ε':
        return {'ε'}

    for production in grammar[symbol]:
        for char in production:
            char_first = compute_first(char)
            FIRST[symbol].update(char_first - {'ε'})
            if 'ε' not in char_first:
                break
        else:
            FIRST[symbol].add('ε')
    return FIRST[symbol]


def compute_follow():
    FOLLOW[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for head, productions in grammar.items():
            for prod in productions:
                for i in range(len(prod)):
                    symbol = prod[i]
                    if symbol in non_terminals:
                        next_symbols = prod[i + 1:]
                        if next_symbols:
                            first_next = set()
                            for s in next_symbols:
                                s_first = compute_first(s)
                                first_next.update(s_first - {'ε'})
                                if 'ε' not in s_first:
                                    break
                            else:
                                first_next.add('ε')

                            before = len(FOLLOW[symbol])
                            FOLLOW[symbol].update(first_next - {'ε'})
                            if 'ε' in first_next:
                                FOLLOW[symbol].update(FOLLOW[head])
                            if len(FOLLOW[symbol]) > before:
                                changed = True
                        else:
                            before = len(FOLLOW[symbol])
                            FOLLOW[symbol].update(FOLLOW[head])
                            if len(FOLLOW[symbol]) > before:
                                changed = True


for nt in non_terminals:
    compute_first(nt)

compute_follow()

print("FIRST Sets:")
for nt in non_terminals:
    print(f"FIRST({nt}) = {FIRST[nt]}")

print("\nFOLLOW Sets:")
for nt in non_terminals:
    print(f"FOLLOW({nt}) = {FOLLOW[nt]}")