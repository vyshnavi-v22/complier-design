# NFA to DFA Conversion using Subset Construction

def nfa_to_dfa(nfa, start_state, final_states):
    dfa = {}
    unmarked_states = [frozenset([start_state])]
    dfa_states = []
    
    while unmarked_states:
        current = unmarked_states.pop(0)
        dfa_states.append(current)
        dfa[current] = {}

        for symbol in nfa:
            next_state = set()
            for state in current:
                if state in nfa[symbol]:
                    next_state.update(nfa[symbol][state])

            next_state = frozenset(next_state)
            dfa[current][symbol] = next_state

            if next_state not in dfa_states and next_state not in unmarked_states:
                unmarked_states.append(next_state)

    dfa_final_states = [state for state in dfa_states if state & final_states]
    return dfa, dfa_states, dfa_final_states


# Example NFA
nfa = {
    'a': {
        0: {0, 1},
        1: {2}
    },
    'b': {
        0: {0},
        1: {1},
        2: {2}
    }
}

start_state = 0
final_states = {2}

dfa, dfa_states, dfa_final_states = nfa_to_dfa(nfa, start_state, final_states)

print("DFA States:")
for state in dfa_states:
    print(state)

print("\nDFA Transitions:")
for state, transitions in dfa.items():
    for symbol, next_state in transitions.items():
        print(f"{state} --{symbol}--> {next_state}")

print("\nDFA Final States:")
for state in dfa_final_states:
    print(state)