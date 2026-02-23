# Regular Expression to NFA (Simple Version)

class NFA:
    def __init__(self, start, accept, transitions):
        self.start = start
        self.accept = accept
        self.transitions = transitions


def re_to_nfa(regex):
    state = 0
    transitions = []

    start_state = state
    state += 1

    for symbol in regex:
        next_state = state
        state += 1
        transitions.append((start_state, symbol, next_state))
        start_state = next_state

    accept_state = start_state

    return NFA(0, accept_state, transitions)


# Input Regular Expression
regex = input("Enter Regular Expression: ")

nfa = re_to_nfa(regex)

print("\nNFA Representation")
print("Start State:", nfa.start)
print("Accept State:", nfa.accept)
print("\nTransitions:")
for t in nfa.transitions:
    print(f"{t[0]} -- {t[1]} --> {t[2]}")
    # Regular Expression to NFA (Simple Version)

class NFA:
    def __init__(self, start, accept, transitions):
        self.start = start
        self.accept = accept
        self.transitions = transitions


def re_to_nfa(regex):
    state = 0
    transitions = []

    start_state = state
    state += 1

    for symbol in regex:
        next_state = state
        state += 1
        transitions.append((start_state, symbol, next_state))
        start_state = next_state

    accept_state = start_state

    return NFA(0, accept_state, transitions)


# Input Regular Expression
regex = input("Enter Regular Expression: ")

nfa = re_to_nfa(regex)

print("\nNFA Representation")
print("Start State:", nfa.start)
print("Accept State:", nfa.accept)
print("\nTransitions:")
for t in nfa.transitions:
    print(f"{t[0]} -- {t[1]} --> {t[2]}")