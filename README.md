VYSHNAVI D

CSE E

RA2311003050282

**1.LEXICAL-ANALYSER:**
# Lexical Analyzer using Python

## Description
This project is a simple lexical analyzer implemented using Python.  
It identifies tokens such as keywords, identifiers, operators, separators, and numbers from the given source code.

## Features
- Identifies keywords
- Identifies identifiers
- Identifies operators
- Identifies separators
- Identifies numbers

## Technologies Used
- Python
- VS Code

## How to Run the Program
1. Open the project folder in VS Code
2. Open `lexical_analyzer.py`
3. Run the file using:
   - Run button ▶️  
   - OR press `Ctrl + F5`
   - OR use terminal:
     ```
     python lexical_analyzer.py
     ```

## Output
The output is displayed in the terminal showing token type and value.

**2.PARSING-TABLE:**
# Parsing Table Construction

## Aim
To construct an LL(1) parsing table for a given grammar.

## Theory
LL(1) parsing table helps in predictive parsing by selecting productions using input symbols.

## Program
Implemented using Python.

## Output
Displays the LL(1) parsing table.

**3.ELIMINATION-OF-AMBIGUITY:**
# Elimination of Ambiguity, Left Recursion and Left Factoring

## Aim
To eliminate ambiguity, left recursion, and perform left factoring in a given grammar.

## Theory
Ambiguous grammars produce multiple parse trees. Left recursion and common prefixes cause problems in top-down parsing. These are removed to make the grammar suitable for parsing.

## Algorithm
1. Identify left recursive productions.
2. Eliminate left recursion.
3. Identify common prefixes.
4. Apply left factoring.

## Program
Implemented using Python.

## Output
Displays the modified grammar after eliminating left recursion and left factoring.

**4.NFA-TO-DFA:**
# NFA to DFA Conversion

## Aim
To convert a given Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA).

## Theory
NFA to DFA conversion is done using the subset construction method where each DFA state represents a set of NFA states.

## Algorithm
1. Start with the initial NFA state.
2. Generate all possible subsets of NFA states.
3. For each subset and input symbol, compute transitions.
4. Mark final states containing NFA final state.

## Program
Implemented using Python.

## Output
The program displays DFA states, transitions, and final states.

**5.FIRST-AND-FOLLOW:**
# FIRST and FOLLOW Computation

## Aim
To compute FIRST and FOLLOW sets for a given context-free grammar.

## Theory
FIRST and FOLLOW sets are used in syntax analysis to construct predictive parsing tables.

## Algorithm
1. Define grammar productions.
2. Compute FIRST for all non-terminals.
3. Compute FOLLOW using FIRST information.
4. Display the sets.

## Program
Implemented using Python.

## Output
Displays FIRST and FOLLOW sets for the grammar.

**6.REGULAR-EXPRESSION-TO-NFA:**
## Regular Expression to NFA

### Aim
To convert a given Regular Expression into a Non-Deterministic
Finite Automaton (NFA).

### Description
This program takes a regular expression as input and constructs
an equivalent NFA.

### Algorithm
1. Read the regular expression
2. Create start state
3. Generate transitions for each symbol
4. Mark final state as accept state

### Language Used
Python

### Output
Displays start state, accept state, and NFA transitions.
